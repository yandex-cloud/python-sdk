# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/apploadbalancer/v1/payload.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'yandex/cloud/apploadbalancer/v1/payload.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-yandex/cloud/apploadbalancer/v1/payload.proto\x12\x1fyandex.cloud.apploadbalancer.v1\x1a\x1dyandex/cloud/validation.proto\"2\n\x07Payload\x12\x16\n\x04text\x18\x01 \x01(\tB\x06\x8a\xc8\x31\x02>0H\x00\x42\x0f\n\x07payload\x12\x04\xc0\xc1\x31\x01\x42z\n#yandex.cloud.api.apploadbalancer.v1ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/apploadbalancer/v1;apploadbalancerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.apploadbalancer.v1.payload_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n#yandex.cloud.api.apploadbalancer.v1ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/apploadbalancer/v1;apploadbalancer'
  _globals['_PAYLOAD'].oneofs_by_name['payload']._loaded_options = None
  _globals['_PAYLOAD'].oneofs_by_name['payload']._serialized_options = b'\300\3011\001'
  _globals['_PAYLOAD'].fields_by_name['text']._loaded_options = None
  _globals['_PAYLOAD'].fields_by_name['text']._serialized_options = b'\212\3101\002>0'
  _globals['_PAYLOAD']._serialized_start=113
  _globals['_PAYLOAD']._serialized_end=163
# @@protoc_insertion_point(module_scope)
