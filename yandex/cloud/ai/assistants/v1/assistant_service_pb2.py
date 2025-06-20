# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/ai/assistants/v1/assistant_service.proto
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
    'yandex/cloud/ai/assistants/v1/assistant_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.ai.common import common_pb2 as yandex_dot_cloud_dot_ai_dot_common_dot_common__pb2
from yandex.cloud.ai.assistants.v1 import assistant_pb2 as yandex_dot_cloud_dot_ai_dot_assistants_dot_v1_dot_assistant__pb2
from yandex.cloud.ai.assistants.v1 import common_pb2 as yandex_dot_cloud_dot_ai_dot_assistants_dot_v1_dot_common__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5yandex/cloud/ai/assistants/v1/assistant_service.proto\x12\x1dyandex.cloud.ai.assistants.v1\x1a#yandex/cloud/ai/common/common.proto\x1a-yandex/cloud/ai/assistants/v1/assistant.proto\x1a*yandex/cloud/ai/assistants/v1/common.proto\x1a\x1dyandex/cloud/validation.proto\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\"\xee\x04\n\x16\x43reateAssistantRequest\x12\x17\n\tfolder_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x43\n\x11\x65xpiration_config\x18\x04 \x01(\x0b\x32(.yandex.cloud.ai.common.ExpirationConfig\x12Q\n\x06labels\x18\x05 \x03(\x0b\x32\x41.yandex.cloud.ai.assistants.v1.CreateAssistantRequest.LabelsEntry\x12\x17\n\tmodel_uri\x18\x06 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x13\n\x0binstruction\x18\x07 \x01(\t\x12Y\n\x19prompt_truncation_options\x18\x08 \x01(\x0b\x32\x36.yandex.cloud.ai.assistants.v1.PromptTruncationOptions\x12L\n\x12\x63ompletion_options\x18\t \x01(\x0b\x32\x30.yandex.cloud.ai.assistants.v1.CompletionOptions\x12\x32\n\x05tools\x18\n \x03(\x0b\x32#.yandex.cloud.ai.assistants.v1.Tool\x12\x46\n\x0fresponse_format\x18\x0b \x01(\x0b\x32-.yandex.cloud.ai.assistants.v1.ResponseFormat\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"1\n\x13GetAssistantRequest\x12\x1a\n\x0c\x61ssistant_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"\xa2\x05\n\x16UpdateAssistantRequest\x12\x1a\n\x0c\x61ssistant_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x35\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x04\xe8\xc7\x31\x01\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x43\n\x11\x65xpiration_config\x18\x05 \x01(\x0b\x32(.yandex.cloud.ai.common.ExpirationConfig\x12Q\n\x06labels\x18\x06 \x03(\x0b\x32\x41.yandex.cloud.ai.assistants.v1.UpdateAssistantRequest.LabelsEntry\x12\x11\n\tmodel_uri\x18\x07 \x01(\t\x12\x13\n\x0binstruction\x18\x08 \x01(\t\x12Y\n\x19prompt_truncation_options\x18\t \x01(\x0b\x32\x36.yandex.cloud.ai.assistants.v1.PromptTruncationOptions\x12L\n\x12\x63ompletion_options\x18\n \x01(\x0b\x32\x30.yandex.cloud.ai.assistants.v1.CompletionOptions\x12\x32\n\x05tools\x18\x0b \x03(\x0b\x32#.yandex.cloud.ai.assistants.v1.Tool\x12\x46\n\x0fresponse_format\x18\x0c \x01(\x0b\x32-.yandex.cloud.ai.assistants.v1.ResponseFormat\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"4\n\x16\x44\x65leteAssistantRequest\x12\x1a\n\x0c\x61ssistant_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"\x19\n\x17\x44\x65leteAssistantResponse\"W\n\x15ListAssistantsRequest\x12\x17\n\tfolder_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x11\n\tpage_size\x18\x02 \x01(\x03\x12\x12\n\npage_token\x18\x03 \x01(\t\"o\n\x16ListAssistantsResponse\x12<\n\nassistants\x18\x01 \x03(\x0b\x32(.yandex.cloud.ai.assistants.v1.Assistant\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"a\n\x1cListAssistantVersionsRequest\x12\x1a\n\x0c\x61ssistant_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x11\n\tpage_size\x18\x02 \x01(\x03\x12\x12\n\npage_token\x18\x03 \x01(\t\"\x8c\x01\n\x10\x41ssistantVersion\x12\n\n\x02id\x18\x01 \x01(\t\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12;\n\tassistant\x18\x03 \x01(\x0b\x32(.yandex.cloud.ai.assistants.v1.Assistant\"{\n\x1dListAssistantVersionsResponse\x12\x41\n\x08versions\x18\x01 \x03(\x0b\x32/.yandex.cloud.ai.assistants.v1.AssistantVersion\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xde\x07\n\x10\x41ssistantService\x12\x8f\x01\n\x06\x43reate\x12\x35.yandex.cloud.ai.assistants.v1.CreateAssistantRequest\x1a(.yandex.cloud.ai.assistants.v1.Assistant\"$\x82\xd3\xe4\x93\x02\x1e\"\x19/assistants/v1/assistants:\x01*\x12\x95\x01\n\x03Get\x12\x32.yandex.cloud.ai.assistants.v1.GetAssistantRequest\x1a(.yandex.cloud.ai.assistants.v1.Assistant\"0\x82\xd3\xe4\x93\x02*\x12(/assistants/v1/assistants/{assistant_id}\x12\x9e\x01\n\x06Update\x12\x35.yandex.cloud.ai.assistants.v1.UpdateAssistantRequest\x1a(.yandex.cloud.ai.assistants.v1.Assistant\"3\x82\xd3\xe4\x93\x02-2(/assistants/v1/assistants/{assistant_id}:\x01*\x12\xa9\x01\n\x06\x44\x65lete\x12\x35.yandex.cloud.ai.assistants.v1.DeleteAssistantRequest\x1a\x36.yandex.cloud.ai.assistants.v1.DeleteAssistantResponse\"0\x82\xd3\xe4\x93\x02**(/assistants/v1/assistants/{assistant_id}\x12\x96\x01\n\x04List\x12\x34.yandex.cloud.ai.assistants.v1.ListAssistantsRequest\x1a\x35.yandex.cloud.ai.assistants.v1.ListAssistantsResponse\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/assistants/v1/assistants\x12\xb9\x01\n\x0cListVersions\x12;.yandex.cloud.ai.assistants.v1.ListAssistantVersionsRequest\x1a<.yandex.cloud.ai.assistants.v1.ListAssistantVersionsResponse\".\x82\xd3\xe4\x93\x02(\x12&/assistants/v1/assistants:listVersionsBq\n!yandex.cloud.api.ai.assistants.v1ZLgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/assistants/v1;assistantsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.ai.assistants.v1.assistant_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!yandex.cloud.api.ai.assistants.v1ZLgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/assistants/v1;assistants'
  _globals['_CREATEASSISTANTREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_CREATEASSISTANTREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_CREATEASSISTANTREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_CREATEASSISTANTREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001'
  _globals['_CREATEASSISTANTREQUEST'].fields_by_name['model_uri']._loaded_options = None
  _globals['_CREATEASSISTANTREQUEST'].fields_by_name['model_uri']._serialized_options = b'\350\3071\001'
  _globals['_GETASSISTANTREQUEST'].fields_by_name['assistant_id']._loaded_options = None
  _globals['_GETASSISTANTREQUEST'].fields_by_name['assistant_id']._serialized_options = b'\350\3071\001'
  _globals['_UPDATEASSISTANTREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_UPDATEASSISTANTREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_UPDATEASSISTANTREQUEST'].fields_by_name['assistant_id']._loaded_options = None
  _globals['_UPDATEASSISTANTREQUEST'].fields_by_name['assistant_id']._serialized_options = b'\350\3071\001'
  _globals['_UPDATEASSISTANTREQUEST'].fields_by_name['update_mask']._loaded_options = None
  _globals['_UPDATEASSISTANTREQUEST'].fields_by_name['update_mask']._serialized_options = b'\350\3071\001'
  _globals['_DELETEASSISTANTREQUEST'].fields_by_name['assistant_id']._loaded_options = None
  _globals['_DELETEASSISTANTREQUEST'].fields_by_name['assistant_id']._serialized_options = b'\350\3071\001'
  _globals['_LISTASSISTANTSREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_LISTASSISTANTSREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001'
  _globals['_LISTASSISTANTVERSIONSREQUEST'].fields_by_name['assistant_id']._loaded_options = None
  _globals['_LISTASSISTANTVERSIONSREQUEST'].fields_by_name['assistant_id']._serialized_options = b'\350\3071\001'
  _globals['_ASSISTANTSERVICE'].methods_by_name['Create']._loaded_options = None
  _globals['_ASSISTANTSERVICE'].methods_by_name['Create']._serialized_options = b'\202\323\344\223\002\036\"\031/assistants/v1/assistants:\001*'
  _globals['_ASSISTANTSERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_ASSISTANTSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002*\022(/assistants/v1/assistants/{assistant_id}'
  _globals['_ASSISTANTSERVICE'].methods_by_name['Update']._loaded_options = None
  _globals['_ASSISTANTSERVICE'].methods_by_name['Update']._serialized_options = b'\202\323\344\223\002-2(/assistants/v1/assistants/{assistant_id}:\001*'
  _globals['_ASSISTANTSERVICE'].methods_by_name['Delete']._loaded_options = None
  _globals['_ASSISTANTSERVICE'].methods_by_name['Delete']._serialized_options = b'\202\323\344\223\002**(/assistants/v1/assistants/{assistant_id}'
  _globals['_ASSISTANTSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_ASSISTANTSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002\033\022\031/assistants/v1/assistants'
  _globals['_ASSISTANTSERVICE'].methods_by_name['ListVersions']._loaded_options = None
  _globals['_ASSISTANTSERVICE'].methods_by_name['ListVersions']._serialized_options = b'\202\323\344\223\002(\022&/assistants/v1/assistants:listVersions'
  _globals['_CREATEASSISTANTREQUEST']._serialized_start=312
  _globals['_CREATEASSISTANTREQUEST']._serialized_end=934
  _globals['_CREATEASSISTANTREQUEST_LABELSENTRY']._serialized_start=889
  _globals['_CREATEASSISTANTREQUEST_LABELSENTRY']._serialized_end=934
  _globals['_GETASSISTANTREQUEST']._serialized_start=936
  _globals['_GETASSISTANTREQUEST']._serialized_end=985
  _globals['_UPDATEASSISTANTREQUEST']._serialized_start=988
  _globals['_UPDATEASSISTANTREQUEST']._serialized_end=1662
  _globals['_UPDATEASSISTANTREQUEST_LABELSENTRY']._serialized_start=889
  _globals['_UPDATEASSISTANTREQUEST_LABELSENTRY']._serialized_end=934
  _globals['_DELETEASSISTANTREQUEST']._serialized_start=1664
  _globals['_DELETEASSISTANTREQUEST']._serialized_end=1716
  _globals['_DELETEASSISTANTRESPONSE']._serialized_start=1718
  _globals['_DELETEASSISTANTRESPONSE']._serialized_end=1743
  _globals['_LISTASSISTANTSREQUEST']._serialized_start=1745
  _globals['_LISTASSISTANTSREQUEST']._serialized_end=1832
  _globals['_LISTASSISTANTSRESPONSE']._serialized_start=1834
  _globals['_LISTASSISTANTSRESPONSE']._serialized_end=1945
  _globals['_LISTASSISTANTVERSIONSREQUEST']._serialized_start=1947
  _globals['_LISTASSISTANTVERSIONSREQUEST']._serialized_end=2044
  _globals['_ASSISTANTVERSION']._serialized_start=2047
  _globals['_ASSISTANTVERSION']._serialized_end=2187
  _globals['_LISTASSISTANTVERSIONSRESPONSE']._serialized_start=2189
  _globals['_LISTASSISTANTVERSIONSRESPONSE']._serialized_end=2312
  _globals['_ASSISTANTSERVICE']._serialized_start=2315
  _globals['_ASSISTANTSERVICE']._serialized_end=3305
# @@protoc_insertion_point(module_scope)
