# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.loadbalancer.v1 import network_load_balancer_pb2 as yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__pb2
from yandex.cloud.loadbalancer.v1 import network_load_balancer_service_pb2 as yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2

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
        + f' but the generated code in yandex/cloud/loadbalancer/v1/network_load_balancer_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class NetworkLoadBalancerServiceStub(object):
    """A set of methods for managing NetworkLoadBalancer resources.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.loadbalancer.v1.NetworkLoadBalancerService/Get',
                request_serializer=yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.GetNetworkLoadBalancerRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__pb2.NetworkLoadBalancer.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/yandex.cloud.loadbalancer.v1.NetworkLoadBalancerService/List',
                request_serializer=yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.ListNetworkLoadBalancersRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.ListNetworkLoadBalancersResponse.FromString,
                _registered_method=True)
        self.Create = channel.unary_unary(
                '/yandex.cloud.loadbalancer.v1.NetworkLoadBalancerService/Create',
                request_serializer=yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.CreateNetworkLoadBalancerRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Update = channel.unary_unary(
                '/yandex.cloud.loadbalancer.v1.NetworkLoadBalancerService/Update',
                request_serializer=yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.UpdateNetworkLoadBalancerRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/yandex.cloud.loadbalancer.v1.NetworkLoadBalancerService/Delete',
                request_serializer=yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.DeleteNetworkLoadBalancerRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Start = channel.unary_unary(
                '/yandex.cloud.loadbalancer.v1.NetworkLoadBalancerService/Start',
                request_serializer=yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.StartNetworkLoadBalancerRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Stop = channel.unary_unary(
                '/yandex.cloud.loadbalancer.v1.NetworkLoadBalancerService/Stop',
                request_serializer=yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.StopNetworkLoadBalancerRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.AttachTargetGroup = channel.unary_unary(
                '/yandex.cloud.loadbalancer.v1.NetworkLoadBalancerService/AttachTargetGroup',
                request_serializer=yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.AttachNetworkLoadBalancerTargetGroupRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.DetachTargetGroup = channel.unary_unary(
                '/yandex.cloud.loadbalancer.v1.NetworkLoadBalancerService/DetachTargetGroup',
                request_serializer=yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.DetachNetworkLoadBalancerTargetGroupRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.GetTargetStates = channel.unary_unary(
                '/yandex.cloud.loadbalancer.v1.NetworkLoadBalancerService/GetTargetStates',
                request_serializer=yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.GetTargetStatesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.GetTargetStatesResponse.FromString,
                _registered_method=True)
        self.AddListener = channel.unary_unary(
                '/yandex.cloud.loadbalancer.v1.NetworkLoadBalancerService/AddListener',
                request_serializer=yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.AddNetworkLoadBalancerListenerRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.RemoveListener = channel.unary_unary(
                '/yandex.cloud.loadbalancer.v1.NetworkLoadBalancerService/RemoveListener',
                request_serializer=yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.RemoveNetworkLoadBalancerListenerRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.ListOperations = channel.unary_unary(
                '/yandex.cloud.loadbalancer.v1.NetworkLoadBalancerService/ListOperations',
                request_serializer=yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.ListNetworkLoadBalancerOperationsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.ListNetworkLoadBalancerOperationsResponse.FromString,
                _registered_method=True)
        self.DisableZones = channel.unary_unary(
                '/yandex.cloud.loadbalancer.v1.NetworkLoadBalancerService/DisableZones',
                request_serializer=yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.DisableZonesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.EnableZones = channel.unary_unary(
                '/yandex.cloud.loadbalancer.v1.NetworkLoadBalancerService/EnableZones',
                request_serializer=yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.EnableZonesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)


class NetworkLoadBalancerServiceServicer(object):
    """A set of methods for managing NetworkLoadBalancer resources.
    """

    def Get(self, request, context):
        """Returns the specified NetworkLoadBalancer resource.

        Get the list of available NetworkLoadBalancer resources by making a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of NetworkLoadBalancer resources in the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates a network load balancer in the specified folder using the data specified in the request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates the specified network load balancer.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified network load balancer.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Start(self, request, context):
        """Starts load balancing and health checking with the specified network load balancer with specified settings.
        Changes network load balancer status to `` ACTIVE ``.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stop(self, request, context):
        """Stops load balancing and health checking with the specified network load balancer.
        Changes load balancer status to `` STOPPED ``.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AttachTargetGroup(self, request, context):
        """Attaches a target group to the specified network load balancer.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DetachTargetGroup(self, request, context):
        """Detaches the target group from the specified network load balancer.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTargetStates(self, request, context):
        """Gets states of target resources in the attached target group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddListener(self, request, context):
        """Adds a listener to the specified network load balancer.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveListener(self, request, context):
        """Removes the listener from the specified network load balancer.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOperations(self, request, context):
        """Lists operations for the specified network load balancer.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DisableZones(self, request, context):
        """Disable zones for the specified network load balancer.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EnableZones(self, request, context):
        """Enable zones for the specified network load balancer.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NetworkLoadBalancerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.GetNetworkLoadBalancerRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__pb2.NetworkLoadBalancer.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.ListNetworkLoadBalancersRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.ListNetworkLoadBalancersResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.CreateNetworkLoadBalancerRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.UpdateNetworkLoadBalancerRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.DeleteNetworkLoadBalancerRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Start': grpc.unary_unary_rpc_method_handler(
                    servicer.Start,
                    request_deserializer=yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.StartNetworkLoadBalancerRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Stop': grpc.unary_unary_rpc_method_handler(
                    servicer.Stop,
                    request_deserializer=yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.StopNetworkLoadBalancerRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'AttachTargetGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.AttachTargetGroup,
                    request_deserializer=yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.AttachNetworkLoadBalancerTargetGroupRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'DetachTargetGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.DetachTargetGroup,
                    request_deserializer=yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.DetachNetworkLoadBalancerTargetGroupRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'GetTargetStates': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTargetStates,
                    request_deserializer=yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.GetTargetStatesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.GetTargetStatesResponse.SerializeToString,
            ),
            'AddListener': grpc.unary_unary_rpc_method_handler(
                    servicer.AddListener,
                    request_deserializer=yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.AddNetworkLoadBalancerListenerRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'RemoveListener': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveListener,
                    request_deserializer=yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.RemoveNetworkLoadBalancerListenerRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListOperations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOperations,
                    request_deserializer=yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.ListNetworkLoadBalancerOperationsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.ListNetworkLoadBalancerOperationsResponse.SerializeToString,
            ),
            'DisableZones': grpc.unary_unary_rpc_method_handler(
                    servicer.DisableZones,
                    request_deserializer=yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.DisableZonesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'EnableZones': grpc.unary_unary_rpc_method_handler(
                    servicer.EnableZones,
                    request_deserializer=yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.EnableZonesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.loadbalancer.v1.NetworkLoadBalancerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.loadbalancer.v1.NetworkLoadBalancerService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class NetworkLoadBalancerService(object):
    """A set of methods for managing NetworkLoadBalancer resources.
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
            '/yandex.cloud.loadbalancer.v1.NetworkLoadBalancerService/Get',
            yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.GetNetworkLoadBalancerRequest.SerializeToString,
            yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__pb2.NetworkLoadBalancer.FromString,
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
            '/yandex.cloud.loadbalancer.v1.NetworkLoadBalancerService/List',
            yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.ListNetworkLoadBalancersRequest.SerializeToString,
            yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.ListNetworkLoadBalancersResponse.FromString,
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
            '/yandex.cloud.loadbalancer.v1.NetworkLoadBalancerService/Create',
            yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.CreateNetworkLoadBalancerRequest.SerializeToString,
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
            '/yandex.cloud.loadbalancer.v1.NetworkLoadBalancerService/Update',
            yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.UpdateNetworkLoadBalancerRequest.SerializeToString,
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
            '/yandex.cloud.loadbalancer.v1.NetworkLoadBalancerService/Delete',
            yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.DeleteNetworkLoadBalancerRequest.SerializeToString,
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
    def Start(request,
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
            '/yandex.cloud.loadbalancer.v1.NetworkLoadBalancerService/Start',
            yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.StartNetworkLoadBalancerRequest.SerializeToString,
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
    def Stop(request,
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
            '/yandex.cloud.loadbalancer.v1.NetworkLoadBalancerService/Stop',
            yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.StopNetworkLoadBalancerRequest.SerializeToString,
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
    def AttachTargetGroup(request,
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
            '/yandex.cloud.loadbalancer.v1.NetworkLoadBalancerService/AttachTargetGroup',
            yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.AttachNetworkLoadBalancerTargetGroupRequest.SerializeToString,
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
    def DetachTargetGroup(request,
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
            '/yandex.cloud.loadbalancer.v1.NetworkLoadBalancerService/DetachTargetGroup',
            yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.DetachNetworkLoadBalancerTargetGroupRequest.SerializeToString,
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
    def GetTargetStates(request,
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
            '/yandex.cloud.loadbalancer.v1.NetworkLoadBalancerService/GetTargetStates',
            yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.GetTargetStatesRequest.SerializeToString,
            yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.GetTargetStatesResponse.FromString,
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
    def AddListener(request,
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
            '/yandex.cloud.loadbalancer.v1.NetworkLoadBalancerService/AddListener',
            yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.AddNetworkLoadBalancerListenerRequest.SerializeToString,
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
    def RemoveListener(request,
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
            '/yandex.cloud.loadbalancer.v1.NetworkLoadBalancerService/RemoveListener',
            yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.RemoveNetworkLoadBalancerListenerRequest.SerializeToString,
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
            '/yandex.cloud.loadbalancer.v1.NetworkLoadBalancerService/ListOperations',
            yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.ListNetworkLoadBalancerOperationsRequest.SerializeToString,
            yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.ListNetworkLoadBalancerOperationsResponse.FromString,
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
    def DisableZones(request,
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
            '/yandex.cloud.loadbalancer.v1.NetworkLoadBalancerService/DisableZones',
            yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.DisableZonesRequest.SerializeToString,
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
    def EnableZones(request,
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
            '/yandex.cloud.loadbalancer.v1.NetworkLoadBalancerService/EnableZones',
            yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__service__pb2.EnableZonesRequest.SerializeToString,
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
