"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import google.protobuf.wrappers_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Project(google.protobuf.message.Message):
    """A Project resource."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Settings(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        class _Ide:
            ValueType = typing.NewType("ValueType", builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _IdeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Project.Settings._Ide.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            IDE_UNSPECIFIED: Project.Settings._Ide.ValueType  # 0
            JUPYTER_LAB: Project.Settings._Ide.ValueType  # 1
            """Project running on JupyterLab IDE."""

        class Ide(_Ide, metaclass=_IdeEnumTypeWrapper): ...
        IDE_UNSPECIFIED: Project.Settings.Ide.ValueType  # 0
        JUPYTER_LAB: Project.Settings.Ide.ValueType  # 1
        """Project running on JupyterLab IDE."""

        class _StaleExecutionTimeoutMode:
            ValueType = typing.NewType("ValueType", builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _StaleExecutionTimeoutModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Project.Settings._StaleExecutionTimeoutMode.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            STALE_EXECUTION_TIMEOUT_MODE_UNSPECIFIED: Project.Settings._StaleExecutionTimeoutMode.ValueType  # 0
            ONE_HOUR: Project.Settings._StaleExecutionTimeoutMode.ValueType  # 1
            """Setting to automatically stop stale execution after one hour with low consumption."""
            THREE_HOURS: Project.Settings._StaleExecutionTimeoutMode.ValueType  # 2
            """Setting to automatically stop stale execution after three hours with low consumption."""
            NO_TIMEOUT: Project.Settings._StaleExecutionTimeoutMode.ValueType  # 3
            """Setting to never automatically stop stale executions."""

        class StaleExecutionTimeoutMode(_StaleExecutionTimeoutMode, metaclass=_StaleExecutionTimeoutModeEnumTypeWrapper): ...
        STALE_EXECUTION_TIMEOUT_MODE_UNSPECIFIED: Project.Settings.StaleExecutionTimeoutMode.ValueType  # 0
        ONE_HOUR: Project.Settings.StaleExecutionTimeoutMode.ValueType  # 1
        """Setting to automatically stop stale execution after one hour with low consumption."""
        THREE_HOURS: Project.Settings.StaleExecutionTimeoutMode.ValueType  # 2
        """Setting to automatically stop stale execution after three hours with low consumption."""
        NO_TIMEOUT: Project.Settings.StaleExecutionTimeoutMode.ValueType  # 3
        """Setting to never automatically stop stale executions."""

        SERVICE_ACCOUNT_ID_FIELD_NUMBER: builtins.int
        SUBNET_ID_FIELD_NUMBER: builtins.int
        DATA_PROC_CLUSTER_ID_FIELD_NUMBER: builtins.int
        SECURITY_GROUP_IDS_FIELD_NUMBER: builtins.int
        EARLY_ACCESS_FIELD_NUMBER: builtins.int
        IDE_FIELD_NUMBER: builtins.int
        DEFAULT_FOLDER_ID_FIELD_NUMBER: builtins.int
        STALE_EXEC_TIMEOUT_MODE_FIELD_NUMBER: builtins.int
        VM_INACTIVITY_TIMEOUT_FIELD_NUMBER: builtins.int
        DEFAULT_DEDICATED_SPEC_FIELD_NUMBER: builtins.int
        service_account_id: builtins.str
        """ID of the service account, on whose behalf all operations with clusters will be performed."""
        subnet_id: builtins.str
        """ID of the subnet where the DataProc cluster resides.
        Currently only subnets created in the availability zone ru-central1-a are supported.
        """
        data_proc_cluster_id: builtins.str
        """ID of the DataProc cluster."""
        early_access: builtins.bool
        """Is early access preview enabled for the project."""
        ide: global___Project.Settings.Ide.ValueType
        """Project IDE."""
        default_folder_id: builtins.str
        """Default project folder ID."""
        stale_exec_timeout_mode: global___Project.Settings.StaleExecutionTimeoutMode.ValueType
        """Timeout to automatically stop stale executions."""
        default_dedicated_spec: builtins.str
        """Default VM configuration for DEDICATED mode."""
        @property
        def security_group_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
            """Network interfaces security groups."""

        @property
        def vm_inactivity_timeout(self) -> google.protobuf.duration_pb2.Duration:
            """Timeout for VM deallocation."""

        def __init__(
            self,
            *,
            service_account_id: builtins.str = ...,
            subnet_id: builtins.str = ...,
            data_proc_cluster_id: builtins.str = ...,
            security_group_ids: collections.abc.Iterable[builtins.str] | None = ...,
            early_access: builtins.bool = ...,
            ide: global___Project.Settings.Ide.ValueType = ...,
            default_folder_id: builtins.str = ...,
            stale_exec_timeout_mode: global___Project.Settings.StaleExecutionTimeoutMode.ValueType = ...,
            vm_inactivity_timeout: google.protobuf.duration_pb2.Duration | None = ...,
            default_dedicated_spec: builtins.str = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["vm_inactivity_timeout", b"vm_inactivity_timeout"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["data_proc_cluster_id", b"data_proc_cluster_id", "default_dedicated_spec", b"default_dedicated_spec", "default_folder_id", b"default_folder_id", "early_access", b"early_access", "ide", b"ide", "security_group_ids", b"security_group_ids", "service_account_id", b"service_account_id", "stale_exec_timeout_mode", b"stale_exec_timeout_mode", "subnet_id", b"subnet_id", "vm_inactivity_timeout", b"vm_inactivity_timeout"]) -> None: ...

    @typing.final
    class Limits(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        MAX_UNITS_PER_HOUR_FIELD_NUMBER: builtins.int
        MAX_UNITS_PER_EXECUTION_FIELD_NUMBER: builtins.int
        @property
        def max_units_per_hour(self) -> google.protobuf.wrappers_pb2.Int64Value:
            """The number of units that can be spent per hour."""

        @property
        def max_units_per_execution(self) -> google.protobuf.wrappers_pb2.Int64Value:
            """The number of units that can be spent on the one execution."""

        def __init__(
            self,
            *,
            max_units_per_hour: google.protobuf.wrappers_pb2.Int64Value | None = ...,
            max_units_per_execution: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["max_units_per_execution", b"max_units_per_execution", "max_units_per_hour", b"max_units_per_hour"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["max_units_per_execution", b"max_units_per_execution", "max_units_per_hour", b"max_units_per_hour"]) -> None: ...

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
    CREATED_AT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    CREATED_BY_ID_FIELD_NUMBER: builtins.int
    SETTINGS_FIELD_NUMBER: builtins.int
    LIMITS_FIELD_NUMBER: builtins.int
    COMMUNITY_ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the project."""
    name: builtins.str
    """Name of the project. 1-63 characters long."""
    description: builtins.str
    """Description of the project. 0-256 characters long."""
    created_by_id: builtins.str
    community_id: builtins.str
    """ID of the community that the project belongs to."""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    @property
    def settings(self) -> global___Project.Settings:
        """Settings of the project."""

    @property
    def limits(self) -> global___Project.Limits:
        """Limits of the project."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        created_by_id: builtins.str = ...,
        settings: global___Project.Settings | None = ...,
        limits: global___Project.Limits | None = ...,
        community_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at", "limits", b"limits", "settings", b"settings"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["community_id", b"community_id", "created_at", b"created_at", "created_by_id", b"created_by_id", "description", b"description", "id", b"id", "labels", b"labels", "limits", b"limits", "name", b"name", "settings", b"settings"]) -> None: ...

global___Project = Project
