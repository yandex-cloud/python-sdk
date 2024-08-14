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
import yandex.cloud.iam.v1.workload.oidc.federation_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetFederationRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEDERATION_ID_FIELD_NUMBER: builtins.int
    federation_id: builtins.str
    """ID of the OIDC workload identity federation to return.
    To get the OIDC workload identity federation ID, make a [FederationService.List] request.
    """
    def __init__(
        self,
        *,
        federation_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["federation_id", b"federation_id"]) -> None: ...

global___GetFederationRequest = GetFederationRequest

@typing.final
class ListFederationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to list OIDC workload identity federations in.
    To get the folder ID, make a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListFederationsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token]
    to the [ListFederationsResponse.next_page_token]
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

global___ListFederationsRequest = ListFederationsRequest

@typing.final
class ListFederationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEDERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListFederationsRequest.page_size], use
    the [next_page_token] as the value
    for the [ListFederationsRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    [next_page_token] to continue paging through the results.
    """
    @property
    def federations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.iam.v1.workload.oidc.federation_pb2.Federation]:
        """List of OIDC workload identity federations."""

    def __init__(
        self,
        *,
        federations: collections.abc.Iterable[yandex.cloud.iam.v1.workload.oidc.federation_pb2.Federation] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["federations", b"federations", "next_page_token", b"next_page_token"]) -> None: ...

global___ListFederationsResponse = ListFederationsResponse

@typing.final
class CreateFederationRequest(google.protobuf.message.Message):
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
    DISABLED_FIELD_NUMBER: builtins.int
    AUDIENCES_FIELD_NUMBER: builtins.int
    ISSUER_FIELD_NUMBER: builtins.int
    JWKS_URL_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to create an OIDC workload identity federation in.
    To get the folder ID, make a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    name: builtins.str
    """Name of the OIDC workload identity federation.
    The name must be unique within the folder.
    """
    description: builtins.str
    """Description of the OIDC workload identity federation."""
    disabled: builtins.bool
    """True - the OIDC workload identity federation is disabled and cannot be used for authentication.
    False - the OIDC workload identity federation is enabled and can be used for authentication.
    """
    issuer: builtins.str
    """URL of the external IdP server to be used for authentication."""
    jwks_url: builtins.str
    """URL reference to trusted keys in format of JSON Web Key Set."""
    @property
    def audiences(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of trusted values for aud claim."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `` key:value `` pairs"""

    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        disabled: builtins.bool = ...,
        audiences: collections.abc.Iterable[builtins.str] | None = ...,
        issuer: builtins.str = ...,
        jwks_url: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["audiences", b"audiences", "description", b"description", "disabled", b"disabled", "folder_id", b"folder_id", "issuer", b"issuer", "jwks_url", b"jwks_url", "labels", b"labels", "name", b"name"]) -> None: ...

global___CreateFederationRequest = CreateFederationRequest

@typing.final
class CreateFederationMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEDERATION_ID_FIELD_NUMBER: builtins.int
    federation_id: builtins.str
    """ID of the OIDC workload identity federation that is being created."""
    def __init__(
        self,
        *,
        federation_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["federation_id", b"federation_id"]) -> None: ...

global___CreateFederationMetadata = CreateFederationMetadata

@typing.final
class UpdateFederationRequest(google.protobuf.message.Message):
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

    FEDERATION_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    DISABLED_FIELD_NUMBER: builtins.int
    AUDIENCES_FIELD_NUMBER: builtins.int
    JWKS_URL_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    federation_id: builtins.str
    """ID of the OIDC workload identity federation to update.
    To get the OIDC workload identity federation ID, make a [FederationService.List] request.
    """
    name: builtins.str
    """Name of the OIDC workload identity federation.
    The name must be unique within the folder.
    """
    description: builtins.str
    """Description of the OIDC workload identity federation."""
    disabled: builtins.bool
    """True - the OIDC workload identity federation is disabled and cannot be used for authentication.
    False - the OIDC workload identity federation is enabled and can be used for authentication.
    """
    jwks_url: builtins.str
    """URL reference to trusted keys in format of JSON Web Key Set."""
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which fields of the OIDC workload identity federation are going to be updated."""

    @property
    def audiences(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of trusted values for aud claim."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `` key:value `` pairs"""

    def __init__(
        self,
        *,
        federation_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        disabled: builtins.bool = ...,
        audiences: collections.abc.Iterable[builtins.str] | None = ...,
        jwks_url: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["audiences", b"audiences", "description", b"description", "disabled", b"disabled", "federation_id", b"federation_id", "jwks_url", b"jwks_url", "labels", b"labels", "name", b"name", "update_mask", b"update_mask"]) -> None: ...

global___UpdateFederationRequest = UpdateFederationRequest

@typing.final
class UpdateFederationMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEDERATION_ID_FIELD_NUMBER: builtins.int
    federation_id: builtins.str
    """ID of the OIDC workload identity federation that is being updated."""
    def __init__(
        self,
        *,
        federation_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["federation_id", b"federation_id"]) -> None: ...

global___UpdateFederationMetadata = UpdateFederationMetadata

@typing.final
class DeleteFederationRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEDERATION_ID_FIELD_NUMBER: builtins.int
    federation_id: builtins.str
    """ID of the OIDC workload identity federation to delete.
    To get the OIDC workload identity federation ID, make a [FederationService.List] request.
    """
    def __init__(
        self,
        *,
        federation_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["federation_id", b"federation_id"]) -> None: ...

global___DeleteFederationRequest = DeleteFederationRequest

@typing.final
class DeleteFederationMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEDERATION_ID_FIELD_NUMBER: builtins.int
    federation_id: builtins.str
    """ID of the OIDC workload identity federation that is being deleted."""
    def __init__(
        self,
        *,
        federation_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["federation_id", b"federation_id"]) -> None: ...

global___DeleteFederationMetadata = DeleteFederationMetadata
