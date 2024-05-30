"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys
import typing
import yandex.cloud.mdb.kafka.v1.cluster_pb2
import yandex.cloud.mdb.kafka.v1.maintenance_pb2
import yandex.cloud.mdb.kafka.v1.topic_pb2
import yandex.cloud.mdb.kafka.v1.user_pb2
import yandex.cloud.operation.operation_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetClusterRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Apache Kafka® Cluster resource to return.

    To get the cluster ID, make a [ClusterService.List] request.
    """
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id"]) -> None: ...

global___GetClusterRequest = GetClusterRequest

@typing.final
class ListClustersRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to list Apache Kafka® clusters in.

    To get the folder ID, make a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return.

    If the number of available results is larger than [page_size], the service returns a [ListClustersResponse.next_page_token] that can be used to get the next page of results in subsequent list requests.
    """
    page_token: builtins.str
    """Page token.

    To get the next page of results, set [page_token] to the [ListClustersResponse.next_page_token] returned by the previous list request.
    """
    filter: builtins.str
    """Filter support is not currently implemented. Any filters are ignored."""
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["filter", b"filter", "folder_id", b"folder_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListClustersRequest = ListClustersRequest

@typing.final
class ListClustersResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTERS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token that allows you to get the next page of results for list requests.

    If the number of results is larger than [ListClustersRequest.page_size], use [next_page_token] as the value for the [ListClustersRequest.page_token] parameter in the next list request.
    Each subsequent list request will have its own [next_page_token] to continue paging through the results.
    """
    @property
    def clusters(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.mdb.kafka.v1.cluster_pb2.Cluster]:
        """List of Apache Kafka® clusters."""

    def __init__(
        self,
        *,
        clusters: collections.abc.Iterable[yandex.cloud.mdb.kafka.v1.cluster_pb2.Cluster] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["clusters", b"clusters", "next_page_token", b"next_page_token"]) -> None: ...

global___ListClustersResponse = ListClustersResponse

@typing.final
class CreateClusterRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class LabelsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    FOLDER_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    ENVIRONMENT_FIELD_NUMBER: builtins.int
    CONFIG_SPEC_FIELD_NUMBER: builtins.int
    TOPIC_SPECS_FIELD_NUMBER: builtins.int
    USER_SPECS_FIELD_NUMBER: builtins.int
    NETWORK_ID_FIELD_NUMBER: builtins.int
    SUBNET_ID_FIELD_NUMBER: builtins.int
    SECURITY_GROUP_IDS_FIELD_NUMBER: builtins.int
    HOST_GROUP_IDS_FIELD_NUMBER: builtins.int
    DELETION_PROTECTION_FIELD_NUMBER: builtins.int
    MAINTENANCE_WINDOW_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to create the Apache Kafka® cluster in.

    To get the folder ID, make a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    name: builtins.str
    """Name of the Apache Kafka® cluster. The name must be unique within the folder."""
    description: builtins.str
    """Description of the Apache Kafka® cluster."""
    environment: yandex.cloud.mdb.kafka.v1.cluster_pb2.Cluster.Environment.ValueType
    """Deployment environment of the Apache Kafka® cluster."""
    network_id: builtins.str
    """ID of the network to create the Apache Kafka® cluster in."""
    deletion_protection: builtins.bool
    """Deletion Protection inhibits deletion of the cluster"""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Custom labels for the Apache Kafka® cluster as `key:value` pairs.

        For example, "project": "mvp" or "source": "dictionary".
        """

    @property
    def config_spec(self) -> yandex.cloud.mdb.kafka.v1.cluster_pb2.ConfigSpec:
        """Kafka and hosts configuration the Apache Kafka® cluster."""

    @property
    def topic_specs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.mdb.kafka.v1.topic_pb2.TopicSpec]:
        """One or more configurations of topics to be created in the Apache Kafka® cluster."""

    @property
    def user_specs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.mdb.kafka.v1.user_pb2.UserSpec]:
        """Configurations of accounts to be created in the Apache Kafka® cluster."""

    @property
    def subnet_id(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """IDs of subnets to create brokers in."""

    @property
    def security_group_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """User security groups"""

    @property
    def host_group_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Host groups to place VMs of cluster on."""

    @property
    def maintenance_window(self) -> yandex.cloud.mdb.kafka.v1.maintenance_pb2.MaintenanceWindow:
        """Window of maintenance operations."""

    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        environment: yandex.cloud.mdb.kafka.v1.cluster_pb2.Cluster.Environment.ValueType = ...,
        config_spec: yandex.cloud.mdb.kafka.v1.cluster_pb2.ConfigSpec | None = ...,
        topic_specs: collections.abc.Iterable[yandex.cloud.mdb.kafka.v1.topic_pb2.TopicSpec] | None = ...,
        user_specs: collections.abc.Iterable[yandex.cloud.mdb.kafka.v1.user_pb2.UserSpec] | None = ...,
        network_id: builtins.str = ...,
        subnet_id: collections.abc.Iterable[builtins.str] | None = ...,
        security_group_ids: collections.abc.Iterable[builtins.str] | None = ...,
        host_group_ids: collections.abc.Iterable[builtins.str] | None = ...,
        deletion_protection: builtins.bool = ...,
        maintenance_window: yandex.cloud.mdb.kafka.v1.maintenance_pb2.MaintenanceWindow | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["config_spec", b"config_spec", "maintenance_window", b"maintenance_window"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["config_spec", b"config_spec", "deletion_protection", b"deletion_protection", "description", b"description", "environment", b"environment", "folder_id", b"folder_id", "host_group_ids", b"host_group_ids", "labels", b"labels", "maintenance_window", b"maintenance_window", "name", b"name", "network_id", b"network_id", "security_group_ids", b"security_group_ids", "subnet_id", b"subnet_id", "topic_specs", b"topic_specs", "user_specs", b"user_specs"]) -> None: ...

global___CreateClusterRequest = CreateClusterRequest

@typing.final
class CreateClusterMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Apache Kafka® cluster that is being created."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id"]) -> None: ...

global___CreateClusterMetadata = CreateClusterMetadata

@typing.final
class UpdateClusterRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class LabelsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    CONFIG_SPEC_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    SECURITY_GROUP_IDS_FIELD_NUMBER: builtins.int
    DELETION_PROTECTION_FIELD_NUMBER: builtins.int
    MAINTENANCE_WINDOW_FIELD_NUMBER: builtins.int
    SUBNET_IDS_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Apache Kafka® cluster to update.

    To get the Apache Kafka® cluster ID, make a [ClusterService.List] request.
    """
    description: builtins.str
    """New description of the Apache Kafka® cluster."""
    name: builtins.str
    """New name for the Apache Kafka® cluster."""
    deletion_protection: builtins.bool
    """Deletion Protection inhibits deletion of the cluster"""
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask: ...
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Custom labels for the Apache Kafka® cluster as `key:value` pairs.

        For example, "project": "mvp" or "source": "dictionary".

        The new set of labels will completely replace the old ones.
        To add a label, request the current set with the [ClusterService.Get] method, then send an [ClusterService.Update] request with the new label added to the set.
        """

    @property
    def config_spec(self) -> yandex.cloud.mdb.kafka.v1.cluster_pb2.ConfigSpec:
        """New configuration and resources for hosts in the Apache Kafka® cluster.

        Use [update_mask] to prevent reverting all cluster settings that are not listed in [config_spec] to their default values.
        """

    @property
    def security_group_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """User security groups"""

    @property
    def maintenance_window(self) -> yandex.cloud.mdb.kafka.v1.maintenance_pb2.MaintenanceWindow:
        """New maintenance window settings for the cluster."""

    @property
    def subnet_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """IDs of subnets where the hosts are located or a new host is being created"""

    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        config_spec: yandex.cloud.mdb.kafka.v1.cluster_pb2.ConfigSpec | None = ...,
        name: builtins.str = ...,
        security_group_ids: collections.abc.Iterable[builtins.str] | None = ...,
        deletion_protection: builtins.bool = ...,
        maintenance_window: yandex.cloud.mdb.kafka.v1.maintenance_pb2.MaintenanceWindow | None = ...,
        subnet_ids: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["config_spec", b"config_spec", "maintenance_window", b"maintenance_window", "update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "config_spec", b"config_spec", "deletion_protection", b"deletion_protection", "description", b"description", "labels", b"labels", "maintenance_window", b"maintenance_window", "name", b"name", "security_group_ids", b"security_group_ids", "subnet_ids", b"subnet_ids", "update_mask", b"update_mask"]) -> None: ...

global___UpdateClusterRequest = UpdateClusterRequest

@typing.final
class UpdateClusterMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Apache Kafka® cluster that is being updated."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id"]) -> None: ...

global___UpdateClusterMetadata = UpdateClusterMetadata

@typing.final
class DeleteClusterRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Apache Kafka® cluster to delete.

    To get the Apache Kafka® cluster ID, make a [ClusterService.List] request.
    """
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id"]) -> None: ...

global___DeleteClusterRequest = DeleteClusterRequest

@typing.final
class DeleteClusterMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Apache Kafka® cluster that is being deleted."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id"]) -> None: ...

