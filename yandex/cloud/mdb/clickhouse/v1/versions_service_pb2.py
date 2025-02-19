# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/mdb/clickhouse/v1/versions_service.proto
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
    'yandex/cloud/mdb/clickhouse/v1/versions_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.mdb.clickhouse.v1 import version_pb2 as yandex_dot_cloud_dot_mdb_dot_clickhouse_dot_v1_dot_version__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5yandex/cloud/mdb/clickhouse/v1/versions_service.proto\x12\x1eyandex.cloud.mdb.clickhouse.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1dyandex/cloud/validation.proto\x1a,yandex/cloud/mdb/clickhouse/v1/version.proto\"S\n\x13ListVersionsRequest\x12\x1d\n\tpage_size\x18\x01 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x02 \x01(\tB\t\x8a\xc8\x31\x05<=100\"i\n\x14ListVersionsResponse\x12\x38\n\x07version\x18\x01 \x03(\x0b\x32\'.yandex.cloud.mdb.clickhouse.v1.Version\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xae\x01\n\x0fVersionsService\x12\x9a\x01\n\x04List\x12\x33.yandex.cloud.mdb.clickhouse.v1.ListVersionsRequest\x1a\x34.yandex.cloud.mdb.clickhouse.v1.ListVersionsResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/managed-clickhouse/v1/versionsBs\n\"yandex.cloud.api.mdb.clickhouse.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/clickhouse/v1;clickhouseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.clickhouse.v1.versions_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"yandex.cloud.api.mdb.clickhouse.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/clickhouse/v1;clickhouse'
  _globals['_LISTVERSIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTVERSIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _globals['_LISTVERSIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTVERSIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_VERSIONSSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_VERSIONSSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002!\022\037/managed-clickhouse/v1/versions'
  _globals['_LISTVERSIONSREQUEST']._serialized_start=196
  _globals['_LISTVERSIONSREQUEST']._serialized_end=279
  _globals['_LISTVERSIONSRESPONSE']._serialized_start=281
  _globals['_LISTVERSIONSRESPONSE']._serialized_end=386
  _globals['_VERSIONSSERVICE']._serialized_start=389
  _globals['_VERSIONSSERVICE']._serialized_end=563
# @@protoc_insertion_point(module_scope)
