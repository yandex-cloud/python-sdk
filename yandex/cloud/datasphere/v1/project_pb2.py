# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/datasphere/v1/project.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(yandex/cloud/datasphere/v1/project.proto\x12\x1ayandex.cloud.datasphere.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xff\x04\n\x07Project\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12>\n\x08settings\x18\x06 \x01(\x0b\x32,.yandex.cloud.datasphere.v1.Project.Settings\x12:\n\x06limits\x18\x07 \x01(\x0b\x32*.yandex.cloud.datasphere.v1.Project.Limits\x1a\x84\x02\n\x08Settings\x12\x1a\n\x12service_account_id\x18\x01 \x01(\t\x12\x11\n\tsubnet_id\x18\x02 \x01(\t\x12\x1c\n\x14\x64\x61ta_proc_cluster_id\x18\x03 \x01(\t\x12L\n\x0b\x63ommit_mode\x18\x04 \x01(\x0e\x32\x37.yandex.cloud.datasphere.v1.Project.Settings.CommitMode\x12\x1a\n\x12security_group_ids\x18\x05 \x03(\t\"A\n\nCommitMode\x12\x1b\n\x17\x43OMMIT_MODE_UNSPECIFIED\x10\x00\x12\x0c\n\x08STANDARD\x10\x01\x12\x08\n\x04\x41UTO\x10\x02\x1a\x7f\n\x06Limits\x12\x37\n\x12max_units_per_hour\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12<\n\x17max_units_per_execution\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueBk\n\x1eyandex.cloud.api.datasphere.v1ZIgithub.com/yandex-cloud/go-genproto/yandex/cloud/datasphere/v1;datasphereb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.datasphere.v1.project_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\036yandex.cloud.api.datasphere.v1ZIgithub.com/yandex-cloud/go-genproto/yandex/cloud/datasphere/v1;datasphere'
  _globals['_PROJECT']._serialized_start=138
  _globals['_PROJECT']._serialized_end=777
  _globals['_PROJECT_SETTINGS']._serialized_start=388
  _globals['_PROJECT_SETTINGS']._serialized_end=648
  _globals['_PROJECT_SETTINGS_COMMITMODE']._serialized_start=583
  _globals['_PROJECT_SETTINGS_COMMITMODE']._serialized_end=648
  _globals['_PROJECT_LIMITS']._serialized_start=650
  _globals['_PROJECT_LIMITS']._serialized_end=777
# @@protoc_insertion_point(module_scope)
