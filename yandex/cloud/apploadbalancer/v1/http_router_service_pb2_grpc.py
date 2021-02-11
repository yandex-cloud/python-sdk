# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.apploadbalancer.v1 import http_router_pb2 as yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_http__router__pb2
from yandex.cloud.apploadbalancer.v1 import http_router_service_pb2 as yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_http__router__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class HttpRouterServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.apploadbalancer.v1.HttpRouterService/Get',
                request_serializer=yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_http__router__service__pb2.GetHttpRouterRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_http__router__pb2.HttpRouter.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.apploadbalancer.v1.HttpRouterService/List',
                request_serializer=yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_http__router__service__pb2.ListHttpRoutersRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_http__router__service__pb2.ListHttpRoutersResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/yandex.cloud.apploadbalancer.v1.HttpRouterService/Create',
                request_serializer=yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_http__router__service__pb2.CreateHttpRouterRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Update = channel.unary_unary(
                '/yandex.cloud.apploadbalancer.v1.HttpRouterService/Update',
                request_serializer=yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_http__router__service__pb2.UpdateHttpRouterRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Delete = channel.unary_unary(
                '/yandex.cloud.apploadbalancer.v1.HttpRouterService/Delete',
                request_serializer=yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_http__router__service__pb2.DeleteHttpRouterRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.ListOperations = channel.unary_unary(
                '/yandex.cloud.apploadbalancer.v1.HttpRouterService/ListOperations',
                request_serializer=yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_http__router__service__pb2.ListHttpRouterOperationsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_http__router__service__pb2.ListHttpRouterOperationsResponse.FromString,
                )


class HttpRouterServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOperations(self, request, context):
        """Lists operations for the specified http router.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HttpRouterServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_http__router__service__pb2.GetHttpRouterRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_http__router__pb2.HttpRouter.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_http__router__service__pb2.ListHttpRoutersRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_http__router__service__pb2.ListHttpRoutersResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_http__router__service__pb2.CreateHttpRouterRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_http__router__service__pb2.UpdateHttpRouterRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_http__router__service__pb2.DeleteHttpRouterRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListOperations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOperations,
                    request_deserializer=yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_http__router__service__pb2.ListHttpRouterOperationsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_http__router__service__pb2.ListHttpRouterOperationsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.apploadbalancer.v1.HttpRouterService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class HttpRouterService(object):
    """Missing associated documentation comment in .proto file."""

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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.apploadbalancer.v1.HttpRouterService/Get',
            yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_http__router__service__pb2.GetHttpRouterRequest.SerializeToString,
            yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_http__router__pb2.HttpRouter.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.apploadbalancer.v1.HttpRouterService/List',
            yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_http__router__service__pb2.ListHttpRoutersRequest.SerializeToString,
            yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_http__router__service__pb2.ListHttpRoutersResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.apploadbalancer.v1.HttpRouterService/Create',
            yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_http__router__service__pb2.CreateHttpRouterRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.apploadbalancer.v1.HttpRouterService/Update',
            yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_http__router__service__pb2.UpdateHttpRouterRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.apploadbalancer.v1.HttpRouterService/Delete',
            yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_http__router__service__pb2.DeleteHttpRouterRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListOperations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.apploadbalancer.v1.HttpRouterService/ListOperations',
            yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_http__router__service__pb2.ListHttpRouterOperationsRequest.SerializeToString,
            yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_http__router__service__pb2.ListHttpRouterOperationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
