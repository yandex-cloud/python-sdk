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

class _MlModelType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _MlModelTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_MlModelType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    ML_MODEL_TYPE_UNSPECIFIED: _MlModelType.ValueType  # 0
    ML_MODEL_TYPE_CATBOOST: _MlModelType.ValueType  # 1
    """CatBoost model."""

class MlModelType(_MlModelType, metaclass=_MlModelTypeEnumTypeWrapper): ...

ML_MODEL_TYPE_UNSPECIFIED: MlModelType.ValueType  # 0
ML_MODEL_TYPE_CATBOOST: MlModelType.ValueType  # 1
"""CatBoost model."""
global___MlModelType = MlModelType

@typing.final
class MlModel(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the the model."""
    cluster_id: builtins.str
    """ID of the ClickHouse cluster that the model belongs to."""
    type: global___MlModelType.ValueType
    """Type of the model."""
    uri: builtins.str
    """Model file URL. You can only use models stored in Object Storage."""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        cluster_id: builtins.str = ...,
        type: global___MlModelType.ValueType = ...,
        uri: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "name", b"name", "type", b"type", "uri", b"uri"]) -> None: ...

global___MlModel = MlModel