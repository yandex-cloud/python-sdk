# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/dataproc/v1/job_service.proto
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
    'yandex/cloud/dataproc/v1/job_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.dataproc.v1 import job_pb2 as yandex_dot_cloud_dot_dataproc_dot_v1_dot_job__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*yandex/cloud/dataproc/v1/job_service.proto\x12\x18yandex.cloud.dataproc.v1\x1a\x1cgoogle/api/annotations.proto\x1a\"yandex/cloud/dataproc/v1/job.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\x1a yandex/cloud/api/operation.proto\"O\n\rGetJobRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1c\n\x06job_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\x8d\x01\n\x0fListJobsRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"X\n\x10ListJobsResponse\x12+\n\x04jobs\x18\x01 \x03(\x0b\x32\x1d.yandex.cloud.dataproc.v1.Job\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xdf\x02\n\x10\x43reateJobRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x04name\x18\x02 \x01(\tB!\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12?\n\rmapreduce_job\x18\x03 \x01(\x0b\x32&.yandex.cloud.dataproc.v1.MapreduceJobH\x00\x12\x37\n\tspark_job\x18\x04 \x01(\x0b\x32\".yandex.cloud.dataproc.v1.SparkJobH\x00\x12;\n\x0bpyspark_job\x18\x05 \x01(\x0b\x32$.yandex.cloud.dataproc.v1.PysparkJobH\x00\x12\x35\n\x08hive_job\x18\x06 \x01(\x0b\x32!.yandex.cloud.dataproc.v1.HiveJobH\x00\x42\n\n\x08job_spec\"O\n\x11\x43reateJobMetadata\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x18\n\x06job_id\x18\x02 \x01(\tB\x08\x8a\xc8\x31\x04<=50\"R\n\x10\x43\x61ncelJobRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1c\n\x06job_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\x90\x01\n\x11ListJobLogRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x18\n\x06job_id\x18\x02 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12 \n\tpage_size\x18\x03 \x01(\x03\x42\r\xfa\xc7\x31\t<=1048576\x12\x1d\n\npage_token\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=100\">\n\x12ListJobLogResponse\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xb1\x06\n\nJobService\x12\x8e\x01\n\x04List\x12).yandex.cloud.dataproc.v1.ListJobsRequest\x1a*.yandex.cloud.dataproc.v1.ListJobsResponse\"/\x82\xd3\xe4\x93\x02)\x12\'/dataproc/v1/clusters/{cluster_id}/jobs\x12\xa7\x01\n\x06\x43reate\x12*.yandex.cloud.dataproc.v1.CreateJobRequest\x1a!.yandex.cloud.operation.Operation\"N\xb2\xd2*\x18\n\x11\x43reateJobMetadata\x12\x03Job\x82\xd3\xe4\x93\x02,\"\'/dataproc/v1/clusters/{cluster_id}/jobs:\x01*\x12\x87\x01\n\x03Get\x12\'.yandex.cloud.dataproc.v1.GetJobRequest\x1a\x1d.yandex.cloud.dataproc.v1.Job\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/dataproc/v1/clusters/{cluster_id}/jobs/{job_id}\x12\xa3\x01\n\x07ListLog\x12+.yandex.cloud.dataproc.v1.ListJobLogRequest\x1a,.yandex.cloud.dataproc.v1.ListJobLogResponse\"=\x82\xd3\xe4\x93\x02\x37\x12\x35/dataproc/v1/clusters/{cluster_id}/jobs/{job_id}:logs\x12\xb7\x01\n\x06\x43\x61ncel\x12*.yandex.cloud.dataproc.v1.CancelJobRequest\x1a!.yandex.cloud.operation.Operation\"^\xb2\xd2*\x18\n\x11\x43reateJobMetadata\x12\x03Job\x82\xd3\xe4\x93\x02<\"7/dataproc/v1/clusters/{cluster_id}/jobs/{job_id}:cancel:\x01*Bk\n\x1cyandex.cloud.api.dataproc.v1B\x04PHJSZEgithub.com/yandex-cloud/go-genproto/yandex/cloud/dataproc/v1;dataprocb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.dataproc.v1.job_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034yandex.cloud.api.dataproc.v1B\004PHJSZEgithub.com/yandex-cloud/go-genproto/yandex/cloud/dataproc/v1;dataproc'
  _globals['_GETJOBREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_GETJOBREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_GETJOBREQUEST'].fields_by_name['job_id']._loaded_options = None
  _globals['_GETJOBREQUEST'].fields_by_name['job_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTJOBSREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_LISTJOBSREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTJOBSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTJOBSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTJOBSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTJOBSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTJOBSREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTJOBSREQUEST'].fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _globals['_CREATEJOBREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_CREATEJOBREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_CREATEJOBREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_CREATEJOBREQUEST'].fields_by_name['name']._serialized_options = b'\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _globals['_CREATEJOBMETADATA'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_CREATEJOBMETADATA'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_CREATEJOBMETADATA'].fields_by_name['job_id']._loaded_options = None
  _globals['_CREATEJOBMETADATA'].fields_by_name['job_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_CANCELJOBREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_CANCELJOBREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_CANCELJOBREQUEST'].fields_by_name['job_id']._loaded_options = None
  _globals['_CANCELJOBREQUEST'].fields_by_name['job_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTJOBLOGREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_LISTJOBLOGREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTJOBLOGREQUEST'].fields_by_name['job_id']._loaded_options = None
  _globals['_LISTJOBLOGREQUEST'].fields_by_name['job_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_LISTJOBLOGREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTJOBLOGREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\t<=1048576'
  _globals['_LISTJOBLOGREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTJOBLOGREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_JOBSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_JOBSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002)\022\'/dataproc/v1/clusters/{cluster_id}/jobs'
  _globals['_JOBSERVICE'].methods_by_name['Create']._loaded_options = None
  _globals['_JOBSERVICE'].methods_by_name['Create']._serialized_options = b'\262\322*\030\n\021CreateJobMetadata\022\003Job\202\323\344\223\002,\"\'/dataproc/v1/clusters/{cluster_id}/jobs:\001*'
  _globals['_JOBSERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_JOBSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\0022\0220/dataproc/v1/clusters/{cluster_id}/jobs/{job_id}'
  _globals['_JOBSERVICE'].methods_by_name['ListLog']._loaded_options = None
  _globals['_JOBSERVICE'].methods_by_name['ListLog']._serialized_options = b'\202\323\344\223\0027\0225/dataproc/v1/clusters/{cluster_id}/jobs/{job_id}:logs'
  _globals['_JOBSERVICE'].methods_by_name['Cancel']._loaded_options = None
  _globals['_JOBSERVICE'].methods_by_name['Cancel']._serialized_options = b'\262\322*\030\n\021CreateJobMetadata\022\003Job\202\323\344\223\002<\"7/dataproc/v1/clusters/{cluster_id}/jobs/{job_id}:cancel:\001*'
  _globals['_GETJOBREQUEST']._serialized_start=243
  _globals['_GETJOBREQUEST']._serialized_end=322
  _globals['_LISTJOBSREQUEST']._serialized_start=325
  _globals['_LISTJOBSREQUEST']._serialized_end=466
  _globals['_LISTJOBSRESPONSE']._serialized_start=468
  _globals['_LISTJOBSRESPONSE']._serialized_end=556
  _globals['_CREATEJOBREQUEST']._serialized_start=559
  _globals['_CREATEJOBREQUEST']._serialized_end=910
  _globals['_CREATEJOBMETADATA']._serialized_start=912
  _globals['_CREATEJOBMETADATA']._serialized_end=991
  _globals['_CANCELJOBREQUEST']._serialized_start=993
  _globals['_CANCELJOBREQUEST']._serialized_end=1075
  _globals['_LISTJOBLOGREQUEST']._serialized_start=1078
  _globals['_LISTJOBLOGREQUEST']._serialized_end=1222
  _globals['_LISTJOBLOGRESPONSE']._serialized_start=1224
  _globals['_LISTJOBLOGRESPONSE']._serialized_end=1286
  _globals['_JOBSERVICE']._serialized_start=1289
  _globals['_JOBSERVICE']._serialized_end=2106
# @@protoc_insertion_point(module_scope)
