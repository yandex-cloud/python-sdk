import inspect

import grpc

from yandexcloud import _channels, _helpers, _operation_waiter
from yandexcloud._backoff import backoff_exponential_with_jitter
from yandexcloud._retry_interceptor import RetryInterceptor
from yandexcloud._wrappers import Wrappers


class SDK(object):
    def __init__(self, interceptor=None, user_agent=None, **kwargs):
        """
        API entry-point object.

        :param interceptor: GRPC interceptor to be used instead of default RetryInterceptor
        :type interceptor: Union[
            UnaryUnaryClientInterceptor,
            UnaryStreamClientInterceptor,
            StreamUnaryClientInterceptor,
            StreamStreamClientInterceptor
        ]
        :param user_agent: String to prepend User-Agent metadata header for all GRPC requests made via SDK object
        :type user_agent: Optional[str]
        """
        self._channels = _channels.Channels(client_user_agent=user_agent, **kwargs)
        if interceptor is None:
            interceptor = RetryInterceptor(
                max_retry_count=5,
                per_call_timeout=30,
                back_off_func=backoff_exponential_with_jitter(1, 30),
            )
        self._default_interceptor = interceptor
        self.helpers = _helpers.Helpers(self)
        self.wrappers = Wrappers(self)

    def set_interceptor(self, interceptor):
        self._default_interceptor = interceptor

    def client(self, stub_ctor, interceptor=None):
        service = _service_for_ctor(stub_ctor)
        channel = self._channels.channel(service)
        if interceptor is not None:
            channel = grpc.intercept_channel(channel, interceptor)
        elif self._default_interceptor is not None:
            channel = grpc.intercept_channel(channel, self._default_interceptor)
        return stub_ctor(channel)

    def waiter(self, operation_id, timeout=None):
        return _operation_waiter.operation_waiter(self, operation_id, timeout)

    def wait_operation_and_get_result(self, operation, response_type=None, meta_type=None, timeout=None, logger=None):
        return _operation_waiter.get_operation_result(self, operation, response_type, meta_type, timeout, logger)

    def create_operation_and_get_result(
        self,
        request,
        service,
        method_name,
        response_type=None,
        meta_type=None,
        timeout=None,
        logger=None,
    ):
        operation = getattr(self.client(service), method_name)(request)
        return self.wait_operation_and_get_result(
            operation,
            response_type=response_type,
            meta_type=meta_type,
            timeout=timeout,
            logger=logger,
        )


def _service_for_ctor(stub_ctor):
    m = inspect.getmodule(stub_ctor)
    name = m.__name__
    if not name.startswith("yandex.cloud"):
        raise RuntimeError("Not a yandex.cloud service {}".format(stub_ctor))

    for k, v in _supported_modules:
        if name.startswith(k):
            return v

    raise RuntimeError("Unknown service {}".format(stub_ctor))


_supported_modules = [
    ("yandex.cloud.ai.stt", "ai-stt"),
    ("yandex.cloud.ai.translate", "ai-translate"),
    ("yandex.cloud.ai.tts", "ai-speechkit"),
    ("yandex.cloud.ai.vision", "ai-vision"),
    ("yandex.cloud.apploadbalancer", "alb"),
    ("yandex.cloud.billing", "billing"),
    ("yandex.cloud.cdn", "cdn"),
    ("yandex.cloud.compute", "compute"),
    ("yandex.cloud.containerregistry", "container-registry"),
    ("yandex.cloud.dataproc.manager", "dataproc-manager"),
    ("yandex.cloud.dataproc", "dataproc"),
    ("yandex.cloud.datatransfer", "datatransfer"),
    ("yandex.cloud.dns", "dns"),
    ("yandex.cloud.endpoint", "endpoint"),
    ("yandex.cloud.iam", "iam"),
    ("yandex.cloud.iot.devices", "iot-devices"),
    ("yandex.cloud.k8s", "managed-kubernetes"),
    ("yandex.cloud.kms.v1.symmetric_crypto_service", "kms-crypto"),
    ("yandex.cloud.kms", "kms"),
    ("yandex.cloud.loadbalancer", "load-balancer"),
    ("yandex.cloud.lockbox.v1.payload_service", "lockbox-payload"),
    ("yandex.cloud.lockbox", "lockbox"),
    ("yandex.cloud.logging.v1.log_ingestion_service", "log-ingestion"),
    ("yandex.cloud.logging.v1.log_reading_service", "log-reading"),
    ("yandex.cloud.logging", "logging"),
    ("yandex.cloud.marketplace", "marketplace"),
    ("yandex.cloud.mdb.clickhouse", "managed-clickhouse"),
    ("yandex.cloud.mdb.kafka", "managed-kafka"),
    ("yandex.cloud.mdb.mongodb", "managed-mongodb"),
    ("yandex.cloud.mdb.mysql", "managed-mysql"),
    ("yandex.cloud.mdb.postgresql", "managed-postgresql"),
    ("yandex.cloud.mdb.redis", "managed-redis"),
    ("yandex.cloud.mdb.sqlserver", "managed-sqlserver"),
    ("yandex.cloud.mdb.elasticsearch", "managed-elasticsearch"),
    ("yandex.cloud.operation", "operation"),
    ("yandex.cloud.organizationmanager", "organization-manager"),
    ("yandex.cloud.resourcemanager", "resource-manager"),
    ("yandex.cloud.serverless.apigateway", "serverless-apigateway"),
    ("yandex.cloud.serverless.containers", "serverless-containers"),
    ("yandex.cloud.serverless.functions", "serverless-functions"),
    ("yandex.cloud.serverless.triggers", "serverless-triggers"),
    ("yandex.cloud.vpc", "vpc"),
    ("yandex.cloud.ydb", "ydb"),
]
