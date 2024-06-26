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
import yandex.cloud.logging.v1.log_entry_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Export(google.protobuf.message.Message):
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
    CLOUD_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    GROUP_ID_FIELD_NUMBER: builtins.int
    SINK_ID_FIELD_NUMBER: builtins.int
    PARAMS_FIELD_NUMBER: builtins.int
    id: builtins.str
    """Export ID."""
    folder_id: builtins.str
    """Export folder ID."""
    cloud_id: builtins.str
    """Export cloud ID."""
    name: builtins.str
    """Export name."""
    description: builtins.str
    """Export description."""
    group_id: builtins.str
    """Group logs are exported from."""
    sink_id: builtins.str
    """Sink logs are exported to."""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Export creation time."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Export lables."""

    @property
    def params(self) -> global___ExportParams:
        """Parameters of logs filtration."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        folder_id: builtins.str = ...,
        cloud_id: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        group_id: builtins.str = ...,
        sink_id: builtins.str = ...,
        params: global___ExportParams | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at", "params", b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cloud_id", b"cloud_id", "created_at", b"created_at", "description", b"description", "folder_id", b"folder_id", "group_id", b"group_id", "id", b"id", "labels", b"labels", "name", b"name", "params", b"params", "sink_id", b"sink_id"]) -> None: ...

global___Export = Export

@typing.final
class ExportParams(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_TYPES_FIELD_NUMBER: builtins.int
    RESOURCE_IDS_FIELD_NUMBER: builtins.int
    STREAM_NAMES_FIELD_NUMBER: builtins.int
    LEVELS_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    filter: builtins.str
    @property
    def resource_types(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def resource_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def stream_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def levels(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[yandex.cloud.logging.v1.log_entry_pb2.LogLevel.Level.ValueType]: ...
    def __init__(
        self,
        *,
        resource_types: collections.abc.Iterable[builtins.str] | None = ...,
        resource_ids: collections.abc.Iterable[builtins.str] | None = ...,
        stream_names: collections.abc.Iterable[builtins.str] | None = ...,
        levels: collections.abc.Iterable[yandex.cloud.logging.v1.log_entry_pb2.LogLevel.Level.ValueType] | None = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["filter", b"filter", "levels", b"levels", "resource_ids", b"resource_ids", "resource_types", b"resource_types", "stream_names", b"stream_names"]) -> None: ...

global___ExportParams = ExportParams
