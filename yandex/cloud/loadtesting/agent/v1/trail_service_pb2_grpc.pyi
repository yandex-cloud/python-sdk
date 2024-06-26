"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.loadtesting.agent.v1.trail_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class TrailServiceStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.loadtesting.agent.v1.trail_service_pb2.CreateTrailRequest,
        yandex.cloud.loadtesting.agent.v1.trail_service_pb2.CreateTrailResponse,
    ]
    """Creates trail for specified job."""

class TrailServiceAsyncStub:
    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.loadtesting.agent.v1.trail_service_pb2.CreateTrailRequest,
        yandex.cloud.loadtesting.agent.v1.trail_service_pb2.CreateTrailResponse,
    ]
    """Creates trail for specified job."""

class TrailServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.loadtesting.agent.v1.trail_service_pb2.CreateTrailRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.loadtesting.agent.v1.trail_service_pb2.CreateTrailResponse, collections.abc.Awaitable[yandex.cloud.loadtesting.agent.v1.trail_service_pb2.CreateTrailResponse]]:
        """Creates trail for specified job."""

def add_TrailServiceServicer_to_server(servicer: TrailServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
