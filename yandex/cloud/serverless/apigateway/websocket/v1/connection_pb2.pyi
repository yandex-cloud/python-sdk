"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Connection(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    GATEWAY_ID_FIELD_NUMBER: builtins.int
    IDENTITY_FIELD_NUMBER: builtins.int
    CONNECTED_AT_FIELD_NUMBER: builtins.int
    LAST_ACTIVE_AT_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the connection."""
    gateway_id: builtins.str
    """ID of the API Gateway."""
    @property
    def identity(self) -> global___Identity:
        """The information about the caller making the request to API Gateway."""

    @property
    def connected_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The timestamp at which connection was established."""

    @property
    def last_active_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The timestamp at which connection was last accessed."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        gateway_id: builtins.str = ...,
        identity: global___Identity | None = ...,
        connected_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        last_active_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["connected_at", b"connected_at", "identity", b"identity", "last_active_at", b"last_active_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["connected_at", b"connected_at", "gateway_id", b"gateway_id", "id", b"id", "identity", b"identity", "last_active_at", b"last_active_at"]) -> None: ...

global___Connection = Connection

@typing.final
class Identity(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SOURCE_IP_FIELD_NUMBER: builtins.int
    USER_AGENT_FIELD_NUMBER: builtins.int
    source_ip: builtins.str
    """The source IP address of the caller making the request to API Gateway."""
    user_agent: builtins.str
    """The User Agent of the caller making the request to API Gateway."""
    def __init__(
        self,
        *,
        source_ip: builtins.str = ...,
        user_agent: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["source_ip", b"source_ip", "user_agent", b"user_agent"]) -> None: ...

global___Identity = Identity
