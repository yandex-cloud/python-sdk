# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/searchapi/v2/search_query.proto
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
    'yandex/cloud/searchapi/v2/search_query.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,yandex/cloud/searchapi/v2/search_query.proto\x12\x19yandex.cloud.searchapi.v2\x1a\x1dyandex/cloud/validation.proto\"\x87\x05\n\x0bSearchQuery\x12L\n\x0bsearch_type\x18\x01 \x01(\x0e\x32\x31.yandex.cloud.searchapi.v2.SearchQuery.SearchTypeB\x04\xe8\xc7\x31\x01\x12!\n\nquery_text\x18\x02 \x01(\tB\r\xe8\xc7\x31\x01\x8a\xc8\x31\x05<=400\x12\x46\n\x0b\x66\x61mily_mode\x18\x03 \x01(\x0e\x32\x31.yandex.cloud.searchapi.v2.SearchQuery.FamilyMode\x12\x15\n\x04page\x18\x04 \x01(\x03\x42\x07\xfa\xc7\x31\x03>=0\x12I\n\rfix_typo_mode\x18\x05 \x01(\x0e\x32\x32.yandex.cloud.searchapi.v2.SearchQuery.FixTypoMode\"\x8e\x01\n\nSearchType\x12\x1b\n\x17SEARCH_TYPE_UNSPECIFIED\x10\x00\x12\x12\n\x0eSEARCH_TYPE_RU\x10\x01\x12\x12\n\x0eSEARCH_TYPE_TR\x10\x02\x12\x13\n\x0fSEARCH_TYPE_COM\x10\x03\x12\x12\n\x0eSEARCH_TYPE_KK\x10\x04\x12\x12\n\x0eSEARCH_TYPE_BE\x10\x05\"q\n\nFamilyMode\x12\x1b\n\x17\x46\x41MILY_MODE_UNSPECIFIED\x10\x00\x12\x14\n\x10\x46\x41MILY_MODE_NONE\x10\x01\x12\x18\n\x14\x46\x41MILY_MODE_MODERATE\x10\x02\x12\x16\n\x12\x46\x41MILY_MODE_STRICT\x10\x03\"Y\n\x0b\x46ixTypoMode\x12\x1d\n\x19\x46IX_TYPO_MODE_UNSPECIFIED\x10\x00\x12\x14\n\x10\x46IX_TYPO_MODE_ON\x10\x01\x12\x15\n\x11\x46IX_TYPO_MODE_OFF\x10\x02\x42\x65\n\x1ayandex.cloud.api.search.v2ZGgithub.com/yandex-cloud/go-genproto/yandex/cloud/searchapi/v2;searchapib\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.searchapi.v2.search_query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032yandex.cloud.api.search.v2ZGgithub.com/yandex-cloud/go-genproto/yandex/cloud/searchapi/v2;searchapi'
  _globals['_SEARCHQUERY'].fields_by_name['search_type']._loaded_options = None
  _globals['_SEARCHQUERY'].fields_by_name['search_type']._serialized_options = b'\350\3071\001'
  _globals['_SEARCHQUERY'].fields_by_name['query_text']._loaded_options = None
  _globals['_SEARCHQUERY'].fields_by_name['query_text']._serialized_options = b'\350\3071\001\212\3101\005<=400'
  _globals['_SEARCHQUERY'].fields_by_name['page']._loaded_options = None
  _globals['_SEARCHQUERY'].fields_by_name['page']._serialized_options = b'\372\3071\003>=0'
  _globals['_SEARCHQUERY']._serialized_start=107
  _globals['_SEARCHQUERY']._serialized_end=754
  _globals['_SEARCHQUERY_SEARCHTYPE']._serialized_start=406
  _globals['_SEARCHQUERY_SEARCHTYPE']._serialized_end=548
  _globals['_SEARCHQUERY_FAMILYMODE']._serialized_start=550
  _globals['_SEARCHQUERY_FAMILYMODE']._serialized_end=663
  _globals['_SEARCHQUERY_FIXTYPOMODE']._serialized_start=665
  _globals['_SEARCHQUERY_FIXTYPOMODE']._serialized_end=754
# @@protoc_insertion_point(module_scope)
