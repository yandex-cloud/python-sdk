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
class RawAudio(google.protobuf.message.Message):
    """RAW Audio format spec (no container to infer type). Used in AudioFormat options."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _AudioEncoding:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _AudioEncodingEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[RawAudio._AudioEncoding.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        AUDIO_ENCODING_UNSPECIFIED: RawAudio._AudioEncoding.ValueType  # 0
        AUDIO_ENCODING_LINEAR16_PCM: RawAudio._AudioEncoding.ValueType  # 1
        """Audio bit depth 16-bit signed little-endian (Linear PCM)."""

    class AudioEncoding(_AudioEncoding, metaclass=_AudioEncodingEnumTypeWrapper): ...
    AUDIO_ENCODING_UNSPECIFIED: RawAudio.AudioEncoding.ValueType  # 0
    AUDIO_ENCODING_LINEAR16_PCM: RawAudio.AudioEncoding.ValueType  # 1
    """Audio bit depth 16-bit signed little-endian (Linear PCM)."""

    AUDIO_ENCODING_FIELD_NUMBER: builtins.int
    SAMPLE_RATE_HERTZ_FIELD_NUMBER: builtins.int
    AUDIO_CHANNEL_COUNT_FIELD_NUMBER: builtins.int
    audio_encoding: global___RawAudio.AudioEncoding.ValueType
    """ Type of audio encoding"""
    sample_rate_hertz: builtins.int
    """ PCM sample rate"""
    audio_channel_count: builtins.int
    """ PCM channel count."""
    def __init__(
        self,
        *,
        audio_encoding: global___RawAudio.AudioEncoding.ValueType = ...,
        sample_rate_hertz: builtins.int = ...,
        audio_channel_count: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["audio_channel_count", b"audio_channel_count", "audio_encoding", b"audio_encoding", "sample_rate_hertz", b"sample_rate_hertz"]) -> None: ...

global___RawAudio = RawAudio

@typing.final
class ContainerAudio(google.protobuf.message.Message):
    """Audio with fixed type in container. Used in AudioFormat options."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _ContainerAudioType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _ContainerAudioTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ContainerAudio._ContainerAudioType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        CONTAINER_AUDIO_TYPE_UNSPECIFIED: ContainerAudio._ContainerAudioType.ValueType  # 0
        CONTAINER_AUDIO_TYPE_WAV: ContainerAudio._ContainerAudioType.ValueType  # 1
        """Audio bit depth 16-bit signed little-endian (Linear PCM)."""
        CONTAINER_AUDIO_TYPE_OGG_OPUS: ContainerAudio._ContainerAudioType.ValueType  # 2
        """Data is encoded using the OPUS audio codec and compressed using the OGG container format."""
        CONTAINER_AUDIO_TYPE_MP3: ContainerAudio._ContainerAudioType.ValueType  # 3
        """Data is encoded using MPEG-1/2 Layer III and compressed using the MP3 container format."""

    class ContainerAudioType(_ContainerAudioType, metaclass=_ContainerAudioTypeEnumTypeWrapper): ...
    CONTAINER_AUDIO_TYPE_UNSPECIFIED: ContainerAudio.ContainerAudioType.ValueType  # 0
    CONTAINER_AUDIO_TYPE_WAV: ContainerAudio.ContainerAudioType.ValueType  # 1
    """Audio bit depth 16-bit signed little-endian (Linear PCM)."""
    CONTAINER_AUDIO_TYPE_OGG_OPUS: ContainerAudio.ContainerAudioType.ValueType  # 2
    """Data is encoded using the OPUS audio codec and compressed using the OGG container format."""
    CONTAINER_AUDIO_TYPE_MP3: ContainerAudio.ContainerAudioType.ValueType  # 3
    """Data is encoded using MPEG-1/2 Layer III and compressed using the MP3 container format."""

    CONTAINER_AUDIO_TYPE_FIELD_NUMBER: builtins.int
    container_audio_type: global___ContainerAudio.ContainerAudioType.ValueType
    """ Type of audio container."""
    def __init__(
        self,
        *,
        container_audio_type: global___ContainerAudio.ContainerAudioType.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["container_audio_type", b"container_audio_type"]) -> None: ...

global___ContainerAudio = ContainerAudio

@typing.final
class AudioMetadata(google.protobuf.message.Message):
    """Audio format options."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RAW_AUDIO_FIELD_NUMBER: builtins.int
    CONTAINER_AUDIO_FIELD_NUMBER: builtins.int
    @property
    def raw_audio(self) -> global___RawAudio:
        """Audio without container."""

    @property
    def container_audio(self) -> global___ContainerAudio:
        """Audio is wrapped in container."""

    def __init__(
        self,
        *,
        raw_audio: global___RawAudio | None = ...,
        container_audio: global___ContainerAudio | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["AudioFormat", b"AudioFormat", "container_audio", b"container_audio", "raw_audio", b"raw_audio"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["AudioFormat", b"AudioFormat", "container_audio", b"container_audio", "raw_audio", b"raw_audio"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["AudioFormat", b"AudioFormat"]) -> typing.Literal["raw_audio", "container_audio"] | None: ...

global___AudioMetadata = AudioMetadata

@typing.final
class AudioChunk(google.protobuf.message.Message):
    """Data chunk with audio."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_FIELD_NUMBER: builtins.int
    data: builtins.bytes
    """Bytes with audio data."""
    def __init__(
        self,
        *,
        data: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["data", b"data"]) -> None: ...

global___AudioChunk = AudioChunk

@typing.final
class AudioStreamingRequest(google.protobuf.message.Message):
    """Streaming audio request
    First message should be audio metadata.
    The next messages are audio data chunks.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AUDIO_METADATA_FIELD_NUMBER: builtins.int
    CHUNK_FIELD_NUMBER: builtins.int
    @property
    def audio_metadata(self) -> global___AudioMetadata:
        """Session options. Should be the first message from user."""

    @property
    def chunk(self) -> global___AudioChunk:
        """Chunk with audio data."""

    def __init__(
        self,
        *,
        audio_metadata: global___AudioMetadata | None = ...,
        chunk: global___AudioChunk | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["AudioEvent", b"AudioEvent", "audio_metadata", b"audio_metadata", "chunk", b"chunk"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["AudioEvent", b"AudioEvent", "audio_metadata", b"audio_metadata", "chunk", b"chunk"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["AudioEvent", b"AudioEvent"]) -> typing.Literal["audio_metadata", "chunk"] | None: ...

global___AudioStreamingRequest = AudioStreamingRequest

@typing.final
class AudioRequest(google.protobuf.message.Message):
    """request for sending small audios (< 128 mb) in one go"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AUDIO_METADATA_FIELD_NUMBER: builtins.int
    AUDIO_DATA_FIELD_NUMBER: builtins.int
    @property
    def audio_metadata(self) -> global___AudioMetadata:
        """audio metadata"""

    @property
    def audio_data(self) -> global___AudioChunk:
        """Bytes with audio data."""

    def __init__(
        self,
        *,
        audio_metadata: global___AudioMetadata | None = ...,
        audio_data: global___AudioChunk | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["audio_data", b"audio_data", "audio_metadata", b"audio_metadata"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["audio_data", b"audio_data", "audio_metadata", b"audio_metadata"]) -> None: ...

global___AudioRequest = AudioRequest