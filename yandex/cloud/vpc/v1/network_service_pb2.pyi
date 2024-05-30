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
import yandex.cloud.operation.operation_pb2
import yandex.cloud.vpc.v1.network_pb2
import yandex.cloud.vpc.v1.route_table_pb2
import yandex.cloud.vpc.v1.security_group_pb2
import yandex.cloud.vpc.v1.subnet_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetNetworkRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NETWORK_ID_FIELD_NUMBER: builtins.int
    network_id: builtins.str
    """ID of the Network resource to return.
    To get the network ID, use a [NetworkService.List] request.
    """
    def __init__(
        self,
        *,
        network_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["network_id", b"network_id"]) -> None: ...

global___GetNetworkRequest = GetNetworkRequest

@typing.final
class ListNetworksRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to list networks in.
    To get the folder ID, use a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListNetworksResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests. Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token] to the
    [ListNetworksResponse.next_page_token] returned by a previous list request.
    """
    filter: builtins.str
    """A filter expression that filters resources listed in the response.
    The expression must specify:
    1. The field name. Currently you can use filtering only on the [Network.name] field.
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

global___ListNetworksRequest = ListNetworksRequest

@typing.final
class ListNetworksResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NETWORKS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListNetworksRequest.page_size], use
    the [next_page_token] as the value
    for the [ListNetworksRequest.page_token] query parameter
    in the next list request. Subsequent list requests will have their own
    [next_page_token] to continue paging through the results.
    """
    @property
    def networks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.vpc.v1.network_pb2.Network]:
        """List of Network resources."""

    def __init__(
        self,
        *,
        networks: collections.abc.Iterable[yandex.cloud.vpc.v1.network_pb2.Network] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["networks", b"networks", "next_page_token", b"next_page_token"]) -> None: ...

global___ListNetworksResponse = ListNetworksResponse

@typing.final
class CreateNetworkRequest(google.protobuf.message.Message):
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
    """ID of the folder for this request to create a network in.
    To get the folder ID, use a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    name: builtins.str
    """Name of the network.
    The name must be unique within the folder.
    """
    description: builtins.str
    """Description of the network."""
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

global___CreateNetworkRequest = CreateNetworkRequest

@typing.final
class CreateNetworkMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NETWORK_ID_FIELD_NUMBER: builtins.int
    network_id: builtins.str
    """ID of the Network that is being created."""
    def __init__(
        self,
        *,
        network_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["network_id", b"network_id"]) -> None: ...

global___CreateNetworkMetadata = CreateNetworkMetadata

@typing.final
class UpdateNetworkRequest(google.protobuf.message.Message):
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

    NETWORK_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    network_id: builtins.str
    """ID of the Network resource to update.
    To get the network ID use a [NetworkService.List] request.
    """
    name: builtins.str
    """Name of the network.
    The name must be unique within the folder.
    """
    description: builtins.str
    """Description of the network."""
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which fields of the Network resource are going to be updated."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `` key:value `` pairs."""

    def __init__(
        self,
        *,
        network_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "labels", b"labels", "name", b"name", "network_id", b"network_id", "update_mask", b"update_mask"]) -> None: ...

global___UpdateNetworkRequest = UpdateNetworkRequest

@typing.final
class UpdateNetworkMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NETWORK_ID_FIELD_NUMBER: builtins.int
    network_id: builtins.str
    """ID of the Network resource that is being updated."""
    def __init__(
        self,
        *,
        network_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["network_id", b"network_id"]) -> None: ...

global___UpdateNetworkMetadata = UpdateNetworkMetadata

@typing.final
class DeleteNetworkRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NETWORK_ID_FIELD_NUMBER: builtins.int
    network_id: builtins.str
    """ID of the Network resource to update.
    To get the network ID, use a [NetworkService.List] request.
    """
    def __init__(
        self,
        *,
        network_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["network_id", b"network_id"]) -> None: ...

global___DeleteNetworkRequest = DeleteNetworkRequest

@typing.final
class DeleteNetworkMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NETWORK_ID_FIELD_NUMBER: builtins.int
    network_id: builtins.str
    """ID of the network that is being deleted."""
    def __init__(
        self,
        *,
        network_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["network_id", b"network_id"]) -> None: ...

global___DeleteNetworkMetadata = DeleteNetworkMetadata

