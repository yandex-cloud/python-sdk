# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.backup.v1 import provider_service_pb2 as yandex_dot_cloud_dot_backup_dot_v1_dot_provider__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class ProviderServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Activate = channel.unary_unary(
                '/yandex.cloud.backup.v1.ProviderService/Activate',
                request_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_provider__service__pb2.ActivateProviderRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.ListActivated = channel.unary_unary(
                '/yandex.cloud.backup.v1.ProviderService/ListActivated',
                request_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_provider__service__pb2.ListActivatedProvidersRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_provider__service__pb2.ListActivatedProvidersResponse.FromString,
                )


class ProviderServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Activate(self, request, context):
        """Activate provider for specified client.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListActivated(self, request, context):
        """List activated providers for specified client.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProviderServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Activate': grpc.unary_unary_rpc_method_handler(
                    servicer.Activate,
                    request_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_provider__service__pb2.ActivateProviderRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListActivated': grpc.unary_unary_rpc_method_handler(
                    servicer.ListActivated,
                    request_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_provider__service__pb2.ListActivatedProvidersRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_provider__service__pb2.ListActivatedProvidersResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.backup.v1.ProviderService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProviderService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Activate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.backup.v1.ProviderService/Activate',
            yandex_dot_cloud_dot_backup_dot_v1_dot_provider__service__pb2.ActivateProviderRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListActivated(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.backup.v1.ProviderService/ListActivated',
            yandex_dot_cloud_dot_backup_dot_v1_dot_provider__service__pb2.ListActivatedProvidersRequest.SerializeToString,
            yandex_dot_cloud_dot_backup_dot_v1_dot_provider__service__pb2.ListActivatedProvidersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)