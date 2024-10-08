# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.cloudrouter.v1 import routing_instance_pb2 as yandex_dot_cloud_dot_cloudrouter_dot_v1_dot_routing__instance__pb2
from yandex.cloud.cloudrouter.v1 import routing_instance_service_pb2 as yandex_dot_cloud_dot_cloudrouter_dot_v1_dot_routing__instance__service__pb2


class RoutingInstanceServiceStub(object):
    """A set of methods for managing RoutingInstance resources.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.cloudrouter.v1.RoutingInstanceService/Get',
                request_serializer=yandex_dot_cloud_dot_cloudrouter_dot_v1_dot_routing__instance__service__pb2.GetRoutingInstanceRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_cloudrouter_dot_v1_dot_routing__instance__pb2.RoutingInstance.FromString,
                )
        self.GetByVpcNetworkId = channel.unary_unary(
                '/yandex.cloud.cloudrouter.v1.RoutingInstanceService/GetByVpcNetworkId',
                request_serializer=yandex_dot_cloud_dot_cloudrouter_dot_v1_dot_routing__instance__service__pb2.GetRoutingInstanceByVpcNetworkIdRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_cloudrouter_dot_v1_dot_routing__instance__pb2.RoutingInstance.FromString,
                )
        self.GetByCicPrivateConnectionId = channel.unary_unary(
                '/yandex.cloud.cloudrouter.v1.RoutingInstanceService/GetByCicPrivateConnectionId',
                request_serializer=yandex_dot_cloud_dot_cloudrouter_dot_v1_dot_routing__instance__service__pb2.GetRoutingInstanceByCicPrivateConnectionIdRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_cloudrouter_dot_v1_dot_routing__instance__pb2.RoutingInstance.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.cloudrouter.v1.RoutingInstanceService/List',
                request_serializer=yandex_dot_cloud_dot_cloudrouter_dot_v1_dot_routing__instance__service__pb2.ListRoutingInstancesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_cloudrouter_dot_v1_dot_routing__instance__service__pb2.ListRoutingInstancesResponse.FromString,
                )


class RoutingInstanceServiceServicer(object):
    """A set of methods for managing RoutingInstance resources.
    """

    def Get(self, request, context):
        """Returns the specified RoutingInstance resource.

        To get the list of available RoutingInstance resources, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetByVpcNetworkId(self, request, context):
        """Returns the RoutingInstance resource by vpcNetworkId

        To get the list of available RoutingInstance resources, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetByCicPrivateConnectionId(self, request, context):
        """Returns the RoutingInstance resource by cicPrivateConnectionId

        To get the list of available RoutingInstance resources, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of RoutingInstance resources in the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RoutingInstanceServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_cloudrouter_dot_v1_dot_routing__instance__service__pb2.GetRoutingInstanceRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_cloudrouter_dot_v1_dot_routing__instance__pb2.RoutingInstance.SerializeToString,
            ),
            'GetByVpcNetworkId': grpc.unary_unary_rpc_method_handler(
                    servicer.GetByVpcNetworkId,
                    request_deserializer=yandex_dot_cloud_dot_cloudrouter_dot_v1_dot_routing__instance__service__pb2.GetRoutingInstanceByVpcNetworkIdRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_cloudrouter_dot_v1_dot_routing__instance__pb2.RoutingInstance.SerializeToString,
            ),
            'GetByCicPrivateConnectionId': grpc.unary_unary_rpc_method_handler(
                    servicer.GetByCicPrivateConnectionId,
                    request_deserializer=yandex_dot_cloud_dot_cloudrouter_dot_v1_dot_routing__instance__service__pb2.GetRoutingInstanceByCicPrivateConnectionIdRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_cloudrouter_dot_v1_dot_routing__instance__pb2.RoutingInstance.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_cloudrouter_dot_v1_dot_routing__instance__service__pb2.ListRoutingInstancesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_cloudrouter_dot_v1_dot_routing__instance__service__pb2.ListRoutingInstancesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.cloudrouter.v1.RoutingInstanceService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RoutingInstanceService(object):
    """A set of methods for managing RoutingInstance resources.
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.cloudrouter.v1.RoutingInstanceService/Get',
            yandex_dot_cloud_dot_cloudrouter_dot_v1_dot_routing__instance__service__pb2.GetRoutingInstanceRequest.SerializeToString,
            yandex_dot_cloud_dot_cloudrouter_dot_v1_dot_routing__instance__pb2.RoutingInstance.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetByVpcNetworkId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.cloudrouter.v1.RoutingInstanceService/GetByVpcNetworkId',
            yandex_dot_cloud_dot_cloudrouter_dot_v1_dot_routing__instance__service__pb2.GetRoutingInstanceByVpcNetworkIdRequest.SerializeToString,
            yandex_dot_cloud_dot_cloudrouter_dot_v1_dot_routing__instance__pb2.RoutingInstance.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetByCicPrivateConnectionId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.cloudrouter.v1.RoutingInstanceService/GetByCicPrivateConnectionId',
            yandex_dot_cloud_dot_cloudrouter_dot_v1_dot_routing__instance__service__pb2.GetRoutingInstanceByCicPrivateConnectionIdRequest.SerializeToString,
            yandex_dot_cloud_dot_cloudrouter_dot_v1_dot_routing__instance__pb2.RoutingInstance.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.cloudrouter.v1.RoutingInstanceService/List',
            yandex_dot_cloud_dot_cloudrouter_dot_v1_dot_routing__instance__service__pb2.ListRoutingInstancesRequest.SerializeToString,
            yandex_dot_cloud_dot_cloudrouter_dot_v1_dot_routing__instance__service__pb2.ListRoutingInstancesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
