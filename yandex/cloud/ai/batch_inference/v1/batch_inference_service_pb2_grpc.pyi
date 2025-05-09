"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.ai.batch_inference.v1.batch_inference_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class BatchInferenceServiceStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Describe: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ai.batch_inference.v1.batch_inference_service_pb2.DescribeBatchInferenceRequest,
        yandex.cloud.ai.batch_inference.v1.batch_inference_service_pb2.DescribeBatchInferenceResponse,
    ]
    """Describes a concrete task"""

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ai.batch_inference.v1.batch_inference_service_pb2.ListBatchInferencesRequest,
        yandex.cloud.ai.batch_inference.v1.batch_inference_service_pb2.ListBatchInferencesResponse,
    ]
    """Lists tasks in folder"""

    Cancel: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ai.batch_inference.v1.batch_inference_service_pb2.CancelBatchInferenceRequest,
        yandex.cloud.ai.batch_inference.v1.batch_inference_service_pb2.CancelBatchInferenceResponse,
    ]
    """Cancels a concrete task"""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ai.batch_inference.v1.batch_inference_service_pb2.DeleteBatchInferenceRequest,
        yandex.cloud.ai.batch_inference.v1.batch_inference_service_pb2.DeleteBatchInferenceResponse,
    ]
    """Deletes a concrete task"""

class BatchInferenceServiceAsyncStub:
    Describe: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.ai.batch_inference.v1.batch_inference_service_pb2.DescribeBatchInferenceRequest,
        yandex.cloud.ai.batch_inference.v1.batch_inference_service_pb2.DescribeBatchInferenceResponse,
    ]
    """Describes a concrete task"""

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.ai.batch_inference.v1.batch_inference_service_pb2.ListBatchInferencesRequest,
        yandex.cloud.ai.batch_inference.v1.batch_inference_service_pb2.ListBatchInferencesResponse,
    ]
    """Lists tasks in folder"""

    Cancel: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.ai.batch_inference.v1.batch_inference_service_pb2.CancelBatchInferenceRequest,
        yandex.cloud.ai.batch_inference.v1.batch_inference_service_pb2.CancelBatchInferenceResponse,
    ]
    """Cancels a concrete task"""

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.ai.batch_inference.v1.batch_inference_service_pb2.DeleteBatchInferenceRequest,
        yandex.cloud.ai.batch_inference.v1.batch_inference_service_pb2.DeleteBatchInferenceResponse,
    ]
    """Deletes a concrete task"""

class BatchInferenceServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Describe(
        self,
        request: yandex.cloud.ai.batch_inference.v1.batch_inference_service_pb2.DescribeBatchInferenceRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.ai.batch_inference.v1.batch_inference_service_pb2.DescribeBatchInferenceResponse, collections.abc.Awaitable[yandex.cloud.ai.batch_inference.v1.batch_inference_service_pb2.DescribeBatchInferenceResponse]]:
        """Describes a concrete task"""

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.ai.batch_inference.v1.batch_inference_service_pb2.ListBatchInferencesRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.ai.batch_inference.v1.batch_inference_service_pb2.ListBatchInferencesResponse, collections.abc.Awaitable[yandex.cloud.ai.batch_inference.v1.batch_inference_service_pb2.ListBatchInferencesResponse]]:
        """Lists tasks in folder"""

    @abc.abstractmethod
    def Cancel(
        self,
        request: yandex.cloud.ai.batch_inference.v1.batch_inference_service_pb2.CancelBatchInferenceRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.ai.batch_inference.v1.batch_inference_service_pb2.CancelBatchInferenceResponse, collections.abc.Awaitable[yandex.cloud.ai.batch_inference.v1.batch_inference_service_pb2.CancelBatchInferenceResponse]]:
        """Cancels a concrete task"""

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.ai.batch_inference.v1.batch_inference_service_pb2.DeleteBatchInferenceRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.ai.batch_inference.v1.batch_inference_service_pb2.DeleteBatchInferenceResponse, collections.abc.Awaitable[yandex.cloud.ai.batch_inference.v1.batch_inference_service_pb2.DeleteBatchInferenceResponse]]:
        """Deletes a concrete task"""

def add_BatchInferenceServiceServicer_to_server(servicer: BatchInferenceServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
