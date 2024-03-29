# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.organizationmanager.v1 import user_service_pb2 as yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_user__service__pb2


class UserServiceStub(object):
    """A set of methods for managing Organization users.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListMembers = channel.unary_unary(
                '/yandex.cloud.organizationmanager.v1.UserService/ListMembers',
                request_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_user__service__pb2.ListMembersRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_user__service__pb2.ListMembersResponse.FromString,
                )
        self.DeleteMembership = channel.unary_unary(
                '/yandex.cloud.organizationmanager.v1.UserService/DeleteMembership',
                request_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_user__service__pb2.DeleteMembershipRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )


class UserServiceServicer(object):
    """A set of methods for managing Organization users.
    """

    def ListMembers(self, request, context):
        """List organization active members.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteMembership(self, request, context):
        """Delete user membership.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListMembers': grpc.unary_unary_rpc_method_handler(
                    servicer.ListMembers,
                    request_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_user__service__pb2.ListMembersRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_user__service__pb2.ListMembersResponse.SerializeToString,
            ),
            'DeleteMembership': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteMembership,
                    request_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_user__service__pb2.DeleteMembershipRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.organizationmanager.v1.UserService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserService(object):
    """A set of methods for managing Organization users.
    """

    @staticmethod
    def ListMembers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.organizationmanager.v1.UserService/ListMembers',
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_user__service__pb2.ListMembersRequest.SerializeToString,
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_user__service__pb2.ListMembersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteMembership(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.organizationmanager.v1.UserService/DeleteMembership',
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_user__service__pb2.DeleteMembershipRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
