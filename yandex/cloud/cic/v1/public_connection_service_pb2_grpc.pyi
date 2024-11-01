"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.cic.v1.public_connection_pb2
import yandex.cloud.cic.v1.public_connection_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class PublicConnectionServiceStub:
    """A set of methods for managing PublicConnection resources."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.cic.v1.public_connection_service_pb2.GetPublicConnectionRequest,
        yandex.cloud.cic.v1.public_connection_pb2.PublicConnection,
    ]
    """Returns the specified PublicConnection resource.

    To get the list of available PublicConnection resources, make a [List] request.
    """

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.cic.v1.public_connection_service_pb2.ListPublicConnectionsRequest,
        yandex.cloud.cic.v1.public_connection_service_pb2.ListPublicConnectionsResponse,
    ]
    """Retrieves the list of PublicConnection resources in the specified folder."""

class PublicConnectionServiceAsyncStub:
    """A set of methods for managing PublicConnection resources."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.cic.v1.public_connection_service_pb2.GetPublicConnectionRequest,
        yandex.cloud.cic.v1.public_connection_pb2.PublicConnection,
    ]
    """Returns the specified PublicConnection resource.

    To get the list of available PublicConnection resources, make a [List] request.
    """

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.cic.v1.public_connection_service_pb2.ListPublicConnectionsRequest,
        yandex.cloud.cic.v1.public_connection_service_pb2.ListPublicConnectionsResponse,
    ]
    """Retrieves the list of PublicConnection resources in the specified folder."""

class PublicConnectionServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing PublicConnection resources."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.cic.v1.public_connection_service_pb2.GetPublicConnectionRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.cic.v1.public_connection_pb2.PublicConnection, collections.abc.Awaitable[yandex.cloud.cic.v1.public_connection_pb2.PublicConnection]]:
        """Returns the specified PublicConnection resource.

        To get the list of available PublicConnection resources, make a [List] request.
        """

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.cic.v1.public_connection_service_pb2.ListPublicConnectionsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.cic.v1.public_connection_service_pb2.ListPublicConnectionsResponse, collections.abc.Awaitable[yandex.cloud.cic.v1.public_connection_service_pb2.ListPublicConnectionsResponse]]:
        """Retrieves the list of PublicConnection resources in the specified folder."""

def add_PublicConnectionServiceServicer_to_server(servicer: PublicConnectionServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...