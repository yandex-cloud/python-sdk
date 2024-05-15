# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/cdn/v1/provider_service.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*yandex/cloud/cdn/v1/provider_service.proto\x12\x13yandex.cloud.cdn.v1\x1a\x1cgoogle/api/annotations.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"_\n\x17\x41\x63tivateProviderRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12#\n\rprovider_type\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\";\n\x18\x41\x63tivateProviderMetadata\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"@\n\x1dListActivatedProvidersRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"3\n\x1eListActivatedProvidersResponse\x12\x11\n\tproviders\x18\x01 \x03(\t2\xe1\x02\n\x0fProviderService\x12\xb7\x01\n\x08\x41\x63tivate\x12,.yandex.cloud.cdn.v1.ActivateProviderRequest\x1a!.yandex.cloud.operation.Operation\"Z\xb2\xd2*1\n\x18\x41\x63tivateProviderMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x1f\"\x1a/cdn/v1/providers:activate:\x01*\x12\x93\x01\n\rListActivated\x12\x32.yandex.cloud.cdn.v1.ListActivatedProvidersRequest\x1a\x33.yandex.cloud.cdn.v1.ListActivatedProvidersResponse\"\x19\x82\xd3\xe4\x93\x02\x13\x12\x11/cdn/v1/providersBV\n\x17yandex.cloud.api.cdn.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/cdn/v1;cdnb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.cdn.v1.provider_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027yandex.cloud.api.cdn.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/cdn/v1;cdn'
  _globals['_ACTIVATEPROVIDERREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_ACTIVATEPROVIDERREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_ACTIVATEPROVIDERREQUEST'].fields_by_name['provider_type']._loaded_options = None
  _globals['_ACTIVATEPROVIDERREQUEST'].fields_by_name['provider_type']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_ACTIVATEPROVIDERMETADATA'].fields_by_name['folder_id']._loaded_options = None
  _globals['_ACTIVATEPROVIDERMETADATA'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTACTIVATEDPROVIDERSREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_LISTACTIVATEDPROVIDERSREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_PROVIDERSERVICE'].methods_by_name['Activate']._loaded_options = None
  _globals['_PROVIDERSERVICE'].methods_by_name['Activate']._serialized_options = b'\262\322*1\n\030ActivateProviderMetadata\022\025google.protobuf.Empty\202\323\344\223\002\037\"\032/cdn/v1/providers:activate:\001*'
  _globals['_PROVIDERSERVICE'].methods_by_name['ListActivated']._loaded_options = None
  _globals['_PROVIDERSERVICE'].methods_by_name['ListActivated']._serialized_options = b'\202\323\344\223\002\023\022\021/cdn/v1/providers'
  _globals['_ACTIVATEPROVIDERREQUEST']._serialized_start=202
  _globals['_ACTIVATEPROVIDERREQUEST']._serialized_end=297
  _globals['_ACTIVATEPROVIDERMETADATA']._serialized_start=299
  _globals['_ACTIVATEPROVIDERMETADATA']._serialized_end=358
  _globals['_LISTACTIVATEDPROVIDERSREQUEST']._serialized_start=360
  _globals['_LISTACTIVATEDPROVIDERSREQUEST']._serialized_end=424
  _globals['_LISTACTIVATEDPROVIDERSRESPONSE']._serialized_start=426
  _globals['_LISTACTIVATEDPROVIDERSRESPONSE']._serialized_end=477
  _globals['_PROVIDERSERVICE']._serialized_start=480
  _globals['_PROVIDERSERVICE']._serialized_end=833
# @@protoc_insertion_point(module_scope)
