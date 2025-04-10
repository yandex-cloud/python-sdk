# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/cdn/v1/cache_service.proto
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
    'yandex/cloud/cdn/v1/cache_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'yandex/cloud/cdn/v1/cache_service.proto\x12\x13yandex.cloud.cdn.v1\x1a\x1cgoogle/api/annotations.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"E\n\x11PurgeCacheRequest\x12!\n\x0bresource_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\r\n\x05paths\x18\x02 \x03(\t\"7\n\x12PurgeCacheMetadata\x12!\n\x0bresource_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"H\n\x14PrefetchCacheRequest\x12!\n\x0bresource_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\r\n\x05paths\x18\x02 \x03(\t\":\n\x15PrefetchCacheMetadata\x12!\n\x0bresource_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=502\xfe\x02\n\x0c\x43\x61\x63heService\x12\xaf\x01\n\x05Purge\x12&.yandex.cloud.cdn.v1.PurgeCacheRequest\x1a!.yandex.cloud.operation.Operation\"[\xb2\xd2*+\n\x12PurgeCacheMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02&\"!/cdn/v1/cache/{resource_id}:purge:\x01*\x12\xbb\x01\n\x08Prefetch\x12).yandex.cloud.cdn.v1.PrefetchCacheRequest\x1a!.yandex.cloud.operation.Operation\"a\xb2\xd2*.\n\x15PrefetchCacheMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02)\"$/cdn/v1/cache/{resource_id}:prefetch:\x01*BV\n\x17yandex.cloud.api.cdn.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/cdn/v1;cdnb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.cdn.v1.cache_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027yandex.cloud.api.cdn.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/cdn/v1;cdn'
  _globals['_PURGECACHEREQUEST'].fields_by_name['resource_id']._loaded_options = None
  _globals['_PURGECACHEREQUEST'].fields_by_name['resource_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_PURGECACHEMETADATA'].fields_by_name['resource_id']._loaded_options = None
  _globals['_PURGECACHEMETADATA'].fields_by_name['resource_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_PREFETCHCACHEREQUEST'].fields_by_name['resource_id']._loaded_options = None
  _globals['_PREFETCHCACHEREQUEST'].fields_by_name['resource_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_PREFETCHCACHEMETADATA'].fields_by_name['resource_id']._loaded_options = None
  _globals['_PREFETCHCACHEMETADATA'].fields_by_name['resource_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_CACHESERVICE'].methods_by_name['Purge']._loaded_options = None
  _globals['_CACHESERVICE'].methods_by_name['Purge']._serialized_options = b'\262\322*+\n\022PurgeCacheMetadata\022\025google.protobuf.Empty\202\323\344\223\002&\"!/cdn/v1/cache/{resource_id}:purge:\001*'
  _globals['_CACHESERVICE'].methods_by_name['Prefetch']._loaded_options = None
  _globals['_CACHESERVICE'].methods_by_name['Prefetch']._serialized_options = b'\262\322*.\n\025PrefetchCacheMetadata\022\025google.protobuf.Empty\202\323\344\223\002)\"$/cdn/v1/cache/{resource_id}:prefetch:\001*'
  _globals['_PURGECACHEREQUEST']._serialized_start=199
  _globals['_PURGECACHEREQUEST']._serialized_end=268
  _globals['_PURGECACHEMETADATA']._serialized_start=270
  _globals['_PURGECACHEMETADATA']._serialized_end=325
  _globals['_PREFETCHCACHEREQUEST']._serialized_start=327
  _globals['_PREFETCHCACHEREQUEST']._serialized_end=399
  _globals['_PREFETCHCACHEMETADATA']._serialized_start=401
  _globals['_PREFETCHCACHEMETADATA']._serialized_end=459
  _globals['_CACHESERVICE']._serialized_start=462
  _globals['_CACHESERVICE']._serialized_end=844
# @@protoc_insertion_point(module_scope)
