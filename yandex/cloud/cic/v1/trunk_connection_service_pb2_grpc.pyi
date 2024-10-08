"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.cic.v1.trunk_connection_pb2
import yandex.cloud.cic.v1.trunk_connection_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class TrunkConnectionServiceStub:
    """A set of methods for managing TrunkConnection resources."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.cic.v1.trunk_connection_service_pb2.GetTrunkConnectionRequest,
        yandex.cloud.cic.v1.trunk_connection_pb2.TrunkConnection,
    ]
    """Returns the specified TrunkConnection resource.

    To get the list of available TrunkConnection resources, make a [List] request.
    """

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.cic.v1.trunk_connection_service_pb2.ListTrunkConnectionsRequest,
        yandex.cloud.cic.v1.trunk_connection_service_pb2.ListTrunkConnectionsResponse,
    ]
    """Retrieves the list of TrunkConnection resources in the specified folder."""

class TrunkConnectionServiceAsyncStub:
    """A set of methods for managing TrunkConnection resources."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.cic.v1.trunk_connection_service_pb2.GetTrunkConnectionRequest,
        yandex.cloud.cic.v1.trunk_connection_pb2.TrunkConnection,
    ]
    """Returns the specified TrunkConnection resource.

    To get the list of available TrunkConnection resources, make a [List] request.
    """

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.cic.v1.trunk_connection_service_pb2.ListTrunkConnectionsRequest,
        yandex.cloud.cic.v1.trunk_connection_service_pb2.ListTrunkConnectionsResponse,
    ]
    """Retrieves the list of TrunkConnection resources in the specified folder."""

class TrunkConnectionServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing TrunkConnection resources."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.cic.v1.trunk_connection_service_pb2.GetTrunkConnectionRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.cic.v1.trunk_connection_pb2.TrunkConnection, collections.abc.Awaitable[yandex.cloud.cic.v1.trunk_connection_pb2.TrunkConnection]]:
        """Returns the specified TrunkConnection resource.

        To get the list of available TrunkConnection resources, make a [List] request.
        """

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.cic.v1.trunk_connection_service_pb2.ListTrunkConnectionsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.cic.v1.trunk_connection_service_pb2.ListTrunkConnectionsResponse, collections.abc.Awaitable[yandex.cloud.cic.v1.trunk_connection_service_pb2.ListTrunkConnectionsResponse]]:
        """Retrieves the list of TrunkConnection resources in the specified folder."""

def add_TrunkConnectionServiceServicer_to_server(servicer: TrunkConnectionServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
