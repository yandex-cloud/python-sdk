# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.kms.v1.asymmetricencryption import asymmetric_encryption_crypto_service_pb2 as yandex_dot_cloud_dot_kms_dot_v1_dot_asymmetricencryption_dot_asymmetric__encryption__crypto__service__pb2

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
        + f' but the generated code in yandex/cloud/kms/v1/asymmetricencryption/asymmetric_encryption_crypto_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class AsymmetricEncryptionCryptoServiceStub(object):
    """Data plane for KMS symmetric cryptography operations

    Set of methods that perform asymmetric decryption.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Decrypt = channel.unary_unary(
                '/yandex.cloud.kms.v1.asymmetricencryption.AsymmetricEncryptionCryptoService/Decrypt',
                request_serializer=yandex_dot_cloud_dot_kms_dot_v1_dot_asymmetricencryption_dot_asymmetric__encryption__crypto__service__pb2.AsymmetricDecryptRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_kms_dot_v1_dot_asymmetricencryption_dot_asymmetric__encryption__crypto__service__pb2.AsymmetricDecryptResponse.FromString,
                _registered_method=True)
        self.GetPublicKey = channel.unary_unary(
                '/yandex.cloud.kms.v1.asymmetricencryption.AsymmetricEncryptionCryptoService/GetPublicKey',
                request_serializer=yandex_dot_cloud_dot_kms_dot_v1_dot_asymmetricencryption_dot_asymmetric__encryption__crypto__service__pb2.AsymmetricGetPublicKeyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_kms_dot_v1_dot_asymmetricencryption_dot_asymmetric__encryption__crypto__service__pb2.AsymmetricGetPublicKeyResponse.FromString,
                _registered_method=True)


class AsymmetricEncryptionCryptoServiceServicer(object):
    """Data plane for KMS symmetric cryptography operations

    Set of methods that perform asymmetric decryption.
    """

    def Decrypt(self, request, context):
        """Decrypts the given ciphertext with the specified key.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPublicKey(self, request, context):
        """Gets value of public key.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AsymmetricEncryptionCryptoServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Decrypt': grpc.unary_unary_rpc_method_handler(
                    servicer.Decrypt,
                    request_deserializer=yandex_dot_cloud_dot_kms_dot_v1_dot_asymmetricencryption_dot_asymmetric__encryption__crypto__service__pb2.AsymmetricDecryptRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_kms_dot_v1_dot_asymmetricencryption_dot_asymmetric__encryption__crypto__service__pb2.AsymmetricDecryptResponse.SerializeToString,
            ),
            'GetPublicKey': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPublicKey,
                    request_deserializer=yandex_dot_cloud_dot_kms_dot_v1_dot_asymmetricencryption_dot_asymmetric__encryption__crypto__service__pb2.AsymmetricGetPublicKeyRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_kms_dot_v1_dot_asymmetricencryption_dot_asymmetric__encryption__crypto__service__pb2.AsymmetricGetPublicKeyResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.kms.v1.asymmetricencryption.AsymmetricEncryptionCryptoService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AsymmetricEncryptionCryptoService(object):
    """Data plane for KMS symmetric cryptography operations

    Set of methods that perform asymmetric decryption.
    """

    @staticmethod
    def Decrypt(request,
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
            '/yandex.cloud.kms.v1.asymmetricencryption.AsymmetricEncryptionCryptoService/Decrypt',
            yandex_dot_cloud_dot_kms_dot_v1_dot_asymmetricencryption_dot_asymmetric__encryption__crypto__service__pb2.AsymmetricDecryptRequest.SerializeToString,
            yandex_dot_cloud_dot_kms_dot_v1_dot_asymmetricencryption_dot_asymmetric__encryption__crypto__service__pb2.AsymmetricDecryptResponse.FromString,
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
    def GetPublicKey(request,
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
            '/yandex.cloud.kms.v1.asymmetricencryption.AsymmetricEncryptionCryptoService/GetPublicKey',
            yandex_dot_cloud_dot_kms_dot_v1_dot_asymmetricencryption_dot_asymmetric__encryption__crypto__service__pb2.AsymmetricGetPublicKeyRequest.SerializeToString,
            yandex_dot_cloud_dot_kms_dot_v1_dot_asymmetricencryption_dot_asymmetric__encryption__crypto__service__pb2.AsymmetricGetPublicKeyResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
