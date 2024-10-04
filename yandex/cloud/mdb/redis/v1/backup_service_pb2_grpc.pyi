"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.mdb.redis.v1.backup_pb2
import yandex.cloud.mdb.redis.v1.backup_service_pb2
import yandex.cloud.operation.operation_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class BackupServiceStub:
    """A set of methods for managing Redis backups."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.redis.v1.backup_service_pb2.GetBackupRequest,
        yandex.cloud.mdb.redis.v1.backup_pb2.Backup,
    ]
    """Returns the specified Redis backup.

    To get the list of available Redis backups, make a [List] request.
    """

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.redis.v1.backup_service_pb2.ListBackupsRequest,
        yandex.cloud.mdb.redis.v1.backup_service_pb2.ListBackupsResponse,
    ]
    """Retrieves the list of Redis backups available for the specified folder."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.redis.v1.backup_service_pb2.DeleteBackupRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Returns the list of available backups for the specified Redis cluster."""

class BackupServiceAsyncStub:
    """A set of methods for managing Redis backups."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.redis.v1.backup_service_pb2.GetBackupRequest,
        yandex.cloud.mdb.redis.v1.backup_pb2.Backup,
    ]
    """Returns the specified Redis backup.

    To get the list of available Redis backups, make a [List] request.
    """

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.redis.v1.backup_service_pb2.ListBackupsRequest,
        yandex.cloud.mdb.redis.v1.backup_service_pb2.ListBackupsResponse,
    ]
    """Retrieves the list of Redis backups available for the specified folder."""

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.redis.v1.backup_service_pb2.DeleteBackupRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Returns the list of available backups for the specified Redis cluster."""

class BackupServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing Redis backups."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.mdb.redis.v1.backup_service_pb2.GetBackupRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.redis.v1.backup_pb2.Backup, collections.abc.Awaitable[yandex.cloud.mdb.redis.v1.backup_pb2.Backup]]:
        """Returns the specified Redis backup.

        To get the list of available Redis backups, make a [List] request.
        """

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.mdb.redis.v1.backup_service_pb2.ListBackupsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.redis.v1.backup_service_pb2.ListBackupsResponse, collections.abc.Awaitable[yandex.cloud.mdb.redis.v1.backup_service_pb2.ListBackupsResponse]]:
        """Retrieves the list of Redis backups available for the specified folder."""

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.mdb.redis.v1.backup_service_pb2.DeleteBackupRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Returns the list of available backups for the specified Redis cluster."""

def add_BackupServiceServicer_to_server(servicer: BackupServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
