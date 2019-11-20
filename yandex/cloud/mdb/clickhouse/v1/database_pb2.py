# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/clickhouse/v1/database.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/mdb/clickhouse/v1/database.proto',
  package='yandex.cloud.mdb.clickhouse.v1',
  syntax='proto3',
  serialized_options=_b('\n\"yandex.cloud.api.mdb.clickhouse.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/clickhouse/v1;clickhouse'),
  serialized_pb=_b('\n-yandex/cloud/mdb/clickhouse/v1/database.proto\x12\x1eyandex.cloud.mdb.clickhouse.v1\x1a\x1dyandex/cloud/validation.proto\",\n\x08\x44\x61tabase\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ncluster_id\x18\x02 \x01(\t\"<\n\x0c\x44\x61tabaseSpec\x12,\n\x04name\x18\x01 \x01(\tB\x1e\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=63\xf2\xc7\x31\x0e[a-zA-Z0-9_-]*Bs\n\"yandex.cloud.api.mdb.clickhouse.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/clickhouse/v1;clickhouseb\x06proto3')
  ,
  dependencies=[yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_DATABASE = _descriptor.Descriptor(
  name='Database',
  full_name='yandex.cloud.mdb.clickhouse.v1.Database',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.mdb.clickhouse.v1.Database.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.clickhouse.v1.Database.cluster_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=156,
)


_DATABASESPEC = _descriptor.Descriptor(
  name='DatabaseSpec',
  full_name='yandex.cloud.mdb.clickhouse.v1.DatabaseSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.mdb.clickhouse.v1.DatabaseSpec.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001\212\3101\004<=63\362\3071\016[a-zA-Z0-9_-]*'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=158,
  serialized_end=218,
)

DESCRIPTOR.message_types_by_name['Database'] = _DATABASE
DESCRIPTOR.message_types_by_name['DatabaseSpec'] = _DATABASESPEC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Database = _reflection.GeneratedProtocolMessageType('Database', (_message.Message,), dict(
  DESCRIPTOR = _DATABASE,
  __module__ = 'yandex.cloud.mdb.clickhouse.v1.database_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.clickhouse.v1.Database)
  ))
_sym_db.RegisterMessage(Database)

DatabaseSpec = _reflection.GeneratedProtocolMessageType('DatabaseSpec', (_message.Message,), dict(
  DESCRIPTOR = _DATABASESPEC,
  __module__ = 'yandex.cloud.mdb.clickhouse.v1.database_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.clickhouse.v1.DatabaseSpec)
  ))
_sym_db.RegisterMessage(DatabaseSpec)


DESCRIPTOR._options = None
_DATABASESPEC.fields_by_name['name']._options = None
# @@protoc_insertion_point(module_scope)
