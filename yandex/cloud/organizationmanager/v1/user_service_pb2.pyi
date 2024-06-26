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
import yandex.cloud.oauth.claims_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class ListMembersRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    organization_id: builtins.str
    """ID of the Organization resource to list members for."""
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size], the service returns a [ListMembersResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Acceptable values are 0 to 1000, inclusive. Default value: 100.
    """
    page_token: builtins.str
    """Page token. Set [page_token]
    to the [ListMembersResponse.next_page_token]
    returned by a previous list request to get the next page of results.
    """
    def __init__(
        self,
        *,
        organization_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["organization_id", b"organization_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListMembersRequest = ListMembersRequest

@typing.final
class ListMembersResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class OrganizationUser(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        SUBJECT_CLAIMS_FIELD_NUMBER: builtins.int
        @property
        def subject_claims(self) -> yandex.cloud.oauth.claims_pb2.SubjectClaims:
            """OpenID standard claims with additional Cloud Organization claims."""

        def __init__(
            self,
            *,
            subject_claims: yandex.cloud.oauth.claims_pb2.SubjectClaims | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["subject_claims", b"subject_claims"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["subject_claims", b"subject_claims"]) -> None: ...

    USERS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListMembersRequest.page_size], use the [next_page_token] as the value
    for the [ListMembersRequest.page_token] query parameter in the next list request.
    Each subsequent list request will have its own [next_page_token] to continue paging through the results.
    """
    @property
    def users(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ListMembersResponse.OrganizationUser]:
        """List of users for the specified organization."""

    def __init__(
        self,
        *,
        users: collections.abc.Iterable[global___ListMembersResponse.OrganizationUser] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "users", b"users"]) -> None: ...

global___ListMembersResponse = ListMembersResponse

@typing.final
class DeleteMembershipRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    SUBJECT_ID_FIELD_NUMBER: builtins.int
    organization_id: builtins.str
    """ID of the organization to delete membership."""
    subject_id: builtins.str
    """ID of the subject that is being deleted from organization.
    By default equals to authenticated subject.
    """
    def __init__(
        self,
        *,
        organization_id: builtins.str = ...,
        subject_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["organization_id", b"organization_id", "subject_id", b"subject_id"]) -> None: ...

global___DeleteMembershipRequest = DeleteMembershipRequest

@typing.final
class DeleteMembershipMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    SUBJECT_ID_FIELD_NUMBER: builtins.int
    organization_id: builtins.str
    """ID of the organization to delete membership."""
    subject_id: builtins.str
    """ID of the subject that is being deleted from organization."""
    def __init__(
        self,
        *,
        organization_id: builtins.str = ...,
        subject_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["organization_id", b"organization_id", "subject_id", b"subject_id"]) -> None: ...

global___DeleteMembershipMetadata = DeleteMembershipMetadata

@typing.final
class DeleteMembershipResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    SUBJECT_ID_FIELD_NUMBER: builtins.int
    organization_id: builtins.str
    """ID of the organization to delete membership."""
    subject_id: builtins.str
    """ID of the subject that is being deleted from organization."""
    def __init__(
        self,
        *,
        organization_id: builtins.str = ...,
        subject_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["organization_id", b"organization_id", "subject_id", b"subject_id"]) -> None: ...

global___DeleteMembershipResponse = DeleteMembershipResponse
