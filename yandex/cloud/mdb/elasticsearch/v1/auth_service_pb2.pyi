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
import yandex.cloud.mdb.elasticsearch.v1.auth_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class ListAuthProvidersRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """Required. ID of the ElasticSearch cluster."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id"]) -> None: ...

global___ListAuthProvidersRequest = ListAuthProvidersRequest

@typing.final
class ListAuthProvidersResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROVIDERS_FIELD_NUMBER: builtins.int
    @property
    def providers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.mdb.elasticsearch.v1.auth_pb2.AuthProvider]:
        """List of auth providers of the Elasticsearch cluster."""

    def __init__(
        self,
        *,
        providers: collections.abc.Iterable[yandex.cloud.mdb.elasticsearch.v1.auth_pb2.AuthProvider] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["providers", b"providers"]) -> None: ...

global___ListAuthProvidersResponse = ListAuthProvidersResponse

@typing.final
class GetAuthProviderRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """Required. ID of the ElasticSearch cluster."""
    name: builtins.str
    """Required. Name of the provider to delete."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "name", b"name"]) -> None: ...

global___GetAuthProviderRequest = GetAuthProviderRequest

@typing.final
class AddAuthProvidersRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    PROVIDERS_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """Required. ID of the ElasticSearch cluster."""
    @property
    def providers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.mdb.elasticsearch.v1.auth_pb2.AuthProvider]:
        """Required. List of providers to add."""

    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        providers: collections.abc.Iterable[yandex.cloud.mdb.elasticsearch.v1.auth_pb2.AuthProvider] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "providers", b"providers"]) -> None: ...

global___AddAuthProvidersRequest = AddAuthProvidersRequest

@typing.final
class UpdateAuthProvidersRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    PROVIDERS_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """Required. ID of the ElasticSearch cluster."""
    @property
    def providers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.mdb.elasticsearch.v1.auth_pb2.AuthProvider]:
        """Required. List of providers to set."""

    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        providers: collections.abc.Iterable[yandex.cloud.mdb.elasticsearch.v1.auth_pb2.AuthProvider] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "providers", b"providers"]) -> None: ...

global___UpdateAuthProvidersRequest = UpdateAuthProvidersRequest

@typing.final
class DeleteAuthProvidersRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    PROVIDER_NAMES_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """Required. ID of the ElasticSearch cluster."""
    @property
    def provider_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Required. List of providers to delete."""

    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        provider_names: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "provider_names", b"provider_names"]) -> None: ...

global___DeleteAuthProvidersRequest = DeleteAuthProvidersRequest

@typing.final
class UpdateAuthProviderRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    PROVIDER_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """Required. ID of the ElasticSearch cluster."""
    name: builtins.str
    """Required. Name of the provider to update."""
    @property
    def provider(self) -> yandex.cloud.mdb.elasticsearch.v1.auth_pb2.AuthProvider:
        """Required. New provider defenition."""

    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        name: builtins.str = ...,
        provider: yandex.cloud.mdb.elasticsearch.v1.auth_pb2.AuthProvider | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["provider", b"provider"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "name", b"name", "provider", b"provider"]) -> None: ...

global___UpdateAuthProviderRequest = UpdateAuthProviderRequest

@typing.final
class DeleteAuthProviderRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """Required. ID of the ElasticSearch cluster."""
    name: builtins.str
    """Required. Name of the provider to delete."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "name", b"name"]) -> None: ...

global___DeleteAuthProviderRequest = DeleteAuthProviderRequest

@typing.final
class AddAuthProvidersMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    NAMES_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the ElasticSearch cluster."""
    @property
    def names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Names of the providers being added."""

    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        names: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "names", b"names"]) -> None: ...

global___AddAuthProvidersMetadata = AddAuthProvidersMetadata

@typing.final
class UpdateAuthProvidersMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    NAMES_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the ElasticSearch cluster."""
    @property
    def names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Names of the providers being added."""

    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        names: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "names", b"names"]) -> None: ...

global___UpdateAuthProvidersMetadata = UpdateAuthProvidersMetadata

@typing.final
class DeleteAuthProvidersMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    NAMES_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the ElasticSearch cluster."""
    @property
    def names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Names of the providers being removed."""

    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        names: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "names", b"names"]) -> None: ...

global___DeleteAuthProvidersMetadata = DeleteAuthProvidersMetadata
