from concurrent import futures
from unittest.mock import Mock, patch

import grpc
import pytest

from yandex.cloud.vpc.v1.network_service_pb2 import (
    GetNetworkRequest,
    ListNetworksRequest,
    ListNetworksResponse,
)
from yandex.cloud.vpc.v1.network_service_pb2_grpc import (
    NetworkServiceStub,
    add_NetworkServiceServicer_to_server,
)
from yandexcloud import SDK, RetryPolicy

INSECURE_SERVICE_PORT = "50051"
SERVICE_ADDR = "localhost"


def side_effect_internal(_, context):
    context.set_code(grpc.StatusCode.INTERNAL)


def side_effect_unavailable(_, context):
    context.set_code(grpc.StatusCode.UNAVAILABLE)


class VPCServiceMock:
    def __init__(self, fn):
        self.Get = Mock(side_effect=fn)
        self.Create = Mock()
        self.Update = Mock()
        self.Delete = Mock()
        self.ListSubnets = Mock()
        self.ListSecurityGroups = Mock()
        self.ListRouteTables = Mock()
        self.ListOperations = Mock()
        self.Move = Mock()
        self.List = Mock()


def test_default_retries():
    service = VPCServiceMock(side_effect_unavailable)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server.add_insecure_port("localhost:" + INSECURE_SERVICE_PORT)
    add_NetworkServiceServicer_to_server(service, server)
    server.start()

    sdk = SDK(retry_policy=RetryPolicy())
    network_client = sdk.client(NetworkServiceStub, endpoint=f"localhost:{INSECURE_SERVICE_PORT}", insecure=True)
    try:
        request = GetNetworkRequest(network_id="asdf")
        network_client.Get(request)
    except grpc.RpcError:
        assert service.Get.call_count == 4


def test_custom_retries():
    service = VPCServiceMock(side_effect_internal)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server.add_insecure_port("localhost:" + INSECURE_SERVICE_PORT)
    add_NetworkServiceServicer_to_server(service, server)
    server.start()

    sdk = SDK(retry_policy=RetryPolicy(status_codes=(grpc.StatusCode.INTERNAL,), max_attempts=4))
    network_client = sdk.client(NetworkServiceStub, endpoint=f"localhost:{INSECURE_SERVICE_PORT}", insecure=True)
    try:
        request = GetNetworkRequest(network_id="asdf")
        network_client.Get(request)
    except grpc.RpcError:
        assert service.Get.call_count == 4


def test_no_retries():
    service = VPCServiceMock(side_effect_internal)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server.add_insecure_port("localhost:" + INSECURE_SERVICE_PORT)
    add_NetworkServiceServicer_to_server(service, server)
    server.start()

    sdk = SDK()
    network_client = sdk.client(NetworkServiceStub, endpoint=f"localhost:{INSECURE_SERVICE_PORT}", insecure=True)
    try:
        request = GetNetworkRequest(network_id="asdf")
        network_client.Get(request)
    except grpc.RpcError:
        assert service.Get.call_count == 1
