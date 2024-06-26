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
import yandex.cloud.loadtesting.api.v1.test.agent_selector_pb2
import yandex.cloud.loadtesting.api.v1.test.file_pointer_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class SingleAgentConfiguration(google.protobuf.message.Message):
    """Configuration of a test."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class FilesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> yandex.cloud.loadtesting.api.v1.test.file_pointer_pb2.FilePointer: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: yandex.cloud.loadtesting.api.v1.test.file_pointer_pb2.FilePointer | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    CONFIG_ID_FIELD_NUMBER: builtins.int
    AGENT_SELECTOR_FIELD_NUMBER: builtins.int
    FILES_FIELD_NUMBER: builtins.int
    config_id: builtins.str
    """ID of the config."""
    @property
    def agent_selector(self) -> yandex.cloud.loadtesting.api.v1.test.agent_selector_pb2.AgentSelector:
        """Agent selection criterion."""

    @property
    def files(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, yandex.cloud.loadtesting.api.v1.test.file_pointer_pb2.FilePointer]:
        """Additional files to be used during test execution, represented as `rel_path:file` pairs.

        `rel_path` can be either a simple file name, a relative path, or absolute path. Files are
        downloaded by the agent to appropriate location.

        Use cases include:
        - [Test Data files](/docs/load-testing/concepts/payload).
        - Custom Pandora executable.
        - JMeter executable or ".jmx" scenario.
        - etc.
        """

    def __init__(
        self,
        *,
        config_id: builtins.str = ...,
        agent_selector: yandex.cloud.loadtesting.api.v1.test.agent_selector_pb2.AgentSelector | None = ...,
        files: collections.abc.Mapping[builtins.str, yandex.cloud.loadtesting.api.v1.test.file_pointer_pb2.FilePointer] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["agent_selector", b"agent_selector"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["agent_selector", b"agent_selector", "config_id", b"config_id", "files", b"files"]) -> None: ...

global___SingleAgentConfiguration = SingleAgentConfiguration
