# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/mysql/v1alpha/config/mysql5_7.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/mdb/mysql/v1alpha/config/mysql5_7.proto',
  package='yandex.cloud.mdb.mysql.v1alpha.config',
  syntax='proto3',
  serialized_options=_b('\n)yandex.cloud.api.mdb.mysql.v1alpha.configZOgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mysql/v1alpha/config;mysql'),
  serialized_pb=_b('\n4yandex/cloud/mdb/mysql/v1alpha/config/mysql5_7.proto\x12%yandex.cloud.mdb.mysql.v1alpha.config\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dyandex/cloud/validation.proto\"\xd8\x01\n\x0eMysqlConfig5_7\x12K\n\x17innodb_buffer_pool_size\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\r\xfa\xc7\x31\t>=5242880\x12\x42\n\x0fmax_connections\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0c\xfa\xc7\x31\x08\x31\x30-10000\x12\x35\n\x0flong_query_time\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\"\xff\x01\n\x11MysqlConfigSet5_7\x12O\n\x10\x65\x66\x66\x65\x63tive_config\x18\x01 \x01(\x0b\x32\x35.yandex.cloud.mdb.mysql.v1alpha.config.MysqlConfig5_7\x12J\n\x0buser_config\x18\x02 \x01(\x0b\x32\x35.yandex.cloud.mdb.mysql.v1alpha.config.MysqlConfig5_7\x12M\n\x0e\x64\x65\x66\x61ult_config\x18\x03 \x01(\x0b\x32\x35.yandex.cloud.mdb.mysql.v1alpha.config.MysqlConfig5_7B|\n)yandex.cloud.api.mdb.mysql.v1alpha.configZOgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mysql/v1alpha/config;mysqlb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_MYSQLCONFIG5_7 = _descriptor.Descriptor(
  name='MysqlConfig5_7',
  full_name='yandex.cloud.mdb.mysql.v1alpha.config.MysqlConfig5_7',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='innodb_buffer_pool_size', full_name='yandex.cloud.mdb.mysql.v1alpha.config.MysqlConfig5_7.innodb_buffer_pool_size', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\372\3071\t>=5242880'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_connections', full_name='yandex.cloud.mdb.mysql.v1alpha.config.MysqlConfig5_7.max_connections', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\372\3071\01010-10000'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='long_query_time', full_name='yandex.cloud.mdb.mysql.v1alpha.config.MysqlConfig5_7.long_query_time', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=159,
  serialized_end=375,
)


_MYSQLCONFIGSET5_7 = _descriptor.Descriptor(
  name='MysqlConfigSet5_7',
  full_name='yandex.cloud.mdb.mysql.v1alpha.config.MysqlConfigSet5_7',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='effective_config', full_name='yandex.cloud.mdb.mysql.v1alpha.config.MysqlConfigSet5_7.effective_config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_config', full_name='yandex.cloud.mdb.mysql.v1alpha.config.MysqlConfigSet5_7.user_config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default_config', full_name='yandex.cloud.mdb.mysql.v1alpha.config.MysqlConfigSet5_7.default_config', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=378,
  serialized_end=633,
)

_MYSQLCONFIG5_7.fields_by_name['innodb_buffer_pool_size'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_MYSQLCONFIG5_7.fields_by_name['max_connections'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_MYSQLCONFIG5_7.fields_by_name['long_query_time'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_MYSQLCONFIGSET5_7.fields_by_name['effective_config'].message_type = _MYSQLCONFIG5_7
_MYSQLCONFIGSET5_7.fields_by_name['user_config'].message_type = _MYSQLCONFIG5_7
_MYSQLCONFIGSET5_7.fields_by_name['default_config'].message_type = _MYSQLCONFIG5_7
DESCRIPTOR.message_types_by_name['MysqlConfig5_7'] = _MYSQLCONFIG5_7
DESCRIPTOR.message_types_by_name['MysqlConfigSet5_7'] = _MYSQLCONFIGSET5_7
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MysqlConfig5_7 = _reflection.GeneratedProtocolMessageType('MysqlConfig5_7', (_message.Message,), dict(
  DESCRIPTOR = _MYSQLCONFIG5_7,
  __module__ = 'yandex.cloud.mdb.mysql.v1alpha.config.mysql5_7_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mysql.v1alpha.config.MysqlConfig5_7)
  ))
_sym_db.RegisterMessage(MysqlConfig5_7)

MysqlConfigSet5_7 = _reflection.GeneratedProtocolMessageType('MysqlConfigSet5_7', (_message.Message,), dict(
  DESCRIPTOR = _MYSQLCONFIGSET5_7,
  __module__ = 'yandex.cloud.mdb.mysql.v1alpha.config.mysql5_7_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mysql.v1alpha.config.MysqlConfigSet5_7)
  ))
_sym_db.RegisterMessage(MysqlConfigSet5_7)


DESCRIPTOR._options = None
_MYSQLCONFIG5_7.fields_by_name['innodb_buffer_pool_size']._options = None
_MYSQLCONFIG5_7.fields_by_name['max_connections']._options = None
# @@protoc_insertion_point(module_scope)
