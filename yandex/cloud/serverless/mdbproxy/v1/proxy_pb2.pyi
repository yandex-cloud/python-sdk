"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Proxy(google.protobuf.message.Message):
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

    ID_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    TARGET_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the proxy."""
    folder_id: builtins.str
    """ID of the folder that the proxy belongs to."""
    name: builtins.str
    """Name of the proxy."""
    description: builtins.str
    """Description of the proxy."""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp for the proxy."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `key:value` pairs."""

    @property
    def target(self) -> global___Target:
        """MDB specific settings."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        folder_id: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        target: global___Target | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at", "target", b"target"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["created_at", b"created_at", "description", b"description", "folder_id", b"folder_id", "id", b"id", "labels", b"labels", "name", b"name", "target", b"target"]) -> None: ...

global___Proxy = Proxy

@typing.final
class Target(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class PostgreSQL(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        CLUSTER_ID_FIELD_NUMBER: builtins.int
        USER_FIELD_NUMBER: builtins.int
        PASSWORD_FIELD_NUMBER: builtins.int
        DB_FIELD_NUMBER: builtins.int
        ENDPOINT_FIELD_NUMBER: builtins.int
        cluster_id: builtins.str
        """Cluster identifier for postgresql."""
        user: builtins.str
        """PostgreSQL user."""
        password: builtins.str
        """PostgreSQL password, input only field."""
        db: builtins.str
        """PostgreSQL database name."""
        endpoint: builtins.str
        """PostgreSQL proxy-host for connection, output only field."""
        def __init__(
            self,
            *,
            cluster_id: builtins.str = ...,
            user: builtins.str = ...,
            password: builtins.str = ...,
            db: builtins.str = ...,
            endpoint: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "db", b"db", "endpoint", b"endpoint", "password", b"password", "user", b"user"]) -> None: ...

    @typing.final
    class ClickHouse(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        CLUSTER_ID_FIELD_NUMBER: builtins.int
        USER_FIELD_NUMBER: builtins.int
        PASSWORD_FIELD_NUMBER: builtins.int
        DB_FIELD_NUMBER: builtins.int
        ENDPOINT_FIELD_NUMBER: builtins.int
        cluster_id: builtins.str
        """Cluster identifier for clickhouse."""
        user: builtins.str
        """Clickhouse user."""
        password: builtins.str
        """Clickhouse password, input only field."""
        db: builtins.str
        """Clickhouse database name."""
        endpoint: builtins.str
        """Clickhouse proxy-host for connection, output only field."""
        def __init__(
            self,
            *,
            cluster_id: builtins.str = ...,
            user: builtins.str = ...,
            password: builtins.str = ...,
            db: builtins.str = ...,
            endpoint: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "db", b"db", "endpoint", b"endpoint", "password", b"password", "user", b"user"]) -> None: ...

    CLICKHOUSE_FIELD_NUMBER: builtins.int
    POSTGRESQL_FIELD_NUMBER: builtins.int
    @property
    def clickhouse(self) -> global___Target.ClickHouse:
        """Clickhouse settings for proxy."""

    @property
    def postgresql(self) -> global___Target.PostgreSQL:
        """PostgreSQL settings for proxy."""

    def __init__(
        self,
        *,
        clickhouse: global___Target.ClickHouse | None = ...,
        postgresql: global___Target.PostgreSQL | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["clickhouse", b"clickhouse", "mdb", b"mdb", "postgresql", b"postgresql"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["clickhouse", b"clickhouse", "mdb", b"mdb", "postgresql", b"postgresql"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["mdb", b"mdb"]) -> typing.Literal["clickhouse", "postgresql"] | None: ...

global___Target = Target
