# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.ai.vision.v1 import vision_service_pb2 as yandex_dot_cloud_dot_ai_dot_vision_dot_v1_dot_vision__service__pb2

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
        + f' but the generated code in yandex/cloud/ai/vision/v1/vision_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class VisionServiceStub(object):
    """A set of methods for the Vision service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.BatchAnalyze = channel.unary_unary(
                '/yandex.cloud.ai.vision.v1.VisionService/BatchAnalyze',
                request_serializer=yandex_dot_cloud_dot_ai_dot_vision_dot_v1_dot_vision__service__pb2.BatchAnalyzeRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_ai_dot_vision_dot_v1_dot_vision__service__pb2.BatchAnalyzeResponse.FromString,
                _registered_method=True)


class VisionServiceServicer(object):
    """A set of methods for the Vision service.
    """

    def BatchAnalyze(self, request, context):
        """Analyzes a batch of images and returns results with annotations.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VisionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'BatchAnalyze': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchAnalyze,
                    request_deserializer=yandex_dot_cloud_dot_ai_dot_vision_dot_v1_dot_vision__service__pb2.BatchAnalyzeRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_ai_dot_vision_dot_v1_dot_vision__service__pb2.BatchAnalyzeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.ai.vision.v1.VisionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.ai.vision.v1.VisionService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class VisionService(object):
    """A set of methods for the Vision service.
    """

    @staticmethod
    def BatchAnalyze(request,
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
            '/yandex.cloud.ai.vision.v1.VisionService/BatchAnalyze',
            yandex_dot_cloud_dot_ai_dot_vision_dot_v1_dot_vision__service__pb2.BatchAnalyzeRequest.SerializeToString,
            yandex_dot_cloud_dot_ai_dot_vision_dot_v1_dot_vision__service__pb2.BatchAnalyzeResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
