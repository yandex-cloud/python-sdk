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
class Payload(google.protobuf.message.Message):
    """A health check payload resource."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TEXT_FIELD_NUMBER: builtins.int
    text: builtins.str
    """Payload text."""
    def __init__(
        self,
        *,
        text: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["payload", b"payload", "text", b"text"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["payload", b"payload", "text", b"text"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["payload", b"payload"]) -> typing.Literal["text"] | None: ...

global___Payload = Payload
