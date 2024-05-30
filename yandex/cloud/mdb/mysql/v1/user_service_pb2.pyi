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
import yandex.cloud.mdb.mysql.v1.user_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetUserRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    USER_NAME_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the cluster the user belongs to.

    To get this ID, make a [ClusterService.List] request.
    """
    user_name: builtins.str
    """Name of the user to return information about.

    To get this name, make a [UserService.List] request.
    """
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        user_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "user_name", b"user_name"]) -> None: ...

global___GetUserRequest = GetUserRequest

@typing.final
class ListUsersRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the cluster to list the users in.

    To get this ID, make a [ClusterService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return.

    If the number of available results is larger than [page_size], the API returns a [ListUsersResponse.next_page_token] that can be used to get the next page of results in the subsequent [UserService.List] requests.
    """
    page_token: builtins.str
    """Page token that can be used to iterate through multiple pages of results.

    To get the next page of results, set [page_token] to the [ListUsersResponse.next_page_token] returned by the previous [UserService.List] request.
    """
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListUsersRequest = ListUsersRequest

@typing.final
class ListUsersResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USERS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """The token that can be used to get the next page of results.

    If the number of results is larger than [ListUsersRequest.page_size], use the [next_page_token] as the value for the [ListUsersRequest.page_token] in the subsequent [UserService.List] request to iterate through multiple pages of results.

    Each of the subsequent [UserService.List] requests should use the [next_page_token] value returned by the previous request to continue paging through the results.
    """
    @property
    def users(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.mdb.mysql.v1.user_pb2.User]:
        """List of users."""

    def __init__(
        self,
        *,
        users: collections.abc.Iterable[yandex.cloud.mdb.mysql.v1.user_pb2.User] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "users", b"users"]) -> None: ...

global___ListUsersResponse = ListUsersResponse

@typing.final
class CreateUserRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    USER_SPEC_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the cluster to create the user in.

    To get this ID, make a [ClusterService.List] request.
    """
    @property
    def user_spec(self) -> yandex.cloud.mdb.mysql.v1.user_pb2.UserSpec:
        """Configuration of the user."""

    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        user_spec: yandex.cloud.mdb.mysql.v1.user_pb2.UserSpec | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["user_spec", b"user_spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "user_spec", b"user_spec"]) -> None: ...

global___CreateUserRequest = CreateUserRequest

@typing.final
class CreateUserMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    USER_NAME_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the cluster the user is being created in."""
    user_name: builtins.str
    """Name of the user that is being created."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        user_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "user_name", b"user_name"]) -> None: ...

global___CreateUserMetadata = CreateUserMetadata

@typing.final
class UpdateUserRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    USER_NAME_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    PERMISSIONS_FIELD_NUMBER: builtins.int
    GLOBAL_PERMISSIONS_FIELD_NUMBER: builtins.int
    CONNECTION_LIMITS_FIELD_NUMBER: builtins.int
    AUTHENTICATION_PLUGIN_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the cluster to update the user in.

    To get this ID, make a [ClusterService.List] request.
    """
    user_name: builtins.str
    """Name of the user to update.

    To get this name, make a [UserService.List] request.
    """
    password: builtins.str
    """New password for the user."""
    authentication_plugin: yandex.cloud.mdb.mysql.v1.user_pb2.AuthPlugin.ValueType
    """New user authentication plugin."""
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which settings of the user should be updated."""

    @property
    def permissions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.mdb.mysql.v1.user_pb2.Permission]:
        """A new set of permissions that should be granted to the user."""

    @property
    def global_permissions(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[yandex.cloud.mdb.mysql.v1.user_pb2.GlobalPermission.ValueType]:
        """New set of global permissions to grant to the user."""

    @property
    def connection_limits(self) -> yandex.cloud.mdb.mysql.v1.user_pb2.ConnectionLimits:
        """Set of changed user connection limits."""

    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        user_name: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        password: builtins.str = ...,
        permissions: collections.abc.Iterable[yandex.cloud.mdb.mysql.v1.user_pb2.Permission] | None = ...,
        global_permissions: collections.abc.Iterable[yandex.cloud.mdb.mysql.v1.user_pb2.GlobalPermission.ValueType] | None = ...,
        connection_limits: yandex.cloud.mdb.mysql.v1.user_pb2.ConnectionLimits | None = ...,
        authentication_plugin: yandex.cloud.mdb.mysql.v1.user_pb2.AuthPlugin.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["connection_limits", b"connection_limits", "update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["authentication_plugin", b"authentication_plugin", "cluster_id", b"cluster_id", "connection_limits", b"connection_limits", "global_permissions", b"global_permissions", "password", b"password", "permissions", b"permissions", "update_mask", b"update_mask", "user_name", b"user_name"]) -> None: ...

global___UpdateUserRequest = UpdateUserRequest

@typing.final
class UpdateUserMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    USER_NAME_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the cluster the user is being updated in."""
    user_name: builtins.str
    """Name of the user that is being updated."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        user_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "user_name", b"user_name"]) -> None: ...

global___UpdateUserMetadata = UpdateUserMetadata

@typing.final
class DeleteUserRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    USER_NAME_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the cluster to delete the user from.

    To get this ID, make a [ClusterService.List] request.
    """
    user_name: builtins.str
    """Name of the user to delete.

    To get this name, make a [UserService.List] request.
    """
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        user_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "user_name", b"user_name"]) -> None: ...

