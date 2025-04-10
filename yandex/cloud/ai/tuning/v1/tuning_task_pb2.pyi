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
class TuningTask(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[TuningTask._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: TuningTask._Status.ValueType  # 0
        CREATED: TuningTask._Status.ValueType  # 1
        PENDING: TuningTask._Status.ValueType  # 2
        IN_PROGRESS: TuningTask._Status.ValueType  # 3
        COMPLETED: TuningTask._Status.ValueType  # 4
        FAILED: TuningTask._Status.ValueType  # 5
        CANCELED: TuningTask._Status.ValueType  # 6
        DRAFT: TuningTask._Status.ValueType  # 7

    class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...
    STATUS_UNSPECIFIED: TuningTask.Status.ValueType  # 0
    CREATED: TuningTask.Status.ValueType  # 1
    PENDING: TuningTask.Status.ValueType  # 2
    IN_PROGRESS: TuningTask.Status.ValueType  # 3
    COMPLETED: TuningTask.Status.ValueType  # 4
    FAILED: TuningTask.Status.ValueType  # 5
    CANCELED: TuningTask.Status.ValueType  # 6
    DRAFT: TuningTask.Status.ValueType  # 7

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

    TASK_ID_FIELD_NUMBER: builtins.int
    OPERATION_ID_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    CREATED_BY_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    STARTED_AT_FIELD_NUMBER: builtins.int
    FINISHED_AT_FIELD_NUMBER: builtins.int
    SOURCE_MODEL_URI_FIELD_NUMBER: builtins.int
    TARGET_MODEL_URI_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    task_id: builtins.str
    operation_id: builtins.str
    status: global___TuningTask.Status.ValueType
    folder_id: builtins.str
    created_by: builtins.str
    source_model_uri: builtins.str
    target_model_uri: builtins.str
    name: builtins.str
    description: builtins.str
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def started_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def finished_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    def __init__(
        self,
        *,
        task_id: builtins.str = ...,
        operation_id: builtins.str = ...,
        status: global___TuningTask.Status.ValueType = ...,
        folder_id: builtins.str = ...,
        created_by: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        started_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        finished_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        source_model_uri: builtins.str = ...,
        target_model_uri: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at", "finished_at", b"finished_at", "started_at", b"started_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["created_at", b"created_at", "created_by", b"created_by", "description", b"description", "finished_at", b"finished_at", "folder_id", b"folder_id", "labels", b"labels", "name", b"name", "operation_id", b"operation_id", "source_model_uri", b"source_model_uri", "started_at", b"started_at", "status", b"status", "target_model_uri", b"target_model_uri", "task_id", b"task_id"]) -> None: ...

global___TuningTask = TuningTask
