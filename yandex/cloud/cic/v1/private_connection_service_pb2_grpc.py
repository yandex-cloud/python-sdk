# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.cic.v1 import private_connection_pb2 as yandex_dot_cloud_dot_cic_dot_v1_dot_private__connection__pb2
from yandex.cloud.cic.v1 import private_connection_service_pb2 as yandex_dot_cloud_dot_cic_dot_v1_dot_private__connection__service__pb2


class PrivateConnectionServiceStub(object):
    """A set of methods for managing PrivateConnection resources.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.cic.v1.PrivateConnectionService/Get',
                request_serializer=yandex_dot_cloud_dot_cic_dot_v1_dot_private__connection__service__pb2.GetPrivateConnectionRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_cic_dot_v1_dot_private__connection__pb2.PrivateConnection.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.cic.v1.PrivateConnectionService/List',
                request_serializer=yandex_dot_cloud_dot_cic_dot_v1_dot_private__connection__service__pb2.ListPrivateConnectionsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_cic_dot_v1_dot_private__connection__service__pb2.ListPrivateConnectionsResponse.FromString,
                )


class PrivateConnectionServiceServicer(object):
    """A set of methods for managing PrivateConnection resources.
    """

    def Get(self, request, context):
        """Returns the specified PrivateConnection resource.

        To get the list of available PrivateConnection resources, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of PrivateConnection resources in the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PrivateConnectionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_cic_dot_v1_dot_private__connection__service__pb2.GetPrivateConnectionRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_cic_dot_v1_dot_private__connection__pb2.PrivateConnection.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_cic_dot_v1_dot_private__connection__service__pb2.ListPrivateConnectionsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_cic_dot_v1_dot_private__connection__service__pb2.ListPrivateConnectionsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.cic.v1.PrivateConnectionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PrivateConnectionService(object):
    """A set of methods for managing PrivateConnection resources.
    """

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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.cic.v1.PrivateConnectionService/Get',
            yandex_dot_cloud_dot_cic_dot_v1_dot_private__connection__service__pb2.GetPrivateConnectionRequest.SerializeToString,
            yandex_dot_cloud_dot_cic_dot_v1_dot_private__connection__pb2.PrivateConnection.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.cic.v1.PrivateConnectionService/List',
            yandex_dot_cloud_dot_cic_dot_v1_dot_private__connection__service__pb2.ListPrivateConnectionsRequest.SerializeToString,
            yandex_dot_cloud_dot_cic_dot_v1_dot_private__connection__service__pb2.ListPrivateConnectionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
