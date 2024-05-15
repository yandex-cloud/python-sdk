# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/datasphere/v2/project.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(yandex/cloud/datasphere/v2/project.proto\x12\x1ayandex.cloud.datasphere.v2\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\x9b\x0b\n\x07Project\x12\n\n\x02id\x18\x01 \x01(\t\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12?\n\x06labels\x18\x05 \x03(\x0b\x32/.yandex.cloud.datasphere.v2.Project.LabelsEntry\x12\x15\n\rcreated_by_id\x18\x06 \x01(\t\x12>\n\x08settings\x18\x07 \x01(\x0b\x32,.yandex.cloud.datasphere.v2.Project.Settings\x12:\n\x06limits\x18\x08 \x01(\x0b\x32*.yandex.cloud.datasphere.v2.Project.Limits\x12\x14\n\x0c\x63ommunity_id\x18\x0b \x01(\t\x1a\x90\x07\n\x08Settings\x12\x1a\n\x12service_account_id\x18\x01 \x01(\t\x12\x11\n\tsubnet_id\x18\x02 \x01(\t\x12\x1c\n\x14\x64\x61ta_proc_cluster_id\x18\x03 \x01(\t\x12L\n\x0b\x63ommit_mode\x18\x04 \x01(\x0e\x32\x37.yandex.cloud.datasphere.v2.Project.Settings.CommitMode\x12\x1a\n\x12security_group_ids\x18\x05 \x03(\t\x12\x14\n\x0c\x65\x61rly_access\x18\x06 \x01(\x08\x12=\n\x03ide\x18\x07 \x01(\x0e\x32\x30.yandex.cloud.datasphere.v2.Project.Settings.Ide\x12\x19\n\x11\x64\x65\x66\x61ult_folder_id\x18\x08 \x01(\t\x12g\n\x17stale_exec_timeout_mode\x18\t \x01(\x0e\x32\x46.yandex.cloud.datasphere.v2.Project.Settings.StaleExecutionTimeoutMode\x12Y\n\x12ide_execution_mode\x18\n \x01(\x0e\x32=.yandex.cloud.datasphere.v2.Project.Settings.IdeExecutionMode\x12\x38\n\x15vm_inactivity_timeout\x18\x0b \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x1e\n\x16\x64\x65\x66\x61ult_dedicated_spec\x18\x0c \x01(\t\"A\n\nCommitMode\x12\x1b\n\x17\x43OMMIT_MODE_UNSPECIFIED\x10\x00\x12\x0c\n\x08STANDARD\x10\x01\x12\x08\n\x04\x41UTO\x10\x02\"+\n\x03Ide\x12\x13\n\x0fIDE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bJUPYTER_LAB\x10\x01\"x\n\x19StaleExecutionTimeoutMode\x12,\n(STALE_EXECUTION_TIMEOUT_MODE_UNSPECIFIED\x10\x00\x12\x0c\n\x08ONE_HOUR\x10\x01\x12\x0f\n\x0bTHREE_HOURS\x10\x02\x12\x0e\n\nNO_TIMEOUT\x10\x03\"U\n\x10IdeExecutionMode\x12\"\n\x1eIDE_EXECUTION_MODE_UNSPECIFIED\x10\x00\x12\x0e\n\nSERVERLESS\x10\x01\x12\r\n\tDEDICATED\x10\x02\x1a\x7f\n\x06Limits\x12\x37\n\x12max_units_per_hour\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12<\n\x17max_units_per_execution\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01J\x04\x08\t\x10\nBk\n\x1eyandex.cloud.api.datasphere.v2ZIgithub.com/yandex-cloud/go-genproto/yandex/cloud/datasphere/v2;datasphereb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.datasphere.v2.project_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036yandex.cloud.api.datasphere.v2ZIgithub.com/yandex-cloud/go-genproto/yandex/cloud/datasphere/v2;datasphere'
  _globals['_PROJECT_LABELSENTRY']._loaded_options = None
  _globals['_PROJECT_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_PROJECT']._serialized_start=170
  _globals['_PROJECT']._serialized_end=1605
  _globals['_PROJECT_SETTINGS']._serialized_start=511
  _globals['_PROJECT_SETTINGS']._serialized_end=1423
  _globals['_PROJECT_SETTINGS_COMMITMODE']._serialized_start=1104
  _globals['_PROJECT_SETTINGS_COMMITMODE']._serialized_end=1169
  _globals['_PROJECT_SETTINGS_IDE']._serialized_start=1171
  _globals['_PROJECT_SETTINGS_IDE']._serialized_end=1214
  _globals['_PROJECT_SETTINGS_STALEEXECUTIONTIMEOUTMODE']._serialized_start=1216
  _globals['_PROJECT_SETTINGS_STALEEXECUTIONTIMEOUTMODE']._serialized_end=1336
  _globals['_PROJECT_SETTINGS_IDEEXECUTIONMODE']._serialized_start=1338
  _globals['_PROJECT_SETTINGS_IDEEXECUTIONMODE']._serialized_end=1423
  _globals['_PROJECT_LIMITS']._serialized_start=1425
  _globals['_PROJECT_LIMITS']._serialized_end=1552
  _globals['_PROJECT_LABELSENTRY']._serialized_start=1554
  _globals['_PROJECT_LABELSENTRY']._serialized_end=1599
# @@protoc_insertion_point(module_scope)
