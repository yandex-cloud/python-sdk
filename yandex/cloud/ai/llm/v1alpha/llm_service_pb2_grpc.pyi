"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.ai.llm.v1alpha.llm_service_pb2
import yandex.cloud.operation.operation_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class TextGenerationServiceStub:
    """Service for text generation and conversation."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Instruct: grpc.UnaryStreamMultiCallable[
        yandex.cloud.ai.llm.v1alpha.llm_service_pb2.InstructRequest,
        yandex.cloud.ai.llm.v1alpha.llm_service_pb2.InstructResponse,
    ]
    """RPC method for instructing the model to generate text."""

    Chat: grpc.UnaryStreamMultiCallable[
        yandex.cloud.ai.llm.v1alpha.llm_service_pb2.ChatRequest,
        yandex.cloud.ai.llm.v1alpha.llm_service_pb2.ChatResponse,
    ]
    """RPC method for engaging in a chat conversation with the model."""

class TextGenerationServiceAsyncStub:
    """Service for text generation and conversation."""

    Instruct: grpc.aio.UnaryStreamMultiCallable[
        yandex.cloud.ai.llm.v1alpha.llm_service_pb2.InstructRequest,
        yandex.cloud.ai.llm.v1alpha.llm_service_pb2.InstructResponse,
    ]
    """RPC method for instructing the model to generate text."""

    Chat: grpc.aio.UnaryStreamMultiCallable[
        yandex.cloud.ai.llm.v1alpha.llm_service_pb2.ChatRequest,
        yandex.cloud.ai.llm.v1alpha.llm_service_pb2.ChatResponse,
    ]
    """RPC method for engaging in a chat conversation with the model."""

class TextGenerationServiceServicer(metaclass=abc.ABCMeta):
    """Service for text generation and conversation."""

    @abc.abstractmethod
    def Instruct(
        self,
        request: yandex.cloud.ai.llm.v1alpha.llm_service_pb2.InstructRequest,
        context: _ServicerContext,
    ) -> typing.Union[collections.abc.Iterator[yandex.cloud.ai.llm.v1alpha.llm_service_pb2.InstructResponse], collections.abc.AsyncIterator[yandex.cloud.ai.llm.v1alpha.llm_service_pb2.InstructResponse]]:
        """RPC method for instructing the model to generate text."""

    @abc.abstractmethod
    def Chat(
        self,
        request: yandex.cloud.ai.llm.v1alpha.llm_service_pb2.ChatRequest,
        context: _ServicerContext,
    ) -> typing.Union[collections.abc.Iterator[yandex.cloud.ai.llm.v1alpha.llm_service_pb2.ChatResponse], collections.abc.AsyncIterator[yandex.cloud.ai.llm.v1alpha.llm_service_pb2.ChatResponse]]:
        """RPC method for engaging in a chat conversation with the model."""

def add_TextGenerationServiceServicer_to_server(servicer: TextGenerationServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...

class TokenizerServiceStub:
    """Service for tokenizing input text."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Tokenize: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ai.llm.v1alpha.llm_service_pb2.TokenizeRequest,
        yandex.cloud.ai.llm.v1alpha.llm_service_pb2.TokenizeResponse,
    ]
    """RPC method for tokenizing input text."""

class TokenizerServiceAsyncStub:
    """Service for tokenizing input text."""

    Tokenize: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.ai.llm.v1alpha.llm_service_pb2.TokenizeRequest,
        yandex.cloud.ai.llm.v1alpha.llm_service_pb2.TokenizeResponse,
    ]
    """RPC method for tokenizing input text."""

class TokenizerServiceServicer(metaclass=abc.ABCMeta):
    """Service for tokenizing input text."""

    @abc.abstractmethod
    def Tokenize(
        self,
        request: yandex.cloud.ai.llm.v1alpha.llm_service_pb2.TokenizeRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.ai.llm.v1alpha.llm_service_pb2.TokenizeResponse, collections.abc.Awaitable[yandex.cloud.ai.llm.v1alpha.llm_service_pb2.TokenizeResponse]]:
        """RPC method for tokenizing input text."""

def add_TokenizerServiceServicer_to_server(servicer: TokenizerServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...

class EmbeddingsServiceStub:
    """Service for obtaining embeddings for text data."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Embedding: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ai.llm.v1alpha.llm_service_pb2.EmbeddingRequest,
        yandex.cloud.ai.llm.v1alpha.llm_service_pb2.EmbeddingResponse,
    ]
    """RPC method to obtain embeddings for input text data."""

class EmbeddingsServiceAsyncStub:
    """Service for obtaining embeddings for text data."""

    Embedding: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.ai.llm.v1alpha.llm_service_pb2.EmbeddingRequest,
        yandex.cloud.ai.llm.v1alpha.llm_service_pb2.EmbeddingResponse,
    ]
    """RPC method to obtain embeddings for input text data."""

class EmbeddingsServiceServicer(metaclass=abc.ABCMeta):
    """Service for obtaining embeddings for text data."""

    @abc.abstractmethod
    def Embedding(
        self,
        request: yandex.cloud.ai.llm.v1alpha.llm_service_pb2.EmbeddingRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.ai.llm.v1alpha.llm_service_pb2.EmbeddingResponse, collections.abc.Awaitable[yandex.cloud.ai.llm.v1alpha.llm_service_pb2.EmbeddingResponse]]:
        """RPC method to obtain embeddings for input text data."""

def add_EmbeddingsServiceServicer_to_server(servicer: EmbeddingsServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...

class TextGenerationAsyncServiceStub:
    """Service for asynchronous text generation."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Instruct: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ai.llm.v1alpha.llm_service_pb2.InstructRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """RPC method for instructing the model to generate text."""

class TextGenerationAsyncServiceAsyncStub:
    """Service for asynchronous text generation."""

    Instruct: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.ai.llm.v1alpha.llm_service_pb2.InstructRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """RPC method for instructing the model to generate text."""

class TextGenerationAsyncServiceServicer(metaclass=abc.ABCMeta):
    """Service for asynchronous text generation."""

    @abc.abstractmethod
    def Instruct(
        self,
        request: yandex.cloud.ai.llm.v1alpha.llm_service_pb2.InstructRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """RPC method for instructing the model to generate text."""

def add_TextGenerationAsyncServiceServicer_to_server(servicer: TextGenerationAsyncServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
