# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.containerregistry.v1 import image_pb2 as yandex_dot_cloud_dot_containerregistry_dot_v1_dot_image__pb2
from yandex.cloud.containerregistry.v1 import image_service_pb2 as yandex_dot_cloud_dot_containerregistry_dot_v1_dot_image__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class ImageServiceStub(object):
    """A set of methods for managing Image resources.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_unary(
                '/yandex.cloud.containerregistry.v1.ImageService/List',
                request_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_image__service__pb2.ListImagesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_image__service__pb2.ListImagesResponse.FromString,
                )
        self.Get = channel.unary_unary(
                '/yandex.cloud.containerregistry.v1.ImageService/Get',
                request_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_image__service__pb2.GetImageRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_image__pb2.Image.FromString,
                )
        self.Delete = channel.unary_unary(
                '/yandex.cloud.containerregistry.v1.ImageService/Delete',
                request_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_image__service__pb2.DeleteImageRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )


class ImageServiceServicer(object):
    """A set of methods for managing Image resources.
    """

    def List(self, request, context):
        """Retrieves the list of Image resources in the specified registry or repository.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Returns the specified Image resource.

        To get the list of available Image resources, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified Docker image.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ImageServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_image__service__pb2.ListImagesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_image__service__pb2.ListImagesResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_image__service__pb2.GetImageRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_image__pb2.Image.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_image__service__pb2.DeleteImageRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.containerregistry.v1.ImageService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ImageService(object):
    """A set of methods for managing Image resources.
    """

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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.containerregistry.v1.ImageService/List',
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_image__service__pb2.ListImagesRequest.SerializeToString,
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_image__service__pb2.ListImagesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.containerregistry.v1.ImageService/Get',
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_image__service__pb2.GetImageRequest.SerializeToString,
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_image__pb2.Image.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.containerregistry.v1.ImageService/Delete',
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_image__service__pb2.DeleteImageRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
