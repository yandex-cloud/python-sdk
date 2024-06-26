# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.speechsense.v1 import talk_service_pb2 as yandex_dot_cloud_dot_speechsense_dot_v1_dot_talk__service__pb2


class TalkServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UploadAsStream = channel.stream_unary(
                '/yandex.cloud.speechsense.v1.TalkService/UploadAsStream',
                request_serializer=yandex_dot_cloud_dot_speechsense_dot_v1_dot_talk__service__pb2.StreamTalkRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_speechsense_dot_v1_dot_talk__service__pb2.UploadTalkResponse.FromString,
                )
        self.Upload = channel.unary_unary(
                '/yandex.cloud.speechsense.v1.TalkService/Upload',
                request_serializer=yandex_dot_cloud_dot_speechsense_dot_v1_dot_talk__service__pb2.UploadTalkRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_speechsense_dot_v1_dot_talk__service__pb2.UploadTalkResponse.FromString,
                )
        self.UploadText = channel.unary_unary(
                '/yandex.cloud.speechsense.v1.TalkService/UploadText',
                request_serializer=yandex_dot_cloud_dot_speechsense_dot_v1_dot_talk__service__pb2.UploadTextRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_speechsense_dot_v1_dot_talk__service__pb2.UploadTextResponse.FromString,
                )
        self.Search = channel.unary_unary(
                '/yandex.cloud.speechsense.v1.TalkService/Search',
                request_serializer=yandex_dot_cloud_dot_speechsense_dot_v1_dot_talk__service__pb2.SearchTalkRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_speechsense_dot_v1_dot_talk__service__pb2.SearchTalkResponse.FromString,
                )
        self.Get = channel.unary_unary(
                '/yandex.cloud.speechsense.v1.TalkService/Get',
                request_serializer=yandex_dot_cloud_dot_speechsense_dot_v1_dot_talk__service__pb2.GetTalkRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_speechsense_dot_v1_dot_talk__service__pb2.GetTalkResponse.FromString,
                )


class TalkServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def UploadAsStream(self, request_iterator, context):
        """rpc for streaming talk documents. First message should contain Talk related metadata,
        second - audio metadata, others should contain audio bytes in chunks
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Upload(self, request, context):
        """rpc for uploading talk document as single message
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UploadText(self, request, context):
        """rpc for uploading text talk document
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Search(self, request, context):
        """rpc for searching talks. will return ids only
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """rpc for bulk get
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TalkServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UploadAsStream': grpc.stream_unary_rpc_method_handler(
                    servicer.UploadAsStream,
                    request_deserializer=yandex_dot_cloud_dot_speechsense_dot_v1_dot_talk__service__pb2.StreamTalkRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_speechsense_dot_v1_dot_talk__service__pb2.UploadTalkResponse.SerializeToString,
            ),
            'Upload': grpc.unary_unary_rpc_method_handler(
                    servicer.Upload,
                    request_deserializer=yandex_dot_cloud_dot_speechsense_dot_v1_dot_talk__service__pb2.UploadTalkRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_speechsense_dot_v1_dot_talk__service__pb2.UploadTalkResponse.SerializeToString,
            ),
            'UploadText': grpc.unary_unary_rpc_method_handler(
                    servicer.UploadText,
                    request_deserializer=yandex_dot_cloud_dot_speechsense_dot_v1_dot_talk__service__pb2.UploadTextRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_speechsense_dot_v1_dot_talk__service__pb2.UploadTextResponse.SerializeToString,
            ),
            'Search': grpc.unary_unary_rpc_method_handler(
                    servicer.Search,
                    request_deserializer=yandex_dot_cloud_dot_speechsense_dot_v1_dot_talk__service__pb2.SearchTalkRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_speechsense_dot_v1_dot_talk__service__pb2.SearchTalkResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_speechsense_dot_v1_dot_talk__service__pb2.GetTalkRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_speechsense_dot_v1_dot_talk__service__pb2.GetTalkResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.speechsense.v1.TalkService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TalkService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def UploadAsStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/yandex.cloud.speechsense.v1.TalkService/UploadAsStream',
            yandex_dot_cloud_dot_speechsense_dot_v1_dot_talk__service__pb2.StreamTalkRequest.SerializeToString,
            yandex_dot_cloud_dot_speechsense_dot_v1_dot_talk__service__pb2.UploadTalkResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Upload(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.speechsense.v1.TalkService/Upload',
            yandex_dot_cloud_dot_speechsense_dot_v1_dot_talk__service__pb2.UploadTalkRequest.SerializeToString,
            yandex_dot_cloud_dot_speechsense_dot_v1_dot_talk__service__pb2.UploadTalkResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UploadText(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.speechsense.v1.TalkService/UploadText',
            yandex_dot_cloud_dot_speechsense_dot_v1_dot_talk__service__pb2.UploadTextRequest.SerializeToString,
            yandex_dot_cloud_dot_speechsense_dot_v1_dot_talk__service__pb2.UploadTextResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Search(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.speechsense.v1.TalkService/Search',
            yandex_dot_cloud_dot_speechsense_dot_v1_dot_talk__service__pb2.SearchTalkRequest.SerializeToString,
            yandex_dot_cloud_dot_speechsense_dot_v1_dot_talk__service__pb2.SearchTalkResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.speechsense.v1.TalkService/Get',
            yandex_dot_cloud_dot_speechsense_dot_v1_dot_talk__service__pb2.GetTalkRequest.SerializeToString,
            yandex_dot_cloud_dot_speechsense_dot_v1_dot_talk__service__pb2.GetTalkResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
