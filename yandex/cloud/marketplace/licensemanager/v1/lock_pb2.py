# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/marketplace/licensemanager/v1/lock.proto
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
    'yandex/cloud/marketplace/licensemanager/v1/lock.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5yandex/cloud/marketplace/licensemanager/v1/lock.proto\x12*yandex.cloud.marketplace.licensemanager.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\x9d\x03\n\x04Lock\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0binstance_id\x18\x02 \x01(\t\x12\x13\n\x0bresource_id\x18\x03 \x01(\t\x12.\n\nstart_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\ncreated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x45\n\x05state\x18\x08 \x01(\x0e\x32\x36.yandex.cloud.marketplace.licensemanager.v1.Lock.State\x12\x13\n\x0btemplate_id\x18\t \x01(\t\"E\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08UNLOCKED\x10\x01\x12\n\n\x06LOCKED\x10\x02\x12\x0b\n\x07\x44\x45LETED\x10\x03\x42\x8f\x01\n.yandex.cloud.api.marketplace.licensemanager.v1Z]github.com/yandex-cloud/go-genproto/yandex/cloud/marketplace/licensemanager/v1;licensemanagerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.marketplace.licensemanager.v1.lock_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n.yandex.cloud.api.marketplace.licensemanager.v1Z]github.com/yandex-cloud/go-genproto/yandex/cloud/marketplace/licensemanager/v1;licensemanager'
  _globals['_LOCK']._serialized_start=135
  _globals['_LOCK']._serialized_end=548
  _globals['_LOCK_STATE']._serialized_start=479
  _globals['_LOCK_STATE']._serialized_end=548
# @@protoc_insertion_point(module_scope)
