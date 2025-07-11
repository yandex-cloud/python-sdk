"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import yandex.cloud.video.v1.subtitle_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetSubtitleRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBTITLE_ID_FIELD_NUMBER: builtins.int
    subtitle_id: builtins.str
    """ID of the subtitle."""
    def __init__(
        self,
        *,
        subtitle_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["subtitle_id", b"subtitle_id"]) -> None: ...

global___GetSubtitleRequest = GetSubtitleRequest

@typing.final
class ListSubtitlesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    VIDEO_ID_FIELD_NUMBER: builtins.int
    page_size: builtins.int
    """The maximum number of the results per page to return.
    Default value: 100.
    """
    page_token: builtins.str
    """Page token for getting the next page of the result."""
    video_id: builtins.str
    """ID of the video."""
    def __init__(
        self,
        *,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        video_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["parent_id", b"parent_id", "video_id", b"video_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["page_size", b"page_size", "page_token", b"page_token", "parent_id", b"parent_id", "video_id", b"video_id"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["parent_id", b"parent_id"]) -> typing.Literal["video_id"] | None: ...

global___ListSubtitlesRequest = ListSubtitlesRequest

@typing.final
class ListSubtitlesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBTITLES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token for getting the next page."""
    @property
    def subtitles(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.video.v1.subtitle_pb2.Subtitle]: ...
    def __init__(
        self,
        *,
        subtitles: collections.abc.Iterable[yandex.cloud.video.v1.subtitle_pb2.Subtitle] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "subtitles", b"subtitles"]) -> None: ...

global___ListSubtitlesResponse = ListSubtitlesResponse

@typing.final
class CreateSubtitleRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LANGUAGE_FIELD_NUMBER: builtins.int
    LABEL_FIELD_NUMBER: builtins.int
    VIDEO_ID_FIELD_NUMBER: builtins.int
    UPLOAD_FIELD_NUMBER: builtins.int
    language: builtins.str
    """Subtitle language represented as a three-letter code according to ISO 639-2/T."""
    label: builtins.str
    """Contains the subtitle label (or title) that will be displayed on screen during video playback.
    Should provide a concise and accurate representation of the spoken content.
    If not provided, it will be auto-generated based on the specified language.
    """
    video_id: builtins.str
    """ID of the video."""
    @property
    def upload(self) -> global___SubtitleUploadParams:
        """Upload subtitle."""

    def __init__(
        self,
        *,
        language: builtins.str = ...,
        label: builtins.str = ...,
        video_id: builtins.str = ...,
        upload: global___SubtitleUploadParams | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["parent_id", b"parent_id", "source", b"source", "upload", b"upload", "video_id", b"video_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["label", b"label", "language", b"language", "parent_id", b"parent_id", "source", b"source", "upload", b"upload", "video_id", b"video_id"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["parent_id", b"parent_id"]) -> typing.Literal["video_id"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["source", b"source"]) -> typing.Literal["upload"] | None: ...

global___CreateSubtitleRequest = CreateSubtitleRequest

@typing.final
class SubtitleUploadParams(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FILENAME_FIELD_NUMBER: builtins.int
    filename: builtins.str
    def __init__(
        self,
        *,
        filename: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["filename", b"filename"]) -> None: ...

global___SubtitleUploadParams = SubtitleUploadParams

@typing.final
class CreateSubtitleMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBTITLE_ID_FIELD_NUMBER: builtins.int
    subtitle_id: builtins.str
    """ID of the subtitle."""
    def __init__(
        self,
        *,
        subtitle_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["subtitle_id", b"subtitle_id"]) -> None: ...

global___CreateSubtitleMetadata = CreateSubtitleMetadata

@typing.final
class GenerateSubtitleUploadURLRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBTITLE_ID_FIELD_NUMBER: builtins.int
    subtitle_id: builtins.str
    """ID of the subtitle."""
    def __init__(
        self,
        *,
        subtitle_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["subtitle_id", b"subtitle_id"]) -> None: ...

global___GenerateSubtitleUploadURLRequest = GenerateSubtitleUploadURLRequest

@typing.final
class GenerateSubtitleUploadURLResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    UPLOAD_URL_FIELD_NUMBER: builtins.int
    upload_url: builtins.str
    """Upload url."""
    def __init__(
        self,
        *,
        upload_url: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["upload_url", b"upload_url"]) -> None: ...

global___GenerateSubtitleUploadURLResponse = GenerateSubtitleUploadURLResponse

@typing.final
class DeleteSubtitleRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBTITLE_ID_FIELD_NUMBER: builtins.int
    subtitle_id: builtins.str
    """ID of the subtitle."""
    def __init__(
        self,
        *,
        subtitle_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["subtitle_id", b"subtitle_id"]) -> None: ...

global___DeleteSubtitleRequest = DeleteSubtitleRequest

@typing.final
class DeleteSubtitleMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBTITLE_ID_FIELD_NUMBER: builtins.int
    subtitle_id: builtins.str
    """ID of the subtitle."""
    def __init__(
        self,
        *,
        subtitle_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["subtitle_id", b"subtitle_id"]) -> None: ...

global___DeleteSubtitleMetadata = DeleteSubtitleMetadata
