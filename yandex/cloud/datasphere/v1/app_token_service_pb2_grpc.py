# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from yandex.cloud.datasphere.v1 import app_token_service_pb2 as yandex_dot_cloud_dot_datasphere_dot_v1_dot_app__token__service__pb2


class AppTokenServiceStub(object):
    """A set of methods for managing app tokens.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Validate = channel.unary_unary(
                '/yandex.cloud.datasphere.v1.AppTokenService/Validate',
                request_serializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_app__token__service__pb2.AppTokenValidateRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class AppTokenServiceServicer(object):
    """A set of methods for managing app tokens.
    """

    def Validate(self, request, context):
        """Validates app token.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AppTokenServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Validate': grpc.unary_unary_rpc_method_handler(
                    servicer.Validate,
                    request_deserializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_app__token__service__pb2.AppTokenValidateRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.datasphere.v1.AppTokenService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AppTokenService(object):
    """A set of methods for managing app tokens.
    """

    @staticmethod
    def Validate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.datasphere.v1.AppTokenService/Validate',
            yandex_dot_cloud_dot_datasphere_dot_v1_dot_app__token__service__pb2.AppTokenValidateRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
