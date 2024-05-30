"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class TargetGroup(google.protobuf.message.Message):
    """A TargetGroup resource. For more information, see [Target groups and resources](/docs/network-load-balancer/concepts/target-resources)."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class LabelsEntry(google.protobuf.message.Message):
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

    ID_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    REGION_ID_FIELD_NUMBER: builtins.int
    TARGETS_FIELD_NUMBER: builtins.int
    id: builtins.str
    """Output only. ID of the target group."""
    folder_id: builtins.str
    """ID of the folder that the target group belongs to."""
    name: builtins.str
    """Name of the target group.
    The name is unique within the folder. 3-63 characters long.
    """
    description: builtins.str
    """Description of the target group. 0-256 characters long."""
    region_id: builtins.str
    """ID of the region where the target group resides."""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `` key:value `` pairs. Maximum of 64 per resource."""

    @property
    def targets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Target]:
        """A list of targets in the target group."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        folder_id: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        region_id: builtins.str = ...,
        targets: collections.abc.Iterable[global___Target] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["created_at", b"created_at", "description", b"description", "folder_id", b"folder_id", "id", b"id", "labels", b"labels", "name", b"name", "region_id", b"region_id", "targets", b"targets"]) -> None: ...

global___TargetGroup = TargetGroup

@typing.final
class Target(google.protobuf.message.Message):
    """A Target resource. For more information, see [Target groups and resources](/docs/network-load-balancer/concepts/target-resources)."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBNET_ID_FIELD_NUMBER: builtins.int
    ADDRESS_FIELD_NUMBER: builtins.int
    subnet_id: builtins.str
    """ID of the subnet that targets are connected to.
    All targets in the target group must be connected to the same subnet within a single availability zone.
    """
    address: builtins.str
    """IP address of the target."""
    def __init__(
        self,
        *,
        subnet_id: builtins.str = ...,
        address: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["address", b"address", "subnet_id", b"subnet_id"]) -> None: ...

global___Target = Target
