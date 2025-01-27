# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/ai/assistants/v1/searchindex/search_index.proto
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
    'yandex/cloud/ai/assistants/v1/searchindex/search_index.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.ai.common import common_pb2 as yandex_dot_cloud_dot_ai_dot_common_dot_common__pb2
from yandex.cloud.ai.assistants.v1.searchindex import common_pb2 as yandex_dot_cloud_dot_ai_dot_assistants_dot_v1_dot_searchindex_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<yandex/cloud/ai/assistants/v1/searchindex/search_index.proto\x12)yandex.cloud.ai.assistants.v1.searchindex\x1a#yandex/cloud/ai/common/common.proto\x1a\x36yandex/cloud/ai/assistants/v1/searchindex/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xef\x05\n\x0bSearchIndex\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x12\n\ncreated_by\x18\x05 \x01(\t\x12.\n\ncreated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nupdated_by\x18\x07 \x01(\t\x12.\n\nupdated_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x43\n\x11\x65xpiration_config\x18\t \x01(\x0b\x32(.yandex.cloud.ai.common.ExpirationConfig\x12.\n\nexpires_at\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12R\n\x06labels\x18\x0b \x03(\x0b\x32\x42.yandex.cloud.ai.assistants.v1.searchindex.SearchIndex.LabelsEntry\x12W\n\x11text_search_index\x18\x0c \x01(\x0b\x32:.yandex.cloud.ai.assistants.v1.searchindex.TextSearchIndexH\x00\x12[\n\x13vector_search_index\x18\r \x01(\x0b\x32<.yandex.cloud.ai.assistants.v1.searchindex.VectorSearchIndexH\x00\x12[\n\x13hybrid_search_index\x18\x0e \x01(\x0b\x32<.yandex.cloud.ai.assistants.v1.searchindex.HybridSearchIndexH\x00\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x0b\n\tIndexType\"\xd0\x01\n\x0fTextSearchIndex\x12V\n\x11\x63hunking_strategy\x18\x01 \x01(\x0b\x32;.yandex.cloud.ai.assistants.v1.searchindex.ChunkingStrategy\x12T\n\x0fngram_tokenizer\x18\x02 \x01(\x0b\x32\x39.yandex.cloud.ai.assistants.v1.searchindex.NgramTokenizerH\x00\x42\x0f\n\rTextTokenizer\"\xa1\x01\n\x11VectorSearchIndex\x12\x18\n\x10\x64oc_embedder_uri\x18\x01 \x01(\t\x12\x1a\n\x12query_embedder_uri\x18\x02 \x01(\t\x12V\n\x11\x63hunking_strategy\x18\x03 \x01(\x0b\x32;.yandex.cloud.ai.assistants.v1.searchindex.ChunkingStrategy\"\xdd\x03\n\x11HybridSearchIndex\x12U\n\x11text_search_index\x18\x01 \x01(\x0b\x32:.yandex.cloud.ai.assistants.v1.searchindex.TextSearchIndex\x12Y\n\x13vector_search_index\x18\x02 \x01(\x0b\x32<.yandex.cloud.ai.assistants.v1.searchindex.VectorSearchIndex\x12V\n\x11\x63hunking_strategy\x18\x03 \x01(\x0b\x32;.yandex.cloud.ai.assistants.v1.searchindex.ChunkingStrategy\x12`\n\x16normalization_strategy\x18\x04 \x01(\x0e\x32@.yandex.cloud.ai.assistants.v1.searchindex.NormalizationStrategy\x12\\\n\x14\x63ombination_strategy\x18\x05 \x01(\x0b\x32>.yandex.cloud.ai.assistants.v1.searchindex.CombinationStrategyB\x8a\x01\n-yandex.cloud.api.ai.assistants.v1.searchindexZYgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/assistants/v1/searchindex;searchindexb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.ai.assistants.v1.searchindex.search_index_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n-yandex.cloud.api.ai.assistants.v1.searchindexZYgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/assistants/v1/searchindex;searchindex'
  _globals['_SEARCHINDEX_LABELSENTRY']._loaded_options = None
  _globals['_SEARCHINDEX_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_SEARCHINDEX']._serialized_start=234
  _globals['_SEARCHINDEX']._serialized_end=985
  _globals['_SEARCHINDEX_LABELSENTRY']._serialized_start=927
  _globals['_SEARCHINDEX_LABELSENTRY']._serialized_end=972
  _globals['_TEXTSEARCHINDEX']._serialized_start=988
  _globals['_TEXTSEARCHINDEX']._serialized_end=1196
  _globals['_VECTORSEARCHINDEX']._serialized_start=1199
  _globals['_VECTORSEARCHINDEX']._serialized_end=1360
  _globals['_HYBRIDSEARCHINDEX']._serialized_start=1363
  _globals['_HYBRIDSEARCHINDEX']._serialized_end=1840
# @@protoc_insertion_point(module_scope)
