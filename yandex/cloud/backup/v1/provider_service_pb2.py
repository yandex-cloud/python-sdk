# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/backup/v1/provider_service.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-yandex/cloud/backup/v1/provider_service.proto\x12\x16yandex.cloud.backup.v1\x1a\x1cgoogle/api/annotations.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"T\n\x17\x41\x63tivateProviderRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x12\n\x04name\x18\x03 \x01(\tB\x04\xe8\xc7\x31\x01J\x04\x08\x02\x10\x03\";\n\x18\x41\x63tivateProviderMetadata\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"@\n\x1dListActivatedProvidersRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"H\n\x1eListActivatedProvidersResponse\x12\x11\n\tfolder_id\x18\x01 \x01(\t\x12\r\n\x05names\x18\x03 \x03(\tJ\x04\x08\x02\x10\x03\x32\xf7\x02\n\x0fProviderService\x12\xc4\x01\n\x08\x41\x63tivate\x12/.yandex.cloud.backup.v1.ActivateProviderRequest\x1a!.yandex.cloud.operation.Operation\"d\xb2\xd2*1\n\x18\x41\x63tivateProviderMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02)\"$/backup/v1/providers/{name}:activate:\x01*\x12\x9c\x01\n\rListActivated\x12\x35.yandex.cloud.backup.v1.ListActivatedProvidersRequest\x1a\x36.yandex.cloud.backup.v1.ListActivatedProvidersResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/backup/v1/providersB_\n\x1ayandex.cloud.api.backup.v1ZAgithub.com/yandex-cloud/go-genproto/yandex/cloud/backup/v1;backupb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.backup.v1.provider_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032yandex.cloud.api.backup.v1ZAgithub.com/yandex-cloud/go-genproto/yandex/cloud/backup/v1;backup'
  _globals['_ACTIVATEPROVIDERREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_ACTIVATEPROVIDERREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_ACTIVATEPROVIDERREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_ACTIVATEPROVIDERREQUEST'].fields_by_name['name']._serialized_options = b'\350\3071\001'
  _globals['_ACTIVATEPROVIDERMETADATA'].fields_by_name['folder_id']._loaded_options = None
  _globals['_ACTIVATEPROVIDERMETADATA'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTACTIVATEDPROVIDERSREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_LISTACTIVATEDPROVIDERSREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_PROVIDERSERVICE'].methods_by_name['Activate']._loaded_options = None
  _globals['_PROVIDERSERVICE'].methods_by_name['Activate']._serialized_options = b'\262\322*1\n\030ActivateProviderMetadata\022\025google.protobuf.Empty\202\323\344\223\002)\"$/backup/v1/providers/{name}:activate:\001*'
  _globals['_PROVIDERSERVICE'].methods_by_name['ListActivated']._loaded_options = None
  _globals['_PROVIDERSERVICE'].methods_by_name['ListActivated']._serialized_options = b'\202\323\344\223\002\026\022\024/backup/v1/providers'
  _globals['_ACTIVATEPROVIDERREQUEST']._serialized_start=208
  _globals['_ACTIVATEPROVIDERREQUEST']._serialized_end=292
  _globals['_ACTIVATEPROVIDERMETADATA']._serialized_start=294
  _globals['_ACTIVATEPROVIDERMETADATA']._serialized_end=353
  _globals['_LISTACTIVATEDPROVIDERSREQUEST']._serialized_start=355
  _globals['_LISTACTIVATEDPROVIDERSREQUEST']._serialized_end=419
  _globals['_LISTACTIVATEDPROVIDERSRESPONSE']._serialized_start=421
  _globals['_LISTACTIVATEDPROVIDERSRESPONSE']._serialized_end=493
  _globals['_PROVIDERSERVICE']._serialized_start=496
  _globals['_PROVIDERSERVICE']._serialized_end=871
# @@protoc_insertion_point(module_scope)
