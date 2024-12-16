# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.containerregistry.v1 import scanner_pb2 as yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scanner__pb2
from yandex.cloud.containerregistry.v1 import scanner_service_pb2 as yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scanner__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2

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
        + f' but the generated code in yandex/cloud/containerregistry/v1/scanner_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ScannerServiceStub(object):
    """A set of methods for scanning Docker images.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Scan = channel.unary_unary(
                '/yandex.cloud.containerregistry.v1.ScannerService/Scan',
                request_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scanner__service__pb2.ScanRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Get = channel.unary_unary(
                '/yandex.cloud.containerregistry.v1.ScannerService/Get',
                request_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scanner__service__pb2.GetScanResultRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scanner__pb2.ScanResult.FromString,
                _registered_method=True)
        self.GetLast = channel.unary_unary(
                '/yandex.cloud.containerregistry.v1.ScannerService/GetLast',
                request_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scanner__service__pb2.GetLastScanResultRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scanner__pb2.ScanResult.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/yandex.cloud.containerregistry.v1.ScannerService/List',
                request_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scanner__service__pb2.ListScanResultsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scanner__service__pb2.ListScanResultsResponse.FromString,
                _registered_method=True)
        self.ListVulnerabilities = channel.unary_unary(
                '/yandex.cloud.containerregistry.v1.ScannerService/ListVulnerabilities',
                request_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scanner__service__pb2.ListVulnerabilitiesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scanner__service__pb2.ListVulnerabilitiesResponse.FromString,
                _registered_method=True)


class ScannerServiceServicer(object):
    """A set of methods for scanning Docker images.
    """

    def Scan(self, request, context):
        """Executes scanning of specified image.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Returns the specified ScanResult resource.

        To get the list of ScanResults for specified Image, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLast(self, request, context):
        """Returns the last finished ScanResult for the specified Image.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of ScanResults for specified Image.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListVulnerabilities(self, request, context):
        """Retrieves the list of vulnerabilities found in particular scan.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ScannerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Scan': grpc.unary_unary_rpc_method_handler(
                    servicer.Scan,
                    request_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scanner__service__pb2.ScanRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scanner__service__pb2.GetScanResultRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scanner__pb2.ScanResult.SerializeToString,
            ),
            'GetLast': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLast,
                    request_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scanner__service__pb2.GetLastScanResultRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scanner__pb2.ScanResult.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scanner__service__pb2.ListScanResultsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scanner__service__pb2.ListScanResultsResponse.SerializeToString,
            ),
            'ListVulnerabilities': grpc.unary_unary_rpc_method_handler(
                    servicer.ListVulnerabilities,
                    request_deserializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scanner__service__pb2.ListVulnerabilitiesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scanner__service__pb2.ListVulnerabilitiesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.containerregistry.v1.ScannerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.containerregistry.v1.ScannerService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ScannerService(object):
    """A set of methods for scanning Docker images.
    """

    @staticmethod
    def Scan(request,
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
            '/yandex.cloud.containerregistry.v1.ScannerService/Scan',
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scanner__service__pb2.ScanRequest.SerializeToString,
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
            '/yandex.cloud.containerregistry.v1.ScannerService/Get',
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scanner__service__pb2.GetScanResultRequest.SerializeToString,
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scanner__pb2.ScanResult.FromString,
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
    def GetLast(request,
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
            '/yandex.cloud.containerregistry.v1.ScannerService/GetLast',
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scanner__service__pb2.GetLastScanResultRequest.SerializeToString,
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scanner__pb2.ScanResult.FromString,
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
            '/yandex.cloud.containerregistry.v1.ScannerService/List',
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scanner__service__pb2.ListScanResultsRequest.SerializeToString,
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scanner__service__pb2.ListScanResultsResponse.FromString,
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
    def ListVulnerabilities(request,
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
            '/yandex.cloud.containerregistry.v1.ScannerService/ListVulnerabilities',
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scanner__service__pb2.ListVulnerabilitiesRequest.SerializeToString,
            yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scanner__service__pb2.ListVulnerabilitiesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
