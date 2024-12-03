"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing
import yandex.cloud.searchapi.v2.search_query_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class SortSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _SortOrder:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _SortOrderEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[SortSpec._SortOrder.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        SORT_ORDER_UNSPECIFIED: SortSpec._SortOrder.ValueType  # 0
        SORT_ORDER_ASC: SortSpec._SortOrder.ValueType  # 1
        """Reverse order from oldest to most recent."""
        SORT_ORDER_DESC: SortSpec._SortOrder.ValueType  # 2
        """Direct order from most recent to oldest (default)."""

    class SortOrder(_SortOrder, metaclass=_SortOrderEnumTypeWrapper): ...
    SORT_ORDER_UNSPECIFIED: SortSpec.SortOrder.ValueType  # 0
    SORT_ORDER_ASC: SortSpec.SortOrder.ValueType  # 1
    """Reverse order from oldest to most recent."""
    SORT_ORDER_DESC: SortSpec.SortOrder.ValueType  # 2
    """Direct order from most recent to oldest (default)."""

    class _SortMode:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _SortModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[SortSpec._SortMode.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        SORT_MODE_UNSPECIFIED: SortSpec._SortMode.ValueType  # 0
        SORT_MODE_BY_RELEVANCE: SortSpec._SortMode.ValueType  # 1
        """Sort documents by relevance (default value)."""
        SORT_MODE_BY_TIME: SortSpec._SortMode.ValueType  # 2
        """Sort documents by update time."""

    class SortMode(_SortMode, metaclass=_SortModeEnumTypeWrapper): ...
    SORT_MODE_UNSPECIFIED: SortSpec.SortMode.ValueType  # 0
    SORT_MODE_BY_RELEVANCE: SortSpec.SortMode.ValueType  # 1
    """Sort documents by relevance (default value)."""
    SORT_MODE_BY_TIME: SortSpec.SortMode.ValueType  # 2
    """Sort documents by update time."""

    SORT_MODE_FIELD_NUMBER: builtins.int
    SORT_ORDER_FIELD_NUMBER: builtins.int
    sort_mode: global___SortSpec.SortMode.ValueType
    """Documents sorting mode."""
    sort_order: global___SortSpec.SortOrder.ValueType
    """Documents sorting order."""
    def __init__(
        self,
        *,
        sort_mode: global___SortSpec.SortMode.ValueType = ...,
        sort_order: global___SortSpec.SortOrder.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["sort_mode", b"sort_mode", "sort_order", b"sort_order"]) -> None: ...

global___SortSpec = SortSpec

@typing.final
class GroupSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _GroupMode:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _GroupModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[GroupSpec._GroupMode.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        GROUP_MODE_UNSPECIFIED: GroupSpec._GroupMode.ValueType  # 0
        GROUP_MODE_FLAT: GroupSpec._GroupMode.ValueType  # 1
        """Flat grouping. Each group contains a single document."""
        GROUP_MODE_DEEP: GroupSpec._GroupMode.ValueType  # 2
        """Grouping by domain. Each group contains documents from one domain."""

    class GroupMode(_GroupMode, metaclass=_GroupModeEnumTypeWrapper): ...
    GROUP_MODE_UNSPECIFIED: GroupSpec.GroupMode.ValueType  # 0
    GROUP_MODE_FLAT: GroupSpec.GroupMode.ValueType  # 1
    """Flat grouping. Each group contains a single document."""
    GROUP_MODE_DEEP: GroupSpec.GroupMode.ValueType  # 2
    """Grouping by domain. Each group contains documents from one domain."""

    GROUP_MODE_FIELD_NUMBER: builtins.int
    GROUPS_ON_PAGE_FIELD_NUMBER: builtins.int
    DOCS_IN_GROUP_FIELD_NUMBER: builtins.int
    group_mode: global___GroupSpec.GroupMode.ValueType
    """Grouping method."""
    groups_on_page: builtins.int
    """Maximum number of groups that can be returned per page with search results."""
    docs_in_group: builtins.int
    """Maximum number of documents that can be returned per group."""
    def __init__(
        self,
        *,
        group_mode: global___GroupSpec.GroupMode.ValueType = ...,
        groups_on_page: builtins.int = ...,
        docs_in_group: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["docs_in_group", b"docs_in_group", "group_mode", b"group_mode", "groups_on_page", b"groups_on_page"]) -> None: ...

global___GroupSpec = GroupSpec

@typing.final
class WebSearchRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Localization:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _LocalizationEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[WebSearchRequest._Localization.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        LOCALIZATION_UNSPECIFIED: WebSearchRequest._Localization.ValueType  # 0
        LOCALIZATION_RU: WebSearchRequest._Localization.ValueType  # 1
        """Russian (default value)"""
        LOCALIZATION_UK: WebSearchRequest._Localization.ValueType  # 2
        """Ukrainian"""
        LOCALIZATION_BE: WebSearchRequest._Localization.ValueType  # 3
        """Belarusian"""
        LOCALIZATION_KK: WebSearchRequest._Localization.ValueType  # 4
        """Kazakh"""
        LOCALIZATION_TR: WebSearchRequest._Localization.ValueType  # 5
        """Turkish"""
        LOCALIZATION_EN: WebSearchRequest._Localization.ValueType  # 6
        """English"""

    class Localization(_Localization, metaclass=_LocalizationEnumTypeWrapper): ...
    LOCALIZATION_UNSPECIFIED: WebSearchRequest.Localization.ValueType  # 0
    LOCALIZATION_RU: WebSearchRequest.Localization.ValueType  # 1
    """Russian (default value)"""
    LOCALIZATION_UK: WebSearchRequest.Localization.ValueType  # 2
    """Ukrainian"""
    LOCALIZATION_BE: WebSearchRequest.Localization.ValueType  # 3
    """Belarusian"""
    LOCALIZATION_KK: WebSearchRequest.Localization.ValueType  # 4
    """Kazakh"""
    LOCALIZATION_TR: WebSearchRequest.Localization.ValueType  # 5
    """Turkish"""
    LOCALIZATION_EN: WebSearchRequest.Localization.ValueType  # 6
    """English"""

    class _Format:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _FormatEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[WebSearchRequest._Format.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        FORMAT_UNSPECIFIED: WebSearchRequest._Format.ValueType  # 0
        FORMAT_XML: WebSearchRequest._Format.ValueType  # 1
        """XML format (default value)"""
        FORMAT_HTML: WebSearchRequest._Format.ValueType  # 2
        """HTML format"""

    class Format(_Format, metaclass=_FormatEnumTypeWrapper): ...
    FORMAT_UNSPECIFIED: WebSearchRequest.Format.ValueType  # 0
    FORMAT_XML: WebSearchRequest.Format.ValueType  # 1
    """XML format (default value)"""
    FORMAT_HTML: WebSearchRequest.Format.ValueType  # 2
    """HTML format"""

    QUERY_FIELD_NUMBER: builtins.int
    SORT_SPEC_FIELD_NUMBER: builtins.int
    GROUP_SPEC_FIELD_NUMBER: builtins.int
    MAX_PASSAGES_FIELD_NUMBER: builtins.int
    REGION_FIELD_NUMBER: builtins.int
    L10N_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    RESPONSE_FORMAT_FIELD_NUMBER: builtins.int
    USER_AGENT_FIELD_NUMBER: builtins.int
    max_passages: builtins.int
    """The maximum number of passages that can be used when generating a document snippet."""
    region: builtins.str
    """ID of the search country or region that impacts the document ranking rules."""
    l10n: global___WebSearchRequest.Localization.ValueType
    """The notification language for a search response."""
    folder_id: builtins.str
    """ID of the folder."""
    response_format: global___WebSearchRequest.Format.ValueType
    """Search results format."""
    user_agent: builtins.str
    """User-Agent request header value."""
    @property
    def query(self) -> yandex.cloud.searchapi.v2.search_query_pb2.SearchQuery:
        """Search query."""

    @property
    def sort_spec(self) -> global___SortSpec:
        """The rules for sorting search results that define the sequence of the returned search results."""

    @property
    def group_spec(self) -> global___GroupSpec:
        """Grouping settings that are used to group documents from a single domain into a container."""

    def __init__(
        self,
        *,
        query: yandex.cloud.searchapi.v2.search_query_pb2.SearchQuery | None = ...,
        sort_spec: global___SortSpec | None = ...,
        group_spec: global___GroupSpec | None = ...,
        max_passages: builtins.int = ...,
        region: builtins.str = ...,
        l10n: global___WebSearchRequest.Localization.ValueType = ...,
        folder_id: builtins.str = ...,
        response_format: global___WebSearchRequest.Format.ValueType = ...,
        user_agent: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["group_spec", b"group_spec", "query", b"query", "sort_spec", b"sort_spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["folder_id", b"folder_id", "group_spec", b"group_spec", "l10n", b"l10n", "max_passages", b"max_passages", "query", b"query", "region", b"region", "response_format", b"response_format", "sort_spec", b"sort_spec", "user_agent", b"user_agent"]) -> None: ...

global___WebSearchRequest = WebSearchRequest

@typing.final
class WebSearchResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RAW_DATA_FIELD_NUMBER: builtins.int
    raw_data: builtins.bytes
    """Search results, either in XML or HTML format depending on the request settings."""
    def __init__(
        self,
        *,
        raw_data: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["raw_data", b"raw_data"]) -> None: ...

global___WebSearchResponse = WebSearchResponse
