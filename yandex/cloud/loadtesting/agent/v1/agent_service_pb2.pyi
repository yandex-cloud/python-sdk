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

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class ClaimAgentStatusRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ClaimAgentStatusRequest._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: ClaimAgentStatusRequest._Status.ValueType  # 0
        READY_FOR_TEST: ClaimAgentStatusRequest._Status.ValueType  # 1
        PREPARING_TEST: ClaimAgentStatusRequest._Status.ValueType  # 2
        TESTING: ClaimAgentStatusRequest._Status.ValueType  # 3
        TANK_FAILED: ClaimAgentStatusRequest._Status.ValueType  # 4
        STOPPED: ClaimAgentStatusRequest._Status.ValueType  # 5
        UPLOADING_ARTIFACTS: ClaimAgentStatusRequest._Status.ValueType  # 6
        ERROR: ClaimAgentStatusRequest._Status.ValueType  # 7

    class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...
    STATUS_UNSPECIFIED: ClaimAgentStatusRequest.Status.ValueType  # 0
    READY_FOR_TEST: ClaimAgentStatusRequest.Status.ValueType  # 1
    PREPARING_TEST: ClaimAgentStatusRequest.Status.ValueType  # 2
    TESTING: ClaimAgentStatusRequest.Status.ValueType  # 3
    TANK_FAILED: ClaimAgentStatusRequest.Status.ValueType  # 4
    STOPPED: ClaimAgentStatusRequest.Status.ValueType  # 5
    UPLOADING_ARTIFACTS: ClaimAgentStatusRequest.Status.ValueType  # 6
    ERROR: ClaimAgentStatusRequest.Status.ValueType  # 7

    AGENT_INSTANCE_ID_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    STATUS_MESSAGE_FIELD_NUMBER: builtins.int
    agent_instance_id: builtins.str
    status: global___ClaimAgentStatusRequest.Status.ValueType
    status_message: builtins.str
    def __init__(
        self,
        *,
        agent_instance_id: builtins.str = ...,
        status: global___ClaimAgentStatusRequest.Status.ValueType = ...,
        status_message: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["agent_instance_id", b"agent_instance_id", "status", b"status", "status_message", b"status_message"]) -> None: ...

global___ClaimAgentStatusRequest = ClaimAgentStatusRequest

@typing.final
class ClaimAgentStatusResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CODE_FIELD_NUMBER: builtins.int
    code: builtins.int
    def __init__(
        self,
        *,
        code: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["code", b"code"]) -> None: ...

global___ClaimAgentStatusResponse = ClaimAgentStatusResponse

@typing.final
class ReportEventLogsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AGENT_INSTANCE_ID_FIELD_NUMBER: builtins.int
    IDEMPOTENCY_KEY_FIELD_NUMBER: builtins.int
    EVENTS_FIELD_NUMBER: builtins.int
    agent_instance_id: builtins.str
    idempotency_key: builtins.str
    @property
    def events(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EventLog]: ...
    def __init__(
        self,
        *,
        agent_instance_id: builtins.str = ...,
        idempotency_key: builtins.str = ...,
        events: collections.abc.Iterable[global___EventLog] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["agent_instance_id", b"agent_instance_id", "events", b"events", "idempotency_key", b"idempotency_key"]) -> None: ...

global___ReportEventLogsRequest = ReportEventLogsRequest

@typing.final
class ReportEventLogsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ReportEventLogsResponse = ReportEventLogsResponse

@typing.final
class EventLog(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Severity:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _SeverityEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[EventLog._Severity.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        SEVERITY_UNSPECIFIED: EventLog._Severity.ValueType  # 0
        DEBUG: EventLog._Severity.ValueType  # 1
        INFO: EventLog._Severity.ValueType  # 2
        WARNING: EventLog._Severity.ValueType  # 3
        ERROR: EventLog._Severity.ValueType  # 4
        FATAL: EventLog._Severity.ValueType  # 5

    class Severity(_Severity, metaclass=_SeverityEnumTypeWrapper): ...
    SEVERITY_UNSPECIFIED: EventLog.Severity.ValueType  # 0
    DEBUG: EventLog.Severity.ValueType  # 1
    INFO: EventLog.Severity.ValueType  # 2
    WARNING: EventLog.Severity.ValueType  # 3
    ERROR: EventLog.Severity.ValueType  # 4
    FATAL: EventLog.Severity.ValueType  # 5

    @typing.final
    class MetadataEntry(google.protobuf.message.Message):
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

    MESSAGE_FIELD_NUMBER: builtins.int
    SEVERITY_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    message: builtins.str
    severity: global___EventLog.Severity.ValueType
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def metadata(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    def __init__(
        self,
        *,
        message: builtins.str = ...,
        severity: global___EventLog.Severity.ValueType = ...,
        timestamp: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        metadata: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["timestamp", b"timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["message", b"message", "metadata", b"metadata", "severity", b"severity", "timestamp", b"timestamp"]) -> None: ...

global___EventLog = EventLog
