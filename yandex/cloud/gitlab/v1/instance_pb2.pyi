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
import yandex.cloud.gitlab.v1.maintenance_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Instance(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Instance._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: Instance._Status.ValueType  # 0
        CREATING: Instance._Status.ValueType  # 1
        RUNNING: Instance._Status.ValueType  # 2
        UPDATING: Instance._Status.ValueType  # 3
        ERROR: Instance._Status.ValueType  # 4
        DELETING: Instance._Status.ValueType  # 5
        BACKUP_CREATING: Instance._Status.ValueType  # 6
        BACKUP_RESTORING: Instance._Status.ValueType  # 7
        STARTING: Instance._Status.ValueType  # 8
        STOPPING: Instance._Status.ValueType  # 9
        STOPPED: Instance._Status.ValueType  # 10
        BACKGROUND_MIGRATIONS: Instance._Status.ValueType  # 11
        OBJECT_STORAGE_MIGRATIONS: Instance._Status.ValueType  # 12
        SNAPSHOT_RESTORING: Instance._Status.ValueType  # 13

    class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...
    STATUS_UNSPECIFIED: Instance.Status.ValueType  # 0
    CREATING: Instance.Status.ValueType  # 1
    RUNNING: Instance.Status.ValueType  # 2
    UPDATING: Instance.Status.ValueType  # 3
    ERROR: Instance.Status.ValueType  # 4
    DELETING: Instance.Status.ValueType  # 5
    BACKUP_CREATING: Instance.Status.ValueType  # 6
    BACKUP_RESTORING: Instance.Status.ValueType  # 7
    STARTING: Instance.Status.ValueType  # 8
    STOPPING: Instance.Status.ValueType  # 9
    STOPPED: Instance.Status.ValueType  # 10
    BACKGROUND_MIGRATIONS: Instance.Status.ValueType  # 11
    OBJECT_STORAGE_MIGRATIONS: Instance.Status.ValueType  # 12
    SNAPSHOT_RESTORING: Instance.Status.ValueType  # 13

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
    UPDATED_AT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    RESOURCE_PRESET_ID_FIELD_NUMBER: builtins.int
    DISK_SIZE_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    ADMIN_LOGIN_FIELD_NUMBER: builtins.int
    ADMIN_EMAIL_FIELD_NUMBER: builtins.int
    DOMAIN_FIELD_NUMBER: builtins.int
    SUBNET_ID_FIELD_NUMBER: builtins.int
    PLANNED_OPERATION_FIELD_NUMBER: builtins.int
    BACKUP_RETAIN_PERIOD_DAYS_FIELD_NUMBER: builtins.int
    MAINTENANCE_DELETE_UNTAGGED_FIELD_NUMBER: builtins.int
    DELETION_PROTECTION_FIELD_NUMBER: builtins.int
    APPROVAL_RULES_ID_FIELD_NUMBER: builtins.int
    GITLAB_VERSION_FIELD_NUMBER: builtins.int
    id: builtins.str
    folder_id: builtins.str
    name: builtins.str
    description: builtins.str
    resource_preset_id: builtins.str
    disk_size: builtins.int
    status: global___Instance.Status.ValueType
    admin_login: builtins.str
    admin_email: builtins.str
    domain: builtins.str
    subnet_id: builtins.str
    backup_retain_period_days: builtins.int
    maintenance_delete_untagged: builtins.bool
    deletion_protection: builtins.bool
    approval_rules_id: builtins.str
    gitlab_version: builtins.str
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def updated_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    @property
    def planned_operation(self) -> yandex.cloud.gitlab.v1.maintenance_pb2.MaintenanceOperation: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        folder_id: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        updated_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        resource_preset_id: builtins.str = ...,
        disk_size: builtins.int = ...,
        status: global___Instance.Status.ValueType = ...,
        admin_login: builtins.str = ...,
        admin_email: builtins.str = ...,
        domain: builtins.str = ...,
        subnet_id: builtins.str = ...,
        planned_operation: yandex.cloud.gitlab.v1.maintenance_pb2.MaintenanceOperation | None = ...,
        backup_retain_period_days: builtins.int = ...,
        maintenance_delete_untagged: builtins.bool = ...,
        deletion_protection: builtins.bool = ...,
        approval_rules_id: builtins.str = ...,
        gitlab_version: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at", "planned_operation", b"planned_operation", "updated_at", b"updated_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["admin_email", b"admin_email", "admin_login", b"admin_login", "approval_rules_id", b"approval_rules_id", "backup_retain_period_days", b"backup_retain_period_days", "created_at", b"created_at", "deletion_protection", b"deletion_protection", "description", b"description", "disk_size", b"disk_size", "domain", b"domain", "folder_id", b"folder_id", "gitlab_version", b"gitlab_version", "id", b"id", "labels", b"labels", "maintenance_delete_untagged", b"maintenance_delete_untagged", "name", b"name", "planned_operation", b"planned_operation", "resource_preset_id", b"resource_preset_id", "status", b"status", "subnet_id", b"subnet_id", "updated_at", b"updated_at"]) -> None: ...

global___Instance = Instance
