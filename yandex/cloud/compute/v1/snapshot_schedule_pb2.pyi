"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.duration_pb2
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
class SnapshotSchedule(google.protobuf.message.Message):
    """A snapshot schedule. For details about the concept, see [documentation](/docs/compute/concepts/snapshot-schedule)."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[SnapshotSchedule._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: SnapshotSchedule._Status.ValueType  # 0
        CREATING: SnapshotSchedule._Status.ValueType  # 1
        """The snapshot schedule is being created."""
        ACTIVE: SnapshotSchedule._Status.ValueType  # 2
        """The snapshot schedule is on: new disk snapshots will be created, old ones deleted
        (if [SnapshotSchedule.retention_policy] is specified).
        """
        INACTIVE: SnapshotSchedule._Status.ValueType  # 3
        """The schedule is interrupted, snapshots won't be created or deleted."""
        DELETING: SnapshotSchedule._Status.ValueType  # 4
        """The schedule is being deleted."""
        UPDATING: SnapshotSchedule._Status.ValueType  # 5
        """Changes are being made to snapshot schedule settings or a list of attached disks."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...
    STATUS_UNSPECIFIED: SnapshotSchedule.Status.ValueType  # 0
    CREATING: SnapshotSchedule.Status.ValueType  # 1
    """The snapshot schedule is being created."""
    ACTIVE: SnapshotSchedule.Status.ValueType  # 2
    """The snapshot schedule is on: new disk snapshots will be created, old ones deleted
    (if [SnapshotSchedule.retention_policy] is specified).
    """
    INACTIVE: SnapshotSchedule.Status.ValueType  # 3
    """The schedule is interrupted, snapshots won't be created or deleted."""
    DELETING: SnapshotSchedule.Status.ValueType  # 4
    """The schedule is being deleted."""
    UPDATING: SnapshotSchedule.Status.ValueType  # 5
    """Changes are being made to snapshot schedule settings or a list of attached disks."""

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
    STATUS_FIELD_NUMBER: builtins.int
    SCHEDULE_POLICY_FIELD_NUMBER: builtins.int
    RETENTION_PERIOD_FIELD_NUMBER: builtins.int
    SNAPSHOT_COUNT_FIELD_NUMBER: builtins.int
    SNAPSHOT_SPEC_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the snapshot schedule."""
    folder_id: builtins.str
    """ID of the folder that the snapshot schedule belongs to."""
    name: builtins.str
    """Name of the snapshot schedule.

    The name is unique within the folder.
    """
    description: builtins.str
    """Description of the snapshot schedule."""
    status: global___SnapshotSchedule.Status.ValueType
    """Status of the snapshot schedule."""
    snapshot_count: builtins.int
    """Retention count of the snapshot schedule. Once the number of snapshots created by the schedule exceeds this
    number, the oldest ones are automatically deleted. E.g. if the number is 5, the first snapshot is deleted
    after the sixth one is created, the second is deleted after the seventh one is created, and so on.
    """
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Snapshot schedule labels as `key:value` pairs."""

    @property
    def schedule_policy(self) -> global___SchedulePolicy:
        """Frequency settings of the snapshot schedule."""

    @property
    def retention_period(self) -> google.protobuf.duration_pb2.Duration:
        """Retention period of the snapshot schedule. Once a snapshot created by the schedule reaches this age, it is
        automatically deleted.
        """

    @property
    def snapshot_spec(self) -> global___SnapshotSpec:
        """Attributes of snapshots created by the snapshot schedule."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        folder_id: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        status: global___SnapshotSchedule.Status.ValueType = ...,
        schedule_policy: global___SchedulePolicy | None = ...,
        retention_period: google.protobuf.duration_pb2.Duration | None = ...,
        snapshot_count: builtins.int = ...,
        snapshot_spec: global___SnapshotSpec | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at", "retention_period", b"retention_period", "retention_policy", b"retention_policy", "schedule_policy", b"schedule_policy", "snapshot_count", b"snapshot_count", "snapshot_spec", b"snapshot_spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["created_at", b"created_at", "description", b"description", "folder_id", b"folder_id", "id", b"id", "labels", b"labels", "name", b"name", "retention_period", b"retention_period", "retention_policy", b"retention_policy", "schedule_policy", b"schedule_policy", "snapshot_count", b"snapshot_count", "snapshot_spec", b"snapshot_spec", "status", b"status"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["retention_policy", b"retention_policy"]) -> typing.Literal["retention_period", "snapshot_count"] | None: ...

global___SnapshotSchedule = SnapshotSchedule

@typing.final
class SchedulePolicy(google.protobuf.message.Message):
    """A resource for frequency settings of a snapshot schedule."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    START_AT_FIELD_NUMBER: builtins.int
    EXPRESSION_FIELD_NUMBER: builtins.int
    expression: builtins.str
    """Cron expression for the snapshot schedule (UTC+0).

    The expression must consist of five fields (`Minutes Hours Day-of-month Month Day-of-week`) or be one of
    nonstandard predefined expressions (e.g. `@hourly`). For details about the format,
    see [documentation](/docs/compute/concepts/snapshot-schedule#cron)
    """
    @property
    def start_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Timestamp for creating the first snapshot."""

    def __init__(
        self,
        *,
        start_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        expression: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["start_at", b"start_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["expression", b"expression", "start_at", b"start_at"]) -> None: ...

global___SchedulePolicy = SchedulePolicy

@typing.final
class SnapshotSpec(google.protobuf.message.Message):
    """A resource for attributes of snapshots created by the snapshot schedule."""

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

    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    description: builtins.str
    """Description of the created snapshot."""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Snapshot labels as `key:value` pairs."""

    def __init__(
        self,
        *,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "labels", b"labels"]) -> None: ...

global___SnapshotSpec = SnapshotSpec
