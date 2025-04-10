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
import yandex.cloud.k8s.v1.resource_preset_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetResourcePresetRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_PRESET_ID_FIELD_NUMBER: builtins.int
    resource_preset_id: builtins.str
    """Required. ID of the resource preset to return."""
    def __init__(
        self,
        *,
        resource_preset_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["resource_preset_id", b"resource_preset_id"]) -> None: ...

global___GetResourcePresetRequest = GetResourcePresetRequest

@typing.final
class ListResourcePresetsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size], the service returns a [ListResourcePresetsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token] to the [ListResourcePresetsResponse.next_page_token]
    returned by a previous list request.
    """
    def __init__(
        self,
        *,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListResourcePresetsRequest = ListResourcePresetsRequest

@typing.final
class ListResourcePresetsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_PRESETS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListResourcePresetsRequest.page_size], use the [next_page_token] as the value
    for the [ListResourcePresetsRequest.page_token] parameter in the next list request. Each subsequent
    list request will have its own [next_page_token] to continue paging through the results.
    """
    @property
    def resource_presets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.k8s.v1.resource_preset_pb2.ResourcePreset]:
        """List of ResourcePreset resources."""

    def __init__(
        self,
        *,
        resource_presets: collections.abc.Iterable[yandex.cloud.k8s.v1.resource_preset_pb2.ResourcePreset] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "resource_presets", b"resource_presets"]) -> None: ...

global___ListResourcePresetsResponse = ListResourcePresetsResponse
