"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Timeline(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PERIOD_FIELD_NUMBER: builtins.int
    REFRESH_INTERVAL_FIELD_NUMBER: builtins.int
    period: builtins.str
    """default time window"""
    refresh_interval: builtins.int
    """default refresh interval"""
    def __init__(
        self,
        *,
        period: builtins.str = ...,
        refresh_interval: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["period", b"period", "refresh_interval", b"refresh_interval"]) -> None: ...

global___Timeline = Timeline
