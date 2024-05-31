"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.ai.stt.v3.stt_pb2
import yandex.cloud.ai.stt.v3.stt_service_pb2
import yandex.cloud.operation.operation_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class RecognizerStub:
    """A set of methods for voice recognition."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    RecognizeStreaming: grpc.StreamStreamMultiCallable[
        yandex.cloud.ai.stt.v3.stt_pb2.StreamingRequest,
        yandex.cloud.ai.stt.v3.stt_pb2.StreamingResponse,
    ]
    """Expects audio in real-time"""

class RecognizerAsyncStub:
    """A set of methods for voice recognition."""

    RecognizeStreaming: grpc.aio.StreamStreamMultiCallable[
        yandex.cloud.ai.stt.v3.stt_pb2.StreamingRequest,
        yandex.cloud.ai.stt.v3.stt_pb2.StreamingResponse,
    ]
    """Expects audio in real-time"""

class RecognizerServicer(metaclass=abc.ABCMeta):
    """A set of methods for voice recognition."""

    @abc.abstractmethod
    def RecognizeStreaming(
        self,
        request_iterator: _MaybeAsyncIterator[yandex.cloud.ai.stt.v3.stt_pb2.StreamingRequest],
        context: _ServicerContext,
    ) -> typing.Union[collections.abc.Iterator[yandex.cloud.ai.stt.v3.stt_pb2.StreamingResponse], collections.abc.AsyncIterator[yandex.cloud.ai.stt.v3.stt_pb2.StreamingResponse]]:
        """Expects audio in real-time"""

def add_RecognizerServicer_to_server(servicer: RecognizerServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...

class AsyncRecognizerStub:
    """A set of methods for async voice recognition."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    RecognizeFile: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ai.stt.v3.stt_pb2.RecognizeFileRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]

    GetRecognition: grpc.UnaryStreamMultiCallable[
        yandex.cloud.ai.stt.v3.stt_service_pb2.GetRecognitionRequest,
        yandex.cloud.ai.stt.v3.stt_pb2.StreamingResponse,
    ]

class AsyncRecognizerAsyncStub:
    """A set of methods for async voice recognition."""

    RecognizeFile: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.ai.stt.v3.stt_pb2.RecognizeFileRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]

    GetRecognition: grpc.aio.UnaryStreamMultiCallable[
        yandex.cloud.ai.stt.v3.stt_service_pb2.GetRecognitionRequest,
        yandex.cloud.ai.stt.v3.stt_pb2.StreamingResponse,
    ]

class AsyncRecognizerServicer(metaclass=abc.ABCMeta):
    """A set of methods for async voice recognition."""

    @abc.abstractmethod
    def RecognizeFile(
        self,
        request: yandex.cloud.ai.stt.v3.stt_pb2.RecognizeFileRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]: ...

    @abc.abstractmethod
    def GetRecognition(
        self,
        request: yandex.cloud.ai.stt.v3.stt_service_pb2.GetRecognitionRequest,
        context: _ServicerContext,
    ) -> typing.Union[collections.abc.Iterator[yandex.cloud.ai.stt.v3.stt_pb2.StreamingResponse], collections.abc.AsyncIterator[yandex.cloud.ai.stt.v3.stt_pb2.StreamingResponse]]: ...

def add_AsyncRecognizerServicer_to_server(servicer: AsyncRecognizerServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
