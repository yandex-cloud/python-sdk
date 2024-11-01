"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import yandex.cloud.ai.assistants.v1.assistant_pb2
import yandex.cloud.ai.assistants.v1.common_pb2
import yandex.cloud.ai.common.common_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class CreateAssistantRequest(google.protobuf.message.Message):
    """Request to create a new assistant."""

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

    FOLDER_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    EXPIRATION_CONFIG_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    MODEL_URI_FIELD_NUMBER: builtins.int
    INSTRUCTION_FIELD_NUMBER: builtins.int
    PROMPT_TRUNCATION_OPTIONS_FIELD_NUMBER: builtins.int
    COMPLETION_OPTIONS_FIELD_NUMBER: builtins.int
    TOOLS_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    name: builtins.str
    """Name of the assistant."""
    description: builtins.str
    """Description of the assistant."""
    model_uri: builtins.str
    """The [ID of the model](/docs/foundation-models/concepts/yandexgpt/models) to be used for completion generation."""
    instruction: builtins.str
    """Instructions or guidelines that the assistant should follow when generating responses or performing tasks.
    These instructions can help guide the assistant's behavior and responses.
    """
    @property
    def expiration_config(self) -> yandex.cloud.ai.common.common_pb2.ExpirationConfig:
        """Expiration configuration for the assistant."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Set of key-value pairs to label the user."""

    @property
    def prompt_truncation_options(self) -> yandex.cloud.ai.assistants.v1.common_pb2.PromptTruncationOptions:
        """Configuration options for truncating the prompt when the token count exceeds a specified limit."""

    @property
    def completion_options(self) -> yandex.cloud.ai.assistants.v1.common_pb2.CompletionOptions:
        """Configuration options for completion generation."""

    @property
    def tools(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.ai.assistants.v1.common_pb2.Tool]:
        """List of tools that the assistant can use to perform additional tasks.
        One example is the SearchIndexTool, which is used for Retrieval-Augmented Generation (RAG).
        """

    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        expiration_config: yandex.cloud.ai.common.common_pb2.ExpirationConfig | None = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        model_uri: builtins.str = ...,
        instruction: builtins.str = ...,
        prompt_truncation_options: yandex.cloud.ai.assistants.v1.common_pb2.PromptTruncationOptions | None = ...,
        completion_options: yandex.cloud.ai.assistants.v1.common_pb2.CompletionOptions | None = ...,
        tools: collections.abc.Iterable[yandex.cloud.ai.assistants.v1.common_pb2.Tool] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["completion_options", b"completion_options", "expiration_config", b"expiration_config", "prompt_truncation_options", b"prompt_truncation_options"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["completion_options", b"completion_options", "description", b"description", "expiration_config", b"expiration_config", "folder_id", b"folder_id", "instruction", b"instruction", "labels", b"labels", "model_uri", b"model_uri", "name", b"name", "prompt_truncation_options", b"prompt_truncation_options", "tools", b"tools"]) -> None: ...

global___CreateAssistantRequest = CreateAssistantRequest

