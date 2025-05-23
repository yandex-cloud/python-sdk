"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.marketplace.metering.v1.product_usage_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class ProductUsageServiceStub:
    """A set of methods for managing product's usage with product instances."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Write: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.marketplace.metering.v1.product_usage_service_pb2.WriteUsageRequest,
        yandex.cloud.marketplace.metering.v1.product_usage_service_pb2.WriteUsageResponse,
    ]
    """Writes product's usage (authenticated by publisher's service account)"""

class ProductUsageServiceAsyncStub:
    """A set of methods for managing product's usage with product instances."""

    Write: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.marketplace.metering.v1.product_usage_service_pb2.WriteUsageRequest,
        yandex.cloud.marketplace.metering.v1.product_usage_service_pb2.WriteUsageResponse,
    ]
    """Writes product's usage (authenticated by publisher's service account)"""

class ProductUsageServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing product's usage with product instances."""

    @abc.abstractmethod
    def Write(
        self,
        request: yandex.cloud.marketplace.metering.v1.product_usage_service_pb2.WriteUsageRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.marketplace.metering.v1.product_usage_service_pb2.WriteUsageResponse, collections.abc.Awaitable[yandex.cloud.marketplace.metering.v1.product_usage_service_pb2.WriteUsageResponse]]:
        """Writes product's usage (authenticated by publisher's service account)"""

def add_ProductUsageServiceServicer_to_server(servicer: ProductUsageServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
