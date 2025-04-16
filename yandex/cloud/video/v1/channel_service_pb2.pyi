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
    """ID of the channel."""
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
    """ID of the organization."""
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
    Possible fields: ["id", "title", "createdAt", "updatedAt"].
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
    """Token for getting the next page."""
    @property
    def channels(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.video.v1.channel_pb2.Channel]:
        """List of channels for specific organization."""

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
    """ID of the organization."""
    title: builtins.str
    """Channel title."""
    description: builtins.str
    """Channel description."""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Custom labels as `` key:value `` pairs. Maximum 64 per resource."""

    @property
    def settings(self) -> yandex.cloud.video.v1.channel_pb2.ChannelSettings:
        """Channel settings."""

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
    """ID of the channel."""
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
    LABELS_FIELD_NUMBER: builtins.int
    SETTINGS_FIELD_NUMBER: builtins.int
    channel_id: builtins.str
    """ID of the channel."""
    title: builtins.str
    """Channel title."""
    description: builtins.str
    """Channel description."""
    @property
    def field_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which fields of the channel are going to be updated."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Custom labels as `` key:value `` pairs. Maximum 64 per resource."""

    @property
    def settings(self) -> yandex.cloud.video.v1.channel_pb2.ChannelSettings:
        """Channel settings."""

    def __init__(
        self,
        *,
        channel_id: builtins.str = ...,
        field_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        title: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        settings: yandex.cloud.video.v1.channel_pb2.ChannelSettings | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["field_mask", b"field_mask", "settings", b"settings"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["channel_id", b"channel_id", "description", b"description", "field_mask", b"field_mask", "labels", b"labels", "settings", b"settings", "title", b"title"]) -> None: ...

global___UpdateChannelRequest = UpdateChannelRequest

@typing.final
class UpdateChannelMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CHANNEL_ID_FIELD_NUMBER: builtins.int
    channel_id: builtins.str
    """ID of the channel."""
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
    """ID of the channel."""
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
    """ID of the channel."""
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
    """ID of the organization."""
    @property
    def channel_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of channel IDs."""

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
        """List of channel IDs."""

    def __init__(
        self,
        *,
        channel_ids: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["channel_ids", b"channel_ids"]) -> None: ...

global___BatchDeleteChannelsMetadata = BatchDeleteChannelsMetadata
