# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/ai/tuning/v1/tuning_task.proto
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
    'yandex/cloud/ai/tuning/v1/tuning_task.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+yandex/cloud/ai/tuning/v1/tuning_task.proto\x12\x19yandex.cloud.ai.tuning.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\xd9\x03\n\nTuningTask\x12\x0f\n\x07task_id\x18\x01 \x01(\t\x12\x14\n\x0coperation_id\x18\x03 \x01(\t\x12<\n\x06status\x18\x04 \x01(\x0e\x32,.yandex.cloud.ai.tuning.v1.TuningTask.Status\x12\x11\n\tfolder_id\x18\x05 \x01(\t\x12\x12\n\ncreated_by\x18\x06 \x01(\t\x12.\n\ncreated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nstarted_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x66inished_at\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x18\n\x10source_model_uri\x18\n \x01(\t\x12\x18\n\x10target_model_uri\x18\x0b \x01(\t\"t\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0b\n\x07\x43REATED\x10\x01\x12\x0b\n\x07PENDING\x10\x02\x12\x0f\n\x0bIN_PROGRESS\x10\x03\x12\r\n\tCOMPLETED\x10\x04\x12\n\n\x06\x46\x41ILED\x10\x05\x12\x0c\n\x08\x43\x41NCELED\x10\x06J\x04\x08\x02\x10\x03\x42\x63\n\x1dyandex.cloud.api.ai.tuning.v1ZBgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/tuning/v1;fomob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.ai.tuning.v1.tuning_task_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035yandex.cloud.api.ai.tuning.v1ZBgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/tuning/v1;fomo'
  _globals['_TUNINGTASK']._serialized_start=108
  _globals['_TUNINGTASK']._serialized_end=581
  _globals['_TUNINGTASK_STATUS']._serialized_start=459
  _globals['_TUNINGTASK_STATUS']._serialized_end=575
# @@protoc_insertion_point(module_scope)
