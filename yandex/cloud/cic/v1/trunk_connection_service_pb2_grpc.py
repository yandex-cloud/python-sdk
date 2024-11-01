# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.cic.v1 import trunk_connection_pb2 as yandex_dot_cloud_dot_cic_dot_v1_dot_trunk__connection__pb2
from yandex.cloud.cic.v1 import trunk_connection_service_pb2 as yandex_dot_cloud_dot_cic_dot_v1_dot_trunk__connection__service__pb2


class TrunkConnectionServiceStub(object):
    """A set of methods for managing TrunkConnection resources.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.cic.v1.TrunkConnectionService/Get',
                request_serializer=yandex_dot_cloud_dot_cic_dot_v1_dot_trunk__connection__service__pb2.GetTrunkConnectionRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_cic_dot_v1_dot_trunk__connection__pb2.TrunkConnection.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.cic.v1.TrunkConnectionService/List',
                request_serializer=yandex_dot_cloud_dot_cic_dot_v1_dot_trunk__connection__service__pb2.ListTrunkConnectionsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_cic_dot_v1_dot_trunk__connection__service__pb2.ListTrunkConnectionsResponse.FromString,
                )


class TrunkConnectionServiceServicer(object):
    """A set of methods for managing TrunkConnection resources.
    """

    def Get(self, request, context):
        """Returns the specified TrunkConnection resource.

        To get the list of available TrunkConnection resources, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of TrunkConnection resources in the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TrunkConnectionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_cic_dot_v1_dot_trunk__connection__service__pb2.GetTrunkConnectionRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_cic_dot_v1_dot_trunk__connection__pb2.TrunkConnection.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_cic_dot_v1_dot_trunk__connection__service__pb2.ListTrunkConnectionsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_cic_dot_v1_dot_trunk__connection__service__pb2.ListTrunkConnectionsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.cic.v1.TrunkConnectionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TrunkConnectionService(object):
    """A set of methods for managing TrunkConnection resources.
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.cic.v1.TrunkConnectionService/Get',
            yandex_dot_cloud_dot_cic_dot_v1_dot_trunk__connection__service__pb2.GetTrunkConnectionRequest.SerializeToString,
            yandex_dot_cloud_dot_cic_dot_v1_dot_trunk__connection__pb2.TrunkConnection.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.cic.v1.TrunkConnectionService/List',
            yandex_dot_cloud_dot_cic_dot_v1_dot_trunk__connection__service__pb2.ListTrunkConnectionsRequest.SerializeToString,
            yandex_dot_cloud_dot_cic_dot_v1_dot_trunk__connection__service__pb2.ListTrunkConnectionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)