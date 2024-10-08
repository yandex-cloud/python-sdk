"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import yandex.cloud.ai.common.common_pb2
import yandex.cloud.ai.files.v1.file_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class CreateFileRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class LabelsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    FOLDER_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    MIME_TYPE_FIELD_NUMBER: builtins.int
    CONTENT_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    EXPIRATION_CONFIG_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    name: builtins.str
    description: builtins.str
    mime_type: builtins.str
    content: builtins.bytes
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    @property
    def expiration_config(self) -> yandex.cloud.ai.common.common_pb2.ExpirationConfig: ...
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        mime_type: builtins.str = ...,
        content: builtins.bytes = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        expiration_config: yandex.cloud.ai.common.common_pb2.ExpirationConfig | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["expiration_config", b"expiration_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["content", b"content", "description", b"description", "expiration_config", b"expiration_config", "folder_id", b"folder_id", "labels", b"labels", "mime_type", b"mime_type", "name", b"name"]) -> None: ...

global___CreateFileRequest = CreateFileRequest

@typing.final
class GetFileRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FILE_ID_FIELD_NUMBER: builtins.int
    file_id: builtins.str
    def __init__(
        self,
        *,
        file_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["file_id", b"file_id"]) -> None: ...

global___GetFileRequest = GetFileRequest

@typing.final
class GetFileUrlRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FILE_ID_FIELD_NUMBER: builtins.int
    file_id: builtins.str
    def __init__(
        self,
        *,
        file_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["file_id", b"file_id"]) -> None: ...

global___GetFileUrlRequest = GetFileUrlRequest

@typing.final
class GetFileUrlResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    URL_FIELD_NUMBER: builtins.int
    url: builtins.str
    def __init__(
        self,
        *,
        url: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["url", b"url"]) -> None: ...

global___GetFileUrlResponse = GetFileUrlResponse

@typing.final
class UpdateFileRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class LabelsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    FILE_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    EXPIRATION_CONFIG_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    file_id: builtins.str
    name: builtins.str
    description: builtins.str
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask: ...
    @property
    def expiration_config(self) -> yandex.cloud.ai.common.common_pb2.ExpirationConfig: ...
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    def __init__(
        self,
        *,
        file_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        expiration_config: yandex.cloud.ai.common.common_pb2.ExpirationConfig | None = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["expiration_config", b"expiration_config", "update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "expiration_config", b"expiration_config", "file_id", b"file_id", "labels", b"labels", "name", b"name", "update_mask", b"update_mask"]) -> None: ...

global___UpdateFileRequest = UpdateFileRequest

@typing.final
class DeleteFileRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FILE_ID_FIELD_NUMBER: builtins.int
    file_id: builtins.str
    def __init__(
        self,
        *,
        file_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["file_id", b"file_id"]) -> None: ...

global___DeleteFileRequest = DeleteFileRequest

@typing.final
class DeleteFileResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___DeleteFileResponse = DeleteFileResponse

@typing.final
class ListFilesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    page_size: builtins.int
    page_token: builtins.str
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["folder_id", b"folder_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListFilesRequest = ListFilesRequest

@typing.final
class ListFilesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FILES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    @property
    def files(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.ai.files.v1.file_pb2.File]: ...
    def __init__(
        self,
        *,
        files: collections.abc.Iterable[yandex.cloud.ai.files.v1.file_pb2.File] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["files", b"files", "next_page_token", b"next_page_token"]) -> None: ...

global___ListFilesResponse = ListFilesResponse
