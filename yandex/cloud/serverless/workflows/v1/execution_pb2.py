# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/serverless/workflows/v1/execution.proto
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
    'yandex/cloud/serverless/workflows/v1/execution.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4yandex/cloud/serverless/workflows/v1/execution.proto\x12$yandex.cloud.serverless.workflows.v1\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dyandex/cloud/validation.proto\"\x96\x04\n\tExecution\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0bworkflow_id\x18\x02 \x01(\t\x12\x43\n\x05input\x18\x04 \x01(\x0b\x32\x34.yandex.cloud.serverless.workflows.v1.ExecutionInput\x12\x45\n\x06result\x18\x05 \x01(\x0b\x32\x35.yandex.cloud.serverless.workflows.v1.ExecutionResult\x12\x43\n\x05\x65rror\x18\x06 \x01(\x0b\x32\x34.yandex.cloud.serverless.workflows.v1.ExecutionError\x12\x46\n\x06status\x18\x07 \x01(\x0e\x32\x36.yandex.cloud.serverless.workflows.v1.Execution.Status\x12.\n\nstarted_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x08\x64uration\x18\t \x01(\x0b\x32\x19.google.protobuf.Duration\"l\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\n\n\x06QUEUED\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\n\n\x06PAUSED\x10\x03\x12\x0b\n\x07STOPPED\x10\x04\x12\n\n\x06\x46\x41ILED\x10\x05\x12\x0c\n\x08\x46INISHED\x10\x06J\x04\x08\x03\x10\x04\"\xde\x01\n\x10\x45xecutionPreview\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0bworkflow_id\x18\x02 \x01(\t\x12\x46\n\x06status\x18\x04 \x01(\x0e\x32\x36.yandex.cloud.serverless.workflows.v1.Execution.Status\x12.\n\nstarted_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x08\x64uration\x18\x06 \x01(\x0b\x32\x19.google.protobuf.DurationJ\x04\x08\x03\x10\x04\"5\n\x0e\x45xecutionInput\x12\x14\n\ninput_json\x18\x01 \x01(\tH\x00\x42\r\n\x05input\x12\x04\xc0\xc1\x31\x01\"8\n\x0f\x45xecutionResult\x12\x15\n\x0bresult_json\x18\x01 \x01(\tH\x00\x42\x0e\n\x06result\x12\x04\xc0\xc1\x31\x01\"5\n\x0e\x45xecutionError\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x12\n\nerror_code\x18\x02 \x01(\tB~\n(yandex.cloud.api.serverless.workflows.v1ZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/workflows/v1;workflowsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.serverless.workflows.v1.execution_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n(yandex.cloud.api.serverless.workflows.v1ZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/workflows/v1;workflows'
  _globals['_EXECUTIONINPUT'].oneofs_by_name['input']._loaded_options = None
  _globals['_EXECUTIONINPUT'].oneofs_by_name['input']._serialized_options = b'\300\3011\001'
  _globals['_EXECUTIONRESULT'].oneofs_by_name['result']._loaded_options = None
  _globals['_EXECUTIONRESULT'].oneofs_by_name['result']._serialized_options = b'\300\3011\001'
  _globals['_EXECUTION']._serialized_start=191
  _globals['_EXECUTION']._serialized_end=725
  _globals['_EXECUTION_STATUS']._serialized_start=611
  _globals['_EXECUTION_STATUS']._serialized_end=719
  _globals['_EXECUTIONPREVIEW']._serialized_start=728
  _globals['_EXECUTIONPREVIEW']._serialized_end=950
  _globals['_EXECUTIONINPUT']._serialized_start=952
  _globals['_EXECUTIONINPUT']._serialized_end=1005
  _globals['_EXECUTIONRESULT']._serialized_start=1007
  _globals['_EXECUTIONRESULT']._serialized_end=1063
  _globals['_EXECUTIONERROR']._serialized_start=1065
  _globals['_EXECUTIONERROR']._serialized_end=1118
# @@protoc_insertion_point(module_scope)
