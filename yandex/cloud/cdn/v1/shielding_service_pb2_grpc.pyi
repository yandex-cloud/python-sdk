"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.cdn.v1.shielding_pb2
import yandex.cloud.cdn.v1.shielding_service_pb2
import yandex.cloud.operation.operation_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class ShieldingServiceStub:
    """Shielding management service."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Activate: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.cdn.v1.shielding_service_pb2.ActivateShieldingRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Activate shielding for a resource."""

    Deactivate: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.cdn.v1.shielding_service_pb2.DeactivateShieldingRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deactivate shielding for a resource."""

    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.cdn.v1.shielding_service_pb2.GetShieldingDetailsRequest,
        yandex.cloud.cdn.v1.shielding_pb2.ShieldingDetails,
    ]
    """Get shielding details by resource ID."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.cdn.v1.shielding_service_pb2.UpdateShieldingRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates shielding parameters for a resource, such as changing the geographical location of the shielding server.
    Changes may take up to 15 minutes to propagate across CDN servers.
    After updating, it is recommended to purge the resource's cache.
    """

    ListAvailableLocations: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.cdn.v1.shielding_service_pb2.ListShieldingLocationsRequest,
        yandex.cloud.cdn.v1.shielding_service_pb2.ListShieldingLocationsResponse,
    ]
    """Lists available geographical locations."""

class ShieldingServiceAsyncStub:
    """Shielding management service."""

    Activate: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.cdn.v1.shielding_service_pb2.ActivateShieldingRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Activate shielding for a resource."""

    Deactivate: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.cdn.v1.shielding_service_pb2.DeactivateShieldingRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deactivate shielding for a resource."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.cdn.v1.shielding_service_pb2.GetShieldingDetailsRequest,
        yandex.cloud.cdn.v1.shielding_pb2.ShieldingDetails,
    ]
    """Get shielding details by resource ID."""

    Update: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.cdn.v1.shielding_service_pb2.UpdateShieldingRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates shielding parameters for a resource, such as changing the geographical location of the shielding server.
    Changes may take up to 15 minutes to propagate across CDN servers.
    After updating, it is recommended to purge the resource's cache.
    """

    ListAvailableLocations: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.cdn.v1.shielding_service_pb2.ListShieldingLocationsRequest,
        yandex.cloud.cdn.v1.shielding_service_pb2.ListShieldingLocationsResponse,
    ]
    """Lists available geographical locations."""

class ShieldingServiceServicer(metaclass=abc.ABCMeta):
    """Shielding management service."""

    @abc.abstractmethod
    def Activate(
        self,
        request: yandex.cloud.cdn.v1.shielding_service_pb2.ActivateShieldingRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Activate shielding for a resource."""

    @abc.abstractmethod
    def Deactivate(
        self,
        request: yandex.cloud.cdn.v1.shielding_service_pb2.DeactivateShieldingRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deactivate shielding for a resource."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.cdn.v1.shielding_service_pb2.GetShieldingDetailsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.cdn.v1.shielding_pb2.ShieldingDetails, collections.abc.Awaitable[yandex.cloud.cdn.v1.shielding_pb2.ShieldingDetails]]:
        """Get shielding details by resource ID."""

    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.cdn.v1.shielding_service_pb2.UpdateShieldingRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates shielding parameters for a resource, such as changing the geographical location of the shielding server.
        Changes may take up to 15 minutes to propagate across CDN servers.
        After updating, it is recommended to purge the resource's cache.
        """

    @abc.abstractmethod
    def ListAvailableLocations(
        self,
        request: yandex.cloud.cdn.v1.shielding_service_pb2.ListShieldingLocationsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.cdn.v1.shielding_service_pb2.ListShieldingLocationsResponse, collections.abc.Awaitable[yandex.cloud.cdn.v1.shielding_service_pb2.ListShieldingLocationsResponse]]:
        """Lists available geographical locations."""

def add_ShieldingServiceServicer_to_server(servicer: ShieldingServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
