# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.cic.v1 import partner_pb2 as yandex_dot_cloud_dot_cic_dot_v1_dot_partner__pb2
from yandex.cloud.cic.v1 import partner_service_pb2 as yandex_dot_cloud_dot_cic_dot_v1_dot_partner__service__pb2


class PartnerServiceStub(object):
    """A set of methods for managing Partner resources.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.cic.v1.PartnerService/Get',
                request_serializer=yandex_dot_cloud_dot_cic_dot_v1_dot_partner__service__pb2.GetPartnerRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_cic_dot_v1_dot_partner__pb2.Partner.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.cic.v1.PartnerService/List',
                request_serializer=yandex_dot_cloud_dot_cic_dot_v1_dot_partner__service__pb2.ListPartnersRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_cic_dot_v1_dot_partner__service__pb2.ListPartnersResponse.FromString,
                )


class PartnerServiceServicer(object):
    """A set of methods for managing Partner resources.
    """

    def Get(self, request, context):
        """Returns the specified Partner resource.

        To get the list of available Partner resources, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of Partner resources in the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PartnerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_cic_dot_v1_dot_partner__service__pb2.GetPartnerRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_cic_dot_v1_dot_partner__pb2.Partner.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_cic_dot_v1_dot_partner__service__pb2.ListPartnersRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_cic_dot_v1_dot_partner__service__pb2.ListPartnersResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.cic.v1.PartnerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PartnerService(object):
    """A set of methods for managing Partner resources.
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.cic.v1.PartnerService/Get',
            yandex_dot_cloud_dot_cic_dot_v1_dot_partner__service__pb2.GetPartnerRequest.SerializeToString,
            yandex_dot_cloud_dot_cic_dot_v1_dot_partner__pb2.Partner.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.cic.v1.PartnerService/List',
            yandex_dot_cloud_dot_cic_dot_v1_dot_partner__service__pb2.ListPartnersRequest.SerializeToString,
            yandex_dot_cloud_dot_cic_dot_v1_dot_partner__service__pb2.ListPartnersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)