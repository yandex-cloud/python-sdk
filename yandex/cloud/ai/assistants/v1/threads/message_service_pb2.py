# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/ai/assistants/v1/threads/message_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.ai.assistants.v1.threads import message_pb2 as yandex_dot_cloud_dot_ai_dot_assistants_dot_v1_dot_threads_dot_message__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;yandex/cloud/ai/assistants/v1/threads/message_service.proto\x12%yandex.cloud.ai.assistants.v1.threads\x1a\x33yandex/cloud/ai/assistants/v1/threads/message.proto\x1a\x1dyandex/cloud/validation.proto\x1a\x1cgoogle/api/annotations.proto\"\xc4\x02\n\x14\x43reateMessageRequest\x12\x17\n\tthread_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12=\n\x06\x61uthor\x18\x02 \x01(\x0b\x32-.yandex.cloud.ai.assistants.v1.threads.Author\x12W\n\x06labels\x18\x03 \x03(\x0b\x32G.yandex.cloud.ai.assistants.v1.threads.CreateMessageRequest.LabelsEntry\x12L\n\x07\x63ontent\x18\x04 \x01(\x0b\x32\x35.yandex.cloud.ai.assistants.v1.threads.MessageContentB\x04\xe8\xc7\x31\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"F\n\x11GetMessageRequest\x12\x17\n\tthread_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x18\n\nmessage_id\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\".\n\x13ListMessagesRequest\x12\x17\n\tthread_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x32\xe4\x03\n\x0eMessageService\x12\x99\x01\n\x06\x43reate\x12;.yandex.cloud.ai.assistants.v1.threads.CreateMessageRequest\x1a..yandex.cloud.ai.assistants.v1.threads.Message\"\"\x82\xd3\xe4\x93\x02\x1c\"\x17/assistants/v1/messages:\x01*\x12\x9d\x01\n\x03Get\x12\x38.yandex.cloud.ai.assistants.v1.threads.GetMessageRequest\x1a..yandex.cloud.ai.assistants.v1.threads.Message\",\x82\xd3\xe4\x93\x02&\x12$/assistants/v1/messages/{message_id}\x12\x95\x01\n\x04List\x12:.yandex.cloud.ai.assistants.v1.threads.ListMessagesRequest\x1a..yandex.cloud.ai.assistants.v1.threads.Message\"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/assistants/v1/messages0\x01\x42~\n)yandex.cloud.api.ai.assistants.v1.threadsZQgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/assistants/v1/threads;threadsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.ai.assistants.v1.threads.message_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n)yandex.cloud.api.ai.assistants.v1.threadsZQgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/assistants/v1/threads;threads'
  _CREATEMESSAGEREQUEST_LABELSENTRY._options = None
  _CREATEMESSAGEREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _CREATEMESSAGEREQUEST.fields_by_name['thread_id']._options = None
  _CREATEMESSAGEREQUEST.fields_by_name['thread_id']._serialized_options = b'\350\3071\001'
  _CREATEMESSAGEREQUEST.fields_by_name['content']._options = None
  _CREATEMESSAGEREQUEST.fields_by_name['content']._serialized_options = b'\350\3071\001'
  _GETMESSAGEREQUEST.fields_by_name['thread_id']._options = None
  _GETMESSAGEREQUEST.fields_by_name['thread_id']._serialized_options = b'\350\3071\001'
  _GETMESSAGEREQUEST.fields_by_name['message_id']._options = None
  _GETMESSAGEREQUEST.fields_by_name['message_id']._serialized_options = b'\350\3071\001'
  _LISTMESSAGESREQUEST.fields_by_name['thread_id']._options = None
  _LISTMESSAGESREQUEST.fields_by_name['thread_id']._serialized_options = b'\350\3071\001'
  _MESSAGESERVICE.methods_by_name['Create']._options = None
  _MESSAGESERVICE.methods_by_name['Create']._serialized_options = b'\202\323\344\223\002\034\"\027/assistants/v1/messages:\001*'
  _MESSAGESERVICE.methods_by_name['Get']._options = None
  _MESSAGESERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002&\022$/assistants/v1/messages/{message_id}'
  _MESSAGESERVICE.methods_by_name['List']._options = None
  _MESSAGESERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\031\022\027/assistants/v1/messages'
  _globals['_CREATEMESSAGEREQUEST']._serialized_start=217
  _globals['_CREATEMESSAGEREQUEST']._serialized_end=541
  _globals['_CREATEMESSAGEREQUEST_LABELSENTRY']._serialized_start=496
  _globals['_CREATEMESSAGEREQUEST_LABELSENTRY']._serialized_end=541
  _globals['_GETMESSAGEREQUEST']._serialized_start=543
  _globals['_GETMESSAGEREQUEST']._serialized_end=613
  _globals['_LISTMESSAGESREQUEST']._serialized_start=615
  _globals['_LISTMESSAGESREQUEST']._serialized_end=661
  _globals['_MESSAGESERVICE']._serialized_start=664
  _globals['_MESSAGESERVICE']._serialized_end=1148
# @@protoc_insertion_point(module_scope)