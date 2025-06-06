# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.vpc.v1 import address_pb2 as yandex_dot_cloud_dot_vpc_dot_v1_dot_address__pb2
from yandex.cloud.vpc.v1 import address_service_pb2 as yandex_dot_cloud_dot_vpc_dot_v1_dot_address__service__pb2

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
        + f' but the generated code in yandex/cloud/vpc/v1/address_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class AddressServiceStub(object):
    """A set of methods for managing Address resources.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.vpc.v1.AddressService/Get',
                request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_address__service__pb2.GetAddressRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_address__pb2.Address.FromString,
                _registered_method=True)
        self.GetByValue = channel.unary_unary(
                '/yandex.cloud.vpc.v1.AddressService/GetByValue',
                request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_address__service__pb2.GetAddressByValueRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_address__pb2.Address.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/yandex.cloud.vpc.v1.AddressService/List',
                request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_address__service__pb2.ListAddressesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_address__service__pb2.ListAddressesResponse.FromString,
                _registered_method=True)
        self.Create = channel.unary_unary(
                '/yandex.cloud.vpc.v1.AddressService/Create',
                request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_address__service__pb2.CreateAddressRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Update = channel.unary_unary(
                '/yandex.cloud.vpc.v1.AddressService/Update',
                request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_address__service__pb2.UpdateAddressRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/yandex.cloud.vpc.v1.AddressService/Delete',
                request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_address__service__pb2.DeleteAddressRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.ListOperations = channel.unary_unary(
                '/yandex.cloud.vpc.v1.AddressService/ListOperations',
                request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_address__service__pb2.ListAddressOperationsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_address__service__pb2.ListAddressOperationsResponse.FromString,
                _registered_method=True)
        self.Move = channel.unary_unary(
                '/yandex.cloud.vpc.v1.AddressService/Move',
                request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_address__service__pb2.MoveAddressRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)


class AddressServiceServicer(object):
    """A set of methods for managing Address resources.
    """

    def Get(self, request, context):
        """Returns the specified Address resource.

        To get the list of all available Address resources, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetByValue(self, request, context):
        """Returns the specified Address resource by a given value.

        To get the list of all available Address resources, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of Address resources in the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates an address in the specified folder and network.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates the specified address.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified address.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOperations(self, request, context):
        """List operations for the specified address.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Move(self, request, context):
        """Move an address to another folder
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AddressServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_address__service__pb2.GetAddressRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_address__pb2.Address.SerializeToString,
            ),
            'GetByValue': grpc.unary_unary_rpc_method_handler(
                    servicer.GetByValue,
                    request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_address__service__pb2.GetAddressByValueRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_address__pb2.Address.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_address__service__pb2.ListAddressesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_address__service__pb2.ListAddressesResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_address__service__pb2.CreateAddressRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_address__service__pb2.UpdateAddressRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_address__service__pb2.DeleteAddressRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListOperations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOperations,
                    request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_address__service__pb2.ListAddressOperationsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_address__service__pb2.ListAddressOperationsResponse.SerializeToString,
            ),
            'Move': grpc.unary_unary_rpc_method_handler(
                    servicer.Move,
                    request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_address__service__pb2.MoveAddressRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.vpc.v1.AddressService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.vpc.v1.AddressService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class AddressService(object):
    """A set of methods for managing Address resources.
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
            '/yandex.cloud.vpc.v1.AddressService/Get',
            yandex_dot_cloud_dot_vpc_dot_v1_dot_address__service__pb2.GetAddressRequest.SerializeToString,
            yandex_dot_cloud_dot_vpc_dot_v1_dot_address__pb2.Address.FromString,
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
    def GetByValue(request,
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
            '/yandex.cloud.vpc.v1.AddressService/GetByValue',
            yandex_dot_cloud_dot_vpc_dot_v1_dot_address__service__pb2.GetAddressByValueRequest.SerializeToString,
            yandex_dot_cloud_dot_vpc_dot_v1_dot_address__pb2.Address.FromString,
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
            '/yandex.cloud.vpc.v1.AddressService/List',
            yandex_dot_cloud_dot_vpc_dot_v1_dot_address__service__pb2.ListAddressesRequest.SerializeToString,
            yandex_dot_cloud_dot_vpc_dot_v1_dot_address__service__pb2.ListAddressesResponse.FromString,
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
            '/yandex.cloud.vpc.v1.AddressService/Create',
            yandex_dot_cloud_dot_vpc_dot_v1_dot_address__service__pb2.CreateAddressRequest.SerializeToString,
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
            '/yandex.cloud.vpc.v1.AddressService/Update',
            yandex_dot_cloud_dot_vpc_dot_v1_dot_address__service__pb2.UpdateAddressRequest.SerializeToString,
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
            '/yandex.cloud.vpc.v1.AddressService/Delete',
            yandex_dot_cloud_dot_vpc_dot_v1_dot_address__service__pb2.DeleteAddressRequest.SerializeToString,
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
            '/yandex.cloud.vpc.v1.AddressService/ListOperations',
            yandex_dot_cloud_dot_vpc_dot_v1_dot_address__service__pb2.ListAddressOperationsRequest.SerializeToString,
            yandex_dot_cloud_dot_vpc_dot_v1_dot_address__service__pb2.ListAddressOperationsResponse.FromString,
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
    def Move(request,
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
            '/yandex.cloud.vpc.v1.AddressService/Move',
            yandex_dot_cloud_dot_vpc_dot_v1_dot_address__service__pb2.MoveAddressRequest.SerializeToString,
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
