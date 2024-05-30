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
class ActivateDockerImageRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_ID_FIELD_NUMBER: builtins.int
    DOCKER_ID_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    docker_id: builtins.str
    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
        docker_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["docker_id", b"docker_id", "project_id", b"project_id"]) -> None: ...

global___ActivateDockerImageRequest = ActivateDockerImageRequest
