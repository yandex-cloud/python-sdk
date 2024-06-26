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

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class UsageRecord(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    UUID_FIELD_NUMBER: builtins.int
    SKU_ID_FIELD_NUMBER: builtins.int
    QUANTITY_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    uuid: builtins.str
    """Unique identifier of the usage record (UUID format)."""
    sku_id: builtins.str
    """Consumed Marketplace SKU ID, linked to `UsageRecord.product_id`."""
    quantity: builtins.int
    """Quantity of SKU consumed, measured in `sku.usage_unit` units (e.g. bytes)."""
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Timestamp in UTC for which the usage is being reported."""

    def __init__(
        self,
        *,
        uuid: builtins.str = ...,
        sku_id: builtins.str = ...,
        quantity: builtins.int = ...,
        timestamp: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["timestamp", b"timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["quantity", b"quantity", "sku_id", b"sku_id", "timestamp", b"timestamp", "uuid", b"uuid"]) -> None: ...

global___UsageRecord = UsageRecord

@typing.final
class AcceptedUsageRecord(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    UUID_FIELD_NUMBER: builtins.int
    uuid: builtins.str
    """Unique identifier of the usage record (UUID format)."""
    def __init__(
        self,
        *,
        uuid: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["uuid", b"uuid"]) -> None: ...

global___AcceptedUsageRecord = AcceptedUsageRecord

@typing.final
class RejectedUsageRecord(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Reason:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _ReasonEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[RejectedUsageRecord._Reason.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        REASON_UNSPECIFIED: RejectedUsageRecord._Reason.ValueType  # 0
        DUPLICATE: RejectedUsageRecord._Reason.ValueType  # 1
        EXPIRED: RejectedUsageRecord._Reason.ValueType  # 2
        INVALID_TIMESTAMP: RejectedUsageRecord._Reason.ValueType  # 3
        INVALID_SKU_ID: RejectedUsageRecord._Reason.ValueType  # 4
        INVALID_PRODUCT_ID: RejectedUsageRecord._Reason.ValueType  # 5
        INVALID_QUANTITY: RejectedUsageRecord._Reason.ValueType  # 6
        INVALID_ID: RejectedUsageRecord._Reason.ValueType  # 7

    class Reason(_Reason, metaclass=_ReasonEnumTypeWrapper): ...
    REASON_UNSPECIFIED: RejectedUsageRecord.Reason.ValueType  # 0
    DUPLICATE: RejectedUsageRecord.Reason.ValueType  # 1
    EXPIRED: RejectedUsageRecord.Reason.ValueType  # 2
    INVALID_TIMESTAMP: RejectedUsageRecord.Reason.ValueType  # 3
    INVALID_SKU_ID: RejectedUsageRecord.Reason.ValueType  # 4
    INVALID_PRODUCT_ID: RejectedUsageRecord.Reason.ValueType  # 5
    INVALID_QUANTITY: RejectedUsageRecord.Reason.ValueType  # 6
    INVALID_ID: RejectedUsageRecord.Reason.ValueType  # 7

    UUID_FIELD_NUMBER: builtins.int
    REASON_FIELD_NUMBER: builtins.int
    uuid: builtins.str
    """Unique identifier of the usage record (UUID format)."""
    reason: global___RejectedUsageRecord.Reason.ValueType
    """The reason of rejection."""
    def __init__(
        self,
        *,
        uuid: builtins.str = ...,
        reason: global___RejectedUsageRecord.Reason.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["reason", b"reason", "uuid", b"uuid"]) -> None: ...

global___RejectedUsageRecord = RejectedUsageRecord
