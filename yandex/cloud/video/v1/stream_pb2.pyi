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
import google.protobuf.wrappers_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Stream(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _StreamStatus:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StreamStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Stream._StreamStatus.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STREAM_STATUS_UNSPECIFIED: Stream._StreamStatus.ValueType  # 0
        """Stream status unspecified."""
        OFFLINE: Stream._StreamStatus.ValueType  # 1
        """Stream offline."""
        PREPARING: Stream._StreamStatus.ValueType  # 2
        """Preparing the infrastructure for receiving video signal."""
        READY: Stream._StreamStatus.ValueType  # 3
        """Everything is ready to launch stream."""
        ONAIR: Stream._StreamStatus.ValueType  # 4
        """Stream onair."""
        FINISHED: Stream._StreamStatus.ValueType  # 5
        """Stream finished."""

    class StreamStatus(_StreamStatus, metaclass=_StreamStatusEnumTypeWrapper):
        """Stream status."""

    STREAM_STATUS_UNSPECIFIED: Stream.StreamStatus.ValueType  # 0
    """Stream status unspecified."""
    OFFLINE: Stream.StreamStatus.ValueType  # 1
    """Stream offline."""
    PREPARING: Stream.StreamStatus.ValueType  # 2
    """Preparing the infrastructure for receiving video signal."""
    READY: Stream.StreamStatus.ValueType  # 3
    """Everything is ready to launch stream."""
    ONAIR: Stream.StreamStatus.ValueType  # 4
    """Stream onair."""
    FINISHED: Stream.StreamStatus.ValueType  # 5
    """Stream finished."""

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
    CHANNEL_ID_FIELD_NUMBER: builtins.int
    LINE_ID_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    THUMBNAIL_ID_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    START_TIME_FIELD_NUMBER: builtins.int
    PUBLISH_TIME_FIELD_NUMBER: builtins.int
    FINISH_TIME_FIELD_NUMBER: builtins.int
    AUTO_PUBLISH_FIELD_NUMBER: builtins.int
    ON_DEMAND_FIELD_NUMBER: builtins.int
    SCHEDULE_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    UPDATED_AT_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the stream."""
    channel_id: builtins.str
    """ID of the channel where the stream was created."""
    line_id: builtins.str
    """ID of the line to which stream is linked."""
    title: builtins.str
    """Stream title."""
    description: builtins.str
    """Stream description."""
    thumbnail_id: builtins.str
    """ID of the thumbnail."""
    status: global___Stream.StreamStatus.ValueType
    """Stream status."""
    @property
    def start_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Stream start time."""

    @property
    def publish_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Stream publish time. Time when stream switched to ONAIR status."""

    @property
    def finish_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Stream finish time."""

    @property
    def auto_publish(self) -> google.protobuf.wrappers_pb2.BoolValue:
        """Automatically publish stream when ready.
        Switches status from READY to ONAIR.
        """

    @property
    def on_demand(self) -> global___OnDemand:
        """On-demand stream. Starts immediately when a signal appears."""

    @property
    def schedule(self) -> global___Schedule:
        """Schedule stream. Starts or finished at the specified time."""

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time when stream was created."""

    @property
    def updated_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time of last stream update."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Custom labels as `` key:value `` pairs. Maximum 64 per resource."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        channel_id: builtins.str = ...,
        line_id: builtins.str = ...,
        title: builtins.str = ...,
        description: builtins.str = ...,
        thumbnail_id: builtins.str = ...,
        status: global___Stream.StreamStatus.ValueType = ...,
        start_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        publish_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        finish_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        auto_publish: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        on_demand: global___OnDemand | None = ...,
        schedule: global___Schedule | None = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        updated_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["auto_publish", b"auto_publish", "created_at", b"created_at", "finish_time", b"finish_time", "on_demand", b"on_demand", "publish_time", b"publish_time", "schedule", b"schedule", "start_time", b"start_time", "stream_type", b"stream_type", "updated_at", b"updated_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["auto_publish", b"auto_publish", "channel_id", b"channel_id", "created_at", b"created_at", "description", b"description", "finish_time", b"finish_time", "id", b"id", "labels", b"labels", "line_id", b"line_id", "on_demand", b"on_demand", "publish_time", b"publish_time", "schedule", b"schedule", "start_time", b"start_time", "status", b"status", "stream_type", b"stream_type", "thumbnail_id", b"thumbnail_id", "title", b"title", "updated_at", b"updated_at"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["stream_type", b"stream_type"]) -> typing.Literal["on_demand", "schedule"] | None: ...

global___Stream = Stream

@typing.final
class OnDemand(google.protobuf.message.Message):
    """On-demand stream type.
    This type of streams should be started and finished explicitly.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___OnDemand = OnDemand

@typing.final
class Schedule(google.protobuf.message.Message):
    """Schedule stream type.
    This type of streams start and finish automatically at the specified time.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    START_TIME_FIELD_NUMBER: builtins.int
    FINISH_TIME_FIELD_NUMBER: builtins.int
    @property
    def start_time(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def finish_time(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(
        self,
        *,
        start_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        finish_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["finish_time", b"finish_time", "start_time", b"start_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["finish_time", b"finish_time", "start_time", b"start_time"]) -> None: ...

global___Schedule = Schedule
