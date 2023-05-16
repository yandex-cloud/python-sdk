# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/redis/v1/config/redis6_2.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/mdb/redis/v1/config/redis6_2.proto',
  package='yandex.cloud.mdb.redis.v1.config',
  syntax='proto3',
  serialized_options=b'\n$yandex.cloud.api.mdb.redis.v1.configZJgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/redis/v1/config;redis',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n/yandex/cloud/mdb/redis/v1/config/redis6_2.proto\x12 yandex.cloud.mdb.redis.v1.config\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dyandex/cloud/validation.proto\"\x8c\t\n\x0eRedisConfig6_2\x12Z\n\x10maxmemory_policy\x18\x01 \x01(\x0e\x32@.yandex.cloud.mdb.redis.v1.config.RedisConfig6_2.MaxmemoryPolicy\x12,\n\x07timeout\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x38\n\x08password\x18\x03 \x01(\tB&\xf2\xc7\x31\"[a-zA-Z0-9@=+?*.,!&#$^<>_-]{8,128}\x12\x36\n\tdatabases\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x06\xfa\xc7\x31\x02>0\x12\x45\n\x17slowlog_log_slower_than\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12=\n\x0fslowlog_max_len\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12\x39\n\x16notify_keyspace_events\x18\x07 \x01(\tB\x19\xf2\xc7\x31\x15[KEg$lshzxeAtm]{0,13}\x12s\n!client_output_buffer_limit_pubsub\x18\x08 \x01(\x0b\x32H.yandex.cloud.mdb.redis.v1.config.RedisConfig6_2.ClientOutputBufferLimit\x12s\n!client_output_buffer_limit_normal\x18\t \x01(\x0b\x32H.yandex.cloud.mdb.redis.v1.config.RedisConfig6_2.ClientOutputBufferLimit\x12@\n\x11maxmemory_percent\x18\n \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x08\xfa\xc7\x31\x04\x31-75\x1a\xc9\x01\n\x17\x43lientOutputBufferLimit\x12\x38\n\nhard_limit\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12\x38\n\nsoft_limit\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12:\n\x0csoft_seconds\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\"\xc4\x01\n\x0fMaxmemoryPolicy\x12 \n\x1cMAXMEMORY_POLICY_UNSPECIFIED\x10\x00\x12\x10\n\x0cVOLATILE_LRU\x10\x01\x12\x0f\n\x0b\x41LLKEYS_LRU\x10\x02\x12\x10\n\x0cVOLATILE_LFU\x10\x03\x12\x0f\n\x0b\x41LLKEYS_LFU\x10\x04\x12\x13\n\x0fVOLATILE_RANDOM\x10\x05\x12\x12\n\x0e\x41LLKEYS_RANDOM\x10\x06\x12\x10\n\x0cVOLATILE_TTL\x10\x07\x12\x0e\n\nNOEVICTION\x10\x08\"\xf0\x01\n\x11RedisConfigSet6_2\x12J\n\x10\x65\x66\x66\x65\x63tive_config\x18\x01 \x01(\x0b\x32\x30.yandex.cloud.mdb.redis.v1.config.RedisConfig6_2\x12\x45\n\x0buser_config\x18\x02 \x01(\x0b\x32\x30.yandex.cloud.mdb.redis.v1.config.RedisConfig6_2\x12H\n\x0e\x64\x65\x66\x61ult_config\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.mdb.redis.v1.config.RedisConfig6_2Br\n$yandex.cloud.api.mdb.redis.v1.configZJgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/redis/v1/config;redisb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])



_REDISCONFIG6_2_MAXMEMORYPOLICY = _descriptor.EnumDescriptor(
  name='MaxmemoryPolicy',
  full_name='yandex.cloud.mdb.redis.v1.config.RedisConfig6_2.MaxmemoryPolicy',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MAXMEMORY_POLICY_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VOLATILE_LRU', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALLKEYS_LRU', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VOLATILE_LFU', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALLKEYS_LFU', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VOLATILE_RANDOM', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALLKEYS_RANDOM', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VOLATILE_TTL', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NOEVICTION', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1117,
  serialized_end=1313,
)
_sym_db.RegisterEnumDescriptor(_REDISCONFIG6_2_MAXMEMORYPOLICY)


