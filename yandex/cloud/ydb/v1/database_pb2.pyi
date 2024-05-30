"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys
import typing
import yandex.cloud.ydb.v1.backup_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _AlertEvaluationStatus:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _AlertEvaluationStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_AlertEvaluationStatus.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    ALERT_EVALUATION_STATUS_UNSPECIFIED: _AlertEvaluationStatus.ValueType  # 0
    ALERT_EVALUATION_STATUS_OK: _AlertEvaluationStatus.ValueType  # 1
    ALERT_EVALUATION_STATUS_NO_DATA: _AlertEvaluationStatus.ValueType  # 2
    ALERT_EVALUATION_STATUS_ERROR: _AlertEvaluationStatus.ValueType  # 3
    ALERT_EVALUATION_STATUS_ALARM: _AlertEvaluationStatus.ValueType  # 4
    ALERT_EVALUATION_STATUS_WARN: _AlertEvaluationStatus.ValueType  # 5

class AlertEvaluationStatus(_AlertEvaluationStatus, metaclass=_AlertEvaluationStatusEnumTypeWrapper): ...

ALERT_EVALUATION_STATUS_UNSPECIFIED: AlertEvaluationStatus.ValueType  # 0
ALERT_EVALUATION_STATUS_OK: AlertEvaluationStatus.ValueType  # 1
ALERT_EVALUATION_STATUS_NO_DATA: AlertEvaluationStatus.ValueType  # 2
ALERT_EVALUATION_STATUS_ERROR: AlertEvaluationStatus.ValueType  # 3
ALERT_EVALUATION_STATUS_ALARM: AlertEvaluationStatus.ValueType  # 4
ALERT_EVALUATION_STATUS_WARN: AlertEvaluationStatus.ValueType  # 5
global___AlertEvaluationStatus = AlertEvaluationStatus

