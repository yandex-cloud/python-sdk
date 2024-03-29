# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.datasphere.v2 import dataset_service_pb2 as yandex_dot_cloud_dot_datasphere_dot_v2_dot_dataset__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class DatasetServiceStub(object):
    """A set of methods for managing Datasets.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Activate = channel.unary_unary(
                '/yandex.cloud.datasphere.v2.DatasetService/Activate',
                request_serializer=yandex_dot_cloud_dot_datasphere_dot_v2_dot_dataset__service__pb2.ActivateDatasetRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Deactivate = channel.unary_unary(
                '/yandex.cloud.datasphere.v2.DatasetService/Deactivate',
                request_serializer=yandex_dot_cloud_dot_datasphere_dot_v2_dot_dataset__service__pb2.DeactivateDatasetRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )


class DatasetServiceServicer(object):
    """A set of methods for managing Datasets.
    """

    def Activate(self, request, context):
        """Activates shared dataset for project
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Deactivate(self, request, context):
        """Deactivates shared dataset for project
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DatasetServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Activate': grpc.unary_unary_rpc_method_handler(
                    servicer.Activate,
                    request_deserializer=yandex_dot_cloud_dot_datasphere_dot_v2_dot_dataset__service__pb2.ActivateDatasetRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Deactivate': grpc.unary_unary_rpc_method_handler(
                    servicer.Deactivate,
                    request_deserializer=yandex_dot_cloud_dot_datasphere_dot_v2_dot_dataset__service__pb2.DeactivateDatasetRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.datasphere.v2.DatasetService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DatasetService(object):
    """A set of methods for managing Datasets.
    """

    @staticmethod
    def Activate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.datasphere.v2.DatasetService/Activate',
            yandex_dot_cloud_dot_datasphere_dot_v2_dot_dataset__service__pb2.ActivateDatasetRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Deactivate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.datasphere.v2.DatasetService/Deactivate',
            yandex_dot_cloud_dot_datasphere_dot_v2_dot_dataset__service__pb2.DeactivateDatasetRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
