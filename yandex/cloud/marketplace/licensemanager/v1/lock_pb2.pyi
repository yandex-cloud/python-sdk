"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys
import typing
import yandex.cloud.marketplace.licensemanager.v1.external_instance_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Lock(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _State:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Lock._State.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATE_UNSPECIFIED: Lock._State.ValueType  # 0
        UNLOCKED: Lock._State.ValueType  # 1
        """Subscription unlocked."""
        LOCKED: Lock._State.ValueType  # 2
        """Subscription locked to the resource."""
        DELETED: Lock._State.ValueType  # 3
        """Subscription lock deleted."""

    class State(_State, metaclass=_StateEnumTypeWrapper): ...
    STATE_UNSPECIFIED: Lock.State.ValueType  # 0
    UNLOCKED: Lock.State.ValueType  # 1
    """Subscription unlocked."""
    LOCKED: Lock.State.ValueType  # 2
    """Subscription locked to the resource."""
    DELETED: Lock.State.ValueType  # 3
    """Subscription lock deleted."""

    ID_FIELD_NUMBER: builtins.int
    INSTANCE_ID_FIELD_NUMBER: builtins.int
    RESOURCE_ID_FIELD_NUMBER: builtins.int
    START_TIME_FIELD_NUMBER: builtins.int
    END_TIME_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    UPDATED_AT_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    TEMPLATE_ID_FIELD_NUMBER: builtins.int
    EXTERNAL_INSTANCE_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the subscription lock."""
    instance_id: builtins.str
    """ID of the subscription instance."""
    resource_id: builtins.str
    """ID of the resource."""
    state: global___Lock.State.ValueType
    """Subscription lock state."""
    template_id: builtins.str
    """ID of the subscription template."""
    @property
    def start_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Timestamp of the start of the subscription lock."""

    @property
    def end_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Timestamp of the end of the subscription lock."""

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp."""

    @property
    def updated_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Update timestamp."""

    @property
    def external_instance(self) -> yandex.cloud.marketplace.licensemanager.v1.external_instance_pb2.ExternalInstance:
        """External subscription instance (optional), for usage convenience propagated
        from parent subscription instance.
        """

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        instance_id: builtins.str = ...,
        resource_id: builtins.str = ...,
        start_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        end_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        updated_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        state: global___Lock.State.ValueType = ...,
        template_id: builtins.str = ...,
        external_instance: yandex.cloud.marketplace.licensemanager.v1.external_instance_pb2.ExternalInstance | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at", "end_time", b"end_time", "external_instance", b"external_instance", "start_time", b"start_time", "updated_at", b"updated_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["created_at", b"created_at", "end_time", b"end_time", "external_instance", b"external_instance", "id", b"id", "instance_id", b"instance_id", "resource_id", b"resource_id", "start_time", b"start_time", "state", b"state", "template_id", b"template_id", "updated_at", b"updated_at"]) -> None: ...

global___Lock = Lock
