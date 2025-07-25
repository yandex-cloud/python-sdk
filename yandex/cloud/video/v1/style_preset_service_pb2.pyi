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
import yandex.cloud.video.v1.style_preset_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetStylePresetRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STYLE_PRESET_ID_FIELD_NUMBER: builtins.int
    style_preset_id: builtins.str
    """ID of the style preset to retrieve."""
    def __init__(
        self,
        *,
        style_preset_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["style_preset_id", b"style_preset_id"]) -> None: ...

global___GetStylePresetRequest = GetStylePresetRequest

@typing.final
class ListStylePresetsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CHANNEL_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    ORDER_BY_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    channel_id: builtins.str
    """ID of the channel containing the style presets to list."""
    page_size: builtins.int
    """The maximum number of style presets to return per page."""
    page_token: builtins.str
    """Page token for retrieving the next page of results.
    This token is obtained from the next_page_token field in the previous ListStylePresetsResponse.
    """
    order_by: builtins.str
    """Specifies the ordering of results.
    Format is "<field> <order>" (e.g., "createdAt desc").
    Default: "id asc".
    Supported fields: ["id", "title", "createdAt", "updatedAt"].
    Both snake_case and camelCase field names are supported.
    """
    filter: builtins.str
    """Filter expression to narrow down the list of returned style presets.
    Expressions consist of terms connected by logical operators.
    Values containing spaces or quotes must be enclosed in quotes (`'` or `"`)
    with inner quotes being backslash-escaped.

    Supported logical operators: ["AND", "OR"].
    Supported comparison operators: ["=", "!=", ":"] where ":" enables substring matching.
    Parentheses can be used to group logical expressions.

    Example: `title:'dark' AND id='preset-1'`

    Filterable fields: ["id", "title"].
    Both snake_case and camelCase field names are supported.
    """
    def __init__(
        self,
        *,
        channel_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        order_by: builtins.str = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["channel_id", b"channel_id", "filter", b"filter", "order_by", b"order_by", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListStylePresetsRequest = ListStylePresetsRequest

@typing.final
class ListStylePresetsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STYLE_PRESETS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token for retrieving the next page of results.
    Empty if there are no more results available.
    """
    @property
    def style_presets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.video.v1.style_preset_pb2.StylePreset]:
        """List of style presets matching the request criteria.
        May be empty if no style presets match the criteria or if the channel has no style presets.
        """

    def __init__(
        self,
        *,
        style_presets: collections.abc.Iterable[yandex.cloud.video.v1.style_preset_pb2.StylePreset] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "style_presets", b"style_presets"]) -> None: ...

global___ListStylePresetsResponse = ListStylePresetsResponse

@typing.final
class CreateStylePresetRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CHANNEL_ID_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    BACKGROUND_COLOR_FIELD_NUMBER: builtins.int
    WIDGET_TEXT_COLOR_PRIMARY_FIELD_NUMBER: builtins.int
    WIDGET_TEXT_COLOR_SECONDARY_FIELD_NUMBER: builtins.int
    WIDGET_ACCENT_COLOR_FIELD_NUMBER: builtins.int
    WIDGET_BLOCK_GAP_FIELD_NUMBER: builtins.int
    WIDGET_BLOCK_SEPARATOR_COLOR_FIELD_NUMBER: builtins.int
    PLAYER_BORDER_RADIUS_FIELD_NUMBER: builtins.int
    PLAYER_COLOR_FIELD_NUMBER: builtins.int
    PLAYLIST_SELECTED_ITEM_BACKGROUND_COLOR_FIELD_NUMBER: builtins.int
    PLAYLIST_ITEM_BORDER_RADIUS_FIELD_NUMBER: builtins.int
    PLAYLIST_ITEM_GAP_FIELD_NUMBER: builtins.int
    PLAYLIST_LOCATION_FIELD_NUMBER: builtins.int
    RIGHT_WIDGETS_FIELD_NUMBER: builtins.int
    BOTTOM_WIDGETS_FIELD_NUMBER: builtins.int
    channel_id: builtins.str
    """ID of the channel."""
    title: builtins.str
    """Style preset title."""
    background_color: builtins.str
    """Background color."""
    widget_text_color_primary: builtins.str
    """Widget primary text color."""
    widget_text_color_secondary: builtins.str
    """Widget secondary text color."""
    widget_accent_color: builtins.str
    """Widget accent color."""
    widget_block_gap: builtins.int
    """Gap between widget blocks."""
    widget_block_separator_color: builtins.str
    """Line color between widget blocks."""
    player_border_radius: builtins.int
    """Player border radius."""
    player_color: builtins.str
    """Player color."""
    playlist_selected_item_background_color: builtins.str
    """Background color of selected video in playlist."""
    playlist_item_border_radius: builtins.int
    """Playlist item border radius."""
    playlist_item_gap: builtins.int
    """Gap between videos in playlist."""
    playlist_location: yandex.cloud.video.v1.style_preset_pb2.StylePreset.WidgetLocation.ValueType
    """Playlist widget location."""
    @property
    def right_widgets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.video.v1.style_preset_pb2.Widget]:
        """List of widgets to display to the right of the player."""

    @property
    def bottom_widgets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.video.v1.style_preset_pb2.Widget]:
        """List of widgets to display below the player."""

    def __init__(
        self,
        *,
        channel_id: builtins.str = ...,
        title: builtins.str = ...,
        background_color: builtins.str = ...,
        widget_text_color_primary: builtins.str = ...,
        widget_text_color_secondary: builtins.str = ...,
        widget_accent_color: builtins.str = ...,
        widget_block_gap: builtins.int = ...,
        widget_block_separator_color: builtins.str = ...,
        player_border_radius: builtins.int = ...,
        player_color: builtins.str = ...,
        playlist_selected_item_background_color: builtins.str = ...,
        playlist_item_border_radius: builtins.int = ...,
        playlist_item_gap: builtins.int = ...,
        playlist_location: yandex.cloud.video.v1.style_preset_pb2.StylePreset.WidgetLocation.ValueType = ...,
        right_widgets: collections.abc.Iterable[yandex.cloud.video.v1.style_preset_pb2.Widget] | None = ...,
        bottom_widgets: collections.abc.Iterable[yandex.cloud.video.v1.style_preset_pb2.Widget] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["background_color", b"background_color", "bottom_widgets", b"bottom_widgets", "channel_id", b"channel_id", "player_border_radius", b"player_border_radius", "player_color", b"player_color", "playlist_item_border_radius", b"playlist_item_border_radius", "playlist_item_gap", b"playlist_item_gap", "playlist_location", b"playlist_location", "playlist_selected_item_background_color", b"playlist_selected_item_background_color", "right_widgets", b"right_widgets", "title", b"title", "widget_accent_color", b"widget_accent_color", "widget_block_gap", b"widget_block_gap", "widget_block_separator_color", b"widget_block_separator_color", "widget_text_color_primary", b"widget_text_color_primary", "widget_text_color_secondary", b"widget_text_color_secondary"]) -> None: ...

global___CreateStylePresetRequest = CreateStylePresetRequest

@typing.final
class CreateStylePresetMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STYLE_PRESET_ID_FIELD_NUMBER: builtins.int
    style_preset_id: builtins.str
    """ID of the style preset being created."""
    def __init__(
        self,
        *,
        style_preset_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["style_preset_id", b"style_preset_id"]) -> None: ...

global___CreateStylePresetMetadata = CreateStylePresetMetadata

@typing.final
class UpdateStylePresetRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STYLE_PRESET_ID_FIELD_NUMBER: builtins.int
    FIELD_MASK_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    BACKGROUND_COLOR_FIELD_NUMBER: builtins.int
    WIDGET_TEXT_COLOR_PRIMARY_FIELD_NUMBER: builtins.int
    WIDGET_TEXT_COLOR_SECONDARY_FIELD_NUMBER: builtins.int
    WIDGET_ACCENT_COLOR_FIELD_NUMBER: builtins.int
    WIDGET_BLOCK_GAP_FIELD_NUMBER: builtins.int
    WIDGET_BLOCK_SEPARATOR_COLOR_FIELD_NUMBER: builtins.int
    PLAYER_BORDER_RADIUS_FIELD_NUMBER: builtins.int
    PLAYER_COLOR_FIELD_NUMBER: builtins.int
    PLAYLIST_SELECTED_ITEM_BACKGROUND_COLOR_FIELD_NUMBER: builtins.int
    PLAYLIST_ITEM_BORDER_RADIUS_FIELD_NUMBER: builtins.int
    PLAYLIST_ITEM_GAP_FIELD_NUMBER: builtins.int
    PLAYLIST_LOCATION_FIELD_NUMBER: builtins.int
    RIGHT_WIDGETS_FIELD_NUMBER: builtins.int
    BOTTOM_WIDGETS_FIELD_NUMBER: builtins.int
    style_preset_id: builtins.str
    """ID of the style preset."""
    title: builtins.str
    """Style preset title."""
    background_color: builtins.str
    """Background color."""
    widget_text_color_primary: builtins.str
    """Widget primary text color."""
    widget_text_color_secondary: builtins.str
    """Widget secondary text color."""
    widget_accent_color: builtins.str
    """Widget accent color."""
    widget_block_gap: builtins.int
    """Gap between widget blocks."""
    widget_block_separator_color: builtins.str
    """Line color between widget blocks."""
    player_border_radius: builtins.int
    """Player border radius."""
    player_color: builtins.str
    """Player color."""
    playlist_selected_item_background_color: builtins.str
    """Background color of selected video in playlist."""
    playlist_item_border_radius: builtins.int
    """Playlist item border radius."""
    playlist_item_gap: builtins.int
    """Gap between videos in playlist."""
    playlist_location: yandex.cloud.video.v1.style_preset_pb2.StylePreset.WidgetLocation.ValueType
    """Playlist widget location."""
    @property
    def field_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask specifying which fields of the style preset should be updated.
        Only fields specified in this mask will be modified;
        all other fields will retain their current values.
        This allows for partial updates.
        """

    @property
    def right_widgets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.video.v1.style_preset_pb2.Widget]:
        """List of widgets to display to the right of the player."""

    @property
    def bottom_widgets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.video.v1.style_preset_pb2.Widget]:
        """List of widgets to display below the player."""

    def __init__(
        self,
        *,
        style_preset_id: builtins.str = ...,
        field_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        title: builtins.str = ...,
        background_color: builtins.str = ...,
        widget_text_color_primary: builtins.str = ...,
        widget_text_color_secondary: builtins.str = ...,
        widget_accent_color: builtins.str = ...,
        widget_block_gap: builtins.int = ...,
        widget_block_separator_color: builtins.str = ...,
        player_border_radius: builtins.int = ...,
        player_color: builtins.str = ...,
        playlist_selected_item_background_color: builtins.str = ...,
        playlist_item_border_radius: builtins.int = ...,
        playlist_item_gap: builtins.int = ...,
        playlist_location: yandex.cloud.video.v1.style_preset_pb2.StylePreset.WidgetLocation.ValueType = ...,
        right_widgets: collections.abc.Iterable[yandex.cloud.video.v1.style_preset_pb2.Widget] | None = ...,
        bottom_widgets: collections.abc.Iterable[yandex.cloud.video.v1.style_preset_pb2.Widget] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["field_mask", b"field_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["background_color", b"background_color", "bottom_widgets", b"bottom_widgets", "field_mask", b"field_mask", "player_border_radius", b"player_border_radius", "player_color", b"player_color", "playlist_item_border_radius", b"playlist_item_border_radius", "playlist_item_gap", b"playlist_item_gap", "playlist_location", b"playlist_location", "playlist_selected_item_background_color", b"playlist_selected_item_background_color", "right_widgets", b"right_widgets", "style_preset_id", b"style_preset_id", "title", b"title", "widget_accent_color", b"widget_accent_color", "widget_block_gap", b"widget_block_gap", "widget_block_separator_color", b"widget_block_separator_color", "widget_text_color_primary", b"widget_text_color_primary", "widget_text_color_secondary", b"widget_text_color_secondary"]) -> None: ...

global___UpdateStylePresetRequest = UpdateStylePresetRequest

@typing.final
class UpdateStylePresetMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STYLE_PRESET_ID_FIELD_NUMBER: builtins.int
    style_preset_id: builtins.str
    """ID of the style preset being updated."""
    def __init__(
        self,
        *,
        style_preset_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["style_preset_id", b"style_preset_id"]) -> None: ...

global___UpdateStylePresetMetadata = UpdateStylePresetMetadata

@typing.final
class DeleteStylePresetRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STYLE_PRESET_ID_FIELD_NUMBER: builtins.int
    style_preset_id: builtins.str
    """ID of the style preset to delete.
    The style preset must not be in use by any videos, episodes, or playlists.
    """
    def __init__(
        self,
        *,
        style_preset_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["style_preset_id", b"style_preset_id"]) -> None: ...

global___DeleteStylePresetRequest = DeleteStylePresetRequest

@typing.final
class DeleteStylePresetMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STYLE_PRESET_ID_FIELD_NUMBER: builtins.int
    style_preset_id: builtins.str
    """ID of the style preset being deleted.
    This identifier can be used to track the style preset deletion operation.
    """
    def __init__(
        self,
        *,
        style_preset_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["style_preset_id", b"style_preset_id"]) -> None: ...

global___DeleteStylePresetMetadata = DeleteStylePresetMetadata
