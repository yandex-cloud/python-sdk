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
import yandex.cloud.datasphere.v1.app_token_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class AppTokenServiceStub:
    """A set of methods for managing app tokens."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Validate: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v1.app_token_service_pb2.AppTokenValidateRequest,
        google.protobuf.empty_pb2.Empty,
    ]
    """Validates app token."""

class AppTokenServiceAsyncStub:
    """A set of methods for managing app tokens."""

    Validate: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v1.app_token_service_pb2.AppTokenValidateRequest,
        google.protobuf.empty_pb2.Empty,
    ]
    """Validates app token."""

class AppTokenServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing app tokens."""

    @abc.abstractmethod
    def Validate(
        self,
        request: yandex.cloud.datasphere.v1.app_token_service_pb2.AppTokenValidateRequest,
        context: _ServicerContext,
    ) -> typing.Union[google.protobuf.empty_pb2.Empty, collections.abc.Awaitable[google.protobuf.empty_pb2.Empty]]:
        """Validates app token."""

def add_AppTokenServiceServicer_to_server(servicer: AppTokenServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
