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
class Workflow(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Workflow._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: Workflow._Status.ValueType  # 0
        CREATING: Workflow._Status.ValueType  # 1
        """Workflow is being created."""
        ACTIVE: Workflow._Status.ValueType  # 2
        """Workflow is ready for use."""
        UPDATING: Workflow._Status.ValueType  # 3
        """Workflow is being updated."""
        DELETING: Workflow._Status.ValueType  # 4
        """Workflow is being deleted."""
        ERROR: Workflow._Status.ValueType  # 5
        """Workflow failed. The only allowed action is delete."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...
    STATUS_UNSPECIFIED: Workflow.Status.ValueType  # 0
    CREATING: Workflow.Status.ValueType  # 1
    """Workflow is being created."""
    ACTIVE: Workflow.Status.ValueType  # 2
    """Workflow is ready for use."""
    UPDATING: Workflow.Status.ValueType  # 3
    """Workflow is being updated."""
    DELETING: Workflow.Status.ValueType  # 4
    """Workflow is being deleted."""
    ERROR: Workflow.Status.ValueType  # 5
    """Workflow failed. The only allowed action is delete."""

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
    SPECIFICATION_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    LOG_OPTIONS_FIELD_NUMBER: builtins.int
    NETWORK_ID_FIELD_NUMBER: builtins.int
    SERVICE_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    EXPRESS_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the Workflow. Generated at creation time."""
    folder_id: builtins.str
    """ID of the folder that the Workflow belongs to."""
    name: builtins.str
    """Name of the Workflow. The name is unique within the folder."""
    description: builtins.str
    """Description of the Workflow."""
    status: global___Workflow.Status.ValueType
    """Status of the Workflow."""
    network_id: builtins.str
    """ID of the VPC network Workflow will be executed in, in order to access private resources."""
    service_account_id: builtins.str
    """ID of the Service Account which will be used for resource access in Workflow execution."""
    express: builtins.bool
    """Express execution mode."""
    @property
    def specification(self) -> global___WorkflowSpecification:
        """Specification of the Workflow"""

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp for the Workflow."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Workflow labels as `key:value` pairs."""

    @property
    def log_options(self) -> global___LogOptions:
        """Options for logging from the Workflow."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        folder_id: builtins.str = ...,
        specification: global___WorkflowSpecification | None = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        status: global___Workflow.Status.ValueType = ...,
        log_options: global___LogOptions | None = ...,
        network_id: builtins.str = ...,
        service_account_id: builtins.str = ...,
        express: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at", "log_options", b"log_options", "specification", b"specification"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["created_at", b"created_at", "description", b"description", "express", b"express", "folder_id", b"folder_id", "id", b"id", "labels", b"labels", "log_options", b"log_options", "name", b"name", "network_id", b"network_id", "service_account_id", b"service_account_id", "specification", b"specification", "status", b"status"]) -> None: ...

global___Workflow = Workflow

@typing.final
class WorkflowPreview(google.protobuf.message.Message):
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

    ID_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    LOG_OPTIONS_FIELD_NUMBER: builtins.int
    NETWORK_ID_FIELD_NUMBER: builtins.int
    SERVICE_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    EXPRESS_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the Workflow. Generated at creation time."""
    folder_id: builtins.str
    """ID of the folder that the Workflow belongs to."""
    name: builtins.str
    """Name of the Workflow. The name is unique within the folder."""
    description: builtins.str
    """Description of the Workflow."""
    status: global___Workflow.Status.ValueType
    """Status of the Workflow."""
    network_id: builtins.str
    """ID of the VPC network Workflow will be executed in, in order to access private resources."""
    service_account_id: builtins.str
    """ID of the Service Account which will be used for resources access in Workflow execution."""
    express: builtins.bool
    """Express execution mode."""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp for the Workflow."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Workflow labels as `key:value` pairs."""

    @property
    def log_options(self) -> global___LogOptions:
        """Options for logging from the Workflow."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        folder_id: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        status: global___Workflow.Status.ValueType = ...,
        log_options: global___LogOptions | None = ...,
        network_id: builtins.str = ...,
        service_account_id: builtins.str = ...,
        express: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at", "log_options", b"log_options"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["created_at", b"created_at", "description", b"description", "express", b"express", "folder_id", b"folder_id", "id", b"id", "labels", b"labels", "log_options", b"log_options", "name", b"name", "network_id", b"network_id", "service_account_id", b"service_account_id", "status", b"status"]) -> None: ...

global___WorkflowPreview = WorkflowPreview

@typing.final
class WorkflowSpecification(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SPEC_YAML_FIELD_NUMBER: builtins.int
    spec_yaml: builtins.str
    """Workflow specification in YAML format."""
    def __init__(
        self,
        *,
        spec_yaml: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["spec", b"spec", "spec_yaml", b"spec_yaml"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["spec", b"spec", "spec_yaml", b"spec_yaml"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["spec", b"spec"]) -> typing.Literal["spec_yaml"] | None: ...

global___WorkflowSpecification = WorkflowSpecification

@typing.final
class LogOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DISABLED_FIELD_NUMBER: builtins.int
    LOG_GROUP_ID_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    MIN_LEVEL_FIELD_NUMBER: builtins.int
    disabled: builtins.bool
    """Is logging from Workflow disabled."""
    log_group_id: builtins.str
    """ID of the logging group which should be used for Workflows logs."""
    folder_id: builtins.str
    """ID of the folder which default logging group should be used for Workflows."""
    min_level: yandex.cloud.logging.v1.log_entry_pb2.LogLevel.Level.ValueType
    """Minimum logs level.

    See [LogLevel.Level] for details.
    """
    def __init__(
        self,
        *,
        disabled: builtins.bool = ...,
        log_group_id: builtins.str = ...,
        folder_id: builtins.str = ...,
        min_level: yandex.cloud.logging.v1.log_entry_pb2.LogLevel.Level.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["destination", b"destination", "folder_id", b"folder_id", "log_group_id", b"log_group_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["destination", b"destination", "disabled", b"disabled", "folder_id", b"folder_id", "log_group_id", b"log_group_id", "min_level", b"min_level"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["destination", b"destination"]) -> typing.Literal["log_group_id", "folder_id"] | None: ...

global___LogOptions = LogOptions
