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

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class SearchQuery(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _SearchType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _SearchTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[SearchQuery._SearchType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        SEARCH_TYPE_UNSPECIFIED: SearchQuery._SearchType.ValueType  # 0
        SEARCH_TYPE_RU: SearchQuery._SearchType.ValueType  # 1
        """Russian search type (default), yandex.ru search domain name will be used."""
        SEARCH_TYPE_TR: SearchQuery._SearchType.ValueType  # 2
        """Turkish search type, yandex.tr search domain name will be used."""
        SEARCH_TYPE_COM: SearchQuery._SearchType.ValueType  # 3
        """International search type, yandex.com search domain name will be used."""

    class SearchType(_SearchType, metaclass=_SearchTypeEnumTypeWrapper): ...
    SEARCH_TYPE_UNSPECIFIED: SearchQuery.SearchType.ValueType  # 0
    SEARCH_TYPE_RU: SearchQuery.SearchType.ValueType  # 1
    """Russian search type (default), yandex.ru search domain name will be used."""
    SEARCH_TYPE_TR: SearchQuery.SearchType.ValueType  # 2
    """Turkish search type, yandex.tr search domain name will be used."""
    SEARCH_TYPE_COM: SearchQuery.SearchType.ValueType  # 3
    """International search type, yandex.com search domain name will be used."""

    class _FamilyMode:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _FamilyModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[SearchQuery._FamilyMode.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        FAMILY_MODE_UNSPECIFIED: SearchQuery._FamilyMode.ValueType  # 0
        FAMILY_MODE_NONE: SearchQuery._FamilyMode.ValueType  # 1
        """Filtering is disabled. Search results include any documents regardless of their contents."""
        FAMILY_MODE_MODERATE: SearchQuery._FamilyMode.ValueType  # 2
        """Moderate filter (default value). Documents of the Adult category are excluded from search results
        unless a query is explicitly made for searching resources of this category.
        """
        FAMILY_MODE_STRICT: SearchQuery._FamilyMode.ValueType  # 3
        """Regardless of a search query, documents of the Adult category
        and those with profanity are excluded from search results.
        """

    class FamilyMode(_FamilyMode, metaclass=_FamilyModeEnumTypeWrapper): ...
    FAMILY_MODE_UNSPECIFIED: SearchQuery.FamilyMode.ValueType  # 0
    FAMILY_MODE_NONE: SearchQuery.FamilyMode.ValueType  # 1
    """Filtering is disabled. Search results include any documents regardless of their contents."""
    FAMILY_MODE_MODERATE: SearchQuery.FamilyMode.ValueType  # 2
    """Moderate filter (default value). Documents of the Adult category are excluded from search results
    unless a query is explicitly made for searching resources of this category.
    """
    FAMILY_MODE_STRICT: SearchQuery.FamilyMode.ValueType  # 3
    """Regardless of a search query, documents of the Adult category
    and those with profanity are excluded from search results.
    """

    class _FixTypoMode:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _FixTypoModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[SearchQuery._FixTypoMode.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        FIX_TYPO_MODE_UNSPECIFIED: SearchQuery._FixTypoMode.ValueType  # 0
        FIX_TYPO_MODE_ON: SearchQuery._FixTypoMode.ValueType  # 1
        """Automatically correct typos (default value)."""
        FIX_TYPO_MODE_OFF: SearchQuery._FixTypoMode.ValueType  # 2
        """Autocorrection is off."""

    class FixTypoMode(_FixTypoMode, metaclass=_FixTypoModeEnumTypeWrapper): ...
    FIX_TYPO_MODE_UNSPECIFIED: SearchQuery.FixTypoMode.ValueType  # 0
    FIX_TYPO_MODE_ON: SearchQuery.FixTypoMode.ValueType  # 1
    """Automatically correct typos (default value)."""
    FIX_TYPO_MODE_OFF: SearchQuery.FixTypoMode.ValueType  # 2
    """Autocorrection is off."""

    SEARCH_TYPE_FIELD_NUMBER: builtins.int
    QUERY_TEXT_FIELD_NUMBER: builtins.int
    FAMILY_MODE_FIELD_NUMBER: builtins.int
    PAGE_FIELD_NUMBER: builtins.int
    FIX_TYPO_MODE_FIELD_NUMBER: builtins.int
    search_type: global___SearchQuery.SearchType.ValueType
    """Search type that determines the domain name that will be used for the search queries."""
    query_text: builtins.str
    """Search query text"""
    family_mode: global___SearchQuery.FamilyMode.ValueType
    """Rule for filtering search results and determines whether any documents should be excluded."""
    page: builtins.int
    """The number of a requested page with search results"""
    fix_typo_mode: global___SearchQuery.FixTypoMode.ValueType
    """Typos autocorrections mode"""
    def __init__(
        self,
        *,
        search_type: global___SearchQuery.SearchType.ValueType = ...,
        query_text: builtins.str = ...,
        family_mode: global___SearchQuery.FamilyMode.ValueType = ...,
        page: builtins.int = ...,
        fix_typo_mode: global___SearchQuery.FixTypoMode.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["family_mode", b"family_mode", "fix_typo_mode", b"fix_typo_mode", "page", b"page", "query_text", b"query_text", "search_type", b"search_type"]) -> None: ...

global___SearchQuery = SearchQuery
