# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from yandex.cloud.iam.v1 import key_pb2 as yandex_dot_cloud_dot_iam_dot_v1_dot_key__pb2
from yandex.cloud.iam.v1 import key_service_pb2 as yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class KeyServiceStub(object):
  """A set of methods for managing Key resources.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Get = channel.unary_unary(
        '/yandex.cloud.iam.v1.KeyService/Get',
        request_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.GetKeyRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_key__pb2.Key.FromString,
        )
    self.List = channel.unary_unary(
        '/yandex.cloud.iam.v1.KeyService/List',
        request_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.ListKeysRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.ListKeysResponse.FromString,
        )
    self.Create = channel.unary_unary(
        '/yandex.cloud.iam.v1.KeyService/Create',
        request_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.CreateKeyRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.CreateKeyResponse.FromString,
        )
    self.Delete = channel.unary_unary(
        '/yandex.cloud.iam.v1.KeyService/Delete',
        request_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.DeleteKeyRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.ListOperations = channel.unary_unary(
        '/yandex.cloud.iam.v1.KeyService/ListOperations',
        request_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.ListKeyOperationsRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.ListKeyOperationsResponse.FromString,
        )


class KeyServiceServicer(object):
  """A set of methods for managing Key resources.
  """

  def Get(self, request, context):
    """Returns the specified Key resource.

    To get the list of available Key resources, make a [List] request.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def List(self, request, context):
    """Retrieves the list of Key resources for the specified service account.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Create(self, request, context):
    """Creates a key pair for the specified service account.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    """Deletes the specified key pair.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListOperations(self, request, context):
    """Lists operations for the specified key.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_KeyServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.GetKeyRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_key__pb2.Key.SerializeToString,
      ),
      'List': grpc.unary_unary_rpc_method_handler(
          servicer.List,
          request_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.ListKeysRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.ListKeysResponse.SerializeToString,
      ),
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.CreateKeyRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.CreateKeyResponse.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.DeleteKeyRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'ListOperations': grpc.unary_unary_rpc_method_handler(
          servicer.ListOperations,
          request_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.ListKeyOperationsRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.ListKeyOperationsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'yandex.cloud.iam.v1.KeyService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
