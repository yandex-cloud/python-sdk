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
class ActivateS3Request(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    S3_ID_FIELD_NUMBER: builtins.int
    PROJECT_ID_FIELD_NUMBER: builtins.int
    s3_id: builtins.str
    project_id: builtins.str
    def __init__(
        self,
        *,
        s3_id: builtins.str = ...,
        project_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["project_id", b"project_id", "s3_id", b"s3_id"]) -> None: ...

global___ActivateS3Request = ActivateS3Request

@typing.final
class DeactivateS3Request(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    S3_ID_FIELD_NUMBER: builtins.int
    PROJECT_ID_FIELD_NUMBER: builtins.int
    s3_id: builtins.str
    project_id: builtins.str
    def __init__(
        self,
        *,
        s3_id: builtins.str = ...,
        project_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["project_id", b"project_id", "s3_id", b"s3_id"]) -> None: ...

global___DeactivateS3Request = DeactivateS3Request
