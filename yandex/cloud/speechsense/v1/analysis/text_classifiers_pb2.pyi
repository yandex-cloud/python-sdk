"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.wrappers_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class TextClassifiers(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLASSIFICATION_RESULT_FIELD_NUMBER: builtins.int
    @property
    def classification_result(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ClassificationResult]: ...
    def __init__(
        self,
        *,
        classification_result: collections.abc.Iterable[global___ClassificationResult] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["classification_result", b"classification_result"]) -> None: ...

global___TextClassifiers = TextClassifiers

@typing.final
class ClassificationResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLASSIFIER_FIELD_NUMBER: builtins.int
    CLASSIFIER_STATISTICS_FIELD_NUMBER: builtins.int
    classifier: builtins.str
    """Classifier name"""
    @property
    def classifier_statistics(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ClassifierStatistics]:
        """Classifier statistics"""

    def __init__(
        self,
        *,
        classifier: builtins.str = ...,
        classifier_statistics: collections.abc.Iterable[global___ClassifierStatistics] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["classifier", b"classifier", "classifier_statistics", b"classifier_statistics"]) -> None: ...

global___ClassificationResult = ClassificationResult

@typing.final
class ClassifierStatistics(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CHANNEL_NUMBER_FIELD_NUMBER: builtins.int
    TOTAL_COUNT_FIELD_NUMBER: builtins.int
    HISTOGRAMS_FIELD_NUMBER: builtins.int
    total_count: builtins.int
    """classifier total count"""
    @property
    def channel_number(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """Channel number, null for whole talk"""

    @property
    def histograms(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Histogram]:
        """Represents various histograms build on top of classifiers"""

    def __init__(
        self,
        *,
        channel_number: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        total_count: builtins.int = ...,
        histograms: collections.abc.Iterable[global___Histogram] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["channel_number", b"channel_number"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["channel_number", b"channel_number", "histograms", b"histograms", "total_count", b"total_count"]) -> None: ...

global___ClassifierStatistics = ClassifierStatistics

@typing.final
class Histogram(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COUNT_VALUES_FIELD_NUMBER: builtins.int
    @property
    def count_values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """histogram count values. For example:
        if len(count_values) = 2, it means that histogram is 50/50,
        if len(count_values) = 3 - [0] value represents first third, [1] - second third, [2] - last third, etc.
        """

    def __init__(
        self,
        *,
        count_values: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["count_values", b"count_values"]) -> None: ...

global___Histogram = Histogram
