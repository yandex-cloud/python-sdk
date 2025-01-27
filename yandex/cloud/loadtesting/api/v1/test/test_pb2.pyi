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
import yandex.cloud.loadtesting.api.v1.test.details_pb2
import yandex.cloud.loadtesting.api.v1.test.single_agent_configuration_pb2
import yandex.cloud.loadtesting.api.v1.test.summary_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Test(google.protobuf.message.Message):
    """Load Test.

    In context of the service, Test represents a single testing task/job.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    CONFIGURATIONS_FIELD_NUMBER: builtins.int
    DETAILS_FIELD_NUMBER: builtins.int
    SUMMARY_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the test. Generated at creation time."""
    folder_id: builtins.str
    """ID of the folder that the test belongs to."""
    @property
    def configurations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.loadtesting.api.v1.test.single_agent_configuration_pb2.SingleAgentConfiguration]:
        """Configuration of the test.

        A test can have multiple configurations if it can be
        executed on multiple agents simultaneously. For more information, see
        [Load testing using multiple agents](/docs/load-testing/tutorials/loadtesting-multiply).
        """

    @property
    def details(self) -> yandex.cloud.loadtesting.api.v1.test.details_pb2.Details:
        """Test meta information. Name, description, etc."""

    @property
    def summary(self) -> yandex.cloud.loadtesting.api.v1.test.summary_pb2.Summary:
        """Test execution information."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        configurations: collections.abc.Iterable[yandex.cloud.loadtesting.api.v1.test.single_agent_configuration_pb2.SingleAgentConfiguration] | None = ...,
        details: yandex.cloud.loadtesting.api.v1.test.details_pb2.Details | None = ...,
        summary: yandex.cloud.loadtesting.api.v1.test.summary_pb2.Summary | None = ...,
        folder_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["details", b"details", "summary", b"summary"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["configurations", b"configurations", "details", b"details", "folder_id", b"folder_id", "id", b"id", "summary", b"summary"]) -> None: ...

global___Test = Test