@typing.final
class ListNetworkSubnetsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NETWORK_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    network_id: builtins.str
    """ID of the Network resource to list subnets for."""
    page_size: builtins.int
    """The maximum number of results per page that should be returned. If the number of available
    results is larger than [page_size],
    the service returns a [ListNetworkSubnetsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests. Default value: 100.
    """
    page_token: builtins.str
    """Page token. Set [page_token]
    to the [ListNetworkSubnetsResponse.next_page_token]
    returned by a previous list request to get the next page of results.
    """
    def __init__(
        self,
        *,
        network_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["network_id", b"network_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListNetworkSubnetsRequest = ListNetworkSubnetsRequest

@typing.final
class ListNetworkSubnetsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBNETS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListNetworkSubnetsRequest.page_size], use
    the [next_page_token] as the value
    for the [ListNetworkSubnetsRequest.page_token] query parameter
    in the next list request. Subsequent list requests will have their own
    [next_page_token] to continue paging through the results.
    """
    @property
    def subnets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.vpc.v1.subnet_pb2.Subnet]:
        """List of subnets that belong to the network which is specified in the request."""

    def __init__(
        self,
        *,
        subnets: collections.abc.Iterable[yandex.cloud.vpc.v1.subnet_pb2.Subnet] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "subnets", b"subnets"]) -> None: ...

global___ListNetworkSubnetsResponse = ListNetworkSubnetsResponse

@typing.final
class ListNetworkSecurityGroupsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NETWORK_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    network_id: builtins.str
    """ID of the Network resource to list security groups for."""
    page_size: builtins.int
    """The maximum number of results per page that should be returned. If the number of available
    results is larger than [page_size],
    the service returns a [ListNetworkSecurityGroupsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests. Default value: 100.
    """
    page_token: builtins.str
    """Page token. Set [page_token]
    to the [ListNetworkSecurityGroupsResponse.next_page_token]
    returned by a previous list request to get the next page of results.
    """
    def __init__(
        self,
        *,
        network_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["network_id", b"network_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListNetworkSecurityGroupsRequest = ListNetworkSecurityGroupsRequest

@typing.final
class ListNetworkSecurityGroupsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SECURITY_GROUPS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListNetworkSecurityGroupsRequest.page_size], use
    the [next_page_token] as the value
    for the [ListNetworkSecurityGroupsRequest.page_token] query parameter
    in the next list request. Subsequent list requests will have their own
    [next_page_token] to continue paging through the results.
    """
    @property
    def security_groups(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.vpc.v1.security_group_pb2.SecurityGroup]:
        """List of security groups that belong to the network which is specified in the request."""

    def __init__(
        self,
        *,
        security_groups: collections.abc.Iterable[yandex.cloud.vpc.v1.security_group_pb2.SecurityGroup] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "security_groups", b"security_groups"]) -> None: ...

global___ListNetworkSecurityGroupsResponse = ListNetworkSecurityGroupsResponse

@typing.final
class ListNetworkRouteTablesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NETWORK_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    network_id: builtins.str
    """ID of the Network resource to list route tables for."""
    page_size: builtins.int
    """The maximum number of results per page that should be returned. If the number of available
    results is larger than [page_size],
    the service returns a [ListNetworkRouteTablesResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests. Default value: 100.
    """
    page_token: builtins.str
    """Page token. Set [page_token]
    to the [ListNetworkRouteTablesResponse.next_page_token]
    returned by a previous list request to get the next page of results.
    """
    def __init__(
        self,
        *,
        network_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["network_id", b"network_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListNetworkRouteTablesRequest = ListNetworkRouteTablesRequest

@typing.final
class ListNetworkRouteTablesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ROUTE_TABLES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListNetworkRouteTablesRequest.page_size], use
    the [next_page_token] as the value
    for the [ListNetworkRouteTablesRequest.page_token] query parameter
    in the next list request. Subsequent list requests will have their own
    [next_page_token] to continue paging through the results.
    """
    @property
    def route_tables(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.vpc.v1.route_table_pb2.RouteTable]:
        """List of route tables that belong to the network which is specified in the request."""

    def __init__(
        self,
        *,
        route_tables: collections.abc.Iterable[yandex.cloud.vpc.v1.route_table_pb2.RouteTable] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "route_tables", b"route_tables"]) -> None: ...

global___ListNetworkRouteTablesResponse = ListNetworkRouteTablesResponse

@typing.final
class ListNetworkOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NETWORK_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    network_id: builtins.str
    """ID of the Network resource to list operations for."""
    page_size: builtins.int
    """The maximum number of results per page that should be returned. If the number of available
    results is larger than [page_size], the service returns a [ListNetworkOperationsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests. Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token] to the
    [ListNetworkOperationsResponse.next_page_token] returned by a previous list request.
    """
    def __init__(
        self,
        *,
        network_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["network_id", b"network_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListNetworkOperationsRequest = ListNetworkOperationsRequest

@typing.final
class ListNetworkOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListNetworkOperationsRequest.page_size], use the [next_page_token] as the value
    for the [ListNetworkOperationsRequest.page_token] query parameter in the next list request.
    Each subsequent list request will have its own [next_page_token] to continue paging through the results.
    """
    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.operation.operation_pb2.Operation]:
        """List of operations for the specified network."""

    def __init__(
        self,
        *,
        operations: collections.abc.Iterable[yandex.cloud.operation.operation_pb2.Operation] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "operations", b"operations"]) -> None: ...

global___ListNetworkOperationsResponse = ListNetworkOperationsResponse

@typing.final
class MoveNetworkRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NETWORK_ID_FIELD_NUMBER: builtins.int
    DESTINATION_FOLDER_ID_FIELD_NUMBER: builtins.int
    network_id: builtins.str
    """ID of the Network resource to move."""
    destination_folder_id: builtins.str
    """ID of the destination folder."""
    def __init__(
        self,
        *,
        network_id: builtins.str = ...,
        destination_folder_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["destination_folder_id", b"destination_folder_id", "network_id", b"network_id"]) -> None: ...

global___MoveNetworkRequest = MoveNetworkRequest

@typing.final
class MoveNetworkMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NETWORK_ID_FIELD_NUMBER: builtins.int
    network_id: builtins.str
    """ID of the network that is being moved."""
    def __init__(
        self,
        *,
        network_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["network_id", b"network_id"]) -> None: ...

global___MoveNetworkMetadata = MoveNetworkMetadata
