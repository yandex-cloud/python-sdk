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
import google.protobuf.timestamp_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Test(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Test._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: Test._Status.ValueType  # 0
        CREATED: Test._Status.ValueType  # 1
        INITIATED: Test._Status.ValueType  # 2
        PREPARING: Test._Status.ValueType  # 3
        RUNNING: Test._Status.ValueType  # 4
        FINISHING: Test._Status.ValueType  # 5
        DONE: Test._Status.ValueType  # 6
        POST_PROCESSING: Test._Status.ValueType  # 7
        FAILED: Test._Status.ValueType  # 8
        STOPPING: Test._Status.ValueType  # 9
        STOPPED: Test._Status.ValueType  # 10
        AUTOSTOPPED: Test._Status.ValueType  # 11
        WAITING: Test._Status.ValueType  # 12
        DELETING: Test._Status.ValueType  # 13
        LOST: Test._Status.ValueType  # 14
        CANCELLED: Test._Status.ValueType  # 15

    class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...
    STATUS_UNSPECIFIED: Test.Status.ValueType  # 0
    CREATED: Test.Status.ValueType  # 1
    INITIATED: Test.Status.ValueType  # 2
    PREPARING: Test.Status.ValueType  # 3
    RUNNING: Test.Status.ValueType  # 4
    FINISHING: Test.Status.ValueType  # 5
    DONE: Test.Status.ValueType  # 6
    POST_PROCESSING: Test.Status.ValueType  # 7
    FAILED: Test.Status.ValueType  # 8
    STOPPING: Test.Status.ValueType  # 9
    STOPPED: Test.Status.ValueType  # 10
    AUTOSTOPPED: Test.Status.ValueType  # 11
    WAITING: Test.Status.ValueType  # 12
    DELETING: Test.Status.ValueType  # 13
    LOST: Test.Status.ValueType  # 14
    CANCELLED: Test.Status.ValueType  # 15

    class _Generator:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _GeneratorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Test._Generator.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        GENERATOR_UNSPECIFIED: Test._Generator.ValueType  # 0
        PANDORA: Test._Generator.ValueType  # 1
        PHANTOM: Test._Generator.ValueType  # 2
        JMETER: Test._Generator.ValueType  # 3

    class Generator(_Generator, metaclass=_GeneratorEnumTypeWrapper): ...
    GENERATOR_UNSPECIFIED: Test.Generator.ValueType  # 0
    PANDORA: Test.Generator.ValueType  # 1
    PHANTOM: Test.Generator.ValueType  # 2
    JMETER: Test.Generator.ValueType  # 3

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
    CREATED_AT_FIELD_NUMBER: builtins.int
    STARTED_AT_FIELD_NUMBER: builtins.int
    FINISHED_AT_FIELD_NUMBER: builtins.int
    UPDATED_AT_FIELD_NUMBER: builtins.int
    GENERATOR_FIELD_NUMBER: builtins.int
    AGENT_INSTANCE_ID_FIELD_NUMBER: builtins.int
    TARGET_ADDRESS_FIELD_NUMBER: builtins.int
    TARGET_PORT_FIELD_NUMBER: builtins.int
    TARGET_VERSION_FIELD_NUMBER: builtins.int
    CONFIG_FIELD_NUMBER: builtins.int
    AMMO_URLS_FIELD_NUMBER: builtins.int
    AMMO_ID_FIELD_NUMBER: builtins.int
    CASES_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    ERRORS_FIELD_NUMBER: builtins.int
    FAVORITE_FIELD_NUMBER: builtins.int
    id: builtins.str
    folder_id: builtins.str
    name: builtins.str
    description: builtins.str
    generator: global___Test.Generator.ValueType
    agent_instance_id: builtins.str
    """AgentInstance ID where Test is running."""
    target_address: builtins.str
    """Target VM."""
    target_port: builtins.int
    target_version: builtins.str
    """Version of object under test."""
    config: builtins.str
    """Test details"""
    ammo_urls: builtins.str
    ammo_id: builtins.str
    status: global___Test.Status.ValueType
    favorite: builtins.bool
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def started_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def finished_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def updated_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def cases(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def errors(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        folder_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        started_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        finished_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        updated_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        generator: global___Test.Generator.ValueType = ...,
        agent_instance_id: builtins.str = ...,
        target_address: builtins.str = ...,
        target_port: builtins.int = ...,
        target_version: builtins.str = ...,
        config: builtins.str = ...,
        ammo_urls: builtins.str = ...,
        ammo_id: builtins.str = ...,
        cases: collections.abc.Iterable[builtins.str] | None = ...,
        status: global___Test.Status.ValueType = ...,
        errors: collections.abc.Iterable[builtins.str] | None = ...,
        favorite: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["ammo", b"ammo", "ammo_id", b"ammo_id", "ammo_urls", b"ammo_urls", "created_at", b"created_at", "finished_at", b"finished_at", "started_at", b"started_at", "updated_at", b"updated_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["agent_instance_id", b"agent_instance_id", "ammo", b"ammo", "ammo_id", b"ammo_id", "ammo_urls", b"ammo_urls", "cases", b"cases", "config", b"config", "created_at", b"created_at", "description", b"description", "errors", b"errors", "favorite", b"favorite", "finished_at", b"finished_at", "folder_id", b"folder_id", "generator", b"generator", "id", b"id", "labels", b"labels", "name", b"name", "started_at", b"started_at", "status", b"status", "target_address", b"target_address", "target_port", b"target_port", "target_version", b"target_version", "updated_at", b"updated_at"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["ammo", b"ammo"]) -> typing.Literal["ammo_urls", "ammo_id"] | None: ...

global___Test = Test
