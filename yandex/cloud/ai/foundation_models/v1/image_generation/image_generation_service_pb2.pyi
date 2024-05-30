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
import yandex.cloud.ai.foundation_models.v1.image_generation.image_generation_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class ImageGenerationRequest(google.protobuf.message.Message):
    """Request for the service to generate an image."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MODEL_URI_FIELD_NUMBER: builtins.int
    MESSAGES_FIELD_NUMBER: builtins.int
    GENERATION_OPTIONS_FIELD_NUMBER: builtins.int
    model_uri: builtins.str
    """The [ID of the model](/docs/foundation-models/concepts/yandexart/models) to be used for image generation."""
    @property
    def messages(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.ai.foundation_models.v1.image_generation.image_generation_pb2.Message]:
        """A list of messages representing the context for the image generation model."""

    @property
    def generation_options(self) -> yandex.cloud.ai.foundation_models.v1.image_generation.image_generation_pb2.ImageGenerationOptions:
        """Image generation options."""

    def __init__(
        self,
        *,
        model_uri: builtins.str = ...,
        messages: collections.abc.Iterable[yandex.cloud.ai.foundation_models.v1.image_generation.image_generation_pb2.Message] | None = ...,
        generation_options: yandex.cloud.ai.foundation_models.v1.image_generation.image_generation_pb2.ImageGenerationOptions | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["generation_options", b"generation_options"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["generation_options", b"generation_options", "messages", b"messages", "model_uri", b"model_uri"]) -> None: ...

global___ImageGenerationRequest = ImageGenerationRequest

@typing.final
class ImageGenerationResponse(google.protobuf.message.Message):
    """Response containing generated image."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IMAGE_FIELD_NUMBER: builtins.int
    MODEL_VERSION_FIELD_NUMBER: builtins.int
    image: builtins.bytes
    """The image is serialized as an array of bytes encoded in base64."""
    model_version: builtins.str
    """The model version changes with each new releases."""
    def __init__(
        self,
        *,
        image: builtins.bytes = ...,
        model_version: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["image", b"image", "model_version", b"model_version"]) -> None: ...

global___ImageGenerationResponse = ImageGenerationResponse
