"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.mdb.sqlserver.v1.cluster_pb2
import yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2
import yandex.cloud.operation.operation_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class ClusterServiceStub:
    """A set of methods for managing SQL Server clusters."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.GetClusterRequest,
        yandex.cloud.mdb.sqlserver.v1.cluster_pb2.Cluster,
    ]
    """Returns the specified SQL Server cluster.

    To get the list of available SQL Server clusters, make a [List] request.
    """

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.ListClustersRequest,
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.ListClustersResponse,
    ]
    """Retrieves the list of SQL Server clusters that belong to the specified folder."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.CreateClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates an SQL Server cluster in the specified folder."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.UpdateClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Modifies the specified SQL Server cluster."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.DeleteClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified SQL Server cluster."""

    Start: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.StartClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Starts the specified SQL Server cluster."""

    Stop: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.StopClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Stops the specified SQL Server cluster."""

    Move: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.MoveClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Moves the specified SQL Server cluster to the specified folder."""

    Backup: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.BackupClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a backup for the specified SQL Server cluster."""

    Restore: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.RestoreClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a new SQL Server cluster using the specified backup."""

    StartFailover: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.StartClusterFailoverRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Starts a manual failover for a cluster."""

    ListLogs: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.ListClusterLogsRequest,
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.ListClusterLogsResponse,
    ]
    """Retrieves logs for the specified SQL Server cluster.

    For more information about logs, see the [Logs](/docs/managed-sqlserver/operations/cluster-logs) section in the documentation.
    """

    ListOperations: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.ListClusterOperationsRequest,
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.ListClusterOperationsResponse,
    ]
    """Retrieves the list of operations for the specified SQL Server cluster."""

    ListBackups: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.ListClusterBackupsRequest,
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.ListClusterBackupsResponse,
    ]
    """Retrieves the list of available backups for the specified SQL Server cluster."""

    ListHosts: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.ListClusterHostsRequest,
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.ListClusterHostsResponse,
    ]
    """Retrieves the list of hosts for the specified SQL Server cluster."""

    UpdateHosts: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.UpdateClusterHostsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified hosts."""

class ClusterServiceAsyncStub:
    """A set of methods for managing SQL Server clusters."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.GetClusterRequest,
        yandex.cloud.mdb.sqlserver.v1.cluster_pb2.Cluster,
    ]
    """Returns the specified SQL Server cluster.

    To get the list of available SQL Server clusters, make a [List] request.
    """

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.ListClustersRequest,
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.ListClustersResponse,
    ]
    """Retrieves the list of SQL Server clusters that belong to the specified folder."""

    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.CreateClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates an SQL Server cluster in the specified folder."""

    Update: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.UpdateClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Modifies the specified SQL Server cluster."""

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.DeleteClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified SQL Server cluster."""

    Start: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.StartClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Starts the specified SQL Server cluster."""

    Stop: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.StopClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Stops the specified SQL Server cluster."""

    Move: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.MoveClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Moves the specified SQL Server cluster to the specified folder."""

    Backup: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.BackupClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a backup for the specified SQL Server cluster."""

    Restore: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.RestoreClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a new SQL Server cluster using the specified backup."""

    StartFailover: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.StartClusterFailoverRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Starts a manual failover for a cluster."""

    ListLogs: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.ListClusterLogsRequest,
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.ListClusterLogsResponse,
    ]
    """Retrieves logs for the specified SQL Server cluster.

    For more information about logs, see the [Logs](/docs/managed-sqlserver/operations/cluster-logs) section in the documentation.
    """

    ListOperations: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.ListClusterOperationsRequest,
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.ListClusterOperationsResponse,
    ]
    """Retrieves the list of operations for the specified SQL Server cluster."""

    ListBackups: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.ListClusterBackupsRequest,
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.ListClusterBackupsResponse,
    ]
    """Retrieves the list of available backups for the specified SQL Server cluster."""

    ListHosts: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.ListClusterHostsRequest,
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.ListClusterHostsResponse,
    ]
    """Retrieves the list of hosts for the specified SQL Server cluster."""

    UpdateHosts: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.UpdateClusterHostsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified hosts."""

class ClusterServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing SQL Server clusters."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.GetClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.sqlserver.v1.cluster_pb2.Cluster, collections.abc.Awaitable[yandex.cloud.mdb.sqlserver.v1.cluster_pb2.Cluster]]:
        """Returns the specified SQL Server cluster.

        To get the list of available SQL Server clusters, make a [List] request.
        """

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.ListClustersRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.ListClustersResponse, collections.abc.Awaitable[yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.ListClustersResponse]]:
        """Retrieves the list of SQL Server clusters that belong to the specified folder."""

    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.CreateClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates an SQL Server cluster in the specified folder."""

    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.UpdateClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Modifies the specified SQL Server cluster."""

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.DeleteClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deletes the specified SQL Server cluster."""

    @abc.abstractmethod
    def Start(
        self,
        request: yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.StartClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Starts the specified SQL Server cluster."""

    @abc.abstractmethod
    def Stop(
        self,
        request: yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.StopClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Stops the specified SQL Server cluster."""

    @abc.abstractmethod
    def Move(
        self,
        request: yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.MoveClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Moves the specified SQL Server cluster to the specified folder."""

    @abc.abstractmethod
    def Backup(
        self,
        request: yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.BackupClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates a backup for the specified SQL Server cluster."""

    @abc.abstractmethod
    def Restore(
        self,
        request: yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.RestoreClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates a new SQL Server cluster using the specified backup."""

    @abc.abstractmethod
    def StartFailover(
        self,
        request: yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.StartClusterFailoverRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Starts a manual failover for a cluster."""

    @abc.abstractmethod
    def ListLogs(
        self,
        request: yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.ListClusterLogsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.ListClusterLogsResponse, collections.abc.Awaitable[yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.ListClusterLogsResponse]]:
        """Retrieves logs for the specified SQL Server cluster.

        For more information about logs, see the [Logs](/docs/managed-sqlserver/operations/cluster-logs) section in the documentation.
        """

    @abc.abstractmethod
    def ListOperations(
        self,
        request: yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.ListClusterOperationsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.ListClusterOperationsResponse, collections.abc.Awaitable[yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.ListClusterOperationsResponse]]:
        """Retrieves the list of operations for the specified SQL Server cluster."""

    @abc.abstractmethod
    def ListBackups(
        self,
        request: yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.ListClusterBackupsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.ListClusterBackupsResponse, collections.abc.Awaitable[yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.ListClusterBackupsResponse]]:
        """Retrieves the list of available backups for the specified SQL Server cluster."""

    @abc.abstractmethod
    def ListHosts(
        self,
        request: yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.ListClusterHostsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.ListClusterHostsResponse, collections.abc.Awaitable[yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.ListClusterHostsResponse]]:
        """Retrieves the list of hosts for the specified SQL Server cluster."""

    @abc.abstractmethod
    def UpdateHosts(
        self,
        request: yandex.cloud.mdb.sqlserver.v1.cluster_service_pb2.UpdateClusterHostsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates the specified hosts."""

def add_ClusterServiceServicer_to_server(servicer: ClusterServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
