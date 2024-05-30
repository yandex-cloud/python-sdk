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
class PlacementGroup(google.protobuf.message.Message):
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
    SPREAD_PLACEMENT_STRATEGY_FIELD_NUMBER: builtins.int
    PARTITION_PLACEMENT_STRATEGY_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the placement group. Generated at creation time."""
    folder_id: builtins.str
    """ID of the folder that the placement group belongs to."""
    name: builtins.str
    """Name of the placement group.
    The name is unique within the folder.
    """
    description: builtins.str
    """Description of the placement group. 0-256 characters long."""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Placement group labels as `key:value` pairs."""

    @property
    def spread_placement_strategy(self) -> global___SpreadPlacementStrategy:
        """Anti-affinity placement strategy (`spread`). Instances are distributed
        over distinct failure domains.
        """

    @property
    def partition_placement_strategy(self) -> global___PartitionPlacementStrategy: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        folder_id: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        spread_placement_strategy: global___SpreadPlacementStrategy | None = ...,
        partition_placement_strategy: global___PartitionPlacementStrategy | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at", "partition_placement_strategy", b"partition_placement_strategy", "placement_strategy", b"placement_strategy", "spread_placement_strategy", b"spread_placement_strategy"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["created_at", b"created_at", "description", b"description", "folder_id", b"folder_id", "id", b"id", "labels", b"labels", "name", b"name", "partition_placement_strategy", b"partition_placement_strategy", "placement_strategy", b"placement_strategy", "spread_placement_strategy", b"spread_placement_strategy"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["placement_strategy", b"placement_strategy"]) -> typing.Literal["spread_placement_strategy", "partition_placement_strategy"] | None: ...

global___PlacementGroup = PlacementGroup

@typing.final
class SpreadPlacementStrategy(google.protobuf.message.Message):
    """This is an empty structure that must be passed to explicitly
    specify the required placement strategy.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___SpreadPlacementStrategy = SpreadPlacementStrategy

@typing.final
class PartitionPlacementStrategy(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARTITIONS_FIELD_NUMBER: builtins.int
    partitions: builtins.int
    def __init__(
        self,
        *,
        partitions: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["partitions", b"partitions"]) -> None: ...

global___PartitionPlacementStrategy = PartitionPlacementStrategy
