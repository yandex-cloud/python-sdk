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

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class RecognitionClassifierResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    START_TIME_MS_FIELD_NUMBER: builtins.int
    END_TIME_MS_FIELD_NUMBER: builtins.int
    CLASSIFIER_FIELD_NUMBER: builtins.int
    HIGHLIGHTS_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    start_time_ms: builtins.int
    """Start time of the audio segment used for classification"""
    end_time_ms: builtins.int
    """End time of the audio segment used for classification"""
    classifier: builtins.str
    """Name of the triggered classifier"""
    @property
    def highlights(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PhraseHighlight]:
        """List of highlights, i.e. parts of phrase that determine the result of the classification"""

    @property
    def labels(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___RecognitionClassifierLabel]:
        """Classifier predictions"""

    def __init__(
        self,
        *,
        start_time_ms: builtins.int = ...,
        end_time_ms: builtins.int = ...,
        classifier: builtins.str = ...,
        highlights: collections.abc.Iterable[global___PhraseHighlight] | None = ...,
        labels: collections.abc.Iterable[global___RecognitionClassifierLabel] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["classifier", b"classifier", "end_time_ms", b"end_time_ms", "highlights", b"highlights", "labels", b"labels", "start_time_ms", b"start_time_ms"]) -> None: ...

global___RecognitionClassifierResult = RecognitionClassifierResult

@typing.final
class PhraseHighlight(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TEXT_FIELD_NUMBER: builtins.int
    OFFSET_FIELD_NUMBER: builtins.int
    COUNT_FIELD_NUMBER: builtins.int
    text: builtins.str
    """Text transcription of the highlighted audio segment"""
    offset: builtins.int
    """offset in symbols from the beginning of whole phrase where highlight begins"""
    count: builtins.int
    """count of symbols in highlighted text"""
    def __init__(
        self,
        *,
        text: builtins.str = ...,
        offset: builtins.int = ...,
        count: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["count", b"count", "offset", b"offset", "text", b"text"]) -> None: ...

global___PhraseHighlight = PhraseHighlight

@typing.final
class RecognitionClassifierLabel(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LABEL_FIELD_NUMBER: builtins.int
    CONFIDENCE_FIELD_NUMBER: builtins.int
    label: builtins.str
    """The label of the class predicted by the classifier"""
    confidence: builtins.float
    """The prediction confidence"""
    def __init__(
        self,
        *,
        label: builtins.str = ...,
        confidence: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["confidence", b"confidence", "label", b"label"]) -> None: ...

global___RecognitionClassifierLabel = RecognitionClassifierLabel