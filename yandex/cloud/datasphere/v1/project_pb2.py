# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/datasphere/v1/project.proto
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
    'yandex/cloud/datasphere/v1/project.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(yandex/cloud/datasphere/v1/project.proto\x12\x1ayandex.cloud.datasphere.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xf3\x03\n\x07Project\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12>\n\x08settings\x18\x06 \x01(\x0b\x32,.yandex.cloud.datasphere.v1.Project.Settings\x12:\n\x06limits\x18\x07 \x01(\x0b\x32*.yandex.cloud.datasphere.v1.Project.Limits\x1ay\n\x08Settings\x12\x1a\n\x12service_account_id\x18\x01 \x01(\t\x12\x11\n\tsubnet_id\x18\x02 \x01(\t\x12\x1c\n\x14\x64\x61ta_proc_cluster_id\x18\x03 \x01(\t\x12\x1a\n\x12security_group_ids\x18\x05 \x03(\tJ\x04\x08\x04\x10\x05\x1a\x7f\n\x06Limits\x12\x37\n\x12max_units_per_hour\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12<\n\x17max_units_per_execution\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueBk\n\x1eyandex.cloud.api.datasphere.v1ZIgithub.com/yandex-cloud/go-genproto/yandex/cloud/datasphere/v1;datasphereb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.datasphere.v1.project_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036yandex.cloud.api.datasphere.v1ZIgithub.com/yandex-cloud/go-genproto/yandex/cloud/datasphere/v1;datasphere'
  _globals['_PROJECT']._serialized_start=138
  _globals['_PROJECT']._serialized_end=637
  _globals['_PROJECT_SETTINGS']._serialized_start=387
  _globals['_PROJECT_SETTINGS']._serialized_end=508
  _globals['_PROJECT_LIMITS']._serialized_start=510
  _globals['_PROJECT_LIMITS']._serialized_end=637
# @@protoc_insertion_point(module_scope)
