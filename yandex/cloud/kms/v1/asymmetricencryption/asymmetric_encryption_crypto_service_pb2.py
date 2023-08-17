# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/kms/v1/asymmetricencryption/asymmetric_encryption_crypto_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nSyandex/cloud/kms/v1/asymmetricencryption/asymmetric_encryption_crypto_service.proto\x12(yandex.cloud.kms.v1.asymmetricencryption\x1a\x1cgoogle/api/annotations.proto\x1a\x1dyandex/cloud/validation.proto\"]\n\x18\x41symmetricDecryptRequest\x12\x1c\n\x06key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12#\n\nciphertext\x18\x02 \x01(\x0c\x42\x0f\xe8\xc7\x31\x01\x8a\xc8\x31\x07<=32768\">\n\x19\x41symmetricDecryptResponse\x12\x0e\n\x06key_id\x18\x01 \x01(\t\x12\x11\n\tplaintext\x18\x02 \x01(\x0c\"=\n\x1d\x41symmetricGetPublicKeyRequest\x12\x1c\n\x06key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"D\n\x1e\x41symmetricGetPublicKeyResponse\x12\x0e\n\x06key_id\x18\x01 \x01(\t\x12\x12\n\npublic_key\x18\x02 \x01(\t2\xd7\x03\n!AsymmetricEncryptionCryptoService\x12\xd0\x01\n\x07\x44\x65\x63rypt\x12\x42.yandex.cloud.kms.v1.asymmetricencryption.AsymmetricDecryptRequest\x1a\x43.yandex.cloud.kms.v1.asymmetricencryption.AsymmetricDecryptResponse\"<\x82\xd3\xe4\x93\x02\x36\"1/kms/v1/asymmetricEncryptionKeys/{key_id}:decrypt:\x01*\x12\xde\x01\n\x0cGetPublicKey\x12G.yandex.cloud.kms.v1.asymmetricencryption.AsymmetricGetPublicKeyRequest\x1aH.yandex.cloud.kms.v1.asymmetricencryption.AsymmetricGetPublicKeyResponse\";\x82\xd3\xe4\x93\x02\x35\x12\x33/kms/v1/asymmetricEncryptionKeys/{key_id}/publicKeyBk\n\x17yandex.cloud.api.kms.v1ZPgithub.com/yandex-cloud/go-genproto/yandex/cloud/kms/v1/asymmetricencryption;kmsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.kms.v1.asymmetricencryption.asymmetric_encryption_crypto_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027yandex.cloud.api.kms.v1ZPgithub.com/yandex-cloud/go-genproto/yandex/cloud/kms/v1/asymmetricencryption;kms'
  _ASYMMETRICDECRYPTREQUEST.fields_by_name['key_id']._options = None
  _ASYMMETRICDECRYPTREQUEST.fields_by_name['key_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _ASYMMETRICDECRYPTREQUEST.fields_by_name['ciphertext']._options = None
  _ASYMMETRICDECRYPTREQUEST.fields_by_name['ciphertext']._serialized_options = b'\350\3071\001\212\3101\007<=32768'
  _ASYMMETRICGETPUBLICKEYREQUEST.fields_by_name['key_id']._options = None
  _ASYMMETRICGETPUBLICKEYREQUEST.fields_by_name['key_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _ASYMMETRICENCRYPTIONCRYPTOSERVICE.methods_by_name['Decrypt']._options = None
  _ASYMMETRICENCRYPTIONCRYPTOSERVICE.methods_by_name['Decrypt']._serialized_options = b'\202\323\344\223\0026\"1/kms/v1/asymmetricEncryptionKeys/{key_id}:decrypt:\001*'
  _ASYMMETRICENCRYPTIONCRYPTOSERVICE.methods_by_name['GetPublicKey']._options = None
  _ASYMMETRICENCRYPTIONCRYPTOSERVICE.methods_by_name['GetPublicKey']._serialized_options = b'\202\323\344\223\0025\0223/kms/v1/asymmetricEncryptionKeys/{key_id}/publicKey'
  _globals['_ASYMMETRICDECRYPTREQUEST']._serialized_start=190
  _globals['_ASYMMETRICDECRYPTREQUEST']._serialized_end=283
  _globals['_ASYMMETRICDECRYPTRESPONSE']._serialized_start=285
  _globals['_ASYMMETRICDECRYPTRESPONSE']._serialized_end=347
  _globals['_ASYMMETRICGETPUBLICKEYREQUEST']._serialized_start=349
  _globals['_ASYMMETRICGETPUBLICKEYREQUEST']._serialized_end=410
  _globals['_ASYMMETRICGETPUBLICKEYRESPONSE']._serialized_start=412
  _globals['_ASYMMETRICGETPUBLICKEYRESPONSE']._serialized_end=480
  _globals['_ASYMMETRICENCRYPTIONCRYPTOSERVICE']._serialized_start=483
  _globals['_ASYMMETRICENCRYPTIONCRYPTOSERVICE']._serialized_end=954
# @@protoc_insertion_point(module_scope)