global___DeleteClusterMetadata = DeleteClusterMetadata

@typing.final
class ListClusterLogsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    COLUMN_FILTER_FIELD_NUMBER: builtins.int
    FROM_TIME_FIELD_NUMBER: builtins.int
    TO_TIME_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    ALWAYS_NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Apache Kafka® cluster to request logs for.

    To get the Apache Kafka® cluster ID, make a [ClusterService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return.

    If the number of available results is larger than [page_size], the service returns a [ListClusterLogsResponse.next_page_token] that can be used to get the next page of results in subsequent list requests.
    """
    page_token: builtins.str
    """Page token.

    To get the next page of results, set [page_token] to the [ListClusterLogsResponse.next_page_token] returned by the previous list request.
    """
    always_next_page_token: builtins.bool
    """The flag that defines behavior of providing the next page token.

    If this flag is set to `true`, this API method will always return [ListClusterLogsResponse.next_page_token], even if current page is empty.
    """
    filter: builtins.str
    """A filter expression that filters resources listed in the response.

    The expression must specify:
    1. The field name to filter by. Currently filtering can be applied to the `hostname` field.
    2. An `=` operator.
    3. The value in double quotes (`"`). Must be 1-63 characters long and match the regular expression `[a-z0-9.-]{1,61}`.

    Example of a filter: `message.hostname='node1.db.cloud.yandex.net'`
    """
    @property
    def column_filter(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Columns from the logs table to request.

        If no columns are specified, full log records are returned.
        """

    @property
    def from_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Start timestamp for the logs request."""

    @property
    def to_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """End timestamp for the logs request."""

    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        column_filter: collections.abc.Iterable[builtins.str] | None = ...,
        from_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        to_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        always_next_page_token: builtins.bool = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["from_time", b"from_time", "to_time", b"to_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["always_next_page_token", b"always_next_page_token", "cluster_id", b"cluster_id", "column_filter", b"column_filter", "filter", b"filter", "from_time", b"from_time", "page_size", b"page_size", "page_token", b"page_token", "to_time", b"to_time"]) -> None: ...

global___ListClusterLogsRequest = ListClusterLogsRequest

@typing.final
class LogRecord(google.protobuf.message.Message):
    """A single log record."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class MessageEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    TIMESTAMP_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Log record timestamp."""

    @property
    def message(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Contents of the log record."""

    def __init__(
        self,
        *,
        timestamp: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        message: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["timestamp", b"timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["message", b"message", "timestamp", b"timestamp"]) -> None: ...

global___LogRecord = LogRecord

@typing.final
class ListClusterLogsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOGS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token that allows you to get the next page of results for list requests.

    If the number of results is larger than [ListClusterLogsRequest.page_size], use [next_page_token] as the value for the [ListClusterLogsRequest.page_token] query parameter in the next list request.
    Each subsequent list request will have its own [next_page_token] to continue paging through the results.
    This value is interchangeable with [StreamLogRecord.next_record_token] from StreamLogs method.
    """
    @property
    def logs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___LogRecord]:
        """Requested log records."""

    def __init__(
        self,
        *,
        logs: collections.abc.Iterable[global___LogRecord] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["logs", b"logs", "next_page_token", b"next_page_token"]) -> None: ...

global___ListClusterLogsResponse = ListClusterLogsResponse

@typing.final
class StreamLogRecord(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RECORD_FIELD_NUMBER: builtins.int
    NEXT_RECORD_TOKEN_FIELD_NUMBER: builtins.int
    next_record_token: builtins.str
    """This token allows you to continue streaming logs starting from the exact same record.

    To continue streaming, specify value of [next_record_token] as value for [StreamClusterLogsRequest.record_token] parameter in the next StreamLogs request.

    This value is interchangeable with [ListClusterLogsResponse.next_page_token] from ListLogs method.
    """
    @property
    def record(self) -> global___LogRecord:
        """One of the requested log records."""

    def __init__(
        self,
        *,
        record: global___LogRecord | None = ...,
        next_record_token: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["record", b"record"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["next_record_token", b"next_record_token", "record", b"record"]) -> None: ...

global___StreamLogRecord = StreamLogRecord

@typing.final
class StreamClusterLogsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    COLUMN_FILTER_FIELD_NUMBER: builtins.int
    FROM_TIME_FIELD_NUMBER: builtins.int
    TO_TIME_FIELD_NUMBER: builtins.int
    RECORD_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Apache Kafka® cluster.

    To get the Apache Kafka® cluster ID, make a [ClusterService.List] request.
    """
    record_token: builtins.str
    """Record token.

    Set [record_token] to the [StreamLogRecord.next_record_token] returned by a previous [ClusterService.StreamLogs] request to start streaming from next log record.
    """
    filter: builtins.str
    """A filter expression that filters resources listed in the response.

    The expression must specify:
    1. The field name to filter by. Currently filtering can be applied to the `hostname` field.
    2. An `=` operator.
    3. The value in double quotes (`"`). Must be 3-63 characters long and match the regular expression `[a-z][-a-z0-9]{1,61}[a-z0-9]`.

    Example of a filter: `message.hostname='node1.db.cloud.yandex.net'`
    """
    @property
    def column_filter(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Columns from logs table to get in the response.

        If no columns are specified, full log records are returned.
        """

    @property
    def from_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Start timestamp for the logs request."""

    @property
    def to_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """End timestamp for the logs request.

        If this field is not set, all existing logs will be sent and then the new ones as they appear.
        In essence it has `tail -f` semantics.
        """

    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        column_filter: collections.abc.Iterable[builtins.str] | None = ...,
        from_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        to_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        record_token: builtins.str = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["from_time", b"from_time", "to_time", b"to_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "column_filter", b"column_filter", "filter", b"filter", "from_time", b"from_time", "record_token", b"record_token", "to_time", b"to_time"]) -> None: ...

global___StreamClusterLogsRequest = StreamClusterLogsRequest

@typing.final
class ListClusterOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Apache Kafka® cluster to list operations for."""
    page_size: builtins.int
    """The maximum number of results per page to return.

    If the number of available results is larger than [page_size], the service returns a [ListClusterOperationsResponse.next_page_token] that can be used to get the next page of results in subsequent list requests.
    """
    page_token: builtins.str
    """Page token.

    To get the next page of results, set [page_token] to the [ListClusterOperationsResponse.next_page_token] returned by the previous list request.
    """
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListClusterOperationsRequest = ListClusterOperationsRequest

@typing.final
class ListClusterOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token that allows you to get the next page of results for list requests.

    If the number of results is larger than [ListClusterOperationsRequest.page_size], use [next_page_token] as the value for the [ListClusterOperationsRequest.page_token] query parameter in the next list request.
    Each subsequent list request will have its own [next_page_token] to continue paging through the results.
    """
    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.operation.operation_pb2.Operation]:
        """List of operations for the specified Apache Kafka® cluster."""

    def __init__(
        self,
        *,
        operations: collections.abc.Iterable[yandex.cloud.operation.operation_pb2.Operation] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "operations", b"operations"]) -> None: ...

global___ListClusterOperationsResponse = ListClusterOperationsResponse

@typing.final
class ListClusterHostsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Apache Kafka® cluster.

    To get the Apache Kafka® cluster ID, make a [ClusterService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return.

    If the number of available results is larger than [page_size], the service returns a [ListClusterHostsResponse.next_page_token] that can be used to get the next page of results in subsequent list requests.
    """
    page_token: builtins.str
    """Page token.

    To get the next page of results, set [page_token] to the [ListClusterHostsResponse.next_page_token] returned by the previous list request.
    """
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListClusterHostsRequest = ListClusterHostsRequest

@typing.final
class ListClusterHostsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOSTS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token that allows you to get the next page of results for list requests.

    If the number of results is larger than [ListClusterHostsRequest.page_size], use the [next_page_token] as the value for the [ListClusterHostsRequest.page_token] query parameter in the next list request.
    Each subsequent list request will have its own [next_page_token] to continue paging through the results.
    """
    @property
    def hosts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.mdb.kafka.v1.cluster_pb2.Host]:
        """List of hosts."""

    def __init__(
        self,
        *,
        hosts: collections.abc.Iterable[yandex.cloud.mdb.kafka.v1.cluster_pb2.Host] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["hosts", b"hosts", "next_page_token", b"next_page_token"]) -> None: ...

global___ListClusterHostsResponse = ListClusterHostsResponse

@typing.final
class MoveClusterRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    DESTINATION_FOLDER_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Apache Kafka® cluster to move.

    To get the Apache Kafka® cluster ID, make a [ClusterService.List] request.
    """
    destination_folder_id: builtins.str
    """ID of the destination folder."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        destination_folder_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "destination_folder_id", b"destination_folder_id"]) -> None: ...

global___MoveClusterRequest = MoveClusterRequest

@typing.final
class MoveClusterMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    SOURCE_FOLDER_ID_FIELD_NUMBER: builtins.int
    DESTINATION_FOLDER_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Apache Kafka® cluster being moved."""
    source_folder_id: builtins.str
    """ID of the source folder."""
    destination_folder_id: builtins.str
    """ID of the destnation folder."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        source_folder_id: builtins.str = ...,
        destination_folder_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "destination_folder_id", b"destination_folder_id", "source_folder_id", b"source_folder_id"]) -> None: ...

global___MoveClusterMetadata = MoveClusterMetadata

@typing.final
class StartClusterRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Apache Kafka® cluster to start.

    To get the Apache Kafka® cluster ID, make a [ClusterService.List] request.
    """
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id"]) -> None: ...

global___StartClusterRequest = StartClusterRequest

@typing.final
class StartClusterMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Apache Kafka® cluster."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id"]) -> None: ...

global___StartClusterMetadata = StartClusterMetadata

@typing.final
class StopClusterRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Apache Kafka® cluster to stop.

    To get the Apache Kafka® cluster ID, make a [ClusterService.List] request.
    """
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id"]) -> None: ...

global___StopClusterRequest = StopClusterRequest

@typing.final
class StopClusterMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Apache Kafka® cluster."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id"]) -> None: ...

global___StopClusterMetadata = StopClusterMetadata

@typing.final
class RescheduleMaintenanceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _RescheduleType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _RescheduleTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[RescheduleMaintenanceRequest._RescheduleType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        RESCHEDULE_TYPE_UNSPECIFIED: RescheduleMaintenanceRequest._RescheduleType.ValueType  # 0
        IMMEDIATE: RescheduleMaintenanceRequest._RescheduleType.ValueType  # 1
        """Start the maintenance operation immediately."""
        NEXT_AVAILABLE_WINDOW: RescheduleMaintenanceRequest._RescheduleType.ValueType  # 2
        """Start the maintenance operation within the next available maintenance window."""
        SPECIFIC_TIME: RescheduleMaintenanceRequest._RescheduleType.ValueType  # 3
        """Start the maintenance operation at the specific time."""

    class RescheduleType(_RescheduleType, metaclass=_RescheduleTypeEnumTypeWrapper): ...
    RESCHEDULE_TYPE_UNSPECIFIED: RescheduleMaintenanceRequest.RescheduleType.ValueType  # 0
    IMMEDIATE: RescheduleMaintenanceRequest.RescheduleType.ValueType  # 1
    """Start the maintenance operation immediately."""
    NEXT_AVAILABLE_WINDOW: RescheduleMaintenanceRequest.RescheduleType.ValueType  # 2
    """Start the maintenance operation within the next available maintenance window."""
    SPECIFIC_TIME: RescheduleMaintenanceRequest.RescheduleType.ValueType  # 3
    """Start the maintenance operation at the specific time."""

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    RESCHEDULE_TYPE_FIELD_NUMBER: builtins.int
    DELAYED_UNTIL_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Kafka cluster to reschedule the maintenance operation for."""
    reschedule_type: global___RescheduleMaintenanceRequest.RescheduleType.ValueType
    """The type of reschedule request."""
    @property
    def delayed_until(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The time until which this maintenance operation should be delayed. The value should be ahead of the first time when the maintenance operation has been scheduled for no more than two weeks. The value can also point to the past moment of time if [reschedule_type.IMMEDIATE] reschedule type is chosen."""

    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        reschedule_type: global___RescheduleMaintenanceRequest.RescheduleType.ValueType = ...,
        delayed_until: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["delayed_until", b"delayed_until"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "delayed_until", b"delayed_until", "reschedule_type", b"reschedule_type"]) -> None: ...

global___RescheduleMaintenanceRequest = RescheduleMaintenanceRequest

@typing.final
class RescheduleMaintenanceMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    DELAYED_UNTIL_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Kafka cluster."""
    @property
    def delayed_until(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The time until which this maintenance operation is to be delayed."""

    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        delayed_until: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["delayed_until", b"delayed_until"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "delayed_until", b"delayed_until"]) -> None: ...

global___RescheduleMaintenanceMetadata = RescheduleMaintenanceMetadata
