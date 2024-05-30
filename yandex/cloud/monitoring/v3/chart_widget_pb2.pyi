"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.wrappers_pb2
import sys
import typing
import yandex.cloud.monitoring.v3.downsampling_pb2
import yandex.cloud.monitoring.v3.unit_format_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class ChartWidget(google.protobuf.message.Message):
    """Chart widget."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _FreezeDuration:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _FreezeDurationEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ChartWidget._FreezeDuration.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        FREEZE_DURATION_UNSPECIFIED: ChartWidget._FreezeDuration.ValueType  # 0
        FREEZE_DURATION_HOUR: ChartWidget._FreezeDuration.ValueType  # 1
        """Last hour."""
        FREEZE_DURATION_DAY: ChartWidget._FreezeDuration.ValueType  # 2
        """Last day = last 24 hours."""
        FREEZE_DURATION_WEEK: ChartWidget._FreezeDuration.ValueType  # 3
        """Last 7 days."""
        FREEZE_DURATION_MONTH: ChartWidget._FreezeDuration.ValueType  # 4
        """Last 31 days."""

    class FreezeDuration(_FreezeDuration, metaclass=_FreezeDurationEnumTypeWrapper): ...
    FREEZE_DURATION_UNSPECIFIED: ChartWidget.FreezeDuration.ValueType  # 0
    FREEZE_DURATION_HOUR: ChartWidget.FreezeDuration.ValueType  # 1
    """Last hour."""
    FREEZE_DURATION_DAY: ChartWidget.FreezeDuration.ValueType  # 2
    """Last day = last 24 hours."""
    FREEZE_DURATION_WEEK: ChartWidget.FreezeDuration.ValueType  # 3
    """Last 7 days."""
    FREEZE_DURATION_MONTH: ChartWidget.FreezeDuration.ValueType  # 4
    """Last 31 days."""

    @typing.final
    class Queries(google.protobuf.message.Message):
        """Query settings."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        @typing.final
        class Target(google.protobuf.message.Message):
            """Query target."""

            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            QUERY_FIELD_NUMBER: builtins.int
            TEXT_MODE_FIELD_NUMBER: builtins.int
            HIDDEN_FIELD_NUMBER: builtins.int
            NAME_FIELD_NUMBER: builtins.int
            query: builtins.str
            """Required. Query."""
            text_mode: builtins.bool
            """Text mode."""
            hidden: builtins.bool
            """Checks that target is visible or invisible."""
            name: builtins.str
            """Name of the query."""
            def __init__(
                self,
                *,
                query: builtins.str = ...,
                text_mode: builtins.bool = ...,
                hidden: builtins.bool = ...,
                name: builtins.str = ...,
            ) -> None: ...
            def ClearField(self, field_name: typing.Literal["hidden", b"hidden", "name", b"name", "query", b"query", "text_mode", b"text_mode"]) -> None: ...

        TARGETS_FIELD_NUMBER: builtins.int
        DOWNSAMPLING_FIELD_NUMBER: builtins.int
        @property
        def targets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ChartWidget.Queries.Target]:
            """Required. List of targets."""

        @property
        def downsampling(self) -> yandex.cloud.monitoring.v3.downsampling_pb2.Downsampling:
            """Required. Downsampling settings."""

        def __init__(
            self,
            *,
            targets: collections.abc.Iterable[global___ChartWidget.Queries.Target] | None = ...,
            downsampling: yandex.cloud.monitoring.v3.downsampling_pb2.Downsampling | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["downsampling", b"downsampling"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["downsampling", b"downsampling", "targets", b"targets"]) -> None: ...

    @typing.final
    class VisualizationSettings(google.protobuf.message.Message):
        """Visualization settings."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        class _VisualizationType:
            ValueType = typing.NewType("ValueType", builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _VisualizationTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ChartWidget.VisualizationSettings._VisualizationType.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            VISUALIZATION_TYPE_UNSPECIFIED: ChartWidget.VisualizationSettings._VisualizationType.ValueType  # 0
            """Not specified (line by default)."""
            VISUALIZATION_TYPE_LINE: ChartWidget.VisualizationSettings._VisualizationType.ValueType  # 1
            """Line chart."""
            VISUALIZATION_TYPE_STACK: ChartWidget.VisualizationSettings._VisualizationType.ValueType  # 2
            """Stack chart."""
            VISUALIZATION_TYPE_COLUMN: ChartWidget.VisualizationSettings._VisualizationType.ValueType  # 3
            """Points as columns chart."""
            VISUALIZATION_TYPE_POINTS: ChartWidget.VisualizationSettings._VisualizationType.ValueType  # 4
            """Points."""
            VISUALIZATION_TYPE_PIE: ChartWidget.VisualizationSettings._VisualizationType.ValueType  # 5
            """Pie aggregation chart."""
            VISUALIZATION_TYPE_BARS: ChartWidget.VisualizationSettings._VisualizationType.ValueType  # 6
            """Bars aggregation chart."""
            VISUALIZATION_TYPE_DISTRIBUTION: ChartWidget.VisualizationSettings._VisualizationType.ValueType  # 7
            """Distribution aggregation chart."""
            VISUALIZATION_TYPE_HEATMAP: ChartWidget.VisualizationSettings._VisualizationType.ValueType  # 8
            """Heatmap aggregation chart."""

        class VisualizationType(_VisualizationType, metaclass=_VisualizationTypeEnumTypeWrapper):
            """Chart visualization type."""

        VISUALIZATION_TYPE_UNSPECIFIED: ChartWidget.VisualizationSettings.VisualizationType.ValueType  # 0
        """Not specified (line by default)."""
        VISUALIZATION_TYPE_LINE: ChartWidget.VisualizationSettings.VisualizationType.ValueType  # 1
        """Line chart."""
        VISUALIZATION_TYPE_STACK: ChartWidget.VisualizationSettings.VisualizationType.ValueType  # 2
        """Stack chart."""
        VISUALIZATION_TYPE_COLUMN: ChartWidget.VisualizationSettings.VisualizationType.ValueType  # 3
        """Points as columns chart."""
        VISUALIZATION_TYPE_POINTS: ChartWidget.VisualizationSettings.VisualizationType.ValueType  # 4
        """Points."""
        VISUALIZATION_TYPE_PIE: ChartWidget.VisualizationSettings.VisualizationType.ValueType  # 5
        """Pie aggregation chart."""
        VISUALIZATION_TYPE_BARS: ChartWidget.VisualizationSettings.VisualizationType.ValueType  # 6
        """Bars aggregation chart."""
        VISUALIZATION_TYPE_DISTRIBUTION: ChartWidget.VisualizationSettings.VisualizationType.ValueType  # 7
        """Distribution aggregation chart."""
        VISUALIZATION_TYPE_HEATMAP: ChartWidget.VisualizationSettings.VisualizationType.ValueType  # 8
        """Heatmap aggregation chart."""

        class _Interpolate:
            ValueType = typing.NewType("ValueType", builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _InterpolateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ChartWidget.VisualizationSettings._Interpolate.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            INTERPOLATE_UNSPECIFIED: ChartWidget.VisualizationSettings._Interpolate.ValueType  # 0
            """Not specified (linear by default)."""
            INTERPOLATE_LINEAR: ChartWidget.VisualizationSettings._Interpolate.ValueType  # 1
            """Linear."""
            INTERPOLATE_LEFT: ChartWidget.VisualizationSettings._Interpolate.ValueType  # 2
            """Left."""
            INTERPOLATE_RIGHT: ChartWidget.VisualizationSettings._Interpolate.ValueType  # 3
            """Right."""

        class Interpolate(_Interpolate, metaclass=_InterpolateEnumTypeWrapper): ...
        INTERPOLATE_UNSPECIFIED: ChartWidget.VisualizationSettings.Interpolate.ValueType  # 0
        """Not specified (linear by default)."""
        INTERPOLATE_LINEAR: ChartWidget.VisualizationSettings.Interpolate.ValueType  # 1
        """Linear."""
        INTERPOLATE_LEFT: ChartWidget.VisualizationSettings.Interpolate.ValueType  # 2
        """Left."""
        INTERPOLATE_RIGHT: ChartWidget.VisualizationSettings.Interpolate.ValueType  # 3
        """Right."""

        class _YaxisType:
            ValueType = typing.NewType("ValueType", builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _YaxisTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ChartWidget.VisualizationSettings._YaxisType.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            YAXIS_TYPE_UNSPECIFIED: ChartWidget.VisualizationSettings._YaxisType.ValueType  # 0
            """Not specified (linear by default)."""
            YAXIS_TYPE_LINEAR: ChartWidget.VisualizationSettings._YaxisType.ValueType  # 1
            """Linear."""
            YAXIS_TYPE_LOGARITHMIC: ChartWidget.VisualizationSettings._YaxisType.ValueType  # 2
            """Logarithmic."""

        class YaxisType(_YaxisType, metaclass=_YaxisTypeEnumTypeWrapper):
            """Y axis type.
            N.B. _TYPE prefix is necessary to expect name clash with Interpolate LINEAR value.
            """

        YAXIS_TYPE_UNSPECIFIED: ChartWidget.VisualizationSettings.YaxisType.ValueType  # 0
        """Not specified (linear by default)."""
        YAXIS_TYPE_LINEAR: ChartWidget.VisualizationSettings.YaxisType.ValueType  # 1
        """Linear."""
        YAXIS_TYPE_LOGARITHMIC: ChartWidget.VisualizationSettings.YaxisType.ValueType  # 2
        """Logarithmic."""

        class _SeriesAggregation:
            ValueType = typing.NewType("ValueType", builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _SeriesAggregationEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ChartWidget.VisualizationSettings._SeriesAggregation.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            SERIES_AGGREGATION_UNSPECIFIED: ChartWidget.VisualizationSettings._SeriesAggregation.ValueType  # 0
            """Not specified (avg by default)."""
            SERIES_AGGREGATION_AVG: ChartWidget.VisualizationSettings._SeriesAggregation.ValueType  # 1
            """Average."""
            SERIES_AGGREGATION_MIN: ChartWidget.VisualizationSettings._SeriesAggregation.ValueType  # 2
            """Minimum."""
            SERIES_AGGREGATION_MAX: ChartWidget.VisualizationSettings._SeriesAggregation.ValueType  # 3
            """Maximum."""
            SERIES_AGGREGATION_LAST: ChartWidget.VisualizationSettings._SeriesAggregation.ValueType  # 4
            """Last non-NaN value."""
            SERIES_AGGREGATION_SUM: ChartWidget.VisualizationSettings._SeriesAggregation.ValueType  # 5
            """Sum."""

        class SeriesAggregation(_SeriesAggregation, metaclass=_SeriesAggregationEnumTypeWrapper): ...
        SERIES_AGGREGATION_UNSPECIFIED: ChartWidget.VisualizationSettings.SeriesAggregation.ValueType  # 0
        """Not specified (avg by default)."""
        SERIES_AGGREGATION_AVG: ChartWidget.VisualizationSettings.SeriesAggregation.ValueType  # 1
        """Average."""
        SERIES_AGGREGATION_MIN: ChartWidget.VisualizationSettings.SeriesAggregation.ValueType  # 2
        """Minimum."""
        SERIES_AGGREGATION_MAX: ChartWidget.VisualizationSettings.SeriesAggregation.ValueType  # 3
        """Maximum."""
        SERIES_AGGREGATION_LAST: ChartWidget.VisualizationSettings.SeriesAggregation.ValueType  # 4
        """Last non-NaN value."""
        SERIES_AGGREGATION_SUM: ChartWidget.VisualizationSettings.SeriesAggregation.ValueType  # 5
        """Sum."""

        @typing.final
        class ColorSchemeSettings(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            @typing.final
            class AutomaticColorScheme(google.protobuf.message.Message):
                DESCRIPTOR: google.protobuf.descriptor.Descriptor

                def __init__(
                    self,
                ) -> None: ...

            @typing.final
            class StandardColorScheme(google.protobuf.message.Message):
                DESCRIPTOR: google.protobuf.descriptor.Descriptor

                def __init__(
                    self,
                ) -> None: ...

            @typing.final
            class GradientColorScheme(google.protobuf.message.Message):
                DESCRIPTOR: google.protobuf.descriptor.Descriptor

                GREEN_VALUE_FIELD_NUMBER: builtins.int
                YELLOW_VALUE_FIELD_NUMBER: builtins.int
                RED_VALUE_FIELD_NUMBER: builtins.int
                VIOLET_VALUE_FIELD_NUMBER: builtins.int
                green_value: builtins.str
                """Gradient green value."""
                yellow_value: builtins.str
                """Gradient yellow value."""
                red_value: builtins.str
                """Gradient red value."""
                violet_value: builtins.str
                """Gradient violet_value."""
                def __init__(
                    self,
                    *,
                    green_value: builtins.str = ...,
                    yellow_value: builtins.str = ...,
                    red_value: builtins.str = ...,
                    violet_value: builtins.str = ...,
                ) -> None: ...
                def ClearField(self, field_name: typing.Literal["green_value", b"green_value", "red_value", b"red_value", "violet_value", b"violet_value", "yellow_value", b"yellow_value"]) -> None: ...

            AUTOMATIC_FIELD_NUMBER: builtins.int
            STANDARD_FIELD_NUMBER: builtins.int
            GRADIENT_FIELD_NUMBER: builtins.int
            @property
            def automatic(self) -> global___ChartWidget.VisualizationSettings.ColorSchemeSettings.AutomaticColorScheme:
                """Automatic color scheme."""

            @property
            def standard(self) -> global___ChartWidget.VisualizationSettings.ColorSchemeSettings.StandardColorScheme:
                """Standard color scheme."""

            @property
            def gradient(self) -> global___ChartWidget.VisualizationSettings.ColorSchemeSettings.GradientColorScheme:
                """Gradient color scheme."""

            def __init__(
                self,
                *,
                automatic: global___ChartWidget.VisualizationSettings.ColorSchemeSettings.AutomaticColorScheme | None = ...,
                standard: global___ChartWidget.VisualizationSettings.ColorSchemeSettings.StandardColorScheme | None = ...,
                gradient: global___ChartWidget.VisualizationSettings.ColorSchemeSettings.GradientColorScheme | None = ...,
            ) -> None: ...
            def HasField(self, field_name: typing.Literal["automatic", b"automatic", "gradient", b"gradient", "scheme", b"scheme", "standard", b"standard"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing.Literal["automatic", b"automatic", "gradient", b"gradient", "scheme", b"scheme", "standard", b"standard"]) -> None: ...
            def WhichOneof(self, oneof_group: typing.Literal["scheme", b"scheme"]) -> typing.Literal["automatic", "standard", "gradient"] | None: ...

        @typing.final
        class HeatmapSettings(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            GREEN_VALUE_FIELD_NUMBER: builtins.int
            YELLOW_VALUE_FIELD_NUMBER: builtins.int
            RED_VALUE_FIELD_NUMBER: builtins.int
            VIOLET_VALUE_FIELD_NUMBER: builtins.int
            green_value: builtins.str
            """Heatmap green value."""
            yellow_value: builtins.str
            """Heatmap yellow value."""
            red_value: builtins.str
            """Heatmap red value."""
            violet_value: builtins.str
            """Heatmap violet_value."""
            def __init__(
                self,
                *,
                green_value: builtins.str = ...,
                yellow_value: builtins.str = ...,
                red_value: builtins.str = ...,
                violet_value: builtins.str = ...,
            ) -> None: ...
            def ClearField(self, field_name: typing.Literal["green_value", b"green_value", "red_value", b"red_value", "violet_value", b"violet_value", "yellow_value", b"yellow_value"]) -> None: ...

        @typing.final
        class Yaxis(google.protobuf.message.Message):
            """Y axis settings."""

            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            TYPE_FIELD_NUMBER: builtins.int
            TITLE_FIELD_NUMBER: builtins.int
            MIN_FIELD_NUMBER: builtins.int
            MAX_FIELD_NUMBER: builtins.int
            UNIT_FORMAT_FIELD_NUMBER: builtins.int
            PRECISION_FIELD_NUMBER: builtins.int
            type: global___ChartWidget.VisualizationSettings.YaxisType.ValueType
            """Type."""
            title: builtins.str
            """Title or empty."""
            min: builtins.str
            """Min value in extended number format or empty."""
            max: builtins.str
            """Max value in extended number format or empty."""
            unit_format: yandex.cloud.monitoring.v3.unit_format_pb2.UnitFormat.ValueType
            """Unit format."""
            @property
            def precision(self) -> google.protobuf.wrappers_pb2.Int64Value:
                """Tick value precision (null as default, 0-7 in other cases)."""

            def __init__(
                self,
                *,
                type: global___ChartWidget.VisualizationSettings.YaxisType.ValueType = ...,
                title: builtins.str = ...,
                min: builtins.str = ...,
                max: builtins.str = ...,
                unit_format: yandex.cloud.monitoring.v3.unit_format_pb2.UnitFormat.ValueType = ...,
                precision: google.protobuf.wrappers_pb2.Int64Value | None = ...,
            ) -> None: ...
            def HasField(self, field_name: typing.Literal["precision", b"precision"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing.Literal["max", b"max", "min", b"min", "precision", b"precision", "title", b"title", "type", b"type", "unit_format", b"unit_format"]) -> None: ...

        @typing.final
        class YaxisSettings(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            LEFT_FIELD_NUMBER: builtins.int
            RIGHT_FIELD_NUMBER: builtins.int
            @property
            def left(self) -> global___ChartWidget.VisualizationSettings.Yaxis:
                """Left Y axis settings."""

            @property
            def right(self) -> global___ChartWidget.VisualizationSettings.Yaxis:
                """Right Y axis settings."""

            def __init__(
                self,
                *,
                left: global___ChartWidget.VisualizationSettings.Yaxis | None = ...,
                right: global___ChartWidget.VisualizationSettings.Yaxis | None = ...,
            ) -> None: ...
            def HasField(self, field_name: typing.Literal["left", b"left", "right", b"right"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing.Literal["left", b"left", "right", b"right"]) -> None: ...

        TYPE_FIELD_NUMBER: builtins.int
        NORMALIZE_FIELD_NUMBER: builtins.int
        INTERPOLATE_FIELD_NUMBER: builtins.int
        AGGREGATION_FIELD_NUMBER: builtins.int
        COLOR_SCHEME_SETTINGS_FIELD_NUMBER: builtins.int
        HEATMAP_SETTINGS_FIELD_NUMBER: builtins.int
        YAXIS_SETTINGS_FIELD_NUMBER: builtins.int
        TITLE_FIELD_NUMBER: builtins.int
        SHOW_LABELS_FIELD_NUMBER: builtins.int
        type: global___ChartWidget.VisualizationSettings.VisualizationType.ValueType
        """Visualization type."""
        normalize: builtins.bool
        """Normalize."""
        interpolate: global___ChartWidget.VisualizationSettings.Interpolate.ValueType
        """Interpolate."""
        aggregation: global___ChartWidget.VisualizationSettings.SeriesAggregation.ValueType
        """Aggregation."""
        title: builtins.str
        """Inside chart title."""
        show_labels: builtins.bool
        """Show chart labels."""
        @property
        def color_scheme_settings(self) -> global___ChartWidget.VisualizationSettings.ColorSchemeSettings:
            """Color scheme settings."""

        @property
        def heatmap_settings(self) -> global___ChartWidget.VisualizationSettings.HeatmapSettings:
            """Heatmap settings."""

        @property
        def yaxis_settings(self) -> global___ChartWidget.VisualizationSettings.YaxisSettings:
            """Y axis settings."""

        def __init__(
            self,
            *,
            type: global___ChartWidget.VisualizationSettings.VisualizationType.ValueType = ...,
            normalize: builtins.bool = ...,
            interpolate: global___ChartWidget.VisualizationSettings.Interpolate.ValueType = ...,
            aggregation: global___ChartWidget.VisualizationSettings.SeriesAggregation.ValueType = ...,
            color_scheme_settings: global___ChartWidget.VisualizationSettings.ColorSchemeSettings | None = ...,
            heatmap_settings: global___ChartWidget.VisualizationSettings.HeatmapSettings | None = ...,
            yaxis_settings: global___ChartWidget.VisualizationSettings.YaxisSettings | None = ...,
            title: builtins.str = ...,
            show_labels: builtins.bool = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["color_scheme_settings", b"color_scheme_settings", "heatmap_settings", b"heatmap_settings", "yaxis_settings", b"yaxis_settings"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["aggregation", b"aggregation", "color_scheme_settings", b"color_scheme_settings", "heatmap_settings", b"heatmap_settings", "interpolate", b"interpolate", "normalize", b"normalize", "show_labels", b"show_labels", "title", b"title", "type", b"type", "yaxis_settings", b"yaxis_settings"]) -> None: ...

    @typing.final
    class SeriesOverrides(google.protobuf.message.Message):
        """Series override settings."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        class _YaxisPosition:
            ValueType = typing.NewType("ValueType", builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _YaxisPositionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ChartWidget.SeriesOverrides._YaxisPosition.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            YAXIS_POSITION_UNSPECIFIED: ChartWidget.SeriesOverrides._YaxisPosition.ValueType  # 0
            """Not specified (left by default)."""
            YAXIS_POSITION_LEFT: ChartWidget.SeriesOverrides._YaxisPosition.ValueType  # 1
            """Left."""
            YAXIS_POSITION_RIGHT: ChartWidget.SeriesOverrides._YaxisPosition.ValueType  # 2
            """Right."""

        class YaxisPosition(_YaxisPosition, metaclass=_YaxisPositionEnumTypeWrapper): ...
        YAXIS_POSITION_UNSPECIFIED: ChartWidget.SeriesOverrides.YaxisPosition.ValueType  # 0
        """Not specified (left by default)."""
        YAXIS_POSITION_LEFT: ChartWidget.SeriesOverrides.YaxisPosition.ValueType  # 1
        """Left."""
        YAXIS_POSITION_RIGHT: ChartWidget.SeriesOverrides.YaxisPosition.ValueType  # 2
        """Right."""

        class _SeriesVisualizationType:
            ValueType = typing.NewType("ValueType", builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _SeriesVisualizationTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ChartWidget.SeriesOverrides._SeriesVisualizationType.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            SERIES_VISUALIZATION_TYPE_UNSPECIFIED: ChartWidget.SeriesOverrides._SeriesVisualizationType.ValueType  # 0
            """Not specified (line by default)."""
            SERIES_VISUALIZATION_TYPE_LINE: ChartWidget.SeriesOverrides._SeriesVisualizationType.ValueType  # 1
            """Line chart."""
            SERIES_VISUALIZATION_TYPE_STACK: ChartWidget.SeriesOverrides._SeriesVisualizationType.ValueType  # 2
            """Stack chart."""
            SERIES_VISUALIZATION_TYPE_COLUMN: ChartWidget.SeriesOverrides._SeriesVisualizationType.ValueType  # 3
            """Points as columns chart."""
            SERIES_VISUALIZATION_TYPE_POINTS: ChartWidget.SeriesOverrides._SeriesVisualizationType.ValueType  # 4
            """Points."""

        class SeriesVisualizationType(_SeriesVisualizationType, metaclass=_SeriesVisualizationTypeEnumTypeWrapper): ...
        SERIES_VISUALIZATION_TYPE_UNSPECIFIED: ChartWidget.SeriesOverrides.SeriesVisualizationType.ValueType  # 0
        """Not specified (line by default)."""
        SERIES_VISUALIZATION_TYPE_LINE: ChartWidget.SeriesOverrides.SeriesVisualizationType.ValueType  # 1
        """Line chart."""
        SERIES_VISUALIZATION_TYPE_STACK: ChartWidget.SeriesOverrides.SeriesVisualizationType.ValueType  # 2
        """Stack chart."""
        SERIES_VISUALIZATION_TYPE_COLUMN: ChartWidget.SeriesOverrides.SeriesVisualizationType.ValueType  # 3
        """Points as columns chart."""
        SERIES_VISUALIZATION_TYPE_POINTS: ChartWidget.SeriesOverrides.SeriesVisualizationType.ValueType  # 4
        """Points."""

        @typing.final
        class SeriesOverrideSettings(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            NAME_FIELD_NUMBER: builtins.int
            COLOR_FIELD_NUMBER: builtins.int
            TYPE_FIELD_NUMBER: builtins.int
            STACK_NAME_FIELD_NUMBER: builtins.int
            GROW_DOWN_FIELD_NUMBER: builtins.int
            YAXIS_POSITION_FIELD_NUMBER: builtins.int
            name: builtins.str
            """Series name or empty."""
            color: builtins.str
            """Series color or empty."""
            type: global___ChartWidget.SeriesOverrides.SeriesVisualizationType.ValueType
            """Type."""
            stack_name: builtins.str
            """Stack name or empty."""
            grow_down: builtins.bool
            """Stack grow down."""
            yaxis_position: global___ChartWidget.SeriesOverrides.YaxisPosition.ValueType
            """Yaxis position."""
            def __init__(
                self,
                *,
                name: builtins.str = ...,
                color: builtins.str = ...,
                type: global___ChartWidget.SeriesOverrides.SeriesVisualizationType.ValueType = ...,
                stack_name: builtins.str = ...,
                grow_down: builtins.bool = ...,
                yaxis_position: global___ChartWidget.SeriesOverrides.YaxisPosition.ValueType = ...,
            ) -> None: ...
            def ClearField(self, field_name: typing.Literal["color", b"color", "grow_down", b"grow_down", "name", b"name", "stack_name", b"stack_name", "type", b"type", "yaxis_position", b"yaxis_position"]) -> None: ...

        NAME_FIELD_NUMBER: builtins.int
        TARGET_INDEX_FIELD_NUMBER: builtins.int
        SETTINGS_FIELD_NUMBER: builtins.int
        name: builtins.str
        """Series name."""
        target_index: builtins.str
        """Target index."""
        @property
        def settings(self) -> global___ChartWidget.SeriesOverrides.SeriesOverrideSettings:
            """Required. Override settings."""

        def __init__(
            self,
            *,
            name: builtins.str = ...,
            target_index: builtins.str = ...,
            settings: global___ChartWidget.SeriesOverrides.SeriesOverrideSettings | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["name", b"name", "settings", b"settings", "target_index", b"target_index", "type", b"type"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["name", b"name", "settings", b"settings", "target_index", b"target_index", "type", b"type"]) -> None: ...
        def WhichOneof(self, oneof_group: typing.Literal["type", b"type"]) -> typing.Literal["name", "target_index"] | None: ...

    @typing.final
    class NameHidingSettings(google.protobuf.message.Message):
        """Name hiding settings."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        POSITIVE_FIELD_NUMBER: builtins.int
        NAMES_FIELD_NUMBER: builtins.int
        positive: builtins.bool
        """True if we want to show concrete series names only, false if we want to hide concrete series names."""
        @property
        def names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
            """Series names to show or hide."""

        def __init__(
            self,
            *,
            positive: builtins.bool = ...,
            names: collections.abc.Iterable[builtins.str] | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["names", b"names", "positive", b"positive"]) -> None: ...

    ID_FIELD_NUMBER: builtins.int
    QUERIES_FIELD_NUMBER: builtins.int
    VISUALIZATION_SETTINGS_FIELD_NUMBER: builtins.int
    SERIES_OVERRIDES_FIELD_NUMBER: builtins.int
    NAME_HIDING_SETTINGS_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    DISPLAY_LEGEND_FIELD_NUMBER: builtins.int
    FREEZE_FIELD_NUMBER: builtins.int
    id: builtins.str
    """Required. Chart ID."""
    description: builtins.str
    """Chart description in dashboard (not enabled in UI)."""
    title: builtins.str
    """Chart widget title."""
    display_legend: builtins.bool
    """Enable legend under chart."""
    freeze: global___ChartWidget.FreezeDuration.ValueType
    """Fixed time interval for chart."""
    @property
    def queries(self) -> global___ChartWidget.Queries:
        """Queries."""

    @property
    def visualization_settings(self) -> global___ChartWidget.VisualizationSettings:
        """Visualization settings."""

    @property
    def series_overrides(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ChartWidget.SeriesOverrides]:
        """Override settings."""

    @property
    def name_hiding_settings(self) -> global___ChartWidget.NameHidingSettings:
        """Name hiding settings."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        queries: global___ChartWidget.Queries | None = ...,
        visualization_settings: global___ChartWidget.VisualizationSettings | None = ...,
        series_overrides: collections.abc.Iterable[global___ChartWidget.SeriesOverrides] | None = ...,
        name_hiding_settings: global___ChartWidget.NameHidingSettings | None = ...,
        description: builtins.str = ...,
        title: builtins.str = ...,
        display_legend: builtins.bool = ...,
        freeze: global___ChartWidget.FreezeDuration.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["name_hiding_settings", b"name_hiding_settings", "queries", b"queries", "visualization_settings", b"visualization_settings"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "display_legend", b"display_legend", "freeze", b"freeze", "id", b"id", "name_hiding_settings", b"name_hiding_settings", "queries", b"queries", "series_overrides", b"series_overrides", "title", b"title", "visualization_settings", b"visualization_settings"]) -> None: ...

global___ChartWidget = ChartWidget
