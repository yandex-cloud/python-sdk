# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/datatransfer/v1/endpoint/metrika.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.datatransfer.v1.endpoint import common_pb2 as yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3yandex/cloud/datatransfer/v1/endpoint/metrika.proto\x12%yandex.cloud.datatransfer.v1.endpoint\x1a\x32yandex/cloud/datatransfer/v1/endpoint/common.proto\"h\n\rMetrikaStream\x12\x46\n\x04type\x18\x01 \x01(\x0e\x32\x38.yandex.cloud.datatransfer.v1.endpoint.MetrikaStreamType\x12\x0f\n\x07\x63olumns\x18\x02 \x03(\t\"\xa9\x01\n\rMetrikaSource\x12\x13\n\x0b\x63ounter_ids\x18\x01 \x03(\x03\x12<\n\x05token\x18\x02 \x01(\x0b\x32-.yandex.cloud.datatransfer.v1.endpoint.Secret\x12\x45\n\x07streams\x18\x03 \x03(\x0b\x32\x34.yandex.cloud.datatransfer.v1.endpoint.MetrikaStream*\x97\x01\n\x11MetrikaStreamType\x12#\n\x1fMETRIKA_STREAM_TYPE_UNSPECIFIED\x10\x00\x12\x1c\n\x18METRIKA_STREAM_TYPE_HITS\x10\x01\x12\x1e\n\x1aMETRIKA_STREAM_TYPE_VISITS\x10\x02\x12\x1f\n\x1bMETRIKA_STREAM_TYPE_HITS_V2\x10\x03\x42\xa7\x01\n)yandex.cloud.api.datatransfer.v1.endpointZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/datatransfer/v1/endpoint;endpoint\xaa\x02%Yandex.Cloud.Datatransfer.V1.EndPointb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.datatransfer.v1.endpoint.metrika_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n)yandex.cloud.api.datatransfer.v1.endpointZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/datatransfer/v1/endpoint;endpoint\252\002%Yandex.Cloud.Datatransfer.V1.EndPoint'
  _globals['_METRIKASTREAMTYPE']._serialized_start=425
  _globals['_METRIKASTREAMTYPE']._serialized_end=576
  _globals['_METRIKASTREAM']._serialized_start=146
  _globals['_METRIKASTREAM']._serialized_end=250
  _globals['_METRIKASOURCE']._serialized_start=253
  _globals['_METRIKASOURCE']._serialized_end=422
# @@protoc_insertion_point(module_scope)
