# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/dataproc/manager/v1/job_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.dataproc.manager.v1 import job_pb2 as yandex_dot_cloud_dot_dataproc_dot_manager_dot_v1_dot_job__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2yandex/cloud/dataproc/manager/v1/job_service.proto\x12 yandex.cloud.dataproc.manager.v1\x1a\x1dyandex/cloud/validation.proto\x1a*yandex/cloud/dataproc/manager/v1/job.proto\"\x89\x01\n\x0fListJobsRequest\x12\x1c\n\ncluster_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"`\n\x10ListJobsResponse\x12\x33\n\x04jobs\x18\x01 \x03(\x0b\x32%.yandex.cloud.dataproc.manager.v1.Job\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xdb\x01\n\x16UpdateJobStatusRequest\x12\x1c\n\ncluster_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x18\n\x06job_id\x18\x02 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12<\n\x06status\x18\x03 \x01(\x0e\x32,.yandex.cloud.dataproc.manager.v1.Job.Status\x12K\n\x10\x61pplication_info\x18\x04 \x01(\x0b\x32\x31.yandex.cloud.dataproc.manager.v1.ApplicationInfo\"\x19\n\x17UpdateJobStatusResponse2\x8b\x02\n\nJobService\x12u\n\nListActive\x12\x31.yandex.cloud.dataproc.manager.v1.ListJobsRequest\x1a\x32.yandex.cloud.dataproc.manager.v1.ListJobsResponse\"\x00\x12\x85\x01\n\x0cUpdateStatus\x12\x38.yandex.cloud.dataproc.manager.v1.UpdateJobStatusRequest\x1a\x39.yandex.cloud.dataproc.manager.v1.UpdateJobStatusResponse\"\x00\x42}\n$yandex.cloud.api.dataproc.manager.v1ZUgithub.com/yandex-cloud/go-genproto/yandex/cloud/dataproc/manager/v1;dataproc_managerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.dataproc.manager.v1.job_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n$yandex.cloud.api.dataproc.manager.v1ZUgithub.com/yandex-cloud/go-genproto/yandex/cloud/dataproc/manager/v1;dataproc_manager'
  _LISTJOBSREQUEST.fields_by_name['cluster_id']._options = None
  _LISTJOBSREQUEST.fields_by_name['cluster_id']._serialized_options = b'\212\3101\004<=50'
  _LISTJOBSREQUEST.fields_by_name['page_size']._options = None
  _LISTJOBSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTJOBSREQUEST.fields_by_name['page_token']._options = None
  _LISTJOBSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _LISTJOBSREQUEST.fields_by_name['filter']._options = None
  _LISTJOBSREQUEST.fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _UPDATEJOBSTATUSREQUEST.fields_by_name['cluster_id']._options = None
  _UPDATEJOBSTATUSREQUEST.fields_by_name['cluster_id']._serialized_options = b'\212\3101\004<=50'
  _UPDATEJOBSTATUSREQUEST.fields_by_name['job_id']._options = None
  _UPDATEJOBSTATUSREQUEST.fields_by_name['job_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_LISTJOBSREQUEST']._serialized_start=164
  _globals['_LISTJOBSREQUEST']._serialized_end=301
  _globals['_LISTJOBSRESPONSE']._serialized_start=303
  _globals['_LISTJOBSRESPONSE']._serialized_end=399
  _globals['_UPDATEJOBSTATUSREQUEST']._serialized_start=402
  _globals['_UPDATEJOBSTATUSREQUEST']._serialized_end=621
  _globals['_UPDATEJOBSTATUSRESPONSE']._serialized_start=623
  _globals['_UPDATEJOBSTATUSRESPONSE']._serialized_end=648
  _globals['_JOBSERVICE']._serialized_start=651
  _globals['_JOBSERVICE']._serialized_end=918
# @@protoc_insertion_point(module_scope)
