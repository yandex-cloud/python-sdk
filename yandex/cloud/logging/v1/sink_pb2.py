# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/logging/v1/sink.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"yandex/cloud/logging/v1/sink.proto\x12\x17yandex.cloud.logging.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dyandex/cloud/validation.proto\"\xfd\x03\n\x04Sink\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12\x10\n\x08\x63loud_id\x18\x03 \x01(\t\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\x39\n\x06labels\x18\x07 \x03(\x0b\x32).yandex.cloud.logging.v1.Sink.LabelsEntry\x12\x1a\n\x12service_account_id\x18\x08 \x01(\t\x12\x30\n\x03yds\x18\t \x01(\x0b\x32!.yandex.cloud.logging.v1.Sink.YdsH\x00\x12.\n\x02s3\x18\n \x01(\x0b\x32 .yandex.cloud.logging.v1.Sink.S3H\x00\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a%\n\x03Yds\x12\x1e\n\x0bstream_name\x18\x01 \x01(\tB\t\x8a\xc8\x31\x05<=512\x1aT\n\x02S3\x12\x32\n\x06\x62ucket\x18\x01 \x01(\tB\"\xf2\xc7\x31\x1e[a-zA-Z0-9][-a-zA-Z0-9.]{2,62}\x12\x1a\n\x06prefix\x18\x02 \x01(\tB\n\x8a\xc8\x31\x06<=1024B\x0c\n\x04sink\x12\x04\xc0\xc1\x31\x01\x42\x62\n\x1byandex.cloud.api.logging.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/logging/v1;loggingb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.logging.v1.sink_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033yandex.cloud.api.logging.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/logging/v1;logging'
  _SINK_LABELSENTRY._options = None
  _SINK_LABELSENTRY._serialized_options = b'8\001'
  _SINK_YDS.fields_by_name['stream_name']._options = None
  _SINK_YDS.fields_by_name['stream_name']._serialized_options = b'\212\3101\005<=512'
  _SINK_S3.fields_by_name['bucket']._options = None
  _SINK_S3.fields_by_name['bucket']._serialized_options = b'\362\3071\036[a-zA-Z0-9][-a-zA-Z0-9.]{2,62}'
  _SINK_S3.fields_by_name['prefix']._options = None
  _SINK_S3.fields_by_name['prefix']._serialized_options = b'\212\3101\006<=1024'
  _SINK.oneofs_by_name['sink']._options = None
  _SINK.oneofs_by_name['sink']._serialized_options = b'\300\3011\001'
  _globals['_SINK']._serialized_start=128
  _globals['_SINK']._serialized_end=637
  _globals['_SINK_LABELSENTRY']._serialized_start=453
  _globals['_SINK_LABELSENTRY']._serialized_end=498
  _globals['_SINK_YDS']._serialized_start=500
  _globals['_SINK_YDS']._serialized_end=537
  _globals['_SINK_S3']._serialized_start=539
  _globals['_SINK_S3']._serialized_end=623
# @@protoc_insertion_point(module_scope)