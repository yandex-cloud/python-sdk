# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.monitoring.v3 import dashboard_pb2 as yandex_dot_cloud_dot_monitoring_dot_v3_dot_dashboard__pb2
from yandex.cloud.monitoring.v3 import dashboard_service_pb2 as yandex_dot_cloud_dot_monitoring_dot_v3_dot_dashboard__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2

GRPC_GENERATED_VERSION = '1.63.0'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in yandex/cloud/monitoring/v3/dashboard_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class DashboardServiceStub(object):
    """A set of methods for managing dashboards.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.monitoring.v3.DashboardService/Get',
                request_serializer=yandex_dot_cloud_dot_monitoring_dot_v3_dot_dashboard__service__pb2.GetDashboardRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_monitoring_dot_v3_dot_dashboard__pb2.Dashboard.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/yandex.cloud.monitoring.v3.DashboardService/List',
                request_serializer=yandex_dot_cloud_dot_monitoring_dot_v3_dot_dashboard__service__pb2.ListDashboardsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_monitoring_dot_v3_dot_dashboard__service__pb2.ListDashboardsResponse.FromString,
                _registered_method=True)
        self.Create = channel.unary_unary(
                '/yandex.cloud.monitoring.v3.DashboardService/Create',
                request_serializer=yandex_dot_cloud_dot_monitoring_dot_v3_dot_dashboard__service__pb2.CreateDashboardRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Update = channel.unary_unary(
                '/yandex.cloud.monitoring.v3.DashboardService/Update',
                request_serializer=yandex_dot_cloud_dot_monitoring_dot_v3_dot_dashboard__service__pb2.UpdateDashboardRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/yandex.cloud.monitoring.v3.DashboardService/Delete',
                request_serializer=yandex_dot_cloud_dot_monitoring_dot_v3_dot_dashboard__service__pb2.DeleteDashboardRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.ListOperations = channel.unary_unary(
                '/yandex.cloud.monitoring.v3.DashboardService/ListOperations',
                request_serializer=yandex_dot_cloud_dot_monitoring_dot_v3_dot_dashboard__service__pb2.ListDashboardOperationsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_monitoring_dot_v3_dot_dashboard__service__pb2.ListDashboardOperationsResponse.FromString,
                _registered_method=True)


class DashboardServiceServicer(object):
    """A set of methods for managing dashboards.
    """

    def Get(self, request, context):
        """Returns the specified dashboard.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of dashboards in the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates a new dashboard in the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates the specified dashboard.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified dashboard.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOperations(self, request, context):
        """Lists operations for the specified dashboard.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DashboardServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_monitoring_dot_v3_dot_dashboard__service__pb2.GetDashboardRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_monitoring_dot_v3_dot_dashboard__pb2.Dashboard.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_monitoring_dot_v3_dot_dashboard__service__pb2.ListDashboardsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_monitoring_dot_v3_dot_dashboard__service__pb2.ListDashboardsResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_monitoring_dot_v3_dot_dashboard__service__pb2.CreateDashboardRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_monitoring_dot_v3_dot_dashboard__service__pb2.UpdateDashboardRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_monitoring_dot_v3_dot_dashboard__service__pb2.DeleteDashboardRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListOperations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOperations,
                    request_deserializer=yandex_dot_cloud_dot_monitoring_dot_v3_dot_dashboard__service__pb2.ListDashboardOperationsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_monitoring_dot_v3_dot_dashboard__service__pb2.ListDashboardOperationsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.monitoring.v3.DashboardService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DashboardService(object):
    """A set of methods for managing dashboards.
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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.monitoring.v3.DashboardService/Get',
            yandex_dot_cloud_dot_monitoring_dot_v3_dot_dashboard__service__pb2.GetDashboardRequest.SerializeToString,
            yandex_dot_cloud_dot_monitoring_dot_v3_dot_dashboard__pb2.Dashboard.FromString,
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
            '/yandex.cloud.monitoring.v3.DashboardService/List',
            yandex_dot_cloud_dot_monitoring_dot_v3_dot_dashboard__service__pb2.ListDashboardsRequest.SerializeToString,
            yandex_dot_cloud_dot_monitoring_dot_v3_dot_dashboard__service__pb2.ListDashboardsResponse.FromString,
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
            '/yandex.cloud.monitoring.v3.DashboardService/Create',
            yandex_dot_cloud_dot_monitoring_dot_v3_dot_dashboard__service__pb2.CreateDashboardRequest.SerializeToString,
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
            '/yandex.cloud.monitoring.v3.DashboardService/Update',
            yandex_dot_cloud_dot_monitoring_dot_v3_dot_dashboard__service__pb2.UpdateDashboardRequest.SerializeToString,
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
            '/yandex.cloud.monitoring.v3.DashboardService/Delete',
            yandex_dot_cloud_dot_monitoring_dot_v3_dot_dashboard__service__pb2.DeleteDashboardRequest.SerializeToString,
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
    def ListOperations(request,
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
            '/yandex.cloud.monitoring.v3.DashboardService/ListOperations',
            yandex_dot_cloud_dot_monitoring_dot_v3_dot_dashboard__service__pb2.ListDashboardOperationsRequest.SerializeToString,
            yandex_dot_cloud_dot_monitoring_dot_v3_dot_dashboard__service__pb2.ListDashboardOperationsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
