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
class ResourcePreset(google.protobuf.message.Message):
    """A ResourcePreset resource for describing hardware configuration presets."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    ZONE_IDS_FIELD_NUMBER: builtins.int
    CORES_FIELD_NUMBER: builtins.int
    MEMORY_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the ResourcePreset resource."""
    cores: builtins.int
    """Number of CPU cores for a Yandex Data Processing host created with the preset."""
    memory: builtins.int
    """RAM volume for a Yandex Data Processing host created with the preset, in bytes."""
    @property
    def zone_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """IDs of availability zones where the resource preset is available."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        zone_ids: collections.abc.Iterable[builtins.str] | None = ...,
        cores: builtins.int = ...,
        memory: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cores", b"cores", "id", b"id", "memory", b"memory", "zone_ids", b"zone_ids"]) -> None: ...

global___ResourcePreset = ResourcePreset
