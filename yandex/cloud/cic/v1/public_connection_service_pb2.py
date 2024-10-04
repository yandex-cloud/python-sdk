# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/cic/v1/public_connection_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.cic.v1 import public_connection_pb2 as yandex_dot_cloud_dot_cic_dot_v1_dot_public__connection__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3yandex/cloud/cic/v1/public_connection_service.proto\x12\x13yandex.cloud.cic.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1dyandex/cloud/validation.proto\x1a+yandex/cloud/cic/v1/public_connection.proto\"H\n\x1aGetPublicConnectionRequest\x12*\n\x14public_connection_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\x99\x01\n\x1cListPublicConnectionsRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"{\n\x1dListPublicConnectionsResponse\x12\x41\n\x12public_connections\x18\x01 \x03(\x0b\x32%.yandex.cloud.cic.v1.PublicConnection\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xc6\x02\n\x17PublicConnectionService\x12\x97\x01\n\x03Get\x12/.yandex.cloud.cic.v1.GetPublicConnectionRequest\x1a%.yandex.cloud.cic.v1.PublicConnection\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/cic/v1/publicConnections/{public_connection_id}\x12\x90\x01\n\x04List\x12\x31.yandex.cloud.cic.v1.ListPublicConnectionsRequest\x1a\x32.yandex.cloud.cic.v1.ListPublicConnectionsResponse\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/cic/v1/publicConnectionsBV\n\x17yandex.cloud.api.cic.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/cic/v1;cicb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.cic.v1.public_connection_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027yandex.cloud.api.cic.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/cic/v1;cic'
  _GETPUBLICCONNECTIONREQUEST.fields_by_name['public_connection_id']._options = None
  _GETPUBLICCONNECTIONREQUEST.fields_by_name['public_connection_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTPUBLICCONNECTIONSREQUEST.fields_by_name['folder_id']._options = None
  _LISTPUBLICCONNECTIONSREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTPUBLICCONNECTIONSREQUEST.fields_by_name['page_size']._options = None
  _LISTPUBLICCONNECTIONSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTPUBLICCONNECTIONSREQUEST.fields_by_name['page_token']._options = None
  _LISTPUBLICCONNECTIONSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _LISTPUBLICCONNECTIONSREQUEST.fields_by_name['filter']._options = None
  _LISTPUBLICCONNECTIONSREQUEST.fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _PUBLICCONNECTIONSERVICE.methods_by_name['Get']._options = None
  _PUBLICCONNECTIONSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\0022\0220/cic/v1/publicConnections/{public_connection_id}'
  _PUBLICCONNECTIONSERVICE.methods_by_name['List']._options = None
  _PUBLICCONNECTIONSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\033\022\031/cic/v1/publicConnections'
  _globals['_GETPUBLICCONNECTIONREQUEST']._serialized_start=182
  _globals['_GETPUBLICCONNECTIONREQUEST']._serialized_end=254
  _globals['_LISTPUBLICCONNECTIONSREQUEST']._serialized_start=257
  _globals['_LISTPUBLICCONNECTIONSREQUEST']._serialized_end=410
  _globals['_LISTPUBLICCONNECTIONSRESPONSE']._serialized_start=412
  _globals['_LISTPUBLICCONNECTIONSRESPONSE']._serialized_end=535
  _globals['_PUBLICCONNECTIONSERVICE']._serialized_start=538
  _globals['_PUBLICCONNECTIONSERVICE']._serialized_end=864
# @@protoc_insertion_point(module_scope)
