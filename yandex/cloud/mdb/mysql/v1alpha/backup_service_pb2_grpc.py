# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.mdb.mysql.v1alpha import backup_pb2 as yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1alpha_dot_backup__pb2
from yandex.cloud.mdb.mysql.v1alpha import backup_service_pb2 as yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1alpha_dot_backup__service__pb2

GRPC_GENERATED_VERSION = '1.68.1'
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
        + f' but the generated code in yandex/cloud/mdb/mysql/v1alpha/backup_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class BackupServiceStub(object):
    """A set of methods for managing MySQL backups.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.mdb.mysql.v1alpha.BackupService/Get',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1alpha_dot_backup__service__pb2.GetBackupRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1alpha_dot_backup__pb2.Backup.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/yandex.cloud.mdb.mysql.v1alpha.BackupService/List',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1alpha_dot_backup__service__pb2.ListBackupsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1alpha_dot_backup__service__pb2.ListBackupsResponse.FromString,
                _registered_method=True)


class BackupServiceServicer(object):
    """A set of methods for managing MySQL backups.
    """

    def Get(self, request, context):
        """Returns the specified MySQL backup.

        To get the list of available MySQL backups, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of MySQL backups available for the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BackupServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1alpha_dot_backup__service__pb2.GetBackupRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1alpha_dot_backup__pb2.Backup.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1alpha_dot_backup__service__pb2.ListBackupsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1alpha_dot_backup__service__pb2.ListBackupsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.mdb.mysql.v1alpha.BackupService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.mdb.mysql.v1alpha.BackupService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class BackupService(object):
    """A set of methods for managing MySQL backups.
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
            '/yandex.cloud.mdb.mysql.v1alpha.BackupService/Get',
            yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1alpha_dot_backup__service__pb2.GetBackupRequest.SerializeToString,
            yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1alpha_dot_backup__pb2.Backup.FromString,
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
            '/yandex.cloud.mdb.mysql.v1alpha.BackupService/List',
            yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1alpha_dot_backup__service__pb2.ListBackupsRequest.SerializeToString,
            yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1alpha_dot_backup__service__pb2.ListBackupsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
