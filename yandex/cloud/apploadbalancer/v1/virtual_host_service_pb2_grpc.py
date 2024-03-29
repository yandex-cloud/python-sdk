# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.apploadbalancer.v1 import virtual_host_pb2 as yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_virtual__host__pb2
from yandex.cloud.apploadbalancer.v1 import virtual_host_service_pb2 as yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_virtual__host__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class VirtualHostServiceStub(object):
    """A set of methods for managing virtual hosts of HTTP routers.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.apploadbalancer.v1.VirtualHostService/Get',
                request_serializer=yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_virtual__host__service__pb2.GetVirtualHostRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_virtual__host__pb2.VirtualHost.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.apploadbalancer.v1.VirtualHostService/List',
                request_serializer=yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_virtual__host__service__pb2.ListVirtualHostsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_virtual__host__service__pb2.ListVirtualHostsResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/yandex.cloud.apploadbalancer.v1.VirtualHostService/Create',
                request_serializer=yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_virtual__host__service__pb2.CreateVirtualHostRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Update = channel.unary_unary(
                '/yandex.cloud.apploadbalancer.v1.VirtualHostService/Update',
                request_serializer=yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_virtual__host__service__pb2.UpdateVirtualHostRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Delete = channel.unary_unary(
                '/yandex.cloud.apploadbalancer.v1.VirtualHostService/Delete',
                request_serializer=yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_virtual__host__service__pb2.DeleteVirtualHostRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.RemoveRoute = channel.unary_unary(
                '/yandex.cloud.apploadbalancer.v1.VirtualHostService/RemoveRoute',
                request_serializer=yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_virtual__host__service__pb2.RemoveRouteRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.UpdateRoute = channel.unary_unary(
                '/yandex.cloud.apploadbalancer.v1.VirtualHostService/UpdateRoute',
                request_serializer=yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_virtual__host__service__pb2.UpdateRouteRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )


class VirtualHostServiceServicer(object):
    """A set of methods for managing virtual hosts of HTTP routers.
    """

    def Get(self, request, context):
        """Returns the specified virtual host.

        To get the list of all virtual hosts of an HTTP router, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Lists virtual hosts of the specified HTTP router.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates a virtual host in the specified HTTP router.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates the specified virtual host of the specified HTTP router.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified virtual host.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveRoute(self, request, context):
        """Deletes the specified route from the specified virtual host.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateRoute(self, request, context):
        """Updates the specified route of the specified virtual host.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VirtualHostServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_virtual__host__service__pb2.GetVirtualHostRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_virtual__host__pb2.VirtualHost.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_virtual__host__service__pb2.ListVirtualHostsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_virtual__host__service__pb2.ListVirtualHostsResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_virtual__host__service__pb2.CreateVirtualHostRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_virtual__host__service__pb2.UpdateVirtualHostRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_virtual__host__service__pb2.DeleteVirtualHostRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'RemoveRoute': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveRoute,
                    request_deserializer=yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_virtual__host__service__pb2.RemoveRouteRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'UpdateRoute': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateRoute,
                    request_deserializer=yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_virtual__host__service__pb2.UpdateRouteRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.apploadbalancer.v1.VirtualHostService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class VirtualHostService(object):
    """A set of methods for managing virtual hosts of HTTP routers.
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.apploadbalancer.v1.VirtualHostService/Get',
            yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_virtual__host__service__pb2.GetVirtualHostRequest.SerializeToString,
            yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_virtual__host__pb2.VirtualHost.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.apploadbalancer.v1.VirtualHostService/List',
            yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_virtual__host__service__pb2.ListVirtualHostsRequest.SerializeToString,
            yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_virtual__host__service__pb2.ListVirtualHostsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.apploadbalancer.v1.VirtualHostService/Create',
            yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_virtual__host__service__pb2.CreateVirtualHostRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.apploadbalancer.v1.VirtualHostService/Update',
            yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_virtual__host__service__pb2.UpdateVirtualHostRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.apploadbalancer.v1.VirtualHostService/Delete',
            yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_virtual__host__service__pb2.DeleteVirtualHostRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveRoute(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.apploadbalancer.v1.VirtualHostService/RemoveRoute',
            yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_virtual__host__service__pb2.RemoveRouteRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateRoute(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.apploadbalancer.v1.VirtualHostService/UpdateRoute',
            yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_virtual__host__service__pb2.UpdateRouteRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
