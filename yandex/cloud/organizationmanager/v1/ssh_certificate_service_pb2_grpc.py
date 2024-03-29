# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.organizationmanager.v1 import ssh_certificate_service_pb2 as yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_ssh__certificate__service__pb2


class SshCertificateServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Generate = channel.unary_unary(
                '/yandex.cloud.organizationmanager.v1.SshCertificateService/Generate',
                request_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_ssh__certificate__service__pb2.GenerateSshCertificateRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_ssh__certificate__service__pb2.GenerateSshCertificateResponse.FromString,
                )


class SshCertificateServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Generate(self, request, context):
        """Members of an organization can generate certificates for themselves
        Signing certificates for other users requires a special permission
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SshCertificateServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Generate': grpc.unary_unary_rpc_method_handler(
                    servicer.Generate,
                    request_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_ssh__certificate__service__pb2.GenerateSshCertificateRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_ssh__certificate__service__pb2.GenerateSshCertificateResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.organizationmanager.v1.SshCertificateService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SshCertificateService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Generate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.organizationmanager.v1.SshCertificateService/Generate',
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_ssh__certificate__service__pb2.GenerateSshCertificateRequest.SerializeToString,
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_ssh__certificate__service__pb2.GenerateSshCertificateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
