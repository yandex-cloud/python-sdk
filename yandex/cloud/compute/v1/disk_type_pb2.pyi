"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class DiskType(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    ZONE_IDS_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the disk type."""
    description: builtins.str
    """Description of the disk type. 0-256 characters long."""
    @property
    def zone_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Array of availability zones where the disk type is available."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        description: builtins.str = ...,
        zone_ids: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "id", b"id", "zone_ids", b"zone_ids"]) -> None: ...

global___DiskType = DiskType
