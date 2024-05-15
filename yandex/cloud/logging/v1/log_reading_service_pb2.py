# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/logging/v1/log_reading_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.logging.v1 import log_entry_pb2 as yandex_dot_cloud_dot_logging_dot_v1_dot_log__entry__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1yandex/cloud/logging/v1/log_reading_service.proto\x12\x17yandex.cloud.logging.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dyandex/cloud/validation.proto\x1a\'yandex/cloud/logging/v1/log_entry.proto\"f\n\x0bReadRequest\x12\x14\n\npage_token\x18\x01 \x01(\tH\x00\x12\x35\n\x08\x63riteria\x18\x02 \x01(\x0b\x32!.yandex.cloud.logging.v1.CriteriaH\x00\x42\n\n\x08selector\"\x8e\x01\n\x0cReadResponse\x12\x14\n\x0clog_group_id\x18\x01 \x01(\t\x12\x32\n\x07\x65ntries\x18\x02 \x03(\x0b\x32!.yandex.cloud.logging.v1.LogEntry\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t\x12\x1b\n\x13previous_page_token\x18\x04 \x01(\t\"\xaa\x03\n\x08\x43riteria\x12\"\n\x0clog_group_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=64\x12)\n\x0eresource_types\x18\x02 \x03(\tB\x11\x82\xc8\x31\x05<=100\x8a\xc8\x31\x04<=63\x12\'\n\x0cresource_ids\x18\x03 \x03(\tB\x11\x82\xc8\x31\x05<=100\x8a\xc8\x31\x04<=63\x12)\n\x05since\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12)\n\x05until\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x41\n\x06levels\x18\x06 \x03(\x0e\x32\'.yandex.cloud.logging.v1.LogLevel.LevelB\x08\x82\xc8\x31\x04<=10\x12\x1a\n\x06\x66ilter\x18\x07 \x01(\tB\n\x8a\xc8\x31\x06<=1000\x12\'\n\x0cstream_names\x18\n \x03(\tB\x11\x82\xc8\x31\x05<=100\x8a\xc8\x31\x04<=63\x12\x1d\n\tpage_size\x18\x08 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12)\n\x11max_response_size\x18\t \x01(\x03\x42\x0e\xfa\xc7\x31\n0-104857602h\n\x11LogReadingService\x12S\n\x04Read\x12$.yandex.cloud.logging.v1.ReadRequest\x1a%.yandex.cloud.logging.v1.ReadResponseBb\n\x1byandex.cloud.api.logging.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/logging/v1;loggingb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.logging.v1.log_reading_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033yandex.cloud.api.logging.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/logging/v1;logging'
  _CRITERIA.fields_by_name['log_group_id']._options = None
  _CRITERIA.fields_by_name['log_group_id']._serialized_options = b'\350\3071\001\212\3101\004<=64'
  _CRITERIA.fields_by_name['resource_types']._options = None
  _CRITERIA.fields_by_name['resource_types']._serialized_options = b'\202\3101\005<=100\212\3101\004<=63'
  _CRITERIA.fields_by_name['resource_ids']._options = None
  _CRITERIA.fields_by_name['resource_ids']._serialized_options = b'\202\3101\005<=100\212\3101\004<=63'
  _CRITERIA.fields_by_name['levels']._options = None
  _CRITERIA.fields_by_name['levels']._serialized_options = b'\202\3101\004<=10'
  _CRITERIA.fields_by_name['filter']._options = None
  _CRITERIA.fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _CRITERIA.fields_by_name['stream_names']._options = None
  _CRITERIA.fields_by_name['stream_names']._serialized_options = b'\202\3101\005<=100\212\3101\004<=63'
  _CRITERIA.fields_by_name['page_size']._options = None
  _CRITERIA.fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _CRITERIA.fields_by_name['max_response_size']._options = None
  _CRITERIA.fields_by_name['max_response_size']._serialized_options = b'\372\3071\n0-10485760'
  _globals['_READREQUEST']._serialized_start=183
  _globals['_READREQUEST']._serialized_end=285
  _globals['_READRESPONSE']._serialized_start=288
  _globals['_READRESPONSE']._serialized_end=430
  _globals['_CRITERIA']._serialized_start=433
  _globals['_CRITERIA']._serialized_end=859
  _globals['_LOGREADINGSERVICE']._serialized_start=861
  _globals['_LOGREADINGSERVICE']._serialized_end=965
# @@protoc_insertion_point(module_scope)
