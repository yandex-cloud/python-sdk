# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/loadtesting/api/v1/agent/agent.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.loadtesting.api.v1.agent import status_pb2 as yandex_dot_cloud_dot_loadtesting_dot_api_dot_v1_dot_agent_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1yandex/cloud/loadtesting/api/v1/agent/agent.proto\x12%yandex.cloud.loadtesting.api.v1.agent\x1a\x32yandex/cloud/loadtesting/api/v1/agent/status.proto\"\xec\x02\n\x05\x41gent\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x1b\n\x13\x63ompute_instance_id\x18\x05 \x01(\t\x12=\n\x06status\x18\x07 \x01(\x0e\x32-.yandex.cloud.loadtesting.api.v1.agent.Status\x12\x0e\n\x06\x65rrors\x18\x08 \x03(\t\x12\x16\n\x0e\x63urrent_job_id\x18\t \x01(\t\x12\x18\n\x10\x61gent_version_id\x18\n \x01(\t\x12H\n\x06labels\x18\x0c \x03(\x0b\x32\x38.yandex.cloud.loadtesting.api.v1.agent.Agent.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01J\x04\x08\x06\x10\x07J\x04\x08\x0b\x10\x0c\x42|\n)yandex.cloud.api.loadtesting.api.v1.agentZOgithub.com/yandex-cloud/go-genproto/yandex/cloud/loadtesting/api/v1/agent;agentb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.loadtesting.api.v1.agent.agent_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n)yandex.cloud.api.loadtesting.api.v1.agentZOgithub.com/yandex-cloud/go-genproto/yandex/cloud/loadtesting/api/v1/agent;agent'
  _globals['_AGENT_LABELSENTRY']._loaded_options = None
  _globals['_AGENT_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_AGENT']._serialized_start=145
  _globals['_AGENT']._serialized_end=509
  _globals['_AGENT_LABELSENTRY']._serialized_start=452
  _globals['_AGENT_LABELSENTRY']._serialized_end=497
# @@protoc_insertion_point(module_scope)
