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
import yandex.cloud.video.v1.channel_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetChannelRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CHANNEL_ID_FIELD_NUMBER: builtins.int
    channel_id: builtins.str
    """ID of the channel to retrieve."""
    def __init__(
        self,
        *,
        channel_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["channel_id", b"channel_id"]) -> None: ...

global___GetChannelRequest = GetChannelRequest

@typing.final
class ListChannelsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    ORDER_BY_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    organization_id: builtins.str
    """ID of the organization containing the channels to list."""
    page_size: builtins.int
    """The maximum number of channels to return per page."""
    page_token: builtins.str
    """Page token for retrieving the next page of results.
    This token is obtained from the next_page_token field in the previous ListChannelsResponse.
    """
    order_by: builtins.str
    """Specifies the ordering of results.
    Format is "<field> <order>" (e.g., "createdAt desc").
    Default: "id asc".
    Supported fields: ["id", "title", "createdAt", "updatedAt"].
    Both snake_case and camelCase field names are supported.
    """
    filter: builtins.str
    """Filter expression to narrow down the list of returned channels.
    Expressions consist of terms connected by logical operators.
    Values containing spaces or quotes must be enclosed in quotes (`'` or `"`)
    with inner quotes being backslash-escaped.

    Supported logical operators: ["AND", "OR"].
    Supported comparison operators: ["=", "!=", ":"] where ":" enables substring matching.
    Parentheses can be used to group logical expressions.

    Example: `title:'news' AND id!='channel-123'`

    Filterable fields: ["id", "title"].
    Both snake_case and camelCase field names are supported.
    """
    def __init__(
        self,
        *,
        organization_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        order_by: builtins.str = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["filter", b"filter", "order_by", b"order_by", "organization_id", b"organization_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListChannelsRequest = ListChannelsRequest

@typing.final
class ListChannelsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CHANNELS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token for retrieving the next page of results.
    Empty if there are no more results available.
    """
    @property
    def channels(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.video.v1.channel_pb2.Channel]:
        """List of channels matching the request criteria.
        May be empty if no channels match the criteria or if the organization has no channels.
        """

    def __init__(
        self,
        *,
        channels: collections.abc.Iterable[yandex.cloud.video.v1.channel_pb2.Channel] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["channels", b"channels", "next_page_token", b"next_page_token"]) -> None: ...

global___ListChannelsResponse = ListChannelsResponse

@typing.final
class CreateChannelRequest(google.protobuf.message.Message):
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

    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    SETTINGS_FIELD_NUMBER: builtins.int
    organization_id: builtins.str
    """ID of the organization where the channel will be created."""
    title: builtins.str
    """Title of the channel to be displayed in interfaces."""
    description: builtins.str
    """Detailed description of the channel's purpose and content."""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Custom user-defined labels as key:value pairs.
        Maximum 64 labels per channel.
        Keys must be lowercase alphanumeric strings with optional hyphens/underscores.
        Values can contain alphanumeric characters and various symbols.
        """

    @property
    def settings(self) -> yandex.cloud.video.v1.channel_pb2.ChannelSettings:
        """Configuration settings for the channel's behavior and features.
        Includes settings for advertisements, content cleanup, and Referer verification.
        """

    def __init__(
        self,
        *,
        organization_id: builtins.str = ...,
        title: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        settings: yandex.cloud.video.v1.channel_pb2.ChannelSettings | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["settings", b"settings"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "labels", b"labels", "organization_id", b"organization_id", "settings", b"settings", "title", b"title"]) -> None: ...

global___CreateChannelRequest = CreateChannelRequest

@typing.final
class CreateChannelMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CHANNEL_ID_FIELD_NUMBER: builtins.int
    channel_id: builtins.str
    """ID of the channel being created."""
    def __init__(
        self,
        *,
        channel_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["channel_id", b"channel_id"]) -> None: ...

global___CreateChannelMetadata = CreateChannelMetadata

@typing.final
class UpdateChannelRequest(google.protobuf.message.Message):
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

    CHANNEL_ID_FIELD_NUMBER: builtins.int
    FIELD_MASK_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    DEFAULT_STYLE_PRESET_ID_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    SETTINGS_FIELD_NUMBER: builtins.int
    channel_id: builtins.str
    """ID of the channel to update."""
    title: builtins.str
    """New title for the channel."""
    description: builtins.str
    """New description for the channel."""
    default_style_preset_id: builtins.str
    """New default style preset ID for the channel.
    This preset will be applied to new videos created in this channel unless explicitly overridden.
    """
    @property
    def field_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask specifying which fields of the channel should be updated.
        Only fields specified in this mask will be modified;
        all other fields will retain their current values.
        This allows for partial updates.
        """

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """New custom labels for the channel as `key:value` pairs.
        Maximum 64 labels per channel.
        If provided, replaces all existing labels.
        """

    @property
    def settings(self) -> yandex.cloud.video.v1.channel_pb2.ChannelSettings:
        """New configuration settings for the channel's behavior and features."""

    def __init__(
        self,
        *,
        channel_id: builtins.str = ...,
        field_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        title: builtins.str = ...,
        description: builtins.str = ...,
        default_style_preset_id: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        settings: yandex.cloud.video.v1.channel_pb2.ChannelSettings | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["field_mask", b"field_mask", "settings", b"settings"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["channel_id", b"channel_id", "default_style_preset_id", b"default_style_preset_id", "description", b"description", "field_mask", b"field_mask", "labels", b"labels", "settings", b"settings", "title", b"title"]) -> None: ...

global___UpdateChannelRequest = UpdateChannelRequest

@typing.final
class UpdateChannelMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CHANNEL_ID_FIELD_NUMBER: builtins.int
    channel_id: builtins.str
    """ID of the channel being updated."""
    def __init__(
        self,
        *,
        channel_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["channel_id", b"channel_id"]) -> None: ...

global___UpdateChannelMetadata = UpdateChannelMetadata

@typing.final
class DeleteChannelRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CHANNEL_ID_FIELD_NUMBER: builtins.int
    channel_id: builtins.str
    """ID of the channel to delete.
    Deleting a channel will also delete all its content,
    including videos, streams, and related resources.
    """
    def __init__(
        self,
        *,
        channel_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["channel_id", b"channel_id"]) -> None: ...

global___DeleteChannelRequest = DeleteChannelRequest

@typing.final
class DeleteChannelMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CHANNEL_ID_FIELD_NUMBER: builtins.int
    channel_id: builtins.str
    """ID of the channel being deleted.
    This identifier can be used to track the channel deletion operation.
    """
    def __init__(
        self,
        *,
        channel_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["channel_id", b"channel_id"]) -> None: ...

global___DeleteChannelMetadata = DeleteChannelMetadata

@typing.final
class BatchDeleteChannelsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    CHANNEL_IDS_FIELD_NUMBER: builtins.int
    organization_id: builtins.str
    """ID of the organization containing the channels to delete."""
    @property
    def channel_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of channel IDs to delete.
        Deleting channels will also delete all their content,
        including videos, streams, and related resources.
        """

    def __init__(
        self,
        *,
        organization_id: builtins.str = ...,
        channel_ids: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["channel_ids", b"channel_ids", "organization_id", b"organization_id"]) -> None: ...

global___BatchDeleteChannelsRequest = BatchDeleteChannelsRequest

@typing.final
class BatchDeleteChannelsMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CHANNEL_IDS_FIELD_NUMBER: builtins.int
    @property
    def channel_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of channel IDs being deleted.
        This list can be used to track which channels are included
        in the batch deletion operation.
        """

    def __init__(
        self,
        *,
        channel_ids: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["channel_ids", b"channel_ids"]) -> None: ...

global___BatchDeleteChannelsMetadata = BatchDeleteChannelsMetadata
