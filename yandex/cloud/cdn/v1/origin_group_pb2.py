# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/cdn/v1/origin_group.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.cdn.v1 import origin_pb2 as yandex_dot_cloud_dot_cdn_dot_v1_dot_origin__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&yandex/cloud/cdn/v1/origin_group.proto\x12\x13yandex.cloud.cdn.v1\x1a yandex/cloud/cdn/v1/origin.proto\"z\n\x0bOriginGroup\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x10\n\x08use_next\x18\x04 \x01(\x08\x12,\n\x07origins\x18\x05 \x03(\x0b\x32\x1b.yandex.cloud.cdn.v1.OriginBV\n\x17yandex.cloud.api.cdn.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/cdn/v1;cdnb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.cdn.v1.origin_group_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027yandex.cloud.api.cdn.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/cdn/v1;cdn'
  _globals['_ORIGINGROUP']._serialized_start=97
  _globals['_ORIGINGROUP']._serialized_end=219
# @@protoc_insertion_point(module_scope)
