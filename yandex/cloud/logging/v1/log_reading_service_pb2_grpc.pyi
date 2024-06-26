"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.logging.v1.log_reading_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class LogReadingServiceStub:
    """A set of methods for reading from log groups."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Read: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.logging.v1.log_reading_service_pb2.ReadRequest,
        yandex.cloud.logging.v1.log_reading_service_pb2.ReadResponse,
    ]
    """Read log entries from the specified log group."""

class LogReadingServiceAsyncStub:
    """A set of methods for reading from log groups."""

    Read: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.logging.v1.log_reading_service_pb2.ReadRequest,
        yandex.cloud.logging.v1.log_reading_service_pb2.ReadResponse,
    ]
    """Read log entries from the specified log group."""

class LogReadingServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for reading from log groups."""

    @abc.abstractmethod
    def Read(
        self,
        request: yandex.cloud.logging.v1.log_reading_service_pb2.ReadRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.logging.v1.log_reading_service_pb2.ReadResponse, collections.abc.Awaitable[yandex.cloud.logging.v1.log_reading_service_pb2.ReadResponse]]:
        """Read log entries from the specified log group."""

def add_LogReadingServiceServicer_to_server(servicer: LogReadingServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
