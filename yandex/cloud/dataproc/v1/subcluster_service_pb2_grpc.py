# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.dataproc.v1 import subcluster_pb2 as yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__pb2
from yandex.cloud.dataproc.v1 import subcluster_service_pb2 as yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__service__pb2
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
        + f' but the generated code in yandex/cloud/dataproc/v1/subcluster_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class SubclusterServiceStub(object):
    """A set of methods for managing Yandex Data Processing subclusters.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.dataproc.v1.SubclusterService/Get',
                request_serializer=yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__service__pb2.GetSubclusterRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__pb2.Subcluster.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/yandex.cloud.dataproc.v1.SubclusterService/List',
                request_serializer=yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__service__pb2.ListSubclustersRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__service__pb2.ListSubclustersResponse.FromString,
                _registered_method=True)
        self.Create = channel.unary_unary(
                '/yandex.cloud.dataproc.v1.SubclusterService/Create',
                request_serializer=yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__service__pb2.CreateSubclusterRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Update = channel.unary_unary(
                '/yandex.cloud.dataproc.v1.SubclusterService/Update',
                request_serializer=yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__service__pb2.UpdateSubclusterRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/yandex.cloud.dataproc.v1.SubclusterService/Delete',
                request_serializer=yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__service__pb2.DeleteSubclusterRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)


class SubclusterServiceServicer(object):
    """A set of methods for managing Yandex Data Processing subclusters.
    """

    def Get(self, request, context):
        """Returns the specified subcluster.

        To get the list of all available subclusters, make a [SubclusterService.List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves a list of subclusters in the specified cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates a subcluster in the specified cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates the specified subcluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified subcluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SubclusterServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__service__pb2.GetSubclusterRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__pb2.Subcluster.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__service__pb2.ListSubclustersRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__service__pb2.ListSubclustersResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__service__pb2.CreateSubclusterRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__service__pb2.UpdateSubclusterRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__service__pb2.DeleteSubclusterRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.dataproc.v1.SubclusterService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.dataproc.v1.SubclusterService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class SubclusterService(object):
    """A set of methods for managing Yandex Data Processing subclusters.
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
            '/yandex.cloud.dataproc.v1.SubclusterService/Get',
            yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__service__pb2.GetSubclusterRequest.SerializeToString,
            yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__pb2.Subcluster.FromString,
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
            '/yandex.cloud.dataproc.v1.SubclusterService/List',
            yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__service__pb2.ListSubclustersRequest.SerializeToString,
            yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__service__pb2.ListSubclustersResponse.FromString,
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
            '/yandex.cloud.dataproc.v1.SubclusterService/Create',
            yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__service__pb2.CreateSubclusterRequest.SerializeToString,
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
            '/yandex.cloud.dataproc.v1.SubclusterService/Update',
            yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__service__pb2.UpdateSubclusterRequest.SerializeToString,
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
            '/yandex.cloud.dataproc.v1.SubclusterService/Delete',
            yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__service__pb2.DeleteSubclusterRequest.SerializeToString,
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
