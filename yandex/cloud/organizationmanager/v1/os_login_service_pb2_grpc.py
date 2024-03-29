# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.organizationmanager.v1 import os_login_service_pb2 as yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_os__login__service__pb2


class OsLoginServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetSettings = channel.unary_unary(
                '/yandex.cloud.organizationmanager.v1.OsLoginService/GetSettings',
                request_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_os__login__service__pb2.GetOsLoginSettingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_os__login__service__pb2.OsLoginSettings.FromString,
                )
        self.UpdateSettings = channel.unary_unary(
                '/yandex.cloud.organizationmanager.v1.OsLoginService/UpdateSettings',
                request_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_os__login__service__pb2.UpdateOsLoginSettingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.GetProfile = channel.unary_unary(
                '/yandex.cloud.organizationmanager.v1.OsLoginService/GetProfile',
                request_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_os__login__service__pb2.GetOsLoginProfileRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_os__login__service__pb2.OsLoginProfile.FromString,
                )
        self.ListProfiles = channel.unary_unary(
                '/yandex.cloud.organizationmanager.v1.OsLoginService/ListProfiles',
                request_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_os__login__service__pb2.ListOsLoginProfilesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_os__login__service__pb2.ListOsLoginProfilesResponse.FromString,
                )
        self.CreateProfile = channel.unary_unary(
                '/yandex.cloud.organizationmanager.v1.OsLoginService/CreateProfile',
                request_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_os__login__service__pb2.CreateOsLoginProfileRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.UpdateProfile = channel.unary_unary(
                '/yandex.cloud.organizationmanager.v1.OsLoginService/UpdateProfile',
                request_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_os__login__service__pb2.UpdateOsLoginProfileRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.SetDefaultProfile = channel.unary_unary(
                '/yandex.cloud.organizationmanager.v1.OsLoginService/SetDefaultProfile',
                request_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_os__login__service__pb2.SetDefaultOsLoginProfileRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.DeleteProfile = channel.unary_unary(
                '/yandex.cloud.organizationmanager.v1.OsLoginService/DeleteProfile',
                request_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_os__login__service__pb2.DeleteOsLoginProfileRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )


class OsLoginServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetSettings(self, request, context):
        """OsLogin settings
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateSettings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProfile(self, request, context):
        """OsLogin Profiles
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListProfiles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateProfile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateProfile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetDefaultProfile(self, request, context):
        """Sets a profile as a default for the subject assigned to this profile
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteProfile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OsLoginServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetSettings': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSettings,
                    request_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_os__login__service__pb2.GetOsLoginSettingsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_os__login__service__pb2.OsLoginSettings.SerializeToString,
            ),
            'UpdateSettings': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateSettings,
                    request_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_os__login__service__pb2.UpdateOsLoginSettingsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'GetProfile': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProfile,
                    request_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_os__login__service__pb2.GetOsLoginProfileRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_os__login__service__pb2.OsLoginProfile.SerializeToString,
            ),
            'ListProfiles': grpc.unary_unary_rpc_method_handler(
                    servicer.ListProfiles,
                    request_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_os__login__service__pb2.ListOsLoginProfilesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_os__login__service__pb2.ListOsLoginProfilesResponse.SerializeToString,
            ),
            'CreateProfile': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateProfile,
                    request_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_os__login__service__pb2.CreateOsLoginProfileRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'UpdateProfile': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateProfile,
                    request_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_os__login__service__pb2.UpdateOsLoginProfileRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'SetDefaultProfile': grpc.unary_unary_rpc_method_handler(
                    servicer.SetDefaultProfile,
                    request_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_os__login__service__pb2.SetDefaultOsLoginProfileRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'DeleteProfile': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteProfile,
                    request_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_os__login__service__pb2.DeleteOsLoginProfileRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.organizationmanager.v1.OsLoginService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OsLoginService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetSettings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.organizationmanager.v1.OsLoginService/GetSettings',
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_os__login__service__pb2.GetOsLoginSettingsRequest.SerializeToString,
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_os__login__service__pb2.OsLoginSettings.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateSettings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.organizationmanager.v1.OsLoginService/UpdateSettings',
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_os__login__service__pb2.UpdateOsLoginSettingsRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProfile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.organizationmanager.v1.OsLoginService/GetProfile',
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_os__login__service__pb2.GetOsLoginProfileRequest.SerializeToString,
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_os__login__service__pb2.OsLoginProfile.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListProfiles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.organizationmanager.v1.OsLoginService/ListProfiles',
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_os__login__service__pb2.ListOsLoginProfilesRequest.SerializeToString,
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_os__login__service__pb2.ListOsLoginProfilesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateProfile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.organizationmanager.v1.OsLoginService/CreateProfile',
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_os__login__service__pb2.CreateOsLoginProfileRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateProfile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.organizationmanager.v1.OsLoginService/UpdateProfile',
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_os__login__service__pb2.UpdateOsLoginProfileRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetDefaultProfile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.organizationmanager.v1.OsLoginService/SetDefaultProfile',
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_os__login__service__pb2.SetDefaultOsLoginProfileRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteProfile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.organizationmanager.v1.OsLoginService/DeleteProfile',
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_os__login__service__pb2.DeleteOsLoginProfileRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
