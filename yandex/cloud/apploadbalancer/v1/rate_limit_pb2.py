# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/apploadbalancer/v1/rate_limit.proto
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
    'yandex/cloud/apploadbalancer/v1/rate_limit.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0yandex/cloud/apploadbalancer/v1/rate_limit.proto\x12\x1fyandex.cloud.apploadbalancer.v1\x1a\x1dyandex/cloud/validation.proto\"\xf1\x01\n\tRateLimit\x12\x46\n\x0c\x61ll_requests\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.apploadbalancer.v1.RateLimit.Limit\x12I\n\x0frequests_per_ip\x18\x04 \x01(\x0b\x32\x30.yandex.cloud.apploadbalancer.v1.RateLimit.Limit\x1aQ\n\x05Limit\x12\x1c\n\nper_second\x18\x01 \x01(\x03\x42\x06\xfa\xc7\x31\x02>0H\x00\x12\x1c\n\nper_minute\x18\x02 \x01(\x03\x42\x06\xfa\xc7\x31\x02>0H\x00\x42\x0c\n\x04rate\x12\x04\xc0\xc1\x31\x01\x42z\n#yandex.cloud.api.apploadbalancer.v1ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/apploadbalancer/v1;apploadbalancerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.apploadbalancer.v1.rate_limit_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n#yandex.cloud.api.apploadbalancer.v1ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/apploadbalancer/v1;apploadbalancer'
  _globals['_RATELIMIT_LIMIT'].oneofs_by_name['rate']._loaded_options = None
  _globals['_RATELIMIT_LIMIT'].oneofs_by_name['rate']._serialized_options = b'\300\3011\001'
  _globals['_RATELIMIT_LIMIT'].fields_by_name['per_second']._loaded_options = None
  _globals['_RATELIMIT_LIMIT'].fields_by_name['per_second']._serialized_options = b'\372\3071\002>0'
  _globals['_RATELIMIT_LIMIT'].fields_by_name['per_minute']._loaded_options = None
  _globals['_RATELIMIT_LIMIT'].fields_by_name['per_minute']._serialized_options = b'\372\3071\002>0'
  _globals['_RATELIMIT']._serialized_start=117
  _globals['_RATELIMIT']._serialized_end=358
  _globals['_RATELIMIT_LIMIT']._serialized_start=277
  _globals['_RATELIMIT_LIMIT']._serialized_end=358
# @@protoc_insertion_point(module_scope)
