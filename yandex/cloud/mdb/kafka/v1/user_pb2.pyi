"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class User(google.protobuf.message.Message):
    """A Kafka user.
    For more information, see the [Operations -> Accounts](/docs/managed-kafka/operations/cluster-accounts) section of the documentation.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    PERMISSIONS_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the Kafka user."""
    cluster_id: builtins.str
    """ID of the Apache Kafka® cluster the user belongs to.

    To get the Apache Kafka® cluster ID, make a [ClusterService.List] request.
    """
    @property
    def permissions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Permission]:
        """Set of permissions granted to this user."""

    def __init__(
        self,
        *,
        name: builtins.str = ...,
        cluster_id: builtins.str = ...,
        permissions: collections.abc.Iterable[global___Permission] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "name", b"name", "permissions", b"permissions"]) -> None: ...

global___User = User

@typing.final
class UserSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    PERMISSIONS_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the Kafka user."""
    password: builtins.str
    """Password of the Kafka user."""
    @property
    def permissions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Permission]:
        """Set of permissions granted to the user."""

    def __init__(
        self,
        *,
        name: builtins.str = ...,
        password: builtins.str = ...,
        permissions: collections.abc.Iterable[global___Permission] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["name", b"name", "password", b"password", "permissions", b"permissions"]) -> None: ...

global___UserSpec = UserSpec

@typing.final
class Permission(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _AccessRole:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _AccessRoleEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Permission._AccessRole.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        ACCESS_ROLE_UNSPECIFIED: Permission._AccessRole.ValueType  # 0
        ACCESS_ROLE_PRODUCER: Permission._AccessRole.ValueType  # 1
        """Producer role for the user."""
        ACCESS_ROLE_CONSUMER: Permission._AccessRole.ValueType  # 2
        """Consumer role for the user."""
        ACCESS_ROLE_ADMIN: Permission._AccessRole.ValueType  # 3
        """Admin role for the user."""
        ACCESS_ROLE_TOPIC_ADMIN: Permission._AccessRole.ValueType  # 4
        """Admin permissions on topics role for the user."""
        ACCESS_ROLE_TOPIC_PRODUCER: Permission._AccessRole.ValueType  # 5
        ACCESS_ROLE_TOPIC_CONSUMER: Permission._AccessRole.ValueType  # 6
        ACCESS_ROLE_SCHEMA_READER: Permission._AccessRole.ValueType  # 7
        ACCESS_ROLE_SCHEMA_WRITER: Permission._AccessRole.ValueType  # 8

    class AccessRole(_AccessRole, metaclass=_AccessRoleEnumTypeWrapper): ...
    ACCESS_ROLE_UNSPECIFIED: Permission.AccessRole.ValueType  # 0
    ACCESS_ROLE_PRODUCER: Permission.AccessRole.ValueType  # 1
    """Producer role for the user."""
    ACCESS_ROLE_CONSUMER: Permission.AccessRole.ValueType  # 2
    """Consumer role for the user."""
    ACCESS_ROLE_ADMIN: Permission.AccessRole.ValueType  # 3
    """Admin role for the user."""
    ACCESS_ROLE_TOPIC_ADMIN: Permission.AccessRole.ValueType  # 4
    """Admin permissions on topics role for the user."""
    ACCESS_ROLE_TOPIC_PRODUCER: Permission.AccessRole.ValueType  # 5
    ACCESS_ROLE_TOPIC_CONSUMER: Permission.AccessRole.ValueType  # 6
    ACCESS_ROLE_SCHEMA_READER: Permission.AccessRole.ValueType  # 7
    ACCESS_ROLE_SCHEMA_WRITER: Permission.AccessRole.ValueType  # 8

    TOPIC_NAME_FIELD_NUMBER: builtins.int
    ROLE_FIELD_NUMBER: builtins.int
    ALLOW_HOSTS_FIELD_NUMBER: builtins.int
    topic_name: builtins.str
    """Name or prefix-pattern with wildcard for the topic that the permission grants access to.
    With roles SCHEMA_READER and SCHEMA_WRITER: string that contains set of schema registry subjects, separated by ';'.

    To get the topic name, make a [TopicService.List] request.
    """
    role: global___Permission.AccessRole.ValueType
    """Access role type to grant to the user."""
    @property
    def allow_hosts(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Lists hosts allowed for this permission.
        Only ip-addresses allowed as value of single host.
        When not defined, access from any host is allowed.

        Bare in mind that the same host might appear in multiple permissions at the same time,
        hence removing individual permission doesn't automatically restricts access from the [allow_hosts] of the permission.
        If the same host(s) is listed for another permission of the same principal/topic, the host(s) remains allowed.
        """

    def __init__(
        self,
        *,
        topic_name: builtins.str = ...,
        role: global___Permission.AccessRole.ValueType = ...,
        allow_hosts: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["allow_hosts", b"allow_hosts", "role", b"role", "topic_name", b"topic_name"]) -> None: ...

global___Permission = Permission
