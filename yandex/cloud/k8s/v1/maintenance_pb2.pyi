"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import google.type.dayofweek_pb2
import google.type.timeofday_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class MaintenanceWindow(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ANYTIME_FIELD_NUMBER: builtins.int
    DAILY_MAINTENANCE_WINDOW_FIELD_NUMBER: builtins.int
    WEEKLY_MAINTENANCE_WINDOW_FIELD_NUMBER: builtins.int
    @property
    def anytime(self) -> global___AnytimeMaintenanceWindow:
        """Updating the master at any time."""

    @property
    def daily_maintenance_window(self) -> global___DailyMaintenanceWindow:
        """Updating the master on any day during the specified time window."""

    @property
    def weekly_maintenance_window(self) -> global___WeeklyMaintenanceWindow:
        """Updating the master on selected days during the specified time window."""

    def __init__(
        self,
        *,
        anytime: global___AnytimeMaintenanceWindow | None = ...,
        daily_maintenance_window: global___DailyMaintenanceWindow | None = ...,
        weekly_maintenance_window: global___WeeklyMaintenanceWindow | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["anytime", b"anytime", "daily_maintenance_window", b"daily_maintenance_window", "policy", b"policy", "weekly_maintenance_window", b"weekly_maintenance_window"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["anytime", b"anytime", "daily_maintenance_window", b"daily_maintenance_window", "policy", b"policy", "weekly_maintenance_window", b"weekly_maintenance_window"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["policy", b"policy"]) -> typing.Literal["anytime", "daily_maintenance_window", "weekly_maintenance_window"] | None: ...

global___MaintenanceWindow = MaintenanceWindow

@typing.final
class AnytimeMaintenanceWindow(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___AnytimeMaintenanceWindow = AnytimeMaintenanceWindow

@typing.final
class DailyMaintenanceWindow(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    START_TIME_FIELD_NUMBER: builtins.int
    DURATION_FIELD_NUMBER: builtins.int
    @property
    def start_time(self) -> google.type.timeofday_pb2.TimeOfDay:
        """Window start time, in the UTC timezone."""

    @property
    def duration(self) -> google.protobuf.duration_pb2.Duration:
        """Window duration."""

    def __init__(
        self,
        *,
        start_time: google.type.timeofday_pb2.TimeOfDay | None = ...,
        duration: google.protobuf.duration_pb2.Duration | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["duration", b"duration", "start_time", b"start_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["duration", b"duration", "start_time", b"start_time"]) -> None: ...

global___DailyMaintenanceWindow = DailyMaintenanceWindow

@typing.final
class DaysOfWeekMaintenanceWindow(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DAYS_FIELD_NUMBER: builtins.int
    START_TIME_FIELD_NUMBER: builtins.int
    DURATION_FIELD_NUMBER: builtins.int
    @property
    def days(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[google.type.dayofweek_pb2.DayOfWeek.ValueType]:
        """Days of the week when automatic updates are allowed."""

    @property
    def start_time(self) -> google.type.timeofday_pb2.TimeOfDay:
        """Window start time, in the UTC timezone."""

    @property
    def duration(self) -> google.protobuf.duration_pb2.Duration:
        """Window duration."""

    def __init__(
        self,
        *,
        days: collections.abc.Iterable[google.type.dayofweek_pb2.DayOfWeek.ValueType] | None = ...,
        start_time: google.type.timeofday_pb2.TimeOfDay | None = ...,
        duration: google.protobuf.duration_pb2.Duration | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["duration", b"duration", "start_time", b"start_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["days", b"days", "duration", b"duration", "start_time", b"start_time"]) -> None: ...

global___DaysOfWeekMaintenanceWindow = DaysOfWeekMaintenanceWindow

@typing.final
class WeeklyMaintenanceWindow(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DAYS_OF_WEEK_FIELD_NUMBER: builtins.int
    @property
    def days_of_week(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DaysOfWeekMaintenanceWindow]:
        """Days of the week and the maintenance window for these days when automatic updates are allowed."""

    def __init__(
        self,
        *,
        days_of_week: collections.abc.Iterable[global___DaysOfWeekMaintenanceWindow] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["days_of_week", b"days_of_week"]) -> None: ...

global___WeeklyMaintenanceWindow = WeeklyMaintenanceWindow
