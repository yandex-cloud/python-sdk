# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.ai.llm.v1alpha import llm_service_pb2 as yandex_dot_cloud_dot_ai_dot_llm_dot_v1alpha_dot_llm__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2

GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in yandex/cloud/ai/llm/v1alpha/llm_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class TextGenerationServiceStub(object):
    """Service for text generation and conversation.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Instruct = channel.unary_stream(
                '/yandex.cloud.ai.llm.v1alpha.TextGenerationService/Instruct',
                request_serializer=yandex_dot_cloud_dot_ai_dot_llm_dot_v1alpha_dot_llm__service__pb2.InstructRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_ai_dot_llm_dot_v1alpha_dot_llm__service__pb2.InstructResponse.FromString,
                _registered_method=True)
        self.Chat = channel.unary_stream(
                '/yandex.cloud.ai.llm.v1alpha.TextGenerationService/Chat',
                request_serializer=yandex_dot_cloud_dot_ai_dot_llm_dot_v1alpha_dot_llm__service__pb2.ChatRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_ai_dot_llm_dot_v1alpha_dot_llm__service__pb2.ChatResponse.FromString,
                _registered_method=True)


class TextGenerationServiceServicer(object):
    """Service for text generation and conversation.
    """

    def Instruct(self, request, context):
        """RPC method for instructing the model to generate text.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Chat(self, request, context):
        """RPC method for engaging in a chat conversation with the model.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TextGenerationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Instruct': grpc.unary_stream_rpc_method_handler(
                    servicer.Instruct,
                    request_deserializer=yandex_dot_cloud_dot_ai_dot_llm_dot_v1alpha_dot_llm__service__pb2.InstructRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_ai_dot_llm_dot_v1alpha_dot_llm__service__pb2.InstructResponse.SerializeToString,
            ),
            'Chat': grpc.unary_stream_rpc_method_handler(
                    servicer.Chat,
                    request_deserializer=yandex_dot_cloud_dot_ai_dot_llm_dot_v1alpha_dot_llm__service__pb2.ChatRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_ai_dot_llm_dot_v1alpha_dot_llm__service__pb2.ChatResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.ai.llm.v1alpha.TextGenerationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.ai.llm.v1alpha.TextGenerationService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class TextGenerationService(object):
    """Service for text generation and conversation.
    """

    @staticmethod
    def Instruct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/yandex.cloud.ai.llm.v1alpha.TextGenerationService/Instruct',
            yandex_dot_cloud_dot_ai_dot_llm_dot_v1alpha_dot_llm__service__pb2.InstructRequest.SerializeToString,
            yandex_dot_cloud_dot_ai_dot_llm_dot_v1alpha_dot_llm__service__pb2.InstructResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Chat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/yandex.cloud.ai.llm.v1alpha.TextGenerationService/Chat',
            yandex_dot_cloud_dot_ai_dot_llm_dot_v1alpha_dot_llm__service__pb2.ChatRequest.SerializeToString,
            yandex_dot_cloud_dot_ai_dot_llm_dot_v1alpha_dot_llm__service__pb2.ChatResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class TokenizerServiceStub(object):
    """Service for tokenizing input text.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Tokenize = channel.unary_unary(
                '/yandex.cloud.ai.llm.v1alpha.TokenizerService/Tokenize',
                request_serializer=yandex_dot_cloud_dot_ai_dot_llm_dot_v1alpha_dot_llm__service__pb2.TokenizeRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_ai_dot_llm_dot_v1alpha_dot_llm__service__pb2.TokenizeResponse.FromString,
                _registered_method=True)


class TokenizerServiceServicer(object):
    """Service for tokenizing input text.
    """

    def Tokenize(self, request, context):
        """RPC method for tokenizing input text.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TokenizerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Tokenize': grpc.unary_unary_rpc_method_handler(
                    servicer.Tokenize,
                    request_deserializer=yandex_dot_cloud_dot_ai_dot_llm_dot_v1alpha_dot_llm__service__pb2.TokenizeRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_ai_dot_llm_dot_v1alpha_dot_llm__service__pb2.TokenizeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.ai.llm.v1alpha.TokenizerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.ai.llm.v1alpha.TokenizerService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class TokenizerService(object):
    """Service for tokenizing input text.
    """

    @staticmethod
    def Tokenize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.ai.llm.v1alpha.TokenizerService/Tokenize',
            yandex_dot_cloud_dot_ai_dot_llm_dot_v1alpha_dot_llm__service__pb2.TokenizeRequest.SerializeToString,
            yandex_dot_cloud_dot_ai_dot_llm_dot_v1alpha_dot_llm__service__pb2.TokenizeResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class EmbeddingsServiceStub(object):
    """Service for obtaining embeddings for text data.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Embedding = channel.unary_unary(
                '/yandex.cloud.ai.llm.v1alpha.EmbeddingsService/Embedding',
                request_serializer=yandex_dot_cloud_dot_ai_dot_llm_dot_v1alpha_dot_llm__service__pb2.EmbeddingRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_ai_dot_llm_dot_v1alpha_dot_llm__service__pb2.EmbeddingResponse.FromString,
                _registered_method=True)


class EmbeddingsServiceServicer(object):
    """Service for obtaining embeddings for text data.
    """

    def Embedding(self, request, context):
        """RPC method to obtain embeddings for input text data.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EmbeddingsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Embedding': grpc.unary_unary_rpc_method_handler(
                    servicer.Embedding,
                    request_deserializer=yandex_dot_cloud_dot_ai_dot_llm_dot_v1alpha_dot_llm__service__pb2.EmbeddingRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_ai_dot_llm_dot_v1alpha_dot_llm__service__pb2.EmbeddingResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.ai.llm.v1alpha.EmbeddingsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.ai.llm.v1alpha.EmbeddingsService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class EmbeddingsService(object):
    """Service for obtaining embeddings for text data.
    """

    @staticmethod
    def Embedding(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.ai.llm.v1alpha.EmbeddingsService/Embedding',
            yandex_dot_cloud_dot_ai_dot_llm_dot_v1alpha_dot_llm__service__pb2.EmbeddingRequest.SerializeToString,
            yandex_dot_cloud_dot_ai_dot_llm_dot_v1alpha_dot_llm__service__pb2.EmbeddingResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class TextGenerationAsyncServiceStub(object):
    """Service for asynchronous text generation.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Instruct = channel.unary_unary(
                '/yandex.cloud.ai.llm.v1alpha.TextGenerationAsyncService/Instruct',
                request_serializer=yandex_dot_cloud_dot_ai_dot_llm_dot_v1alpha_dot_llm__service__pb2.InstructRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)


class TextGenerationAsyncServiceServicer(object):
    """Service for asynchronous text generation.
    """

    def Instruct(self, request, context):
        """RPC method for instructing the model to generate text.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TextGenerationAsyncServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Instruct': grpc.unary_unary_rpc_method_handler(
                    servicer.Instruct,
                    request_deserializer=yandex_dot_cloud_dot_ai_dot_llm_dot_v1alpha_dot_llm__service__pb2.InstructRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.ai.llm.v1alpha.TextGenerationAsyncService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.ai.llm.v1alpha.TextGenerationAsyncService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class TextGenerationAsyncService(object):
    """Service for asynchronous text generation.
    """

    @staticmethod
    def Instruct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.ai.llm.v1alpha.TextGenerationAsyncService/Instruct',
            yandex_dot_cloud_dot_ai_dot_llm_dot_v1alpha_dot_llm__service__pb2.InstructRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
