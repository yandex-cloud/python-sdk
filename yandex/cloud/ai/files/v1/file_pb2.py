# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/ai/files/v1/file.proto
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
    'yandex/cloud/ai/files/v1/file.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.ai.common import common_pb2 as yandex_dot_cloud_dot_ai_dot_common_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#yandex/cloud/ai/files/v1/file.proto\x12\x18yandex.cloud.ai.files.v1\x1a#yandex/cloud/ai/common/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xc3\x03\n\x04\x46ile\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x11\n\tmime_type\x18\x05 \x01(\t\x12\x12\n\ncreated_by\x18\x06 \x01(\t\x12.\n\ncreated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nupdated_by\x18\x08 \x01(\t\x12.\n\nupdated_at\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x43\n\x11\x65xpiration_config\x18\n \x01(\x0b\x32(.yandex.cloud.ai.common.ExpirationConfig\x12.\n\nexpires_at\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12:\n\x06labels\x18\x0c \x03(\x0b\x32*.yandex.cloud.ai.files.v1.File.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x62\n\x1cyandex.cloud.api.ai.files.v1ZBgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/files/v1;filesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.ai.files.v1.file_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034yandex.cloud.api.ai.files.v1ZBgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/files/v1;files'
  _globals['_FILE_LABELSENTRY']._loaded_options = None
  _globals['_FILE_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_FILE']._serialized_start=136
  _globals['_FILE']._serialized_end=587
  _globals['_FILE_LABELSENTRY']._serialized_start=542
  _globals['_FILE_LABELSENTRY']._serialized_end=587
# @@protoc_insertion_point(module_scope)
