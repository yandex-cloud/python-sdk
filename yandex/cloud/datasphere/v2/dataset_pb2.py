# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/datasphere/v2/dataset.proto
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
    'yandex/cloud/datasphere/v2/dataset.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(yandex/cloud/datasphere/v2/dataset.proto\x12\x1ayandex.cloud.datasphere.v2\x1a\x1fgoogle/protobuf/timestamp.proto\"\xe1\x02\n\x07\x44\x61taset\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12?\n\x06labels\x18\x06 \x03(\x0b\x32/.yandex.cloud.datasphere.v2.Dataset.LabelsEntry\x12\x15\n\rcreated_by_id\x18\x07 \x01(\t\x12\x0c\n\x04\x63ode\x18\x08 \x01(\t\x12\x0f\n\x07size_gb\x18\t \x01(\x03\x12\x10\n\x08zone_ids\x18\n \x03(\t\x12\x12\n\nmount_path\x18\x0b \x01(\t\x12\x17\n\x0f\x64\x61ta_capsule_id\x18\x0c \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xce\x02\n\rDatasetStatus\x12O\n\rstatus_active\x18\x01 \x01(\x0b\x32\x36.yandex.cloud.datasphere.v2.DatasetStatus.StatusActiveH\x00\x12S\n\x0fstatus_inactive\x18\x02 \x01(\x0b\x32\x38.yandex.cloud.datasphere.v2.DatasetStatus.StatusInactiveH\x00\x12M\n\x0cstatus_error\x18\x03 \x01(\x0b\x32\x35.yandex.cloud.datasphere.v2.DatasetStatus.StatusErrorH\x00\x1a\x0e\n\x0cStatusActive\x1a\x10\n\x0eStatusInactive\x1a\x1c\n\x0bStatusError\x12\r\n\x05\x65rror\x18\x01 \x01(\tB\x08\n\x06statusBk\n\x1eyandex.cloud.api.datasphere.v2ZIgithub.com/yandex-cloud/go-genproto/yandex/cloud/datasphere/v2;datasphereb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.datasphere.v2.dataset_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036yandex.cloud.api.datasphere.v2ZIgithub.com/yandex-cloud/go-genproto/yandex/cloud/datasphere/v2;datasphere'
  _globals['_DATASET_LABELSENTRY']._loaded_options = None
  _globals['_DATASET_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_DATASET']._serialized_start=106
  _globals['_DATASET']._serialized_end=459
  _globals['_DATASET_LABELSENTRY']._serialized_start=414
  _globals['_DATASET_LABELSENTRY']._serialized_end=459
  _globals['_DATASETSTATUS']._serialized_start=462
  _globals['_DATASETSTATUS']._serialized_end=796
  _globals['_DATASETSTATUS_STATUSACTIVE']._serialized_start=724
  _globals['_DATASETSTATUS_STATUSACTIVE']._serialized_end=738
  _globals['_DATASETSTATUS_STATUSINACTIVE']._serialized_start=740
  _globals['_DATASETSTATUS_STATUSINACTIVE']._serialized_end=756
  _globals['_DATASETSTATUS_STATUSERROR']._serialized_start=758
  _globals['_DATASETSTATUS_STATUSERROR']._serialized_end=786
# @@protoc_insertion_point(module_scope)
