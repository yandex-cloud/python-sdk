import time
from unittest.mock import MagicMock, Mock, patch

import grpc
import pytest

import yandexcloud._operation_waiter as waiter_module
from yandex.cloud.dataproc.v1.cluster_pb2 import Cluster
from yandex.cloud.dataproc.v1.cluster_service_pb2 import (
    CreateClusterMetadata,
    CreateClusterRequest,
)
from yandex.cloud.dataproc.v1.cluster_service_pb2_grpc import ClusterServiceStub
from yandex.cloud.operation.operation_pb2 import Operation
from yandex.cloud.operation.operation_service_pb2_grpc import OperationServiceStub
from yandexcloud import SDK
from yandexcloud._wrappers.dataproc import Dataproc, DataprocRetryInterceptor


class MockOperationService:
    def __init__(self, fail_attempts=0, fail_code=grpc.StatusCode.CANCELLED):
        self.fail_attempts = fail_attempts
        self.fail_code = fail_code
        self.call_count = 0

    def Get(self, request):
        self.call_count += 1
        if self.call_count <= self.fail_attempts:
            error = grpc.RpcError()
            error._state = Mock()
            error._state.code = self.fail_code
            error.code = lambda: self.fail_code
            raise error
        return Operation(id="test-op", done=True)


class MockClusterService:
    def Create(self, request):
        return Operation(id="test-cluster-op", done=False)


class MockSDK:
    def __init__(self):
        self.client_calls = []

    def client(self, service_class, interceptor=None):
        self.client_calls.append((service_class, interceptor))
        if service_class == ClusterServiceStub:
            return MockClusterService()
        elif service_class == OperationServiceStub:
            return MockOperationService()

    def create_operation_and_get_result(self, request, service, method_name, response_type, meta_type):
        operation = Operation(id="test-op", done=False)
        waiter = waiter_module.operation_waiter(self, operation.id, None)
        for _ in waiter:
            time.sleep(0.01)
        return MockOperationResult()


class MockOperationResult:
    def __init__(self):
        self.response = Mock()
        self.response.id = "test-cluster-id"


@pytest.fixture
def mock_sdk():
    return MockSDK()


def test_dataproc_custom_interceptor_max_attempts(mock_sdk):
    dataproc = Dataproc(sdk=mock_sdk, enable_custom_interceptor=True)

    mock_operation_service = MockOperationService(fail_attempts=51, fail_code=grpc.StatusCode.CANCELLED)

    with patch.object(waiter_module, "operation_waiter") as mock_waiter_fn:
        mock_waiter = Mock()
        mock_waiter.__iter__ = Mock(return_value=iter([]))
        mock_waiter.operation = Operation(id="test", done=True)
        mock_waiter_fn.return_value = mock_waiter

        with patch.object(mock_sdk, "client") as mock_client:
            mock_client.return_value = mock_operation_service

            with pytest.raises(grpc.RpcError) as exc_info:
                dataproc.create_cluster(
                    folder_id="test-folder",
                    cluster_name="test-cluster",
                    subnet_id="test-subnet",
                    service_account_id="test-sa",
                    ssh_public_keys="test-ssh-key",
                )

            assert exc_info.value.code() == grpc.StatusCode.CANCELLED
            assert mock_operation_service.call_count <= 50


def test_dataproc_interceptor_inheritance():
    interceptor = DataprocRetryInterceptor(
        max_retry_count=10, retriable_codes=(grpc.StatusCode.CANCELLED, grpc.StatusCode.UNAVAILABLE)
    )

    assert interceptor._RetryInterceptor__is_retriable(grpc.StatusCode.CANCELLED) == True

    assert interceptor._RetryInterceptor__is_retriable(grpc.StatusCode.UNAVAILABLE) == True

    assert interceptor._RetryInterceptor__is_retriable(grpc.StatusCode.PERMISSION_DENIED) == False


def test_dataproc_monkey_patch_restoration():
    mock_sdk = Mock()
    original_waiter = waiter_module.operation_waiter

    dataproc = Dataproc(sdk=mock_sdk, enable_custom_interceptor=True)

    with patch.object(mock_sdk, "create_operation_and_get_result") as mock_create:
        mock_create.return_value = MockOperationResult()

        result = dataproc.delete_cluster(cluster_id="test-cluster-id")

        assert result is not None

    assert waiter_module.operation_waiter == original_waiter


def test_dataproc_all_methods_use_wrapper(mock_sdk):
    dataproc = Dataproc(sdk=mock_sdk, enable_custom_interceptor=True)

    methods_to_test = [
        (
            "create_cluster",
            {
                "folder_id": "test",
                "cluster_name": "test",
                "subnet_id": "test",
                "service_account_id": "test",
                "ssh_public_keys": "test-ssh-key",
            },
        ),
        ("delete_cluster", {"cluster_id": "test"}),
        ("stop_cluster", {"cluster_id": "test"}),
        ("start_cluster", {"cluster_id": "test"}),
    ]

    with patch.object(dataproc, "_with_dataproc_waiter") as mock_wrapper:
        mock_wrapper.return_value = MockOperationResult()

        for method_name, kwargs in methods_to_test:
            method = getattr(dataproc, method_name)
            method(**kwargs)

            assert mock_wrapper.called
            mock_wrapper.reset_mock()
