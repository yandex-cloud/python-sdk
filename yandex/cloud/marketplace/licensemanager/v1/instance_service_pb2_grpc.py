# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.marketplace.licensemanager.v1 import instance_pb2 as yandex_dot_cloud_dot_marketplace_dot_licensemanager_dot_v1_dot_instance__pb2
from yandex.cloud.marketplace.licensemanager.v1 import instance_service_pb2 as yandex_dot_cloud_dot_marketplace_dot_licensemanager_dot_v1_dot_instance__service__pb2

GRPC_GENERATED_VERSION = '1.63.0'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in yandex/cloud/marketplace/licensemanager/v1/instance_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class InstanceServiceStub(object):
    """A set of methods for managing subscription instances.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.marketplace.licensemanager.v1.InstanceService/Get',
                request_serializer=yandex_dot_cloud_dot_marketplace_dot_licensemanager_dot_v1_dot_instance__service__pb2.GetInstanceRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_marketplace_dot_licensemanager_dot_v1_dot_instance__pb2.Instance.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/yandex.cloud.marketplace.licensemanager.v1.InstanceService/List',
                request_serializer=yandex_dot_cloud_dot_marketplace_dot_licensemanager_dot_v1_dot_instance__service__pb2.ListInstancesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_marketplace_dot_licensemanager_dot_v1_dot_instance__service__pb2.ListInstancesResponse.FromString,
                _registered_method=True)


class InstanceServiceServicer(object):
    """A set of methods for managing subscription instances.
    """

    def Get(self, request, context):
        """Returns the specified subscription instance.

        To get the list of all available subscription instances, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of subscription instances in the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InstanceServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_marketplace_dot_licensemanager_dot_v1_dot_instance__service__pb2.GetInstanceRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_marketplace_dot_licensemanager_dot_v1_dot_instance__pb2.Instance.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_marketplace_dot_licensemanager_dot_v1_dot_instance__service__pb2.ListInstancesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_marketplace_dot_licensemanager_dot_v1_dot_instance__service__pb2.ListInstancesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.marketplace.licensemanager.v1.InstanceService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InstanceService(object):
    """A set of methods for managing subscription instances.
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
            '/yandex.cloud.marketplace.licensemanager.v1.InstanceService/Get',
            yandex_dot_cloud_dot_marketplace_dot_licensemanager_dot_v1_dot_instance__service__pb2.GetInstanceRequest.SerializeToString,
            yandex_dot_cloud_dot_marketplace_dot_licensemanager_dot_v1_dot_instance__pb2.Instance.FromString,
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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.marketplace.licensemanager.v1.InstanceService/List',
            yandex_dot_cloud_dot_marketplace_dot_licensemanager_dot_v1_dot_instance__service__pb2.ListInstancesRequest.SerializeToString,
            yandex_dot_cloud_dot_marketplace_dot_licensemanager_dot_v1_dot_instance__service__pb2.ListInstancesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
