# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/spark/v1/job.proto
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
    'yandex/cloud/spark/v1/job.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fyandex/cloud/spark/v1/job.proto\x12\x15yandex.cloud.spark.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\xdc\x04\n\x03Job\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ncluster_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nstarted_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x66inished_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x12\n\ncreated_by\x18\x07 \x01(\t\x12\x31\n\x06status\x18\x08 \x01(\x0e\x32!.yandex.cloud.spark.v1.Job.Status\x12\x34\n\tspark_job\x18\t \x01(\x0b\x32\x1f.yandex.cloud.spark.v1.SparkJobH\x00\x12\x38\n\x0bpyspark_job\x18\n \x01(\x0b\x32!.yandex.cloud.spark.v1.PysparkJobH\x00\x12@\n\x10\x61pplication_info\x18\x0b \x01(\x0b\x32&.yandex.cloud.spark.v1.ApplicationInfo\x12\x0e\n\x06ui_url\x18\x0c \x01(\t\"\x80\x01\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x10\n\x0cPROVISIONING\x10\x01\x12\x0b\n\x07PENDING\x10\x02\x12\x0b\n\x07RUNNING\x10\x03\x12\t\n\x05\x45RROR\x10\x04\x12\x08\n\x04\x44ONE\x10\x05\x12\r\n\tCANCELLED\x10\x06\x12\x0e\n\nCANCELLING\x10\x07\x42\n\n\x08job_spec\"9\n\x12\x41pplicationAttempt\x12\n\n\x02id\x18\x01 \x01(\t\x12\x17\n\x0f\x61m_container_id\x18\x02 \x01(\t\"f\n\x0f\x41pplicationInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12G\n\x14\x61pplication_attempts\x18\x02 \x03(\x0b\x32).yandex.cloud.spark.v1.ApplicationAttempt\"\xc1\x02\n\x08SparkJob\x12\x0c\n\x04\x61rgs\x18\x01 \x03(\t\x12\x15\n\rjar_file_uris\x18\x02 \x03(\t\x12\x11\n\tfile_uris\x18\x03 \x03(\t\x12\x14\n\x0c\x61rchive_uris\x18\x04 \x03(\t\x12\x43\n\nproperties\x18\x05 \x03(\x0b\x32/.yandex.cloud.spark.v1.SparkJob.PropertiesEntry\x12\x19\n\x11main_jar_file_uri\x18\x06 \x01(\t\x12\x12\n\nmain_class\x18\x07 \x01(\t\x12\x10\n\x08packages\x18\x08 \x03(\t\x12\x14\n\x0crepositories\x18\t \x03(\t\x12\x18\n\x10\x65xclude_packages\x18\n \x03(\t\x1a\x31\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xce\x02\n\nPysparkJob\x12\x0c\n\x04\x61rgs\x18\x01 \x03(\t\x12\x15\n\rjar_file_uris\x18\x02 \x03(\t\x12\x11\n\tfile_uris\x18\x03 \x03(\t\x12\x14\n\x0c\x61rchive_uris\x18\x04 \x03(\t\x12\x45\n\nproperties\x18\x05 \x03(\x0b\x32\x31.yandex.cloud.spark.v1.PysparkJob.PropertiesEntry\x12\x1c\n\x14main_python_file_uri\x18\x06 \x01(\t\x12\x18\n\x10python_file_uris\x18\x07 \x03(\t\x12\x10\n\x08packages\x18\x08 \x03(\t\x12\x14\n\x0crepositories\x18\t \x03(\t\x12\x18\n\x10\x65xclude_packages\x18\n \x03(\t\x1a\x31\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\\\n\x19yandex.cloud.api.spark.v1Z?github.com/yandex-cloud/go-genproto/yandex/cloud/spark/v1;sparkb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.spark.v1.job_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031yandex.cloud.api.spark.v1Z?github.com/yandex-cloud/go-genproto/yandex/cloud/spark/v1;spark'
  _globals['_SPARKJOB_PROPERTIESENTRY']._loaded_options = None
  _globals['_SPARKJOB_PROPERTIESENTRY']._serialized_options = b'8\001'
  _globals['_PYSPARKJOB_PROPERTIESENTRY']._loaded_options = None
  _globals['_PYSPARKJOB_PROPERTIESENTRY']._serialized_options = b'8\001'
  _globals['_JOB']._serialized_start=92
  _globals['_JOB']._serialized_end=696
  _globals['_JOB_STATUS']._serialized_start=556
  _globals['_JOB_STATUS']._serialized_end=684
  _globals['_APPLICATIONATTEMPT']._serialized_start=698
  _globals['_APPLICATIONATTEMPT']._serialized_end=755
  _globals['_APPLICATIONINFO']._serialized_start=757
  _globals['_APPLICATIONINFO']._serialized_end=859
  _globals['_SPARKJOB']._serialized_start=862
  _globals['_SPARKJOB']._serialized_end=1183
  _globals['_SPARKJOB_PROPERTIESENTRY']._serialized_start=1134
  _globals['_SPARKJOB_PROPERTIESENTRY']._serialized_end=1183
  _globals['_PYSPARKJOB']._serialized_start=1186
  _globals['_PYSPARKJOB']._serialized_end=1520
  _globals['_PYSPARKJOB_PROPERTIESENTRY']._serialized_start=1134
  _globals['_PYSPARKJOB_PROPERTIESENTRY']._serialized_end=1183
# @@protoc_insertion_point(module_scope)
