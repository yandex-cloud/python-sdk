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
import yandex.cloud.baremetal.v1alpha.zone_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetZoneRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ZONE_ID_FIELD_NUMBER: builtins.int
    zone_id: builtins.str
    """ID of the Zone resource to return.

    To get the zone ID, use a [ZoneService.List] request.
    """
    def __init__(
        self,
        *,
        zone_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["zone_id", b"zone_id"]) -> None: ...

global___GetZoneRequest = GetZoneRequest

@typing.final
class ListZonesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is greater than `page_size`,
    the service returns a [ListZonesResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value is 20.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set `page_token` to the
    [ListZonesResponse.next_page_token] returned by a previous list request.
    """
    def __init__(
        self,
        *,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListZonesRequest = ListZonesRequest

@typing.final
class ListZonesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ZONES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token for getting the next page of the list. If the number of results is greater than
    [ListZonesRequest.page_size], use `next_page_token` as the value
    for the [ListZonesRequest.page_token] parameter in the next list request.

    Each subsequent page will have its own `next_page_token` to continue paging through the results.
    """
    @property
    def zones(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.baremetal.v1alpha.zone_pb2.Zone]:
        """List of Zone resources."""

    def __init__(
        self,
        *,
        zones: collections.abc.Iterable[yandex.cloud.baremetal.v1alpha.zone_pb2.Zone] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "zones", b"zones"]) -> None: ...

global___ListZonesResponse = ListZonesResponse
