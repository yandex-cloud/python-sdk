# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.organizationmanager.v1.saml import federation_pb2 as yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__pb2
from yandex.cloud.organizationmanager.v1.saml import federation_service_pb2 as yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2

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
        + f' but the generated code in yandex/cloud/organizationmanager/v1/saml/federation_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class FederationServiceStub(object):
    """A set of methods for managing federations.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.organizationmanager.v1.saml.FederationService/Get',
                request_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.GetFederationRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__pb2.Federation.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/yandex.cloud.organizationmanager.v1.saml.FederationService/List',
                request_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.ListFederationsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.ListFederationsResponse.FromString,
                _registered_method=True)
        self.Create = channel.unary_unary(
                '/yandex.cloud.organizationmanager.v1.saml.FederationService/Create',
                request_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.CreateFederationRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Update = channel.unary_unary(
                '/yandex.cloud.organizationmanager.v1.saml.FederationService/Update',
                request_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.UpdateFederationRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/yandex.cloud.organizationmanager.v1.saml.FederationService/Delete',
                request_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.DeleteFederationRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.AddUserAccounts = channel.unary_unary(
                '/yandex.cloud.organizationmanager.v1.saml.FederationService/AddUserAccounts',
                request_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.AddFederatedUserAccountsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.DeleteUserAccounts = channel.unary_unary(
                '/yandex.cloud.organizationmanager.v1.saml.FederationService/DeleteUserAccounts',
                request_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.DeleteFederatedUserAccountsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.ListUserAccounts = channel.unary_unary(
                '/yandex.cloud.organizationmanager.v1.saml.FederationService/ListUserAccounts',
                request_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.ListFederatedUserAccountsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.ListFederatedUserAccountsResponse.FromString,
                _registered_method=True)
        self.ListOperations = channel.unary_unary(
                '/yandex.cloud.organizationmanager.v1.saml.FederationService/ListOperations',
                request_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.ListFederationOperationsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.ListFederationOperationsResponse.FromString,
                _registered_method=True)
        self.GetDomain = channel.unary_unary(
                '/yandex.cloud.organizationmanager.v1.saml.FederationService/GetDomain',
                request_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.GetFederationDomainRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__pb2.Domain.FromString,
                _registered_method=True)
        self.ListDomains = channel.unary_unary(
                '/yandex.cloud.organizationmanager.v1.saml.FederationService/ListDomains',
                request_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.ListFederationDomainsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.ListFederationDomainsResponse.FromString,
                _registered_method=True)
        self.AddDomain = channel.unary_unary(
                '/yandex.cloud.organizationmanager.v1.saml.FederationService/AddDomain',
                request_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.AddFederationDomainRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.ValidateDomain = channel.unary_unary(
                '/yandex.cloud.organizationmanager.v1.saml.FederationService/ValidateDomain',
                request_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.ValidateFederationDomainRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.DeleteDomain = channel.unary_unary(
                '/yandex.cloud.organizationmanager.v1.saml.FederationService/DeleteDomain',
                request_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.DeleteFederationDomainRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)


class FederationServiceServicer(object):
    """A set of methods for managing federations.
    """

    def Get(self, request, context):
        """Returns the specified federation.

        To get the list of available federations, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of federations in the specified organization.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates a federation in the specified organization.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates the specified federation.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified federation.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddUserAccounts(self, request, context):
        """Adds users to the specified federation.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteUserAccounts(self, request, context):
        """Deletes users from the specified federation.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListUserAccounts(self, request, context):
        """Lists users for the specified federation.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOperations(self, request, context):
        """Lists operations for the specified federation.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDomain(self, request, context):
        """Returns the specified domain in the federation.

        To get the list of available domains, make a [ListDomains] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListDomains(self, request, context):
        """Retrieves the list of domains in the specified federation.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddDomain(self, request, context):
        """Adds a domain to the specified federation.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ValidateDomain(self, request, context):
        """Validates a domain in the specified federation.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteDomain(self, request, context):
        """Deletes the specified domain from the federation.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FederationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.GetFederationRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__pb2.Federation.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.ListFederationsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.ListFederationsResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.CreateFederationRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.UpdateFederationRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.DeleteFederationRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'AddUserAccounts': grpc.unary_unary_rpc_method_handler(
                    servicer.AddUserAccounts,
                    request_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.AddFederatedUserAccountsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'DeleteUserAccounts': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteUserAccounts,
                    request_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.DeleteFederatedUserAccountsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListUserAccounts': grpc.unary_unary_rpc_method_handler(
                    servicer.ListUserAccounts,
                    request_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.ListFederatedUserAccountsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.ListFederatedUserAccountsResponse.SerializeToString,
            ),
            'ListOperations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOperations,
                    request_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.ListFederationOperationsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.ListFederationOperationsResponse.SerializeToString,
            ),
            'GetDomain': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDomain,
                    request_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.GetFederationDomainRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__pb2.Domain.SerializeToString,
            ),
            'ListDomains': grpc.unary_unary_rpc_method_handler(
                    servicer.ListDomains,
                    request_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.ListFederationDomainsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.ListFederationDomainsResponse.SerializeToString,
            ),
            'AddDomain': grpc.unary_unary_rpc_method_handler(
                    servicer.AddDomain,
                    request_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.AddFederationDomainRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ValidateDomain': grpc.unary_unary_rpc_method_handler(
                    servicer.ValidateDomain,
                    request_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.ValidateFederationDomainRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'DeleteDomain': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteDomain,
                    request_deserializer=yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.DeleteFederationDomainRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.organizationmanager.v1.saml.FederationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.organizationmanager.v1.saml.FederationService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class FederationService(object):
    """A set of methods for managing federations.
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
            '/yandex.cloud.organizationmanager.v1.saml.FederationService/Get',
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.GetFederationRequest.SerializeToString,
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__pb2.Federation.FromString,
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
            '/yandex.cloud.organizationmanager.v1.saml.FederationService/List',
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.ListFederationsRequest.SerializeToString,
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.ListFederationsResponse.FromString,
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
            '/yandex.cloud.organizationmanager.v1.saml.FederationService/Create',
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.CreateFederationRequest.SerializeToString,
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
            '/yandex.cloud.organizationmanager.v1.saml.FederationService/Update',
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.UpdateFederationRequest.SerializeToString,
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
            '/yandex.cloud.organizationmanager.v1.saml.FederationService/Delete',
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.DeleteFederationRequest.SerializeToString,
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
    def AddUserAccounts(request,
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
            '/yandex.cloud.organizationmanager.v1.saml.FederationService/AddUserAccounts',
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.AddFederatedUserAccountsRequest.SerializeToString,
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
    def DeleteUserAccounts(request,
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
            '/yandex.cloud.organizationmanager.v1.saml.FederationService/DeleteUserAccounts',
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.DeleteFederatedUserAccountsRequest.SerializeToString,
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
    def ListUserAccounts(request,
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
            '/yandex.cloud.organizationmanager.v1.saml.FederationService/ListUserAccounts',
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.ListFederatedUserAccountsRequest.SerializeToString,
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.ListFederatedUserAccountsResponse.FromString,
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
            '/yandex.cloud.organizationmanager.v1.saml.FederationService/ListOperations',
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.ListFederationOperationsRequest.SerializeToString,
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.ListFederationOperationsResponse.FromString,
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
    def GetDomain(request,
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
            '/yandex.cloud.organizationmanager.v1.saml.FederationService/GetDomain',
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.GetFederationDomainRequest.SerializeToString,
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__pb2.Domain.FromString,
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
    def ListDomains(request,
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
            '/yandex.cloud.organizationmanager.v1.saml.FederationService/ListDomains',
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.ListFederationDomainsRequest.SerializeToString,
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.ListFederationDomainsResponse.FromString,
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
    def AddDomain(request,
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
            '/yandex.cloud.organizationmanager.v1.saml.FederationService/AddDomain',
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.AddFederationDomainRequest.SerializeToString,
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
    def ValidateDomain(request,
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
            '/yandex.cloud.organizationmanager.v1.saml.FederationService/ValidateDomain',
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.ValidateFederationDomainRequest.SerializeToString,
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
    def DeleteDomain(request,
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
            '/yandex.cloud.organizationmanager.v1.saml.FederationService/DeleteDomain',
            yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_saml_dot_federation__service__pb2.DeleteFederationDomainRequest.SerializeToString,
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
