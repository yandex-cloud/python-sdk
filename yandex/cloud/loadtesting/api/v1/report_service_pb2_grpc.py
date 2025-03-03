# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.loadtesting.api.v1 import report_service_pb2 as yandex_dot_cloud_dot_loadtesting_dot_api_dot_v1_dot_report__service__pb2

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
        + f' but the generated code in yandex/cloud/loadtesting/api/v1/report_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ReportServiceStub(object):
    """A set of methods for managing test reports.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTable = channel.unary_unary(
                '/yandex.cloud.loadtesting.api.v1.ReportService/GetTable',
                request_serializer=yandex_dot_cloud_dot_loadtesting_dot_api_dot_v1_dot_report__service__pb2.GetTableReportRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_loadtesting_dot_api_dot_v1_dot_report__service__pb2.GetTableReportResponse.FromString,
                _registered_method=True)
        self.CalculateKpiValues = channel.unary_unary(
                '/yandex.cloud.loadtesting.api.v1.ReportService/CalculateKpiValues',
                request_serializer=yandex_dot_cloud_dot_loadtesting_dot_api_dot_v1_dot_report__service__pb2.CalculateReportKpiValuesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_loadtesting_dot_api_dot_v1_dot_report__service__pb2.CalculateReportKpiValuesResponse.FromString,
                _registered_method=True)


class ReportServiceServicer(object):
    """A set of methods for managing test reports.
    """

    def GetTable(self, request, context):
        """Returns a report table for the specified test.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CalculateKpiValues(self, request, context):
        """Returns a list of KPI values for tests matching the specified filter.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ReportServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTable': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTable,
                    request_deserializer=yandex_dot_cloud_dot_loadtesting_dot_api_dot_v1_dot_report__service__pb2.GetTableReportRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_loadtesting_dot_api_dot_v1_dot_report__service__pb2.GetTableReportResponse.SerializeToString,
            ),
            'CalculateKpiValues': grpc.unary_unary_rpc_method_handler(
                    servicer.CalculateKpiValues,
                    request_deserializer=yandex_dot_cloud_dot_loadtesting_dot_api_dot_v1_dot_report__service__pb2.CalculateReportKpiValuesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_loadtesting_dot_api_dot_v1_dot_report__service__pb2.CalculateReportKpiValuesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.loadtesting.api.v1.ReportService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.loadtesting.api.v1.ReportService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ReportService(object):
    """A set of methods for managing test reports.
    """

    @staticmethod
    def GetTable(request,
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
            '/yandex.cloud.loadtesting.api.v1.ReportService/GetTable',
            yandex_dot_cloud_dot_loadtesting_dot_api_dot_v1_dot_report__service__pb2.GetTableReportRequest.SerializeToString,
            yandex_dot_cloud_dot_loadtesting_dot_api_dot_v1_dot_report__service__pb2.GetTableReportResponse.FromString,
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
    def CalculateKpiValues(request,
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
            '/yandex.cloud.loadtesting.api.v1.ReportService/CalculateKpiValues',
            yandex_dot_cloud_dot_loadtesting_dot_api_dot_v1_dot_report__service__pb2.CalculateReportKpiValuesRequest.SerializeToString,
            yandex_dot_cloud_dot_loadtesting_dot_api_dot_v1_dot_report__service__pb2.CalculateReportKpiValuesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
