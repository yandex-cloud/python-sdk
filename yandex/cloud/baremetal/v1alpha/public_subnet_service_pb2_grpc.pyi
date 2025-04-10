"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.baremetal.v1alpha.public_subnet_pb2
import yandex.cloud.baremetal.v1alpha.public_subnet_service_pb2
import yandex.cloud.operation.operation_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class PublicSubnetServiceStub:
    """A set of methods for managing PublicSubnet resources."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.baremetal.v1alpha.public_subnet_service_pb2.GetPublicSubnetRequest,
        yandex.cloud.baremetal.v1alpha.public_subnet_pb2.PublicSubnet,
    ]
    """Returns the specific PublicSubnet resource.

    To get the list of available PublicSubnet resources, make a [List] request.
    """

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.baremetal.v1alpha.public_subnet_service_pb2.ListPublicSubnetRequest,
        yandex.cloud.baremetal.v1alpha.public_subnet_service_pb2.ListPublicSubnetResponse,
    ]
    """Retrieves the list of PublicSubnet resources in the specified folder."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.baremetal.v1alpha.public_subnet_service_pb2.CreatePublicSubnetRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a public subnet in the specified folder."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.baremetal.v1alpha.public_subnet_service_pb2.UpdatePublicSubnetRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified public subnet."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.baremetal.v1alpha.public_subnet_service_pb2.DeletePublicSubnetRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified public subnet.

    Deleting a public subnet removes its data permanently and is irreversible.
    """

    ListOperations: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.baremetal.v1alpha.public_subnet_service_pb2.ListPublicSubnetOperationsRequest,
        yandex.cloud.baremetal.v1alpha.public_subnet_service_pb2.ListPublicSubnetOperationsResponse,
    ]
    """Lists operations for the specified public subnet."""

class PublicSubnetServiceAsyncStub:
    """A set of methods for managing PublicSubnet resources."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.baremetal.v1alpha.public_subnet_service_pb2.GetPublicSubnetRequest,
        yandex.cloud.baremetal.v1alpha.public_subnet_pb2.PublicSubnet,
    ]
    """Returns the specific PublicSubnet resource.

    To get the list of available PublicSubnet resources, make a [List] request.
    """

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.baremetal.v1alpha.public_subnet_service_pb2.ListPublicSubnetRequest,
        yandex.cloud.baremetal.v1alpha.public_subnet_service_pb2.ListPublicSubnetResponse,
    ]
    """Retrieves the list of PublicSubnet resources in the specified folder."""

    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.baremetal.v1alpha.public_subnet_service_pb2.CreatePublicSubnetRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a public subnet in the specified folder."""

    Update: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.baremetal.v1alpha.public_subnet_service_pb2.UpdatePublicSubnetRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified public subnet."""

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.baremetal.v1alpha.public_subnet_service_pb2.DeletePublicSubnetRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified public subnet.

    Deleting a public subnet removes its data permanently and is irreversible.
    """

    ListOperations: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.baremetal.v1alpha.public_subnet_service_pb2.ListPublicSubnetOperationsRequest,
        yandex.cloud.baremetal.v1alpha.public_subnet_service_pb2.ListPublicSubnetOperationsResponse,
    ]
    """Lists operations for the specified public subnet."""

class PublicSubnetServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing PublicSubnet resources."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.baremetal.v1alpha.public_subnet_service_pb2.GetPublicSubnetRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.baremetal.v1alpha.public_subnet_pb2.PublicSubnet, collections.abc.Awaitable[yandex.cloud.baremetal.v1alpha.public_subnet_pb2.PublicSubnet]]:
        """Returns the specific PublicSubnet resource.

        To get the list of available PublicSubnet resources, make a [List] request.
        """

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.baremetal.v1alpha.public_subnet_service_pb2.ListPublicSubnetRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.baremetal.v1alpha.public_subnet_service_pb2.ListPublicSubnetResponse, collections.abc.Awaitable[yandex.cloud.baremetal.v1alpha.public_subnet_service_pb2.ListPublicSubnetResponse]]:
        """Retrieves the list of PublicSubnet resources in the specified folder."""

    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.baremetal.v1alpha.public_subnet_service_pb2.CreatePublicSubnetRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates a public subnet in the specified folder."""

    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.baremetal.v1alpha.public_subnet_service_pb2.UpdatePublicSubnetRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates the specified public subnet."""

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.baremetal.v1alpha.public_subnet_service_pb2.DeletePublicSubnetRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deletes the specified public subnet.

        Deleting a public subnet removes its data permanently and is irreversible.
        """

    @abc.abstractmethod
    def ListOperations(
        self,
        request: yandex.cloud.baremetal.v1alpha.public_subnet_service_pb2.ListPublicSubnetOperationsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.baremetal.v1alpha.public_subnet_service_pb2.ListPublicSubnetOperationsResponse, collections.abc.Awaitable[yandex.cloud.baremetal.v1alpha.public_subnet_service_pb2.ListPublicSubnetOperationsResponse]]:
        """Lists operations for the specified public subnet."""

def add_PublicSubnetServiceServicer_to_server(servicer: PublicSubnetServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
