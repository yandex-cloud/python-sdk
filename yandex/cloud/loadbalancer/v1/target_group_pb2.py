# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/loadbalancer/v1/target_group.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/yandex/cloud/loadbalancer/v1/target_group.proto\x12\x1cyandex.cloud.loadbalancer.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dyandex/cloud/validation.proto\"\xbf\x02\n\x0bTargetGroup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x45\n\x06labels\x18\x06 \x03(\x0b\x32\x35.yandex.cloud.loadbalancer.v1.TargetGroup.LabelsEntry\x12\x11\n\tregion_id\x18\x07 \x01(\t\x12\x35\n\x07targets\x18\t \x03(\x0b\x32$.yandex.cloud.loadbalancer.v1.Target\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"6\n\x06Target\x12\x1b\n\tsubnet_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\tBq\n yandex.cloud.api.loadbalancer.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/loadbalancer/v1;loadbalancerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.loadbalancer.v1.target_group_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n yandex.cloud.api.loadbalancer.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/loadbalancer/v1;loadbalancer'
  _globals['_TARGETGROUP_LABELSENTRY']._loaded_options = None
  _globals['_TARGETGROUP_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_TARGET'].fields_by_name['subnet_id']._loaded_options = None
  _globals['_TARGET'].fields_by_name['subnet_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_TARGETGROUP']._serialized_start=146
  _globals['_TARGETGROUP']._serialized_end=465
  _globals['_TARGETGROUP_LABELSENTRY']._serialized_start=420
  _globals['_TARGETGROUP_LABELSENTRY']._serialized_end=465
  _globals['_TARGET']._serialized_start=467
  _globals['_TARGET']._serialized_end=521
# @@protoc_insertion_point(module_scope)
