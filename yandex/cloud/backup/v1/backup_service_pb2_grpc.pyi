"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.backup.v1.backup_pb2
import yandex.cloud.backup.v1.backup_service_pb2
import yandex.cloud.operation.operation_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class BackupServiceStub:
    """A set of methods for managing [backups](/docs/backup/concepts/backup)."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.backup.v1.backup_service_pb2.ListBackupsRequest,
        yandex.cloud.backup.v1.backup_service_pb2.ListBackupsResponse,
    ]
    """List backups using filters."""

    ListArchives: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.backup.v1.backup_service_pb2.ListArchivesRequest,
        yandex.cloud.backup.v1.backup_service_pb2.ListArchivesResponse,
    ]
    """List archives that holds backups for specified folder or
    specified [Compute Cloud instance](/docs/backup/concepts/vm-connection#os).
    """

    ListFiles: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.backup.v1.backup_service_pb2.ListFilesRequest,
        yandex.cloud.backup.v1.backup_service_pb2.ListFilesResponse,
    ]
    """ListFiles of the backup."""

    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.backup.v1.backup_service_pb2.GetBackupRequest,
        yandex.cloud.backup.v1.backup_pb2.Backup,
    ]
    """Get backup by its id."""

    StartRecovery: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.backup.v1.backup_service_pb2.StartRecoveryRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Start recovery process of specified backup to specific Compute Cloud instance.

    For details, see [Restoring a VM from a backup](/docs/backup/operations/backup-vm/recover).
    """

    StartFilesRecovery: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.backup.v1.backup_service_pb2.StartFilesRecoveryRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """StartFilesRecovery runs recovery process of selected files to specific Compute Cloud instance."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.backup.v1.backup_service_pb2.DeleteBackupRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Delete specific backup."""

    DeleteArchive: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.backup.v1.backup_service_pb2.DeleteArchiveRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Delete specific archive."""

class BackupServiceAsyncStub:
    """A set of methods for managing [backups](/docs/backup/concepts/backup)."""

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.backup.v1.backup_service_pb2.ListBackupsRequest,
        yandex.cloud.backup.v1.backup_service_pb2.ListBackupsResponse,
    ]
    """List backups using filters."""

    ListArchives: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.backup.v1.backup_service_pb2.ListArchivesRequest,
        yandex.cloud.backup.v1.backup_service_pb2.ListArchivesResponse,
    ]
    """List archives that holds backups for specified folder or
    specified [Compute Cloud instance](/docs/backup/concepts/vm-connection#os).
    """

    ListFiles: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.backup.v1.backup_service_pb2.ListFilesRequest,
        yandex.cloud.backup.v1.backup_service_pb2.ListFilesResponse,
    ]
    """ListFiles of the backup."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.backup.v1.backup_service_pb2.GetBackupRequest,
        yandex.cloud.backup.v1.backup_pb2.Backup,
    ]
    """Get backup by its id."""

    StartRecovery: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.backup.v1.backup_service_pb2.StartRecoveryRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Start recovery process of specified backup to specific Compute Cloud instance.

    For details, see [Restoring a VM from a backup](/docs/backup/operations/backup-vm/recover).
    """

    StartFilesRecovery: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.backup.v1.backup_service_pb2.StartFilesRecoveryRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """StartFilesRecovery runs recovery process of selected files to specific Compute Cloud instance."""

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.backup.v1.backup_service_pb2.DeleteBackupRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Delete specific backup."""

    DeleteArchive: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.backup.v1.backup_service_pb2.DeleteArchiveRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Delete specific archive."""

class BackupServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing [backups](/docs/backup/concepts/backup)."""

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.backup.v1.backup_service_pb2.ListBackupsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.backup.v1.backup_service_pb2.ListBackupsResponse, collections.abc.Awaitable[yandex.cloud.backup.v1.backup_service_pb2.ListBackupsResponse]]:
        """List backups using filters."""

    @abc.abstractmethod
    def ListArchives(
        self,
        request: yandex.cloud.backup.v1.backup_service_pb2.ListArchivesRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.backup.v1.backup_service_pb2.ListArchivesResponse, collections.abc.Awaitable[yandex.cloud.backup.v1.backup_service_pb2.ListArchivesResponse]]:
        """List archives that holds backups for specified folder or
        specified [Compute Cloud instance](/docs/backup/concepts/vm-connection#os).
        """

    @abc.abstractmethod
    def ListFiles(
        self,
        request: yandex.cloud.backup.v1.backup_service_pb2.ListFilesRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.backup.v1.backup_service_pb2.ListFilesResponse, collections.abc.Awaitable[yandex.cloud.backup.v1.backup_service_pb2.ListFilesResponse]]:
        """ListFiles of the backup."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.backup.v1.backup_service_pb2.GetBackupRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.backup.v1.backup_pb2.Backup, collections.abc.Awaitable[yandex.cloud.backup.v1.backup_pb2.Backup]]:
        """Get backup by its id."""

    @abc.abstractmethod
    def StartRecovery(
        self,
        request: yandex.cloud.backup.v1.backup_service_pb2.StartRecoveryRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Start recovery process of specified backup to specific Compute Cloud instance.

        For details, see [Restoring a VM from a backup](/docs/backup/operations/backup-vm/recover).
        """

    @abc.abstractmethod
    def StartFilesRecovery(
        self,
        request: yandex.cloud.backup.v1.backup_service_pb2.StartFilesRecoveryRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """StartFilesRecovery runs recovery process of selected files to specific Compute Cloud instance."""

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.backup.v1.backup_service_pb2.DeleteBackupRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Delete specific backup."""

    @abc.abstractmethod
    def DeleteArchive(
        self,
        request: yandex.cloud.backup.v1.backup_service_pb2.DeleteArchiveRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Delete specific archive."""

def add_BackupServiceServicer_to_server(servicer: BackupServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
