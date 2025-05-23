"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import yandex.cloud.video.v1.episode_pb2
import yandex.cloud.video.v1.manifest_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetEpisodeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EPISODE_ID_FIELD_NUMBER: builtins.int
    episode_id: builtins.str
    """ID of the episode."""
    def __init__(
        self,
        *,
        episode_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["episode_id", b"episode_id"]) -> None: ...

global___GetEpisodeRequest = GetEpisodeRequest

@typing.final
class ListEpisodesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STREAM_ID_FIELD_NUMBER: builtins.int
    LINE_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    ORDER_BY_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    stream_id: builtins.str
    """ID of the stream."""
    line_id: builtins.str
    """ID of the line."""
    page_size: builtins.int
    """The maximum number of the results per page to return.
    Default value: 100.
    """
    page_token: builtins.str
    """Page token for getting the next page of the result."""
    order_by: builtins.str
    """By which column the listing should be ordered and in which direction,
    format is "<field> <order>" (e.g. "createdAt desc").
    Default: "id asc".
    Possible fields: ["id", "createdAt", "updatedAt"].
    Both snake_case and camelCase are supported for fields.
    """
    filter: builtins.str
    """Filter expression that filters resources listed in the response.
    Expressions are composed of terms connected by logic operators.
    If value contains spaces or quotes,
    it should be in quotes (`'` or `"`) with the inner quotes being backslash escaped.
    Supported logical operators: ["AND", "OR"].
    Supported string match operators: ["=", "!=", ":"].
    Operator ":" stands for substring matching.
    Filter expressions may also contain parentheses to group logical operands.
    Example: `key1='value' AND (key2!='\\'value\\'' OR key2:"\\"value\\"")`
    Supported fields: ["id", "title"].
    Both snake_case and camelCase are supported for fields.
    """
    def __init__(
        self,
        *,
        stream_id: builtins.str = ...,
        line_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        order_by: builtins.str = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["line_id", b"line_id", "parent_id", b"parent_id", "stream_id", b"stream_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["filter", b"filter", "line_id", b"line_id", "order_by", b"order_by", "page_size", b"page_size", "page_token", b"page_token", "parent_id", b"parent_id", "stream_id", b"stream_id"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["parent_id", b"parent_id"]) -> typing.Literal["stream_id", "line_id"] | None: ...

global___ListEpisodesRequest = ListEpisodesRequest

@typing.final
class ListEpisodesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EPISODES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token for getting the next page."""
    @property
    def episodes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.video.v1.episode_pb2.Episode]:
        """List of episodes for specific parent_id."""

    def __init__(
        self,
        *,
        episodes: collections.abc.Iterable[yandex.cloud.video.v1.episode_pb2.Episode] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["episodes", b"episodes", "next_page_token", b"next_page_token"]) -> None: ...

global___ListEpisodesResponse = ListEpisodesResponse

@typing.final
class BatchGetEpisodesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CHANNEL_ID_FIELD_NUMBER: builtins.int
    EPISODE_IDS_FIELD_NUMBER: builtins.int
    channel_id: builtins.str
    """ID of the channel."""
    @property
    def episode_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of requested episode IDs."""

    def __init__(
        self,
        *,
        channel_id: builtins.str = ...,
        episode_ids: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["channel_id", b"channel_id", "episode_ids", b"episode_ids"]) -> None: ...

global___BatchGetEpisodesRequest = BatchGetEpisodesRequest

@typing.final
class BatchGetEpisodesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EPISODES_FIELD_NUMBER: builtins.int
    @property
    def episodes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.video.v1.episode_pb2.Episode]:
        """List of episodes for specific channel."""

    def __init__(
        self,
        *,
        episodes: collections.abc.Iterable[yandex.cloud.video.v1.episode_pb2.Episode] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["episodes", b"episodes"]) -> None: ...

global___BatchGetEpisodesResponse = BatchGetEpisodesResponse

@typing.final
class CreateEpisodeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STREAM_ID_FIELD_NUMBER: builtins.int
    LINE_ID_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    THUMBNAIL_ID_FIELD_NUMBER: builtins.int
    START_TIME_FIELD_NUMBER: builtins.int
    FINISH_TIME_FIELD_NUMBER: builtins.int
    DVR_SECONDS_FIELD_NUMBER: builtins.int
    PUBLIC_ACCESS_FIELD_NUMBER: builtins.int
    AUTH_SYSTEM_ACCESS_FIELD_NUMBER: builtins.int
    SIGN_URL_ACCESS_FIELD_NUMBER: builtins.int
    stream_id: builtins.str
    """ID of the stream."""
    line_id: builtins.str
    """ID of the line."""
    title: builtins.str
    """Episode title."""
    description: builtins.str
    """Episode description."""
    thumbnail_id: builtins.str
    """ID of the thumbnail."""
    dvr_seconds: builtins.int
    """Enables episode DVR mode.
    Determines how many last seconds of the stream are available.

    Possible values:
     * `0`: infinite dvr size, the full length of the stream allowed to display
     * `>0`: size of dvr window in seconds, the minimum value is 30s
    """
    @property
    def start_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Episode start time."""

    @property
    def finish_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Episode finish time."""

    @property
    def public_access(self) -> global___EpisodePublicAccessParams:
        """Episode is available to everyone."""

    @property
    def auth_system_access(self) -> global___EpisodeAuthSystemAccessParams:
        """Checking access rights using the authorization system."""

    @property
    def sign_url_access(self) -> global___EpisodeSignURLAccessParams:
        """Checking access rights using url's signature."""

    def __init__(
        self,
        *,
        stream_id: builtins.str = ...,
        line_id: builtins.str = ...,
        title: builtins.str = ...,
        description: builtins.str = ...,
        thumbnail_id: builtins.str = ...,
        start_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        finish_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        dvr_seconds: builtins.int = ...,
        public_access: global___EpisodePublicAccessParams | None = ...,
        auth_system_access: global___EpisodeAuthSystemAccessParams | None = ...,
        sign_url_access: global___EpisodeSignURLAccessParams | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["access_rights", b"access_rights", "auth_system_access", b"auth_system_access", "finish_time", b"finish_time", "line_id", b"line_id", "parent_id", b"parent_id", "public_access", b"public_access", "sign_url_access", b"sign_url_access", "start_time", b"start_time", "stream_id", b"stream_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["access_rights", b"access_rights", "auth_system_access", b"auth_system_access", "description", b"description", "dvr_seconds", b"dvr_seconds", "finish_time", b"finish_time", "line_id", b"line_id", "parent_id", b"parent_id", "public_access", b"public_access", "sign_url_access", b"sign_url_access", "start_time", b"start_time", "stream_id", b"stream_id", "thumbnail_id", b"thumbnail_id", "title", b"title"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["access_rights", b"access_rights"]) -> typing.Literal["public_access", "auth_system_access", "sign_url_access"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["parent_id", b"parent_id"]) -> typing.Literal["stream_id", "line_id"] | None: ...

global___CreateEpisodeRequest = CreateEpisodeRequest

@typing.final
class EpisodePublicAccessParams(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___EpisodePublicAccessParams = EpisodePublicAccessParams

@typing.final
class EpisodeAuthSystemAccessParams(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___EpisodeAuthSystemAccessParams = EpisodeAuthSystemAccessParams

@typing.final
class EpisodeSignURLAccessParams(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___EpisodeSignURLAccessParams = EpisodeSignURLAccessParams

@typing.final
class CreateEpisodeMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EPISODE_ID_FIELD_NUMBER: builtins.int
    episode_id: builtins.str
    """ID of the episode."""
    def __init__(
        self,
        *,
        episode_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["episode_id", b"episode_id"]) -> None: ...

global___CreateEpisodeMetadata = CreateEpisodeMetadata

@typing.final
class UpdateEpisodeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EPISODE_ID_FIELD_NUMBER: builtins.int
    FIELD_MASK_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    THUMBNAIL_ID_FIELD_NUMBER: builtins.int
    START_TIME_FIELD_NUMBER: builtins.int
    FINISH_TIME_FIELD_NUMBER: builtins.int
    DVR_SECONDS_FIELD_NUMBER: builtins.int
    PUBLIC_ACCESS_FIELD_NUMBER: builtins.int
    AUTH_SYSTEM_ACCESS_FIELD_NUMBER: builtins.int
    SIGN_URL_ACCESS_FIELD_NUMBER: builtins.int
    episode_id: builtins.str
    """ID of the episode."""
    title: builtins.str
    """Episode title."""
    description: builtins.str
    """Episode description."""
    thumbnail_id: builtins.str
    """ID of the thumbnail."""
    dvr_seconds: builtins.int
    """Enables episode DVR mode.
    Determines how many last seconds of the stream are available.

    Possible values:
     * `0`: infinite dvr size, the full length of the stream allowed to display
     * `>0`: size of dvr window in seconds, the minimum value is 30s
    """
    @property
    def field_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which fields of the episode are going to be updated."""

    @property
    def start_time(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def finish_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Episode finish time."""

    @property
    def public_access(self) -> global___EpisodePublicAccessParams:
        """Episode is available to everyone."""

    @property
    def auth_system_access(self) -> global___EpisodeAuthSystemAccessParams:
        """Checking access rights using the authorization system."""

    @property
    def sign_url_access(self) -> global___EpisodeSignURLAccessParams:
        """Checking access rights using url's signature."""

    def __init__(
        self,
        *,
        episode_id: builtins.str = ...,
        field_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        title: builtins.str = ...,
        description: builtins.str = ...,
        thumbnail_id: builtins.str = ...,
        start_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        finish_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        dvr_seconds: builtins.int = ...,
        public_access: global___EpisodePublicAccessParams | None = ...,
        auth_system_access: global___EpisodeAuthSystemAccessParams | None = ...,
        sign_url_access: global___EpisodeSignURLAccessParams | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["access_rights", b"access_rights", "auth_system_access", b"auth_system_access", "field_mask", b"field_mask", "finish_time", b"finish_time", "public_access", b"public_access", "sign_url_access", b"sign_url_access", "start_time", b"start_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["access_rights", b"access_rights", "auth_system_access", b"auth_system_access", "description", b"description", "dvr_seconds", b"dvr_seconds", "episode_id", b"episode_id", "field_mask", b"field_mask", "finish_time", b"finish_time", "public_access", b"public_access", "sign_url_access", b"sign_url_access", "start_time", b"start_time", "thumbnail_id", b"thumbnail_id", "title", b"title"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["access_rights", b"access_rights"]) -> typing.Literal["public_access", "auth_system_access", "sign_url_access"] | None: ...

global___UpdateEpisodeRequest = UpdateEpisodeRequest

@typing.final
class UpdateEpisodeMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EPISODE_ID_FIELD_NUMBER: builtins.int
    episode_id: builtins.str
    """ID of the episode."""
    def __init__(
        self,
        *,
        episode_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["episode_id", b"episode_id"]) -> None: ...

global___UpdateEpisodeMetadata = UpdateEpisodeMetadata

@typing.final
class DeleteEpisodeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EPISODE_ID_FIELD_NUMBER: builtins.int
    episode_id: builtins.str
    """ID of the episode."""
    def __init__(
        self,
        *,
        episode_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["episode_id", b"episode_id"]) -> None: ...

global___DeleteEpisodeRequest = DeleteEpisodeRequest

@typing.final
class DeleteEpisodeMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EPISODE_ID_FIELD_NUMBER: builtins.int
    episode_id: builtins.str
    """ID of the episode."""
    def __init__(
        self,
        *,
        episode_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["episode_id", b"episode_id"]) -> None: ...

global___DeleteEpisodeMetadata = DeleteEpisodeMetadata

@typing.final
class BatchDeleteEpisodesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STREAM_ID_FIELD_NUMBER: builtins.int
    LINE_ID_FIELD_NUMBER: builtins.int
    EPISODE_IDS_FIELD_NUMBER: builtins.int
    stream_id: builtins.str
    """ID of the stream."""
    line_id: builtins.str
    """ID of the line."""
    @property
    def episode_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        stream_id: builtins.str = ...,
        line_id: builtins.str = ...,
        episode_ids: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["id", b"id", "line_id", b"line_id", "stream_id", b"stream_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["episode_ids", b"episode_ids", "id", b"id", "line_id", b"line_id", "stream_id", b"stream_id"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["id", b"id"]) -> typing.Literal["stream_id", "line_id"] | None: ...

global___BatchDeleteEpisodesRequest = BatchDeleteEpisodesRequest

@typing.final
class BatchDeleteEpisodesMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EPISODE_IDS_FIELD_NUMBER: builtins.int
    @property
    def episode_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        episode_ids: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["episode_ids", b"episode_ids"]) -> None: ...

global___BatchDeleteEpisodesMetadata = BatchDeleteEpisodesMetadata

@typing.final
class PerformEpisodeActionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EPISODE_ID_FIELD_NUMBER: builtins.int
    PUBLISH_FIELD_NUMBER: builtins.int
    UNPUBLISH_FIELD_NUMBER: builtins.int
    episode_id: builtins.str
    """ID of the episode."""
    @property
    def publish(self) -> global___PublishEpisodeAction: ...
    @property
    def unpublish(self) -> global___UnpublishEpisodeAction: ...
    def __init__(
        self,
        *,
        episode_id: builtins.str = ...,
        publish: global___PublishEpisodeAction | None = ...,
        unpublish: global___UnpublishEpisodeAction | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["action", b"action", "publish", b"publish", "unpublish", b"unpublish"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["action", b"action", "episode_id", b"episode_id", "publish", b"publish", "unpublish", b"unpublish"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["action", b"action"]) -> typing.Literal["publish", "unpublish"] | None: ...

global___PerformEpisodeActionRequest = PerformEpisodeActionRequest

@typing.final
class PublishEpisodeAction(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___PublishEpisodeAction = PublishEpisodeAction

@typing.final
class UnpublishEpisodeAction(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___UnpublishEpisodeAction = UnpublishEpisodeAction

@typing.final
class PerformEpisodeActionMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EPISODE_ID_FIELD_NUMBER: builtins.int
    episode_id: builtins.str
    """ID of the episode."""
    def __init__(
        self,
        *,
        episode_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["episode_id", b"episode_id"]) -> None: ...

global___PerformEpisodeActionMetadata = PerformEpisodeActionMetadata

@typing.final
class GetEpisodePlayerURLRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EPISODE_ID_FIELD_NUMBER: builtins.int
    PARAMS_FIELD_NUMBER: builtins.int
    SIGNED_URL_EXPIRATION_DURATION_FIELD_NUMBER: builtins.int
    episode_id: builtins.str
    """ID of the episode."""
    @property
    def params(self) -> global___EpisodePlayerParams: ...
    @property
    def signed_url_expiration_duration(self) -> google.protobuf.duration_pb2.Duration:
        """Optional field, used to set custom url expiration duration for episodes with sign_url_access"""

    def __init__(
        self,
        *,
        episode_id: builtins.str = ...,
        params: global___EpisodePlayerParams | None = ...,
        signed_url_expiration_duration: google.protobuf.duration_pb2.Duration | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["params", b"params", "signed_url_expiration_duration", b"signed_url_expiration_duration"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["episode_id", b"episode_id", "params", b"params", "signed_url_expiration_duration", b"signed_url_expiration_duration"]) -> None: ...

global___GetEpisodePlayerURLRequest = GetEpisodePlayerURLRequest

@typing.final
class EpisodePlayerParams(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MUTE_FIELD_NUMBER: builtins.int
    AUTOPLAY_FIELD_NUMBER: builtins.int
    HIDDEN_FIELD_NUMBER: builtins.int
    mute: builtins.bool
    """If true, a player will be muted by default."""
    autoplay: builtins.bool
    """If true, playback will start automatically."""
    hidden: builtins.bool
    """If true, a player interface will be hidden by default."""
    def __init__(
        self,
        *,
        mute: builtins.bool = ...,
        autoplay: builtins.bool = ...,
        hidden: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["autoplay", b"autoplay", "hidden", b"hidden", "mute", b"mute"]) -> None: ...

global___EpisodePlayerParams = EpisodePlayerParams

@typing.final
class GetEpisodePlayerURLResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PLAYER_URL_FIELD_NUMBER: builtins.int
    HTML_FIELD_NUMBER: builtins.int
    player_url: builtins.str
    """Direct link to the episode."""
    html: builtins.str
    """HTML embed code in Iframe format."""
    def __init__(
        self,
        *,
        player_url: builtins.str = ...,
        html: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["html", b"html", "player_url", b"player_url"]) -> None: ...

global___GetEpisodePlayerURLResponse = GetEpisodePlayerURLResponse

@typing.final
class GetEpisodeManifestsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EPISODE_ID_FIELD_NUMBER: builtins.int
    episode_id: builtins.str
    """ID of the episode."""
    def __init__(
        self,
        *,
        episode_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["episode_id", b"episode_id"]) -> None: ...

global___GetEpisodeManifestsRequest = GetEpisodeManifestsRequest

@typing.final
class GetEpisodeManifestsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MANIFESTS_FIELD_NUMBER: builtins.int
    @property
    def manifests(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.video.v1.manifest_pb2.Manifest]: ...
    def __init__(
        self,
        *,
        manifests: collections.abc.Iterable[yandex.cloud.video.v1.manifest_pb2.Manifest] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["manifests", b"manifests"]) -> None: ...

global___GetEpisodeManifestsResponse = GetEpisodeManifestsResponse
