# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/dataproc/v1/resource_preset_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.dataproc.v1 import resource_preset_pb2 as yandex_dot_cloud_dot_dataproc_dot_v1_dot_resource__preset__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6yandex/cloud/dataproc/v1/resource_preset_service.proto\x12\x18yandex.cloud.dataproc.v1\x1a\x1cgoogle/api/annotations.proto\x1a.yandex/cloud/dataproc/v1/resource_preset.proto\x1a\x1dyandex/cloud/validation.proto\"<\n\x18GetResourcePresetRequest\x12 \n\x12resource_preset_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"Z\n\x1aListResourcePresetsRequest\x12\x1d\n\tpage_size\x18\x01 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x02 \x01(\tB\t\x8a\xc8\x31\x05<=100\"\x85\x01\n\x1bListResourcePresetsResponse\x12\x42\n\x10resource_presets\x18\x01 \x03(\x0b\x32(.yandex.cloud.dataproc.v1.ResourcePreset\x12\"\n\x0fnext_page_token\x18\x02 \x01(\tB\t\x8a\xc8\x31\x05<=1002\xd4\x02\n\x15ResourcePresetService\x12\x9e\x01\n\x03Get\x12\x32.yandex.cloud.dataproc.v1.GetResourcePresetRequest\x1a(.yandex.cloud.dataproc.v1.ResourcePreset\"9\x82\xd3\xe4\x93\x02\x33\x12\x31/dataproc/v1/resourcePresets/{resource_preset_id}\x12\x99\x01\n\x04List\x12\x34.yandex.cloud.dataproc.v1.ListResourcePresetsRequest\x1a\x35.yandex.cloud.dataproc.v1.ListResourcePresetsResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/dataproc/v1/resourcePresetsBe\n\x1cyandex.cloud.api.dataproc.v1ZEgithub.com/yandex-cloud/go-genproto/yandex/cloud/dataproc/v1;dataprocb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.dataproc.v1.resource_preset_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034yandex.cloud.api.dataproc.v1ZEgithub.com/yandex-cloud/go-genproto/yandex/cloud/dataproc/v1;dataproc'
  _globals['_GETRESOURCEPRESETREQUEST'].fields_by_name['resource_preset_id']._loaded_options = None
  _globals['_GETRESOURCEPRESETREQUEST'].fields_by_name['resource_preset_id']._serialized_options = b'\350\3071\001'
  _globals['_LISTRESOURCEPRESETSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTRESOURCEPRESETSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTRESOURCEPRESETSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTRESOURCEPRESETSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTRESOURCEPRESETSRESPONSE'].fields_by_name['next_page_token']._loaded_options = None
  _globals['_LISTRESOURCEPRESETSRESPONSE'].fields_by_name['next_page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_RESOURCEPRESETSERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_RESOURCEPRESETSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\0023\0221/dataproc/v1/resourcePresets/{resource_preset_id}'
  _globals['_RESOURCEPRESETSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_RESOURCEPRESETSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002\036\022\034/dataproc/v1/resourcePresets'
  _globals['_GETRESOURCEPRESETREQUEST']._serialized_start=193
  _globals['_GETRESOURCEPRESETREQUEST']._serialized_end=253
  _globals['_LISTRESOURCEPRESETSREQUEST']._serialized_start=255
  _globals['_LISTRESOURCEPRESETSREQUEST']._serialized_end=345
  _globals['_LISTRESOURCEPRESETSRESPONSE']._serialized_start=348
  _globals['_LISTRESOURCEPRESETSRESPONSE']._serialized_end=481
  _globals['_RESOURCEPRESETSERVICE']._serialized_start=484
  _globals['_RESOURCEPRESETSERVICE']._serialized_end=824
# @@protoc_insertion_point(module_scope)
