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
class Partner(google.protobuf.message.Message):
    """A Partner resource."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Partner._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: Partner._Status.ValueType  # 0
        UP: Partner._Status.ValueType  # 1
        DOWN: Partner._Status.ValueType  # 2

    class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...
    STATUS_UNSPECIFIED: Partner.Status.ValueType  # 0
    UP: Partner.Status.ValueType  # 1
    DOWN: Partner.Status.ValueType  # 2

    ID_FIELD_NUMBER: builtins.int
    REGION_ID_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the partner."""
    region_id: builtins.str
    """ID of the region that the partner belongs to."""
    status: global___Partner.Status.ValueType
    """Status of the partner."""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        region_id: builtins.str = ...,
        status: global___Partner.Status.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["id", b"id", "region_id", b"region_id", "status", b"status"]) -> None: ...

global___Partner = Partner
