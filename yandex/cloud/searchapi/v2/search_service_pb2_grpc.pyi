"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.operation.operation_pb2
import yandex.cloud.searchapi.v2.search_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class WebSearchAsyncServiceStub:
    """A set of methods for async search the Yandex search database."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Search: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.searchapi.v2.search_service_pb2.WebSearchRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]

class WebSearchAsyncServiceAsyncStub:
    """A set of methods for async search the Yandex search database."""

    Search: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.searchapi.v2.search_service_pb2.WebSearchRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]

class WebSearchAsyncServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for async search the Yandex search database."""

    @abc.abstractmethod
    def Search(
        self,
        request: yandex.cloud.searchapi.v2.search_service_pb2.WebSearchRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]: ...

def add_WebSearchAsyncServiceServicer_to_server(servicer: WebSearchAsyncServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...

class WebSearchServiceStub:
    """A set of methods for searching the Yandex search database."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Search: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.searchapi.v2.search_service_pb2.WebSearchRequest,
        yandex.cloud.searchapi.v2.search_service_pb2.WebSearchResponse,
    ]

class WebSearchServiceAsyncStub:
    """A set of methods for searching the Yandex search database."""

    Search: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.searchapi.v2.search_service_pb2.WebSearchRequest,
        yandex.cloud.searchapi.v2.search_service_pb2.WebSearchResponse,
    ]

class WebSearchServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for searching the Yandex search database."""

    @abc.abstractmethod
    def Search(
        self,
        request: yandex.cloud.searchapi.v2.search_service_pb2.WebSearchRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.searchapi.v2.search_service_pb2.WebSearchResponse, collections.abc.Awaitable[yandex.cloud.searchapi.v2.search_service_pb2.WebSearchResponse]]: ...

def add_WebSearchServiceServicer_to_server(servicer: WebSearchServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
