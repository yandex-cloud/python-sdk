# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/ai/assistants/v1/common.proto
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
    'yandex/cloud/ai/assistants/v1/common.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*yandex/cloud/ai/assistants/v1/common.proto\x12\x1dyandex.cloud.ai.assistants.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dyandex/cloud/validation.proto\"\xf2\x02\n\x17PromptTruncationOptions\x12\x36\n\x11max_prompt_tokens\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\\\n\rauto_strategy\x18\x02 \x01(\x0b\x32\x43.yandex.cloud.ai.assistants.v1.PromptTruncationOptions.AutoStrategyH\x00\x12m\n\x16last_messages_strategy\x18\x03 \x01(\x0b\x32K.yandex.cloud.ai.assistants.v1.PromptTruncationOptions.LastMessagesStrategyH\x00\x1a\x0e\n\x0c\x41utoStrategy\x1a,\n\x14LastMessagesStrategy\x12\x14\n\x0cnum_messages\x18\x01 \x01(\x03\x42\x14\n\x12TruncationStrategy\"w\n\x11\x43ompletionOptions\x12/\n\nmax_tokens\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x31\n\x0btemperature\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\"\x9b\x01\n\x04Tool\x12\x46\n\x0csearch_index\x18\x01 \x01(\x0b\x32..yandex.cloud.ai.assistants.v1.SearchIndexToolH\x00\x12?\n\x08\x66unction\x18\x02 \x01(\x0b\x32+.yandex.cloud.ai.assistants.v1.FunctionToolH\x00\x42\n\n\x08ToolType\"`\n\x08ToolCall\x12\x44\n\rfunction_call\x18\x01 \x01(\x0b\x32+.yandex.cloud.ai.assistants.v1.FunctionCallH\x00\x42\x0e\n\x0cToolCallType\"K\n\x0cToolCallList\x12;\n\ntool_calls\x18\x01 \x03(\x0b\x32\'.yandex.cloud.ai.assistants.v1.ToolCall\"h\n\nToolResult\x12H\n\x0f\x66unction_result\x18\x01 \x01(\x0b\x32-.yandex.cloud.ai.assistants.v1.FunctionResultH\x00\x42\x10\n\x0eToolResultType\"Q\n\x0eToolResultList\x12?\n\x0ctool_results\x18\x01 \x03(\x0b\x32).yandex.cloud.ai.assistants.v1.ToolResult\"\xad\x01\n\x0fSearchIndexTool\x12\x18\n\x10search_index_ids\x18\x01 \x03(\t\x12\x34\n\x0fmax_num_results\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12J\n\x11rephraser_options\x18\x03 \x01(\x0b\x32/.yandex.cloud.ai.assistants.v1.RephraserOptions\"^\n\x0c\x46unctionTool\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12+\n\nparameters\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\"H\n\x0c\x46unctionCall\x12\x0c\n\x04name\x18\x01 \x01(\t\x12*\n\targuments\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\"@\n\x0e\x46unctionResult\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\x07\x63ontent\x18\x02 \x01(\tH\x00\x42\r\n\x0b\x43ontentType\"/\n\x10RephraserOptions\x12\x1b\n\rrephraser_uri\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x42q\n!yandex.cloud.api.ai.assistants.v1ZLgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/assistants/v1;assistantsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.ai.assistants.v1.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!yandex.cloud.api.ai.assistants.v1ZLgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/assistants/v1;assistants'
  _globals['_REPHRASEROPTIONS'].fields_by_name['rephraser_uri']._loaded_options = None
  _globals['_REPHRASEROPTIONS'].fields_by_name['rephraser_uri']._serialized_options = b'\350\3071\001'
  _globals['_PROMPTTRUNCATIONOPTIONS']._serialized_start=171
  _globals['_PROMPTTRUNCATIONOPTIONS']._serialized_end=541
  _globals['_PROMPTTRUNCATIONOPTIONS_AUTOSTRATEGY']._serialized_start=459
  _globals['_PROMPTTRUNCATIONOPTIONS_AUTOSTRATEGY']._serialized_end=473
  _globals['_PROMPTTRUNCATIONOPTIONS_LASTMESSAGESSTRATEGY']._serialized_start=475
  _globals['_PROMPTTRUNCATIONOPTIONS_LASTMESSAGESSTRATEGY']._serialized_end=519
  _globals['_COMPLETIONOPTIONS']._serialized_start=543
  _globals['_COMPLETIONOPTIONS']._serialized_end=662
  _globals['_TOOL']._serialized_start=665
  _globals['_TOOL']._serialized_end=820
  _globals['_TOOLCALL']._serialized_start=822
  _globals['_TOOLCALL']._serialized_end=918
  _globals['_TOOLCALLLIST']._serialized_start=920
  _globals['_TOOLCALLLIST']._serialized_end=995
  _globals['_TOOLRESULT']._serialized_start=997
  _globals['_TOOLRESULT']._serialized_end=1101
  _globals['_TOOLRESULTLIST']._serialized_start=1103
  _globals['_TOOLRESULTLIST']._serialized_end=1184
  _globals['_SEARCHINDEXTOOL']._serialized_start=1187
  _globals['_SEARCHINDEXTOOL']._serialized_end=1360
  _globals['_FUNCTIONTOOL']._serialized_start=1362
  _globals['_FUNCTIONTOOL']._serialized_end=1456
  _globals['_FUNCTIONCALL']._serialized_start=1458
  _globals['_FUNCTIONCALL']._serialized_end=1530
  _globals['_FUNCTIONRESULT']._serialized_start=1532
  _globals['_FUNCTIONRESULT']._serialized_end=1596
  _globals['_REPHRASEROPTIONS']._serialized_start=1598
  _globals['_REPHRASEROPTIONS']._serialized_end=1645
# @@protoc_insertion_point(module_scope)
