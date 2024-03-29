# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.serverless.functions.v1 import network_service_pb2 as yandex_dot_cloud_dot_serverless_dot_functions_dot_v1_dot_network__service__pb2


class NetworkServiceStub(object):
    """A set of methods for managing VPC networks connected to serverless resources.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetUsed = channel.unary_unary(
                '/yandex.cloud.serverless.functions.v1.NetworkService/GetUsed',
                request_serializer=yandex_dot_cloud_dot_serverless_dot_functions_dot_v1_dot_network__service__pb2.GetUsedNetworkRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_serverless_dot_functions_dot_v1_dot_network__service__pb2.UsedNetwork.FromString,
                )
        self.ListUsed = channel.unary_unary(
                '/yandex.cloud.serverless.functions.v1.NetworkService/ListUsed',
                request_serializer=yandex_dot_cloud_dot_serverless_dot_functions_dot_v1_dot_network__service__pb2.ListUsedNetworksRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_serverless_dot_functions_dot_v1_dot_network__service__pb2.ListUsedNetworksResponse.FromString,
                )
        self.ListConnectedResources = channel.unary_unary(
                '/yandex.cloud.serverless.functions.v1.NetworkService/ListConnectedResources',
                request_serializer=yandex_dot_cloud_dot_serverless_dot_functions_dot_v1_dot_network__service__pb2.ListConnectedResourcesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_serverless_dot_functions_dot_v1_dot_network__service__pb2.ListConnectedResourcesResponse.FromString,
                )
        self.TriggerUsedCleanup = channel.unary_unary(
                '/yandex.cloud.serverless.functions.v1.NetworkService/TriggerUsedCleanup',
                request_serializer=yandex_dot_cloud_dot_serverless_dot_functions_dot_v1_dot_network__service__pb2.TriggerUsedNetworkCleanupRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_serverless_dot_functions_dot_v1_dot_network__service__pb2.TriggerUsedNetworkCleanupResponse.FromString,
                )


class NetworkServiceServicer(object):
    """A set of methods for managing VPC networks connected to serverless resources.
    """

    def GetUsed(self, request, context):
        """Returns the specified network used in serverless resources.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListUsed(self, request, context):
        """Retrieves the list of networks in the specified scope that are used in serverless resources.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListConnectedResources(self, request, context):
        """Retrieves the list of serverless resources connected to any network from the specified scope.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TriggerUsedCleanup(self, request, context):
        """Forces obsolete used network to start cleanup process as soon as possible.
        Invocation does not wait for start or end of the cleanup process.
        Second invocation with the same network does nothing until network is completely cleaned-up.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NetworkServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetUsed': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUsed,
                    request_deserializer=yandex_dot_cloud_dot_serverless_dot_functions_dot_v1_dot_network__service__pb2.GetUsedNetworkRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_serverless_dot_functions_dot_v1_dot_network__service__pb2.UsedNetwork.SerializeToString,
            ),
            'ListUsed': grpc.unary_unary_rpc_method_handler(
                    servicer.ListUsed,
                    request_deserializer=yandex_dot_cloud_dot_serverless_dot_functions_dot_v1_dot_network__service__pb2.ListUsedNetworksRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_serverless_dot_functions_dot_v1_dot_network__service__pb2.ListUsedNetworksResponse.SerializeToString,
            ),
            'ListConnectedResources': grpc.unary_unary_rpc_method_handler(
                    servicer.ListConnectedResources,
                    request_deserializer=yandex_dot_cloud_dot_serverless_dot_functions_dot_v1_dot_network__service__pb2.ListConnectedResourcesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_serverless_dot_functions_dot_v1_dot_network__service__pb2.ListConnectedResourcesResponse.SerializeToString,
            ),
            'TriggerUsedCleanup': grpc.unary_unary_rpc_method_handler(
                    servicer.TriggerUsedCleanup,
                    request_deserializer=yandex_dot_cloud_dot_serverless_dot_functions_dot_v1_dot_network__service__pb2.TriggerUsedNetworkCleanupRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_serverless_dot_functions_dot_v1_dot_network__service__pb2.TriggerUsedNetworkCleanupResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.serverless.functions.v1.NetworkService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NetworkService(object):
    """A set of methods for managing VPC networks connected to serverless resources.
    """

    @staticmethod
    def GetUsed(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.serverless.functions.v1.NetworkService/GetUsed',
            yandex_dot_cloud_dot_serverless_dot_functions_dot_v1_dot_network__service__pb2.GetUsedNetworkRequest.SerializeToString,
            yandex_dot_cloud_dot_serverless_dot_functions_dot_v1_dot_network__service__pb2.UsedNetwork.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListUsed(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.serverless.functions.v1.NetworkService/ListUsed',
            yandex_dot_cloud_dot_serverless_dot_functions_dot_v1_dot_network__service__pb2.ListUsedNetworksRequest.SerializeToString,
            yandex_dot_cloud_dot_serverless_dot_functions_dot_v1_dot_network__service__pb2.ListUsedNetworksResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListConnectedResources(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.serverless.functions.v1.NetworkService/ListConnectedResources',
            yandex_dot_cloud_dot_serverless_dot_functions_dot_v1_dot_network__service__pb2.ListConnectedResourcesRequest.SerializeToString,
            yandex_dot_cloud_dot_serverless_dot_functions_dot_v1_dot_network__service__pb2.ListConnectedResourcesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TriggerUsedCleanup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.serverless.functions.v1.NetworkService/TriggerUsedCleanup',
            yandex_dot_cloud_dot_serverless_dot_functions_dot_v1_dot_network__service__pb2.TriggerUsedNetworkCleanupRequest.SerializeToString,
            yandex_dot_cloud_dot_serverless_dot_functions_dot_v1_dot_network__service__pb2.TriggerUsedNetworkCleanupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
