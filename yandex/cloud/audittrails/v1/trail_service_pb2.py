# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/audittrails/v1/trail_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.audittrails.v1 import trail_pb2 as yandex_dot_cloud_dot_audittrails_dot_v1_dot_trail__pb2
from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/yandex/cloud/audittrails/v1/trail_service.proto\x12\x1byandex.cloud.audittrails.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\x1a\'yandex/cloud/audittrails/v1/trail.proto\x1a yandex/cloud/access/access.proto\"7\n\x0fGetTrailRequest\x12\x1e\n\x08trail_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50J\x04\x08\x02\x10\x03\"\x94\x01\n\x11ListTrailsRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x0e\n\x06\x66ilter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t\"a\n\x12ListTrailsResponse\x12\x32\n\x06trails\x18\x01 \x03(\x0b\x32\".yandex.cloud.audittrails.v1.Trail\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xfa\x03\n\x12\x43reateTrailRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x32\n\x04name\x18\x02 \x01(\tB$\xf2\xc7\x31 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?\x12\x1f\n\x0b\x64\x65scription\x18\x03 \x01(\tB\n\x8a\xc8\x31\x06<=1024\x12\x88\x01\n\x06labels\x18\x04 \x03(\x0b\x32;.yandex.cloud.audittrails.v1.CreateTrailRequest.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04<=63\x12I\n\x0b\x64\x65stination\x18\x05 \x01(\x0b\x32..yandex.cloud.audittrails.v1.Trail.DestinationB\x04\xe8\xc7\x31\x01\x12(\n\x12service_account_id\x18\x06 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12?\n\x06\x66ilter\x18\x07 \x01(\x0b\x32).yandex.cloud.audittrails.v1.Trail.FilterB\x04\xe8\xc7\x31\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x9a\x04\n\x12UpdateTrailRequest\x12\x1e\n\x08trail_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x32\n\x04name\x18\x03 \x01(\tB$\xf2\xc7\x31 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?\x12\x1f\n\x0b\x64\x65scription\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1024\x12\x88\x01\n\x06labels\x18\x05 \x03(\x0b\x32;.yandex.cloud.audittrails.v1.UpdateTrailRequest.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04<=63\x12\x43\n\x0b\x64\x65stination\x18\x06 \x01(\x0b\x32..yandex.cloud.audittrails.v1.Trail.Destination\x12$\n\x12service_account_id\x18\x07 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x39\n\x06\x66ilter\x18\x08 \x01(\x0b\x32).yandex.cloud.audittrails.v1.Trail.Filter\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"4\n\x12\x44\x65leteTrailRequest\x12\x1e\n\x08trail_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\'\n\x13\x43reateTrailMetadata\x12\x10\n\x08trail_id\x18\x01 \x01(\t\"\'\n\x13UpdateTrailMetadata\x12\x10\n\x08trail_id\x18\x01 \x01(\t\"\'\n\x13\x44\x65leteTrailMetadata\x12\x10\n\x08trail_id\x18\x01 \x01(\t\"z\n\x1aListTrailOperationsRequest\x12\x1e\n\x08trail_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"m\n\x1bListTrailOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\x81\r\n\x0cTrailService\x12\x83\x01\n\x03Get\x12,.yandex.cloud.audittrails.v1.GetTrailRequest\x1a\".yandex.cloud.audittrails.v1.Trail\"*\x82\xd3\xe4\x93\x02$\x12\"/audit-trails/v1/trails/{trail_id}\x12\x88\x01\n\x04List\x12..yandex.cloud.audittrails.v1.ListTrailsRequest\x1a/.yandex.cloud.audittrails.v1.ListTrailsResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/audit-trails/v1/trails\x12\xa0\x01\n\x06\x43reate\x12/.yandex.cloud.audittrails.v1.CreateTrailRequest\x1a!.yandex.cloud.operation.Operation\"B\xb2\xd2*\x1c\n\x13\x43reateTrailMetadata\x12\x05Trail\x82\xd3\xe4\x93\x02\x1c\"\x17/audit-trails/v1/trails:\x01*\x12\xab\x01\n\x06Update\x12/.yandex.cloud.audittrails.v1.UpdateTrailRequest\x1a!.yandex.cloud.operation.Operation\"M\xb2\xd2*\x1c\n\x13UpdateTrailMetadata\x12\x05Trail\x82\xd3\xe4\x93\x02\'2\"/audit-trails/v1/trails/{trail_id}:\x01*\x12\xb8\x01\n\x06\x44\x65lete\x12/.yandex.cloud.audittrails.v1.DeleteTrailRequest\x1a!.yandex.cloud.operation.Operation\"Z\xb2\xd2*,\n\x13\x44\x65leteTrailMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02$*\"/audit-trails/v1/trails/{trail_id}\x12\xba\x01\n\x0eListOperations\x12\x37.yandex.cloud.audittrails.v1.ListTrailOperationsRequest\x1a\x38.yandex.cloud.audittrails.v1.ListTrailOperationsResponse\"5\x82\xd3\xe4\x93\x02/\x12-/audit-trails/v1/trails/{trail_id}/operations\x12\xb7\x01\n\x12ListAccessBindings\x12..yandex.cloud.access.ListAccessBindingsRequest\x1a/.yandex.cloud.access.ListAccessBindingsResponse\"@\x82\xd3\xe4\x93\x02:\x12\x38/audit-trails/v1/trails/{resource_id}:listAccessBindings\x12\xe6\x01\n\x11SetAccessBindings\x12-.yandex.cloud.access.SetAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x7f\xb2\xd2*9\n access.SetAccessBindingsMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02<\"7/audit-trails/v1/trails/{resource_id}:setAccessBindings:\x01*\x12\xf3\x01\n\x14UpdateAccessBindings\x12\x30.yandex.cloud.access.UpdateAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x85\x01\xb2\xd2*<\n#access.UpdateAccessBindingsMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02?\":/audit-trails/v1/trails/{resource_id}:updateAccessBindings:\x01*Bs\n\x1fyandex.cloud.api.audittrails.v1B\x03\x41TSZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/audittrails/v1;audittrailsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.audittrails.v1.trail_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\037yandex.cloud.api.audittrails.v1B\003ATSZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/audittrails/v1;audittrails'
  _GETTRAILREQUEST.fields_by_name['trail_id']._options = None
  _GETTRAILREQUEST.fields_by_name['trail_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTTRAILSREQUEST.fields_by_name['folder_id']._options = None
  _LISTTRAILSREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTTRAILSREQUEST.fields_by_name['page_size']._options = None
  _LISTTRAILSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTTRAILSREQUEST.fields_by_name['page_token']._options = None
  _LISTTRAILSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _CREATETRAILREQUEST_LABELSENTRY._options = None
  _CREATETRAILREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _CREATETRAILREQUEST.fields_by_name['folder_id']._options = None
  _CREATETRAILREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _CREATETRAILREQUEST.fields_by_name['name']._options = None
  _CREATETRAILREQUEST.fields_by_name['name']._serialized_options = b'\362\3071 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?'
  _CREATETRAILREQUEST.fields_by_name['description']._options = None
  _CREATETRAILREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\006<=1024'
  _CREATETRAILREQUEST.fields_by_name['labels']._options = None
  _CREATETRAILREQUEST.fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\004<=63'
  _CREATETRAILREQUEST.fields_by_name['destination']._options = None
  _CREATETRAILREQUEST.fields_by_name['destination']._serialized_options = b'\350\3071\001'
  _CREATETRAILREQUEST.fields_by_name['service_account_id']._options = None
  _CREATETRAILREQUEST.fields_by_name['service_account_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _CREATETRAILREQUEST.fields_by_name['filter']._options = None
  _CREATETRAILREQUEST.fields_by_name['filter']._serialized_options = b'\350\3071\001'
  _UPDATETRAILREQUEST_LABELSENTRY._options = None
  _UPDATETRAILREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _UPDATETRAILREQUEST.fields_by_name['trail_id']._options = None
  _UPDATETRAILREQUEST.fields_by_name['trail_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _UPDATETRAILREQUEST.fields_by_name['name']._options = None
  _UPDATETRAILREQUEST.fields_by_name['name']._serialized_options = b'\362\3071 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?'
  _UPDATETRAILREQUEST.fields_by_name['description']._options = None
  _UPDATETRAILREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\006<=1024'
  _UPDATETRAILREQUEST.fields_by_name['labels']._options = None
  _UPDATETRAILREQUEST.fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\004<=63'
  _UPDATETRAILREQUEST.fields_by_name['service_account_id']._options = None
  _UPDATETRAILREQUEST.fields_by_name['service_account_id']._serialized_options = b'\212\3101\004<=50'
  _DELETETRAILREQUEST.fields_by_name['trail_id']._options = None
  _DELETETRAILREQUEST.fields_by_name['trail_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTTRAILOPERATIONSREQUEST.fields_by_name['trail_id']._options = None
  _LISTTRAILOPERATIONSREQUEST.fields_by_name['trail_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTTRAILOPERATIONSREQUEST.fields_by_name['page_size']._options = None
  _LISTTRAILOPERATIONSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTTRAILOPERATIONSREQUEST.fields_by_name['page_token']._options = None
  _LISTTRAILOPERATIONSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _TRAILSERVICE.methods_by_name['Get']._options = None
  _TRAILSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002$\022\"/audit-trails/v1/trails/{trail_id}'
  _TRAILSERVICE.methods_by_name['List']._options = None
  _TRAILSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\031\022\027/audit-trails/v1/trails'
  _TRAILSERVICE.methods_by_name['Create']._options = None
  _TRAILSERVICE.methods_by_name['Create']._serialized_options = b'\262\322*\034\n\023CreateTrailMetadata\022\005Trail\202\323\344\223\002\034\"\027/audit-trails/v1/trails:\001*'
  _TRAILSERVICE.methods_by_name['Update']._options = None
  _TRAILSERVICE.methods_by_name['Update']._serialized_options = b'\262\322*\034\n\023UpdateTrailMetadata\022\005Trail\202\323\344\223\002\'2\"/audit-trails/v1/trails/{trail_id}:\001*'
  _TRAILSERVICE.methods_by_name['Delete']._options = None
  _TRAILSERVICE.methods_by_name['Delete']._serialized_options = b'\262\322*,\n\023DeleteTrailMetadata\022\025google.protobuf.Empty\202\323\344\223\002$*\"/audit-trails/v1/trails/{trail_id}'
  _TRAILSERVICE.methods_by_name['ListOperations']._options = None
  _TRAILSERVICE.methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\002/\022-/audit-trails/v1/trails/{trail_id}/operations'
  _TRAILSERVICE.methods_by_name['ListAccessBindings']._options = None
  _TRAILSERVICE.methods_by_name['ListAccessBindings']._serialized_options = b'\202\323\344\223\002:\0228/audit-trails/v1/trails/{resource_id}:listAccessBindings'
  _TRAILSERVICE.methods_by_name['SetAccessBindings']._options = None
  _TRAILSERVICE.methods_by_name['SetAccessBindings']._serialized_options = b'\262\322*9\n access.SetAccessBindingsMetadata\022\025google.protobuf.Empty\202\323\344\223\002<\"7/audit-trails/v1/trails/{resource_id}:setAccessBindings:\001*'
  _TRAILSERVICE.methods_by_name['UpdateAccessBindings']._options = None
  _TRAILSERVICE.methods_by_name['UpdateAccessBindings']._serialized_options = b'\262\322*<\n#access.UpdateAccessBindingsMetadata\022\025google.protobuf.Empty\202\323\344\223\002?\":/audit-trails/v1/trails/{resource_id}:updateAccessBindings:\001*'
  _globals['_GETTRAILREQUEST']._serialized_start=324
  _globals['_GETTRAILREQUEST']._serialized_end=379
  _globals['_LISTTRAILSREQUEST']._serialized_start=382
  _globals['_LISTTRAILSREQUEST']._serialized_end=530
  _globals['_LISTTRAILSRESPONSE']._serialized_start=532
  _globals['_LISTTRAILSRESPONSE']._serialized_end=629
  _globals['_CREATETRAILREQUEST']._serialized_start=632
  _globals['_CREATETRAILREQUEST']._serialized_end=1138
  _globals['_CREATETRAILREQUEST_LABELSENTRY']._serialized_start=1093
  _globals['_CREATETRAILREQUEST_LABELSENTRY']._serialized_end=1138
  _globals['_UPDATETRAILREQUEST']._serialized_start=1141
  _globals['_UPDATETRAILREQUEST']._serialized_end=1679
  _globals['_UPDATETRAILREQUEST_LABELSENTRY']._serialized_start=1093
  _globals['_UPDATETRAILREQUEST_LABELSENTRY']._serialized_end=1138
  _globals['_DELETETRAILREQUEST']._serialized_start=1681
  _globals['_DELETETRAILREQUEST']._serialized_end=1733
  _globals['_CREATETRAILMETADATA']._serialized_start=1735
  _globals['_CREATETRAILMETADATA']._serialized_end=1774
  _globals['_UPDATETRAILMETADATA']._serialized_start=1776
  _globals['_UPDATETRAILMETADATA']._serialized_end=1815
  _globals['_DELETETRAILMETADATA']._serialized_start=1817
  _globals['_DELETETRAILMETADATA']._serialized_end=1856
  _globals['_LISTTRAILOPERATIONSREQUEST']._serialized_start=1858
  _globals['_LISTTRAILOPERATIONSREQUEST']._serialized_end=1980
  _globals['_LISTTRAILOPERATIONSRESPONSE']._serialized_start=1982
  _globals['_LISTTRAILOPERATIONSRESPONSE']._serialized_end=2091
  _globals['_TRAILSERVICE']._serialized_start=2094
  _globals['_TRAILSERVICE']._serialized_end=3759
# @@protoc_insertion_point(module_scope)
