"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.monitoring.v3.dashboard_pb2
import yandex.cloud.monitoring.v3.dashboard_service_pb2
import yandex.cloud.operation.operation_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class DashboardServiceStub:
    """A set of methods for managing dashboards."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.monitoring.v3.dashboard_service_pb2.GetDashboardRequest,
        yandex.cloud.monitoring.v3.dashboard_pb2.Dashboard,
    ]
    """Returns the specified dashboard."""

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.monitoring.v3.dashboard_service_pb2.ListDashboardsRequest,
        yandex.cloud.monitoring.v3.dashboard_service_pb2.ListDashboardsResponse,
    ]
    """Retrieves the list of dashboards in the specified folder."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.monitoring.v3.dashboard_service_pb2.CreateDashboardRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a new dashboard in the specified folder."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.monitoring.v3.dashboard_service_pb2.UpdateDashboardRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified dashboard."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.monitoring.v3.dashboard_service_pb2.DeleteDashboardRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified dashboard."""

    ListOperations: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.monitoring.v3.dashboard_service_pb2.ListDashboardOperationsRequest,
        yandex.cloud.monitoring.v3.dashboard_service_pb2.ListDashboardOperationsResponse,
    ]
    """Lists operations for the specified dashboard."""

class DashboardServiceAsyncStub:
    """A set of methods for managing dashboards."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.monitoring.v3.dashboard_service_pb2.GetDashboardRequest,
        yandex.cloud.monitoring.v3.dashboard_pb2.Dashboard,
    ]
    """Returns the specified dashboard."""

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.monitoring.v3.dashboard_service_pb2.ListDashboardsRequest,
        yandex.cloud.monitoring.v3.dashboard_service_pb2.ListDashboardsResponse,
    ]
    """Retrieves the list of dashboards in the specified folder."""

    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.monitoring.v3.dashboard_service_pb2.CreateDashboardRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a new dashboard in the specified folder."""

    Update: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.monitoring.v3.dashboard_service_pb2.UpdateDashboardRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified dashboard."""

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.monitoring.v3.dashboard_service_pb2.DeleteDashboardRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified dashboard."""

    ListOperations: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.monitoring.v3.dashboard_service_pb2.ListDashboardOperationsRequest,
        yandex.cloud.monitoring.v3.dashboard_service_pb2.ListDashboardOperationsResponse,
    ]
    """Lists operations for the specified dashboard."""

class DashboardServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing dashboards."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.monitoring.v3.dashboard_service_pb2.GetDashboardRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.monitoring.v3.dashboard_pb2.Dashboard, collections.abc.Awaitable[yandex.cloud.monitoring.v3.dashboard_pb2.Dashboard]]:
        """Returns the specified dashboard."""

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.monitoring.v3.dashboard_service_pb2.ListDashboardsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.monitoring.v3.dashboard_service_pb2.ListDashboardsResponse, collections.abc.Awaitable[yandex.cloud.monitoring.v3.dashboard_service_pb2.ListDashboardsResponse]]:
        """Retrieves the list of dashboards in the specified folder."""

    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.monitoring.v3.dashboard_service_pb2.CreateDashboardRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates a new dashboard in the specified folder."""

    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.monitoring.v3.dashboard_service_pb2.UpdateDashboardRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates the specified dashboard."""

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.monitoring.v3.dashboard_service_pb2.DeleteDashboardRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deletes the specified dashboard."""

    @abc.abstractmethod
    def ListOperations(
        self,
        request: yandex.cloud.monitoring.v3.dashboard_service_pb2.ListDashboardOperationsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.monitoring.v3.dashboard_service_pb2.ListDashboardOperationsResponse, collections.abc.Awaitable[yandex.cloud.monitoring.v3.dashboard_service_pb2.ListDashboardOperationsResponse]]:
        """Lists operations for the specified dashboard."""

def add_DashboardServiceServicer_to_server(servicer: DashboardServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
