# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/redis/v1/resource_preset_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.mdb.redis.v1 import resource_preset_pb2 as yandex_dot_cloud_dot_mdb_dot_redis_dot_v1_dot_resource__preset__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7yandex/cloud/mdb/redis/v1/resource_preset_service.proto\x12\x19yandex.cloud.mdb.redis.v1\x1a\x1cgoogle/api/annotations.proto\x1a/yandex/cloud/mdb/redis/v1/resource_preset.proto\x1a\x1dyandex/cloud/validation.proto\"<\n\x18GetResourcePresetRequest\x12 \n\x12resource_preset_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"C\n\x1aListResourcePresetsRequest\x12\x11\n\tpage_size\x18\x02 \x01(\x03\x12\x12\n\npage_token\x18\x03 \x01(\t\"{\n\x1bListResourcePresetsResponse\x12\x43\n\x10resource_presets\x18\x01 \x03(\x0b\x32).yandex.cloud.mdb.redis.v1.ResourcePreset\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xe2\x02\n\x15ResourcePresetService\x12\xa5\x01\n\x03Get\x12\x33.yandex.cloud.mdb.redis.v1.GetResourcePresetRequest\x1a).yandex.cloud.mdb.redis.v1.ResourcePreset\">\x82\xd3\xe4\x93\x02\x38\x12\x36/managed-redis/v1/resourcePresets/{resource_preset_id}\x12\xa0\x01\n\x04List\x12\x35.yandex.cloud.mdb.redis.v1.ListResourcePresetsRequest\x1a\x36.yandex.cloud.mdb.redis.v1.ListResourcePresetsResponse\")\x82\xd3\xe4\x93\x02#\x12!/managed-redis/v1/resourcePresetsBd\n\x1dyandex.cloud.api.mdb.redis.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/redis/v1;redisb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.redis.v1.resource_preset_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\035yandex.cloud.api.mdb.redis.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/redis/v1;redis'
  _GETRESOURCEPRESETREQUEST.fields_by_name['resource_preset_id']._options = None
  _GETRESOURCEPRESETREQUEST.fields_by_name['resource_preset_id']._serialized_options = b'\350\3071\001'
  _RESOURCEPRESETSERVICE.methods_by_name['Get']._options = None
  _RESOURCEPRESETSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\0028\0226/managed-redis/v1/resourcePresets/{resource_preset_id}'
  _RESOURCEPRESETSERVICE.methods_by_name['List']._options = None
  _RESOURCEPRESETSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002#\022!/managed-redis/v1/resourcePresets'
  _globals['_GETRESOURCEPRESETREQUEST']._serialized_start=196
  _globals['_GETRESOURCEPRESETREQUEST']._serialized_end=256
  _globals['_LISTRESOURCEPRESETSREQUEST']._serialized_start=258
  _globals['_LISTRESOURCEPRESETSREQUEST']._serialized_end=325
  _globals['_LISTRESOURCEPRESETSRESPONSE']._serialized_start=327
  _globals['_LISTRESOURCEPRESETSRESPONSE']._serialized_end=450
  _globals['_RESOURCEPRESETSERVICE']._serialized_start=453
  _globals['_RESOURCEPRESETSERVICE']._serialized_end=807
# @@protoc_insertion_point(module_scope)
