"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.mdb.spqr.v1.cluster_pb2
import yandex.cloud.mdb.spqr.v1.cluster_service_pb2
import yandex.cloud.mdb.spqr.v1.shard_pb2
import yandex.cloud.operation.operation_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class ClusterServiceStub:
    """A set of methods for managing SPQR Cluster resources."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.GetClusterRequest,
        yandex.cloud.mdb.spqr.v1.cluster_pb2.Cluster,
    ]
    """Returns the specified SPQR Cluster resource.

    To get the list of available SPQR Cluster resources, make a [List] request.
    """

    GetAtRevision: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.GetClusterAtRevisionRequest,
        yandex.cloud.mdb.spqr.v1.cluster_pb2.Cluster,
    ]

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClustersRequest,
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClustersResponse,
    ]
    """Retrieves the list of SPQR Cluster resources that belong
    to the specified folder.
    """

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.CreateClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a SPQR cluster in the specified folder."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.UpdateClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified SPQR cluster."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.DeleteClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified SPQR cluster."""

    AddSubcluster: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.AddSubclusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]

    Start: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.StartClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Start the specified SPQR cluster."""

    Stop: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.StopClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Stop the specified SPQR cluster."""

    Move: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.MoveClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Moves the specified SPQR cluster to the specified folder."""

    Backup: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.BackupClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a backup for the specified SPQR cluster."""

    Restore: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.RestoreClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a new SPQR cluster using the specified backup."""

    RescheduleMaintenance: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.RescheduleMaintenanceRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Reschedules planned maintenance operation."""

    ListLogs: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterLogsRequest,
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterLogsResponse,
    ]
    """Retrieves logs for the specified SPQR cluster.
    See the [Logs](/yandex-mdb-guide/concepts/logs.html) section in the developers guide for detailed logs description.
    """

    StreamLogs: grpc.UnaryStreamMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.StreamClusterLogsRequest,
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.StreamLogRecord,
    ]
    """Same as ListLogs but using server-side streaming. Also allows for 'tail -f' semantics."""

    ListOperations: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterOperationsRequest,
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterOperationsResponse,
    ]
    """Retrieves the list of Operation resources for the specified cluster."""

    ListBackups: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterBackupsRequest,
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterBackupsResponse,
    ]
    """Retrieves the list of available backups for the specified SPQR cluster."""

    ListHosts: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterHostsRequest,
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterHostsResponse,
    ]
    """Retrieves a list of hosts for the specified cluster."""

    ListHostsAtRevision: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterHostsAtRevisionRequest,
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterHostsResponse,
    ]
    """Retrieves a list of hosts for the specified cluster."""

    AddHosts: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.AddClusterHostsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates new hosts for a cluster."""

    UpdateHosts: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.UpdateClusterHostsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified hosts."""

    DeleteHosts: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.DeleteClusterHostsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified hosts for a cluster."""

    ResetupHosts: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ResetupHostsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Resetups hosts."""

    GetShard: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.GetClusterShardRequest,
        yandex.cloud.mdb.spqr.v1.shard_pb2.Shard,
    ]
    """Returns the specified shard."""

    ListShards: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterShardsRequest,
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterShardsResponse,
    ]
    """Retrieves a list of shards."""

    ListShardsAtRevision: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterShardsAtRevisionRequest,
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterShardsResponse,
    ]
    """Retrieves a list of shards."""

    AddShard: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.AddClusterShardRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a new shard."""

    DeleteShard: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.DeleteClusterShardRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified shard."""

