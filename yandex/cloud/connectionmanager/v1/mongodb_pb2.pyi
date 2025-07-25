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
import yandex.cloud.connectionmanager.v1.common_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class MongoDBAuth(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_PASSWORD_FIELD_NUMBER: builtins.int
    @property
    def user_password(self) -> yandex.cloud.connectionmanager.v1.common_pb2.UserPasswordAuth: ...
    def __init__(
        self,
        *,
        user_password: yandex.cloud.connectionmanager.v1.common_pb2.UserPasswordAuth | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["security", b"security", "user_password", b"user_password"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["security", b"security", "user_password", b"user_password"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["security", b"security"]) -> typing.Literal["user_password"] | None: ...

global___MongoDBAuth = MongoDBAuth

@typing.final
class MongoDBCluster(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Host(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        class _Type:
            ValueType = typing.NewType("ValueType", builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[MongoDBCluster.Host._Type.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            TYPE_UNSPECIFIED: MongoDBCluster.Host._Type.ValueType  # 0
            MONGOD: MongoDBCluster.Host._Type.ValueType  # 1
            MONGOS: MongoDBCluster.Host._Type.ValueType  # 2
            MONGOINFRA: MongoDBCluster.Host._Type.ValueType  # 3

        class Type(_Type, metaclass=_TypeEnumTypeWrapper): ...
        TYPE_UNSPECIFIED: MongoDBCluster.Host.Type.ValueType  # 0
        MONGOD: MongoDBCluster.Host.Type.ValueType  # 1
        MONGOS: MongoDBCluster.Host.Type.ValueType  # 2
        MONGOINFRA: MongoDBCluster.Host.Type.ValueType  # 3

        class _Role:
            ValueType = typing.NewType("ValueType", builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _RoleEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[MongoDBCluster.Host._Role.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            ROLE_UNSPECIFIED: MongoDBCluster.Host._Role.ValueType  # 0
            PRIMARY: MongoDBCluster.Host._Role.ValueType  # 1
            SECONDARY: MongoDBCluster.Host._Role.ValueType  # 2

        class Role(_Role, metaclass=_RoleEnumTypeWrapper): ...
        ROLE_UNSPECIFIED: MongoDBCluster.Host.Role.ValueType  # 0
        PRIMARY: MongoDBCluster.Host.Role.ValueType  # 1
        SECONDARY: MongoDBCluster.Host.Role.ValueType  # 2

        class _Health:
            ValueType = typing.NewType("ValueType", builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _HealthEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[MongoDBCluster.Host._Health.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            HEALTH_UNSPECIFIED: MongoDBCluster.Host._Health.ValueType  # 0
            ALIVE: MongoDBCluster.Host._Health.ValueType  # 1
            DEAD: MongoDBCluster.Host._Health.ValueType  # 2
            DEGRADED: MongoDBCluster.Host._Health.ValueType  # 3

        class Health(_Health, metaclass=_HealthEnumTypeWrapper): ...
        HEALTH_UNSPECIFIED: MongoDBCluster.Host.Health.ValueType  # 0
        ALIVE: MongoDBCluster.Host.Health.ValueType  # 1
        DEAD: MongoDBCluster.Host.Health.ValueType  # 2
        DEGRADED: MongoDBCluster.Host.Health.ValueType  # 3

        HOST_FIELD_NUMBER: builtins.int
        PORT_FIELD_NUMBER: builtins.int
        ROLE_FIELD_NUMBER: builtins.int
        HEALTH_FIELD_NUMBER: builtins.int
        TYPE_FIELD_NUMBER: builtins.int
        host: builtins.str
        port: builtins.int
        role: global___MongoDBCluster.Host.Role.ValueType
        health: global___MongoDBCluster.Host.Health.ValueType
        type: global___MongoDBCluster.Host.Type.ValueType
        def __init__(
            self,
            *,
            host: builtins.str = ...,
            port: builtins.int = ...,
            role: global___MongoDBCluster.Host.Role.ValueType = ...,
            health: global___MongoDBCluster.Host.Health.ValueType = ...,
            type: global___MongoDBCluster.Host.Type.ValueType = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["health", b"health", "host", b"host", "port", b"port", "role", b"role", "type", b"type"]) -> None: ...

    HOSTS_FIELD_NUMBER: builtins.int
    TLS_PARAMS_FIELD_NUMBER: builtins.int
    @property
    def hosts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MongoDBCluster.Host]: ...
    @property
    def tls_params(self) -> yandex.cloud.connectionmanager.v1.common_pb2.TLSParams: ...
    def __init__(
        self,
        *,
        hosts: collections.abc.Iterable[global___MongoDBCluster.Host] | None = ...,
        tls_params: yandex.cloud.connectionmanager.v1.common_pb2.TLSParams | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["tls_params", b"tls_params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["hosts", b"hosts", "tls_params", b"tls_params"]) -> None: ...

global___MongoDBCluster = MongoDBCluster

@typing.final
class MongoDBConnection(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_FIELD_NUMBER: builtins.int
    MANAGED_CLUSTER_ID_FIELD_NUMBER: builtins.int
    AUTH_FIELD_NUMBER: builtins.int
    DATABASES_FIELD_NUMBER: builtins.int
    managed_cluster_id: builtins.str
    """When creating/updating Connection, the field "managed_cluster_id" is
    mutually exclusive with "cluster".
    """
    @property
    def cluster(self) -> global___MongoDBCluster:
        """When creating/updating Connection, the field "cluster" is mutually
        exclusive with "managed_cluster_id".
        """

    @property
    def auth(self) -> global___MongoDBAuth: ...
    @property
    def databases(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        cluster: global___MongoDBCluster | None = ...,
        managed_cluster_id: builtins.str = ...,
        auth: global___MongoDBAuth | None = ...,
        databases: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["auth", b"auth", "cluster", b"cluster"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["auth", b"auth", "cluster", b"cluster", "databases", b"databases", "managed_cluster_id", b"managed_cluster_id"]) -> None: ...

global___MongoDBConnection = MongoDBConnection
