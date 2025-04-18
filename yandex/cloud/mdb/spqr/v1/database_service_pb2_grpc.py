# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.mdb.spqr.v1 import database_pb2 as yandex_dot_cloud_dot_mdb_dot_spqr_dot_v1_dot_database__pb2
from yandex.cloud.mdb.spqr.v1 import database_service_pb2 as yandex_dot_cloud_dot_mdb_dot_spqr_dot_v1_dot_database__service__pb2
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
        + f' but the generated code in yandex/cloud/mdb/spqr/v1/database_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class DatabaseServiceStub(object):
    """A set of methods for managing SPQR Database resources.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.mdb.spqr.v1.DatabaseService/Get',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_spqr_dot_v1_dot_database__service__pb2.GetDatabaseRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_mdb_dot_spqr_dot_v1_dot_database__pb2.Database.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/yandex.cloud.mdb.spqr.v1.DatabaseService/List',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_spqr_dot_v1_dot_database__service__pb2.ListDatabasesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_mdb_dot_spqr_dot_v1_dot_database__service__pb2.ListDatabasesResponse.FromString,
                _registered_method=True)
        self.ListAtRevision = channel.unary_unary(
                '/yandex.cloud.mdb.spqr.v1.DatabaseService/ListAtRevision',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_spqr_dot_v1_dot_database__service__pb2.ListDatabasesAtRevisionRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_mdb_dot_spqr_dot_v1_dot_database__service__pb2.ListDatabasesResponse.FromString,
                _registered_method=True)
        self.Create = channel.unary_unary(
                '/yandex.cloud.mdb.spqr.v1.DatabaseService/Create',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_spqr_dot_v1_dot_database__service__pb2.CreateDatabaseRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/yandex.cloud.mdb.spqr.v1.DatabaseService/Delete',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_spqr_dot_v1_dot_database__service__pb2.DeleteDatabaseRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)


class DatabaseServiceServicer(object):
    """A set of methods for managing SPQR Database resources.
    """

    def Get(self, request, context):
        """Returns the specified SPQR Database resource.

        To get the list of available SPQR Database resources, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of SPQR Database resources in the specified cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAtRevision(self, request, context):
        """Retrieves the list of SPQR Database resources in the specified cluster at the specified revision.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates a new SPQR database in the specified cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified SPQR database.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DatabaseServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_spqr_dot_v1_dot_database__service__pb2.GetDatabaseRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_mdb_dot_spqr_dot_v1_dot_database__pb2.Database.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_spqr_dot_v1_dot_database__service__pb2.ListDatabasesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_mdb_dot_spqr_dot_v1_dot_database__service__pb2.ListDatabasesResponse.SerializeToString,
            ),
            'ListAtRevision': grpc.unary_unary_rpc_method_handler(
                    servicer.ListAtRevision,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_spqr_dot_v1_dot_database__service__pb2.ListDatabasesAtRevisionRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_mdb_dot_spqr_dot_v1_dot_database__service__pb2.ListDatabasesResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_spqr_dot_v1_dot_database__service__pb2.CreateDatabaseRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_spqr_dot_v1_dot_database__service__pb2.DeleteDatabaseRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.mdb.spqr.v1.DatabaseService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.mdb.spqr.v1.DatabaseService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class DatabaseService(object):
    """A set of methods for managing SPQR Database resources.
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
            '/yandex.cloud.mdb.spqr.v1.DatabaseService/Get',
            yandex_dot_cloud_dot_mdb_dot_spqr_dot_v1_dot_database__service__pb2.GetDatabaseRequest.SerializeToString,
            yandex_dot_cloud_dot_mdb_dot_spqr_dot_v1_dot_database__pb2.Database.FromString,
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
            '/yandex.cloud.mdb.spqr.v1.DatabaseService/List',
            yandex_dot_cloud_dot_mdb_dot_spqr_dot_v1_dot_database__service__pb2.ListDatabasesRequest.SerializeToString,
            yandex_dot_cloud_dot_mdb_dot_spqr_dot_v1_dot_database__service__pb2.ListDatabasesResponse.FromString,
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
    def ListAtRevision(request,
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
            '/yandex.cloud.mdb.spqr.v1.DatabaseService/ListAtRevision',
            yandex_dot_cloud_dot_mdb_dot_spqr_dot_v1_dot_database__service__pb2.ListDatabasesAtRevisionRequest.SerializeToString,
            yandex_dot_cloud_dot_mdb_dot_spqr_dot_v1_dot_database__service__pb2.ListDatabasesResponse.FromString,
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
            '/yandex.cloud.mdb.spqr.v1.DatabaseService/Create',
            yandex_dot_cloud_dot_mdb_dot_spqr_dot_v1_dot_database__service__pb2.CreateDatabaseRequest.SerializeToString,
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
            '/yandex.cloud.mdb.spqr.v1.DatabaseService/Delete',
            yandex_dot_cloud_dot_mdb_dot_spqr_dot_v1_dot_database__service__pb2.DeleteDatabaseRequest.SerializeToString,
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
