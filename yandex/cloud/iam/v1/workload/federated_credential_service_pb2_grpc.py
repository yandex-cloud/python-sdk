# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.iam.v1.workload import federated_credential_pb2 as yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_federated__credential__pb2
from yandex.cloud.iam.v1.workload import federated_credential_service_pb2 as yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_federated__credential__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2

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
        + f' but the generated code in yandex/cloud/iam/v1/workload/federated_credential_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class FederatedCredentialServiceStub(object):
    """A set of methods for managing federated credentials.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.iam.v1.workload.FederatedCredentialService/Get',
                request_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_federated__credential__service__pb2.GetFederatedCredentialRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_federated__credential__pb2.FederatedCredential.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/yandex.cloud.iam.v1.workload.FederatedCredentialService/List',
                request_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_federated__credential__service__pb2.ListFederatedCredentialsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_federated__credential__service__pb2.ListFederatedCredentialsResponse.FromString,
                _registered_method=True)
        self.Create = channel.unary_unary(
                '/yandex.cloud.iam.v1.workload.FederatedCredentialService/Create',
                request_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_federated__credential__service__pb2.CreateFederatedCredentialRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/yandex.cloud.iam.v1.workload.FederatedCredentialService/Delete',
                request_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_federated__credential__service__pb2.DeleteFederatedCredentialRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)


class FederatedCredentialServiceServicer(object):
    """A set of methods for managing federated credentials.
    """

    def Get(self, request, context):
        """Returns the specified federated credential.

        To get the list of available federated credentials, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of federated credentials for the specified service account.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates a federated credential for the specified service account.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified federated credential.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FederatedCredentialServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_federated__credential__service__pb2.GetFederatedCredentialRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_federated__credential__pb2.FederatedCredential.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_federated__credential__service__pb2.ListFederatedCredentialsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_federated__credential__service__pb2.ListFederatedCredentialsResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_federated__credential__service__pb2.CreateFederatedCredentialRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_federated__credential__service__pb2.DeleteFederatedCredentialRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.iam.v1.workload.FederatedCredentialService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.iam.v1.workload.FederatedCredentialService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class FederatedCredentialService(object):
    """A set of methods for managing federated credentials.
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
            '/yandex.cloud.iam.v1.workload.FederatedCredentialService/Get',
            yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_federated__credential__service__pb2.GetFederatedCredentialRequest.SerializeToString,
            yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_federated__credential__pb2.FederatedCredential.FromString,
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
            '/yandex.cloud.iam.v1.workload.FederatedCredentialService/List',
            yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_federated__credential__service__pb2.ListFederatedCredentialsRequest.SerializeToString,
            yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_federated__credential__service__pb2.ListFederatedCredentialsResponse.FromString,
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
            '/yandex.cloud.iam.v1.workload.FederatedCredentialService/Create',
            yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_federated__credential__service__pb2.CreateFederatedCredentialRequest.SerializeToString,
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
            '/yandex.cloud.iam.v1.workload.FederatedCredentialService/Delete',
            yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_federated__credential__service__pb2.DeleteFederatedCredentialRequest.SerializeToString,
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
