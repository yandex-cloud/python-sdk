"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.quotamanager.v1.quota_limit_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class QuotaLimitServiceStub:
    """A set of methods for managing quota limits."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.quotamanager.v1.quota_limit_service_pb2.GetQuotaLimitRequest,
        yandex.cloud.quotamanager.v1.quota_limit_service_pb2.QuotaLimit,
    ]
    """Returns the specified quota limit."""

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.quotamanager.v1.quota_limit_service_pb2.ListQuotaLimitsRequest,
        yandex.cloud.quotamanager.v1.quota_limit_service_pb2.ListQuotaLimitsResponse,
    ]
    """Retrieves the list of quota limits for a given service."""

    ListServices: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.quotamanager.v1.quota_limit_service_pb2.ListServicesRequest,
        yandex.cloud.quotamanager.v1.quota_limit_service_pb2.ListServicesResponse,
    ]
    """Retrieves the list of services available for quota management."""

class QuotaLimitServiceAsyncStub:
    """A set of methods for managing quota limits."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.quotamanager.v1.quota_limit_service_pb2.GetQuotaLimitRequest,
        yandex.cloud.quotamanager.v1.quota_limit_service_pb2.QuotaLimit,
    ]
    """Returns the specified quota limit."""

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.quotamanager.v1.quota_limit_service_pb2.ListQuotaLimitsRequest,
        yandex.cloud.quotamanager.v1.quota_limit_service_pb2.ListQuotaLimitsResponse,
    ]
    """Retrieves the list of quota limits for a given service."""

    ListServices: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.quotamanager.v1.quota_limit_service_pb2.ListServicesRequest,
        yandex.cloud.quotamanager.v1.quota_limit_service_pb2.ListServicesResponse,
    ]
    """Retrieves the list of services available for quota management."""

class QuotaLimitServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing quota limits."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.quotamanager.v1.quota_limit_service_pb2.GetQuotaLimitRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.quotamanager.v1.quota_limit_service_pb2.QuotaLimit, collections.abc.Awaitable[yandex.cloud.quotamanager.v1.quota_limit_service_pb2.QuotaLimit]]:
        """Returns the specified quota limit."""

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.quotamanager.v1.quota_limit_service_pb2.ListQuotaLimitsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.quotamanager.v1.quota_limit_service_pb2.ListQuotaLimitsResponse, collections.abc.Awaitable[yandex.cloud.quotamanager.v1.quota_limit_service_pb2.ListQuotaLimitsResponse]]:
        """Retrieves the list of quota limits for a given service."""

    @abc.abstractmethod
    def ListServices(
        self,
        request: yandex.cloud.quotamanager.v1.quota_limit_service_pb2.ListServicesRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.quotamanager.v1.quota_limit_service_pb2.ListServicesResponse, collections.abc.Awaitable[yandex.cloud.quotamanager.v1.quota_limit_service_pb2.ListServicesResponse]]:
        """Retrieves the list of services available for quota management."""

def add_QuotaLimitServiceServicer_to_server(servicer: QuotaLimitServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
