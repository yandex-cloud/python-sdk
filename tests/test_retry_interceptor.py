import pytest
import grpc
import time
import uuid

from threading import Event
from concurrent import futures

import yandex.cloud.compute.v1.zone_service_pb2_grpc as zone_service_pb2_grpc
import yandex.cloud.compute.v1.zone_service_pb2 as zone_service_pb2
import yandex.cloud.compute.v1.zone_pb2 as zone_pb2

from yandexcloud._retry_interceptor import RetryInterceptor
from yandexcloud._backoff import default_backoff, backoff_linear_with_jitter

_DEFAULT_SERVICE_PORT = "50051"
_SERVICE_ADDR = "localhost:" + _DEFAULT_SERVICE_PORT
_DEFAULT_ZONE = zone_pb2.Zone()


class ZoneServiceMock(object):
    def __init__(self, handler):
        self.__handler = handler

    def Get(self, request, context):
        return self.__handler(context)

    def List(self, request, context):
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        return zone_service_pb2.ListZonesResponse()


def _grpc_server(handler):
    service = ZoneServiceMock(handler)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server.add_insecure_port("[::]:" + _DEFAULT_SERVICE_PORT)
    zone_service_pb2_grpc.add_ZoneServiceServicer_to_server(service, server)
    server.start()
    assert _is_grpc_endpoint_ready(60)
    return server


def _is_grpc_endpoint_ready(timeout):
    def check_endpoint_ready():
        channel = grpc.insecure_channel(_SERVICE_ADDR)
        client = zone_service_pb2_grpc.ZoneServiceStub(channel)

        try:
            client.List(zone_service_pb2.ListZonesRequest(), timeout=1)
        except grpc.RpcError as e:
            return e.code() not in [grpc.StatusCode.UNAVAILABLE, grpc.StatusCode.DEADLINE_EXCEEDED]

        return True

    deadline = time.monotonic() + timeout

    while time.monotonic() <= deadline:
        if check_endpoint_ready():
            return True

    return False


class _FailFirstAttempts:
    def __init__(self, fail_attempts):
        self.__fail_attempts = fail_attempts

    def handler(self, context):
        if self.__fail_attempts > 0:
            self.__fail_attempts -= 1
            context.set_code(grpc.StatusCode.UNAVAILABLE)

        return _DEFAULT_ZONE

    def reset(self, fail_attempts):
        self.__fail_attempts = fail_attempts


def test_five_retries():
    service = _FailFirstAttempts(5)
    server = _grpc_server(service.handler)

    with grpc.insecure_channel(_SERVICE_ADDR) as channel:
        for max_retry_count in range(4):
            interceptor = RetryInterceptor(max_retry_count=max_retry_count)
            ch = grpc.intercept_channel(channel, interceptor)
            client = zone_service_pb2_grpc.ZoneServiceStub(ch)

            with pytest.raises(grpc.RpcError) as e:
                client.Get(zone_service_pb2.GetZoneRequest(zone_id="id"))

            assert e.value.code() == grpc.StatusCode.UNAVAILABLE
            service.reset(5)

        interceptor = RetryInterceptor(max_retry_count=5)
        ch = grpc.intercept_channel(channel, interceptor)
        client = zone_service_pb2_grpc.ZoneServiceStub(ch)
        res = client.Get(zone_service_pb2.GetZoneRequest(zone_id="id"))

        assert res == _DEFAULT_ZONE
        
    server.stop(0)


class _RetriableCodes:
    def __init__(self, retriable_codes):
        self.__retriable_codes = retriable_codes
        self.__get_count = 0

    def handler(self, context):
        if self.__get_count < len(self.__retriable_codes):
            context.set_code(self.__retriable_codes[self.__get_count])

        self.__get_count += 1
        return _DEFAULT_ZONE

    def reset_state(self):
        self.__get_count = 0


def test_retriable_codes():
    retriable_codes = [grpc.StatusCode.RESOURCE_EXHAUSTED,
                       grpc.StatusCode.UNAVAILABLE,
                       grpc.StatusCode.DATA_LOSS]

    service = _RetriableCodes(retriable_codes)
    server = _grpc_server(service.handler)

    with grpc.insecure_channel(_SERVICE_ADDR) as channel:
        for retry_qty in range(len(retriable_codes)):
            interceptor = RetryInterceptor(max_retry_count=retry_qty, retriable_codes=retriable_codes)
            ch = grpc.intercept_channel(channel, interceptor)
            client = zone_service_pb2_grpc.ZoneServiceStub(ch)

            with pytest.raises(grpc.RpcError) as e:
                client.Get(zone_service_pb2.GetZoneRequest(zone_id="id"))

            assert e.value.code() == retriable_codes[retry_qty]
            service.reset_state()

        interceptor = RetryInterceptor(max_retry_count=len(retriable_codes), retriable_codes=retriable_codes)
        ch = grpc.intercept_channel(channel, interceptor)
        client = zone_service_pb2_grpc.ZoneServiceStub(ch)
        assert client.Get(zone_service_pb2.GetZoneRequest(zone_id="id")) == _DEFAULT_ZONE

    server.stop(0)


class _AlwaysUnavailable:
    def __init__(self):
        self.__get_count = 0
        self.__t_checker = None
        self.__error = False

    @property
    def error(self):
        return self.__error

    def handler(self, context):
        if self.__t_checker and not self.__t_checker():
            self.__error = True

        self.__get_count += 1

        if self.__get_count == 100:
            pass

        context.set_code(grpc.StatusCode.UNAVAILABLE)
        return _DEFAULT_ZONE


