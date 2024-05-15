# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/organizationmanager/v1/organization_service.proto
# Protobuf Python Version: 5.26.1
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
from yandex.cloud.organizationmanager.v1 import organization_pb2 as yandex_dot_cloud_dot_organizationmanager_dot_v1_dot_organization__pb2
from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>yandex/cloud/organizationmanager/v1/organization_service.proto\x12#yandex.cloud.organizationmanager.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/api/operation.proto\x1a\x36yandex/cloud/organizationmanager/v1/organization.proto\x1a yandex/cloud/access/access.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"?\n\x16GetOrganizationRequest\x12%\n\x0forganization_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"u\n\x18ListOrganizationsRequest\x12\x1d\n\tpage_size\x18\x01 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1e\n\npage_token\x18\x02 \x01(\tB\n\x8a\xc8\x31\x06<=2000\x12\x1a\n\x06\x66ilter\x18\x03 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"~\n\x19ListOrganizationsResponse\x12H\n\rorganizations\x18\x01 \x03(\x0b\x32\x31.yandex.cloud.organizationmanager.v1.Organization\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xaa\x03\n\x19UpdateOrganizationRequest\x12%\n\x0forganization_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x32\n\x04name\x18\x03 \x01(\tB$\xf2\xc7\x31 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x18\n\x05title\x18\x05 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x97\x01\n\x06labels\x18\x06 \x03(\x0b\x32J.yandex.cloud.organizationmanager.v1.UpdateOrganizationRequest.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04\x31-63\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"5\n\x1aUpdateOrganizationMetadata\x12\x17\n\x0forganization_id\x18\x01 \x01(\t\"\x89\x01\n!ListOrganizationOperationsRequest\x12%\n\x0forganization_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1e\n\npage_token\x18\x03 \x01(\tB\n\x8a\xc8\x31\x06<=2000\"t\n\"ListOrganizationOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xa0\x0c\n\x13OrganizationService\x12\xb7\x01\n\x03Get\x12;.yandex.cloud.organizationmanager.v1.GetOrganizationRequest\x1a\x31.yandex.cloud.organizationmanager.v1.Organization\"@\x82\xd3\xe4\x93\x02:\x12\x38/organization-manager/v1/organizations/{organization_id}\x12\xb5\x01\n\x04List\x12=.yandex.cloud.organizationmanager.v1.ListOrganizationsRequest\x1a>.yandex.cloud.organizationmanager.v1.ListOrganizationsResponse\".\x82\xd3\xe4\x93\x02(\x12&/organization-manager/v1/organizations\x12\xde\x01\n\x06Update\x12>.yandex.cloud.organizationmanager.v1.UpdateOrganizationRequest\x1a!.yandex.cloud.operation.Operation\"q\xb2\xd2**\n\x1aUpdateOrganizationMetadata\x12\x0cOrganization\x82\xd3\xe4\x93\x02=28/organization-manager/v1/organizations/{organization_id}:\x01*\x12\xee\x01\n\x0eListOperations\x12\x46.yandex.cloud.organizationmanager.v1.ListOrganizationOperationsRequest\x1aG.yandex.cloud.organizationmanager.v1.ListOrganizationOperationsResponse\"K\x82\xd3\xe4\x93\x02\x45\x12\x43/organization-manager/v1/organizations/{organization_id}/operations\x12\xc6\x01\n\x12ListAccessBindings\x12..yandex.cloud.access.ListAccessBindingsRequest\x1a/.yandex.cloud.access.ListAccessBindingsResponse\"O\x82\xd3\xe4\x93\x02I\x12G/organization-manager/v1/organizations/{resource_id}:listAccessBindings\x12\xf6\x01\n\x11SetAccessBindings\x12-.yandex.cloud.access.SetAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x8e\x01\xb2\xd2*9\n access.SetAccessBindingsMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02K\"F/organization-manager/v1/organizations/{resource_id}:setAccessBindings:\x01*\x12\x82\x02\n\x14UpdateAccessBindings\x12\x30.yandex.cloud.access.UpdateAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x94\x01\xb2\xd2*<\n#access.UpdateAccessBindingsMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02N\"I/organization-manager/v1/organizations/{resource_id}:updateAccessBindings:\x01*B\x86\x01\n\'yandex.cloud.api.organizationmanager.v1Z[github.com/yandex-cloud/go-genproto/yandex/cloud/organizationmanager/v1;organizationmanagerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.organizationmanager.v1.organization_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\'yandex.cloud.api.organizationmanager.v1Z[github.com/yandex-cloud/go-genproto/yandex/cloud/organizationmanager/v1;organizationmanager'
  _globals['_GETORGANIZATIONREQUEST'].fields_by_name['organization_id']._loaded_options = None
  _globals['_GETORGANIZATIONREQUEST'].fields_by_name['organization_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTORGANIZATIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTORGANIZATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _globals['_LISTORGANIZATIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTORGANIZATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\006<=2000'
  _globals['_LISTORGANIZATIONSREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTORGANIZATIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _globals['_UPDATEORGANIZATIONREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_UPDATEORGANIZATIONREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_UPDATEORGANIZATIONREQUEST'].fields_by_name['organization_id']._loaded_options = None
  _globals['_UPDATEORGANIZATIONREQUEST'].fields_by_name['organization_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_UPDATEORGANIZATIONREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_UPDATEORGANIZATIONREQUEST'].fields_by_name['name']._serialized_options = b'\362\3071 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?'
  _globals['_UPDATEORGANIZATIONREQUEST'].fields_by_name['description']._loaded_options = None
  _globals['_UPDATEORGANIZATIONREQUEST'].fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _globals['_UPDATEORGANIZATIONREQUEST'].fields_by_name['title']._loaded_options = None
  _globals['_UPDATEORGANIZATIONREQUEST'].fields_by_name['title']._serialized_options = b'\212\3101\005<=256'
  _globals['_UPDATEORGANIZATIONREQUEST'].fields_by_name['labels']._loaded_options = None
  _globals['_UPDATEORGANIZATIONREQUEST'].fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\0041-63'
  _globals['_LISTORGANIZATIONOPERATIONSREQUEST'].fields_by_name['organization_id']._loaded_options = None
  _globals['_LISTORGANIZATIONOPERATIONSREQUEST'].fields_by_name['organization_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTORGANIZATIONOPERATIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTORGANIZATIONOPERATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _globals['_LISTORGANIZATIONOPERATIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTORGANIZATIONOPERATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\006<=2000'
  _globals['_ORGANIZATIONSERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_ORGANIZATIONSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002:\0228/organization-manager/v1/organizations/{organization_id}'
  _globals['_ORGANIZATIONSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_ORGANIZATIONSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002(\022&/organization-manager/v1/organizations'
  _globals['_ORGANIZATIONSERVICE'].methods_by_name['Update']._loaded_options = None
  _globals['_ORGANIZATIONSERVICE'].methods_by_name['Update']._serialized_options = b'\262\322**\n\032UpdateOrganizationMetadata\022\014Organization\202\323\344\223\002=28/organization-manager/v1/organizations/{organization_id}:\001*'
  _globals['_ORGANIZATIONSERVICE'].methods_by_name['ListOperations']._loaded_options = None
  _globals['_ORGANIZATIONSERVICE'].methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\002E\022C/organization-manager/v1/organizations/{organization_id}/operations'
  _globals['_ORGANIZATIONSERVICE'].methods_by_name['ListAccessBindings']._loaded_options = None
  _globals['_ORGANIZATIONSERVICE'].methods_by_name['ListAccessBindings']._serialized_options = b'\202\323\344\223\002I\022G/organization-manager/v1/organizations/{resource_id}:listAccessBindings'
  _globals['_ORGANIZATIONSERVICE'].methods_by_name['SetAccessBindings']._loaded_options = None
  _globals['_ORGANIZATIONSERVICE'].methods_by_name['SetAccessBindings']._serialized_options = b'\262\322*9\n access.SetAccessBindingsMetadata\022\025google.protobuf.Empty\202\323\344\223\002K\"F/organization-manager/v1/organizations/{resource_id}:setAccessBindings:\001*'
  _globals['_ORGANIZATIONSERVICE'].methods_by_name['UpdateAccessBindings']._loaded_options = None
  _globals['_ORGANIZATIONSERVICE'].methods_by_name['UpdateAccessBindings']._serialized_options = b'\262\322*<\n#access.UpdateAccessBindingsMetadata\022\025google.protobuf.Empty\202\323\344\223\002N\"I/organization-manager/v1/organizations/{resource_id}:updateAccessBindings:\001*'
  _globals['_GETORGANIZATIONREQUEST']._serialized_start=362
  _globals['_GETORGANIZATIONREQUEST']._serialized_end=425
  _globals['_LISTORGANIZATIONSREQUEST']._serialized_start=427
  _globals['_LISTORGANIZATIONSREQUEST']._serialized_end=544
  _globals['_LISTORGANIZATIONSRESPONSE']._serialized_start=546
  _globals['_LISTORGANIZATIONSRESPONSE']._serialized_end=672
  _globals['_UPDATEORGANIZATIONREQUEST']._serialized_start=675
  _globals['_UPDATEORGANIZATIONREQUEST']._serialized_end=1101
  _globals['_UPDATEORGANIZATIONREQUEST_LABELSENTRY']._serialized_start=1056
  _globals['_UPDATEORGANIZATIONREQUEST_LABELSENTRY']._serialized_end=1101
  _globals['_UPDATEORGANIZATIONMETADATA']._serialized_start=1103
  _globals['_UPDATEORGANIZATIONMETADATA']._serialized_end=1156
  _globals['_LISTORGANIZATIONOPERATIONSREQUEST']._serialized_start=1159
  _globals['_LISTORGANIZATIONOPERATIONSREQUEST']._serialized_end=1296
  _globals['_LISTORGANIZATIONOPERATIONSRESPONSE']._serialized_start=1298
  _globals['_LISTORGANIZATIONOPERATIONSRESPONSE']._serialized_end=1414
  _globals['_ORGANIZATIONSERVICE']._serialized_start=1417
  _globals['_ORGANIZATIONSERVICE']._serialized_end=2985
# @@protoc_insertion_point(module_scope)
