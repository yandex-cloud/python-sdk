"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.cic.v1.partner_pb2
import yandex.cloud.cic.v1.partner_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class PartnerServiceStub:
    """A set of methods for managing Partner resources."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.cic.v1.partner_service_pb2.GetPartnerRequest,
        yandex.cloud.cic.v1.partner_pb2.Partner,
    ]
    """Returns the specified Partner resource.

    To get the list of available Partner resources, make a [List] request.
    """

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.cic.v1.partner_service_pb2.ListPartnersRequest,
        yandex.cloud.cic.v1.partner_service_pb2.ListPartnersResponse,
    ]
    """Retrieves the list of Partner resources in the specified folder."""

class PartnerServiceAsyncStub:
    """A set of methods for managing Partner resources."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.cic.v1.partner_service_pb2.GetPartnerRequest,
        yandex.cloud.cic.v1.partner_pb2.Partner,
    ]
    """Returns the specified Partner resource.

    To get the list of available Partner resources, make a [List] request.
    """

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.cic.v1.partner_service_pb2.ListPartnersRequest,
        yandex.cloud.cic.v1.partner_service_pb2.ListPartnersResponse,
    ]
    """Retrieves the list of Partner resources in the specified folder."""

class PartnerServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing Partner resources."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.cic.v1.partner_service_pb2.GetPartnerRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.cic.v1.partner_pb2.Partner, collections.abc.Awaitable[yandex.cloud.cic.v1.partner_pb2.Partner]]:
        """Returns the specified Partner resource.

        To get the list of available Partner resources, make a [List] request.
        """

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.cic.v1.partner_service_pb2.ListPartnersRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.cic.v1.partner_service_pb2.ListPartnersResponse, collections.abc.Awaitable[yandex.cloud.cic.v1.partner_service_pb2.ListPartnersResponse]]:
        """Retrieves the list of Partner resources in the specified folder."""

def add_PartnerServiceServicer_to_server(servicer: PartnerServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