@typing.final
class GetAssistantRequest(google.protobuf.message.Message):
    """Request message for retrieving an assistant by ID."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ASSISTANT_ID_FIELD_NUMBER: builtins.int
    assistant_id: builtins.str
    """ID of the assistant to retrieve."""
    def __init__(
        self,
        *,
        assistant_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["assistant_id", b"assistant_id"]) -> None: ...

global___GetAssistantRequest = GetAssistantRequest

@typing.final
class UpdateAssistantRequest(google.protobuf.message.Message):
    """Request message for updating an existing assistant."""

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

    ASSISTANT_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    EXPIRATION_CONFIG_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    MODEL_URI_FIELD_NUMBER: builtins.int
    INSTRUCTION_FIELD_NUMBER: builtins.int
    PROMPT_TRUNCATION_OPTIONS_FIELD_NUMBER: builtins.int
    COMPLETION_OPTIONS_FIELD_NUMBER: builtins.int
    TOOLS_FIELD_NUMBER: builtins.int
    assistant_id: builtins.str
    """ID of the assistant to update."""
    name: builtins.str
    """New name for the assistant."""
    description: builtins.str
    """New description for the assistant."""
    model_uri: builtins.str
    """The new [ID of the model](/docs/foundation-models/concepts/yandexgpt/models) to be used for completion generation."""
    instruction: builtins.str
    """New instructions or guidelines for the assistant to follow."""
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask specifying which fields to update."""

    @property
    def expiration_config(self) -> yandex.cloud.ai.common.common_pb2.ExpirationConfig:
        """New expiration configuration for the assistant."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """New set of labels for the assistant."""

    @property
    def prompt_truncation_options(self) -> yandex.cloud.ai.assistants.v1.common_pb2.PromptTruncationOptions:
        """New configuration for truncating the prompt."""

    @property
    def completion_options(self) -> yandex.cloud.ai.assistants.v1.common_pb2.CompletionOptions:
        """New configuration for completion generation."""

    @property
    def tools(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.ai.assistants.v1.common_pb2.Tool]:
        """New list of tools the assistant can use."""

    def __init__(
        self,
        *,
        assistant_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        expiration_config: yandex.cloud.ai.common.common_pb2.ExpirationConfig | None = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        model_uri: builtins.str = ...,
        instruction: builtins.str = ...,
        prompt_truncation_options: yandex.cloud.ai.assistants.v1.common_pb2.PromptTruncationOptions | None = ...,
        completion_options: yandex.cloud.ai.assistants.v1.common_pb2.CompletionOptions | None = ...,
        tools: collections.abc.Iterable[yandex.cloud.ai.assistants.v1.common_pb2.Tool] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["completion_options", b"completion_options", "expiration_config", b"expiration_config", "prompt_truncation_options", b"prompt_truncation_options", "update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["assistant_id", b"assistant_id", "completion_options", b"completion_options", "description", b"description", "expiration_config", b"expiration_config", "instruction", b"instruction", "labels", b"labels", "model_uri", b"model_uri", "name", b"name", "prompt_truncation_options", b"prompt_truncation_options", "tools", b"tools", "update_mask", b"update_mask"]) -> None: ...

global___UpdateAssistantRequest = UpdateAssistantRequest

@typing.final
class DeleteAssistantRequest(google.protobuf.message.Message):
    """Request message for deleting an assistant by ID."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ASSISTANT_ID_FIELD_NUMBER: builtins.int
    assistant_id: builtins.str
    """ID of the assistant to delete."""
    def __init__(
        self,
        *,
        assistant_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["assistant_id", b"assistant_id"]) -> None: ...

global___DeleteAssistantRequest = DeleteAssistantRequest

@typing.final
class DeleteAssistantResponse(google.protobuf.message.Message):
    """Response message for the delete operation."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___DeleteAssistantResponse = DeleteAssistantResponse

@typing.final
class ListAssistantsRequest(google.protobuf.message.Message):
    """Request message for listing assistants in a specific folder."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """Folder ID from which to list assistants."""
    page_size: builtins.int
    """Maximum number of assistants to return per page."""
    page_token: builtins.str
    """Token to retrieve the next page of results."""
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["folder_id", b"folder_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListAssistantsRequest = ListAssistantsRequest

@typing.final
class ListAssistantsResponse(google.protobuf.message.Message):
    """Response message for the list operation."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ASSISTANTS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token to retrieve the next page of results."""
    @property
    def assistants(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.ai.assistants.v1.assistant_pb2.Assistant]:
        """List of assistants in the specified folder."""

    def __init__(
        self,
        *,
        assistants: collections.abc.Iterable[yandex.cloud.ai.assistants.v1.assistant_pb2.Assistant] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["assistants", b"assistants", "next_page_token", b"next_page_token"]) -> None: ...

global___ListAssistantsResponse = ListAssistantsResponse

@typing.final
class ListAssistantVersionsRequest(google.protobuf.message.Message):
    """Request to list all versions of a specific assistant."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ASSISTANT_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    assistant_id: builtins.str
    """ID of the assistant whose versions are to be listed."""
    page_size: builtins.int
    """Maximum number of versions to return per page."""
    page_token: builtins.str
    """Token to retrieve the next page of results."""
    def __init__(
        self,
        *,
        assistant_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["assistant_id", b"assistant_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListAssistantVersionsRequest = ListAssistantVersionsRequest

@typing.final
class AssistantVersion(google.protobuf.message.Message):
    """Represents a specific version of an assistant."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    ASSISTANT_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the assistant version."""
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Mask specifying which fields were updated in this version."""

    @property
    def assistant(self) -> yandex.cloud.ai.assistants.v1.assistant_pb2.Assistant:
        """Assistant configuration for this version."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        assistant: yandex.cloud.ai.assistants.v1.assistant_pb2.Assistant | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["assistant", b"assistant", "update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["assistant", b"assistant", "id", b"id", "update_mask", b"update_mask"]) -> None: ...

global___AssistantVersion = AssistantVersion

@typing.final
class ListAssistantVersionsResponse(google.protobuf.message.Message):
    """Response message containing the list versions operation."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VERSIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token to retrieve the next page of results."""
    @property
    def versions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AssistantVersion]:
        """List of assistant versions."""

    def __init__(
        self,
        *,
        versions: collections.abc.Iterable[global___AssistantVersion] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "versions", b"versions"]) -> None: ...

global___ListAssistantVersionsResponse = ListAssistantVersionsResponse