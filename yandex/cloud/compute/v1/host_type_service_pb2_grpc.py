# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.compute.v1 import host_type_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_host__type__pb2
from yandex.cloud.compute.v1 import host_type_service_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_host__type__service__pb2

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
        + f' but the generated code in yandex/cloud/compute/v1/host_type_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class HostTypeServiceStub(object):
    """Set of methods to view possible host configurations.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.compute.v1.HostTypeService/Get',
                request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_host__type__service__pb2.GetHostTypeRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_host__type__pb2.HostType.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/yandex.cloud.compute.v1.HostTypeService/List',
                request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_host__type__service__pb2.ListHostTypesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_host__type__service__pb2.ListHostTypesResponse.FromString,
                _registered_method=True)


class HostTypeServiceServicer(object):
    """Set of methods to view possible host configurations.
    """

    def Get(self, request, context):
        """Returns information about specified host type.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """List avaliable host types.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HostTypeServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_host__type__service__pb2.GetHostTypeRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_host__type__pb2.HostType.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_host__type__service__pb2.ListHostTypesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_host__type__service__pb2.ListHostTypesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.compute.v1.HostTypeService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.compute.v1.HostTypeService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class HostTypeService(object):
    """Set of methods to view possible host configurations.
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
            '/yandex.cloud.compute.v1.HostTypeService/Get',
            yandex_dot_cloud_dot_compute_dot_v1_dot_host__type__service__pb2.GetHostTypeRequest.SerializeToString,
            yandex_dot_cloud_dot_compute_dot_v1_dot_host__type__pb2.HostType.FromString,
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
            '/yandex.cloud.compute.v1.HostTypeService/List',
            yandex_dot_cloud_dot_compute_dot_v1_dot_host__type__service__pb2.ListHostTypesRequest.SerializeToString,
            yandex_dot_cloud_dot_compute_dot_v1_dot_host__type__service__pb2.ListHostTypesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
