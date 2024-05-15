# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from yandex.cloud.datasphere.v1 import folder_budget_service_pb2 as yandex_dot_cloud_dot_datasphere_dot_v1_dot_folder__budget__service__pb2


class FolderBudgetServiceStub(object):
    """A set of methods for managing Datasphere folder budgets.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.datasphere.v1.FolderBudgetService/Get',
                request_serializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_folder__budget__service__pb2.GetFolderBudgetRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_folder__budget__service__pb2.GetFolderBudgetResponse.FromString,
                )
        self.Set = channel.unary_unary(
                '/yandex.cloud.datasphere.v1.FolderBudgetService/Set',
                request_serializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_folder__budget__service__pb2.SetFolderBudgetRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class FolderBudgetServiceServicer(object):
    """A set of methods for managing Datasphere folder budgets.
    """

    def Get(self, request, context):
        """Returns the specified folder budget.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Set(self, request, context):
        """Sets the unit balance and the limits of the specified folder budget.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FolderBudgetServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_folder__budget__service__pb2.GetFolderBudgetRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_folder__budget__service__pb2.GetFolderBudgetResponse.SerializeToString,
            ),
            'Set': grpc.unary_unary_rpc_method_handler(
                    servicer.Set,
                    request_deserializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_folder__budget__service__pb2.SetFolderBudgetRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.datasphere.v1.FolderBudgetService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FolderBudgetService(object):
    """A set of methods for managing Datasphere folder budgets.
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.datasphere.v1.FolderBudgetService/Get',
            yandex_dot_cloud_dot_datasphere_dot_v1_dot_folder__budget__service__pb2.GetFolderBudgetRequest.SerializeToString,
            yandex_dot_cloud_dot_datasphere_dot_v1_dot_folder__budget__service__pb2.GetFolderBudgetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Set(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.datasphere.v1.FolderBudgetService/Set',
            yandex_dot_cloud_dot_datasphere_dot_v1_dot_folder__budget__service__pb2.SetFolderBudgetRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
