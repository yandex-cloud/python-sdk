"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import yandex.cloud.operation.operation_pb2
import yandex.cloud.organizationmanager.v1.saml.federation_pb2
import yandex.cloud.organizationmanager.v1.user_account_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetFederationRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEDERATION_ID_FIELD_NUMBER: builtins.int
    federation_id: builtins.str
    """ID of the federation to return.
    To get the federation ID, make a [FederationService.List] request.
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

    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    organization_id: builtins.str
    """ID of the organization to list federations in.
    To get the organization ID, make a [yandex.cloud.organizationmanager.v1.OrganizationService.List] request.
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
    filter: builtins.str
    """A filter expression that filters resources listed in the response.
    The expression must specify:
    1. The field name. Currently you can use filtering only on the [Federation.name] field.
    2. An `=` operator.
    3. The value in double quotes (`"`). Must be 3-63 characters long and match the regular expression `[a-z][-a-z0-9]{1,61}[a-z0-9]`.
    """
    def __init__(
        self,
        *,
        organization_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["filter", b"filter", "organization_id", b"organization_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

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
    def federations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.organizationmanager.v1.saml.federation_pb2.Federation]:
        """List of federations."""

    def __init__(
        self,
        *,
        federations: collections.abc.Iterable[yandex.cloud.organizationmanager.v1.saml.federation_pb2.Federation] | None = ...,
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

    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    COOKIE_MAX_AGE_FIELD_NUMBER: builtins.int
    AUTO_CREATE_ACCOUNT_ON_LOGIN_FIELD_NUMBER: builtins.int
    ISSUER_FIELD_NUMBER: builtins.int
    SSO_BINDING_FIELD_NUMBER: builtins.int
    SSO_URL_FIELD_NUMBER: builtins.int
    SECURITY_SETTINGS_FIELD_NUMBER: builtins.int
    CASE_INSENSITIVE_NAME_IDS_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    organization_id: builtins.str
    """ID of the organization to create a federation in.
    To get the organization ID, make a [yandex.cloud.organizationmanager.v1.OrganizationService.List] request.
    """
    name: builtins.str
    """Name of the federation.
    The name must be unique within the organization.
    """
    description: builtins.str
    """Description of the federation."""
    auto_create_account_on_login: builtins.bool
    """Add new users automatically on successful authentication.
    The user becomes member of the organization automatically,
    but you need to grant other roles to them.

    If the value is `false`, users who aren't added to the organization
    can't log in, even if they have authenticated on your server.
    """
    issuer: builtins.str
    """ID of the IdP server to be used for authentication.
    The IdP server also responds to IAM with this ID after the user authenticates.
    """
    sso_binding: yandex.cloud.organizationmanager.v1.saml.federation_pb2.BindingType.ValueType
    """Single sign-on endpoint binding type. Most Identity Providers support the `POST` binding type.

    SAML Binding is a mapping of a SAML protocol message onto standard messaging
    formats and/or communications protocols.
    """
    sso_url: builtins.str
    """Single sign-on endpoint URL.
    Specify the link to the IdP login page here.
    """
    case_insensitive_name_ids: builtins.bool
    """Use case insensitive Name IDs."""
    @property
    def cookie_max_age(self) -> google.protobuf.duration_pb2.Duration:
        """Browser cookie lifetime in seconds.
        If the cookie is still valid, the management console
        authenticates the user immediately and redirects them to the home page.
        The default value is `8h`.
        """

    @property
    def security_settings(self) -> yandex.cloud.organizationmanager.v1.saml.federation_pb2.FederationSecuritySettings:
        """Federation security settings."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `` key:value `` pairs."""

    def __init__(
        self,
        *,
        organization_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        cookie_max_age: google.protobuf.duration_pb2.Duration | None = ...,
        auto_create_account_on_login: builtins.bool = ...,
        issuer: builtins.str = ...,
        sso_binding: yandex.cloud.organizationmanager.v1.saml.federation_pb2.BindingType.ValueType = ...,
        sso_url: builtins.str = ...,
        security_settings: yandex.cloud.organizationmanager.v1.saml.federation_pb2.FederationSecuritySettings | None = ...,
        case_insensitive_name_ids: builtins.bool = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["cookie_max_age", b"cookie_max_age", "security_settings", b"security_settings"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["auto_create_account_on_login", b"auto_create_account_on_login", "case_insensitive_name_ids", b"case_insensitive_name_ids", "cookie_max_age", b"cookie_max_age", "description", b"description", "issuer", b"issuer", "labels", b"labels", "name", b"name", "organization_id", b"organization_id", "security_settings", b"security_settings", "sso_binding", b"sso_binding", "sso_url", b"sso_url"]) -> None: ...

global___CreateFederationRequest = CreateFederationRequest

@typing.final
class CreateFederationMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEDERATION_ID_FIELD_NUMBER: builtins.int
    federation_id: builtins.str
    """ID of the federation that is being created."""
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
    COOKIE_MAX_AGE_FIELD_NUMBER: builtins.int
    AUTO_CREATE_ACCOUNT_ON_LOGIN_FIELD_NUMBER: builtins.int
    ISSUER_FIELD_NUMBER: builtins.int
    SSO_BINDING_FIELD_NUMBER: builtins.int
    SSO_URL_FIELD_NUMBER: builtins.int
    SECURITY_SETTINGS_FIELD_NUMBER: builtins.int
    CASE_INSENSITIVE_NAME_IDS_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    federation_id: builtins.str
    """ID of the federation to update.
    To get the federation ID, make a [FederationService.List] request.
    """
    name: builtins.str
    """Name of the federation.
    The name must be unique within the organization.
    """
    description: builtins.str
    """Description of the federation."""
    auto_create_account_on_login: builtins.bool
    """Add new users automatically on successful authentication.
    The user becomes member of the organization automatically,
    but you need to grant other roles to them.

    If the value is `false`, users who aren't added to the organization
    can't log in, even if they have authenticated on your server.
    """
    issuer: builtins.str
    """ID of the IdP server to be used for authentication.
    The IdP server also responds to IAM with this ID after the user authenticates.
    """
    sso_binding: yandex.cloud.organizationmanager.v1.saml.federation_pb2.BindingType.ValueType
    """Single sign-on endpoint binding type. Most Identity Providers support the `POST` binding type.

    SAML Binding is a mapping of a SAML protocol message onto standard messaging
    formats and/or communications protocols.
    """
    sso_url: builtins.str
    """Single sign-on endpoint URL.
    Specify the link to the IdP login page here.
    """
    case_insensitive_name_ids: builtins.bool
    """Use case insensitive name ids."""
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which fields of the federation are going to be updated."""

    @property
    def cookie_max_age(self) -> google.protobuf.duration_pb2.Duration:
        """Browser cookie lifetime in seconds.
        If the cookie is still valid, the management console
        authenticates the user immediately and redirects them to the home page.
        The default value is `8h`.
        """

    @property
    def security_settings(self) -> yandex.cloud.organizationmanager.v1.saml.federation_pb2.FederationSecuritySettings:
        """Federation security settings."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `` key:value `` pairs."""

    def __init__(
        self,
        *,
        federation_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        cookie_max_age: google.protobuf.duration_pb2.Duration | None = ...,
        auto_create_account_on_login: builtins.bool = ...,
        issuer: builtins.str = ...,
        sso_binding: yandex.cloud.organizationmanager.v1.saml.federation_pb2.BindingType.ValueType = ...,
        sso_url: builtins.str = ...,
        security_settings: yandex.cloud.organizationmanager.v1.saml.federation_pb2.FederationSecuritySettings | None = ...,
        case_insensitive_name_ids: builtins.bool = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["cookie_max_age", b"cookie_max_age", "security_settings", b"security_settings", "update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["auto_create_account_on_login", b"auto_create_account_on_login", "case_insensitive_name_ids", b"case_insensitive_name_ids", "cookie_max_age", b"cookie_max_age", "description", b"description", "federation_id", b"federation_id", "issuer", b"issuer", "labels", b"labels", "name", b"name", "security_settings", b"security_settings", "sso_binding", b"sso_binding", "sso_url", b"sso_url", "update_mask", b"update_mask"]) -> None: ...

global___UpdateFederationRequest = UpdateFederationRequest

@typing.final
class UpdateFederationMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEDERATION_ID_FIELD_NUMBER: builtins.int
    federation_id: builtins.str
    """ID of the federation that is being updated."""
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
    """ID of the federation to delete.
    To get the federation ID, make a [FederationService.List] request.
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
    """ID of the federation that is being deleted."""
    def __init__(
        self,
        *,
        federation_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["federation_id", b"federation_id"]) -> None: ...

global___DeleteFederationMetadata = DeleteFederationMetadata

@typing.final
class AddFederatedUserAccountsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEDERATION_ID_FIELD_NUMBER: builtins.int
    NAME_IDS_FIELD_NUMBER: builtins.int
    federation_id: builtins.str
    """ID of the federation to add users."""
    @property
    def name_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Name IDs returned by the Identity Provider (IdP) on successful authentication.
        These may be UPNs or user email addresses.
        """

    def __init__(
        self,
        *,
        federation_id: builtins.str = ...,
        name_ids: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["federation_id", b"federation_id", "name_ids", b"name_ids"]) -> None: ...

global___AddFederatedUserAccountsRequest = AddFederatedUserAccountsRequest

@typing.final
class AddFederatedUserAccountsMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEDERATION_ID_FIELD_NUMBER: builtins.int
    federation_id: builtins.str
    """ID of the federation that is being altered."""
    def __init__(
        self,
        *,
        federation_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["federation_id", b"federation_id"]) -> None: ...

global___AddFederatedUserAccountsMetadata = AddFederatedUserAccountsMetadata

@typing.final
class AddFederatedUserAccountsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_ACCOUNTS_FIELD_NUMBER: builtins.int
    @property
    def user_accounts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.organizationmanager.v1.user_account_pb2.UserAccount]:
        """List of users created by [FederationService.AddUserAccounts] request."""

    def __init__(
        self,
        *,
        user_accounts: collections.abc.Iterable[yandex.cloud.organizationmanager.v1.user_account_pb2.UserAccount] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["user_accounts", b"user_accounts"]) -> None: ...

global___AddFederatedUserAccountsResponse = AddFederatedUserAccountsResponse

@typing.final
class DeleteFederatedUserAccountsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEDERATION_ID_FIELD_NUMBER: builtins.int
    SUBJECT_IDS_FIELD_NUMBER: builtins.int
    federation_id: builtins.str
    """ID of the federation to delete users from."""
    @property
    def subject_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of subjects to delete."""

    def __init__(
        self,
        *,
        federation_id: builtins.str = ...,
        subject_ids: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["federation_id", b"federation_id", "subject_ids", b"subject_ids"]) -> None: ...

global___DeleteFederatedUserAccountsRequest = DeleteFederatedUserAccountsRequest

@typing.final
class DeleteFederatedUserAccountsMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEDERATION_ID_FIELD_NUMBER: builtins.int
    federation_id: builtins.str
    """ID of the federation that is being altered."""
    def __init__(
        self,
        *,
        federation_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["federation_id", b"federation_id"]) -> None: ...

global___DeleteFederatedUserAccountsMetadata = DeleteFederatedUserAccountsMetadata

@typing.final
class DeleteFederatedUserAccountsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DELETED_SUBJECTS_FIELD_NUMBER: builtins.int
    NON_EXISTING_SUBJECTS_FIELD_NUMBER: builtins.int
    @property
    def deleted_subjects(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of subjects deleted by [FederationService.DeleteUserAccounts] request."""

    @property
    def non_existing_subjects(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of subjects found in [FederationService.DeleteUserAccounts] request that do not exist."""

    def __init__(
        self,
        *,
        deleted_subjects: collections.abc.Iterable[builtins.str] | None = ...,
        non_existing_subjects: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["deleted_subjects", b"deleted_subjects", "non_existing_subjects", b"non_existing_subjects"]) -> None: ...

global___DeleteFederatedUserAccountsResponse = DeleteFederatedUserAccountsResponse

@typing.final
class ListFederatedUserAccountsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEDERATION_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    federation_id: builtins.str
    """ID of the federation to list user accounts for."""
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size], the service returns a [ListFederatedUserAccountsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token]
    to the [ListFederatedUserAccountsResponse.next_page_token]
    returned by a previous list request.
    """
    filter: builtins.str
    """A filter expression that filters resources listed in the response.
    The expression must specify:
    1. The field name. Currently you can use filtering only on the [name_id] field.
    2. An `=` operator.
    3. The value in double quotes (`"`). Must be 1-1000 characters long and match the regular expression
      `[a-z0-9A-Z/@_.\\-=+*\\\\]+`.
    """
    def __init__(
        self,
        *,
        federation_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["federation_id", b"federation_id", "filter", b"filter", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListFederatedUserAccountsRequest = ListFederatedUserAccountsRequest

@typing.final
class ListFederatedUserAccountsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_ACCOUNTS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListFederatedUserAccountsRequest.page_size], use the [next_page_token] as the value
    for the [ListFederatedUserAccountsRequest.page_token] query parameter in the next list request.
    Each subsequent list request will have its own [next_page_token] to continue paging through the results.
    """
    @property
    def user_accounts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.organizationmanager.v1.user_account_pb2.UserAccount]:
        """List of user accounts for the specified federation."""

    def __init__(
        self,
        *,
        user_accounts: collections.abc.Iterable[yandex.cloud.organizationmanager.v1.user_account_pb2.UserAccount] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "user_accounts", b"user_accounts"]) -> None: ...

global___ListFederatedUserAccountsResponse = ListFederatedUserAccountsResponse

@typing.final
class ListFederationOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEDERATION_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    federation_id: builtins.str
    """ID of the federation to list operations for."""
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size], the service returns a [ListFederationOperationsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token]
    to the [ListFederationOperationsResponse.next_page_token]
    returned by a previous list request.
    """
    def __init__(
        self,
        *,
        federation_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["federation_id", b"federation_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListFederationOperationsRequest = ListFederationOperationsRequest

@typing.final
class ListFederationOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListFederationOperationsRequest.page_size], use the [next_page_token] as the value
    for the [ListFederationOperationsRequest.page_token] query parameter in the next list request.
    Each subsequent list request will have its own [next_page_token] to continue paging through the results.
    """
    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.operation.operation_pb2.Operation]:
        """List of operations for the specified federation."""

    def __init__(
        self,
        *,
        operations: collections.abc.Iterable[yandex.cloud.operation.operation_pb2.Operation] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "operations", b"operations"]) -> None: ...

global___ListFederationOperationsResponse = ListFederationOperationsResponse

@typing.final
class GetFederationDomainRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEDERATION_ID_FIELD_NUMBER: builtins.int
    DOMAIN_FIELD_NUMBER: builtins.int
    federation_id: builtins.str
    """ID of the federation to get domain information for.
    To get the federation ID, make a [FederationService.List] request.
    """
    domain: builtins.str
    """Domain name to get information for.
    Must be a valid domain name (1-253 characters).
    """
    def __init__(
        self,
        *,
        federation_id: builtins.str = ...,
        domain: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["domain", b"domain", "federation_id", b"federation_id"]) -> None: ...

global___GetFederationDomainRequest = GetFederationDomainRequest

@typing.final
class ListFederationDomainsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEDERATION_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    federation_id: builtins.str
    """ID of the federation to list domains for.
    To get the federation ID, make a [FederationService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size], the service returns a [ListFederationDomainsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token]
    to the [ListFederationDomainsResponse.next_page_token]
    returned by a previous list request.
    """
    filter: builtins.str
    """A filter expression that filters resources listed in the response.
    The expression supports the following operations:
    - `=` for exact match: `domain = 'domain-1.com'`
    - `IN` for multiple values: `status IN ('NEED_TO_VALIDATE', 'VALID')`
    - `contains` for domain substring search: `domain contains '3'`
    - `AND` for combining conditions: `status = 'INVALID' AND domain contains '3'`

    Available fields for filtering:
    - `domain` - domain name
    - `status` - domain validation status

    Must be 1-1000 characters long.
    """
    def __init__(
        self,
        *,
        federation_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["federation_id", b"federation_id", "filter", b"filter", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListFederationDomainsRequest = ListFederationDomainsRequest

@typing.final
class ListFederationDomainsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DOMAINS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListFederationDomainsRequest.page_size], use the [next_page_token] as the value
    for the [ListFederationDomainsRequest.page_token] query parameter in the next list request.
    Each subsequent list request will have its own [next_page_token] to continue paging through the results.
    """
    @property
    def domains(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.organizationmanager.v1.saml.federation_pb2.Domain]:
        """List of domains for the specified federation."""

    def __init__(
        self,
        *,
        domains: collections.abc.Iterable[yandex.cloud.organizationmanager.v1.saml.federation_pb2.Domain] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["domains", b"domains", "next_page_token", b"next_page_token"]) -> None: ...

global___ListFederationDomainsResponse = ListFederationDomainsResponse

@typing.final
class AddFederationDomainRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEDERATION_ID_FIELD_NUMBER: builtins.int
    DOMAIN_FIELD_NUMBER: builtins.int
    federation_id: builtins.str
    """ID of the federation to add a domain to.
    To get the federation ID, make a [FederationService.List] request.
    """
    domain: builtins.str
    """Domain name to add to the federation.
    Must be a valid domain name (1-253 characters).
    """
    def __init__(
        self,
        *,
        federation_id: builtins.str = ...,
        domain: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["domain", b"domain", "federation_id", b"federation_id"]) -> None: ...

global___AddFederationDomainRequest = AddFederationDomainRequest

@typing.final
class AddFederationDomainMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEDERATION_ID_FIELD_NUMBER: builtins.int
    DOMAIN_FIELD_NUMBER: builtins.int
    federation_id: builtins.str
    """ID of the federation that the domain is being added to."""
    domain: builtins.str
    """Domain name that is being added to the federation."""
    def __init__(
        self,
        *,
        federation_id: builtins.str = ...,
        domain: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["domain", b"domain", "federation_id", b"federation_id"]) -> None: ...

global___AddFederationDomainMetadata = AddFederationDomainMetadata

@typing.final
class ValidateFederationDomainRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEDERATION_ID_FIELD_NUMBER: builtins.int
    DOMAIN_FIELD_NUMBER: builtins.int
    federation_id: builtins.str
    """ID of the federation to validate a domain for.
    To get the federation ID, make a [FederationService.List] request.
    """
    domain: builtins.str
    """Domain name to validate for the federation.
    Must be a valid domain name (1-253 characters).
    """
    def __init__(
        self,
        *,
        federation_id: builtins.str = ...,
        domain: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["domain", b"domain", "federation_id", b"federation_id"]) -> None: ...

global___ValidateFederationDomainRequest = ValidateFederationDomainRequest

@typing.final
class ValidateFederationDomainMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEDERATION_ID_FIELD_NUMBER: builtins.int
    DOMAIN_FIELD_NUMBER: builtins.int
    federation_id: builtins.str
    """ID of the federation that the domain validation is being performed for."""
    domain: builtins.str
    """Domain name that is being validated for the federation."""
    def __init__(
        self,
        *,
        federation_id: builtins.str = ...,
        domain: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["domain", b"domain", "federation_id", b"federation_id"]) -> None: ...

global___ValidateFederationDomainMetadata = ValidateFederationDomainMetadata

@typing.final
class DeleteFederationDomainRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEDERATION_ID_FIELD_NUMBER: builtins.int
    DOMAIN_FIELD_NUMBER: builtins.int
    federation_id: builtins.str
    """ID of the federation to delete a domain from.
    To get the federation ID, make a [FederationService.List] request.
    """
    domain: builtins.str
    """Domain name to delete from the federation.
    Must be a valid domain name (1-253 characters).
    """
    def __init__(
        self,
        *,
        federation_id: builtins.str = ...,
        domain: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["domain", b"domain", "federation_id", b"federation_id"]) -> None: ...

global___DeleteFederationDomainRequest = DeleteFederationDomainRequest

@typing.final
class DeleteFederationDomainMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEDERATION_ID_FIELD_NUMBER: builtins.int
    DOMAIN_FIELD_NUMBER: builtins.int
    federation_id: builtins.str
    """ID of the federation that the domain is being deleted from."""
    domain: builtins.str
    """Domain name that is being deleted from the federation."""
    def __init__(
        self,
        *,
        federation_id: builtins.str = ...,
        domain: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["domain", b"domain", "federation_id", b"federation_id"]) -> None: ...

global___DeleteFederationDomainMetadata = DeleteFederationDomainMetadata
