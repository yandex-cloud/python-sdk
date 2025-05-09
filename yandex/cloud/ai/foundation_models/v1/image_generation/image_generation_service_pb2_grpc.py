# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.ai.foundation_models.v1.image_generation import image_generation_service_pb2 as yandex_dot_cloud_dot_ai_dot_foundation__models_dot_v1_dot_image__generation_dot_image__generation__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2

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
        + f' but the generated code in yandex/cloud/ai/foundation_models/v1/image_generation/image_generation_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ImageGenerationAsyncServiceStub(object):
    """Service for creating images based on a text description. 
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Generate = channel.unary_unary(
                '/yandex.cloud.ai.foundation_models.v1.image_generation.ImageGenerationAsyncService/Generate',
                request_serializer=yandex_dot_cloud_dot_ai_dot_foundation__models_dot_v1_dot_image__generation_dot_image__generation__service__pb2.ImageGenerationRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)


class ImageGenerationAsyncServiceServicer(object):
    """Service for creating images based on a text description. 
    """

    def Generate(self, request, context):
        """A method for generating an image based on a textual description.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ImageGenerationAsyncServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Generate': grpc.unary_unary_rpc_method_handler(
                    servicer.Generate,
                    request_deserializer=yandex_dot_cloud_dot_ai_dot_foundation__models_dot_v1_dot_image__generation_dot_image__generation__service__pb2.ImageGenerationRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.ai.foundation_models.v1.image_generation.ImageGenerationAsyncService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.ai.foundation_models.v1.image_generation.ImageGenerationAsyncService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ImageGenerationAsyncService(object):
    """Service for creating images based on a text description. 
    """

    @staticmethod
    def Generate(request,
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
            '/yandex.cloud.ai.foundation_models.v1.image_generation.ImageGenerationAsyncService/Generate',
            yandex_dot_cloud_dot_ai_dot_foundation__models_dot_v1_dot_image__generation_dot_image__generation__service__pb2.ImageGenerationRequest.SerializeToString,
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
