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
class ActivateDatasetRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATASET_ID_FIELD_NUMBER: builtins.int
    PROJECT_ID_FIELD_NUMBER: builtins.int
    dataset_id: builtins.str
    project_id: builtins.str
    def __init__(
        self,
        *,
        dataset_id: builtins.str = ...,
        project_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["dataset_id", b"dataset_id", "project_id", b"project_id"]) -> None: ...

global___ActivateDatasetRequest = ActivateDatasetRequest

@typing.final
class DeactivateDatasetRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATASET_ID_FIELD_NUMBER: builtins.int
    PROJECT_ID_FIELD_NUMBER: builtins.int
    dataset_id: builtins.str
    project_id: builtins.str
    def __init__(
        self,
        *,
        dataset_id: builtins.str = ...,
        project_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["dataset_id", b"dataset_id", "project_id", b"project_id"]) -> None: ...

global___DeactivateDatasetRequest = DeactivateDatasetRequest
