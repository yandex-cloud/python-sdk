"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.baremetal.v1alpha.vrf_pb2
import yandex.cloud.baremetal.v1alpha.vrf_service_pb2
import yandex.cloud.operation.operation_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class VrfServiceStub:
    """A set of methods for managing VRF resources."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.baremetal.v1alpha.vrf_service_pb2.GetVrfRequest,
        yandex.cloud.baremetal.v1alpha.vrf_pb2.Vrf,
    ]
    """Returns the specific VRF resource.

    To get the list of available VRFs, make a [List] request.
    """

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.baremetal.v1alpha.vrf_service_pb2.ListVrfRequest,
        yandex.cloud.baremetal.v1alpha.vrf_service_pb2.ListVrfResponse,
    ]
    """Retrieves the list of VRF resources in the specified folder."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.baremetal.v1alpha.vrf_service_pb2.CreateVrfRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a VRF in the specified folder."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.baremetal.v1alpha.vrf_service_pb2.UpdateVrfRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified VRF resource."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.baremetal.v1alpha.vrf_service_pb2.DeleteVrfRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified VRF resource.

    Deleting a VRF removes its data permanently and is irreversible.
    """

    ListOperations: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.baremetal.v1alpha.vrf_service_pb2.ListVrfOperationsRequest,
        yandex.cloud.baremetal.v1alpha.vrf_service_pb2.ListVrfOperationsResponse,
    ]
    """Lists operations for the specified VRF."""

class VrfServiceAsyncStub:
    """A set of methods for managing VRF resources."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.baremetal.v1alpha.vrf_service_pb2.GetVrfRequest,
        yandex.cloud.baremetal.v1alpha.vrf_pb2.Vrf,
    ]
    """Returns the specific VRF resource.

    To get the list of available VRFs, make a [List] request.
    """

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.baremetal.v1alpha.vrf_service_pb2.ListVrfRequest,
        yandex.cloud.baremetal.v1alpha.vrf_service_pb2.ListVrfResponse,
    ]
    """Retrieves the list of VRF resources in the specified folder."""

    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.baremetal.v1alpha.vrf_service_pb2.CreateVrfRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a VRF in the specified folder."""

    Update: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.baremetal.v1alpha.vrf_service_pb2.UpdateVrfRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified VRF resource."""

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.baremetal.v1alpha.vrf_service_pb2.DeleteVrfRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified VRF resource.

    Deleting a VRF removes its data permanently and is irreversible.
    """

    ListOperations: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.baremetal.v1alpha.vrf_service_pb2.ListVrfOperationsRequest,
        yandex.cloud.baremetal.v1alpha.vrf_service_pb2.ListVrfOperationsResponse,
    ]
    """Lists operations for the specified VRF."""

class VrfServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing VRF resources."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.baremetal.v1alpha.vrf_service_pb2.GetVrfRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.baremetal.v1alpha.vrf_pb2.Vrf, collections.abc.Awaitable[yandex.cloud.baremetal.v1alpha.vrf_pb2.Vrf]]:
        """Returns the specific VRF resource.

        To get the list of available VRFs, make a [List] request.
        """

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.baremetal.v1alpha.vrf_service_pb2.ListVrfRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.baremetal.v1alpha.vrf_service_pb2.ListVrfResponse, collections.abc.Awaitable[yandex.cloud.baremetal.v1alpha.vrf_service_pb2.ListVrfResponse]]:
        """Retrieves the list of VRF resources in the specified folder."""

    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.baremetal.v1alpha.vrf_service_pb2.CreateVrfRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates a VRF in the specified folder."""

    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.baremetal.v1alpha.vrf_service_pb2.UpdateVrfRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates the specified VRF resource."""

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.baremetal.v1alpha.vrf_service_pb2.DeleteVrfRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deletes the specified VRF resource.

        Deleting a VRF removes its data permanently and is irreversible.
        """

    @abc.abstractmethod
    def ListOperations(
        self,
        request: yandex.cloud.baremetal.v1alpha.vrf_service_pb2.ListVrfOperationsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.baremetal.v1alpha.vrf_service_pb2.ListVrfOperationsResponse, collections.abc.Awaitable[yandex.cloud.baremetal.v1alpha.vrf_service_pb2.ListVrfOperationsResponse]]:
        """Lists operations for the specified VRF."""

def add_VrfServiceServicer_to_server(servicer: VrfServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
