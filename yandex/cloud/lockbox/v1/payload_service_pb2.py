# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/lockbox/v1/payload_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.lockbox.v1 import payload_pb2 as yandex_dot_cloud_dot_lockbox_dot_v1_dot_payload__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-yandex/cloud/lockbox/v1/payload_service.proto\x12\x17yandex.cloud.lockbox.v1\x1a\x1cgoogle/api/annotations.proto\x1a%yandex/cloud/lockbox/v1/payload.proto\x1a\x1dyandex/cloud/validation.proto\"R\n\x11GetPayloadRequest\x12\x1f\n\tsecret_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1c\n\nversion_id\x18\x02 \x01(\tB\x08\x8a\xc8\x31\x04<=502\x97\x01\n\x0ePayloadService\x12\x84\x01\n\x03Get\x12*.yandex.cloud.lockbox.v1.GetPayloadRequest\x1a .yandex.cloud.lockbox.v1.Payload\"/\x82\xd3\xe4\x93\x02)\x12\'/lockbox/v1/secrets/{secret_id}/payloadBb\n\x1byandex.cloud.api.lockbox.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/lockbox/v1;lockboxb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.lockbox.v1.payload_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033yandex.cloud.api.lockbox.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/lockbox/v1;lockbox'
  _GETPAYLOADREQUEST.fields_by_name['secret_id']._options = None
  _GETPAYLOADREQUEST.fields_by_name['secret_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _GETPAYLOADREQUEST.fields_by_name['version_id']._options = None
  _GETPAYLOADREQUEST.fields_by_name['version_id']._serialized_options = b'\212\3101\004<=50'
  _PAYLOADSERVICE.methods_by_name['Get']._options = None
  _PAYLOADSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002)\022\'/lockbox/v1/secrets/{secret_id}/payload'
  _globals['_GETPAYLOADREQUEST']._serialized_start=174
  _globals['_GETPAYLOADREQUEST']._serialized_end=256
  _globals['_PAYLOADSERVICE']._serialized_start=259
  _globals['_PAYLOADSERVICE']._serialized_end=410
# @@protoc_insertion_point(module_scope)
