"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.ai.assistants.v1.runs.run_pb2
import yandex.cloud.ai.assistants.v1.runs.run_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class RunServiceStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ai.assistants.v1.runs.run_service_pb2.CreateRunRequest,
        yandex.cloud.ai.assistants.v1.runs.run_pb2.Run,
    ]

    Listen: grpc.UnaryStreamMultiCallable[
        yandex.cloud.ai.assistants.v1.runs.run_service_pb2.ListenRunRequest,
        yandex.cloud.ai.assistants.v1.runs.run_service_pb2.StreamEvent,
    ]

    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ai.assistants.v1.runs.run_service_pb2.GetRunRequest,
        yandex.cloud.ai.assistants.v1.runs.run_pb2.Run,
    ]

    GetLastByThread: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ai.assistants.v1.runs.run_service_pb2.GetLastRunByThreadRequest,
        yandex.cloud.ai.assistants.v1.runs.run_pb2.Run,
    ]

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ai.assistants.v1.runs.run_service_pb2.ListRunsRequest,
        yandex.cloud.ai.assistants.v1.runs.run_service_pb2.ListRunsResponse,
    ]

class RunServiceAsyncStub:
    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.ai.assistants.v1.runs.run_service_pb2.CreateRunRequest,
        yandex.cloud.ai.assistants.v1.runs.run_pb2.Run,
    ]

    Listen: grpc.aio.UnaryStreamMultiCallable[
        yandex.cloud.ai.assistants.v1.runs.run_service_pb2.ListenRunRequest,
        yandex.cloud.ai.assistants.v1.runs.run_service_pb2.StreamEvent,
    ]

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.ai.assistants.v1.runs.run_service_pb2.GetRunRequest,
        yandex.cloud.ai.assistants.v1.runs.run_pb2.Run,
    ]

    GetLastByThread: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.ai.assistants.v1.runs.run_service_pb2.GetLastRunByThreadRequest,
        yandex.cloud.ai.assistants.v1.runs.run_pb2.Run,
    ]

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.ai.assistants.v1.runs.run_service_pb2.ListRunsRequest,
        yandex.cloud.ai.assistants.v1.runs.run_service_pb2.ListRunsResponse,
    ]

class RunServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.ai.assistants.v1.runs.run_service_pb2.CreateRunRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.ai.assistants.v1.runs.run_pb2.Run, collections.abc.Awaitable[yandex.cloud.ai.assistants.v1.runs.run_pb2.Run]]: ...

    @abc.abstractmethod
    def Listen(
        self,
        request: yandex.cloud.ai.assistants.v1.runs.run_service_pb2.ListenRunRequest,
        context: _ServicerContext,
    ) -> typing.Union[collections.abc.Iterator[yandex.cloud.ai.assistants.v1.runs.run_service_pb2.StreamEvent], collections.abc.AsyncIterator[yandex.cloud.ai.assistants.v1.runs.run_service_pb2.StreamEvent]]: ...

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.ai.assistants.v1.runs.run_service_pb2.GetRunRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.ai.assistants.v1.runs.run_pb2.Run, collections.abc.Awaitable[yandex.cloud.ai.assistants.v1.runs.run_pb2.Run]]: ...

    @abc.abstractmethod
    def GetLastByThread(
        self,
        request: yandex.cloud.ai.assistants.v1.runs.run_service_pb2.GetLastRunByThreadRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.ai.assistants.v1.runs.run_pb2.Run, collections.abc.Awaitable[yandex.cloud.ai.assistants.v1.runs.run_pb2.Run]]: ...

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.ai.assistants.v1.runs.run_service_pb2.ListRunsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.ai.assistants.v1.runs.run_service_pb2.ListRunsResponse, collections.abc.Awaitable[yandex.cloud.ai.assistants.v1.runs.run_service_pb2.ListRunsResponse]]: ...

def add_RunServiceServicer_to_server(servicer: RunServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
