# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/cloudapps/workload/v1/cloud_application_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.cloudapps.workload.v1 import cloud_application_pb2 as yandex_dot_cloud_dot_cloudapps_dot_workload_dot_v1_dot_cloud__application__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nByandex/cloud/cloudapps/workload/v1/cloud_application_service.proto\x12\"yandex.cloud.cloudapps.workload.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1dyandex/cloud/validation.proto\x1a:yandex/cloud/cloudapps/workload/v1/cloud_application.proto\"\xea\x01\n\x18ResolveByWorkloadRequest\x12\x66\n\rworkload_type\x18\x01 \x01(\x0e\x32I.yandex.cloud.cloudapps.workload.v1.ResolveByWorkloadRequest.WorkloadTypeB\x04\xe8\xc7\x31\x01\x12!\n\x0bworkload_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"C\n\x0cWorkloadType\x12\x1d\n\x19WORKLOAD_TYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10\x43OMPUTE_INSTANCE\x10\x01\"l\n\x19ResolveByWorkloadResponse\x12O\n\x11\x63loud_application\x18\x01 \x01(\x0b\x32\x34.yandex.cloud.cloudapps.workload.v1.CloudApplication2\x85\x02\n\x17\x43loudApplicationService\x12U\n\x03Get\x12\x16.google.protobuf.Empty\x1a\x34.yandex.cloud.cloudapps.workload.v1.CloudApplication\"\x00\x12\x92\x01\n\x11ResolveByWorkload\x12<.yandex.cloud.cloudapps.workload.v1.ResolveByWorkloadRequest\x1a=.yandex.cloud.cloudapps.workload.v1.ResolveByWorkloadResponse\"\x00\x42y\n&yandex.cloud.api.cloudapps.workload.v1ZOgithub.com/yandex-cloud/go-genproto/yandex/cloud/cloudapps/workload/v1;workloadb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.cloudapps.workload.v1.cloud_application_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n&yandex.cloud.api.cloudapps.workload.v1ZOgithub.com/yandex-cloud/go-genproto/yandex/cloud/cloudapps/workload/v1;workload'
  _RESOLVEBYWORKLOADREQUEST.fields_by_name['workload_type']._options = None
  _RESOLVEBYWORKLOADREQUEST.fields_by_name['workload_type']._serialized_options = b'\350\3071\001'
  _RESOLVEBYWORKLOADREQUEST.fields_by_name['workload_id']._options = None
  _RESOLVEBYWORKLOADREQUEST.fields_by_name['workload_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_RESOLVEBYWORKLOADREQUEST']._serialized_start=227
  _globals['_RESOLVEBYWORKLOADREQUEST']._serialized_end=461
  _globals['_RESOLVEBYWORKLOADREQUEST_WORKLOADTYPE']._serialized_start=394
  _globals['_RESOLVEBYWORKLOADREQUEST_WORKLOADTYPE']._serialized_end=461
  _globals['_RESOLVEBYWORKLOADRESPONSE']._serialized_start=463
  _globals['_RESOLVEBYWORKLOADRESPONSE']._serialized_end=571
  _globals['_CLOUDAPPLICATIONSERVICE']._serialized_start=574
  _globals['_CLOUDAPPLICATIONSERVICE']._serialized_end=835
# @@protoc_insertion_point(module_scope)