global___DeleteUserRequest = DeleteUserRequest

@typing.final
class DeleteUserMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    USER_NAME_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the cluster the user is being deleted from."""
    user_name: builtins.str
    """Name of the user that is being deleted."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        user_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "user_name", b"user_name"]) -> None: ...

global___DeleteUserMetadata = DeleteUserMetadata

@typing.final
class GrantUserPermissionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    USER_NAME_FIELD_NUMBER: builtins.int
    PERMISSION_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the cluster to grant permission to the user in.

    To get this ID, make a [ClusterService.List] request.
    """
    user_name: builtins.str
    """Name of the user to grant permission to.

    To get this name, make a [UserService.List] request.
    """
    @property
    def permission(self) -> yandex.cloud.mdb.mysql.v1.user_pb2.Permission:
        """Permission that should be granted to the specified user."""

    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        user_name: builtins.str = ...,
        permission: yandex.cloud.mdb.mysql.v1.user_pb2.Permission | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["permission", b"permission"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "permission", b"permission", "user_name", b"user_name"]) -> None: ...

global___GrantUserPermissionRequest = GrantUserPermissionRequest

@typing.final
class GrantUserPermissionMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    USER_NAME_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the cluster the user is being granted a permission in."""
    user_name: builtins.str
    """Name of the user that is being granted a permission."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        user_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "user_name", b"user_name"]) -> None: ...

global___GrantUserPermissionMetadata = GrantUserPermissionMetadata

@typing.final
class RevokeUserPermissionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    USER_NAME_FIELD_NUMBER: builtins.int
    PERMISSION_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the cluster to revoke permission from the user in.

    To get this ID, make a [ClusterService.List] request.
    """
    user_name: builtins.str
    """Name of the user to revoke permission from.

    To get this name, make a [UserService.List] request.
    """
    @property
    def permission(self) -> yandex.cloud.mdb.mysql.v1.user_pb2.Permission:
        """Permission that should be revoked from the user."""

    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        user_name: builtins.str = ...,
        permission: yandex.cloud.mdb.mysql.v1.user_pb2.Permission | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["permission", b"permission"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "permission", b"permission", "user_name", b"user_name"]) -> None: ...

global___RevokeUserPermissionRequest = RevokeUserPermissionRequest

@typing.final
class RevokeUserPermissionMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    USER_NAME_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the cluster the user is being revoked a permission in."""
    user_name: builtins.str
    """Name of the user whose permission is being revoked."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        user_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "user_name", b"user_name"]) -> None: ...

global___RevokeUserPermissionMetadata = RevokeUserPermissionMetadata
