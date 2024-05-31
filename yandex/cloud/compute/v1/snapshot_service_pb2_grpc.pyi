"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.access.access_pb2
import yandex.cloud.compute.v1.snapshot_pb2
import yandex.cloud.compute.v1.snapshot_service_pb2
import yandex.cloud.operation.operation_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class SnapshotServiceStub:
    """A set of methods for managing Snapshot resources."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.snapshot_service_pb2.GetSnapshotRequest,
        yandex.cloud.compute.v1.snapshot_pb2.Snapshot,
    ]
    """Returns the specified Snapshot resource.

    To get the list of available Snapshot resources, make a [List] request.
    """

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.snapshot_service_pb2.ListSnapshotsRequest,
        yandex.cloud.compute.v1.snapshot_service_pb2.ListSnapshotsResponse,
    ]
    """Retrieves the list of Snapshot resources in the specified folder."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.snapshot_service_pb2.CreateSnapshotRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a snapshot of the specified disk."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.snapshot_service_pb2.UpdateSnapshotRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified snapshot.

    Values of omitted parameters are not changed.
    """

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.snapshot_service_pb2.DeleteSnapshotRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified snapshot.

    Deleting a snapshot removes its data permanently and is irreversible.
    """

    ListOperations: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.snapshot_service_pb2.ListSnapshotOperationsRequest,
        yandex.cloud.compute.v1.snapshot_service_pb2.ListSnapshotOperationsResponse,
    ]
    """Lists operations for the specified snapshot."""

    ListAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        yandex.cloud.access.access_pb2.ListAccessBindingsResponse,
    ]
    """access

    Lists access bindings for the snapshot.
    """

    SetAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Sets access bindings for the snapshot."""

    UpdateAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates access bindings for the snapshot."""

class SnapshotServiceAsyncStub:
    """A set of methods for managing Snapshot resources."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.snapshot_service_pb2.GetSnapshotRequest,
        yandex.cloud.compute.v1.snapshot_pb2.Snapshot,
    ]
    """Returns the specified Snapshot resource.

    To get the list of available Snapshot resources, make a [List] request.
    """

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.snapshot_service_pb2.ListSnapshotsRequest,
        yandex.cloud.compute.v1.snapshot_service_pb2.ListSnapshotsResponse,
    ]
    """Retrieves the list of Snapshot resources in the specified folder."""

    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.snapshot_service_pb2.CreateSnapshotRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a snapshot of the specified disk."""

    Update: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.snapshot_service_pb2.UpdateSnapshotRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified snapshot.

    Values of omitted parameters are not changed.
    """

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.snapshot_service_pb2.DeleteSnapshotRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified snapshot.

    Deleting a snapshot removes its data permanently and is irreversible.
    """

    ListOperations: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.snapshot_service_pb2.ListSnapshotOperationsRequest,
        yandex.cloud.compute.v1.snapshot_service_pb2.ListSnapshotOperationsResponse,
    ]
    """Lists operations for the specified snapshot."""

    ListAccessBindings: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        yandex.cloud.access.access_pb2.ListAccessBindingsResponse,
    ]
    """access

    Lists access bindings for the snapshot.
    """

    SetAccessBindings: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Sets access bindings for the snapshot."""

    UpdateAccessBindings: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates access bindings for the snapshot."""

class SnapshotServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing Snapshot resources."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.compute.v1.snapshot_service_pb2.GetSnapshotRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.compute.v1.snapshot_pb2.Snapshot, collections.abc.Awaitable[yandex.cloud.compute.v1.snapshot_pb2.Snapshot]]:
        """Returns the specified Snapshot resource.

        To get the list of available Snapshot resources, make a [List] request.
        """

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.compute.v1.snapshot_service_pb2.ListSnapshotsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.compute.v1.snapshot_service_pb2.ListSnapshotsResponse, collections.abc.Awaitable[yandex.cloud.compute.v1.snapshot_service_pb2.ListSnapshotsResponse]]:
        """Retrieves the list of Snapshot resources in the specified folder."""

    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.compute.v1.snapshot_service_pb2.CreateSnapshotRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates a snapshot of the specified disk."""

    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.compute.v1.snapshot_service_pb2.UpdateSnapshotRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates the specified snapshot.

        Values of omitted parameters are not changed.
        """

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.compute.v1.snapshot_service_pb2.DeleteSnapshotRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deletes the specified snapshot.

        Deleting a snapshot removes its data permanently and is irreversible.
        """

    @abc.abstractmethod
    def ListOperations(
        self,
        request: yandex.cloud.compute.v1.snapshot_service_pb2.ListSnapshotOperationsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.compute.v1.snapshot_service_pb2.ListSnapshotOperationsResponse, collections.abc.Awaitable[yandex.cloud.compute.v1.snapshot_service_pb2.ListSnapshotOperationsResponse]]:
        """Lists operations for the specified snapshot."""

    @abc.abstractmethod
    def ListAccessBindings(
        self,
        request: yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.access.access_pb2.ListAccessBindingsResponse, collections.abc.Awaitable[yandex.cloud.access.access_pb2.ListAccessBindingsResponse]]:
        """access

        Lists access bindings for the snapshot.
        """

    @abc.abstractmethod
    def SetAccessBindings(
        self,
        request: yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Sets access bindings for the snapshot."""

    @abc.abstractmethod
    def UpdateAccessBindings(
        self,
        request: yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates access bindings for the snapshot."""

def add_SnapshotServiceServicer_to_server(servicer: SnapshotServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
