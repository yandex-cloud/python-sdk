# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/loadtesting/api/v1/agent/agent.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.loadtesting.api.v1.agent import status_pb2 as yandex_dot_cloud_dot_loadtesting_dot_api_dot_v1_dot_agent_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/loadtesting/api/v1/agent/agent.proto',
  package='yandex.cloud.loadtesting.api.v1.agent',
  syntax='proto3',
  serialized_options=b'\n)yandex.cloud.api.loadtesting.api.v1.agentZOgithub.com/yandex-cloud/go-genproto/yandex/cloud/loadtesting/api/v1/agent;agent',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n1yandex/cloud/loadtesting/api/v1/agent/agent.proto\x12%yandex.cloud.loadtesting.api.v1.agent\x1a\x32yandex/cloud/loadtesting/api/v1/agent/status.proto\"\xcd\x01\n\x05\x41gent\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x1b\n\x13\x63ompute_instance_id\x18\x05 \x01(\t\x12=\n\x06status\x18\x07 \x01(\x0e\x32-.yandex.cloud.loadtesting.api.v1.agent.Status\x12\x0e\n\x06\x65rrors\x18\x08 \x03(\t\x12\x16\n\x0e\x63urrent_job_id\x18\t \x01(\tB|\n)yandex.cloud.api.loadtesting.api.v1.agentZOgithub.com/yandex-cloud/go-genproto/yandex/cloud/loadtesting/api/v1/agent;agentb\x06proto3'
  ,
  dependencies=[yandex_dot_cloud_dot_loadtesting_dot_api_dot_v1_dot_agent_dot_status__pb2.DESCRIPTOR,])




_AGENT = _descriptor.Descriptor(
  name='Agent',
  full_name='yandex.cloud.loadtesting.api.v1.agent.Agent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.loadtesting.api.v1.agent.Agent.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.loadtesting.api.v1.agent.Agent.folder_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.loadtesting.api.v1.agent.Agent.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.loadtesting.api.v1.agent.Agent.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='compute_instance_id', full_name='yandex.cloud.loadtesting.api.v1.agent.Agent.compute_instance_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='yandex.cloud.loadtesting.api.v1.agent.Agent.status', index=5,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='errors', full_name='yandex.cloud.loadtesting.api.v1.agent.Agent.errors', index=6,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='current_job_id', full_name='yandex.cloud.loadtesting.api.v1.agent.Agent.current_job_id', index=7,
      number=9, type=9, cpp_type=9, label=1,
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
  serialized_start=145,
  serialized_end=350,
)

_AGENT.fields_by_name['status'].enum_type = yandex_dot_cloud_dot_loadtesting_dot_api_dot_v1_dot_agent_dot_status__pb2._STATUS
DESCRIPTOR.message_types_by_name['Agent'] = _AGENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Agent = _reflection.GeneratedProtocolMessageType('Agent', (_message.Message,), {
  'DESCRIPTOR' : _AGENT,
  '__module__' : 'yandex.cloud.loadtesting.api.v1.agent.agent_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.loadtesting.api.v1.agent.Agent)
  })
_sym_db.RegisterMessage(Agent)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
