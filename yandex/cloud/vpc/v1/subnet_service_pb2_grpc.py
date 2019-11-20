# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.vpc.v1 import subnet_pb2 as yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__pb2
from yandex.cloud.vpc.v1 import subnet_service_pb2 as yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2


class SubnetServiceStub(object):
  """A set of methods for managing Subnet resources.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Get = channel.unary_unary(
        '/yandex.cloud.vpc.v1.SubnetService/Get',
        request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.GetSubnetRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__pb2.Subnet.FromString,
        )
    self.List = channel.unary_unary(
        '/yandex.cloud.vpc.v1.SubnetService/List',
        request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.ListSubnetsRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.ListSubnetsResponse.FromString,
        )
    self.Create = channel.unary_unary(
        '/yandex.cloud.vpc.v1.SubnetService/Create',
        request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.CreateSubnetRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.Update = channel.unary_unary(
        '/yandex.cloud.vpc.v1.SubnetService/Update',
        request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.UpdateSubnetRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.Delete = channel.unary_unary(
        '/yandex.cloud.vpc.v1.SubnetService/Delete',
        request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.DeleteSubnetRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.ListOperations = channel.unary_unary(
        '/yandex.cloud.vpc.v1.SubnetService/ListOperations',
        request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.ListSubnetOperationsRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.ListSubnetOperationsResponse.FromString,
        )
    self.Move = channel.unary_unary(
        '/yandex.cloud.vpc.v1.SubnetService/Move',
        request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.MoveSubnetRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )


class SubnetServiceServicer(object):
  """A set of methods for managing Subnet resources.
  """

  def Get(self, request, context):
    """Returns the specified Subnet resource.

    To get the list of available Subnet resources, make a [List] request.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def List(self, request, context):
    """Retrieves the list of Subnet resources in the specified folder.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Create(self, request, context):
    """Creates a subnet in the specified folder and network.
    Method starts an asynchronous operation that can be cancelled while it is in progress.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Update(self, request, context):
    """Updates the specified subnet.
    Method starts an asynchronous operation that can be cancelled while it is in progress.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    """Deletes the specified subnet.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListOperations(self, request, context):
    """List operations for the specified subnet.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Move(self, request, context):
    """Move subnet to another folder.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SubnetServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.GetSubnetRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__pb2.Subnet.SerializeToString,
      ),
      'List': grpc.unary_unary_rpc_method_handler(
          servicer.List,
          request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.ListSubnetsRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.ListSubnetsResponse.SerializeToString,
      ),
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.CreateSubnetRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'Update': grpc.unary_unary_rpc_method_handler(
          servicer.Update,
          request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.UpdateSubnetRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.DeleteSubnetRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'ListOperations': grpc.unary_unary_rpc_method_handler(
          servicer.ListOperations,
          request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.ListSubnetOperationsRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.ListSubnetOperationsResponse.SerializeToString,
      ),
      'Move': grpc.unary_unary_rpc_method_handler(
          servicer.Move,
          request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__service__pb2.MoveSubnetRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'yandex.cloud.vpc.v1.SubnetService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
