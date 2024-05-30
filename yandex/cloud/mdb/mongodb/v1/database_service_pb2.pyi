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
import yandex.cloud.mdb.mongodb.v1.database_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetDatabaseRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    DATABASE_NAME_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the MongoDB cluster that the database belongs to.
    To get the cluster ID use a [ClusterService.List] request.
    """
    database_name: builtins.str
    """Name of the MongoDB database to return.
    To get the name of the database use a [DatabaseService.List] request.
    """
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        database_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "database_name", b"database_name"]) -> None: ...

global___GetDatabaseRequest = GetDatabaseRequest

@typing.final
class ListDatabasesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the MongoDB cluster to list databases in.
    To get the cluster ID, use a [ClusterService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size], the service returns a [ListDatabasesResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token] to the 
    [ListDatabasesResponse.next_page_token] returned by the previous list request.
    """
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListDatabasesRequest = ListDatabasesRequest

@typing.final
class ListDatabasesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATABASES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListDatabasesRequest.page_size], use the [next_page_token] as the value
    for the [ListDatabasesRequest.page_token] parameter in the next list request. Each subsequent
    list request will have its own [next_page_token] to continue paging through the results.
    """
    @property
    def databases(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.mdb.mongodb.v1.database_pb2.Database]:
        """List of MongoDB databases."""

    def __init__(
        self,
        *,
        databases: collections.abc.Iterable[yandex.cloud.mdb.mongodb.v1.database_pb2.Database] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["databases", b"databases", "next_page_token", b"next_page_token"]) -> None: ...

global___ListDatabasesResponse = ListDatabasesResponse

@typing.final
class CreateDatabaseRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    DATABASE_SPEC_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the MongoDB cluster to create a database in.
    To get the cluster ID, use a [ClusterService.List] request.
    """
    @property
    def database_spec(self) -> yandex.cloud.mdb.mongodb.v1.database_pb2.DatabaseSpec:
        """Configuration of the database to create."""

    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        database_spec: yandex.cloud.mdb.mongodb.v1.database_pb2.DatabaseSpec | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["database_spec", b"database_spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "database_spec", b"database_spec"]) -> None: ...

global___CreateDatabaseRequest = CreateDatabaseRequest

@typing.final
class CreateDatabaseMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    DATABASE_NAME_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the MongoDB cluster where a database is being created."""
    database_name: builtins.str
    """Name of the MongoDB database that is being created."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        database_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "database_name", b"database_name"]) -> None: ...

global___CreateDatabaseMetadata = CreateDatabaseMetadata

@typing.final
class DeleteDatabaseRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    DATABASE_NAME_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the MongoDB cluster to delete a database in.
    To get the cluster ID, use a [ClusterService.List] request.
    """
    database_name: builtins.str
    """Name of the database to delete.
    To get the name of the database, use a [DatabaseService.List] request.
    """
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        database_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "database_name", b"database_name"]) -> None: ...

global___DeleteDatabaseRequest = DeleteDatabaseRequest

@typing.final
class DeleteDatabaseMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    DATABASE_NAME_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the MongoDB cluster where a database is being deleted."""
    database_name: builtins.str
    """Name of the MongoDB database that is being deleted."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        database_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "database_name", b"database_name"]) -> None: ...

global___DeleteDatabaseMetadata = DeleteDatabaseMetadata
