# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/ai/foundation_models/v1/foundation_models.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<yandex/cloud/ai/foundation_models/v1/foundation_models.proto\x12$yandex.cloud.ai.foundation_models.v1\x1a\x1egoogle/protobuf/wrappers.proto\"\x87\x01\n\x11\x43ompletionOptions\x12\x0e\n\x06stream\x18\x01 \x01(\x08\x12\x31\n\x0btemperature\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12/\n\nmax_tokens\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\"2\n\x07Message\x12\x0c\n\x04role\x18\x01 \x01(\t\x12\x0e\n\x04text\x18\x02 \x01(\tH\x00\x42\t\n\x07\x43ontent\"Z\n\x0c\x43ontentUsage\x12\x19\n\x11input_text_tokens\x18\x01 \x01(\x03\x12\x19\n\x11\x63ompletion_tokens\x18\x02 \x01(\x03\x12\x14\n\x0ctotal_tokens\x18\x03 \x01(\x03\"\xc2\x02\n\x0b\x41lternative\x12>\n\x07message\x18\x01 \x01(\x0b\x32-.yandex.cloud.ai.foundation_models.v1.Message\x12S\n\x06status\x18\x02 \x01(\x0e\x32\x43.yandex.cloud.ai.foundation_models.v1.Alternative.AlternativeStatus\"\x9d\x01\n\x11\x41lternativeStatus\x12\"\n\x1e\x41LTERNATIVE_STATUS_UNSPECIFIED\x10\x00\x12\x1e\n\x1a\x41LTERNATIVE_STATUS_PARTIAL\x10\x01\x12&\n\"ALTERNATIVE_STATUS_TRUNCATED_FINAL\x10\x02\x12\x1c\n\x18\x41LTERNATIVE_STATUS_FINAL\x10\x03\"2\n\x05Token\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x0f\n\x07special\x18\x03 \x01(\x08\x42\x86\x01\n(yandex.cloud.api.ai.foundation_models.v1ZZgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/foundation_models/v1;foundation_modelsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.ai.foundation_models.v1.foundation_models_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n(yandex.cloud.api.ai.foundation_models.v1ZZgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/foundation_models/v1;foundation_models'
  _globals['_COMPLETIONOPTIONS']._serialized_start=135
  _globals['_COMPLETIONOPTIONS']._serialized_end=270
  _globals['_MESSAGE']._serialized_start=272
  _globals['_MESSAGE']._serialized_end=322
  _globals['_CONTENTUSAGE']._serialized_start=324
  _globals['_CONTENTUSAGE']._serialized_end=414
  _globals['_ALTERNATIVE']._serialized_start=417
  _globals['_ALTERNATIVE']._serialized_end=739
  _globals['_ALTERNATIVE_ALTERNATIVESTATUS']._serialized_start=582
  _globals['_ALTERNATIVE_ALTERNATIVESTATUS']._serialized_end=739
  _globals['_TOKEN']._serialized_start=741
  _globals['_TOKEN']._serialized_end=791
# @@protoc_insertion_point(module_scope)
