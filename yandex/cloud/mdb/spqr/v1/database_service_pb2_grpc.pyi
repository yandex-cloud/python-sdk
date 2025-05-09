"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.mdb.spqr.v1.database_pb2
import yandex.cloud.mdb.spqr.v1.database_service_pb2
import yandex.cloud.operation.operation_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class DatabaseServiceStub:
    """A set of methods for managing SPQR Database resources."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.database_service_pb2.GetDatabaseRequest,
        yandex.cloud.mdb.spqr.v1.database_pb2.Database,
    ]
    """Returns the specified SPQR Database resource.

    To get the list of available SPQR Database resources, make a [List] request.
    """

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.database_service_pb2.ListDatabasesRequest,
        yandex.cloud.mdb.spqr.v1.database_service_pb2.ListDatabasesResponse,
    ]
    """Retrieves the list of SPQR Database resources in the specified cluster."""

    ListAtRevision: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.database_service_pb2.ListDatabasesAtRevisionRequest,
        yandex.cloud.mdb.spqr.v1.database_service_pb2.ListDatabasesResponse,
    ]
    """Retrieves the list of SPQR Database resources in the specified cluster at the specified revision."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.database_service_pb2.CreateDatabaseRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a new SPQR database in the specified cluster."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.database_service_pb2.DeleteDatabaseRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified SPQR database."""

class DatabaseServiceAsyncStub:
    """A set of methods for managing SPQR Database resources."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.database_service_pb2.GetDatabaseRequest,
        yandex.cloud.mdb.spqr.v1.database_pb2.Database,
    ]
    """Returns the specified SPQR Database resource.

    To get the list of available SPQR Database resources, make a [List] request.
    """

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.database_service_pb2.ListDatabasesRequest,
        yandex.cloud.mdb.spqr.v1.database_service_pb2.ListDatabasesResponse,
    ]
    """Retrieves the list of SPQR Database resources in the specified cluster."""

    ListAtRevision: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.database_service_pb2.ListDatabasesAtRevisionRequest,
        yandex.cloud.mdb.spqr.v1.database_service_pb2.ListDatabasesResponse,
    ]
    """Retrieves the list of SPQR Database resources in the specified cluster at the specified revision."""

    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.database_service_pb2.CreateDatabaseRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a new SPQR database in the specified cluster."""

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.database_service_pb2.DeleteDatabaseRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified SPQR database."""

class DatabaseServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing SPQR Database resources."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.mdb.spqr.v1.database_service_pb2.GetDatabaseRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.spqr.v1.database_pb2.Database, collections.abc.Awaitable[yandex.cloud.mdb.spqr.v1.database_pb2.Database]]:
        """Returns the specified SPQR Database resource.

        To get the list of available SPQR Database resources, make a [List] request.
        """

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.mdb.spqr.v1.database_service_pb2.ListDatabasesRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.spqr.v1.database_service_pb2.ListDatabasesResponse, collections.abc.Awaitable[yandex.cloud.mdb.spqr.v1.database_service_pb2.ListDatabasesResponse]]:
        """Retrieves the list of SPQR Database resources in the specified cluster."""

    @abc.abstractmethod
    def ListAtRevision(
        self,
        request: yandex.cloud.mdb.spqr.v1.database_service_pb2.ListDatabasesAtRevisionRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.spqr.v1.database_service_pb2.ListDatabasesResponse, collections.abc.Awaitable[yandex.cloud.mdb.spqr.v1.database_service_pb2.ListDatabasesResponse]]:
        """Retrieves the list of SPQR Database resources in the specified cluster at the specified revision."""

    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.mdb.spqr.v1.database_service_pb2.CreateDatabaseRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates a new SPQR database in the specified cluster."""

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.mdb.spqr.v1.database_service_pb2.DeleteDatabaseRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deletes the specified SPQR database."""

def add_DatabaseServiceServicer_to_server(servicer: DatabaseServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
