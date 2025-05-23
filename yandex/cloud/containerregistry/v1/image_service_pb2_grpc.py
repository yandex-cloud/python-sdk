# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.containerregistry.v1 import image_pb2 as yandex_dot_cloud_dot_containerregistry_dot_v1_dot_image__pb2
from yandex.cloud.containerregistry.v1 import image_service_pb2 as yandex_dot_cloud_dot_containerregistry_dot_v1_dot_image__service__pb2
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
        + f' but the generated code in yandex/cloud/containerregistry/v1/image_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


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
                _registered_method=True)
        self.Get = channel.unary_unary(
                '/yandex.cloud.containerregistry.v1.ImageService/Get',
                request_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_image__service__pb2.GetImageRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_image__pb2.Image.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/yandex.cloud.containerregistry.v1.ImageService/Delete',
                request_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_image__service__pb2.DeleteImageRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)


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
    server.add_registered_method_handlers('yandex.cloud.containerregistry.v1.ImageService', rpc_method_handlers)


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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.containerregistry.v1.ImageService/List',
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_image__service__pb2.ListImagesRequest.SerializeToString,
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_image__service__pb2.ListImagesResponse.FromString,
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
            '/yandex.cloud.containerregistry.v1.ImageService/Get',
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_image__service__pb2.GetImageRequest.SerializeToString,
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_image__pb2.Image.FromString,
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
            '/yandex.cloud.containerregistry.v1.ImageService/Delete',
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_image__service__pb2.DeleteImageRequest.SerializeToString,
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
