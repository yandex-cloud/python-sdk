"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.wrappers_pb2
import typing
import yandex.cloud.cdn.v1.origin_pb2
import yandex.cloud.cdn.v1.resource_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetResourceRequest(google.protobuf.message.Message):
    """A request to get a resource."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_ID_FIELD_NUMBER: builtins.int
    resource_id: builtins.str
    """ID of the requested resource."""
    def __init__(
        self,
        *,
        resource_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["resource_id", b"resource_id"]) -> None: ...

global___GetResourceRequest = GetResourceRequest

@typing.final
class ListResourcesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to request listing for."""
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListResourcesResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    """
    page_token: builtins.str
    """Page token. To get the next page of results,
    set [page_token] to the [ListResourcesResponse.next_page_token]
    returned by a previous list request.
    """
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["folder_id", b"folder_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListResourcesRequest = ListResourcesRequest

@typing.final
class ListResourcesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """[next_page_token] token allows you to get the next page of results for list requests.
    If the number of results is larger than [ListResourcesRequest.page_size], use
    the [next_page_token] as the value for the [ListResourcesRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    [next_page_token] to continue paging through the results.
    """
    @property
    def resources(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.cdn.v1.resource_pb2.Resource]:
        """List of the resources"""

    def __init__(
        self,
        *,
        resources: collections.abc.Iterable[yandex.cloud.cdn.v1.resource_pb2.Resource] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "resources", b"resources"]) -> None: ...

global___ListResourcesResponse = ListResourcesResponse

@typing.final
class CreateResourceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Origin(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        ORIGIN_GROUP_ID_FIELD_NUMBER: builtins.int
        ORIGIN_SOURCE_FIELD_NUMBER: builtins.int
        ORIGIN_SOURCE_PARAMS_FIELD_NUMBER: builtins.int
        origin_group_id: builtins.int
        """ID of pre-created origin group."""
        origin_source: builtins.str
        """Create new Origins group with single source, it's id will be
        returned in result.
        """
        @property
        def origin_source_params(self) -> global___ResourceOriginParams:
            """Set up resource origin parameters."""

        def __init__(
            self,
            *,
            origin_group_id: builtins.int = ...,
            origin_source: builtins.str = ...,
            origin_source_params: global___ResourceOriginParams | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["origin_group_id", b"origin_group_id", "origin_source", b"origin_source", "origin_source_params", b"origin_source_params", "origin_variant", b"origin_variant"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["origin_group_id", b"origin_group_id", "origin_source", b"origin_source", "origin_source_params", b"origin_source_params", "origin_variant", b"origin_variant"]) -> None: ...
        def WhichOneof(self, oneof_group: typing.Literal["origin_variant", b"origin_variant"]) -> typing.Literal["origin_group_id", "origin_source", "origin_source_params"] | None: ...

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
    CNAME_FIELD_NUMBER: builtins.int
    ORIGIN_FIELD_NUMBER: builtins.int
    SECONDARY_HOSTNAMES_FIELD_NUMBER: builtins.int
    ORIGIN_PROTOCOL_FIELD_NUMBER: builtins.int
    ACTIVE_FIELD_NUMBER: builtins.int
    OPTIONS_FIELD_NUMBER: builtins.int
    SSL_CERTIFICATE_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the to bind with new resource."""
    cname: builtins.str
    """CDN endpoint CNAME, must be unique among clients's resources."""
    origin_protocol: yandex.cloud.cdn.v1.resource_pb2.OriginProtocol.ValueType
    """Specify the protocol schema to be used in communication with origin."""
    @property
    def origin(self) -> global___CreateResourceRequest.Origin:
        """Specify the origins to be used for CDN resources requests."""

    @property
    def secondary_hostnames(self) -> yandex.cloud.cdn.v1.resource_pb2.SecondaryHostnames:
        """List of additional CNAMEs."""

    @property
    def active(self) -> google.protobuf.wrappers_pb2.BoolValue:
        """Flag to create Resource either in active or disabled state.
        In active state Origins payload could be transmitted from CDN CNAME requests.
        Default value: true
        """

    @property
    def options(self) -> yandex.cloud.cdn.v1.resource_pb2.ResourceOptions:
        """Resource settings and options to tune CDN edge behavior. Most is unset."""

    @property
    def ssl_certificate(self) -> yandex.cloud.cdn.v1.resource_pb2.SSLTargetCertificate:
        """SSL Certificate options."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Labels of the resource."""

    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        cname: builtins.str = ...,
        origin: global___CreateResourceRequest.Origin | None = ...,
        secondary_hostnames: yandex.cloud.cdn.v1.resource_pb2.SecondaryHostnames | None = ...,
        origin_protocol: yandex.cloud.cdn.v1.resource_pb2.OriginProtocol.ValueType = ...,
        active: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        options: yandex.cloud.cdn.v1.resource_pb2.ResourceOptions | None = ...,
        ssl_certificate: yandex.cloud.cdn.v1.resource_pb2.SSLTargetCertificate | None = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["active", b"active", "options", b"options", "origin", b"origin", "secondary_hostnames", b"secondary_hostnames", "ssl_certificate", b"ssl_certificate"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["active", b"active", "cname", b"cname", "folder_id", b"folder_id", "labels", b"labels", "options", b"options", "origin", b"origin", "origin_protocol", b"origin_protocol", "secondary_hostnames", b"secondary_hostnames", "ssl_certificate", b"ssl_certificate"]) -> None: ...

global___CreateResourceRequest = CreateResourceRequest

@typing.final
class ResourceOriginParams(google.protobuf.message.Message):
    """A set of resource origin parameters."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SOURCE_FIELD_NUMBER: builtins.int
    META_FIELD_NUMBER: builtins.int
    source: builtins.str
    """Source of the content."""
    @property
    def meta(self) -> yandex.cloud.cdn.v1.origin_pb2.OriginMeta:
        """Set up type of the origin."""

    def __init__(
        self,
        *,
        source: builtins.str = ...,
        meta: yandex.cloud.cdn.v1.origin_pb2.OriginMeta | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["meta", b"meta"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["meta", b"meta", "source", b"source"]) -> None: ...

global___ResourceOriginParams = ResourceOriginParams

@typing.final
class CreateResourceMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_ID_FIELD_NUMBER: builtins.int
    resource_id: builtins.str
    """ID of created resource."""
    def __init__(
        self,
        *,
        resource_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["resource_id", b"resource_id"]) -> None: ...

global___CreateResourceMetadata = CreateResourceMetadata

@typing.final
class UpdateResourceRequest(google.protobuf.message.Message):
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

    RESOURCE_ID_FIELD_NUMBER: builtins.int
    ORIGIN_GROUP_ID_FIELD_NUMBER: builtins.int
    SECONDARY_HOSTNAMES_FIELD_NUMBER: builtins.int
    OPTIONS_FIELD_NUMBER: builtins.int
    ORIGIN_PROTOCOL_FIELD_NUMBER: builtins.int
    ACTIVE_FIELD_NUMBER: builtins.int
    SSL_CERTIFICATE_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    resource_id: builtins.str
    """ID of updated resource."""
    origin_protocol: yandex.cloud.cdn.v1.resource_pb2.OriginProtocol.ValueType
    """Specify the protocol schema to be used in communication with origin."""
    @property
    def origin_group_id(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """ID of updated origin group."""

    @property
    def secondary_hostnames(self) -> yandex.cloud.cdn.v1.resource_pb2.SecondaryHostnames:
        """List of additional CNAMEs."""

    @property
    def options(self) -> yandex.cloud.cdn.v1.resource_pb2.ResourceOptions:
        """Resource settings and options to tune CDN edge behavior."""

    @property
    def active(self) -> google.protobuf.wrappers_pb2.BoolValue:
        """Flag to create Resource either in active or disabled state.
        In active state Origins payload could be transmitted from CDN CNAME requests.
        Default value: true
        """

    @property
    def ssl_certificate(self) -> yandex.cloud.cdn.v1.resource_pb2.SSLTargetCertificate:
        """SSL Certificate options."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels. At some point will be needed for granular detailing."""

    def __init__(
        self,
        *,
        resource_id: builtins.str = ...,
        origin_group_id: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        secondary_hostnames: yandex.cloud.cdn.v1.resource_pb2.SecondaryHostnames | None = ...,
        options: yandex.cloud.cdn.v1.resource_pb2.ResourceOptions | None = ...,
        origin_protocol: yandex.cloud.cdn.v1.resource_pb2.OriginProtocol.ValueType = ...,
        active: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        ssl_certificate: yandex.cloud.cdn.v1.resource_pb2.SSLTargetCertificate | None = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["active", b"active", "options", b"options", "origin_group_id", b"origin_group_id", "secondary_hostnames", b"secondary_hostnames", "ssl_certificate", b"ssl_certificate"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["active", b"active", "labels", b"labels", "options", b"options", "origin_group_id", b"origin_group_id", "origin_protocol", b"origin_protocol", "resource_id", b"resource_id", "secondary_hostnames", b"secondary_hostnames", "ssl_certificate", b"ssl_certificate"]) -> None: ...

global___UpdateResourceRequest = UpdateResourceRequest

@typing.final
class UpdateResourceMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_ID_FIELD_NUMBER: builtins.int
    resource_id: builtins.str
    """ID of updated resource."""
    def __init__(
        self,
        *,
        resource_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["resource_id", b"resource_id"]) -> None: ...

global___UpdateResourceMetadata = UpdateResourceMetadata

@typing.final
class DeleteResourceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_ID_FIELD_NUMBER: builtins.int
    resource_id: builtins.str
    """ID of resource to delete."""
    def __init__(
        self,
        *,
        resource_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["resource_id", b"resource_id"]) -> None: ...

global___DeleteResourceRequest = DeleteResourceRequest

@typing.final
class DeleteResourceMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_ID_FIELD_NUMBER: builtins.int
    resource_id: builtins.str
    """ID of deleted resource."""
    def __init__(
        self,
        *,
        resource_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["resource_id", b"resource_id"]) -> None: ...

global___DeleteResourceMetadata = DeleteResourceMetadata

@typing.final
class GetProviderCNameRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """Folder ID to get provider's CNAME."""
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["folder_id", b"folder_id"]) -> None: ...

global___GetProviderCNameRequest = GetProviderCNameRequest

@typing.final
class GetProviderCNameResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CNAME_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    cname: builtins.str
    """Provider's CNAME."""
    folder_id: builtins.str
    """ID of the folder that the provider belongs to."""
    def __init__(
        self,
        *,
        cname: builtins.str = ...,
        folder_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cname", b"cname", "folder_id", b"folder_id"]) -> None: ...

global___GetProviderCNameResponse = GetProviderCNameResponse