@typing.final
class Database(google.protobuf.message.Message):
    """YDB database."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Database._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: Database._Status.ValueType  # 0
        PROVISIONING: Database._Status.ValueType  # 1
        RUNNING: Database._Status.ValueType  # 2
        UPDATING: Database._Status.ValueType  # 4
        ERROR: Database._Status.ValueType  # 5
        DELETING: Database._Status.ValueType  # 6
        STARTING: Database._Status.ValueType  # 7
        STOPPED: Database._Status.ValueType  # 8

    class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...
    STATUS_UNSPECIFIED: Database.Status.ValueType  # 0
    PROVISIONING: Database.Status.ValueType  # 1
    RUNNING: Database.Status.ValueType  # 2
    UPDATING: Database.Status.ValueType  # 4
    ERROR: Database.Status.ValueType  # 5
    DELETING: Database.Status.ValueType  # 6
    STARTING: Database.Status.ValueType  # 7
    STOPPED: Database.Status.ValueType  # 8

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

    ID_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    ENDPOINT_FIELD_NUMBER: builtins.int
    RESOURCE_PRESET_ID_FIELD_NUMBER: builtins.int
    STORAGE_CONFIG_FIELD_NUMBER: builtins.int
    SCALE_POLICY_FIELD_NUMBER: builtins.int
    NETWORK_ID_FIELD_NUMBER: builtins.int
    SUBNET_IDS_FIELD_NUMBER: builtins.int
    ZONAL_DATABASE_FIELD_NUMBER: builtins.int
    REGIONAL_DATABASE_FIELD_NUMBER: builtins.int
    DEDICATED_DATABASE_FIELD_NUMBER: builtins.int
    SERVERLESS_DATABASE_FIELD_NUMBER: builtins.int
    ASSIGN_PUBLIC_IPS_FIELD_NUMBER: builtins.int
    LOCATION_ID_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    BACKUP_CONFIG_FIELD_NUMBER: builtins.int
    DOCUMENT_API_ENDPOINT_FIELD_NUMBER: builtins.int
    KINESIS_API_ENDPOINT_FIELD_NUMBER: builtins.int
    KAFKA_API_ENDPOINT_FIELD_NUMBER: builtins.int
    MONITORING_CONFIG_FIELD_NUMBER: builtins.int
    DELETION_PROTECTION_FIELD_NUMBER: builtins.int
    id: builtins.str
    folder_id: builtins.str
    name: builtins.str
    description: builtins.str
    status: global___Database.Status.ValueType
    endpoint: builtins.str
    resource_preset_id: builtins.str
    network_id: builtins.str
    assign_public_ips: builtins.bool
    location_id: builtins.str
    document_api_endpoint: builtins.str
    kinesis_api_endpoint: builtins.str
    kafka_api_endpoint: builtins.str
    deletion_protection: builtins.bool
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def storage_config(self) -> global___StorageConfig: ...
    @property
    def scale_policy(self) -> global___ScalePolicy: ...
    @property
    def subnet_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def zonal_database(self) -> global___ZonalDatabase:
        """deprecated field"""

    @property
    def regional_database(self) -> global___RegionalDatabase:
        """deprecated field"""

    @property
    def dedicated_database(self) -> global___DedicatedDatabase: ...
    @property
    def serverless_database(self) -> global___ServerlessDatabase: ...
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    @property
    def backup_config(self) -> yandex.cloud.ydb.v1.backup_pb2.BackupConfig: ...
    @property
    def monitoring_config(self) -> global___MonitoringConfig: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        folder_id: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        status: global___Database.Status.ValueType = ...,
        endpoint: builtins.str = ...,
        resource_preset_id: builtins.str = ...,
        storage_config: global___StorageConfig | None = ...,
        scale_policy: global___ScalePolicy | None = ...,
        network_id: builtins.str = ...,
        subnet_ids: collections.abc.Iterable[builtins.str] | None = ...,
        zonal_database: global___ZonalDatabase | None = ...,
        regional_database: global___RegionalDatabase | None = ...,
        dedicated_database: global___DedicatedDatabase | None = ...,
        serverless_database: global___ServerlessDatabase | None = ...,
        assign_public_ips: builtins.bool = ...,
        location_id: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        backup_config: yandex.cloud.ydb.v1.backup_pb2.BackupConfig | None = ...,
        document_api_endpoint: builtins.str = ...,
        kinesis_api_endpoint: builtins.str = ...,
        kafka_api_endpoint: builtins.str = ...,
        monitoring_config: global___MonitoringConfig | None = ...,
        deletion_protection: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["backup_config", b"backup_config", "created_at", b"created_at", "database_type", b"database_type", "dedicated_database", b"dedicated_database", "monitoring_config", b"monitoring_config", "regional_database", b"regional_database", "scale_policy", b"scale_policy", "serverless_database", b"serverless_database", "storage_config", b"storage_config", "zonal_database", b"zonal_database"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["assign_public_ips", b"assign_public_ips", "backup_config", b"backup_config", "created_at", b"created_at", "database_type", b"database_type", "dedicated_database", b"dedicated_database", "deletion_protection", b"deletion_protection", "description", b"description", "document_api_endpoint", b"document_api_endpoint", "endpoint", b"endpoint", "folder_id", b"folder_id", "id", b"id", "kafka_api_endpoint", b"kafka_api_endpoint", "kinesis_api_endpoint", b"kinesis_api_endpoint", "labels", b"labels", "location_id", b"location_id", "monitoring_config", b"monitoring_config", "name", b"name", "network_id", b"network_id", "regional_database", b"regional_database", "resource_preset_id", b"resource_preset_id", "scale_policy", b"scale_policy", "serverless_database", b"serverless_database", "status", b"status", "storage_config", b"storage_config", "subnet_ids", b"subnet_ids", "zonal_database", b"zonal_database"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["database_type", b"database_type"]) -> typing.Literal["zonal_database", "regional_database", "dedicated_database", "serverless_database"] | None: ...

global___Database = Database

@typing.final
class AlertParameter(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class DoubleParameterValue(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        NAME_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        name: builtins.str
        """Required. Parameter name"""
        value: builtins.float
        """Required. Parameter value"""
        def __init__(
            self,
            *,
            name: builtins.str = ...,
            value: builtins.float = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["name", b"name", "value", b"value"]) -> None: ...

    @typing.final
    class IntegerParameterValue(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        NAME_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        name: builtins.str
        """Required. Parameter name"""
        value: builtins.int
        """Required. Parameter value"""
        def __init__(
            self,
            *,
            name: builtins.str = ...,
            value: builtins.int = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["name", b"name", "value", b"value"]) -> None: ...

    @typing.final
    class TextParameterValue(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        NAME_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        name: builtins.str
        """Required. Parameter name"""
        value: builtins.str
        """Required. Parameter value"""
        def __init__(
            self,
            *,
            name: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["name", b"name", "value", b"value"]) -> None: ...

    @typing.final
    class TextListParameterValue(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        NAME_FIELD_NUMBER: builtins.int
        VALUES_FIELD_NUMBER: builtins.int
        name: builtins.str
        """Required. Parameter name"""
        @property
        def values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
            """Required. Parameter value"""

        def __init__(
            self,
            *,
            name: builtins.str = ...,
            values: collections.abc.Iterable[builtins.str] | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["name", b"name", "values", b"values"]) -> None: ...

    @typing.final
    class LabelListParameterValue(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        NAME_FIELD_NUMBER: builtins.int
        VALUES_FIELD_NUMBER: builtins.int
        name: builtins.str
        """Required. Parameter name"""
        @property
        def values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
            """Required. Parameter value"""

        def __init__(
            self,
            *,
            name: builtins.str = ...,
            values: collections.abc.Iterable[builtins.str] | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["name", b"name", "values", b"values"]) -> None: ...

    DOUBLE_PARAMETER_VALUE_FIELD_NUMBER: builtins.int
    INTEGER_PARAMETER_VALUE_FIELD_NUMBER: builtins.int
    TEXT_PARAMETER_VALUE_FIELD_NUMBER: builtins.int
    TEXT_LIST_PARAMETER_VALUE_FIELD_NUMBER: builtins.int
    LABEL_LIST_PARAMETER_VALUE_FIELD_NUMBER: builtins.int
    @property
    def double_parameter_value(self) -> global___AlertParameter.DoubleParameterValue: ...
    @property
    def integer_parameter_value(self) -> global___AlertParameter.IntegerParameterValue: ...
    @property
    def text_parameter_value(self) -> global___AlertParameter.TextParameterValue: ...
    @property
    def text_list_parameter_value(self) -> global___AlertParameter.TextListParameterValue: ...
    @property
    def label_list_parameter_value(self) -> global___AlertParameter.LabelListParameterValue: ...
    def __init__(
        self,
        *,
        double_parameter_value: global___AlertParameter.DoubleParameterValue | None = ...,
        integer_parameter_value: global___AlertParameter.IntegerParameterValue | None = ...,
        text_parameter_value: global___AlertParameter.TextParameterValue | None = ...,
        text_list_parameter_value: global___AlertParameter.TextListParameterValue | None = ...,
        label_list_parameter_value: global___AlertParameter.LabelListParameterValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["double_parameter_value", b"double_parameter_value", "integer_parameter_value", b"integer_parameter_value", "label_list_parameter_value", b"label_list_parameter_value", "parameter", b"parameter", "text_list_parameter_value", b"text_list_parameter_value", "text_parameter_value", b"text_parameter_value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["double_parameter_value", b"double_parameter_value", "integer_parameter_value", b"integer_parameter_value", "label_list_parameter_value", b"label_list_parameter_value", "parameter", b"parameter", "text_list_parameter_value", b"text_list_parameter_value", "text_parameter_value", b"text_parameter_value"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["parameter", b"parameter"]) -> typing.Literal["double_parameter_value", "integer_parameter_value", "text_parameter_value", "text_list_parameter_value", "label_list_parameter_value"] | None: ...

global___AlertParameter = AlertParameter

@typing.final
class NotificationChannel(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NOTIFICATION_CHANNEL_ID_FIELD_NUMBER: builtins.int
    NOTIFY_ABOUT_STATUSES_FIELD_NUMBER: builtins.int
    REPEATE_NOTIFY_DELAY_MS_FIELD_NUMBER: builtins.int
    notification_channel_id: builtins.str
    repeate_notify_delay_ms: builtins.int
    @property
    def notify_about_statuses(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[global___AlertEvaluationStatus.ValueType]: ...
    def __init__(
        self,
        *,
        notification_channel_id: builtins.str = ...,
        notify_about_statuses: collections.abc.Iterable[global___AlertEvaluationStatus.ValueType] | None = ...,
        repeate_notify_delay_ms: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["notification_channel_id", b"notification_channel_id", "notify_about_statuses", b"notify_about_statuses", "repeate_notify_delay_ms", b"repeate_notify_delay_ms"]) -> None: ...

global___NotificationChannel = NotificationChannel

@typing.final
class Alert(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ALERT_ID_FIELD_NUMBER: builtins.int
    ALERT_TEMPLATE_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    NOTIFICATION_CHANNELS_FIELD_NUMBER: builtins.int
    ALERT_PARAMETERS_FIELD_NUMBER: builtins.int
    ALERT_THRESHOLDS_FIELD_NUMBER: builtins.int
    alert_id: builtins.str
    """output only field."""
    alert_template_id: builtins.str
    """template of the alert."""
    name: builtins.str
    """name of the alert."""
    description: builtins.str
    """human readable description of the alert."""
    @property
    def notification_channels(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___NotificationChannel]:
        """the notification channels of the alert."""

    @property
    def alert_parameters(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AlertParameter]:
        """alert parameters to override."""

    @property
    def alert_thresholds(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AlertParameter]:
        """alert paratemers to override."""

    def __init__(
        self,
        *,
        alert_id: builtins.str = ...,
        alert_template_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        notification_channels: collections.abc.Iterable[global___NotificationChannel] | None = ...,
        alert_parameters: collections.abc.Iterable[global___AlertParameter] | None = ...,
        alert_thresholds: collections.abc.Iterable[global___AlertParameter] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["alert_id", b"alert_id", "alert_parameters", b"alert_parameters", "alert_template_id", b"alert_template_id", "alert_thresholds", b"alert_thresholds", "description", b"description", "name", b"name", "notification_channels", b"notification_channels"]) -> None: ...

global___Alert = Alert

@typing.final
class MonitoringConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ALERTS_FIELD_NUMBER: builtins.int
    @property
    def alerts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Alert]: ...
    def __init__(
        self,
        *,
        alerts: collections.abc.Iterable[global___Alert] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["alerts", b"alerts"]) -> None: ...

global___MonitoringConfig = MonitoringConfig

@typing.final
class DedicatedDatabase(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_PRESET_ID_FIELD_NUMBER: builtins.int
    STORAGE_CONFIG_FIELD_NUMBER: builtins.int
    SCALE_POLICY_FIELD_NUMBER: builtins.int
    NETWORK_ID_FIELD_NUMBER: builtins.int
    SUBNET_IDS_FIELD_NUMBER: builtins.int
    ASSIGN_PUBLIC_IPS_FIELD_NUMBER: builtins.int
    resource_preset_id: builtins.str
    network_id: builtins.str
    assign_public_ips: builtins.bool
    @property
    def storage_config(self) -> global___StorageConfig: ...
    @property
    def scale_policy(self) -> global___ScalePolicy: ...
    @property
    def subnet_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        resource_preset_id: builtins.str = ...,
        storage_config: global___StorageConfig | None = ...,
        scale_policy: global___ScalePolicy | None = ...,
        network_id: builtins.str = ...,
        subnet_ids: collections.abc.Iterable[builtins.str] | None = ...,
        assign_public_ips: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["scale_policy", b"scale_policy", "storage_config", b"storage_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["assign_public_ips", b"assign_public_ips", "network_id", b"network_id", "resource_preset_id", b"resource_preset_id", "scale_policy", b"scale_policy", "storage_config", b"storage_config", "subnet_ids", b"subnet_ids"]) -> None: ...

global___DedicatedDatabase = DedicatedDatabase

@typing.final
class ServerlessDatabase(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    THROTTLING_RCU_LIMIT_FIELD_NUMBER: builtins.int
    STORAGE_SIZE_LIMIT_FIELD_NUMBER: builtins.int
    ENABLE_THROTTLING_RCU_LIMIT_FIELD_NUMBER: builtins.int
    PROVISIONED_RCU_LIMIT_FIELD_NUMBER: builtins.int
    TOPIC_WRITE_QUOTA_FIELD_NUMBER: builtins.int
    throttling_rcu_limit: builtins.int
    """Let's define 1 RU  - 1 request unit
    Let's define 1 RCU - 1 request capacity unit, which is 1 RU per second.
    If `enable_throttling_rcu_limit` flag is true, the database will be throttled using `throttling_rcu_limit` value.
    Otherwise, the database is throttled using the cloud quotas.
    If zero, all requests will be blocked until non zero value is set.
    """
    storage_size_limit: builtins.int
    """Specify serverless database storage size limit. If zero, default value is applied."""
    enable_throttling_rcu_limit: builtins.bool
    """If false, the database is throttled by cloud value."""
    provisioned_rcu_limit: builtins.int
    """Specify the number of provisioned RCUs to pay less if the database has predictable load.
    You will be charged for the provisioned capacity regularly even if this capacity is not fully consumed.
    You will be charged for the on-demand consumption only if provisioned capacity is consumed.
    """
    topic_write_quota: builtins.int
    """write quota for topic service, defined in bytes per second."""
    def __init__(
        self,
        *,
        throttling_rcu_limit: builtins.int = ...,
        storage_size_limit: builtins.int = ...,
        enable_throttling_rcu_limit: builtins.bool = ...,
        provisioned_rcu_limit: builtins.int = ...,
        topic_write_quota: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["enable_throttling_rcu_limit", b"enable_throttling_rcu_limit", "provisioned_rcu_limit", b"provisioned_rcu_limit", "storage_size_limit", b"storage_size_limit", "throttling_rcu_limit", b"throttling_rcu_limit", "topic_write_quota", b"topic_write_quota"]) -> None: ...

global___ServerlessDatabase = ServerlessDatabase

@typing.final
class ZonalDatabase(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ZONE_ID_FIELD_NUMBER: builtins.int
    zone_id: builtins.str
    def __init__(
        self,
        *,
        zone_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["zone_id", b"zone_id"]) -> None: ...

global___ZonalDatabase = ZonalDatabase

@typing.final
class RegionalDatabase(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REGION_ID_FIELD_NUMBER: builtins.int
    region_id: builtins.str
    def __init__(
        self,
        *,
        region_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["region_id", b"region_id"]) -> None: ...

global___RegionalDatabase = RegionalDatabase

@typing.final
class ScalePolicy(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class FixedScale(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        SIZE_FIELD_NUMBER: builtins.int
        size: builtins.int
        def __init__(
            self,
            *,
            size: builtins.int = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["size", b"size"]) -> None: ...

    FIXED_SCALE_FIELD_NUMBER: builtins.int
    @property
    def fixed_scale(self) -> global___ScalePolicy.FixedScale: ...
    def __init__(
        self,
        *,
        fixed_scale: global___ScalePolicy.FixedScale | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["fixed_scale", b"fixed_scale", "scale_type", b"scale_type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["fixed_scale", b"fixed_scale", "scale_type", b"scale_type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["scale_type", b"scale_type"]) -> typing.Literal["fixed_scale"] | None: ...

global___ScalePolicy = ScalePolicy

@typing.final
class StorageConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STORAGE_OPTIONS_FIELD_NUMBER: builtins.int
    STORAGE_SIZE_LIMIT_FIELD_NUMBER: builtins.int
    storage_size_limit: builtins.int
    """output only field: storage size limit of dedicated database."""
    @property
    def storage_options(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StorageOption]: ...
    def __init__(
        self,
        *,
        storage_options: collections.abc.Iterable[global___StorageOption] | None = ...,
        storage_size_limit: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["storage_options", b"storage_options", "storage_size_limit", b"storage_size_limit"]) -> None: ...

global___StorageConfig = StorageConfig

@typing.final
class StorageOption(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STORAGE_TYPE_ID_FIELD_NUMBER: builtins.int
    GROUP_COUNT_FIELD_NUMBER: builtins.int
    storage_type_id: builtins.str
    group_count: builtins.int
    def __init__(
        self,
        *,
        storage_type_id: builtins.str = ...,
        group_count: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["group_count", b"group_count", "storage_type_id", b"storage_type_id"]) -> None: ...

global___StorageOption = StorageOption
