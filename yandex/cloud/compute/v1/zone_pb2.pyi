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
class Zone(google.protobuf.message.Message):
    """Availability zone. For more information, see [Availability zones](/docs/overview/concepts/geo-scope)."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Zone._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: Zone._Status.ValueType  # 0
        UP: Zone._Status.ValueType  # 1
        """Zone is available. You can access the resources allocated in this zone."""
        DOWN: Zone._Status.ValueType  # 2
        """Zone is not available."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...
    STATUS_UNSPECIFIED: Zone.Status.ValueType  # 0
    UP: Zone.Status.ValueType  # 1
    """Zone is available. You can access the resources allocated in this zone."""
    DOWN: Zone.Status.ValueType  # 2
    """Zone is not available."""

    ID_FIELD_NUMBER: builtins.int
    REGION_ID_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the zone."""
    region_id: builtins.str
    """ID of the region."""
    status: global___Zone.Status.ValueType
    """Status of the zone."""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        region_id: builtins.str = ...,
        status: global___Zone.Status.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["id", b"id", "region_id", b"region_id", "status", b"status"]) -> None: ...

global___Zone = Zone
