# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.loadtesting.agent.v1 import agent_registration_service_pb2 as yandex_dot_cloud_dot_loadtesting_dot_agent_dot_v1_dot_agent__registration__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class AgentRegistrationServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Register = channel.unary_unary(
                '/yandex.cloud.loadtesting.agent.v1.AgentRegistrationService/Register',
                request_serializer=yandex_dot_cloud_dot_loadtesting_dot_agent_dot_v1_dot_agent__registration__service__pb2.RegisterRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_loadtesting_dot_agent_dot_v1_dot_agent__registration__service__pb2.RegisterResponse.FromString,
                )
        self.ExternalAgentRegister = channel.unary_unary(
                '/yandex.cloud.loadtesting.agent.v1.AgentRegistrationService/ExternalAgentRegister',
                request_serializer=yandex_dot_cloud_dot_loadtesting_dot_agent_dot_v1_dot_agent__registration__service__pb2.ExternalAgentRegisterRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )


class AgentRegistrationServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Register(self, request, context):
        """Registers specified agent.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExternalAgentRegister(self, request, context):
        """Registers external agent.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AgentRegistrationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Register': grpc.unary_unary_rpc_method_handler(
                    servicer.Register,
                    request_deserializer=yandex_dot_cloud_dot_loadtesting_dot_agent_dot_v1_dot_agent__registration__service__pb2.RegisterRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_loadtesting_dot_agent_dot_v1_dot_agent__registration__service__pb2.RegisterResponse.SerializeToString,
            ),
            'ExternalAgentRegister': grpc.unary_unary_rpc_method_handler(
                    servicer.ExternalAgentRegister,
                    request_deserializer=yandex_dot_cloud_dot_loadtesting_dot_agent_dot_v1_dot_agent__registration__service__pb2.ExternalAgentRegisterRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.loadtesting.agent.v1.AgentRegistrationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AgentRegistrationService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Register(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.loadtesting.agent.v1.AgentRegistrationService/Register',
            yandex_dot_cloud_dot_loadtesting_dot_agent_dot_v1_dot_agent__registration__service__pb2.RegisterRequest.SerializeToString,
            yandex_dot_cloud_dot_loadtesting_dot_agent_dot_v1_dot_agent__registration__service__pb2.RegisterResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExternalAgentRegister(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.loadtesting.agent.v1.AgentRegistrationService/ExternalAgentRegister',
            yandex_dot_cloud_dot_loadtesting_dot_agent_dot_v1_dot_agent__registration__service__pb2.ExternalAgentRegisterRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
