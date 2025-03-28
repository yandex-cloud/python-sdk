# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/logging/v1/log_group.proto
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
    'yandex/cloud/logging/v1/log_group.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'yandex/cloud/logging/v1/log_group.proto\x12\x17yandex.cloud.logging.v1\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xd5\x03\n\x08LogGroup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12\x10\n\x08\x63loud_id\x18\x03 \x01(\t\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12=\n\x06labels\x18\x07 \x03(\x0b\x32-.yandex.cloud.logging.v1.LogGroup.LabelsEntry\x12\x38\n\x06status\x18\x08 \x01(\x0e\x32(.yandex.cloud.logging.v1.LogGroup.Status\x12\x33\n\x10retention_period\x18\t \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x13\n\x0b\x64\x61ta_stream\x18\n \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"S\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12\x0c\n\x08\x44\x45LETING\x10\x03\x12\t\n\x05\x45RROR\x10\x04\x42\x62\n\x1byandex.cloud.api.logging.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/logging/v1;loggingb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.logging.v1.log_group_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033yandex.cloud.api.logging.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/logging/v1;logging'
  _globals['_LOGGROUP_LABELSENTRY']._loaded_options = None
  _globals['_LOGGROUP_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_LOGGROUP']._serialized_start=134
  _globals['_LOGGROUP']._serialized_end=603
  _globals['_LOGGROUP_LABELSENTRY']._serialized_start=473
  _globals['_LOGGROUP_LABELSENTRY']._serialized_end=518
  _globals['_LOGGROUP_STATUS']._serialized_start=520
  _globals['_LOGGROUP_STATUS']._serialized_end=603
# @@protoc_insertion_point(module_scope)
