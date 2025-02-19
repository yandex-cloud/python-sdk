"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.mdb.mongodb.v1.cluster_pb2
import yandex.cloud.mdb.mongodb.v1.cluster_service_pb2
import yandex.cloud.operation.operation_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class ClusterServiceStub:
    """A set of methods for managing MongoDB Cluster resources."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.GetClusterRequest,
        yandex.cloud.mdb.mongodb.v1.cluster_pb2.Cluster,
    ]
    """Returns the specified MongoDB Cluster resource.

    To get the list of available MongoDB Cluster resources, make a [List] request.
    """

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClustersRequest,
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClustersResponse,
    ]
    """Retrieves the list of MongoDB Cluster resources that belong
    to the specified folder.
    """

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.CreateClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a MongoDB cluster in the specified folder."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.UpdateClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified MongoDB cluster."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.DeleteClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified MongoDB cluster."""

    Start: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.StartClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Start the specified MongoDB cluster."""

    Stop: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.StopClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Stop the specified MongoDB cluster."""

    Move: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.MoveClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Moves the specified MongoDB cluster to the specified folder."""

    Backup: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.BackupClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a backup for the specified MongoDB cluster."""

    Restore: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.RestoreClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a new MongoDB cluster using the specified backup."""

    RescheduleMaintenance: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.RescheduleMaintenanceRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Reschedules planned maintenance operation."""

    ListLogs: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClusterLogsRequest,
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClusterLogsResponse,
    ]
    """Retrieves logs for the specified MongoDB cluster."""

    StreamLogs: grpc.UnaryStreamMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.StreamClusterLogsRequest,
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.StreamLogRecord,
    ]
    """Same as ListLogs but using server-side streaming. Also allows for 'tail -f' semantics."""

    ListOperations: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClusterOperationsRequest,
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClusterOperationsResponse,
    ]
    """Retrieves the list of Operation resources for the specified cluster."""

    ListBackups: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClusterBackupsRequest,
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClusterBackupsResponse,
    ]
    """Retrieves the list of available backups for the specified MongoDB cluster."""

    ListHosts: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClusterHostsRequest,
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClusterHostsResponse,
    ]
    """Retrieves a list of hosts for the specified cluster."""

    AddHosts: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.AddClusterHostsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates new hosts for a cluster."""

    DeleteHosts: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.DeleteClusterHostsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified hosts for a cluster."""

    UpdateHosts: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.UpdateClusterHostsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified parameters for the host."""

    EnableSharding: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.EnableClusterShardingRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Enables sharding for the cluster:
    creates 3 mongoinfra (or 3 mongocfg and 2 mongos) hosts
    that would support adding and using shards in the cluster.
    """

    GetShard: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.GetClusterShardRequest,
        yandex.cloud.mdb.mongodb.v1.cluster_pb2.Shard,
    ]
    """Returns the specified shard."""

    ListShards: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClusterShardsRequest,
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClusterShardsResponse,
    ]
    """Retrieves a list of shards."""

    AddShard: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.AddClusterShardRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a new shard."""

    DeleteShard: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.DeleteClusterShardRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified shard."""

    ResetupHosts: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ResetupHostsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Resetups hosts."""

    RestartHosts: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.RestartHostsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Restarts hosts."""

    StepdownHosts: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.StepdownHostsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Stepdown hosts."""

class ClusterServiceAsyncStub:
    """A set of methods for managing MongoDB Cluster resources."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.GetClusterRequest,
        yandex.cloud.mdb.mongodb.v1.cluster_pb2.Cluster,
    ]
    """Returns the specified MongoDB Cluster resource.

    To get the list of available MongoDB Cluster resources, make a [List] request.
    """

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClustersRequest,
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClustersResponse,
    ]
    """Retrieves the list of MongoDB Cluster resources that belong
    to the specified folder.
    """

    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.CreateClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a MongoDB cluster in the specified folder."""

    Update: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.UpdateClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified MongoDB cluster."""

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.DeleteClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified MongoDB cluster."""

    Start: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.StartClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Start the specified MongoDB cluster."""

    Stop: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.StopClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Stop the specified MongoDB cluster."""

    Move: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.MoveClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Moves the specified MongoDB cluster to the specified folder."""

    Backup: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.BackupClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a backup for the specified MongoDB cluster."""

    Restore: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.RestoreClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a new MongoDB cluster using the specified backup."""

    RescheduleMaintenance: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.RescheduleMaintenanceRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Reschedules planned maintenance operation."""

    ListLogs: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClusterLogsRequest,
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClusterLogsResponse,
    ]
    """Retrieves logs for the specified MongoDB cluster."""

    StreamLogs: grpc.aio.UnaryStreamMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.StreamClusterLogsRequest,
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.StreamLogRecord,
    ]
    """Same as ListLogs but using server-side streaming. Also allows for 'tail -f' semantics."""

    ListOperations: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClusterOperationsRequest,
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClusterOperationsResponse,
    ]
    """Retrieves the list of Operation resources for the specified cluster."""

    ListBackups: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClusterBackupsRequest,
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClusterBackupsResponse,
    ]
    """Retrieves the list of available backups for the specified MongoDB cluster."""

    ListHosts: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClusterHostsRequest,
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClusterHostsResponse,
    ]
    """Retrieves a list of hosts for the specified cluster."""

    AddHosts: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.AddClusterHostsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates new hosts for a cluster."""

    DeleteHosts: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.DeleteClusterHostsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified hosts for a cluster."""

    UpdateHosts: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.UpdateClusterHostsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified parameters for the host."""

    EnableSharding: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.EnableClusterShardingRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Enables sharding for the cluster:
    creates 3 mongoinfra (or 3 mongocfg and 2 mongos) hosts
    that would support adding and using shards in the cluster.
    """

    GetShard: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.GetClusterShardRequest,
        yandex.cloud.mdb.mongodb.v1.cluster_pb2.Shard,
    ]
    """Returns the specified shard."""

    ListShards: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClusterShardsRequest,
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClusterShardsResponse,
    ]
    """Retrieves a list of shards."""

    AddShard: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.AddClusterShardRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a new shard."""

    DeleteShard: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.DeleteClusterShardRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified shard."""

    ResetupHosts: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ResetupHostsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Resetups hosts."""

    RestartHosts: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.RestartHostsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Restarts hosts."""

    StepdownHosts: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.StepdownHostsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Stepdown hosts."""

class ClusterServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing MongoDB Cluster resources."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.GetClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.mongodb.v1.cluster_pb2.Cluster, collections.abc.Awaitable[yandex.cloud.mdb.mongodb.v1.cluster_pb2.Cluster]]:
        """Returns the specified MongoDB Cluster resource.

        To get the list of available MongoDB Cluster resources, make a [List] request.
        """

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClustersRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClustersResponse, collections.abc.Awaitable[yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClustersResponse]]:
        """Retrieves the list of MongoDB Cluster resources that belong
        to the specified folder.
        """

    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.CreateClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates a MongoDB cluster in the specified folder."""

    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.UpdateClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates the specified MongoDB cluster."""

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.DeleteClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deletes the specified MongoDB cluster."""

    @abc.abstractmethod
    def Start(
        self,
        request: yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.StartClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Start the specified MongoDB cluster."""

    @abc.abstractmethod
    def Stop(
        self,
        request: yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.StopClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Stop the specified MongoDB cluster."""

    @abc.abstractmethod
    def Move(
        self,
        request: yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.MoveClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Moves the specified MongoDB cluster to the specified folder."""

    @abc.abstractmethod
    def Backup(
        self,
        request: yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.BackupClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates a backup for the specified MongoDB cluster."""

    @abc.abstractmethod
    def Restore(
        self,
        request: yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.RestoreClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates a new MongoDB cluster using the specified backup."""

    @abc.abstractmethod
    def RescheduleMaintenance(
        self,
        request: yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.RescheduleMaintenanceRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Reschedules planned maintenance operation."""

    @abc.abstractmethod
    def ListLogs(
        self,
        request: yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClusterLogsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClusterLogsResponse, collections.abc.Awaitable[yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClusterLogsResponse]]:
        """Retrieves logs for the specified MongoDB cluster."""

    @abc.abstractmethod
    def StreamLogs(
        self,
        request: yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.StreamClusterLogsRequest,
        context: _ServicerContext,
    ) -> typing.Union[collections.abc.Iterator[yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.StreamLogRecord], collections.abc.AsyncIterator[yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.StreamLogRecord]]:
        """Same as ListLogs but using server-side streaming. Also allows for 'tail -f' semantics."""

    @abc.abstractmethod
    def ListOperations(
        self,
        request: yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClusterOperationsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClusterOperationsResponse, collections.abc.Awaitable[yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClusterOperationsResponse]]:
        """Retrieves the list of Operation resources for the specified cluster."""

    @abc.abstractmethod
    def ListBackups(
        self,
        request: yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClusterBackupsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClusterBackupsResponse, collections.abc.Awaitable[yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClusterBackupsResponse]]:
        """Retrieves the list of available backups for the specified MongoDB cluster."""

    @abc.abstractmethod
    def ListHosts(
        self,
        request: yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClusterHostsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClusterHostsResponse, collections.abc.Awaitable[yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClusterHostsResponse]]:
        """Retrieves a list of hosts for the specified cluster."""

    @abc.abstractmethod
    def AddHosts(
        self,
        request: yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.AddClusterHostsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates new hosts for a cluster."""

    @abc.abstractmethod
    def DeleteHosts(
        self,
        request: yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.DeleteClusterHostsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deletes the specified hosts for a cluster."""

    @abc.abstractmethod
    def UpdateHosts(
        self,
        request: yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.UpdateClusterHostsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates the specified parameters for the host."""

    @abc.abstractmethod
    def EnableSharding(
        self,
        request: yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.EnableClusterShardingRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Enables sharding for the cluster:
        creates 3 mongoinfra (or 3 mongocfg and 2 mongos) hosts
        that would support adding and using shards in the cluster.
        """

    @abc.abstractmethod
    def GetShard(
        self,
        request: yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.GetClusterShardRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.mongodb.v1.cluster_pb2.Shard, collections.abc.Awaitable[yandex.cloud.mdb.mongodb.v1.cluster_pb2.Shard]]:
        """Returns the specified shard."""

    @abc.abstractmethod
    def ListShards(
        self,
        request: yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClusterShardsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClusterShardsResponse, collections.abc.Awaitable[yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ListClusterShardsResponse]]:
        """Retrieves a list of shards."""

    @abc.abstractmethod
    def AddShard(
        self,
        request: yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.AddClusterShardRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates a new shard."""

    @abc.abstractmethod
    def DeleteShard(
        self,
        request: yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.DeleteClusterShardRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deletes the specified shard."""

    @abc.abstractmethod
    def ResetupHosts(
        self,
        request: yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.ResetupHostsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Resetups hosts."""

    @abc.abstractmethod
    def RestartHosts(
        self,
        request: yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.RestartHostsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Restarts hosts."""

    @abc.abstractmethod
    def StepdownHosts(
        self,
        request: yandex.cloud.mdb.mongodb.v1.cluster_service_pb2.StepdownHostsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Stepdown hosts."""

def add_ClusterServiceServicer_to_server(servicer: ClusterServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
