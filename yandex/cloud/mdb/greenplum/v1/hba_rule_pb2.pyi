"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
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
class HBARule(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _ConnectionType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _ConnectionTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[HBARule._ConnectionType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        CONNECTION_TYPE_UNSPECIFIED: HBARule._ConnectionType.ValueType  # 0
        HOST: HBARule._ConnectionType.ValueType  # 1
        """Matches connection attempts made using TCP/IP."""
        HOSTSSL: HBARule._ConnectionType.ValueType  # 2
        """Matches connection attempts made using TCP/IP, but only when the connection is made with SSL encryption."""
        HOSTNOSSL: HBARule._ConnectionType.ValueType  # 3
        """Matches connection attempts made over TCP/IP that do not use SSL."""

    class ConnectionType(_ConnectionType, metaclass=_ConnectionTypeEnumTypeWrapper): ...
    CONNECTION_TYPE_UNSPECIFIED: HBARule.ConnectionType.ValueType  # 0
    HOST: HBARule.ConnectionType.ValueType  # 1
    """Matches connection attempts made using TCP/IP."""
    HOSTSSL: HBARule.ConnectionType.ValueType  # 2
    """Matches connection attempts made using TCP/IP, but only when the connection is made with SSL encryption."""
    HOSTNOSSL: HBARule.ConnectionType.ValueType  # 3
    """Matches connection attempts made over TCP/IP that do not use SSL."""

    class _AuthMethod:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _AuthMethodEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[HBARule._AuthMethod.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        AUTH_METHOD_UNSPECIFIED: HBARule._AuthMethod.ValueType  # 0
        MD5: HBARule._AuthMethod.ValueType  # 1
        """Perform SCRAM-SHA-256 or MD5 authentication to verify the user's password."""
        LDAP: HBARule._AuthMethod.ValueType  # 2
        """Perform LDAP authentication, if MDB_GREENPLUM_LDAP flag is set"""
        REJECT: HBARule._AuthMethod.ValueType  # 3
        """Disable authentication"""
        IAM: HBARule._AuthMethod.ValueType  # 4
        """Perform authentication with IAM token"""

    class AuthMethod(_AuthMethod, metaclass=_AuthMethodEnumTypeWrapper): ...
    AUTH_METHOD_UNSPECIFIED: HBARule.AuthMethod.ValueType  # 0
    MD5: HBARule.AuthMethod.ValueType  # 1
    """Perform SCRAM-SHA-256 or MD5 authentication to verify the user's password."""
    LDAP: HBARule.AuthMethod.ValueType  # 2
    """Perform LDAP authentication, if MDB_GREENPLUM_LDAP flag is set"""
    REJECT: HBARule.AuthMethod.ValueType  # 3
    """Disable authentication"""
    IAM: HBARule.AuthMethod.ValueType  # 4
    """Perform authentication with IAM token"""

    PRIORITY_FIELD_NUMBER: builtins.int
    CONNECTION_TYPE_FIELD_NUMBER: builtins.int
    DATABASE_FIELD_NUMBER: builtins.int
    USER_FIELD_NUMBER: builtins.int
    ADDRESS_FIELD_NUMBER: builtins.int
    AUTH_METHOD_FIELD_NUMBER: builtins.int
    priority: builtins.int
    """Priority of the Greenplum cluster rule."""
    connection_type: global___HBARule.ConnectionType.ValueType
    database: builtins.str
    """Specifies which database names this record matches."""
    user: builtins.str
    """Specifies which database role names this user matches."""
    address: builtins.str
    """Specifies the client machine addresses that this record matches."""
    auth_method: global___HBARule.AuthMethod.ValueType
    """Specifies the authentication method to use when a connection matches this record.
    https://gpdb.docs.pivotal.io/6-6/security-guide/topics/Authenticate.html
    """
    def __init__(
        self,
        *,
        priority: builtins.int = ...,
        connection_type: global___HBARule.ConnectionType.ValueType = ...,
        database: builtins.str = ...,
        user: builtins.str = ...,
        address: builtins.str = ...,
        auth_method: global___HBARule.AuthMethod.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["address", b"address", "auth_method", b"auth_method", "connection_type", b"connection_type", "database", b"database", "priority", b"priority", "user", b"user"]) -> None: ...

global___HBARule = HBARule
