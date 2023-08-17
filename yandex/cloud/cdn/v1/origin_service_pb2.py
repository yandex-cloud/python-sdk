# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/cdn/v1/origin_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.cdn.v1 import origin_pb2 as yandex_dot_cloud_dot_cdn_dot_v1_dot_origin__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(yandex/cloud/cdn/v1/origin_service.proto\x12\x13yandex.cloud.cdn.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a yandex/cloud/api/operation.proto\x1a yandex/cloud/cdn/v1/origin.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"N\n\x10GetOriginRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x19\n\torigin_id\x18\x02 \x01(\x03\x42\x06\xfa\xc7\x31\x02>0\"V\n\x12ListOriginsRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1f\n\x0forigin_group_id\x18\x02 \x01(\x03\x42\x06\xfa\xc7\x31\x02>0\"C\n\x13ListOriginsResponse\x12,\n\x07origins\x18\x01 \x03(\x0b\x32\x1b.yandex.cloud.cdn.v1.Origin\"\xfd\x01\n\x13\x43reateOriginRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1f\n\x0forigin_group_id\x18\x02 \x01(\x03\x42\x06\xfa\xc7\x31\x02>0\x12\x1c\n\x06source\x18\x03 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12+\n\x07\x65nabled\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12*\n\x06\x62\x61\x63kup\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12-\n\x04meta\x18\x06 \x01(\x0b\x32\x1f.yandex.cloud.cdn.v1.OriginMeta\"R\n\x14\x43reateOriginMetadata\x12\x19\n\torigin_id\x18\x01 \x01(\x03\x42\x06\xfa\xc7\x31\x02>0\x12\x1f\n\x0forigin_group_id\x18\x02 \x01(\x03\x42\x06\xfa\xc7\x31\x02>0\"\xb1\x01\n\x13UpdateOriginRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x19\n\torigin_id\x18\x02 \x01(\x03\x42\x06\xfa\xc7\x31\x02>0\x12\x0e\n\x06source\x18\x03 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x04 \x01(\x08\x12\x0e\n\x06\x62\x61\x63kup\x18\x05 \x01(\x08\x12-\n\x04meta\x18\x06 \x01(\x0b\x32\x1f.yandex.cloud.cdn.v1.OriginMeta\"R\n\x14UpdateOriginMetadata\x12\x19\n\torigin_id\x18\x01 \x01(\x03\x42\x06\xfa\xc7\x31\x02>0\x12\x1f\n\x0forigin_group_id\x18\x02 \x01(\x03\x42\x06\xfa\xc7\x31\x02>0\"Q\n\x13\x44\x65leteOriginRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x19\n\torigin_id\x18\x02 \x01(\x03\x42\x06\xfa\xc7\x31\x02>0\"1\n\x14\x44\x65leteOriginMetadata\x12\x19\n\torigin_id\x18\x01 \x01(\x03\x42\x06\xfa\xc7\x31\x02>02\xd9\x05\n\rOriginService\x12n\n\x03Get\x12%.yandex.cloud.cdn.v1.GetOriginRequest\x1a\x1b.yandex.cloud.cdn.v1.Origin\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cdn/v1/origins/{origin_id}\x12r\n\x04List\x12\'.yandex.cloud.cdn.v1.ListOriginsRequest\x1a(.yandex.cloud.cdn.v1.ListOriginsResponse\"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0f/cdn/v1/origins\x12\x93\x01\n\x06\x43reate\x12(.yandex.cloud.cdn.v1.CreateOriginRequest\x1a!.yandex.cloud.operation.Operation\"<\xb2\xd2*\x1e\n\x14\x43reateOriginMetadata\x12\x06Origin\x82\xd3\xe4\x93\x02\x14\"\x0f/cdn/v1/origins:\x01*\x12\x9f\x01\n\x06Update\x12(.yandex.cloud.cdn.v1.UpdateOriginRequest\x1a!.yandex.cloud.operation.Operation\"H\xb2\xd2*\x1e\n\x14UpdateOriginMetadata\x12\x06Origin\x82\xd3\xe4\x93\x02 2\x1b/cdn/v1/origins/{origin_id}:\x01*\x12\xab\x01\n\x06\x44\x65lete\x12(.yandex.cloud.cdn.v1.DeleteOriginRequest\x1a!.yandex.cloud.operation.Operation\"T\xb2\xd2*-\n\x14\x44\x65leteOriginMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x1d*\x1b/cdn/v1/origins/{origin_id}BV\n\x17yandex.cloud.api.cdn.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/cdn/v1;cdnb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.cdn.v1.origin_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027yandex.cloud.api.cdn.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/cdn/v1;cdn'
  _GETORIGINREQUEST.fields_by_name['folder_id']._options = None
  _GETORIGINREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _GETORIGINREQUEST.fields_by_name['origin_id']._options = None
  _GETORIGINREQUEST.fields_by_name['origin_id']._serialized_options = b'\372\3071\002>0'
  _LISTORIGINSREQUEST.fields_by_name['folder_id']._options = None
  _LISTORIGINSREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTORIGINSREQUEST.fields_by_name['origin_group_id']._options = None
  _LISTORIGINSREQUEST.fields_by_name['origin_group_id']._serialized_options = b'\372\3071\002>0'
  _CREATEORIGINREQUEST.fields_by_name['folder_id']._options = None
  _CREATEORIGINREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _CREATEORIGINREQUEST.fields_by_name['origin_group_id']._options = None
  _CREATEORIGINREQUEST.fields_by_name['origin_group_id']._serialized_options = b'\372\3071\002>0'
  _CREATEORIGINREQUEST.fields_by_name['source']._options = None
  _CREATEORIGINREQUEST.fields_by_name['source']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _CREATEORIGINMETADATA.fields_by_name['origin_id']._options = None
  _CREATEORIGINMETADATA.fields_by_name['origin_id']._serialized_options = b'\372\3071\002>0'
  _CREATEORIGINMETADATA.fields_by_name['origin_group_id']._options = None
  _CREATEORIGINMETADATA.fields_by_name['origin_group_id']._serialized_options = b'\372\3071\002>0'
  _UPDATEORIGINREQUEST.fields_by_name['folder_id']._options = None
  _UPDATEORIGINREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _UPDATEORIGINREQUEST.fields_by_name['origin_id']._options = None
  _UPDATEORIGINREQUEST.fields_by_name['origin_id']._serialized_options = b'\372\3071\002>0'
  _UPDATEORIGINMETADATA.fields_by_name['origin_id']._options = None
  _UPDATEORIGINMETADATA.fields_by_name['origin_id']._serialized_options = b'\372\3071\002>0'
  _UPDATEORIGINMETADATA.fields_by_name['origin_group_id']._options = None
  _UPDATEORIGINMETADATA.fields_by_name['origin_group_id']._serialized_options = b'\372\3071\002>0'
  _DELETEORIGINREQUEST.fields_by_name['folder_id']._options = None
  _DELETEORIGINREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _DELETEORIGINREQUEST.fields_by_name['origin_id']._options = None
  _DELETEORIGINREQUEST.fields_by_name['origin_id']._serialized_options = b'\372\3071\002>0'
  _DELETEORIGINMETADATA.fields_by_name['origin_id']._options = None
  _DELETEORIGINMETADATA.fields_by_name['origin_id']._serialized_options = b'\372\3071\002>0'
  _ORIGINSERVICE.methods_by_name['Get']._options = None
  _ORIGINSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\035\022\033/cdn/v1/origins/{origin_id}'
  _ORIGINSERVICE.methods_by_name['List']._options = None
  _ORIGINSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\021\022\017/cdn/v1/origins'
  _ORIGINSERVICE.methods_by_name['Create']._options = None
  _ORIGINSERVICE.methods_by_name['Create']._serialized_options = b'\262\322*\036\n\024CreateOriginMetadata\022\006Origin\202\323\344\223\002\024\"\017/cdn/v1/origins:\001*'
  _ORIGINSERVICE.methods_by_name['Update']._options = None
  _ORIGINSERVICE.methods_by_name['Update']._serialized_options = b'\262\322*\036\n\024UpdateOriginMetadata\022\006Origin\202\323\344\223\002 2\033/cdn/v1/origins/{origin_id}:\001*'
  _ORIGINSERVICE.methods_by_name['Delete']._options = None
  _ORIGINSERVICE.methods_by_name['Delete']._serialized_options = b'\262\322*-\n\024DeleteOriginMetadata\022\025google.protobuf.Empty\202\323\344\223\002\035*\033/cdn/v1/origins/{origin_id}'
  _globals['_GETORIGINREQUEST']._serialized_start=266
  _globals['_GETORIGINREQUEST']._serialized_end=344
  _globals['_LISTORIGINSREQUEST']._serialized_start=346
  _globals['_LISTORIGINSREQUEST']._serialized_end=432
  _globals['_LISTORIGINSRESPONSE']._serialized_start=434
  _globals['_LISTORIGINSRESPONSE']._serialized_end=501
  _globals['_CREATEORIGINREQUEST']._serialized_start=504
  _globals['_CREATEORIGINREQUEST']._serialized_end=757
  _globals['_CREATEORIGINMETADATA']._serialized_start=759
  _globals['_CREATEORIGINMETADATA']._serialized_end=841
  _globals['_UPDATEORIGINREQUEST']._serialized_start=844
  _globals['_UPDATEORIGINREQUEST']._serialized_end=1021
  _globals['_UPDATEORIGINMETADATA']._serialized_start=1023
  _globals['_UPDATEORIGINMETADATA']._serialized_end=1105
  _globals['_DELETEORIGINREQUEST']._serialized_start=1107
  _globals['_DELETEORIGINREQUEST']._serialized_end=1188
  _globals['_DELETEORIGINMETADATA']._serialized_start=1190
  _globals['_DELETEORIGINMETADATA']._serialized_end=1239
  _globals['_ORIGINSERVICE']._serialized_start=1242
  _globals['_ORIGINSERVICE']._serialized_end=1971
# @@protoc_insertion_point(module_scope)
