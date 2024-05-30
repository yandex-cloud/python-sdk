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
class Downsampling(google.protobuf.message.Message):
    """List of available aggregate functions for downsampling."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _GridAggregation:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _GridAggregationEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Downsampling._GridAggregation.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        GRID_AGGREGATION_UNSPECIFIED: Downsampling._GridAggregation.ValueType  # 0
        GRID_AGGREGATION_MAX: Downsampling._GridAggregation.ValueType  # 1
        """Max value."""
        GRID_AGGREGATION_MIN: Downsampling._GridAggregation.ValueType  # 2
        """Min value."""
        GRID_AGGREGATION_SUM: Downsampling._GridAggregation.ValueType  # 3
        """Sum of values."""
        GRID_AGGREGATION_AVG: Downsampling._GridAggregation.ValueType  # 4
        """Average value."""
        GRID_AGGREGATION_LAST: Downsampling._GridAggregation.ValueType  # 5
        """Last value."""
        GRID_AGGREGATION_COUNT: Downsampling._GridAggregation.ValueType  # 6
        """Total count of points."""

    class GridAggregation(_GridAggregation, metaclass=_GridAggregationEnumTypeWrapper):
        """List of available aggregate functions for downsampling."""

    GRID_AGGREGATION_UNSPECIFIED: Downsampling.GridAggregation.ValueType  # 0
    GRID_AGGREGATION_MAX: Downsampling.GridAggregation.ValueType  # 1
    """Max value."""
    GRID_AGGREGATION_MIN: Downsampling.GridAggregation.ValueType  # 2
    """Min value."""
    GRID_AGGREGATION_SUM: Downsampling.GridAggregation.ValueType  # 3
    """Sum of values."""
    GRID_AGGREGATION_AVG: Downsampling.GridAggregation.ValueType  # 4
    """Average value."""
    GRID_AGGREGATION_LAST: Downsampling.GridAggregation.ValueType  # 5
    """Last value."""
    GRID_AGGREGATION_COUNT: Downsampling.GridAggregation.ValueType  # 6
    """Total count of points."""

    class _GapFilling:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _GapFillingEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Downsampling._GapFilling.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        GAP_FILLING_UNSPECIFIED: Downsampling._GapFilling.ValueType  # 0
        GAP_FILLING_NULL: Downsampling._GapFilling.ValueType  # 1
        """Returns `null` as a metric value and `timestamp` as a time series value."""
        GAP_FILLING_NONE: Downsampling._GapFilling.ValueType  # 2
        """Returns no value and no timestamp."""
        GAP_FILLING_PREVIOUS: Downsampling._GapFilling.ValueType  # 3
        """Returns the value from the previous time interval."""

    class GapFilling(_GapFilling, metaclass=_GapFillingEnumTypeWrapper):
        """List of available gap filling policy for downsampling."""

    GAP_FILLING_UNSPECIFIED: Downsampling.GapFilling.ValueType  # 0
    GAP_FILLING_NULL: Downsampling.GapFilling.ValueType  # 1
    """Returns `null` as a metric value and `timestamp` as a time series value."""
    GAP_FILLING_NONE: Downsampling.GapFilling.ValueType  # 2
    """Returns no value and no timestamp."""
    GAP_FILLING_PREVIOUS: Downsampling.GapFilling.ValueType  # 3
    """Returns the value from the previous time interval."""

    MAX_POINTS_FIELD_NUMBER: builtins.int
    GRID_INTERVAL_FIELD_NUMBER: builtins.int
    DISABLED_FIELD_NUMBER: builtins.int
    GRID_AGGREGATION_FIELD_NUMBER: builtins.int
    GAP_FILLING_FIELD_NUMBER: builtins.int
    max_points: builtins.int
    """Maximum number of points to be returned."""
    grid_interval: builtins.int
    """Time interval (grid) for downsampling in milliseconds.
    Points in the specified range are aggregated into one time point.
    """
    disabled: builtins.bool
    """Disable downsampling."""
    grid_aggregation: global___Downsampling.GridAggregation.ValueType
    """Function that is used for downsampling."""
    gap_filling: global___Downsampling.GapFilling.ValueType
    """Parameters for filling gaps in data."""
    def __init__(
        self,
        *,
        max_points: builtins.int = ...,
        grid_interval: builtins.int = ...,
        disabled: builtins.bool = ...,
        grid_aggregation: global___Downsampling.GridAggregation.ValueType = ...,
        gap_filling: global___Downsampling.GapFilling.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["disabled", b"disabled", "grid_interval", b"grid_interval", "max_points", b"max_points", "mode", b"mode"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["disabled", b"disabled", "gap_filling", b"gap_filling", "grid_aggregation", b"grid_aggregation", "grid_interval", b"grid_interval", "max_points", b"max_points", "mode", b"mode"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["mode", b"mode"]) -> typing.Literal["max_points", "grid_interval", "disabled"] | None: ...

global___Downsampling = Downsampling
