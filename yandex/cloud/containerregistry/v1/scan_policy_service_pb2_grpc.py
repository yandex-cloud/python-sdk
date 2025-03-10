# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.containerregistry.v1 import scan_policy_pb2 as yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__pb2
from yandex.cloud.containerregistry.v1 import scan_policy_service_pb2 as yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2

GRPC_GENERATED_VERSION = '1.70.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in yandex/cloud/containerregistry/v1/scan_policy_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


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
                _registered_method=True)
        self.GetByRegistry = channel.unary_unary(
                '/yandex.cloud.containerregistry.v1.ScanPolicyService/GetByRegistry',
                request_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__service__pb2.GetScanPolicyByRegistryRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__pb2.ScanPolicy.FromString,
                _registered_method=True)
        self.Create = channel.unary_unary(
                '/yandex.cloud.containerregistry.v1.ScanPolicyService/Create',
                request_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__service__pb2.CreateScanPolicyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Update = channel.unary_unary(
                '/yandex.cloud.containerregistry.v1.ScanPolicyService/Update',
                request_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__service__pb2.UpdateScanPolicyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/yandex.cloud.containerregistry.v1.ScanPolicyService/Delete',
                request_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__service__pb2.DeleteScanPolicyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)


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
    server.add_registered_method_handlers('yandex.cloud.containerregistry.v1.ScanPolicyService', rpc_method_handlers)


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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.containerregistry.v1.ScanPolicyService/Get',
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__service__pb2.GetScanPolicyRequest.SerializeToString,
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__pb2.ScanPolicy.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.containerregistry.v1.ScanPolicyService/GetByRegistry',
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__service__pb2.GetScanPolicyByRegistryRequest.SerializeToString,
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__pb2.ScanPolicy.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.containerregistry.v1.ScanPolicyService/Create',
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__service__pb2.CreateScanPolicyRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.containerregistry.v1.ScanPolicyService/Update',
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__service__pb2.UpdateScanPolicyRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.containerregistry.v1.ScanPolicyService/Delete',
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__service__pb2.DeleteScanPolicyRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
