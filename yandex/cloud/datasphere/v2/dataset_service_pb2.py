# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/datasphere/v2/dataset_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0yandex/cloud/datasphere/v2/dataset_service.proto\x12\x1ayandex.cloud.datasphere.v2\x1a\x1cgoogle/api/annotations.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"\\\n\x16\x41\x63tivateDatasetRequest\x12 \n\ndataset_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12 \n\nproject_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"^\n\x18\x44\x65\x61\x63tivateDatasetRequest\x12 \n\ndataset_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12 \n\nproject_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=502\xec\x02\n\x0e\x44\x61tasetService\x12\xa8\x01\n\x08\x41\x63tivate\x12\x32.yandex.cloud.datasphere.v2.ActivateDatasetRequest\x1a!.yandex.cloud.operation.Operation\"E\xb2\xd2*\x17\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02$\"\x1f/datasphere/v2/dataset/activate:\x01*\x12\xae\x01\n\nDeactivate\x12\x34.yandex.cloud.datasphere.v2.DeactivateDatasetRequest\x1a!.yandex.cloud.operation.Operation\"G\xb2\xd2*\x17\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02&\"!/datasphere/v2/dataset/deactivate:\x01*Bk\n\x1eyandex.cloud.api.datasphere.v2ZIgithub.com/yandex-cloud/go-genproto/yandex/cloud/datasphere/v2;datasphereb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.datasphere.v2.dataset_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036yandex.cloud.api.datasphere.v2ZIgithub.com/yandex-cloud/go-genproto/yandex/cloud/datasphere/v2;datasphere'
  _globals['_ACTIVATEDATASETREQUEST'].fields_by_name['dataset_id']._loaded_options = None
  _globals['_ACTIVATEDATASETREQUEST'].fields_by_name['dataset_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_ACTIVATEDATASETREQUEST'].fields_by_name['project_id']._loaded_options = None
  _globals['_ACTIVATEDATASETREQUEST'].fields_by_name['project_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_DEACTIVATEDATASETREQUEST'].fields_by_name['dataset_id']._loaded_options = None
  _globals['_DEACTIVATEDATASETREQUEST'].fields_by_name['dataset_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_DEACTIVATEDATASETREQUEST'].fields_by_name['project_id']._loaded_options = None
  _globals['_DEACTIVATEDATASETREQUEST'].fields_by_name['project_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_DATASETSERVICE'].methods_by_name['Activate']._loaded_options = None
  _globals['_DATASETSERVICE'].methods_by_name['Activate']._serialized_options = b'\262\322*\027\022\025google.protobuf.Empty\202\323\344\223\002$\"\037/datasphere/v2/dataset/activate:\001*'
  _globals['_DATASETSERVICE'].methods_by_name['Deactivate']._loaded_options = None
  _globals['_DATASETSERVICE'].methods_by_name['Deactivate']._serialized_options = b'\262\322*\027\022\025google.protobuf.Empty\202\323\344\223\002&\"!/datasphere/v2/dataset/deactivate:\001*'
  _globals['_ACTIVATEDATASETREQUEST']._serialized_start=215
  _globals['_ACTIVATEDATASETREQUEST']._serialized_end=307
  _globals['_DEACTIVATEDATASETREQUEST']._serialized_start=309
  _globals['_DEACTIVATEDATASETREQUEST']._serialized_end=403
  _globals['_DATASETSERVICE']._serialized_start=406
  _globals['_DATASETSERVICE']._serialized_end=770
# @@protoc_insertion_point(module_scope)
