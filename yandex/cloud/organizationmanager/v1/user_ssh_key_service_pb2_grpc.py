# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.organizationmanager.v1 import user_ssh_key_pb2 as yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_user__ssh__key__pb2
from yandex.cloud.organizationmanager.v1 import user_ssh_key_service_pb2 as yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_user__ssh__key__service__pb2

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
        + f' but the generated code in yandex/cloud/organizationmanager/v1/user_ssh_key_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class UserSshKeyServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.organizationmanager.v1.UserSshKeyService/Get',
                request_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_user__ssh__key__service__pb2.GetUserSshKeyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_user__ssh__key__pb2.UserSshKey.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/yandex.cloud.organizationmanager.v1.UserSshKeyService/List',
                request_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_user__ssh__key__service__pb2.ListUserSshKeysRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_user__ssh__key__service__pb2.ListUserSshKeysResponse.FromString,
                _registered_method=True)
        self.Create = channel.unary_unary(
                '/yandex.cloud.organizationmanager.v1.UserSshKeyService/Create',
                request_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_user__ssh__key__service__pb2.CreateUserSshKeyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Update = channel.unary_unary(
                '/yandex.cloud.organizationmanager.v1.UserSshKeyService/Update',
                request_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_user__ssh__key__service__pb2.UpdateUserSshKeyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/yandex.cloud.organizationmanager.v1.UserSshKeyService/Delete',
                request_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_user__ssh__key__service__pb2.DeleteUserSshKeyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)


class UserSshKeyServiceServicer(object):
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


def add_UserSshKeyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_user__ssh__key__service__pb2.GetUserSshKeyRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_user__ssh__key__pb2.UserSshKey.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_user__ssh__key__service__pb2.ListUserSshKeysRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_user__ssh__key__service__pb2.ListUserSshKeysResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_user__ssh__key__service__pb2.CreateUserSshKeyRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_user__ssh__key__service__pb2.UpdateUserSshKeyRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_user__ssh__key__service__pb2.DeleteUserSshKeyRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.organizationmanager.v1.UserSshKeyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.organizationmanager.v1.UserSshKeyService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class UserSshKeyService(object):
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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.organizationmanager.v1.UserSshKeyService/Get',
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_user__ssh__key__service__pb2.GetUserSshKeyRequest.SerializeToString,
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_user__ssh__key__pb2.UserSshKey.FromString,
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
            '/yandex.cloud.organizationmanager.v1.UserSshKeyService/List',
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_user__ssh__key__service__pb2.ListUserSshKeysRequest.SerializeToString,
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_user__ssh__key__service__pb2.ListUserSshKeysResponse.FromString,
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
            '/yandex.cloud.organizationmanager.v1.UserSshKeyService/Create',
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_user__ssh__key__service__pb2.CreateUserSshKeyRequest.SerializeToString,
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
            '/yandex.cloud.organizationmanager.v1.UserSshKeyService/Update',
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_user__ssh__key__service__pb2.UpdateUserSshKeyRequest.SerializeToString,
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
            '/yandex.cloud.organizationmanager.v1.UserSshKeyService/Delete',
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_user__ssh__key__service__pb2.DeleteUserSshKeyRequest.SerializeToString,
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
