# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2
from yandex.cloud.logging.v1 import export_pb2 as yandex_dot_cloud_dot_logging_dot_v1_dot_export__pb2
from yandex.cloud.logging.v1 import export_service_pb2 as yandex_dot_cloud_dot_logging_dot_v1_dot_export__service__pb2
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
        + f' but the generated code in yandex/cloud/logging/v1/export_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ExportServiceStub(object):
    """A set of methods for managing log exports.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Run = channel.unary_unary(
                '/yandex.cloud.logging.v1.ExportService/Run',
                request_serializer=yandex_dot_cloud_dot_logging_dot_v1_dot_export__service__pb2.RunExportRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Get = channel.unary_unary(
                '/yandex.cloud.logging.v1.ExportService/Get',
                request_serializer=yandex_dot_cloud_dot_logging_dot_v1_dot_export__service__pb2.GetExportRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_logging_dot_v1_dot_export__pb2.Export.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/yandex.cloud.logging.v1.ExportService/List',
                request_serializer=yandex_dot_cloud_dot_logging_dot_v1_dot_export__service__pb2.ListExportsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_logging_dot_v1_dot_export__service__pb2.ListExportsResponse.FromString,
                _registered_method=True)
        self.Create = channel.unary_unary(
                '/yandex.cloud.logging.v1.ExportService/Create',
                request_serializer=yandex_dot_cloud_dot_logging_dot_v1_dot_export__service__pb2.CreateExportRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Update = channel.unary_unary(
                '/yandex.cloud.logging.v1.ExportService/Update',
                request_serializer=yandex_dot_cloud_dot_logging_dot_v1_dot_export__service__pb2.UpdateExportRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/yandex.cloud.logging.v1.ExportService/Delete',
                request_serializer=yandex_dot_cloud_dot_logging_dot_v1_dot_export__service__pb2.DeleteExportRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.ListOperations = channel.unary_unary(
                '/yandex.cloud.logging.v1.ExportService/ListOperations',
                request_serializer=yandex_dot_cloud_dot_logging_dot_v1_dot_export__service__pb2.ListExportOperationsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_logging_dot_v1_dot_export__service__pb2.ListExportOperationsResponse.FromString,
                _registered_method=True)
        self.ListAccessBindings = channel.unary_unary(
                '/yandex.cloud.logging.v1.ExportService/ListAccessBindings',
                request_serializer=yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsResponse.FromString,
                _registered_method=True)
        self.SetAccessBindings = channel.unary_unary(
                '/yandex.cloud.logging.v1.ExportService/SetAccessBindings',
                request_serializer=yandex_dot_cloud_dot_access_dot_access__pb2.SetAccessBindingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.UpdateAccessBindings = channel.unary_unary(
                '/yandex.cloud.logging.v1.ExportService/UpdateAccessBindings',
                request_serializer=yandex_dot_cloud_dot_access_dot_access__pb2.UpdateAccessBindingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)


class ExportServiceServicer(object):
    """A set of methods for managing log exports.
    """

    def Run(self, request, context):
        """Run new logs export from log group to sink
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Returns the specified export.

        To get the list of all available exports, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of exports in the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates a export in the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates the specified export.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified export.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOperations(self, request, context):
        """Lists operations for the specified export.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAccessBindings(self, request, context):
        """Lists existing access bindings for the specified export.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAccessBindings(self, request, context):
        """Sets access bindings for the specified export.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateAccessBindings(self, request, context):
        """Updates access bindings for the specified export.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ExportServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Run': grpc.unary_unary_rpc_method_handler(
                    servicer.Run,
                    request_deserializer=yandex_dot_cloud_dot_logging_dot_v1_dot_export__service__pb2.RunExportRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_logging_dot_v1_dot_export__service__pb2.GetExportRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_logging_dot_v1_dot_export__pb2.Export.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_logging_dot_v1_dot_export__service__pb2.ListExportsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_logging_dot_v1_dot_export__service__pb2.ListExportsResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_logging_dot_v1_dot_export__service__pb2.CreateExportRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_logging_dot_v1_dot_export__service__pb2.UpdateExportRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_logging_dot_v1_dot_export__service__pb2.DeleteExportRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListOperations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOperations,
                    request_deserializer=yandex_dot_cloud_dot_logging_dot_v1_dot_export__service__pb2.ListExportOperationsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_logging_dot_v1_dot_export__service__pb2.ListExportOperationsResponse.SerializeToString,
            ),
            'ListAccessBindings': grpc.unary_unary_rpc_method_handler(
                    servicer.ListAccessBindings,
                    request_deserializer=yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsResponse.SerializeToString,
            ),
            'SetAccessBindings': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAccessBindings,
                    request_deserializer=yandex_dot_cloud_dot_access_dot_access__pb2.SetAccessBindingsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'UpdateAccessBindings': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateAccessBindings,
                    request_deserializer=yandex_dot_cloud_dot_access_dot_access__pb2.UpdateAccessBindingsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.logging.v1.ExportService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.logging.v1.ExportService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ExportService(object):
    """A set of methods for managing log exports.
    """

    @staticmethod
    def Run(request,
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
            '/yandex.cloud.logging.v1.ExportService/Run',
            yandex_dot_cloud_dot_logging_dot_v1_dot_export__service__pb2.RunExportRequest.SerializeToString,
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
            '/yandex.cloud.logging.v1.ExportService/Get',
            yandex_dot_cloud_dot_logging_dot_v1_dot_export__service__pb2.GetExportRequest.SerializeToString,
            yandex_dot_cloud_dot_logging_dot_v1_dot_export__pb2.Export.FromString,
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
            '/yandex.cloud.logging.v1.ExportService/List',
            yandex_dot_cloud_dot_logging_dot_v1_dot_export__service__pb2.ListExportsRequest.SerializeToString,
            yandex_dot_cloud_dot_logging_dot_v1_dot_export__service__pb2.ListExportsResponse.FromString,
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
            '/yandex.cloud.logging.v1.ExportService/Create',
            yandex_dot_cloud_dot_logging_dot_v1_dot_export__service__pb2.CreateExportRequest.SerializeToString,
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
            '/yandex.cloud.logging.v1.ExportService/Update',
            yandex_dot_cloud_dot_logging_dot_v1_dot_export__service__pb2.UpdateExportRequest.SerializeToString,
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
            '/yandex.cloud.logging.v1.ExportService/Delete',
            yandex_dot_cloud_dot_logging_dot_v1_dot_export__service__pb2.DeleteExportRequest.SerializeToString,
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
            '/yandex.cloud.logging.v1.ExportService/ListOperations',
            yandex_dot_cloud_dot_logging_dot_v1_dot_export__service__pb2.ListExportOperationsRequest.SerializeToString,
            yandex_dot_cloud_dot_logging_dot_v1_dot_export__service__pb2.ListExportOperationsResponse.FromString,
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
    def ListAccessBindings(request,
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
            '/yandex.cloud.logging.v1.ExportService/ListAccessBindings',
            yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsRequest.SerializeToString,
            yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsResponse.FromString,
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
    def SetAccessBindings(request,
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
            '/yandex.cloud.logging.v1.ExportService/SetAccessBindings',
            yandex_dot_cloud_dot_access_dot_access__pb2.SetAccessBindingsRequest.SerializeToString,
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
    def UpdateAccessBindings(request,
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
            '/yandex.cloud.logging.v1.ExportService/UpdateAccessBindings',
            yandex_dot_cloud_dot_access_dot_access__pb2.UpdateAccessBindingsRequest.SerializeToString,
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
