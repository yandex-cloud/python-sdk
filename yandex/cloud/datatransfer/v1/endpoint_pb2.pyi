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
import yandex.cloud.datatransfer.v1.endpoint.clickhouse_pb2
import yandex.cloud.datatransfer.v1.endpoint.kafka_pb2
import yandex.cloud.datatransfer.v1.endpoint.metrika_pb2
import yandex.cloud.datatransfer.v1.endpoint.mongo_pb2
import yandex.cloud.datatransfer.v1.endpoint.mysql_pb2
import yandex.cloud.datatransfer.v1.endpoint.postgres_pb2
import yandex.cloud.datatransfer.v1.endpoint.ydb_pb2
import yandex.cloud.datatransfer.v1.endpoint.yds_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Endpoint(google.protobuf.message.Message):
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
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    SETTINGS_FIELD_NUMBER: builtins.int
    id: builtins.str
    folder_id: builtins.str
    name: builtins.str
    description: builtins.str
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    @property
    def settings(self) -> global___EndpointSettings: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        folder_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        settings: global___EndpointSettings | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["settings", b"settings"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "folder_id", b"folder_id", "id", b"id", "labels", b"labels", "name", b"name", "settings", b"settings"]) -> None: ...

global___Endpoint = Endpoint

@typing.final
class EndpointSettings(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MYSQL_SOURCE_FIELD_NUMBER: builtins.int
    POSTGRES_SOURCE_FIELD_NUMBER: builtins.int
    YDB_SOURCE_FIELD_NUMBER: builtins.int
    YDS_SOURCE_FIELD_NUMBER: builtins.int
    KAFKA_SOURCE_FIELD_NUMBER: builtins.int
    MONGO_SOURCE_FIELD_NUMBER: builtins.int
    CLICKHOUSE_SOURCE_FIELD_NUMBER: builtins.int
    MYSQL_TARGET_FIELD_NUMBER: builtins.int
    POSTGRES_TARGET_FIELD_NUMBER: builtins.int
    CLICKHOUSE_TARGET_FIELD_NUMBER: builtins.int
    YDB_TARGET_FIELD_NUMBER: builtins.int
    KAFKA_TARGET_FIELD_NUMBER: builtins.int
    MONGO_TARGET_FIELD_NUMBER: builtins.int
    METRIKA_SOURCE_FIELD_NUMBER: builtins.int
    YDS_TARGET_FIELD_NUMBER: builtins.int
    @property
    def mysql_source(self) -> yandex.cloud.datatransfer.v1.endpoint.mysql_pb2.MysqlSource: ...
    @property
    def postgres_source(self) -> yandex.cloud.datatransfer.v1.endpoint.postgres_pb2.PostgresSource: ...
    @property
    def ydb_source(self) -> yandex.cloud.datatransfer.v1.endpoint.ydb_pb2.YdbSource: ...
    @property
    def yds_source(self) -> yandex.cloud.datatransfer.v1.endpoint.yds_pb2.YDSSource: ...
    @property
    def kafka_source(self) -> yandex.cloud.datatransfer.v1.endpoint.kafka_pb2.KafkaSource: ...
    @property
    def mongo_source(self) -> yandex.cloud.datatransfer.v1.endpoint.mongo_pb2.MongoSource: ...
    @property
    def clickhouse_source(self) -> yandex.cloud.datatransfer.v1.endpoint.clickhouse_pb2.ClickhouseSource: ...
    @property
    def mysql_target(self) -> yandex.cloud.datatransfer.v1.endpoint.mysql_pb2.MysqlTarget: ...
    @property
    def postgres_target(self) -> yandex.cloud.datatransfer.v1.endpoint.postgres_pb2.PostgresTarget: ...
    @property
    def clickhouse_target(self) -> yandex.cloud.datatransfer.v1.endpoint.clickhouse_pb2.ClickhouseTarget: ...
    @property
    def ydb_target(self) -> yandex.cloud.datatransfer.v1.endpoint.ydb_pb2.YdbTarget: ...
    @property
    def kafka_target(self) -> yandex.cloud.datatransfer.v1.endpoint.kafka_pb2.KafkaTarget: ...
    @property
    def mongo_target(self) -> yandex.cloud.datatransfer.v1.endpoint.mongo_pb2.MongoTarget: ...
    @property
    def metrika_source(self) -> yandex.cloud.datatransfer.v1.endpoint.metrika_pb2.MetrikaSource: ...
    @property
    def yds_target(self) -> yandex.cloud.datatransfer.v1.endpoint.yds_pb2.YDSTarget: ...
    def __init__(
        self,
        *,
        mysql_source: yandex.cloud.datatransfer.v1.endpoint.mysql_pb2.MysqlSource | None = ...,
        postgres_source: yandex.cloud.datatransfer.v1.endpoint.postgres_pb2.PostgresSource | None = ...,
        ydb_source: yandex.cloud.datatransfer.v1.endpoint.ydb_pb2.YdbSource | None = ...,
        yds_source: yandex.cloud.datatransfer.v1.endpoint.yds_pb2.YDSSource | None = ...,
        kafka_source: yandex.cloud.datatransfer.v1.endpoint.kafka_pb2.KafkaSource | None = ...,
        mongo_source: yandex.cloud.datatransfer.v1.endpoint.mongo_pb2.MongoSource | None = ...,
        clickhouse_source: yandex.cloud.datatransfer.v1.endpoint.clickhouse_pb2.ClickhouseSource | None = ...,
        mysql_target: yandex.cloud.datatransfer.v1.endpoint.mysql_pb2.MysqlTarget | None = ...,
        postgres_target: yandex.cloud.datatransfer.v1.endpoint.postgres_pb2.PostgresTarget | None = ...,
        clickhouse_target: yandex.cloud.datatransfer.v1.endpoint.clickhouse_pb2.ClickhouseTarget | None = ...,
        ydb_target: yandex.cloud.datatransfer.v1.endpoint.ydb_pb2.YdbTarget | None = ...,
        kafka_target: yandex.cloud.datatransfer.v1.endpoint.kafka_pb2.KafkaTarget | None = ...,
        mongo_target: yandex.cloud.datatransfer.v1.endpoint.mongo_pb2.MongoTarget | None = ...,
        metrika_source: yandex.cloud.datatransfer.v1.endpoint.metrika_pb2.MetrikaSource | None = ...,
        yds_target: yandex.cloud.datatransfer.v1.endpoint.yds_pb2.YDSTarget | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["clickhouse_source", b"clickhouse_source", "clickhouse_target", b"clickhouse_target", "kafka_source", b"kafka_source", "kafka_target", b"kafka_target", "metrika_source", b"metrika_source", "mongo_source", b"mongo_source", "mongo_target", b"mongo_target", "mysql_source", b"mysql_source", "mysql_target", b"mysql_target", "postgres_source", b"postgres_source", "postgres_target", b"postgres_target", "settings", b"settings", "ydb_source", b"ydb_source", "ydb_target", b"ydb_target", "yds_source", b"yds_source", "yds_target", b"yds_target"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["clickhouse_source", b"clickhouse_source", "clickhouse_target", b"clickhouse_target", "kafka_source", b"kafka_source", "kafka_target", b"kafka_target", "metrika_source", b"metrika_source", "mongo_source", b"mongo_source", "mongo_target", b"mongo_target", "mysql_source", b"mysql_source", "mysql_target", b"mysql_target", "postgres_source", b"postgres_source", "postgres_target", b"postgres_target", "settings", b"settings", "ydb_source", b"ydb_source", "ydb_target", b"ydb_target", "yds_source", b"yds_source", "yds_target", b"yds_target"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["settings", b"settings"]) -> typing.Literal["mysql_source", "postgres_source", "ydb_source", "yds_source", "kafka_source", "mongo_source", "clickhouse_source", "mysql_target", "postgres_target", "clickhouse_target", "ydb_target", "kafka_target", "mongo_target", "metrika_source", "yds_target"] | None: ...

global___EndpointSettings = EndpointSettings
