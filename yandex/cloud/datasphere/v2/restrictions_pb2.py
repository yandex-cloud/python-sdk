# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/datasphere/v2/restrictions.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'yandex/cloud/datasphere/v2/restrictions.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-yandex/cloud/datasphere/v2/restrictions.proto\x12\x1ayandex.cloud.datasphere.v2\"\xd8\x01\n\x0fRestrictionMeta\x12\x0c\n\x04name\x18\x01 \x01(\t\x12T\n\nvalue_type\x18\x02 \x01(\x0e\x32@.yandex.cloud.datasphere.v2.RestrictionMeta.RestrictionValueType\"a\n\x14RestrictionValueType\x12&\n\"RESTRICTION_VALUE_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07\x42OOLEAN\x10\x01\x12\x08\n\x04LONG\x10\x02\x12\n\n\x06STRING\x10\x03\"Y\n\x0bRestriction\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nbool_value\x18\x02 \x03(\x08\x12\x12\n\nlong_value\x18\x03 \x03(\x03\x12\x14\n\x0cstring_value\x18\x04 \x03(\t\"e\n\x1bGetRestrictionsMetaResponse\x12\x46\n\x11restrictions_meta\x18\x01 \x03(\x0b\x32+.yandex.cloud.datasphere.v2.RestrictionMeta\"U\n\x14RestrictionsResponse\x12=\n\x0crestrictions\x18\x01 \x03(\x0b\x32\'.yandex.cloud.datasphere.v2.RestrictionBk\n\x1eyandex.cloud.api.datasphere.v2ZIgithub.com/yandex-cloud/go-genproto/yandex/cloud/datasphere/v2;datasphereb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.datasphere.v2.restrictions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036yandex.cloud.api.datasphere.v2ZIgithub.com/yandex-cloud/go-genproto/yandex/cloud/datasphere/v2;datasphere'
  _globals['_RESTRICTIONMETA']._serialized_start=78
  _globals['_RESTRICTIONMETA']._serialized_end=294
  _globals['_RESTRICTIONMETA_RESTRICTIONVALUETYPE']._serialized_start=197
  _globals['_RESTRICTIONMETA_RESTRICTIONVALUETYPE']._serialized_end=294
  _globals['_RESTRICTION']._serialized_start=296
  _globals['_RESTRICTION']._serialized_end=385
  _globals['_GETRESTRICTIONSMETARESPONSE']._serialized_start=387
  _globals['_GETRESTRICTIONSMETARESPONSE']._serialized_end=488
  _globals['_RESTRICTIONSRESPONSE']._serialized_start=490
  _globals['_RESTRICTIONSRESPONSE']._serialized_end=575
# @@protoc_insertion_point(module_scope)
