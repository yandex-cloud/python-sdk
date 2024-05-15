# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/dataproc/v1/subcluster.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud.dataproc.v1 import common_pb2 as yandex_dot_cloud_dot_dataproc_dot_v1_dot_common__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)yandex/cloud/dataproc/v1/subcluster.proto\x12\x18yandex.cloud.dataproc.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a%yandex/cloud/dataproc/v1/common.proto\x1a\x1dyandex/cloud/validation.proto\x1a\x1egoogle/protobuf/duration.proto\"\xf1\x02\n\x11\x41utoscalingConfig\x12\"\n\x0fmax_hosts_count\x18\x01 \x01(\x03\x42\t\xfa\xc7\x31\x05\x31-100\x12\x13\n\x0bpreemptible\x18\x02 \x01(\x08\x12G\n\x14measurement_duration\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationB\x0e\xe8\xc7\x31\x01\xfa\xc7\x31\x06\x31m-10m\x12=\n\x0fwarmup_duration\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationB\t\xfa\xc7\x31\x05<=10m\x12\x45\n\x16stabilization_duration\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationB\n\xfa\xc7\x31\x06\x31m-30m\x12)\n\x16\x63pu_utilization_target\x18\x06 \x01(\x01\x42\t\xfa\xc7\x31\x05\x30-100\x12)\n\x14\x64\x65\x63ommission_timeout\x18\x07 \x01(\x03\x42\x0b\xfa\xc7\x31\x07\x30-86400\"\x80\x03\n\nSubcluster\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ncluster_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x16\n\x04name\x18\x04 \x01(\tB\x08\x8a\xc8\x31\x04\x31-63\x12,\n\x04role\x18\x05 \x01(\x0e\x32\x1e.yandex.cloud.dataproc.v1.Role\x12\x36\n\tresources\x18\x06 \x01(\x0b\x32#.yandex.cloud.dataproc.v1.Resources\x12\x11\n\tsubnet_id\x18\x07 \x01(\t\x12\x13\n\x0bhosts_count\x18\x08 \x01(\x03\x12\x18\n\x10\x61ssign_public_ip\x18\t \x01(\x08\x12G\n\x12\x61utoscaling_config\x18\n \x01(\x0b\x32+.yandex.cloud.dataproc.v1.AutoscalingConfig\x12\x19\n\x11instance_group_id\x18\x0b \x01(\t\"\xa8\x01\n\x04Host\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rsubcluster_id\x18\x02 \x01(\t\x12\x30\n\x06health\x18\x03 \x01(\x0e\x32 .yandex.cloud.dataproc.v1.Health\x12\x1b\n\x13\x63ompute_instance_id\x18\x04 \x01(\t\x12,\n\x04role\x18\x05 \x01(\x0e\x32\x1e.yandex.cloud.dataproc.v1.Role*K\n\x04Role\x12\x14\n\x10ROLE_UNSPECIFIED\x10\x00\x12\x0e\n\nMASTERNODE\x10\x01\x12\x0c\n\x08\x44\x41TANODE\x10\x02\x12\x0f\n\x0b\x43OMPUTENODE\x10\x03\x42\x65\n\x1cyandex.cloud.api.dataproc.v1ZEgithub.com/yandex-cloud/go-genproto/yandex/cloud/dataproc/v1;dataprocb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.dataproc.v1.subcluster_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034yandex.cloud.api.dataproc.v1ZEgithub.com/yandex-cloud/go-genproto/yandex/cloud/dataproc/v1;dataproc'
  _AUTOSCALINGCONFIG.fields_by_name['max_hosts_count']._options = None
  _AUTOSCALINGCONFIG.fields_by_name['max_hosts_count']._serialized_options = b'\372\3071\0051-100'
  _AUTOSCALINGCONFIG.fields_by_name['measurement_duration']._options = None
  _AUTOSCALINGCONFIG.fields_by_name['measurement_duration']._serialized_options = b'\350\3071\001\372\3071\0061m-10m'
  _AUTOSCALINGCONFIG.fields_by_name['warmup_duration']._options = None
  _AUTOSCALINGCONFIG.fields_by_name['warmup_duration']._serialized_options = b'\372\3071\005<=10m'
  _AUTOSCALINGCONFIG.fields_by_name['stabilization_duration']._options = None
  _AUTOSCALINGCONFIG.fields_by_name['stabilization_duration']._serialized_options = b'\372\3071\0061m-30m'
  _AUTOSCALINGCONFIG.fields_by_name['cpu_utilization_target']._options = None
  _AUTOSCALINGCONFIG.fields_by_name['cpu_utilization_target']._serialized_options = b'\372\3071\0050-100'
  _AUTOSCALINGCONFIG.fields_by_name['decommission_timeout']._options = None
  _AUTOSCALINGCONFIG.fields_by_name['decommission_timeout']._serialized_options = b'\372\3071\0070-86400'
  _SUBCLUSTER.fields_by_name['name']._options = None
  _SUBCLUSTER.fields_by_name['name']._serialized_options = b'\212\3101\0041-63'
  _globals['_ROLE']._serialized_start=1136
  _globals['_ROLE']._serialized_end=1211
  _globals['_AUTOSCALINGCONFIG']._serialized_start=207
  _globals['_AUTOSCALINGCONFIG']._serialized_end=576
  _globals['_SUBCLUSTER']._serialized_start=579
  _globals['_SUBCLUSTER']._serialized_end=963
  _globals['_HOST']._serialized_start=966
  _globals['_HOST']._serialized_end=1134
# @@protoc_insertion_point(module_scope)
