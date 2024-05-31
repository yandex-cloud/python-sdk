"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.mdb.kafka.v1.connector_pb2
import yandex.cloud.mdb.kafka.v1.connector_service_pb2
import yandex.cloud.operation.operation_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class ConnectorServiceStub:
    """A set of methods for managing Apache Kafka® connectors."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.connector_service_pb2.GetConnectorRequest,
        yandex.cloud.mdb.kafka.v1.connector_pb2.Connector,
    ]
    """Returns information about an Apache Kafka® connector."""

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.connector_service_pb2.ListConnectorsRequest,
        yandex.cloud.mdb.kafka.v1.connector_service_pb2.ListConnectorsResponse,
    ]
    """Retrieves the list of Apache Kafka® connectors in a cluster."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.connector_service_pb2.CreateConnectorRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a new Apache Kafka® connector in a cluster."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.connector_service_pb2.UpdateConnectorRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates an Apache Kafka® connector."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.connector_service_pb2.DeleteConnectorRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes an Apache Kafka® connector."""

    Resume: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.connector_service_pb2.ResumeConnectorRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Resumes an Apache Kafka® connector."""

    Pause: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.connector_service_pb2.PauseConnectorRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Pauses an Apache Kafka® connector."""

class ConnectorServiceAsyncStub:
    """A set of methods for managing Apache Kafka® connectors."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.connector_service_pb2.GetConnectorRequest,
        yandex.cloud.mdb.kafka.v1.connector_pb2.Connector,
    ]
    """Returns information about an Apache Kafka® connector."""

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.connector_service_pb2.ListConnectorsRequest,
        yandex.cloud.mdb.kafka.v1.connector_service_pb2.ListConnectorsResponse,
    ]
    """Retrieves the list of Apache Kafka® connectors in a cluster."""

    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.connector_service_pb2.CreateConnectorRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a new Apache Kafka® connector in a cluster."""

    Update: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.connector_service_pb2.UpdateConnectorRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates an Apache Kafka® connector."""

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.connector_service_pb2.DeleteConnectorRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes an Apache Kafka® connector."""

    Resume: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.connector_service_pb2.ResumeConnectorRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Resumes an Apache Kafka® connector."""

    Pause: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.kafka.v1.connector_service_pb2.PauseConnectorRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Pauses an Apache Kafka® connector."""

class ConnectorServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing Apache Kafka® connectors."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.mdb.kafka.v1.connector_service_pb2.GetConnectorRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.kafka.v1.connector_pb2.Connector, collections.abc.Awaitable[yandex.cloud.mdb.kafka.v1.connector_pb2.Connector]]:
        """Returns information about an Apache Kafka® connector."""

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.mdb.kafka.v1.connector_service_pb2.ListConnectorsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.kafka.v1.connector_service_pb2.ListConnectorsResponse, collections.abc.Awaitable[yandex.cloud.mdb.kafka.v1.connector_service_pb2.ListConnectorsResponse]]:
        """Retrieves the list of Apache Kafka® connectors in a cluster."""

    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.mdb.kafka.v1.connector_service_pb2.CreateConnectorRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates a new Apache Kafka® connector in a cluster."""

    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.mdb.kafka.v1.connector_service_pb2.UpdateConnectorRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates an Apache Kafka® connector."""

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.mdb.kafka.v1.connector_service_pb2.DeleteConnectorRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deletes an Apache Kafka® connector."""

    @abc.abstractmethod
    def Resume(
        self,
        request: yandex.cloud.mdb.kafka.v1.connector_service_pb2.ResumeConnectorRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Resumes an Apache Kafka® connector."""

    @abc.abstractmethod
    def Pause(
        self,
        request: yandex.cloud.mdb.kafka.v1.connector_service_pb2.PauseConnectorRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Pauses an Apache Kafka® connector."""

def add_ConnectorServiceServicer_to_server(servicer: ConnectorServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
