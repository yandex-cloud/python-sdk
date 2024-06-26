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

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class TextContent(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MESSAGES_FIELD_NUMBER: builtins.int
    @property
    def messages(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Message]: ...
    def __init__(
        self,
        *,
        messages: collections.abc.Iterable[global___Message] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["messages", b"messages"]) -> None: ...

global___TextContent = TextContent

@typing.final
class Message(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_ID_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    TEXT_FIELD_NUMBER: builtins.int
    user_id: builtins.str
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def text(self) -> global___TextPayload: ...
    def __init__(
        self,
        *,
        user_id: builtins.str = ...,
        timestamp: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        text: global___TextPayload | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["payload", b"payload", "text", b"text", "timestamp", b"timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["payload", b"payload", "text", b"text", "timestamp", b"timestamp", "user_id", b"user_id"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["payload", b"payload"]) -> typing.Literal["text"] | None: ...

global___Message = Message

@typing.final
class TextPayload(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TEXT_FIELD_NUMBER: builtins.int
    text: builtins.str
    def __init__(
        self,
        *,
        text: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["text", b"text"]) -> None: ...

global___TextPayload = TextPayload
