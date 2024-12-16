# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.kms.v1 import symmetric_crypto_service_pb2 as yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2

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
        + f' but the generated code in yandex/cloud/kms/v1/symmetric_crypto_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class SymmetricCryptoServiceStub(object):
    """--- Data plane for KMS symmetric cryptography operations

    Set of methods that perform symmetric encryption and decryption.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Encrypt = channel.unary_unary(
                '/yandex.cloud.kms.v1.SymmetricCryptoService/Encrypt',
                request_serializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.SymmetricEncryptRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.SymmetricEncryptResponse.FromString,
                _registered_method=True)
        self.Decrypt = channel.unary_unary(
                '/yandex.cloud.kms.v1.SymmetricCryptoService/Decrypt',
                request_serializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.SymmetricDecryptRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.SymmetricDecryptResponse.FromString,
                _registered_method=True)
        self.ReEncrypt = channel.unary_unary(
                '/yandex.cloud.kms.v1.SymmetricCryptoService/ReEncrypt',
                request_serializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.SymmetricReEncryptRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.SymmetricReEncryptResponse.FromString,
                _registered_method=True)
        self.GenerateDataKey = channel.unary_unary(
                '/yandex.cloud.kms.v1.SymmetricCryptoService/GenerateDataKey',
                request_serializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.GenerateDataKeyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.GenerateDataKeyResponse.FromString,
                _registered_method=True)


class SymmetricCryptoServiceServicer(object):
    """--- Data plane for KMS symmetric cryptography operations

    Set of methods that perform symmetric encryption and decryption.
    """

    def Encrypt(self, request, context):
        """Encrypts given plaintext with the specified key.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Decrypt(self, request, context):
        """Decrypts the given ciphertext with the specified key.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReEncrypt(self, request, context):
        """Re-encrypts a ciphertext with the specified KMS key.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GenerateDataKey(self, request, context):
        """Generates a new symmetric data encryption key (not a KMS key) and returns
        the generated key as plaintext and as ciphertext encrypted with the specified symmetric KMS key.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SymmetricCryptoServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Encrypt': grpc.unary_unary_rpc_method_handler(
                    servicer.Encrypt,
                    request_deserializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.SymmetricEncryptRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.SymmetricEncryptResponse.SerializeToString,
            ),
            'Decrypt': grpc.unary_unary_rpc_method_handler(
                    servicer.Decrypt,
                    request_deserializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.SymmetricDecryptRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.SymmetricDecryptResponse.SerializeToString,
            ),
            'ReEncrypt': grpc.unary_unary_rpc_method_handler(
                    servicer.ReEncrypt,
                    request_deserializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.SymmetricReEncryptRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.SymmetricReEncryptResponse.SerializeToString,
            ),
            'GenerateDataKey': grpc.unary_unary_rpc_method_handler(
                    servicer.GenerateDataKey,
                    request_deserializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.GenerateDataKeyRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.GenerateDataKeyResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.kms.v1.SymmetricCryptoService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.kms.v1.SymmetricCryptoService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class SymmetricCryptoService(object):
    """--- Data plane for KMS symmetric cryptography operations

    Set of methods that perform symmetric encryption and decryption.
    """

    @staticmethod
    def Encrypt(request,
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
            '/yandex.cloud.kms.v1.SymmetricCryptoService/Encrypt',
            yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.SymmetricEncryptRequest.SerializeToString,
            yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.SymmetricEncryptResponse.FromString,
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
            '/yandex.cloud.kms.v1.SymmetricCryptoService/Decrypt',
            yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.SymmetricDecryptRequest.SerializeToString,
            yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.SymmetricDecryptResponse.FromString,
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
    def ReEncrypt(request,
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
            '/yandex.cloud.kms.v1.SymmetricCryptoService/ReEncrypt',
            yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.SymmetricReEncryptRequest.SerializeToString,
            yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.SymmetricReEncryptResponse.FromString,
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
    def GenerateDataKey(request,
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
            '/yandex.cloud.kms.v1.SymmetricCryptoService/GenerateDataKey',
            yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.GenerateDataKeyRequest.SerializeToString,
            yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__crypto__service__pb2.GenerateDataKeyResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
