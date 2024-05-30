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
import yandex.cloud.monitoring.v3.unit_format_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class LabelValuesParameter(google.protobuf.message.Message):
    """Label values parameter."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    SELECTORS_FIELD_NUMBER: builtins.int
    LABEL_KEY_FIELD_NUMBER: builtins.int
    MULTISELECTABLE_FIELD_NUMBER: builtins.int
    DEFAULT_VALUES_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """Required. Folder ID."""
    selectors: builtins.str
    """Required. Selectors to select metric label values."""
    label_key: builtins.str
    """Required. Label key to list label values."""
    multiselectable: builtins.bool
    """Specifies the multiselectable values of parameter."""
    @property
    def default_values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Default values."""

    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        selectors: builtins.str = ...,
        label_key: builtins.str = ...,
        multiselectable: builtins.bool = ...,
        default_values: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["container", b"container", "folder_id", b"folder_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["container", b"container", "default_values", b"default_values", "folder_id", b"folder_id", "label_key", b"label_key", "multiselectable", b"multiselectable", "selectors", b"selectors"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["container", b"container"]) -> typing.Literal["folder_id"] | None: ...

global___LabelValuesParameter = LabelValuesParameter

@typing.final
class CustomParameter(google.protobuf.message.Message):
    """Custom parameter."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUES_FIELD_NUMBER: builtins.int
    MULTISELECTABLE_FIELD_NUMBER: builtins.int
    DEFAULT_VALUES_FIELD_NUMBER: builtins.int
    multiselectable: builtins.bool
    """Specifies the multiselectable values of parameter."""
    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Required. List of parameter values."""

    @property
    def default_values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Default values."""

    def __init__(
        self,
        *,
        values: collections.abc.Iterable[builtins.str] | None = ...,
        multiselectable: builtins.bool = ...,
        default_values: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["default_values", b"default_values", "multiselectable", b"multiselectable", "values", b"values"]) -> None: ...

global___CustomParameter = CustomParameter

@typing.final
class TextParameter(google.protobuf.message.Message):
    """Text parameter."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEFAULT_VALUE_FIELD_NUMBER: builtins.int
    default_value: builtins.str
    """Default value."""
    def __init__(
        self,
        *,
        default_value: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["default_value", b"default_value"]) -> None: ...

global___TextParameter = TextParameter

@typing.final
class DoubleParameter(google.protobuf.message.Message):
    """Double parameter."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEFAULT_VALUE_FIELD_NUMBER: builtins.int
    UNIT_FORMAT_FIELD_NUMBER: builtins.int
    default_value: builtins.float
    """Default value."""
    unit_format: yandex.cloud.monitoring.v3.unit_format_pb2.UnitFormat.ValueType
    """Parameter unit."""
    def __init__(
        self,
        *,
        default_value: builtins.float = ...,
        unit_format: yandex.cloud.monitoring.v3.unit_format_pb2.UnitFormat.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["default_value", b"default_value", "unit_format", b"unit_format"]) -> None: ...

global___DoubleParameter = DoubleParameter

@typing.final
class IntegerParameter(google.protobuf.message.Message):
    """Integer parameter."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEFAULT_VALUE_FIELD_NUMBER: builtins.int
    UNIT_FORMAT_FIELD_NUMBER: builtins.int
    default_value: builtins.int
    """Default value."""
    unit_format: yandex.cloud.monitoring.v3.unit_format_pb2.UnitFormat.ValueType
    """Parameter unit."""
    def __init__(
        self,
        *,
        default_value: builtins.int = ...,
        unit_format: yandex.cloud.monitoring.v3.unit_format_pb2.UnitFormat.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["default_value", b"default_value", "unit_format", b"unit_format"]) -> None: ...

global___IntegerParameter = IntegerParameter

@typing.final
class TextValuesParameter(google.protobuf.message.Message):
    """Text multiple values parameter."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEFAULT_VALUES_FIELD_NUMBER: builtins.int
    @property
    def default_values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Default value."""

    def __init__(
        self,
        *,
        default_values: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["default_values", b"default_values"]) -> None: ...

global___TextValuesParameter = TextValuesParameter

@typing.final
class Parameter(google.protobuf.message.Message):
    """Parameter."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    LABEL_VALUES_FIELD_NUMBER: builtins.int
    CUSTOM_FIELD_NUMBER: builtins.int
    TEXT_FIELD_NUMBER: builtins.int
    INTEGER_PARAMETER_FIELD_NUMBER: builtins.int
    DOUBLE_PARAMETER_FIELD_NUMBER: builtins.int
    TEXT_VALUES_FIELD_NUMBER: builtins.int
    HIDDEN_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Parameter identifier."""
    title: builtins.str
    """UI-visible title of the parameter."""
    hidden: builtins.bool
    """UI-visibility."""
    description: builtins.str
    """Parameter description."""
    @property
    def label_values(self) -> global___LabelValuesParameter:
        """Label values parameter."""

    @property
    def custom(self) -> global___CustomParameter:
        """Custom parameter."""

    @property
    def text(self) -> global___TextParameter:
        """Text parameter."""

    @property
    def integer_parameter(self) -> global___IntegerParameter:
        """Integer parameter."""

    @property
    def double_parameter(self) -> global___DoubleParameter:
        """Double parameter."""

    @property
    def text_values(self) -> global___TextValuesParameter:
        """Integer parameter."""

    def __init__(
        self,
        *,
        name: builtins.str = ...,
        title: builtins.str = ...,
        label_values: global___LabelValuesParameter | None = ...,
        custom: global___CustomParameter | None = ...,
        text: global___TextParameter | None = ...,
        integer_parameter: global___IntegerParameter | None = ...,
        double_parameter: global___DoubleParameter | None = ...,
        text_values: global___TextValuesParameter | None = ...,
        hidden: builtins.bool = ...,
        description: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["custom", b"custom", "data", b"data", "double_parameter", b"double_parameter", "integer_parameter", b"integer_parameter", "label_values", b"label_values", "text", b"text", "text_values", b"text_values"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["custom", b"custom", "data", b"data", "description", b"description", "double_parameter", b"double_parameter", "hidden", b"hidden", "integer_parameter", b"integer_parameter", "label_values", b"label_values", "name", b"name", "text", b"text", "text_values", b"text_values", "title", b"title"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["data", b"data"]) -> typing.Literal["label_values", "custom", "text", "integer_parameter", "double_parameter", "text_values"] | None: ...

global___Parameter = Parameter

@typing.final
class Parametrization(google.protobuf.message.Message):
    """Parametrization."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARAMETERS_FIELD_NUMBER: builtins.int
    SELECTORS_FIELD_NUMBER: builtins.int
    selectors: builtins.str
    """Predefined selectors."""
    @property
    def parameters(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Parameter]:
        """Parameters."""

    def __init__(
        self,
        *,
        parameters: collections.abc.Iterable[global___Parameter] | None = ...,
        selectors: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["parameters", b"parameters", "selectors", b"selectors"]) -> None: ...

global___Parametrization = Parametrization
