# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.loadtesting.api.v1.test import test_pb2 as yandex_dot_cloud_dot_loadtesting_dot_api_dot_v1_dot_test_dot_test__pb2
from yandex.cloud.loadtesting.api.v1 import test_service_pb2 as yandex_dot_cloud_dot_loadtesting_dot_api_dot_v1_dot_test__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class TestServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/yandex.cloud.loadtesting.api.v1.TestService/Create',
                request_serializer=yandex_dot_cloud_dot_loadtesting_dot_api_dot_v1_dot_test__service__pb2.CreateTestRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Get = channel.unary_unary(
                '/yandex.cloud.loadtesting.api.v1.TestService/Get',
                request_serializer=yandex_dot_cloud_dot_loadtesting_dot_api_dot_v1_dot_test__service__pb2.GetTestRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_loadtesting_dot_api_dot_v1_dot_test_dot_test__pb2.Test.FromString,
                )


class TestServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TestServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_loadtesting_dot_api_dot_v1_dot_test__service__pb2.CreateTestRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_loadtesting_dot_api_dot_v1_dot_test__service__pb2.GetTestRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_loadtesting_dot_api_dot_v1_dot_test_dot_test__pb2.Test.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.loadtesting.api.v1.TestService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TestService(object):
    """Missing associated documentation comment in .proto file."""

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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.loadtesting.api.v1.TestService/Create',
            yandex_dot_cloud_dot_loadtesting_dot_api_dot_v1_dot_test__service__pb2.CreateTestRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.loadtesting.api.v1.TestService/Get',
            yandex_dot_cloud_dot_loadtesting_dot_api_dot_v1_dot_test__service__pb2.GetTestRequest.SerializeToString,
            yandex_dot_cloud_dot_loadtesting_dot_api_dot_v1_dot_test_dot_test__pb2.Test.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
