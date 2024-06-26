"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.compute.v1.disk_type_pb2
import yandex.cloud.compute.v1.disk_type_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class DiskTypeServiceStub:
    """A set of methods to retrieve information about disk types."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.disk_type_service_pb2.GetDiskTypeRequest,
        yandex.cloud.compute.v1.disk_type_pb2.DiskType,
    ]
    """Returns the information about specified disk type.

    To get the list of available disk types, make a [List] request.
    """

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.disk_type_service_pb2.ListDiskTypesRequest,
        yandex.cloud.compute.v1.disk_type_service_pb2.ListDiskTypesResponse,
    ]
    """Retrieves the list of disk types for the specified folder."""

class DiskTypeServiceAsyncStub:
    """A set of methods to retrieve information about disk types."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.disk_type_service_pb2.GetDiskTypeRequest,
        yandex.cloud.compute.v1.disk_type_pb2.DiskType,
    ]
    """Returns the information about specified disk type.

    To get the list of available disk types, make a [List] request.
    """

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.compute.v1.disk_type_service_pb2.ListDiskTypesRequest,
        yandex.cloud.compute.v1.disk_type_service_pb2.ListDiskTypesResponse,
    ]
    """Retrieves the list of disk types for the specified folder."""

class DiskTypeServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods to retrieve information about disk types."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.compute.v1.disk_type_service_pb2.GetDiskTypeRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.compute.v1.disk_type_pb2.DiskType, collections.abc.Awaitable[yandex.cloud.compute.v1.disk_type_pb2.DiskType]]:
        """Returns the information about specified disk type.

        To get the list of available disk types, make a [List] request.
        """

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.compute.v1.disk_type_service_pb2.ListDiskTypesRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.compute.v1.disk_type_service_pb2.ListDiskTypesResponse, collections.abc.Awaitable[yandex.cloud.compute.v1.disk_type_service_pb2.ListDiskTypesResponse]]:
        """Retrieves the list of disk types for the specified folder."""

def add_DiskTypeServiceServicer_to_server(servicer: DiskTypeServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
