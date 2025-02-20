from concurrent import futures
from unittest.mock import Mock, patch

import grpc
import pytest

from yandex.cloud.vpc.v1.network_pb2 import Network
from yandex.cloud.vpc.v1.network_service_pb2 import GetNetworkRequest
from yandex.cloud.vpc.v1.network_service_pb2_grpc import (
    NetworkServiceStub,
    add_NetworkServiceServicer_to_server,
)
from yandexcloud import SDK, RetryPolicy
from yandexcloud._channels import Channels

INSECURE_SERVICE_PORT = "50051"
SERVICE_ADDR = "localhost"


def side_effect_internal(_, context):
    context.set_code(grpc.StatusCode.INTERNAL)


def side_effect_unavailable(_, context):
    context.set_code(grpc.StatusCode.UNAVAILABLE)


class VPCServiceMock:
    def __init__(self, fn):
        self.Get = Mock(return_value=Network(id="12342314"))
        self.Create = Mock()
        self.Update = Mock()
        self.Delete = Mock()
        self.ListSubnets = Mock()
        self.ListSecurityGroups = Mock()
        self.ListRouteTables = Mock()
        self.ListOperations = Mock()
        self.Move = Mock()
        self.List = Mock()


@pytest.fixture
def mock_channel():
    with patch.multiple(
        Channels,
        _get_creds=lambda self, endpoint: grpc.local_channel_credentials(),
        _get_endpoints=lambda self: {
            "vpc": SERVICE_ADDR + ":" + INSECURE_SERVICE_PORT,
            "iam": SERVICE_ADDR + ":" + INSECURE_SERVICE_PORT,
        },
    ) as channel_patch:
        yield channel_patch


def grpc_server(side_effect):
    service = VPCServiceMock(side_effect)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server.add_insecure_port("localhost:" + INSECURE_SERVICE_PORT)
    add_NetworkServiceServicer_to_server(service, server)
    server.start()
    return server, service


def test_default_retries(mock_channel):
    server, service = grpc_server(side_effect_unavailable)

    sdk = SDK(
        retry_policy=RetryPolicy(),
        endpoint=f"localhost:{INSECURE_SERVICE_PORT}",
        endpoints={
            "vpc": SERVICE_ADDR + ":" + INSECURE_SERVICE_PORT,
            "iam": SERVICE_ADDR + ":" + INSECURE_SERVICE_PORT,
        },
    )
    network_client = sdk.client(NetworkServiceStub, insecure=True)
    try:
        request = GetNetworkRequest(network_id="asdf")
        network_client.Get(request)
    except grpc.RpcError:
        assert service.Get.call_count == 4

    server.stop(0)


def test_custom_retries(mock_channel):
    server, service = grpc_server(side_effect_internal)

    sdk = SDK(
        retry_policy=RetryPolicy(status_codes=(grpc.StatusCode.INTERNAL,), max_attempts=4),
        endpoint=f"localhost:{INSECURE_SERVICE_PORT}",
        endpoints={
            "vpc": SERVICE_ADDR + ":" + INSECURE_SERVICE_PORT,
            "iam": SERVICE_ADDR + ":" + INSECURE_SERVICE_PORT,
        },
    )
    network_client = sdk.client(NetworkServiceStub, insecure=True)
    try:
        request = GetNetworkRequest(network_id="asdf")
        network_client.Get(request)
    except grpc.RpcError:
        assert service.Get.call_count == 4

    server.stop(0)


def test_no_retries(mock_channel):
    server, service = grpc_server(side_effect_internal)

    sdk = SDK(
        endpoint=f"localhost:{INSECURE_SERVICE_PORT}",
        endpoints={
            "vpc": SERVICE_ADDR + ":" + INSECURE_SERVICE_PORT,
            "iam": SERVICE_ADDR + ":" + INSECURE_SERVICE_PORT,
        },
    )
    network_client = sdk.client(NetworkServiceStub, insecure=True)
    try:
        request = GetNetworkRequest(network_id="asdf")
        network_client.Get(request)
    except grpc.RpcError:
        assert service.Get.call_count == 1

    server.stop(0)
