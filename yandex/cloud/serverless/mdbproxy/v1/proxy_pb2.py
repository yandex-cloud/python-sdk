# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/serverless/mdbproxy/v1/proxy.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/yandex/cloud/serverless/mdbproxy/v1/proxy.proto\x12#yandex.cloud.serverless.mdbproxy.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dyandex/cloud/validation.proto\"\xa8\x03\n\x05Proxy\x12\n\n\x02id\x18\x01 \x01(\t\x12\x1f\n\tfolder_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x04name\x18\x04 \x01(\tB%\xe8\xc7\x31\x01\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x8b\x01\n\x06labels\x18\x06 \x03(\x0b\x32\x36.yandex.cloud.serverless.mdbproxy.v1.Proxy.LabelsEntryBC\xf2\xc7\x31\x0f[-_./\\@0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x1c\x12\x14[a-z][-_./\\@0-9a-z]*\x1a\x04\x31-63\x12;\n\x06target\x18\x07 \x01(\x0b\x32+.yandex.cloud.serverless.mdbproxy.v1.Target\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x8e\x04\n\x06Target\x12L\n\nclickhouse\x18\x01 \x01(\x0b\x32\x36.yandex.cloud.serverless.mdbproxy.v1.Target.ClickHouseH\x00\x12L\n\npostgresql\x18\x02 \x01(\x0b\x32\x36.yandex.cloud.serverless.mdbproxy.v1.Target.PostgreSQLH\x00\x1a\xac\x01\n\nPostgreSQL\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12,\n\x04user\x18\x02 \x01(\tB\x1e\xe8\xc7\x31\x01\xf2\xc7\x31\x0e[a-zA-Z0-9_-]*\x8a\xc8\x31\x04<=63\x12\x10\n\x08password\x18\x03 \x01(\t\x12*\n\x02\x64\x62\x18\x04 \x01(\tB\x1e\xe8\xc7\x31\x01\xf2\xc7\x31\x0e[a-zA-Z0-9_-]*\x8a\xc8\x31\x04<=63\x12\x10\n\x08\x65ndpoint\x18\x05 \x01(\t\x1a\xab\x01\n\nClickHouse\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12+\n\x04user\x18\x02 \x01(\tB\x1d\xe8\xc7\x31\x01\xf2\xc7\x31\r[a-zA-Z0-9_]*\x8a\xc8\x31\x04<=63\x12\x10\n\x08password\x18\x03 \x01(\t\x12*\n\x02\x64\x62\x18\x04 \x01(\tB\x1e\xe8\xc7\x31\x01\xf2\xc7\x31\x0e[a-zA-Z0-9_-]*\x8a\xc8\x31\x04<=63\x12\x10\n\x08\x65ndpoint\x18\x05 \x01(\tB\x0b\n\x03mdb\x12\x04\xc0\xc1\x31\x01\x42x\n\'yandex.cloud.api.serverless.mdbproxy.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/mdbproxy/v1;proxyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.serverless.mdbproxy.v1.proxy_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\'yandex.cloud.api.serverless.mdbproxy.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/mdbproxy/v1;proxy'
  _PROXY_LABELSENTRY._options = None
  _PROXY_LABELSENTRY._serialized_options = b'8\001'
  _PROXY.fields_by_name['folder_id']._options = None
  _PROXY.fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _PROXY.fields_by_name['name']._options = None
  _PROXY.fields_by_name['name']._serialized_options = b'\350\3071\001\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _PROXY.fields_by_name['labels']._options = None
  _PROXY.fields_by_name['labels']._serialized_options = b'\362\3071\017[-_./\\@0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\034\022\024[a-z][-_./\\@0-9a-z]*\032\0041-63'
  _TARGET_POSTGRESQL.fields_by_name['cluster_id']._options = None
  _TARGET_POSTGRESQL.fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _TARGET_POSTGRESQL.fields_by_name['user']._options = None
  _TARGET_POSTGRESQL.fields_by_name['user']._serialized_options = b'\350\3071\001\362\3071\016[a-zA-Z0-9_-]*\212\3101\004<=63'
  _TARGET_POSTGRESQL.fields_by_name['db']._options = None
  _TARGET_POSTGRESQL.fields_by_name['db']._serialized_options = b'\350\3071\001\362\3071\016[a-zA-Z0-9_-]*\212\3101\004<=63'
  _TARGET_CLICKHOUSE.fields_by_name['cluster_id']._options = None
  _TARGET_CLICKHOUSE.fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _TARGET_CLICKHOUSE.fields_by_name['user']._options = None
  _TARGET_CLICKHOUSE.fields_by_name['user']._serialized_options = b'\350\3071\001\362\3071\r[a-zA-Z0-9_]*\212\3101\004<=63'
  _TARGET_CLICKHOUSE.fields_by_name['db']._options = None
  _TARGET_CLICKHOUSE.fields_by_name['db']._serialized_options = b'\350\3071\001\362\3071\016[a-zA-Z0-9_-]*\212\3101\004<=63'
  _TARGET.oneofs_by_name['mdb']._options = None
  _TARGET.oneofs_by_name['mdb']._serialized_options = b'\300\3011\001'
  _globals['_PROXY']._serialized_start=153
  _globals['_PROXY']._serialized_end=577
  _globals['_PROXY_LABELSENTRY']._serialized_start=532
  _globals['_PROXY_LABELSENTRY']._serialized_end=577
  _globals['_TARGET']._serialized_start=580
  _globals['_TARGET']._serialized_end=1106
  _globals['_TARGET_POSTGRESQL']._serialized_start=747
  _globals['_TARGET_POSTGRESQL']._serialized_end=919
  _globals['_TARGET_CLICKHOUSE']._serialized_start=922
  _globals['_TARGET_CLICKHOUSE']._serialized_end=1093
# @@protoc_insertion_point(module_scope)
