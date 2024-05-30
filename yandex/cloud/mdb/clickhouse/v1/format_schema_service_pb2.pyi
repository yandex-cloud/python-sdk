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
import yandex.cloud.mdb.clickhouse.v1.format_schema_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetFormatSchemaRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    FORMAT_SCHEMA_NAME_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ClickHouse cluster ID.

    To get a ClickHouse cluster ID, use the [ClusterService.List] method.
    """
    format_schema_name: builtins.str
    """Format schema name.

    To get a format schema name, use the [FormatSchemaService.List] method.
    """
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        format_schema_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "format_schema_name", b"format_schema_name"]) -> None: ...

global___GetFormatSchemaRequest = GetFormatSchemaRequest

@typing.final
class ListFormatSchemasRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ClickHouse cluster ID.

    To get a ClickHouse cluster ID, use the [ClusterService.List] method.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of the results is larger than [page_size], the service returns [ListFormatSchemasResponse.next_page_token]. You can use it to get the next page of the results in subsequent requests of a format schema list."""
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token] to the [ListFormatSchemasResponse.next_page_token] returned by the previous format schema list request."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListFormatSchemasRequest = ListFormatSchemasRequest

@typing.final
class ListFormatSchemasResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FORMAT_SCHEMAS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results when requesting the format schema list. If the number of the results is larger than [ListFormatSchemasRequest.page_size], use the [next_page_token] as the value for the [ListFormatSchemasRequest.page_token] parameter in the next request. Each subsequent request will have its own [next_page_token] to continue paging through the results."""
    @property
    def format_schemas(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.mdb.clickhouse.v1.format_schema_pb2.FormatSchema]:
        """List of format schemas."""

    def __init__(
        self,
        *,
        format_schemas: collections.abc.Iterable[yandex.cloud.mdb.clickhouse.v1.format_schema_pb2.FormatSchema] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["format_schemas", b"format_schemas", "next_page_token", b"next_page_token"]) -> None: ...

global___ListFormatSchemasResponse = ListFormatSchemasResponse

@typing.final
class CreateFormatSchemaRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    FORMAT_SCHEMA_NAME_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ClickHouse cluster ID.

    To get a ClickHouse cluster ID, use the [ClusterService.List] method.
    """
    format_schema_name: builtins.str
    """Format schema name."""
    type: yandex.cloud.mdb.clickhouse.v1.format_schema_pb2.FormatSchemaType.ValueType
    """Schema type. Possible values are the following:

    * FORMAT_SCHEMA_TYPE_PROTOBUF - [Protobuf](https://protobuf.dev/) data format (including [ProtobufSingle](https://clickhouse.com/docs/en/interfaces/formats#protobufsingle)).
    * FORMAT_SCHEMA_TYPE_CAPNPROTO - [Cap'n Proto](https://capnproto.org/) data format.
    """
    uri: builtins.str
    """[Link to the file](/docs/managed-clickhouse/operations/s3-access#get-link-to-object) of a format schema in Yandex Object Storage. Managed Service for ClickHouse works only with format schemas imported to Object Storage."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        format_schema_name: builtins.str = ...,
        type: yandex.cloud.mdb.clickhouse.v1.format_schema_pb2.FormatSchemaType.ValueType = ...,
        uri: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "format_schema_name", b"format_schema_name", "type", b"type", "uri", b"uri"]) -> None: ...

global___CreateFormatSchemaRequest = CreateFormatSchemaRequest

@typing.final
class CreateFormatSchemaMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    FORMAT_SCHEMA_NAME_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ClickHouse cluster ID."""
    format_schema_name: builtins.str
    """Format schema name."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        format_schema_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "format_schema_name", b"format_schema_name"]) -> None: ...

global___CreateFormatSchemaMetadata = CreateFormatSchemaMetadata

@typing.final
class UpdateFormatSchemaRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    FORMAT_SCHEMA_NAME_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ClickHouse cluster ID.

    To get a ClickHouse cluster ID, use the [ClusterService.List] method.
    """
    format_schema_name: builtins.str
    """Format schema name.

    To get a format schema name, use the [FormatSchemaService.List] method.
    """
    uri: builtins.str
    """[Link to the file](/docs/managed-clickhouse/operations/s3-access#get-link-to-object) of a format schema in Yandex Object Storage. Managed Service for ClickHouse works only with format schemas imported to Object Storage."""
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask: ...
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        format_schema_name: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        uri: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "format_schema_name", b"format_schema_name", "update_mask", b"update_mask", "uri", b"uri"]) -> None: ...

global___UpdateFormatSchemaRequest = UpdateFormatSchemaRequest

@typing.final
class UpdateFormatSchemaMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    FORMAT_SCHEMA_NAME_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ClickHouse cluster ID."""
    format_schema_name: builtins.str
    """Format schema name."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        format_schema_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "format_schema_name", b"format_schema_name"]) -> None: ...

global___UpdateFormatSchemaMetadata = UpdateFormatSchemaMetadata

@typing.final
class DeleteFormatSchemaRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    FORMAT_SCHEMA_NAME_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ClickHouse cluster ID.

    To get a ClickHouse cluster ID, use the [ClusterService.List] method.
    """
    format_schema_name: builtins.str
    """Format schema name.

    To get a format schema name, use the [FormatSchemaService.List] method.
    """
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        format_schema_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "format_schema_name", b"format_schema_name"]) -> None: ...

global___DeleteFormatSchemaRequest = DeleteFormatSchemaRequest

@typing.final
class DeleteFormatSchemaMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    FORMAT_SCHEMA_NAME_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ClickHouse cluster ID."""
    format_schema_name: builtins.str
    """Format schema name."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        format_schema_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "format_schema_name", b"format_schema_name"]) -> None: ...

global___DeleteFormatSchemaMetadata = DeleteFormatSchemaMetadata
