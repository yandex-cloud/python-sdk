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
class ApiEndpoint(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    ADDRESS_FIELD_NUMBER: builtins.int
    id: builtins.str
    address: builtins.str
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        address: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["address", b"address", "id", b"id"]) -> None: ...

global___ApiEndpoint = ApiEndpoint
