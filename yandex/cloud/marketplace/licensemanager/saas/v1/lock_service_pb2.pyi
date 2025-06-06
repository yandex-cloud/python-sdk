"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class EnsureLockRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INSTANCE_TOKEN_FIELD_NUMBER: builtins.int
    RESOURCE_ID_FIELD_NUMBER: builtins.int
    instance_token: builtins.str
    """Signed JWT token which contains information about subscription."""
    resource_id: builtins.str
    """ID of the resource to which the subscription will be locked."""
    def __init__(
        self,
        *,
        instance_token: builtins.str = ...,
        resource_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["instance_token", b"instance_token", "resource_id", b"resource_id"]) -> None: ...

global___EnsureLockRequest = EnsureLockRequest

@typing.final
class EnsureLockMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOCK_ID_FIELD_NUMBER: builtins.int
    lock_id: builtins.str
    """ID of the subscription lock."""
    def __init__(
        self,
        *,
        lock_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["lock_id", b"lock_id"]) -> None: ...

global___EnsureLockMetadata = EnsureLockMetadata

@typing.final
class GetLockRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOCK_ID_FIELD_NUMBER: builtins.int
    lock_id: builtins.str
    """ID of the subscription lock."""
    def __init__(
        self,
        *,
        lock_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["lock_id", b"lock_id"]) -> None: ...

global___GetLockRequest = GetLockRequest

@typing.final
class GetLockByResourceIDRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_ID_FIELD_NUMBER: builtins.int
    INSTANCE_ID_FIELD_NUMBER: builtins.int
    resource_id: builtins.str
    """ID of the resource to with subscription is locked."""
    instance_id: builtins.str
    """ID of the subscription"""
    def __init__(
        self,
        *,
        resource_id: builtins.str = ...,
        instance_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["instance_id", b"instance_id", "resource_id", b"resource_id"]) -> None: ...

global___GetLockByResourceIDRequest = GetLockByResourceIDRequest
