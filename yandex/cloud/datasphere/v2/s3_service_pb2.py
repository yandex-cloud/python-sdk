# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/datasphere/v2/s3_service.proto
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
    'yandex/cloud/datasphere/v2/s3_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+yandex/cloud/datasphere/v2/s3_service.proto\x12\x1ayandex.cloud.datasphere.v2\x1a\x1cgoogle/api/annotations.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"R\n\x11\x41\x63tivateS3Request\x12\x1b\n\x05s3_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12 \n\nproject_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"T\n\x13\x44\x65\x61\x63tivateS3Request\x12\x1b\n\x05s3_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12 \n\nproject_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=502\xd3\x02\n\tS3Service\x12\x9e\x01\n\x08\x41\x63tivate\x12-.yandex.cloud.datasphere.v2.ActivateS3Request\x1a!.yandex.cloud.operation.Operation\"@\xb2\xd2*\x17\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x1f\"\x1a/datasphere/v2/s3/activate:\x01*\x12\xa4\x01\n\nDeactivate\x12/.yandex.cloud.datasphere.v2.DeactivateS3Request\x1a!.yandex.cloud.operation.Operation\"B\xb2\xd2*\x17\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02!\"\x1c/datasphere/v2/s3/deactivate:\x01*Bk\n\x1eyandex.cloud.api.datasphere.v2ZIgithub.com/yandex-cloud/go-genproto/yandex/cloud/datasphere/v2;datasphereb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.datasphere.v2.s3_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036yandex.cloud.api.datasphere.v2ZIgithub.com/yandex-cloud/go-genproto/yandex/cloud/datasphere/v2;datasphere'
  _globals['_ACTIVATES3REQUEST'].fields_by_name['s3_id']._loaded_options = None
  _globals['_ACTIVATES3REQUEST'].fields_by_name['s3_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_ACTIVATES3REQUEST'].fields_by_name['project_id']._loaded_options = None
  _globals['_ACTIVATES3REQUEST'].fields_by_name['project_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_DEACTIVATES3REQUEST'].fields_by_name['s3_id']._loaded_options = None
  _globals['_DEACTIVATES3REQUEST'].fields_by_name['s3_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_DEACTIVATES3REQUEST'].fields_by_name['project_id']._loaded_options = None
  _globals['_DEACTIVATES3REQUEST'].fields_by_name['project_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_S3SERVICE'].methods_by_name['Activate']._loaded_options = None
  _globals['_S3SERVICE'].methods_by_name['Activate']._serialized_options = b'\262\322*\027\022\025google.protobuf.Empty\202\323\344\223\002\037\"\032/datasphere/v2/s3/activate:\001*'
  _globals['_S3SERVICE'].methods_by_name['Deactivate']._loaded_options = None
  _globals['_S3SERVICE'].methods_by_name['Deactivate']._serialized_options = b'\262\322*\027\022\025google.protobuf.Empty\202\323\344\223\002!\"\034/datasphere/v2/s3/deactivate:\001*'
  _globals['_ACTIVATES3REQUEST']._serialized_start=210
  _globals['_ACTIVATES3REQUEST']._serialized_end=292
  _globals['_DEACTIVATES3REQUEST']._serialized_start=294
  _globals['_DEACTIVATES3REQUEST']._serialized_end=378
  _globals['_S3SERVICE']._serialized_start=381
  _globals['_S3SERVICE']._serialized_end=720
# @@protoc_insertion_point(module_scope)
