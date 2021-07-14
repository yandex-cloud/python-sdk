# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/elasticsearch/v1/config/elasticsearch.proto
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
  name='yandex/cloud/mdb/elasticsearch/v1/config/elasticsearch.proto',
  package='yandex.cloud.mdb.elasticsearch.v1.config',
  syntax='proto3',
  serialized_options=b'\n,yandex.cloud.api.mdb.elasticsearch.v1.configZZgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/elasticsearch/v1/config;elasticsearch',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n<yandex/cloud/mdb/elasticsearch/v1/config/elasticsearch.proto\x12(yandex.cloud.mdb.elasticsearch.v1.config\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dyandex/cloud/validation.proto\"k\n\x14\x45lasticsearchConfig7\x12\x35\n\x10max_clause_count\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x1c\n\x14\x66ielddata_cache_size\x18\x04 \x01(\t\"\xa6\x02\n\x17\x45lasticsearchConfigSet7\x12^\n\x10\x65\x66\x66\x65\x63tive_config\x18\x01 \x01(\x0b\x32>.yandex.cloud.mdb.elasticsearch.v1.config.ElasticsearchConfig7B\x04\xe8\xc7\x31\x01\x12S\n\x0buser_config\x18\x02 \x01(\x0b\x32>.yandex.cloud.mdb.elasticsearch.v1.config.ElasticsearchConfig7\x12V\n\x0e\x64\x65\x66\x61ult_config\x18\x03 \x01(\x0b\x32>.yandex.cloud.mdb.elasticsearch.v1.config.ElasticsearchConfig7B\x8a\x01\n,yandex.cloud.api.mdb.elasticsearch.v1.configZZgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/elasticsearch/v1/config;elasticsearchb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_ELASTICSEARCHCONFIG7 = _descriptor.Descriptor(
  name='ElasticsearchConfig7',
  full_name='yandex.cloud.mdb.elasticsearch.v1.config.ElasticsearchConfig7',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_clause_count', full_name='yandex.cloud.mdb.elasticsearch.v1.config.ElasticsearchConfig7.max_clause_count', index=0,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fielddata_cache_size', full_name='yandex.cloud.mdb.elasticsearch.v1.config.ElasticsearchConfig7.fielddata_cache_size', index=1,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=169,
  serialized_end=276,
)


_ELASTICSEARCHCONFIGSET7 = _descriptor.Descriptor(
  name='ElasticsearchConfigSet7',
  full_name='yandex.cloud.mdb.elasticsearch.v1.config.ElasticsearchConfigSet7',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='effective_config', full_name='yandex.cloud.mdb.elasticsearch.v1.config.ElasticsearchConfigSet7.effective_config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_config', full_name='yandex.cloud.mdb.elasticsearch.v1.config.ElasticsearchConfigSet7.user_config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='default_config', full_name='yandex.cloud.mdb.elasticsearch.v1.config.ElasticsearchConfigSet7.default_config', index=2,
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
  serialized_start=279,
  serialized_end=573,
)

_ELASTICSEARCHCONFIG7.fields_by_name['max_clause_count'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_ELASTICSEARCHCONFIGSET7.fields_by_name['effective_config'].message_type = _ELASTICSEARCHCONFIG7
_ELASTICSEARCHCONFIGSET7.fields_by_name['user_config'].message_type = _ELASTICSEARCHCONFIG7
_ELASTICSEARCHCONFIGSET7.fields_by_name['default_config'].message_type = _ELASTICSEARCHCONFIG7
DESCRIPTOR.message_types_by_name['ElasticsearchConfig7'] = _ELASTICSEARCHCONFIG7
DESCRIPTOR.message_types_by_name['ElasticsearchConfigSet7'] = _ELASTICSEARCHCONFIGSET7
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ElasticsearchConfig7 = _reflection.GeneratedProtocolMessageType('ElasticsearchConfig7', (_message.Message,), {
  'DESCRIPTOR' : _ELASTICSEARCHCONFIG7,
  '__module__' : 'yandex.cloud.mdb.elasticsearch.v1.config.elasticsearch_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.elasticsearch.v1.config.ElasticsearchConfig7)
  })
_sym_db.RegisterMessage(ElasticsearchConfig7)

ElasticsearchConfigSet7 = _reflection.GeneratedProtocolMessageType('ElasticsearchConfigSet7', (_message.Message,), {
  'DESCRIPTOR' : _ELASTICSEARCHCONFIGSET7,
  '__module__' : 'yandex.cloud.mdb.elasticsearch.v1.config.elasticsearch_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.elasticsearch.v1.config.ElasticsearchConfigSet7)
  })
_sym_db.RegisterMessage(ElasticsearchConfigSet7)


DESCRIPTOR._options = None
_ELASTICSEARCHCONFIGSET7.fields_by_name['effective_config']._options = None
# @@protoc_insertion_point(module_scope)