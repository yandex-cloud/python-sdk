# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/cdn/v1/rule.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.cdn.v1 import resource_pb2 as yandex_dot_cloud_dot_cdn_dot_v1_dot_resource__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eyandex/cloud/cdn/v1/rule.proto\x12\x13yandex.cloud.cdn.v1\x1a\"yandex/cloud/cdn/v1/resource.proto\x1a\x1dyandex/cloud/validation.proto\"\x92\x01\n\x04Rule\x12\x12\n\x02id\x18\x01 \x01(\x03\x42\x06\xfa\xc7\x31\x02>0\x12\x1a\n\x04name\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12#\n\x0crule_pattern\x18\x03 \x01(\tB\r\xe8\xc7\x31\x01\x8a\xc8\x31\x05<=100\x12\x35\n\x07options\x18\x04 \x01(\x0b\x32$.yandex.cloud.cdn.v1.ResourceOptionsBV\n\x17yandex.cloud.api.cdn.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/cdn/v1;cdnb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.cdn.v1.rule_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027yandex.cloud.api.cdn.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/cdn/v1;cdn'
  _RULE.fields_by_name['id']._options = None
  _RULE.fields_by_name['id']._serialized_options = b'\372\3071\002>0'
  _RULE.fields_by_name['name']._options = None
  _RULE.fields_by_name['name']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _RULE.fields_by_name['rule_pattern']._options = None
  _RULE.fields_by_name['rule_pattern']._serialized_options = b'\350\3071\001\212\3101\005<=100'
  _globals['_RULE']._serialized_start=123
  _globals['_RULE']._serialized_end=269
# @@protoc_insertion_point(module_scope)