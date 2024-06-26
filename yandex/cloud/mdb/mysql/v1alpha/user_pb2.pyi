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
    """A MySQL user. For more information, see the [documentation](/docs/managed-mysql/concepts)."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    PERMISSIONS_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the MySQL user."""
    cluster_id: builtins.str
    """ID of the MySQL cluster the user belongs to."""
    @property
    def permissions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Permission]:
        """Set of permissions granted to the user."""

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
class Permission(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Privilege:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _PrivilegeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Permission._Privilege.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        PRIVILEGE_UNSPECIFIED: Permission._Privilege.ValueType  # 0
        ALL_PRIVILEGES: Permission._Privilege.ValueType  # 1
        """All privileges that can be made available to the user."""
        ALTER: Permission._Privilege.ValueType  # 2
        """Altering tables."""
        ALTER_ROUTINE: Permission._Privilege.ValueType  # 3
        """Altering stored routines (stored procedures and functions)."""
        CREATE: Permission._Privilege.ValueType  # 4
        """Creating tables or indexes."""
        CREATE_ROUTINE: Permission._Privilege.ValueType  # 5
        """Creating stored routines."""
        CREATE_TEMPORARY_TABLES: Permission._Privilege.ValueType  # 6
        """Creating temporary tables."""
        CREATE_VIEW: Permission._Privilege.ValueType  # 7
        """Creating views."""
        DELETE: Permission._Privilege.ValueType  # 8
        """Deleting tables."""
        DROP: Permission._Privilege.ValueType  # 9
        """Removing tables or views."""
        EVENT: Permission._Privilege.ValueType  # 10
        """Creating, altering, dropping, or displaying events for the Event Scheduler."""
        EXECUTE: Permission._Privilege.ValueType  # 11
        """Executing stored routines."""
        INDEX: Permission._Privilege.ValueType  # 12
        """Creating and removing indexes."""
        INSERT: Permission._Privilege.ValueType  # 13
        """Inserting rows into the database."""
        LOCK_TABLES: Permission._Privilege.ValueType  # 14
        """Using LOCK TABLES statement for tables available with SELECT privilege."""
        SELECT: Permission._Privilege.ValueType  # 15
        """Selecting rows from tables.

        Some SELECT statements can be allowed without the SELECT privilege. All statements that read column values require the SELECT privilege. See details in [MySQL documentation](https://dev.mysql.com/doc/refman/5.7/en/privileges-provided.html#priv_select).
        """
        SHOW_VIEW: Permission._Privilege.ValueType  # 16
        """Using the SHOW CREATE VIEW statement. Also needed for views used with EXPLAIN."""
        TRIGGER: Permission._Privilege.ValueType  # 17
        """Creating, removing, executing, or displaying triggers for a table."""
        UPDATE: Permission._Privilege.ValueType  # 18
        """Updating rows in the database."""

    class Privilege(_Privilege, metaclass=_PrivilegeEnumTypeWrapper): ...
    PRIVILEGE_UNSPECIFIED: Permission.Privilege.ValueType  # 0
    ALL_PRIVILEGES: Permission.Privilege.ValueType  # 1
    """All privileges that can be made available to the user."""
    ALTER: Permission.Privilege.ValueType  # 2
    """Altering tables."""
    ALTER_ROUTINE: Permission.Privilege.ValueType  # 3
    """Altering stored routines (stored procedures and functions)."""
    CREATE: Permission.Privilege.ValueType  # 4
    """Creating tables or indexes."""
    CREATE_ROUTINE: Permission.Privilege.ValueType  # 5
    """Creating stored routines."""
    CREATE_TEMPORARY_TABLES: Permission.Privilege.ValueType  # 6
    """Creating temporary tables."""
    CREATE_VIEW: Permission.Privilege.ValueType  # 7
    """Creating views."""
    DELETE: Permission.Privilege.ValueType  # 8
    """Deleting tables."""
    DROP: Permission.Privilege.ValueType  # 9
    """Removing tables or views."""
    EVENT: Permission.Privilege.ValueType  # 10
    """Creating, altering, dropping, or displaying events for the Event Scheduler."""
    EXECUTE: Permission.Privilege.ValueType  # 11
    """Executing stored routines."""
    INDEX: Permission.Privilege.ValueType  # 12
    """Creating and removing indexes."""
    INSERT: Permission.Privilege.ValueType  # 13
    """Inserting rows into the database."""
    LOCK_TABLES: Permission.Privilege.ValueType  # 14
    """Using LOCK TABLES statement for tables available with SELECT privilege."""
    SELECT: Permission.Privilege.ValueType  # 15
    """Selecting rows from tables.

    Some SELECT statements can be allowed without the SELECT privilege. All statements that read column values require the SELECT privilege. See details in [MySQL documentation](https://dev.mysql.com/doc/refman/5.7/en/privileges-provided.html#priv_select).
    """
    SHOW_VIEW: Permission.Privilege.ValueType  # 16
    """Using the SHOW CREATE VIEW statement. Also needed for views used with EXPLAIN."""
    TRIGGER: Permission.Privilege.ValueType  # 17
    """Creating, removing, executing, or displaying triggers for a table."""
    UPDATE: Permission.Privilege.ValueType  # 18
    """Updating rows in the database."""

    DATABASE_NAME_FIELD_NUMBER: builtins.int
    ROLES_FIELD_NUMBER: builtins.int
    database_name: builtins.str
    """Name of the database that the permission grants access to."""
    @property
    def roles(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[global___Permission.Privilege.ValueType]:
        """Roles granted to the user within the database."""

    def __init__(
        self,
        *,
        database_name: builtins.str = ...,
        roles: collections.abc.Iterable[global___Permission.Privilege.ValueType] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["database_name", b"database_name", "roles", b"roles"]) -> None: ...

global___Permission = Permission

@typing.final
class UserSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    PERMISSIONS_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the MySQL user."""
    password: builtins.str
    """Password of the MySQL user."""
    @property
    def permissions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Permission]:
        """Set of permissions to grant to the user."""

    def __init__(
        self,
        *,
        name: builtins.str = ...,
        password: builtins.str = ...,
        permissions: collections.abc.Iterable[global___Permission] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["name", b"name", "password", b"password", "permissions", b"permissions"]) -> None: ...

global___UserSpec = UserSpec
