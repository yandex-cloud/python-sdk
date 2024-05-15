# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.ai.vision.v1 import vision_service_pb2 as yandex_dot_cloud_dot_ai_dot_vision_dot_v1_dot_vision__service__pb2


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
                )


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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.ai.vision.v1.VisionService/BatchAnalyze',
            yandex_dot_cloud_dot_ai_dot_vision_dot_v1_dot_vision__service__pb2.BatchAnalyzeRequest.SerializeToString,
            yandex_dot_cloud_dot_ai_dot_vision_dot_v1_dot_vision__service__pb2.BatchAnalyzeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
