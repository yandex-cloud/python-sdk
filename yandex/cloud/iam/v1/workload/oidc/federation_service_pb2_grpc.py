# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2
from yandex.cloud.iam.v1.workload.oidc import federation_pb2 as yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_oidc_dot_federation__pb2
from yandex.cloud.iam.v1.workload.oidc import federation_service_pb2 as yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_oidc_dot_federation__service__pb2
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
        + f' but the generated code in yandex/cloud/iam/v1/workload/oidc/federation_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class FederationServiceStub(object):
    """A set of methods for managing OIDC workload identity federations.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.iam.v1.workload.oidc.FederationService/Get',
                request_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_oidc_dot_federation__service__pb2.GetFederationRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_oidc_dot_federation__pb2.Federation.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/yandex.cloud.iam.v1.workload.oidc.FederationService/List',
                request_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_oidc_dot_federation__service__pb2.ListFederationsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_oidc_dot_federation__service__pb2.ListFederationsResponse.FromString,
                _registered_method=True)
        self.Create = channel.unary_unary(
                '/yandex.cloud.iam.v1.workload.oidc.FederationService/Create',
                request_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_oidc_dot_federation__service__pb2.CreateFederationRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Update = channel.unary_unary(
                '/yandex.cloud.iam.v1.workload.oidc.FederationService/Update',
                request_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_oidc_dot_federation__service__pb2.UpdateFederationRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/yandex.cloud.iam.v1.workload.oidc.FederationService/Delete',
                request_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_oidc_dot_federation__service__pb2.DeleteFederationRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.ListAccessBindings = channel.unary_unary(
                '/yandex.cloud.iam.v1.workload.oidc.FederationService/ListAccessBindings',
                request_serializer=yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsResponse.FromString,
                _registered_method=True)
        self.SetAccessBindings = channel.unary_unary(
                '/yandex.cloud.iam.v1.workload.oidc.FederationService/SetAccessBindings',
                request_serializer=yandex_dot_cloud_dot_access_dot_access__pb2.SetAccessBindingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.UpdateAccessBindings = channel.unary_unary(
                '/yandex.cloud.iam.v1.workload.oidc.FederationService/UpdateAccessBindings',
                request_serializer=yandex_dot_cloud_dot_access_dot_access__pb2.UpdateAccessBindingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)


class FederationServiceServicer(object):
    """A set of methods for managing OIDC workload identity federations.
    """

    def Get(self, request, context):
        """Returns the specified OIDC workload identity federation.

        To get the list of available OIDC workload identity federation, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of OIDC workload identity federations in the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates an OIDC workload identity federation in the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates the specified OIDC workload identity federation.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified OIDC workload identity federation.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAccessBindings(self, request, context):
        """Lists access bindings for the specified OIDC workload identity federation.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAccessBindings(self, request, context):
        """Sets access bindings for the specified OIDC workload identity federation.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateAccessBindings(self, request, context):
        """Updates access bindings for the specified OIDC workload identity federation.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FederationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_oidc_dot_federation__service__pb2.GetFederationRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_oidc_dot_federation__pb2.Federation.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_oidc_dot_federation__service__pb2.ListFederationsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_oidc_dot_federation__service__pb2.ListFederationsResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_oidc_dot_federation__service__pb2.CreateFederationRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_oidc_dot_federation__service__pb2.UpdateFederationRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_oidc_dot_federation__service__pb2.DeleteFederationRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
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
            'yandex.cloud.iam.v1.workload.oidc.FederationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.iam.v1.workload.oidc.FederationService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class FederationService(object):
    """A set of methods for managing OIDC workload identity federations.
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
            '/yandex.cloud.iam.v1.workload.oidc.FederationService/Get',
            yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_oidc_dot_federation__service__pb2.GetFederationRequest.SerializeToString,
            yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_oidc_dot_federation__pb2.Federation.FromString,
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
            '/yandex.cloud.iam.v1.workload.oidc.FederationService/List',
            yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_oidc_dot_federation__service__pb2.ListFederationsRequest.SerializeToString,
            yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_oidc_dot_federation__service__pb2.ListFederationsResponse.FromString,
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
            '/yandex.cloud.iam.v1.workload.oidc.FederationService/Create',
            yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_oidc_dot_federation__service__pb2.CreateFederationRequest.SerializeToString,
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
            '/yandex.cloud.iam.v1.workload.oidc.FederationService/Update',
            yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_oidc_dot_federation__service__pb2.UpdateFederationRequest.SerializeToString,
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
            '/yandex.cloud.iam.v1.workload.oidc.FederationService/Delete',
            yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_oidc_dot_federation__service__pb2.DeleteFederationRequest.SerializeToString,
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
            '/yandex.cloud.iam.v1.workload.oidc.FederationService/ListAccessBindings',
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
            '/yandex.cloud.iam.v1.workload.oidc.FederationService/SetAccessBindings',
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
            '/yandex.cloud.iam.v1.workload.oidc.FederationService/UpdateAccessBindings',
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
