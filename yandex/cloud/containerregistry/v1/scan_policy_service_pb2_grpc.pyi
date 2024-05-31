"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.containerregistry.v1.scan_policy_pb2
import yandex.cloud.containerregistry.v1.scan_policy_service_pb2
import yandex.cloud.operation.operation_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class ScanPolicyServiceStub:
    """A set of methods for managing scan policy resources."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.scan_policy_service_pb2.GetScanPolicyRequest,
        yandex.cloud.containerregistry.v1.scan_policy_pb2.ScanPolicy,
    ]
    """Returns the specified scan policy."""

    GetByRegistry: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.scan_policy_service_pb2.GetScanPolicyByRegistryRequest,
        yandex.cloud.containerregistry.v1.scan_policy_pb2.ScanPolicy,
    ]
    """Returns scan policy for the registry if any exists."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.scan_policy_service_pb2.CreateScanPolicyRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a scan policy for the specified registry."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.scan_policy_service_pb2.UpdateScanPolicyRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified scan policy."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.scan_policy_service_pb2.DeleteScanPolicyRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified scan policy."""

class ScanPolicyServiceAsyncStub:
    """A set of methods for managing scan policy resources."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.scan_policy_service_pb2.GetScanPolicyRequest,
        yandex.cloud.containerregistry.v1.scan_policy_pb2.ScanPolicy,
    ]
    """Returns the specified scan policy."""

    GetByRegistry: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.scan_policy_service_pb2.GetScanPolicyByRegistryRequest,
        yandex.cloud.containerregistry.v1.scan_policy_pb2.ScanPolicy,
    ]
    """Returns scan policy for the registry if any exists."""

    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.scan_policy_service_pb2.CreateScanPolicyRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a scan policy for the specified registry."""

    Update: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.scan_policy_service_pb2.UpdateScanPolicyRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified scan policy."""

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.scan_policy_service_pb2.DeleteScanPolicyRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified scan policy."""

class ScanPolicyServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing scan policy resources."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.containerregistry.v1.scan_policy_service_pb2.GetScanPolicyRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.containerregistry.v1.scan_policy_pb2.ScanPolicy, collections.abc.Awaitable[yandex.cloud.containerregistry.v1.scan_policy_pb2.ScanPolicy]]:
        """Returns the specified scan policy."""

    @abc.abstractmethod
    def GetByRegistry(
        self,
        request: yandex.cloud.containerregistry.v1.scan_policy_service_pb2.GetScanPolicyByRegistryRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.containerregistry.v1.scan_policy_pb2.ScanPolicy, collections.abc.Awaitable[yandex.cloud.containerregistry.v1.scan_policy_pb2.ScanPolicy]]:
        """Returns scan policy for the registry if any exists."""

    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.containerregistry.v1.scan_policy_service_pb2.CreateScanPolicyRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates a scan policy for the specified registry."""

    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.containerregistry.v1.scan_policy_service_pb2.UpdateScanPolicyRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates the specified scan policy."""

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.containerregistry.v1.scan_policy_service_pb2.DeleteScanPolicyRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deletes the specified scan policy."""

def add_ScanPolicyServiceServicer_to_server(servicer: ScanPolicyServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
