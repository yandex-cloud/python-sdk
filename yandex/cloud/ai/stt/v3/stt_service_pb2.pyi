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
class GetRecognitionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERATION_ID_FIELD_NUMBER: builtins.int
    operation_id: builtins.str
    def __init__(
        self,
        *,
        operation_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["operation_id", b"operation_id"]) -> None: ...

global___GetRecognitionRequest = GetRecognitionRequest