_REDISCONFIG6_2_CLIENTOUTPUTBUFFERLIMIT = _descriptor.Descriptor(
  name='ClientOutputBufferLimit',
  full_name='yandex.cloud.mdb.redis.v1.config.RedisConfig6_2.ClientOutputBufferLimit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hard_limit', full_name='yandex.cloud.mdb.redis.v1.config.RedisConfig6_2.ClientOutputBufferLimit.hard_limit', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\003>=0', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='soft_limit', full_name='yandex.cloud.mdb.redis.v1.config.RedisConfig6_2.ClientOutputBufferLimit.soft_limit', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\003>=0', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='soft_seconds', full_name='yandex.cloud.mdb.redis.v1.config.RedisConfig6_2.ClientOutputBufferLimit.soft_seconds', index=2,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\003>=0', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=913,
  serialized_end=1114,
)

_REDISCONFIG6_2 = _descriptor.Descriptor(
  name='RedisConfig6_2',
  full_name='yandex.cloud.mdb.redis.v1.config.RedisConfig6_2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='maxmemory_policy', full_name='yandex.cloud.mdb.redis.v1.config.RedisConfig6_2.maxmemory_policy', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='yandex.cloud.mdb.redis.v1.config.RedisConfig6_2.timeout', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='yandex.cloud.mdb.redis.v1.config.RedisConfig6_2.password', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\3071\"[a-zA-Z0-9@=+?*.,!&#$^<>_-]{8,128}', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='databases', full_name='yandex.cloud.mdb.redis.v1.config.RedisConfig6_2.databases', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\002>0', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='slowlog_log_slower_than', full_name='yandex.cloud.mdb.redis.v1.config.RedisConfig6_2.slowlog_log_slower_than', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\003>=0', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='slowlog_max_len', full_name='yandex.cloud.mdb.redis.v1.config.RedisConfig6_2.slowlog_max_len', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\003>=0', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='notify_keyspace_events', full_name='yandex.cloud.mdb.redis.v1.config.RedisConfig6_2.notify_keyspace_events', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\3071\025[KEg$lshzxeAtm]{0,13}', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='client_output_buffer_limit_pubsub', full_name='yandex.cloud.mdb.redis.v1.config.RedisConfig6_2.client_output_buffer_limit_pubsub', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='client_output_buffer_limit_normal', full_name='yandex.cloud.mdb.redis.v1.config.RedisConfig6_2.client_output_buffer_limit_normal', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='maxmemory_percent', full_name='yandex.cloud.mdb.redis.v1.config.RedisConfig6_2.maxmemory_percent', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\0041-75', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_REDISCONFIG6_2_CLIENTOUTPUTBUFFERLIMIT, ],
  enum_types=[
    _REDISCONFIG6_2_MAXMEMORYPOLICY,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=149,
  serialized_end=1313,
)


_REDISCONFIGSET6_2 = _descriptor.Descriptor(
  name='RedisConfigSet6_2',
  full_name='yandex.cloud.mdb.redis.v1.config.RedisConfigSet6_2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='effective_config', full_name='yandex.cloud.mdb.redis.v1.config.RedisConfigSet6_2.effective_config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_config', full_name='yandex.cloud.mdb.redis.v1.config.RedisConfigSet6_2.user_config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='default_config', full_name='yandex.cloud.mdb.redis.v1.config.RedisConfigSet6_2.default_config', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1316,
  serialized_end=1556,
)

_REDISCONFIG6_2_CLIENTOUTPUTBUFFERLIMIT.fields_by_name['hard_limit'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_REDISCONFIG6_2_CLIENTOUTPUTBUFFERLIMIT.fields_by_name['soft_limit'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_REDISCONFIG6_2_CLIENTOUTPUTBUFFERLIMIT.fields_by_name['soft_seconds'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_REDISCONFIG6_2_CLIENTOUTPUTBUFFERLIMIT.containing_type = _REDISCONFIG6_2
_REDISCONFIG6_2.fields_by_name['maxmemory_policy'].enum_type = _REDISCONFIG6_2_MAXMEMORYPOLICY
_REDISCONFIG6_2.fields_by_name['timeout'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_REDISCONFIG6_2.fields_by_name['databases'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_REDISCONFIG6_2.fields_by_name['slowlog_log_slower_than'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_REDISCONFIG6_2.fields_by_name['slowlog_max_len'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_REDISCONFIG6_2.fields_by_name['client_output_buffer_limit_pubsub'].message_type = _REDISCONFIG6_2_CLIENTOUTPUTBUFFERLIMIT
_REDISCONFIG6_2.fields_by_name['client_output_buffer_limit_normal'].message_type = _REDISCONFIG6_2_CLIENTOUTPUTBUFFERLIMIT
_REDISCONFIG6_2.fields_by_name['maxmemory_percent'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_REDISCONFIG6_2_MAXMEMORYPOLICY.containing_type = _REDISCONFIG6_2
_REDISCONFIGSET6_2.fields_by_name['effective_config'].message_type = _REDISCONFIG6_2
_REDISCONFIGSET6_2.fields_by_name['user_config'].message_type = _REDISCONFIG6_2
_REDISCONFIGSET6_2.fields_by_name['default_config'].message_type = _REDISCONFIG6_2
DESCRIPTOR.message_types_by_name['RedisConfig6_2'] = _REDISCONFIG6_2
DESCRIPTOR.message_types_by_name['RedisConfigSet6_2'] = _REDISCONFIGSET6_2
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RedisConfig6_2 = _reflection.GeneratedProtocolMessageType('RedisConfig6_2', (_message.Message,), {

  'ClientOutputBufferLimit' : _reflection.GeneratedProtocolMessageType('ClientOutputBufferLimit', (_message.Message,), {
    'DESCRIPTOR' : _REDISCONFIG6_2_CLIENTOUTPUTBUFFERLIMIT,
    '__module__' : 'yandex.cloud.mdb.redis.v1.config.redis6_2_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.redis.v1.config.RedisConfig6_2.ClientOutputBufferLimit)
    })
  ,
  'DESCRIPTOR' : _REDISCONFIG6_2,
  '__module__' : 'yandex.cloud.mdb.redis.v1.config.redis6_2_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.redis.v1.config.RedisConfig6_2)
  })
_sym_db.RegisterMessage(RedisConfig6_2)
_sym_db.RegisterMessage(RedisConfig6_2.ClientOutputBufferLimit)

RedisConfigSet6_2 = _reflection.GeneratedProtocolMessageType('RedisConfigSet6_2', (_message.Message,), {
  'DESCRIPTOR' : _REDISCONFIGSET6_2,
  '__module__' : 'yandex.cloud.mdb.redis.v1.config.redis6_2_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.redis.v1.config.RedisConfigSet6_2)
  })
_sym_db.RegisterMessage(RedisConfigSet6_2)


DESCRIPTOR._options = None
_REDISCONFIG6_2_CLIENTOUTPUTBUFFERLIMIT.fields_by_name['hard_limit']._options = None
_REDISCONFIG6_2_CLIENTOUTPUTBUFFERLIMIT.fields_by_name['soft_limit']._options = None
_REDISCONFIG6_2_CLIENTOUTPUTBUFFERLIMIT.fields_by_name['soft_seconds']._options = None
_REDISCONFIG6_2.fields_by_name['password']._options = None
_REDISCONFIG6_2.fields_by_name['databases']._options = None
_REDISCONFIG6_2.fields_by_name['slowlog_log_slower_than']._options = None
_REDISCONFIG6_2.fields_by_name['slowlog_max_len']._options = None
_REDISCONFIG6_2.fields_by_name['notify_keyspace_events']._options = None
_REDISCONFIG6_2.fields_by_name['maxmemory_percent']._options = None
# @@protoc_insertion_point(module_scope)