class ClusterServiceAsyncStub:
    """A set of methods for managing SPQR Cluster resources."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.GetClusterRequest,
        yandex.cloud.mdb.spqr.v1.cluster_pb2.Cluster,
    ]
    """Returns the specified SPQR Cluster resource.

    To get the list of available SPQR Cluster resources, make a [List] request.
    """

    GetAtRevision: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.GetClusterAtRevisionRequest,
        yandex.cloud.mdb.spqr.v1.cluster_pb2.Cluster,
    ]

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClustersRequest,
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClustersResponse,
    ]
    """Retrieves the list of SPQR Cluster resources that belong
    to the specified folder.
    """

    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.CreateClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a SPQR cluster in the specified folder."""

    Update: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.UpdateClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified SPQR cluster."""

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.DeleteClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified SPQR cluster."""

    AddSubcluster: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.AddSubclusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]

    Start: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.StartClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Start the specified SPQR cluster."""

    Stop: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.StopClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Stop the specified SPQR cluster."""

    Move: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.MoveClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Moves the specified SPQR cluster to the specified folder."""

    Backup: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.BackupClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a backup for the specified SPQR cluster."""

    Restore: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.RestoreClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a new SPQR cluster using the specified backup."""

    RescheduleMaintenance: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.RescheduleMaintenanceRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Reschedules planned maintenance operation."""

    ListLogs: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterLogsRequest,
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterLogsResponse,
    ]
    """Retrieves logs for the specified SPQR cluster.
    See the [Logs](/yandex-mdb-guide/concepts/logs.html) section in the developers guide for detailed logs description.
    """

    StreamLogs: grpc.aio.UnaryStreamMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.StreamClusterLogsRequest,
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.StreamLogRecord,
    ]
    """Same as ListLogs but using server-side streaming. Also allows for 'tail -f' semantics."""

    ListOperations: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterOperationsRequest,
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterOperationsResponse,
    ]
    """Retrieves the list of Operation resources for the specified cluster."""

    ListBackups: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterBackupsRequest,
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterBackupsResponse,
    ]
    """Retrieves the list of available backups for the specified SPQR cluster."""

    ListHosts: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterHostsRequest,
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterHostsResponse,
    ]
    """Retrieves a list of hosts for the specified cluster."""

    ListHostsAtRevision: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterHostsAtRevisionRequest,
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterHostsResponse,
    ]
    """Retrieves a list of hosts for the specified cluster."""

    AddHosts: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.AddClusterHostsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates new hosts for a cluster."""

    UpdateHosts: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.UpdateClusterHostsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified hosts."""

    DeleteHosts: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.DeleteClusterHostsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified hosts for a cluster."""

    ResetupHosts: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ResetupHostsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Resetups hosts."""

    GetShard: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.GetClusterShardRequest,
        yandex.cloud.mdb.spqr.v1.shard_pb2.Shard,
    ]
    """Returns the specified shard."""

    ListShards: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterShardsRequest,
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterShardsResponse,
    ]
    """Retrieves a list of shards."""

    ListShardsAtRevision: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterShardsAtRevisionRequest,
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterShardsResponse,
    ]
    """Retrieves a list of shards."""

    AddShard: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.AddClusterShardRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a new shard."""

    DeleteShard: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.spqr.v1.cluster_service_pb2.DeleteClusterShardRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified shard."""

class ClusterServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing SPQR Cluster resources."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.mdb.spqr.v1.cluster_service_pb2.GetClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.spqr.v1.cluster_pb2.Cluster, collections.abc.Awaitable[yandex.cloud.mdb.spqr.v1.cluster_pb2.Cluster]]:
        """Returns the specified SPQR Cluster resource.

        To get the list of available SPQR Cluster resources, make a [List] request.
        """

    @abc.abstractmethod
    def GetAtRevision(
        self,
        request: yandex.cloud.mdb.spqr.v1.cluster_service_pb2.GetClusterAtRevisionRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.spqr.v1.cluster_pb2.Cluster, collections.abc.Awaitable[yandex.cloud.mdb.spqr.v1.cluster_pb2.Cluster]]: ...

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClustersRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClustersResponse, collections.abc.Awaitable[yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClustersResponse]]:
        """Retrieves the list of SPQR Cluster resources that belong
        to the specified folder.
        """

    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.mdb.spqr.v1.cluster_service_pb2.CreateClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates a SPQR cluster in the specified folder."""

    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.mdb.spqr.v1.cluster_service_pb2.UpdateClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates the specified SPQR cluster."""

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.mdb.spqr.v1.cluster_service_pb2.DeleteClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deletes the specified SPQR cluster."""

    @abc.abstractmethod
    def AddSubcluster(
        self,
        request: yandex.cloud.mdb.spqr.v1.cluster_service_pb2.AddSubclusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]: ...

    @abc.abstractmethod
    def Start(
        self,
        request: yandex.cloud.mdb.spqr.v1.cluster_service_pb2.StartClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Start the specified SPQR cluster."""

    @abc.abstractmethod
    def Stop(
        self,
        request: yandex.cloud.mdb.spqr.v1.cluster_service_pb2.StopClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Stop the specified SPQR cluster."""

    @abc.abstractmethod
    def Move(
        self,
        request: yandex.cloud.mdb.spqr.v1.cluster_service_pb2.MoveClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Moves the specified SPQR cluster to the specified folder."""

    @abc.abstractmethod
    def Backup(
        self,
        request: yandex.cloud.mdb.spqr.v1.cluster_service_pb2.BackupClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates a backup for the specified SPQR cluster."""

    @abc.abstractmethod
    def Restore(
        self,
        request: yandex.cloud.mdb.spqr.v1.cluster_service_pb2.RestoreClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates a new SPQR cluster using the specified backup."""

    @abc.abstractmethod
    def RescheduleMaintenance(
        self,
        request: yandex.cloud.mdb.spqr.v1.cluster_service_pb2.RescheduleMaintenanceRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Reschedules planned maintenance operation."""

    @abc.abstractmethod
    def ListLogs(
        self,
        request: yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterLogsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterLogsResponse, collections.abc.Awaitable[yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterLogsResponse]]:
        """Retrieves logs for the specified SPQR cluster.
        See the [Logs](/yandex-mdb-guide/concepts/logs.html) section in the developers guide for detailed logs description.
        """

    @abc.abstractmethod
    def StreamLogs(
        self,
        request: yandex.cloud.mdb.spqr.v1.cluster_service_pb2.StreamClusterLogsRequest,
        context: _ServicerContext,
    ) -> typing.Union[collections.abc.Iterator[yandex.cloud.mdb.spqr.v1.cluster_service_pb2.StreamLogRecord], collections.abc.AsyncIterator[yandex.cloud.mdb.spqr.v1.cluster_service_pb2.StreamLogRecord]]:
        """Same as ListLogs but using server-side streaming. Also allows for 'tail -f' semantics."""

    @abc.abstractmethod
    def ListOperations(
        self,
        request: yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterOperationsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterOperationsResponse, collections.abc.Awaitable[yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterOperationsResponse]]:
        """Retrieves the list of Operation resources for the specified cluster."""

    @abc.abstractmethod
    def ListBackups(
        self,
        request: yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterBackupsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterBackupsResponse, collections.abc.Awaitable[yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterBackupsResponse]]:
        """Retrieves the list of available backups for the specified SPQR cluster."""

    @abc.abstractmethod
    def ListHosts(
        self,
        request: yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterHostsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterHostsResponse, collections.abc.Awaitable[yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterHostsResponse]]:
        """Retrieves a list of hosts for the specified cluster."""

    @abc.abstractmethod
    def ListHostsAtRevision(
        self,
        request: yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterHostsAtRevisionRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterHostsResponse, collections.abc.Awaitable[yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterHostsResponse]]:
        """Retrieves a list of hosts for the specified cluster."""

    @abc.abstractmethod
    def AddHosts(
        self,
        request: yandex.cloud.mdb.spqr.v1.cluster_service_pb2.AddClusterHostsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates new hosts for a cluster."""

    @abc.abstractmethod
    def UpdateHosts(
        self,
        request: yandex.cloud.mdb.spqr.v1.cluster_service_pb2.UpdateClusterHostsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates the specified hosts."""

    @abc.abstractmethod
    def DeleteHosts(
        self,
        request: yandex.cloud.mdb.spqr.v1.cluster_service_pb2.DeleteClusterHostsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deletes the specified hosts for a cluster."""

    @abc.abstractmethod
    def ResetupHosts(
        self,
        request: yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ResetupHostsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Resetups hosts."""

    @abc.abstractmethod
    def GetShard(
        self,
        request: yandex.cloud.mdb.spqr.v1.cluster_service_pb2.GetClusterShardRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.spqr.v1.shard_pb2.Shard, collections.abc.Awaitable[yandex.cloud.mdb.spqr.v1.shard_pb2.Shard]]:
        """Returns the specified shard."""

    @abc.abstractmethod
    def ListShards(
        self,
        request: yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterShardsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterShardsResponse, collections.abc.Awaitable[yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterShardsResponse]]:
        """Retrieves a list of shards."""

    @abc.abstractmethod
    def ListShardsAtRevision(
        self,
        request: yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterShardsAtRevisionRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterShardsResponse, collections.abc.Awaitable[yandex.cloud.mdb.spqr.v1.cluster_service_pb2.ListClusterShardsResponse]]:
        """Retrieves a list of shards."""

    @abc.abstractmethod
    def AddShard(
        self,
        request: yandex.cloud.mdb.spqr.v1.cluster_service_pb2.AddClusterShardRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates a new shard."""

    @abc.abstractmethod
    def DeleteShard(
        self,
        request: yandex.cloud.mdb.spqr.v1.cluster_service_pb2.DeleteClusterShardRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deletes the specified shard."""

def add_ClusterServiceServicer_to_server(servicer: ClusterServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
