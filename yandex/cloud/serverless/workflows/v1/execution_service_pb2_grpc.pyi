"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.serverless.workflows.v1.execution_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class ExecutionServiceStub:
    """Set of methods for managing Workflows Executions."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Start: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.workflows.v1.execution_service_pb2.StartExecutionRequest,
        yandex.cloud.serverless.workflows.v1.execution_service_pb2.StartExecutionResponse,
    ]
    """Starts new Workflow execution."""

    Stop: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.workflows.v1.execution_service_pb2.StopExecutionRequest,
        yandex.cloud.serverless.workflows.v1.execution_service_pb2.StopExecutionResponse,
    ]
    """Stops specified Workflow execution."""

    Terminate: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.workflows.v1.execution_service_pb2.TerminateExecutionRequest,
        yandex.cloud.serverless.workflows.v1.execution_service_pb2.TerminateExecutionResponse,
    ]
    """Terminates specified Workflow execution."""

    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.workflows.v1.execution_service_pb2.GetExecutionRequest,
        yandex.cloud.serverless.workflows.v1.execution_service_pb2.GetExecutionResponse,
    ]
    """Retrieves specified Workflow execution."""

    GetHistory: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.workflows.v1.execution_service_pb2.GetExecutionHistoryRequest,
        yandex.cloud.serverless.workflows.v1.execution_service_pb2.GetExecutionHistoryResponse,
    ]
    """Retrieves detailed history of specified Workflow execution."""

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.workflows.v1.execution_service_pb2.ListExecutionsRequest,
        yandex.cloud.serverless.workflows.v1.execution_service_pb2.ListExecutionsResponse,
    ]
    """Retrieves list of Workflow executions."""

class ExecutionServiceAsyncStub:
    """Set of methods for managing Workflows Executions."""

    Start: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.workflows.v1.execution_service_pb2.StartExecutionRequest,
        yandex.cloud.serverless.workflows.v1.execution_service_pb2.StartExecutionResponse,
    ]
    """Starts new Workflow execution."""

    Stop: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.workflows.v1.execution_service_pb2.StopExecutionRequest,
        yandex.cloud.serverless.workflows.v1.execution_service_pb2.StopExecutionResponse,
    ]
    """Stops specified Workflow execution."""

    Terminate: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.workflows.v1.execution_service_pb2.TerminateExecutionRequest,
        yandex.cloud.serverless.workflows.v1.execution_service_pb2.TerminateExecutionResponse,
    ]
    """Terminates specified Workflow execution."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.workflows.v1.execution_service_pb2.GetExecutionRequest,
        yandex.cloud.serverless.workflows.v1.execution_service_pb2.GetExecutionResponse,
    ]
    """Retrieves specified Workflow execution."""

    GetHistory: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.workflows.v1.execution_service_pb2.GetExecutionHistoryRequest,
        yandex.cloud.serverless.workflows.v1.execution_service_pb2.GetExecutionHistoryResponse,
    ]
    """Retrieves detailed history of specified Workflow execution."""

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.workflows.v1.execution_service_pb2.ListExecutionsRequest,
        yandex.cloud.serverless.workflows.v1.execution_service_pb2.ListExecutionsResponse,
    ]
    """Retrieves list of Workflow executions."""

class ExecutionServiceServicer(metaclass=abc.ABCMeta):
    """Set of methods for managing Workflows Executions."""

    @abc.abstractmethod
    def Start(
        self,
        request: yandex.cloud.serverless.workflows.v1.execution_service_pb2.StartExecutionRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.serverless.workflows.v1.execution_service_pb2.StartExecutionResponse, collections.abc.Awaitable[yandex.cloud.serverless.workflows.v1.execution_service_pb2.StartExecutionResponse]]:
        """Starts new Workflow execution."""

    @abc.abstractmethod
    def Stop(
        self,
        request: yandex.cloud.serverless.workflows.v1.execution_service_pb2.StopExecutionRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.serverless.workflows.v1.execution_service_pb2.StopExecutionResponse, collections.abc.Awaitable[yandex.cloud.serverless.workflows.v1.execution_service_pb2.StopExecutionResponse]]:
        """Stops specified Workflow execution."""

    @abc.abstractmethod
    def Terminate(
        self,
        request: yandex.cloud.serverless.workflows.v1.execution_service_pb2.TerminateExecutionRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.serverless.workflows.v1.execution_service_pb2.TerminateExecutionResponse, collections.abc.Awaitable[yandex.cloud.serverless.workflows.v1.execution_service_pb2.TerminateExecutionResponse]]:
        """Terminates specified Workflow execution."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.serverless.workflows.v1.execution_service_pb2.GetExecutionRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.serverless.workflows.v1.execution_service_pb2.GetExecutionResponse, collections.abc.Awaitable[yandex.cloud.serverless.workflows.v1.execution_service_pb2.GetExecutionResponse]]:
        """Retrieves specified Workflow execution."""

    @abc.abstractmethod
    def GetHistory(
        self,
        request: yandex.cloud.serverless.workflows.v1.execution_service_pb2.GetExecutionHistoryRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.serverless.workflows.v1.execution_service_pb2.GetExecutionHistoryResponse, collections.abc.Awaitable[yandex.cloud.serverless.workflows.v1.execution_service_pb2.GetExecutionHistoryResponse]]:
        """Retrieves detailed history of specified Workflow execution."""

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.serverless.workflows.v1.execution_service_pb2.ListExecutionsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.serverless.workflows.v1.execution_service_pb2.ListExecutionsResponse, collections.abc.Awaitable[yandex.cloud.serverless.workflows.v1.execution_service_pb2.ListExecutionsResponse]]:
        """Retrieves list of Workflow executions."""

def add_ExecutionServiceServicer_to_server(servicer: ExecutionServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
