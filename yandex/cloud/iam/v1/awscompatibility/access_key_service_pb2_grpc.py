# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.iam.v1.awscompatibility import access_key_pb2 as yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__pb2
from yandex.cloud.iam.v1.awscompatibility import access_key_service_pb2 as yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2

GRPC_GENERATED_VERSION = '1.63.0'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in yandex/cloud/iam/v1/awscompatibility/access_key_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class AccessKeyServiceStub(object):
    """A set of methods for managing access keys.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_unary(
                '/yandex.cloud.iam.v1.awscompatibility.AccessKeyService/List',
                request_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.ListAccessKeysRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.ListAccessKeysResponse.FromString,
                _registered_method=True)
        self.Get = channel.unary_unary(
                '/yandex.cloud.iam.v1.awscompatibility.AccessKeyService/Get',
                request_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.GetAccessKeyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__pb2.AccessKey.FromString,
                _registered_method=True)
        self.Create = channel.unary_unary(
                '/yandex.cloud.iam.v1.awscompatibility.AccessKeyService/Create',
                request_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.CreateAccessKeyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.CreateAccessKeyResponse.FromString,
                _registered_method=True)
        self.Update = channel.unary_unary(
                '/yandex.cloud.iam.v1.awscompatibility.AccessKeyService/Update',
                request_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.UpdateAccessKeyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/yandex.cloud.iam.v1.awscompatibility.AccessKeyService/Delete',
                request_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.DeleteAccessKeyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.ListOperations = channel.unary_unary(
                '/yandex.cloud.iam.v1.awscompatibility.AccessKeyService/ListOperations',
                request_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.ListAccessKeyOperationsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.ListAccessKeyOperationsResponse.FromString,
                _registered_method=True)


class AccessKeyServiceServicer(object):
    """A set of methods for managing access keys.
    """

    def List(self, request, context):
        """Retrieves the list of access keys for the specified service account.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Returns the specified access key.

        To get the list of available access keys, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates an access key for the specified service account.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates the specified access key.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified access key.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOperations(self, request, context):
        """Retrieves the list of operations for the specified access key.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AccessKeyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.ListAccessKeysRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.ListAccessKeysResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.GetAccessKeyRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__pb2.AccessKey.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.CreateAccessKeyRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.CreateAccessKeyResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.UpdateAccessKeyRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.DeleteAccessKeyRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListOperations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOperations,
                    request_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.ListAccessKeyOperationsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.ListAccessKeyOperationsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.iam.v1.awscompatibility.AccessKeyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AccessKeyService(object):
    """A set of methods for managing access keys.
    """

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
            '/yandex.cloud.iam.v1.awscompatibility.AccessKeyService/List',
            yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.ListAccessKeysRequest.SerializeToString,
            yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.ListAccessKeysResponse.FromString,
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
            '/yandex.cloud.iam.v1.awscompatibility.AccessKeyService/Get',
            yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.GetAccessKeyRequest.SerializeToString,
            yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__pb2.AccessKey.FromString,
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
            '/yandex.cloud.iam.v1.awscompatibility.AccessKeyService/Create',
            yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.CreateAccessKeyRequest.SerializeToString,
            yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.CreateAccessKeyResponse.FromString,
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
            '/yandex.cloud.iam.v1.awscompatibility.AccessKeyService/Update',
            yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.UpdateAccessKeyRequest.SerializeToString,
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
            '/yandex.cloud.iam.v1.awscompatibility.AccessKeyService/Delete',
            yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.DeleteAccessKeyRequest.SerializeToString,
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
            '/yandex.cloud.iam.v1.awscompatibility.AccessKeyService/ListOperations',
            yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.ListAccessKeyOperationsRequest.SerializeToString,
            yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.ListAccessKeyOperationsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
