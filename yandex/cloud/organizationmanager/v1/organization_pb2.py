# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/organizationmanager/v1/organization.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6yandex/cloud/organizationmanager/v1/organization.proto\x12#yandex.cloud.organizationmanager.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\xfa\x01\n\x0cOrganization\x12\n\n\x02id\x18\x01 \x01(\t\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\r\n\x05title\x18\x06 \x01(\t\x12M\n\x06labels\x18\x07 \x03(\x0b\x32=.yandex.cloud.organizationmanager.v1.Organization.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x86\x01\n\'yandex.cloud.api.organizationmanager.v1Z[github.com/yandex-cloud/go-genproto/yandex/cloud/organizationmanager/v1;organizationmanagerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.organizationmanager.v1.organization_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\'yandex.cloud.api.organizationmanager.v1Z[github.com/yandex-cloud/go-genproto/yandex/cloud/organizationmanager/v1;organizationmanager'
  _globals['_ORGANIZATION_LABELSENTRY']._loaded_options = None
  _globals['_ORGANIZATION_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_ORGANIZATION']._serialized_start=129
  _globals['_ORGANIZATION']._serialized_end=379
  _globals['_ORGANIZATION_LABELSENTRY']._serialized_start=334
  _globals['_ORGANIZATION_LABELSENTRY']._serialized_end=379
# @@protoc_insertion_point(module_scope)
