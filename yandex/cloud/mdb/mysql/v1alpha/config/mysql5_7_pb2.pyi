"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.wrappers_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class MysqlConfig5_7(google.protobuf.message.Message):
    """Options and structure of `MysqlConfig5_7` reflects MySQL 5.7 configuration file"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INNODB_BUFFER_POOL_SIZE_FIELD_NUMBER: builtins.int
    MAX_CONNECTIONS_FIELD_NUMBER: builtins.int
    LONG_QUERY_TIME_FIELD_NUMBER: builtins.int
    @property
    def innodb_buffer_pool_size(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """Size of the InnoDB buffer pool used for caching table and index data.

        For details, see [MySQL documentation for the parameter](https://dev.mysql.com/doc/refman/5.7/en/innodb-parameters.html#sysvar_innodb_buffer_pool_size).
        """

    @property
    def max_connections(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The maximum permitted number of simultaneous client connections.

        For details, see [MySQL documentation for the variable](https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_max_connections).
        """

    @property
    def long_query_time(self) -> google.protobuf.wrappers_pb2.DoubleValue:
        """Time that it takes to process a query before it is considered slow.

        For details, see [MySQL documentation for the variable](https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_long_query_time).
        """

    def __init__(
        self,
        *,
        innodb_buffer_pool_size: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        max_connections: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        long_query_time: google.protobuf.wrappers_pb2.DoubleValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["innodb_buffer_pool_size", b"innodb_buffer_pool_size", "long_query_time", b"long_query_time", "max_connections", b"max_connections"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["innodb_buffer_pool_size", b"innodb_buffer_pool_size", "long_query_time", b"long_query_time", "max_connections", b"max_connections"]) -> None: ...

global___MysqlConfig5_7 = MysqlConfig5_7

@typing.final
class MysqlConfigSet5_7(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EFFECTIVE_CONFIG_FIELD_NUMBER: builtins.int
    USER_CONFIG_FIELD_NUMBER: builtins.int
    DEFAULT_CONFIG_FIELD_NUMBER: builtins.int
    @property
    def effective_config(self) -> global___MysqlConfig5_7:
        """Effective settings for a MySQL 5.7 cluster (a combination of settings defined
        in [user_config] and [default_config]).
        """

    @property
    def user_config(self) -> global___MysqlConfig5_7:
        """User-defined settings for a MySQL 5.7 cluster."""

    @property
    def default_config(self) -> global___MysqlConfig5_7:
        """Default configuration for a MySQL 5.7 cluster."""

    def __init__(
        self,
        *,
        effective_config: global___MysqlConfig5_7 | None = ...,
        user_config: global___MysqlConfig5_7 | None = ...,
        default_config: global___MysqlConfig5_7 | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["default_config", b"default_config", "effective_config", b"effective_config", "user_config", b"user_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["default_config", b"default_config", "effective_config", b"effective_config", "user_config", b"user_config"]) -> None: ...

global___MysqlConfigSet5_7 = MysqlConfigSet5_7