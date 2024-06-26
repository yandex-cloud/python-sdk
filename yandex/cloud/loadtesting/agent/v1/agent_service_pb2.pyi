"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
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
