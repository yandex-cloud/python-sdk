"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import google.protobuf.empty_pb2
import grpc
import grpc.aio
import typing
import yandex.cloud.datasphere.v1.folder_budget_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class FolderBudgetServiceStub:
    """A set of methods for managing Datasphere folder budgets."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v1.folder_budget_service_pb2.GetFolderBudgetRequest,
        yandex.cloud.datasphere.v1.folder_budget_service_pb2.GetFolderBudgetResponse,
    ]
    """Returns the specified folder budget."""

    Set: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v1.folder_budget_service_pb2.SetFolderBudgetRequest,
        google.protobuf.empty_pb2.Empty,
    ]
    """Sets the unit balance and the limits of the specified folder budget."""

class FolderBudgetServiceAsyncStub:
    """A set of methods for managing Datasphere folder budgets."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v1.folder_budget_service_pb2.GetFolderBudgetRequest,
        yandex.cloud.datasphere.v1.folder_budget_service_pb2.GetFolderBudgetResponse,
    ]
    """Returns the specified folder budget."""

    Set: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v1.folder_budget_service_pb2.SetFolderBudgetRequest,
        google.protobuf.empty_pb2.Empty,
    ]
    """Sets the unit balance and the limits of the specified folder budget."""

class FolderBudgetServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing Datasphere folder budgets."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.datasphere.v1.folder_budget_service_pb2.GetFolderBudgetRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.datasphere.v1.folder_budget_service_pb2.GetFolderBudgetResponse, collections.abc.Awaitable[yandex.cloud.datasphere.v1.folder_budget_service_pb2.GetFolderBudgetResponse]]:
        """Returns the specified folder budget."""

    @abc.abstractmethod
    def Set(
        self,
        request: yandex.cloud.datasphere.v1.folder_budget_service_pb2.SetFolderBudgetRequest,
        context: _ServicerContext,
    ) -> typing.Union[google.protobuf.empty_pb2.Empty, collections.abc.Awaitable[google.protobuf.empty_pb2.Empty]]:
        """Sets the unit balance and the limits of the specified folder budget."""

def add_FolderBudgetServiceServicer_to_server(servicer: FolderBudgetServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
