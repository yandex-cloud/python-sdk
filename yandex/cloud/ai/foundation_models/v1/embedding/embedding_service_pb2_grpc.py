# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.ai.foundation_models.v1.embedding import embedding_service_pb2 as yandex_dot_cloud_dot_ai_dot_foundation__models_dot_v1_dot_embedding_dot_embedding__service__pb2

GRPC_GENERATED_VERSION = '1.70.0'
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
        + f' but the generated code in yandex/cloud/ai/foundation_models/v1/embedding/embedding_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class EmbeddingsServiceStub(object):
    """Service for obtaining embeddings from input data.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.TextEmbedding = channel.unary_unary(
                '/yandex.cloud.ai.foundation_models.v1.EmbeddingsService/TextEmbedding',
                request_serializer=yandex_dot_cloud_dot_ai_dot_foundation__models_dot_v1_dot_embedding_dot_embedding__service__pb2.TextEmbeddingRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_ai_dot_foundation__models_dot_v1_dot_embedding_dot_embedding__service__pb2.TextEmbeddingResponse.FromString,
                _registered_method=True)


class EmbeddingsServiceServicer(object):
    """Service for obtaining embeddings from input data.
    """

    def TextEmbedding(self, request, context):
        """A method for obtaining embeddings from text data.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EmbeddingsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'TextEmbedding': grpc.unary_unary_rpc_method_handler(
                    servicer.TextEmbedding,
                    request_deserializer=yandex_dot_cloud_dot_ai_dot_foundation__models_dot_v1_dot_embedding_dot_embedding__service__pb2.TextEmbeddingRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_ai_dot_foundation__models_dot_v1_dot_embedding_dot_embedding__service__pb2.TextEmbeddingResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.ai.foundation_models.v1.EmbeddingsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.ai.foundation_models.v1.EmbeddingsService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class EmbeddingsService(object):
    """Service for obtaining embeddings from input data.
    """

    @staticmethod
    def TextEmbedding(request,
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
            '/yandex.cloud.ai.foundation_models.v1.EmbeddingsService/TextEmbedding',
            yandex_dot_cloud_dot_ai_dot_foundation__models_dot_v1_dot_embedding_dot_embedding__service__pb2.TextEmbeddingRequest.SerializeToString,
            yandex_dot_cloud_dot_ai_dot_foundation__models_dot_v1_dot_embedding_dot_embedding__service__pb2.TextEmbeddingResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
