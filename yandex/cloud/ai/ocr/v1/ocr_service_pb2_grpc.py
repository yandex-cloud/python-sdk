# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.ai.ocr.v1 import ocr_service_pb2 as yandex_dot_cloud_dot_ai_dot_ocr_dot_v1_dot_ocr__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class TextRecognitionServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Recognize = channel.unary_stream(
                '/yandex.cloud.ai.ocr.v1.TextRecognitionService/Recognize',
                request_serializer=yandex_dot_cloud_dot_ai_dot_ocr_dot_v1_dot_ocr__service__pb2.RecognizeTextRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_ai_dot_ocr_dot_v1_dot_ocr__service__pb2.RecognizeTextResponse.FromString,
                )


class TextRecognitionServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Recognize(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TextRecognitionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Recognize': grpc.unary_stream_rpc_method_handler(
                    servicer.Recognize,
                    request_deserializer=yandex_dot_cloud_dot_ai_dot_ocr_dot_v1_dot_ocr__service__pb2.RecognizeTextRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_ai_dot_ocr_dot_v1_dot_ocr__service__pb2.RecognizeTextResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.ai.ocr.v1.TextRecognitionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TextRecognitionService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Recognize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/yandex.cloud.ai.ocr.v1.TextRecognitionService/Recognize',
            yandex_dot_cloud_dot_ai_dot_ocr_dot_v1_dot_ocr__service__pb2.RecognizeTextRequest.SerializeToString,
            yandex_dot_cloud_dot_ai_dot_ocr_dot_v1_dot_ocr__service__pb2.RecognizeTextResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class TextRecognitionAsyncServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Recognize = channel.unary_unary(
                '/yandex.cloud.ai.ocr.v1.TextRecognitionAsyncService/Recognize',
                request_serializer=yandex_dot_cloud_dot_ai_dot_ocr_dot_v1_dot_ocr__service__pb2.RecognizeTextRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.GetRecognition = channel.unary_stream(
                '/yandex.cloud.ai.ocr.v1.TextRecognitionAsyncService/GetRecognition',
                request_serializer=yandex_dot_cloud_dot_ai_dot_ocr_dot_v1_dot_ocr__service__pb2.GetRecognitionRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_ai_dot_ocr_dot_v1_dot_ocr__service__pb2.RecognizeTextResponse.FromString,
                )


class TextRecognitionAsyncServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Recognize(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRecognition(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TextRecognitionAsyncServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Recognize': grpc.unary_unary_rpc_method_handler(
                    servicer.Recognize,
                    request_deserializer=yandex_dot_cloud_dot_ai_dot_ocr_dot_v1_dot_ocr__service__pb2.RecognizeTextRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'GetRecognition': grpc.unary_stream_rpc_method_handler(
                    servicer.GetRecognition,
                    request_deserializer=yandex_dot_cloud_dot_ai_dot_ocr_dot_v1_dot_ocr__service__pb2.GetRecognitionRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_ai_dot_ocr_dot_v1_dot_ocr__service__pb2.RecognizeTextResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.ai.ocr.v1.TextRecognitionAsyncService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TextRecognitionAsyncService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Recognize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.ai.ocr.v1.TextRecognitionAsyncService/Recognize',
            yandex_dot_cloud_dot_ai_dot_ocr_dot_v1_dot_ocr__service__pb2.RecognizeTextRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRecognition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/yandex.cloud.ai.ocr.v1.TextRecognitionAsyncService/GetRecognition',
            yandex_dot_cloud_dot_ai_dot_ocr_dot_v1_dot_ocr__service__pb2.GetRecognitionRequest.SerializeToString,
            yandex_dot_cloud_dot_ai_dot_ocr_dot_v1_dot_ocr__service__pb2.RecognizeTextResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)