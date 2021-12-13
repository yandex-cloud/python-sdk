# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.datatransfer.v1 import endpoint_pb2 as yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint__pb2
from yandex.cloud.datatransfer.v1 import endpoint_service_pb2 as yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class EndpointServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.datatransfer.v1.EndpointService/Get',
                request_serializer=yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint__service__pb2.GetEndpointRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint__pb2.Endpoint.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.datatransfer.v1.EndpointService/List',
                request_serializer=yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint__service__pb2.ListEndpointsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint__service__pb2.ListEndpointsResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/yandex.cloud.datatransfer.v1.EndpointService/Create',
                request_serializer=yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint__service__pb2.CreateEndpointRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Update = channel.unary_unary(
                '/yandex.cloud.datatransfer.v1.EndpointService/Update',
                request_serializer=yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint__service__pb2.UpdateEndpointRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Delete = channel.unary_unary(
                '/yandex.cloud.datatransfer.v1.EndpointService/Delete',
                request_serializer=yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint__service__pb2.DeleteEndpointRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )


class EndpointServiceServicer(object):
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


def add_EndpointServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint__service__pb2.GetEndpointRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint__pb2.Endpoint.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint__service__pb2.ListEndpointsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint__service__pb2.ListEndpointsResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint__service__pb2.CreateEndpointRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint__service__pb2.UpdateEndpointRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint__service__pb2.DeleteEndpointRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.datatransfer.v1.EndpointService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EndpointService(object):
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.datatransfer.v1.EndpointService/Get',
            yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint__service__pb2.GetEndpointRequest.SerializeToString,
            yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint__pb2.Endpoint.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.datatransfer.v1.EndpointService/List',
            yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint__service__pb2.ListEndpointsRequest.SerializeToString,
            yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint__service__pb2.ListEndpointsResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.datatransfer.v1.EndpointService/Create',
            yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint__service__pb2.CreateEndpointRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.datatransfer.v1.EndpointService/Update',
            yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint__service__pb2.UpdateEndpointRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.datatransfer.v1.EndpointService/Delete',
            yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint__service__pb2.DeleteEndpointRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)