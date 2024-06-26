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
class UserSshKey(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    SUBJECT_ID_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    FINGERPRINT_FIELD_NUMBER: builtins.int
    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    EXPIRES_AT_FIELD_NUMBER: builtins.int
    id: builtins.str
    subject_id: builtins.str
    data: builtins.str
    name: builtins.str
    fingerprint: builtins.str
    organization_id: builtins.str
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def expires_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Used for temporary keys, if empty the key doesn't expire"""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        subject_id: builtins.str = ...,
        data: builtins.str = ...,
        name: builtins.str = ...,
        fingerprint: builtins.str = ...,
        organization_id: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        expires_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at", "expires_at", b"expires_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["created_at", b"created_at", "data", b"data", "expires_at", b"expires_at", "fingerprint", b"fingerprint", "id", b"id", "name", b"name", "organization_id", b"organization_id", "subject_id", b"subject_id"]) -> None: ...

global___UserSshKey = UserSshKey
