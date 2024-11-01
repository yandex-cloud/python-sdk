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
class PointOfPresence(google.protobuf.message.Message):
    """A PointOfPresence resource."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    REGION_ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the pointOfPresence."""
    region_id: builtins.str
    """ID of the region that the pointOfPresence belongs to."""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        region_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["id", b"id", "region_id", b"region_id"]) -> None: ...

global___PointOfPresence = PointOfPresence