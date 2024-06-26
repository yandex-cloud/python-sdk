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
class ObjectStorage(google.protobuf.message.Message):
    """Reference to a file stored in Object Storage."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BUCKET_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    bucket: builtins.str
    """Bucket name."""
    name: builtins.str
    """File name."""
    def __init__(
        self,
        *,
        bucket: builtins.str = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["bucket", b"bucket", "name", b"name"]) -> None: ...

global___ObjectStorage = ObjectStorage
