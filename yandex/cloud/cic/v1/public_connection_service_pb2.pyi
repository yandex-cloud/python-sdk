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
import yandex.cloud.cic.v1.public_connection_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetPublicConnectionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PUBLIC_CONNECTION_ID_FIELD_NUMBER: builtins.int
    public_connection_id: builtins.str
    """ID of the PublicConnection resource to return.
    To get the publicConnection ID use a [PublicConnectionService.List] request.
    """
    def __init__(
        self,
        *,
        public_connection_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["public_connection_id", b"public_connection_id"]) -> None: ...

global___GetPublicConnectionRequest = GetPublicConnectionRequest

@typing.final
class ListPublicConnectionsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to list publicConnections in.
    To get the folder ID use a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListPublicConnectionsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests. Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token] to the
    [ListPublicConnectionsResponse.next_page_token] returned by a previous list request.
    """
    filter: builtins.str
    """A filter expression that filters resources listed in the response.
    The expression must specify:
    1. The field name. Currently you can use filtering only on [Subnet.name] field.
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

global___ListPublicConnectionsRequest = ListPublicConnectionsRequest

@typing.final
class ListPublicConnectionsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PUBLIC_CONNECTIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListPublicConnectionsRequest.page_size], use
    the [next_page_token] as the value
    for the [ListPublicConnectionsRequest.page_token] query parameter
    in the next list request. Subsequent list requests will have their own
    [next_page_token] to continue paging through the results.
    """
    @property
    def public_connections(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.cic.v1.public_connection_pb2.PublicConnection]:
        """List of PublicConnection resources."""

    def __init__(
        self,
        *,
        public_connections: collections.abc.Iterable[yandex.cloud.cic.v1.public_connection_pb2.PublicConnection] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "public_connections", b"public_connections"]) -> None: ...

global___ListPublicConnectionsResponse = ListPublicConnectionsResponse