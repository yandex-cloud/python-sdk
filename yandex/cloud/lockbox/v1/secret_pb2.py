# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/lockbox/v1/secret.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$yandex/cloud/lockbox/v1/secret.proto\x12\x17yandex.cloud.lockbox.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\xd4\x03\n\x06Secret\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12;\n\x06labels\x18\x06 \x03(\x0b\x32+.yandex.cloud.lockbox.v1.Secret.LabelsEntry\x12\x12\n\nkms_key_id\x18\x07 \x01(\t\x12\x36\n\x06status\x18\x08 \x01(\x0e\x32&.yandex.cloud.lockbox.v1.Secret.Status\x12\x39\n\x0f\x63urrent_version\x18\t \x01(\x0b\x32 .yandex.cloud.lockbox.v1.Version\x12\x1b\n\x13\x64\x65letion_protection\x18\n \x01(\x08\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"H\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12\x0c\n\x08INACTIVE\x10\x03\"\xce\x02\n\x07Version\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tsecret_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\ndestroy_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x37\n\x06status\x18\x06 \x01(\x0e\x32\'.yandex.cloud.lockbox.v1.Version.Status\x12\x1a\n\x12payload_entry_keys\x18\x07 \x03(\t\"Z\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\n\n\x06\x41\x43TIVE\x10\x01\x12\x1d\n\x19SCHEDULED_FOR_DESTRUCTION\x10\x02\x12\r\n\tDESTROYED\x10\x03\x42\x62\n\x1byandex.cloud.api.lockbox.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/lockbox/v1;lockboxb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.lockbox.v1.secret_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033yandex.cloud.api.lockbox.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/lockbox/v1;lockbox'
  _globals['_SECRET_LABELSENTRY']._loaded_options = None
  _globals['_SECRET_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_SECRET']._serialized_start=99
  _globals['_SECRET']._serialized_end=567
  _globals['_SECRET_LABELSENTRY']._serialized_start=448
  _globals['_SECRET_LABELSENTRY']._serialized_end=493
  _globals['_SECRET_STATUS']._serialized_start=495
  _globals['_SECRET_STATUS']._serialized_end=567
  _globals['_VERSION']._serialized_start=570
  _globals['_VERSION']._serialized_end=904
  _globals['_VERSION_STATUS']._serialized_start=814
  _globals['_VERSION_STATUS']._serialized_end=904
# @@protoc_insertion_point(module_scope)
