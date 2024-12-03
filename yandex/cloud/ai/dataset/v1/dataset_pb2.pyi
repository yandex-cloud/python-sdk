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
import google.protobuf.timestamp_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class DatasetInfo(google.protobuf.message.Message):
    """Information about the dataset."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[DatasetInfo._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: DatasetInfo._Status.ValueType  # 0
        DRAFT: DatasetInfo._Status.ValueType  # 1
        VALIDATING: DatasetInfo._Status.ValueType  # 2
        READY: DatasetInfo._Status.ValueType  # 3
        INVALID: DatasetInfo._Status.ValueType  # 4
        DELETING: DatasetInfo._Status.ValueType  # 5

    class Status(_Status, metaclass=_StatusEnumTypeWrapper):
        """Status of the dataset."""

    STATUS_UNSPECIFIED: DatasetInfo.Status.ValueType  # 0
    DRAFT: DatasetInfo.Status.ValueType  # 1
    VALIDATING: DatasetInfo.Status.ValueType  # 2
    READY: DatasetInfo.Status.ValueType  # 3
    INVALID: DatasetInfo.Status.ValueType  # 4
    DELETING: DatasetInfo.Status.ValueType  # 5

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

    DATASET_ID_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    TASK_TYPE_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    UPDATED_AT_FIELD_NUMBER: builtins.int
    ROWS_FIELD_NUMBER: builtins.int
    SIZE_BYTES_FIELD_NUMBER: builtins.int
    CREATED_BY_ID_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    CREATED_BY_FIELD_NUMBER: builtins.int
    UPDATED_BY_FIELD_NUMBER: builtins.int
    dataset_id: builtins.str
    """ID of the dataset."""
    folder_id: builtins.str
    """Folder ID of the dataset."""
    name: builtins.str
    """Name of the dataset."""
    description: builtins.str
    """Description of the dataset."""
    metadata: builtins.str
    """Metadata of the dataset."""
    status: global___DatasetInfo.Status.ValueType
    """Status of the dataset."""
    task_type: builtins.str
    """Task type of the dataset."""
    rows: builtins.int
    """Number of rows in the dataset."""
    size_bytes: builtins.int
    """Size of the dataset."""
    created_by_id: builtins.str
    """Deprecated. Use created_by instead"""
    created_by: builtins.str
    """User ID of the dataset's creator."""
    updated_by: builtins.str
    """User ID of the dataset's last updater."""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Create dataset timestamp."""

    @property
    def updated_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Update dataset timestamp."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Labels of the dataset"""

    def __init__(
        self,
        *,
        dataset_id: builtins.str = ...,
        folder_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        metadata: builtins.str = ...,
        status: global___DatasetInfo.Status.ValueType = ...,
        task_type: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        updated_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        rows: builtins.int = ...,
        size_bytes: builtins.int = ...,
        created_by_id: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        created_by: builtins.str = ...,
        updated_by: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at", "updated_at", b"updated_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["created_at", b"created_at", "created_by", b"created_by", "created_by_id", b"created_by_id", "dataset_id", b"dataset_id", "description", b"description", "folder_id", b"folder_id", "labels", b"labels", "metadata", b"metadata", "name", b"name", "rows", b"rows", "size_bytes", b"size_bytes", "status", b"status", "task_type", b"task_type", "updated_at", b"updated_at", "updated_by", b"updated_by"]) -> None: ...

global___DatasetInfo = DatasetInfo

@typing.final
class ValidationError(google.protobuf.message.Message):
    """Information about dataset validation error."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ERROR_FIELD_NUMBER: builtins.int
    ERROR_DESCRIPTION_FIELD_NUMBER: builtins.int
    ROW_NUMBERS_FIELD_NUMBER: builtins.int
    error: builtins.str
    """Name of the validation error."""
    error_description: builtins.str
    """Description of the validation error."""
    @property
    def row_numbers(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """Row numbers in which the error occurred."""

    def __init__(
        self,
        *,
        error: builtins.str = ...,
        error_description: builtins.str = ...,
        row_numbers: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["error", b"error", "error_description", b"error_description", "row_numbers", b"row_numbers"]) -> None: ...

global___ValidationError = ValidationError
