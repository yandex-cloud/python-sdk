"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.billing.v1.service_pb2
import yandex.cloud.billing.v1.service_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class ServiceServiceStub:
    """A set of methods for managing Service resources."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.billing.v1.service_service_pb2.GetServiceRequest,
        yandex.cloud.billing.v1.service_pb2.Service,
    ]
    """Returns the specified service."""

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.billing.v1.service_service_pb2.ListServicesRequest,
        yandex.cloud.billing.v1.service_service_pb2.ListServicesResponse,
    ]
    """Retrieves the list of services."""

class ServiceServiceAsyncStub:
    """A set of methods for managing Service resources."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.billing.v1.service_service_pb2.GetServiceRequest,
        yandex.cloud.billing.v1.service_pb2.Service,
    ]
    """Returns the specified service."""

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.billing.v1.service_service_pb2.ListServicesRequest,
        yandex.cloud.billing.v1.service_service_pb2.ListServicesResponse,
    ]
    """Retrieves the list of services."""

class ServiceServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing Service resources."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.billing.v1.service_service_pb2.GetServiceRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.billing.v1.service_pb2.Service, collections.abc.Awaitable[yandex.cloud.billing.v1.service_pb2.Service]]:
        """Returns the specified service."""

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.billing.v1.service_service_pb2.ListServicesRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.billing.v1.service_service_pb2.ListServicesResponse, collections.abc.Awaitable[yandex.cloud.billing.v1.service_service_pb2.ListServicesResponse]]:
        """Retrieves the list of services."""

def add_ServiceServiceServicer_to_server(servicer: ServiceServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
