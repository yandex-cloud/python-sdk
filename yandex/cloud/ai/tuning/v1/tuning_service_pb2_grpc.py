# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.ai.tuning.v1 import tuning_service_pb2 as yandex_dot_cloud_dot_ai_dot_tuning_dot_v1_dot_tuning__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class TuningServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Tune = channel.unary_unary(
                '/yandex.cloud.ai.tuning.v1.TuningService/Tune',
                request_serializer=yandex_dot_cloud_dot_ai_dot_tuning_dot_v1_dot_tuning__service__pb2.TuningRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.ai.tuning.v1.TuningService/List',
                request_serializer=yandex_dot_cloud_dot_ai_dot_tuning_dot_v1_dot_tuning__service__pb2.ListTuningsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_ai_dot_tuning_dot_v1_dot_tuning__service__pb2.ListTuningsResponse.FromString,
                )
        self.Describe = channel.unary_unary(
                '/yandex.cloud.ai.tuning.v1.TuningService/Describe',
                request_serializer=yandex_dot_cloud_dot_ai_dot_tuning_dot_v1_dot_tuning__service__pb2.DescribeTuningRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_ai_dot_tuning_dot_v1_dot_tuning__service__pb2.DescribeTuningResponse.FromString,
                )
        self.Cancel = channel.unary_unary(
                '/yandex.cloud.ai.tuning.v1.TuningService/Cancel',
                request_serializer=yandex_dot_cloud_dot_ai_dot_tuning_dot_v1_dot_tuning__service__pb2.CancelTuningRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_ai_dot_tuning_dot_v1_dot_tuning__service__pb2.CancelTuningResponse.FromString,
                )
        self.GetMetricsUrl = channel.unary_unary(
                '/yandex.cloud.ai.tuning.v1.TuningService/GetMetricsUrl',
                request_serializer=yandex_dot_cloud_dot_ai_dot_tuning_dot_v1_dot_tuning__service__pb2.GetMetricsUrlRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_ai_dot_tuning_dot_v1_dot_tuning__service__pb2.GetMetricsUrlResponse.FromString,
                )
        self.GetOptions = channel.unary_unary(
                '/yandex.cloud.ai.tuning.v1.TuningService/GetOptions',
                request_serializer=yandex_dot_cloud_dot_ai_dot_tuning_dot_v1_dot_tuning__service__pb2.GetOptionsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_ai_dot_tuning_dot_v1_dot_tuning__service__pb2.GetOptionsResponse.FromString,
                )


class TuningServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Tune(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Describe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Cancel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMetricsUrl(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOptions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TuningServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Tune': grpc.unary_unary_rpc_method_handler(
                    servicer.Tune,
                    request_deserializer=yandex_dot_cloud_dot_ai_dot_tuning_dot_v1_dot_tuning__service__pb2.TuningRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_ai_dot_tuning_dot_v1_dot_tuning__service__pb2.ListTuningsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_ai_dot_tuning_dot_v1_dot_tuning__service__pb2.ListTuningsResponse.SerializeToString,
            ),
            'Describe': grpc.unary_unary_rpc_method_handler(
                    servicer.Describe,
                    request_deserializer=yandex_dot_cloud_dot_ai_dot_tuning_dot_v1_dot_tuning__service__pb2.DescribeTuningRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_ai_dot_tuning_dot_v1_dot_tuning__service__pb2.DescribeTuningResponse.SerializeToString,
            ),
            'Cancel': grpc.unary_unary_rpc_method_handler(
                    servicer.Cancel,
                    request_deserializer=yandex_dot_cloud_dot_ai_dot_tuning_dot_v1_dot_tuning__service__pb2.CancelTuningRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_ai_dot_tuning_dot_v1_dot_tuning__service__pb2.CancelTuningResponse.SerializeToString,
            ),
            'GetMetricsUrl': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMetricsUrl,
                    request_deserializer=yandex_dot_cloud_dot_ai_dot_tuning_dot_v1_dot_tuning__service__pb2.GetMetricsUrlRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_ai_dot_tuning_dot_v1_dot_tuning__service__pb2.GetMetricsUrlResponse.SerializeToString,
            ),
            'GetOptions': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOptions,
                    request_deserializer=yandex_dot_cloud_dot_ai_dot_tuning_dot_v1_dot_tuning__service__pb2.GetOptionsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_ai_dot_tuning_dot_v1_dot_tuning__service__pb2.GetOptionsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.ai.tuning.v1.TuningService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TuningService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Tune(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.ai.tuning.v1.TuningService/Tune',
            yandex_dot_cloud_dot_ai_dot_tuning_dot_v1_dot_tuning__service__pb2.TuningRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.ai.tuning.v1.TuningService/List',
            yandex_dot_cloud_dot_ai_dot_tuning_dot_v1_dot_tuning__service__pb2.ListTuningsRequest.SerializeToString,
            yandex_dot_cloud_dot_ai_dot_tuning_dot_v1_dot_tuning__service__pb2.ListTuningsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Describe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.ai.tuning.v1.TuningService/Describe',
            yandex_dot_cloud_dot_ai_dot_tuning_dot_v1_dot_tuning__service__pb2.DescribeTuningRequest.SerializeToString,
            yandex_dot_cloud_dot_ai_dot_tuning_dot_v1_dot_tuning__service__pb2.DescribeTuningResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Cancel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.ai.tuning.v1.TuningService/Cancel',
            yandex_dot_cloud_dot_ai_dot_tuning_dot_v1_dot_tuning__service__pb2.CancelTuningRequest.SerializeToString,
            yandex_dot_cloud_dot_ai_dot_tuning_dot_v1_dot_tuning__service__pb2.CancelTuningResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMetricsUrl(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.ai.tuning.v1.TuningService/GetMetricsUrl',
            yandex_dot_cloud_dot_ai_dot_tuning_dot_v1_dot_tuning__service__pb2.GetMetricsUrlRequest.SerializeToString,
            yandex_dot_cloud_dot_ai_dot_tuning_dot_v1_dot_tuning__service__pb2.GetMetricsUrlResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOptions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.ai.tuning.v1.TuningService/GetOptions',
            yandex_dot_cloud_dot_ai_dot_tuning_dot_v1_dot_tuning__service__pb2.GetOptionsRequest.SerializeToString,
            yandex_dot_cloud_dot_ai_dot_tuning_dot_v1_dot_tuning__service__pb2.GetOptionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
