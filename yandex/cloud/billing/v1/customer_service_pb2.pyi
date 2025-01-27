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
import yandex.cloud.billing.v1.customer_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class ListCustomersRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESELLER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    reseller_id: builtins.str
    """ID of the reseller."""
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListCustomersResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    """
    page_token: builtins.str
    """Page token. To get the next page of results,
    set [page_token] to the [ListCustomersResponse.next_page_token]
    returned by a previous list request.
    """
    def __init__(
        self,
        *,
        reseller_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["page_size", b"page_size", "page_token", b"page_token", "reseller_id", b"reseller_id"]) -> None: ...

global___ListCustomersRequest = ListCustomersRequest

@typing.final
class ListCustomersResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CUSTOMERS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListCustomersRequest.page_size], use
    [next_page_token] as the value
    for the [ListCustomersRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    [next_page_token] to continue paging through the results.
    """
    @property
    def customers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.billing.v1.customer_pb2.Customer]:
        """List of customers."""

    def __init__(
        self,
        *,
        customers: collections.abc.Iterable[yandex.cloud.billing.v1.customer_pb2.Customer] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["customers", b"customers", "next_page_token", b"next_page_token"]) -> None: ...

global___ListCustomersResponse = ListCustomersResponse

@typing.final
class InviteCustomerRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESELLER_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    INVITATION_EMAIL_FIELD_NUMBER: builtins.int
    PERSON_FIELD_NUMBER: builtins.int
    reseller_id: builtins.str
    """Billing account ID of the reseller that the customer will be associated with."""
    name: builtins.str
    """Name of the customer."""
    invitation_email: builtins.str
    """Customer email to send invitation to."""
    @property
    def person(self) -> yandex.cloud.billing.v1.customer_pb2.CustomerPerson:
        """Person of the customer."""

    def __init__(
        self,
        *,
        reseller_id: builtins.str = ...,
        name: builtins.str = ...,
        invitation_email: builtins.str = ...,
        person: yandex.cloud.billing.v1.customer_pb2.CustomerPerson | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["person", b"person"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["invitation_email", b"invitation_email", "name", b"name", "person", b"person", "reseller_id", b"reseller_id"]) -> None: ...

global___InviteCustomerRequest = InviteCustomerRequest

@typing.final
class CreateResellerServedCustomerRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESELLER_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    PERSON_FIELD_NUMBER: builtins.int
    reseller_id: builtins.str
    """ID of the reseller that customer will be associated with.</br>

    Value must match either one of the three regular expressions:
    </br>- `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
    </br>- `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{32}$`
    </br>- `^[a-z][-a-zA-Z0-9.]{0,48}[a-zA-Z0-9]$`
    """
    name: builtins.str
    """Name of the customer.

    String length is not limited.
    """
    @property
    def person(self) -> yandex.cloud.billing.v1.customer_pb2.CustomerPerson:
        """Person of the customer."""

    def __init__(
        self,
        *,
        reseller_id: builtins.str = ...,
        name: builtins.str = ...,
        person: yandex.cloud.billing.v1.customer_pb2.CustomerPerson | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["person", b"person"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["name", b"name", "person", b"person", "reseller_id", b"reseller_id"]) -> None: ...

global___CreateResellerServedCustomerRequest = CreateResellerServedCustomerRequest

@typing.final
class ActivateCustomerRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    customer_id: builtins.str
    """ID of the customer.
    To get the customer ID, use [CustomerService.List] request.
    """
    def __init__(
        self,
        *,
        customer_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["customer_id", b"customer_id"]) -> None: ...

global___ActivateCustomerRequest = ActivateCustomerRequest

@typing.final
class SuspendCustomerRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    customer_id: builtins.str
    """ID of the customer.
    To get the customer ID, use [CustomerService.List] request.
    """
    def __init__(
        self,
        *,
        customer_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["customer_id", b"customer_id"]) -> None: ...

global___SuspendCustomerRequest = SuspendCustomerRequest

@typing.final
class CustomerMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESELLER_ID_FIELD_NUMBER: builtins.int
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    reseller_id: builtins.str
    """ID of the reseller."""
    customer_id: builtins.str
    """ID of the customer."""
    def __init__(
        self,
        *,
        reseller_id: builtins.str = ...,
        customer_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["customer_id", b"customer_id", "reseller_id", b"reseller_id"]) -> None: ...

global___CustomerMetadata = CustomerMetadata
