# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.mdb.kafka.v1 import topic_pb2 as yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_topic__pb2
from yandex.cloud.mdb.kafka.v1 import topic_service_pb2 as yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_topic__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class TopicServiceStub(object):
    """A set of methods for managing Kafka topics.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.mdb.kafka.v1.TopicService/Get',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_topic__service__pb2.GetTopicRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_topic__pb2.Topic.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.mdb.kafka.v1.TopicService/List',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_topic__service__pb2.ListTopicsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_topic__service__pb2.ListTopicsResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/yandex.cloud.mdb.kafka.v1.TopicService/Create',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_topic__service__pb2.CreateTopicRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Update = channel.unary_unary(
                '/yandex.cloud.mdb.kafka.v1.TopicService/Update',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_topic__service__pb2.UpdateTopicRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Delete = channel.unary_unary(
                '/yandex.cloud.mdb.kafka.v1.TopicService/Delete',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_topic__service__pb2.DeleteTopicRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )


class TopicServiceServicer(object):
    """A set of methods for managing Kafka topics.
    """

    def Get(self, request, context):
        """Returns the specified Kafka topic.

        To get the list of available Kafka topics, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of Kafka topics in the specified cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates a new Kafka topic in the specified cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates the specified Kafka topic.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified Kafka topic.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TopicServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_topic__service__pb2.GetTopicRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_topic__pb2.Topic.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_topic__service__pb2.ListTopicsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_topic__service__pb2.ListTopicsResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_topic__service__pb2.CreateTopicRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_topic__service__pb2.UpdateTopicRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_topic__service__pb2.DeleteTopicRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.mdb.kafka.v1.TopicService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TopicService(object):
    """A set of methods for managing Kafka topics.
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.kafka.v1.TopicService/Get',
            yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_topic__service__pb2.GetTopicRequest.SerializeToString,
            yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_topic__pb2.Topic.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.kafka.v1.TopicService/List',
            yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_topic__service__pb2.ListTopicsRequest.SerializeToString,
            yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_topic__service__pb2.ListTopicsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.kafka.v1.TopicService/Create',
            yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_topic__service__pb2.CreateTopicRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.kafka.v1.TopicService/Update',
            yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_topic__service__pb2.UpdateTopicRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.kafka.v1.TopicService/Delete',
            yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_topic__service__pb2.DeleteTopicRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
