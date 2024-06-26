"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import yandex.cloud.speechsense.v1.analysis.statistics_common_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class UtteranceStatistics(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SPEAKER_TAG_FIELD_NUMBER: builtins.int
    SPEECH_BOUNDARIES_FIELD_NUMBER: builtins.int
    TOTAL_SPEECH_MS_FIELD_NUMBER: builtins.int
    SPEECH_RATIO_FIELD_NUMBER: builtins.int
    TOTAL_SILENCE_MS_FIELD_NUMBER: builtins.int
    SILENCE_RATIO_FIELD_NUMBER: builtins.int
    WORDS_COUNT_FIELD_NUMBER: builtins.int
    LETTERS_COUNT_FIELD_NUMBER: builtins.int
    WORDS_PER_SECOND_FIELD_NUMBER: builtins.int
    LETTERS_PER_SECOND_FIELD_NUMBER: builtins.int
    speaker_tag: builtins.str
    total_speech_ms: builtins.int
    """Total speech duration"""
    speech_ratio: builtins.float
    """Speech ratio within audio segment"""
    total_silence_ms: builtins.int
    """Total silence duration"""
    silence_ratio: builtins.float
    """Silence ratio within audio segment"""
    words_count: builtins.int
    """Number of words in recognized speech"""
    letters_count: builtins.int
    """Number of letters in recognized speech"""
    @property
    def speech_boundaries(self) -> yandex.cloud.speechsense.v1.analysis.statistics_common_pb2.AudioSegmentBoundaries:
        """Audio segment boundaries"""

    @property
    def words_per_second(self) -> yandex.cloud.speechsense.v1.analysis.statistics_common_pb2.DescriptiveStatistics:
        """Descriptive statistics for words per second distribution"""

    @property
    def letters_per_second(self) -> yandex.cloud.speechsense.v1.analysis.statistics_common_pb2.DescriptiveStatistics:
        """Descriptive statistics for letters per second distribution"""

    def __init__(
        self,
        *,
        speaker_tag: builtins.str = ...,
        speech_boundaries: yandex.cloud.speechsense.v1.analysis.statistics_common_pb2.AudioSegmentBoundaries | None = ...,
        total_speech_ms: builtins.int = ...,
        speech_ratio: builtins.float = ...,
        total_silence_ms: builtins.int = ...,
        silence_ratio: builtins.float = ...,
        words_count: builtins.int = ...,
        letters_count: builtins.int = ...,
        words_per_second: yandex.cloud.speechsense.v1.analysis.statistics_common_pb2.DescriptiveStatistics | None = ...,
        letters_per_second: yandex.cloud.speechsense.v1.analysis.statistics_common_pb2.DescriptiveStatistics | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["letters_per_second", b"letters_per_second", "speech_boundaries", b"speech_boundaries", "words_per_second", b"words_per_second"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["letters_count", b"letters_count", "letters_per_second", b"letters_per_second", "silence_ratio", b"silence_ratio", "speaker_tag", b"speaker_tag", "speech_boundaries", b"speech_boundaries", "speech_ratio", b"speech_ratio", "total_silence_ms", b"total_silence_ms", "total_speech_ms", b"total_speech_ms", "words_count", b"words_count", "words_per_second", b"words_per_second"]) -> None: ...

global___UtteranceStatistics = UtteranceStatistics
