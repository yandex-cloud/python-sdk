# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.containerregistry.v1 import scan_policy_pb2 as yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__pb2
from yandex.cloud.containerregistry.v1 import scan_policy_service_pb2 as yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class ScanPolicyServiceStub(object):
    """A set of methods for managing scan policy resources.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.containerregistry.v1.ScanPolicyService/Get',
                request_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__service__pb2.GetScanPolicyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__pb2.ScanPolicy.FromString,
                )
        self.GetByRegistry = channel.unary_unary(
                '/yandex.cloud.containerregistry.v1.ScanPolicyService/GetByRegistry',
                request_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__service__pb2.GetScanPolicyByRegistryRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__pb2.ScanPolicy.FromString,
                )
        self.Create = channel.unary_unary(
                '/yandex.cloud.containerregistry.v1.ScanPolicyService/Create',
                request_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__service__pb2.CreateScanPolicyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Update = channel.unary_unary(
                '/yandex.cloud.containerregistry.v1.ScanPolicyService/Update',
                request_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__service__pb2.UpdateScanPolicyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Delete = channel.unary_unary(
                '/yandex.cloud.containerregistry.v1.ScanPolicyService/Delete',
                request_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__service__pb2.DeleteScanPolicyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )


class ScanPolicyServiceServicer(object):
    """A set of methods for managing scan policy resources.
    """

    def Get(self, request, context):
        """Returns the specified scan policy.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetByRegistry(self, request, context):
        """Returns scan policy for the registry if any exists.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates a scan policy for the specified registry.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates the specified scan policy.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified scan policy.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ScanPolicyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__service__pb2.GetScanPolicyRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__pb2.ScanPolicy.SerializeToString,
            ),
            'GetByRegistry': grpc.unary_unary_rpc_method_handler(
                    servicer.GetByRegistry,
                    request_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__service__pb2.GetScanPolicyByRegistryRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__pb2.ScanPolicy.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__service__pb2.CreateScanPolicyRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__service__pb2.UpdateScanPolicyRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__service__pb2.DeleteScanPolicyRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.containerregistry.v1.ScanPolicyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ScanPolicyService(object):
    """A set of methods for managing scan policy resources.
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.containerregistry.v1.ScanPolicyService/Get',
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__service__pb2.GetScanPolicyRequest.SerializeToString,
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__pb2.ScanPolicy.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetByRegistry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.containerregistry.v1.ScanPolicyService/GetByRegistry',
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__service__pb2.GetScanPolicyByRegistryRequest.SerializeToString,
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__pb2.ScanPolicy.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.containerregistry.v1.ScanPolicyService/Create',
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__service__pb2.CreateScanPolicyRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.containerregistry.v1.ScanPolicyService/Update',
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__service__pb2.UpdateScanPolicyRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.containerregistry.v1.ScanPolicyService/Delete',
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__service__pb2.DeleteScanPolicyRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
