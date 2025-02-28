"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.access.access_pb2
import yandex.cloud.operation.operation_pb2
import yandex.cloud.video.v1.channel_pb2
import yandex.cloud.video.v1.channel_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class ChannelServiceStub:
    """Channel management service."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.channel_service_pb2.GetChannelRequest,
        yandex.cloud.video.v1.channel_pb2.Channel,
    ]
    """Returns the specific channel."""

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.channel_service_pb2.ListChannelsRequest,
        yandex.cloud.video.v1.channel_service_pb2.ListChannelsResponse,
    ]
    """List channels for organization."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.channel_service_pb2.CreateChannelRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Create channel."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.channel_service_pb2.UpdateChannelRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Update channel."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.channel_service_pb2.DeleteChannelRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Delete channel."""

    BatchDelete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.channel_service_pb2.BatchDeleteChannelsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Batch delete channels."""

    ListAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        yandex.cloud.access.access_pb2.ListAccessBindingsResponse,
    ]
    """Lists existing access bindings for the specified channel."""

    SetAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Sets access bindings for the channel."""

    UpdateAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates access bindings for the specified channel."""

class ChannelServiceAsyncStub:
    """Channel management service."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.channel_service_pb2.GetChannelRequest,
        yandex.cloud.video.v1.channel_pb2.Channel,
    ]
    """Returns the specific channel."""

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.channel_service_pb2.ListChannelsRequest,
        yandex.cloud.video.v1.channel_service_pb2.ListChannelsResponse,
    ]
    """List channels for organization."""

    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.channel_service_pb2.CreateChannelRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Create channel."""

    Update: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.channel_service_pb2.UpdateChannelRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Update channel."""

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.channel_service_pb2.DeleteChannelRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Delete channel."""

    BatchDelete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.channel_service_pb2.BatchDeleteChannelsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Batch delete channels."""

    ListAccessBindings: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        yandex.cloud.access.access_pb2.ListAccessBindingsResponse,
    ]
    """Lists existing access bindings for the specified channel."""

    SetAccessBindings: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Sets access bindings for the channel."""

    UpdateAccessBindings: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates access bindings for the specified channel."""

class ChannelServiceServicer(metaclass=abc.ABCMeta):
    """Channel management service."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.video.v1.channel_service_pb2.GetChannelRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.video.v1.channel_pb2.Channel, collections.abc.Awaitable[yandex.cloud.video.v1.channel_pb2.Channel]]:
        """Returns the specific channel."""

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.video.v1.channel_service_pb2.ListChannelsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.video.v1.channel_service_pb2.ListChannelsResponse, collections.abc.Awaitable[yandex.cloud.video.v1.channel_service_pb2.ListChannelsResponse]]:
        """List channels for organization."""

    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.video.v1.channel_service_pb2.CreateChannelRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Create channel."""

    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.video.v1.channel_service_pb2.UpdateChannelRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Update channel."""

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.video.v1.channel_service_pb2.DeleteChannelRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Delete channel."""

    @abc.abstractmethod
    def BatchDelete(
        self,
        request: yandex.cloud.video.v1.channel_service_pb2.BatchDeleteChannelsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Batch delete channels."""

    @abc.abstractmethod
    def ListAccessBindings(
        self,
        request: yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.access.access_pb2.ListAccessBindingsResponse, collections.abc.Awaitable[yandex.cloud.access.access_pb2.ListAccessBindingsResponse]]:
        """Lists existing access bindings for the specified channel."""

    @abc.abstractmethod
    def SetAccessBindings(
        self,
        request: yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Sets access bindings for the channel."""

    @abc.abstractmethod
    def UpdateAccessBindings(
        self,
        request: yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates access bindings for the specified channel."""

def add_ChannelServiceServicer_to_server(servicer: ChannelServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
