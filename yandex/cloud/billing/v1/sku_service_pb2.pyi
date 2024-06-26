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
import yandex.cloud.billing.v1.sku_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetSkuRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    CURRENCY_FIELD_NUMBER: builtins.int
    BILLING_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the SKU to return.
    To get the SKU ID, use [SkuService.List] request.
    """
    currency: builtins.str
    """Currency of the SKU.
    Can be one of the following:
    * `RUB`
    * `USD`
    * `KZT`
    """
    billing_account_id: builtins.str
    """Optional ID of the billing account.
    If specified, contract prices for a particular billing account are included in the response.
    To get the billing account ID, use [BillingAccountService.List] request.
    """
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        currency: builtins.str = ...,
        billing_account_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["billing_account_id", b"billing_account_id", "currency", b"currency", "id", b"id"]) -> None: ...

global___GetSkuRequest = GetSkuRequest

@typing.final
class ListSkusRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CURRENCY_FIELD_NUMBER: builtins.int
    BILLING_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    currency: builtins.str
    """Currency of the prices.
    Can be one of the following:
    * `RUB`
    * `USD`
    * `KZT`
    """
    billing_account_id: builtins.str
    """Optional ID of the billing account.
    If specified, contract prices for a particular billing account are included in the response.
    To get the billing account ID, use [BillingAccountService.List] request.
    """
    filter: builtins.str
    """A filter expression that filters resources listed in the response.
    The expression must specify:
    1. The field name. Currently you can use filtering only on the [yandex.cloud.billing.v1.Sku.id] and [yandex.cloud.billing.v1.Sku.service_id] field.
    2. An `=` operator.
    3. The value in double quotes (`"`). Must be 3-63 characters long and match the regular expression `[a-z][-a-z0-9]{1,61}[a-z0-9]`.
    E.g. `filter=serviceId="dn28hpu6268356q0j8mk"`.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListSkusResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    """
    page_token: builtins.str
    """Page token. To get the next page of results,
    set [page_token] to the [ListSkusResponse.next_page_token]
    returned by a previous list request.
    """
    def __init__(
        self,
        *,
        currency: builtins.str = ...,
        billing_account_id: builtins.str = ...,
        filter: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["billing_account_id", b"billing_account_id", "currency", b"currency", "filter", b"filter", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListSkusRequest = ListSkusRequest

@typing.final
class ListSkusResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SKUS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListSkusRequest.page_size], use
    [next_page_token] as the value
    for the [ListSkusRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    [next_page_token] to continue paging through the results.
    """
    @property
    def skus(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.billing.v1.sku_pb2.Sku]:
        """List of skus."""

    def __init__(
        self,
        *,
        skus: collections.abc.Iterable[yandex.cloud.billing.v1.sku_pb2.Sku] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "skus", b"skus"]) -> None: ...

global___ListSkusResponse = ListSkusResponse
