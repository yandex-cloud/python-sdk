"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.cloudrouter.v1.routing_instance_pb2
import yandex.cloud.cloudrouter.v1.routing_instance_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class RoutingInstanceServiceStub:
    """A set of methods for managing RoutingInstance resources."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.cloudrouter.v1.routing_instance_service_pb2.GetRoutingInstanceRequest,
        yandex.cloud.cloudrouter.v1.routing_instance_pb2.RoutingInstance,
    ]
    """Returns the specified RoutingInstance resource.

    To get the list of available RoutingInstance resources, make a [List] request.
    """

    GetByVpcNetworkId: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.cloudrouter.v1.routing_instance_service_pb2.GetRoutingInstanceByVpcNetworkIdRequest,
        yandex.cloud.cloudrouter.v1.routing_instance_pb2.RoutingInstance,
    ]
    """Returns the RoutingInstance resource by vpcNetworkId

    To get the list of available RoutingInstance resources, make a [List] request.
    """

    GetByCicPrivateConnectionId: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.cloudrouter.v1.routing_instance_service_pb2.GetRoutingInstanceByCicPrivateConnectionIdRequest,
        yandex.cloud.cloudrouter.v1.routing_instance_pb2.RoutingInstance,
    ]
    """Returns the RoutingInstance resource by cicPrivateConnectionId

    To get the list of available RoutingInstance resources, make a [List] request.
    """

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.cloudrouter.v1.routing_instance_service_pb2.ListRoutingInstancesRequest,
        yandex.cloud.cloudrouter.v1.routing_instance_service_pb2.ListRoutingInstancesResponse,
    ]
    """Retrieves the list of RoutingInstance resources in the specified folder."""

class RoutingInstanceServiceAsyncStub:
    """A set of methods for managing RoutingInstance resources."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.cloudrouter.v1.routing_instance_service_pb2.GetRoutingInstanceRequest,
        yandex.cloud.cloudrouter.v1.routing_instance_pb2.RoutingInstance,
    ]
    """Returns the specified RoutingInstance resource.

    To get the list of available RoutingInstance resources, make a [List] request.
    """

    GetByVpcNetworkId: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.cloudrouter.v1.routing_instance_service_pb2.GetRoutingInstanceByVpcNetworkIdRequest,
        yandex.cloud.cloudrouter.v1.routing_instance_pb2.RoutingInstance,
    ]
    """Returns the RoutingInstance resource by vpcNetworkId

    To get the list of available RoutingInstance resources, make a [List] request.
    """

    GetByCicPrivateConnectionId: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.cloudrouter.v1.routing_instance_service_pb2.GetRoutingInstanceByCicPrivateConnectionIdRequest,
        yandex.cloud.cloudrouter.v1.routing_instance_pb2.RoutingInstance,
    ]
    """Returns the RoutingInstance resource by cicPrivateConnectionId

    To get the list of available RoutingInstance resources, make a [List] request.
    """

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.cloudrouter.v1.routing_instance_service_pb2.ListRoutingInstancesRequest,
        yandex.cloud.cloudrouter.v1.routing_instance_service_pb2.ListRoutingInstancesResponse,
    ]
    """Retrieves the list of RoutingInstance resources in the specified folder."""

class RoutingInstanceServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing RoutingInstance resources."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.cloudrouter.v1.routing_instance_service_pb2.GetRoutingInstanceRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.cloudrouter.v1.routing_instance_pb2.RoutingInstance, collections.abc.Awaitable[yandex.cloud.cloudrouter.v1.routing_instance_pb2.RoutingInstance]]:
        """Returns the specified RoutingInstance resource.

        To get the list of available RoutingInstance resources, make a [List] request.
        """

    @abc.abstractmethod
    def GetByVpcNetworkId(
        self,
        request: yandex.cloud.cloudrouter.v1.routing_instance_service_pb2.GetRoutingInstanceByVpcNetworkIdRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.cloudrouter.v1.routing_instance_pb2.RoutingInstance, collections.abc.Awaitable[yandex.cloud.cloudrouter.v1.routing_instance_pb2.RoutingInstance]]:
        """Returns the RoutingInstance resource by vpcNetworkId

        To get the list of available RoutingInstance resources, make a [List] request.
        """

    @abc.abstractmethod
    def GetByCicPrivateConnectionId(
        self,
        request: yandex.cloud.cloudrouter.v1.routing_instance_service_pb2.GetRoutingInstanceByCicPrivateConnectionIdRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.cloudrouter.v1.routing_instance_pb2.RoutingInstance, collections.abc.Awaitable[yandex.cloud.cloudrouter.v1.routing_instance_pb2.RoutingInstance]]:
        """Returns the RoutingInstance resource by cicPrivateConnectionId

        To get the list of available RoutingInstance resources, make a [List] request.
        """

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.cloudrouter.v1.routing_instance_service_pb2.ListRoutingInstancesRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.cloudrouter.v1.routing_instance_service_pb2.ListRoutingInstancesResponse, collections.abc.Awaitable[yandex.cloud.cloudrouter.v1.routing_instance_service_pb2.ListRoutingInstancesResponse]]:
        """Retrieves the list of RoutingInstance resources in the specified folder."""

def add_RoutingInstanceServiceServicer_to_server(servicer: RoutingInstanceServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
