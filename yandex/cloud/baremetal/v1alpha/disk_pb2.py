# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/baremetal/v1alpha/disk.proto
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
    'yandex/cloud/baremetal/v1alpha/disk.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)yandex/cloud/baremetal/v1alpha/disk.proto\x12\x1eyandex.cloud.baremetal.v1alpha\"a\n\x04\x44isk\x12\n\n\x02id\x18\x01 \x01(\t\x12;\n\x04type\x18\x02 \x01(\x0e\x32-.yandex.cloud.baremetal.v1alpha.DiskDriveType\x12\x10\n\x08size_gib\x18\x03 \x01(\x03*B\n\rDiskDriveType\x12\x1f\n\x1b\x44ISK_DRIVE_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03HDD\x10\x01\x12\x07\n\x03SSD\x10\x02\x42r\n\"yandex.cloud.api.baremetal.v1alphaZLgithub.com/yandex-cloud/go-genproto/yandex/cloud/baremetal/v1alpha;baremetalb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.baremetal.v1alpha.disk_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"yandex.cloud.api.baremetal.v1alphaZLgithub.com/yandex-cloud/go-genproto/yandex/cloud/baremetal/v1alpha;baremetal'
  _globals['_DISKDRIVETYPE']._serialized_start=176
  _globals['_DISKDRIVETYPE']._serialized_end=242
  _globals['_DISK']._serialized_start=77
  _globals['_DISK']._serialized_end=174
# @@protoc_insertion_point(module_scope)
