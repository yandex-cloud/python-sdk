# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/ai/foundation_models/v1/text_common.proto
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
    'yandex/cloud/ai/foundation_models/v1/text_common.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6yandex/cloud/ai/foundation_models/v1/text_common.proto\x12$yandex.cloud.ai.foundation_models.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xda\x01\n\x11\x43ompletionOptions\x12\x0e\n\x06stream\x18\x01 \x01(\x08\x12\x31\n\x0btemperature\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12/\n\nmax_tokens\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12Q\n\x11reasoning_options\x18\x04 \x01(\x0b\x32\x36.yandex.cloud.ai.foundation_models.v1.ReasoningOptions\"\xb9\x01\n\x10ReasoningOptions\x12R\n\x04mode\x18\x01 \x01(\x0e\x32\x44.yandex.cloud.ai.foundation_models.v1.ReasoningOptions.ReasoningMode\"Q\n\rReasoningMode\x12\x1e\n\x1aREASONING_MODE_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x44ISABLED\x10\x01\x12\x12\n\x0e\x45NABLED_HIDDEN\x10\x02\"\xd2\x01\n\x07Message\x12\x0c\n\x04role\x18\x01 \x01(\t\x12\x0e\n\x04text\x18\x02 \x01(\tH\x00\x12L\n\x0etool_call_list\x18\x03 \x01(\x0b\x32\x32.yandex.cloud.ai.foundation_models.v1.ToolCallListH\x00\x12P\n\x10tool_result_list\x18\x04 \x01(\x0b\x32\x34.yandex.cloud.ai.foundation_models.v1.ToolResultListH\x00\x42\t\n\x07\x43ontent\"\xfe\x01\n\x0c\x43ontentUsage\x12\x19\n\x11input_text_tokens\x18\x01 \x01(\x03\x12\x19\n\x11\x63ompletion_tokens\x18\x02 \x01(\x03\x12\x14\n\x0ctotal_tokens\x18\x03 \x01(\x03\x12m\n\x19\x63ompletion_tokens_details\x18\x04 \x01(\x0b\x32J.yandex.cloud.ai.foundation_models.v1.ContentUsage.CompletionTokensDetails\x1a\x33\n\x17\x43ompletionTokensDetails\x12\x18\n\x10reasoning_tokens\x18\x01 \x01(\x03\"\x8c\x03\n\x0b\x41lternative\x12>\n\x07message\x18\x01 \x01(\x0b\x32-.yandex.cloud.ai.foundation_models.v1.Message\x12S\n\x06status\x18\x02 \x01(\x0e\x32\x43.yandex.cloud.ai.foundation_models.v1.Alternative.AlternativeStatus\"\xe7\x01\n\x11\x41lternativeStatus\x12\"\n\x1e\x41LTERNATIVE_STATUS_UNSPECIFIED\x10\x00\x12\x1e\n\x1a\x41LTERNATIVE_STATUS_PARTIAL\x10\x01\x12&\n\"ALTERNATIVE_STATUS_TRUNCATED_FINAL\x10\x02\x12\x1c\n\x18\x41LTERNATIVE_STATUS_FINAL\x10\x03\x12%\n!ALTERNATIVE_STATUS_CONTENT_FILTER\x10\x04\x12!\n\x1d\x41LTERNATIVE_STATUS_TOOL_CALLS\x10\x05\"2\n\x05Token\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x0f\n\x07special\x18\x03 \x01(\x08\"Z\n\x04Tool\x12\x46\n\x08\x66unction\x18\x01 \x01(\x0b\x32\x32.yandex.cloud.ai.foundation_models.v1.FunctionToolH\x00\x42\n\n\x08ToolType\"n\n\x0c\x46unctionTool\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12+\n\nparameters\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0e\n\x06strict\x18\x04 \x01(\x08\"g\n\x08ToolCall\x12K\n\rfunction_call\x18\x01 \x01(\x0b\x32\x32.yandex.cloud.ai.foundation_models.v1.FunctionCallH\x00\x42\x0e\n\x0cToolCallType\"H\n\x0c\x46unctionCall\x12\x0c\n\x04name\x18\x01 \x01(\t\x12*\n\targuments\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\"R\n\x0cToolCallList\x12\x42\n\ntool_calls\x18\x01 \x03(\x0b\x32..yandex.cloud.ai.foundation_models.v1.ToolCall\"o\n\nToolResult\x12O\n\x0f\x66unction_result\x18\x01 \x01(\x0b\x32\x34.yandex.cloud.ai.foundation_models.v1.FunctionResultH\x00\x42\x10\n\x0eToolResultType\"@\n\x0e\x46unctionResult\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\x07\x63ontent\x18\x02 \x01(\tH\x00\x42\r\n\x0b\x43ontentType\"X\n\x0eToolResultList\x12\x46\n\x0ctool_results\x18\x01 \x03(\x0b\x32\x30.yandex.cloud.ai.foundation_models.v1.ToolResult\"5\n\nJsonSchema\x12\'\n\x06schema\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\"\xda\x01\n\nToolChoice\x12O\n\x04mode\x18\x01 \x01(\x0e\x32?.yandex.cloud.ai.foundation_models.v1.ToolChoice.ToolChoiceModeH\x00\x12\x17\n\rfunction_name\x18\x02 \x01(\tH\x00\"T\n\x0eToolChoiceMode\x12 \n\x1cTOOL_CHOICE_MODE_UNSPECIFIED\x10\x00\x12\x08\n\x04NONE\x10\x01\x12\x08\n\x04\x41UTO\x10\x02\x12\x0c\n\x08REQUIRED\x10\x03\x42\x0c\n\nToolChoiceB\x86\x01\n(yandex.cloud.api.ai.foundation_models.v1ZZgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/foundation_models/v1;foundation_modelsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.ai.foundation_models.v1.text_common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n(yandex.cloud.api.ai.foundation_models.v1ZZgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/foundation_models/v1;foundation_models'
  _globals['_COMPLETIONOPTIONS']._serialized_start=159
  _globals['_COMPLETIONOPTIONS']._serialized_end=377
  _globals['_REASONINGOPTIONS']._serialized_start=380
  _globals['_REASONINGOPTIONS']._serialized_end=565
  _globals['_REASONINGOPTIONS_REASONINGMODE']._serialized_start=484
  _globals['_REASONINGOPTIONS_REASONINGMODE']._serialized_end=565
  _globals['_MESSAGE']._serialized_start=568
  _globals['_MESSAGE']._serialized_end=778
  _globals['_CONTENTUSAGE']._serialized_start=781
  _globals['_CONTENTUSAGE']._serialized_end=1035
  _globals['_CONTENTUSAGE_COMPLETIONTOKENSDETAILS']._serialized_start=984
  _globals['_CONTENTUSAGE_COMPLETIONTOKENSDETAILS']._serialized_end=1035
  _globals['_ALTERNATIVE']._serialized_start=1038
  _globals['_ALTERNATIVE']._serialized_end=1434
  _globals['_ALTERNATIVE_ALTERNATIVESTATUS']._serialized_start=1203
  _globals['_ALTERNATIVE_ALTERNATIVESTATUS']._serialized_end=1434
  _globals['_TOKEN']._serialized_start=1436
  _globals['_TOKEN']._serialized_end=1486
  _globals['_TOOL']._serialized_start=1488
  _globals['_TOOL']._serialized_end=1578
  _globals['_FUNCTIONTOOL']._serialized_start=1580
  _globals['_FUNCTIONTOOL']._serialized_end=1690
  _globals['_TOOLCALL']._serialized_start=1692
  _globals['_TOOLCALL']._serialized_end=1795
  _globals['_FUNCTIONCALL']._serialized_start=1797
  _globals['_FUNCTIONCALL']._serialized_end=1869
  _globals['_TOOLCALLLIST']._serialized_start=1871
  _globals['_TOOLCALLLIST']._serialized_end=1953
  _globals['_TOOLRESULT']._serialized_start=1955
  _globals['_TOOLRESULT']._serialized_end=2066
  _globals['_FUNCTIONRESULT']._serialized_start=2068
  _globals['_FUNCTIONRESULT']._serialized_end=2132
  _globals['_TOOLRESULTLIST']._serialized_start=2134
  _globals['_TOOLRESULTLIST']._serialized_end=2222
  _globals['_JSONSCHEMA']._serialized_start=2224
  _globals['_JSONSCHEMA']._serialized_end=2277
  _globals['_TOOLCHOICE']._serialized_start=2280
  _globals['_TOOLCHOICE']._serialized_end=2498
  _globals['_TOOLCHOICE_TOOLCHOICEMODE']._serialized_start=2400
  _globals['_TOOLCHOICE_TOOLCHOICEMODE']._serialized_end=2484
# @@protoc_insertion_point(module_scope)
