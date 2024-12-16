# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.serverless.workflows.v1 import workflow_service_pb2 as yandex_dot_cloud_dot_serverless_dot_workflows_dot_v1_dot_workflow__service__pb2

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
        + f' but the generated code in yandex/cloud/serverless/workflows/v1/workflow_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class WorkflowServiceStub(object):
    """Set of methods for managing Workflows.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/yandex.cloud.serverless.workflows.v1.WorkflowService/Create',
                request_serializer=yandex_dot_cloud_dot_serverless_dot_workflows_dot_v1_dot_workflow__service__pb2.CreateWorkflowRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Update = channel.unary_unary(
                '/yandex.cloud.serverless.workflows.v1.WorkflowService/Update',
                request_serializer=yandex_dot_cloud_dot_serverless_dot_workflows_dot_v1_dot_workflow__service__pb2.UpdateWorkflowRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Get = channel.unary_unary(
                '/yandex.cloud.serverless.workflows.v1.WorkflowService/Get',
                request_serializer=yandex_dot_cloud_dot_serverless_dot_workflows_dot_v1_dot_workflow__service__pb2.GetWorkflowRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_serverless_dot_workflows_dot_v1_dot_workflow__service__pb2.GetWorkflowResponse.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/yandex.cloud.serverless.workflows.v1.WorkflowService/Delete',
                request_serializer=yandex_dot_cloud_dot_serverless_dot_workflows_dot_v1_dot_workflow__service__pb2.DeleteWorkflowRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/yandex.cloud.serverless.workflows.v1.WorkflowService/List',
                request_serializer=yandex_dot_cloud_dot_serverless_dot_workflows_dot_v1_dot_workflow__service__pb2.ListWorkflowsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_serverless_dot_workflows_dot_v1_dot_workflow__service__pb2.ListWorkflowsResponse.FromString,
                _registered_method=True)
        self.ListOperations = channel.unary_unary(
                '/yandex.cloud.serverless.workflows.v1.WorkflowService/ListOperations',
                request_serializer=yandex_dot_cloud_dot_serverless_dot_workflows_dot_v1_dot_workflow__service__pb2.ListOperationsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_serverless_dot_workflows_dot_v1_dot_workflow__service__pb2.ListOperationsResponse.FromString,
                _registered_method=True)


class WorkflowServiceServicer(object):
    """Set of methods for managing Workflows.
    """

    def Create(self, request, context):
        """Creates Workflow in specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates specified Workflow.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Retrieves specified Workflow.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes specified Workflow.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves list of Workflows in specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOperations(self, request, context):
        """Lists operations for specified Workflow.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WorkflowServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_serverless_dot_workflows_dot_v1_dot_workflow__service__pb2.CreateWorkflowRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_serverless_dot_workflows_dot_v1_dot_workflow__service__pb2.UpdateWorkflowRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_serverless_dot_workflows_dot_v1_dot_workflow__service__pb2.GetWorkflowRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_serverless_dot_workflows_dot_v1_dot_workflow__service__pb2.GetWorkflowResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_serverless_dot_workflows_dot_v1_dot_workflow__service__pb2.DeleteWorkflowRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_serverless_dot_workflows_dot_v1_dot_workflow__service__pb2.ListWorkflowsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_serverless_dot_workflows_dot_v1_dot_workflow__service__pb2.ListWorkflowsResponse.SerializeToString,
            ),
            'ListOperations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOperations,
                    request_deserializer=yandex_dot_cloud_dot_serverless_dot_workflows_dot_v1_dot_workflow__service__pb2.ListOperationsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_serverless_dot_workflows_dot_v1_dot_workflow__service__pb2.ListOperationsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.serverless.workflows.v1.WorkflowService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.serverless.workflows.v1.WorkflowService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class WorkflowService(object):
    """Set of methods for managing Workflows.
    """

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
            '/yandex.cloud.serverless.workflows.v1.WorkflowService/Create',
            yandex_dot_cloud_dot_serverless_dot_workflows_dot_v1_dot_workflow__service__pb2.CreateWorkflowRequest.SerializeToString,
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
            '/yandex.cloud.serverless.workflows.v1.WorkflowService/Update',
            yandex_dot_cloud_dot_serverless_dot_workflows_dot_v1_dot_workflow__service__pb2.UpdateWorkflowRequest.SerializeToString,
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
            '/yandex.cloud.serverless.workflows.v1.WorkflowService/Get',
            yandex_dot_cloud_dot_serverless_dot_workflows_dot_v1_dot_workflow__service__pb2.GetWorkflowRequest.SerializeToString,
            yandex_dot_cloud_dot_serverless_dot_workflows_dot_v1_dot_workflow__service__pb2.GetWorkflowResponse.FromString,
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
            '/yandex.cloud.serverless.workflows.v1.WorkflowService/Delete',
            yandex_dot_cloud_dot_serverless_dot_workflows_dot_v1_dot_workflow__service__pb2.DeleteWorkflowRequest.SerializeToString,
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
            '/yandex.cloud.serverless.workflows.v1.WorkflowService/List',
            yandex_dot_cloud_dot_serverless_dot_workflows_dot_v1_dot_workflow__service__pb2.ListWorkflowsRequest.SerializeToString,
            yandex_dot_cloud_dot_serverless_dot_workflows_dot_v1_dot_workflow__service__pb2.ListWorkflowsResponse.FromString,
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
            '/yandex.cloud.serverless.workflows.v1.WorkflowService/ListOperations',
            yandex_dot_cloud_dot_serverless_dot_workflows_dot_v1_dot_workflow__service__pb2.ListOperationsRequest.SerializeToString,
            yandex_dot_cloud_dot_serverless_dot_workflows_dot_v1_dot_workflow__service__pb2.ListOperationsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