@pytest.mark.parametrize("backoff", [None, default_backoff(), backoff_linear_with_jitter(0.05, 0.1)])
def test_infinite_retries_deadline_and_backoff(backoff):
    service = _AlwaysUnavailable()
    server = _grpc_server(service.handler)

    with grpc.insecure_channel(_SERVICE_ADDR) as channel:
        interceptor = RetryInterceptor(max_retry_count=-1, retriable_codes=[grpc.StatusCode.UNAVAILABLE],
                                       add_retry_count_to_header=True, back_off_func=backoff)

        ch = grpc.intercept_channel(channel, interceptor)
        client = zone_service_pb2_grpc.ZoneServiceStub(ch)

        with pytest.raises(grpc.RpcError) as e:
            client.Get(zone_service_pb2.GetZoneRequest(zone_id="id"), timeout=5)

        assert e.value.code() == grpc.StatusCode.DEADLINE_EXCEEDED

    server.stop(0)


class _NeverReturnsInTime:
    def __init__(self, shutdown):
        self.__shutdown = shutdown

    def handler(self, context):
        time_remaining = context.time_remaining()

        # using hack here, since deadline is never None. 31557600 ~= one year in seconds
        if time_remaining < 31557600.:
            self.__shutdown.wait()

        context.set_code(grpc.StatusCode.UNAVAILABLE)
        return _DEFAULT_ZONE


def test_per_call_timeout():
    shutdown = Event()
    service = _NeverReturnsInTime(shutdown)
    server = _grpc_server(service.handler)

    with grpc.insecure_channel(_SERVICE_ADDR) as channel:
        interceptor = RetryInterceptor(max_retry_count=10, retriable_codes=[grpc.StatusCode.UNAVAILABLE],
                                       per_call_timeout=1, add_retry_count_to_header=True)

        ch = grpc.intercept_channel(channel, interceptor)
        client = zone_service_pb2_grpc.ZoneServiceStub(ch)

        with pytest.raises(grpc.RpcError) as e:
            client.Get(zone_service_pb2.GetZoneRequest(zone_id="id"))

        assert e.value.code() == grpc.StatusCode.DEADLINE_EXCEEDED

    shutdown.set()
    server.stop(1)


class _HeaderTokenAndRetryCount:
    def __init__(self):
        self.__query_count = 0
        self.__token = None
        self.__token_error = False
        self.__header_error = False

    @property
    def error(self):
        return self.__header_error or self.__token_error

    def handler(self, context):
        metadata = context.invocation_metadata()

        if metadata is not None:
            token = [v[1] for v in metadata if v[0] == "idempotency-key"]

            if len(token) != 1:
                self.__token_error = True
            else:
                # store token on first call, on consequent calls, check that token didn't change
                if self.__query_count == 0:
                    self.__token = token[0]
                else:
                    if self.__token != token[0]:
                        self.__token_error = True

            if self.__query_count > 0:
                retry_meta = [v[1] for v in metadata if v[0] == "x-retry-attempt"]

                if len(retry_meta) != 1 or retry_meta[0] != str(self.__query_count):
                    self.__header_error = True
        else:
            self.__token_error = True
            self.__header_error = True

        self.__query_count += 1

        context.set_code(grpc.StatusCode.UNAVAILABLE)
        return _DEFAULT_ZONE


def test_header_token_and_retry_count():
    service = _HeaderTokenAndRetryCount()
    server = _grpc_server(service.handler)

    with grpc.insecure_channel(_SERVICE_ADDR) as channel:
        interceptor = RetryInterceptor(max_retry_count=100, retriable_codes=[grpc.StatusCode.UNAVAILABLE],
                                       add_retry_count_to_header=True)
        ch = grpc.intercept_channel(channel, interceptor)
        client = zone_service_pb2_grpc.ZoneServiceStub(ch)

        with pytest.raises(grpc.RpcError) as e:
            client.Get(zone_service_pb2.GetZoneRequest(zone_id="id"))

        assert e.value.code() == grpc.StatusCode.UNAVAILABLE

    assert not service.error
    server.stop(0)


class _TokenUnchanged:
    def __init__(self, token):
        self.__token = token
        self.__token_changed = False

    @property
    def token_changed(self):
        return self.__token_changed

    def handler(self, context):
        metadata = context.invocation_metadata()

        if metadata is not None:
            token = [v[1] for v in metadata if v[0] == "idempotency-key"]

            if len(token) != 1 or token[0] != self.__token:
                self.__token_changed = True
        else:
            self.__token_changed = True

        context.set_code(grpc.StatusCode.UNAVAILABLE)
        return _DEFAULT_ZONE


def test_idempotency_token_not_changed():
    token = str(uuid.uuid4())
    service = _TokenUnchanged(token)
    server = _grpc_server(service.handler)

    with grpc.insecure_channel(_SERVICE_ADDR) as channel:
        interceptor = RetryInterceptor(max_retry_count=100, retriable_codes=[grpc.StatusCode.UNAVAILABLE],
                                       add_retry_count_to_header=True)
        ch = grpc.intercept_channel(channel, interceptor)
        client = zone_service_pb2_grpc.ZoneServiceStub(ch)

        with pytest.raises(grpc.RpcError) as e:
            client.Get(zone_service_pb2.GetZoneRequest(zone_id="id"), metadata=[("idempotency-key", token)])

        assert e.value.code() == grpc.StatusCode.UNAVAILABLE

    assert not service.token_changed
    server.stop(0)
