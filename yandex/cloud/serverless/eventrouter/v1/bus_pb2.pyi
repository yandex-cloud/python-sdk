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
import yandex.cloud.logging.v1.log_entry_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class LogOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOG_GROUP_ID_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    MIN_LEVEL_FIELD_NUMBER: builtins.int
    SERVICE_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    log_group_id: builtins.str
    """Entry will be written to log group resolved by ID."""
    folder_id: builtins.str
    """Entry will be written to default log group for specified folder."""
    min_level: yandex.cloud.logging.v1.log_entry_pb2.LogLevel.Level.ValueType
    """Minimum log entry level.

    See [LogLevel.Level] for details.
    """
    service_account_id: builtins.str
    """Service account, which has permission to write to destination"""
    def __init__(
        self,
        *,
        log_group_id: builtins.str = ...,
        folder_id: builtins.str = ...,
        min_level: yandex.cloud.logging.v1.log_entry_pb2.LogLevel.Level.ValueType = ...,
        service_account_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["destination", b"destination", "folder_id", b"folder_id", "log_group_id", b"log_group_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["destination", b"destination", "folder_id", b"folder_id", "log_group_id", b"log_group_id", "min_level", b"min_level", "service_account_id", b"service_account_id"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["destination", b"destination"]) -> typing.Literal["log_group_id", "folder_id"] | None: ...

global___LogOptions = LogOptions

@typing.final
class Bus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Bus._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: Bus._Status.ValueType  # 0
        CREATING: Bus._Status.ValueType  # 1
        ACTIVE: Bus._Status.ValueType  # 2
        DELETING: Bus._Status.ValueType  # 3

    class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...
    STATUS_UNSPECIFIED: Bus.Status.ValueType  # 0
    CREATING: Bus.Status.ValueType  # 1
    ACTIVE: Bus.Status.ValueType  # 2
    DELETING: Bus.Status.ValueType  # 3

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
    CLOUD_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    DELETION_PROTECTION_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    LOGGING_ENABLED_FIELD_NUMBER: builtins.int
    LOG_OPTIONS_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the bus."""
    folder_id: builtins.str
    """ID of the folder that the bus belongs to."""
    cloud_id: builtins.str
    """ID of the cloud that the bus resides in."""
    name: builtins.str
    """Name of the bus."""
    description: builtins.str
    """Description of the bus."""
    deletion_protection: builtins.bool
    """Deletion protection."""
    status: global___Bus.Status.ValueType
    """Status of the bus."""
    logging_enabled: builtins.bool
    """Is logging from the bus enabled."""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `key:value` pairs."""

    @property
    def log_options(self) -> global___LogOptions:
        """Options for logging from the bus."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        folder_id: builtins.str = ...,
        cloud_id: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        deletion_protection: builtins.bool = ...,
        status: global___Bus.Status.ValueType = ...,
        logging_enabled: builtins.bool = ...,
        log_options: global___LogOptions | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at", "log_options", b"log_options"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cloud_id", b"cloud_id", "created_at", b"created_at", "deletion_protection", b"deletion_protection", "description", b"description", "folder_id", b"folder_id", "id", b"id", "labels", b"labels", "log_options", b"log_options", "logging_enabled", b"logging_enabled", "name", b"name", "status", b"status"]) -> None: ...

global___Bus = Bus
