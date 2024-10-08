"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.ai.assistants.v1.threads.message_pb2
import yandex.cloud.ai.assistants.v1.threads.message_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class MessageServiceStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ai.assistants.v1.threads.message_service_pb2.CreateMessageRequest,
        yandex.cloud.ai.assistants.v1.threads.message_pb2.Message,
    ]

    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ai.assistants.v1.threads.message_service_pb2.GetMessageRequest,
        yandex.cloud.ai.assistants.v1.threads.message_pb2.Message,
    ]

    List: grpc.UnaryStreamMultiCallable[
        yandex.cloud.ai.assistants.v1.threads.message_service_pb2.ListMessagesRequest,
        yandex.cloud.ai.assistants.v1.threads.message_pb2.Message,
    ]

class MessageServiceAsyncStub:
    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.ai.assistants.v1.threads.message_service_pb2.CreateMessageRequest,
        yandex.cloud.ai.assistants.v1.threads.message_pb2.Message,
    ]

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.ai.assistants.v1.threads.message_service_pb2.GetMessageRequest,
        yandex.cloud.ai.assistants.v1.threads.message_pb2.Message,
    ]

    List: grpc.aio.UnaryStreamMultiCallable[
        yandex.cloud.ai.assistants.v1.threads.message_service_pb2.ListMessagesRequest,
        yandex.cloud.ai.assistants.v1.threads.message_pb2.Message,
    ]

class MessageServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.ai.assistants.v1.threads.message_service_pb2.CreateMessageRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.ai.assistants.v1.threads.message_pb2.Message, collections.abc.Awaitable[yandex.cloud.ai.assistants.v1.threads.message_pb2.Message]]: ...

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.ai.assistants.v1.threads.message_service_pb2.GetMessageRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.ai.assistants.v1.threads.message_pb2.Message, collections.abc.Awaitable[yandex.cloud.ai.assistants.v1.threads.message_pb2.Message]]: ...

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.ai.assistants.v1.threads.message_service_pb2.ListMessagesRequest,
        context: _ServicerContext,
    ) -> typing.Union[collections.abc.Iterator[yandex.cloud.ai.assistants.v1.threads.message_pb2.Message], collections.abc.AsyncIterator[yandex.cloud.ai.assistants.v1.threads.message_pb2.Message]]: ...

def add_MessageServiceServicer_to_server(servicer: MessageServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
