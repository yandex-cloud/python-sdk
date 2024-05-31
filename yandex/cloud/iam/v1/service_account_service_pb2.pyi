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
import yandex.cloud.iam.v1.service_account_pb2
import yandex.cloud.operation.operation_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetServiceAccountRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVICE_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    service_account_id: builtins.str
    """ID of the ServiceAccount resource to return.
    To get the service account ID, use a [ServiceAccountService.List] request.
    """
    def __init__(
        self,
        *,
        service_account_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["service_account_id", b"service_account_id"]) -> None: ...

global___GetServiceAccountRequest = GetServiceAccountRequest

@typing.final
class ListServiceAccountsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to list service accounts in.
    To get the folder ID, use a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListServiceAccountsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token]
    to the [ListServiceAccountsResponse.next_page_token]
    returned by a previous list request.
    """
    filter: builtins.str
    """A filter expression that filters resources listed in the response.
    The expression must specify:
    1. The field name. Currently you can use filtering only on the [ServiceAccount.name] field.
    2. An `=` operator.
    3. The value in double quotes (`"`). Must be 3-63 characters long and match the regular expression `[a-z][-a-z0-9]{1,61}[a-z0-9]`.
    """
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["filter", b"filter", "folder_id", b"folder_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListServiceAccountsRequest = ListServiceAccountsRequest

@typing.final
class ListServiceAccountsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVICE_ACCOUNTS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListServiceAccountsRequest.page_size], use
    the [next_page_token] as the value
    for the [ListServiceAccountsRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    [next_page_token] to continue paging through the results.
    """
    @property
    def service_accounts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.iam.v1.service_account_pb2.ServiceAccount]:
        """List of ServiceAccount resources."""

    def __init__(
        self,
        *,
        service_accounts: collections.abc.Iterable[yandex.cloud.iam.v1.service_account_pb2.ServiceAccount] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "service_accounts", b"service_accounts"]) -> None: ...

global___ListServiceAccountsResponse = ListServiceAccountsResponse

@typing.final
class CreateServiceAccountRequest(google.protobuf.message.Message):
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

    FOLDER_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to create a service account in.
    To get the folder ID, use a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    name: builtins.str
    """Name of the service account.
    The name must be unique within the cloud.
    """
    description: builtins.str
    """Description of the service account."""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `` key:value `` pairs."""

    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "folder_id", b"folder_id", "labels", b"labels", "name", b"name"]) -> None: ...

global___CreateServiceAccountRequest = CreateServiceAccountRequest

@typing.final
class CreateServiceAccountMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVICE_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    service_account_id: builtins.str
    """ID of the service account that is being created."""
    def __init__(
        self,
        *,
        service_account_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["service_account_id", b"service_account_id"]) -> None: ...

global___CreateServiceAccountMetadata = CreateServiceAccountMetadata

@typing.final
class UpdateServiceAccountRequest(google.protobuf.message.Message):
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

    SERVICE_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    service_account_id: builtins.str
    """ID of the ServiceAccount resource to update.
    To get the service account ID, use a [ServiceAccountService.List] request.
    """
    name: builtins.str
    """Name of the service account.
    The name must be unique within the cloud.
    """
    description: builtins.str
    """Description of the service account."""
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which fields of the ServiceAccount resource are going to be updated."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `` key:value `` pairs."""

    def __init__(
        self,
        *,
        service_account_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "labels", b"labels", "name", b"name", "service_account_id", b"service_account_id", "update_mask", b"update_mask"]) -> None: ...

global___UpdateServiceAccountRequest = UpdateServiceAccountRequest

@typing.final
class UpdateServiceAccountMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVICE_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    service_account_id: builtins.str
    """ID of the ServiceAccount resource that is being updated."""
    def __init__(
        self,
        *,
        service_account_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["service_account_id", b"service_account_id"]) -> None: ...

global___UpdateServiceAccountMetadata = UpdateServiceAccountMetadata

@typing.final
class DeleteServiceAccountRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVICE_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    service_account_id: builtins.str
    """ID of the service account to delete.
    To get the service account ID, use a [ServiceAccountService.List] request.
    """
    def __init__(
        self,
        *,
        service_account_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["service_account_id", b"service_account_id"]) -> None: ...

global___DeleteServiceAccountRequest = DeleteServiceAccountRequest

@typing.final
class DeleteServiceAccountMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVICE_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    service_account_id: builtins.str
    """ID of the service account that is being deleted."""
    def __init__(
        self,
        *,
        service_account_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["service_account_id", b"service_account_id"]) -> None: ...

global___DeleteServiceAccountMetadata = DeleteServiceAccountMetadata

@typing.final
class ListServiceAccountOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVICE_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    service_account_id: builtins.str
    """ID of the ServiceAccount resource to list operations for."""
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size], the service returns a [ListServiceAccountOperationsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token]
    to the [ListServiceAccountOperationsResponse.next_page_token]
    returned by a previous list request.
    """
    def __init__(
        self,
        *,
        service_account_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["page_size", b"page_size", "page_token", b"page_token", "service_account_id", b"service_account_id"]) -> None: ...

global___ListServiceAccountOperationsRequest = ListServiceAccountOperationsRequest

@typing.final
class ListServiceAccountOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListServiceAccountOperationsRequest.page_size], use the [next_page_token] as the value
    for the [ListServiceAccountOperationsRequest.page_token] query parameter in the next list request.
    Each subsequent list request will have its own [next_page_token] to continue paging through the results.
    """
    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.operation.operation_pb2.Operation]:
        """List of operations for the specified service account."""

    def __init__(
        self,
        *,
        operations: collections.abc.Iterable[yandex.cloud.operation.operation_pb2.Operation] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "operations", b"operations"]) -> None: ...

global___ListServiceAccountOperationsResponse = ListServiceAccountOperationsResponse