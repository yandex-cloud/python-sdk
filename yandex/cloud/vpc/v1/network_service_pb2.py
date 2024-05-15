# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/vpc/v1/network_service.proto
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
from yandex.cloud.vpc.v1 import network_pb2 as yandex_dot_cloud_dot_vpc_dot_v1_dot_network__pb2
from yandex.cloud.vpc.v1 import subnet_pb2 as yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__pb2
from yandex.cloud.vpc.v1 import security_group_pb2 as yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__pb2
from yandex.cloud.vpc.v1 import route_table_pb2 as yandex_dot_cloud_dot_vpc_dot_v1_dot_route__table__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)yandex/cloud/vpc/v1/network_service.proto\x12\x13yandex.cloud.vpc.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/api/operation.proto\x1a!yandex/cloud/vpc/v1/network.proto\x1a yandex/cloud/vpc/v1/subnet.proto\x1a(yandex/cloud/vpc/v1/security_group.proto\x1a%yandex/cloud/vpc/v1/route_table.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"5\n\x11GetNetworkRequest\x12 \n\nnetwork_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\x90\x01\n\x13ListNetworksRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"_\n\x14ListNetworksResponse\x12.\n\x08networks\x18\x01 \x03(\x0b\x32\x1c.yandex.cloud.vpc.v1.Network\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xc9\x02\n\x14\x43reateNetworkRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12<\n\x04name\x18\x02 \x01(\tB.\xf2\xc7\x31*|[a-zA-Z]([-_a-zA-Z0-9]{0,61}[a-zA-Z0-9])?\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x82\x01\n\x06labels\x18\x04 \x03(\x0b\x32\x35.yandex.cloud.vpc.v1.CreateNetworkRequest.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04\x31-63\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"+\n\x15\x43reateNetworkMetadata\x12\x12\n\nnetwork_id\x18\x01 \x01(\t\"\xfb\x02\n\x14UpdateNetworkRequest\x12 \n\nnetwork_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12<\n\x04name\x18\x03 \x01(\tB.\xf2\xc7\x31*|[a-zA-Z]([-_a-zA-Z0-9]{0,61}[a-zA-Z0-9])?\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x82\x01\n\x06labels\x18\x05 \x03(\x0b\x32\x35.yandex.cloud.vpc.v1.UpdateNetworkRequest.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04\x31-63\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"+\n\x15UpdateNetworkMetadata\x12\x12\n\nnetwork_id\x18\x01 \x01(\t\"8\n\x14\x44\x65leteNetworkRequest\x12 \n\nnetwork_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"+\n\x15\x44\x65leteNetworkMetadata\x12\x12\n\nnetwork_id\x18\x01 \x01(\t\"{\n\x19ListNetworkSubnetsRequest\x12 \n\nnetwork_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"c\n\x1aListNetworkSubnetsResponse\x12,\n\x07subnets\x18\x01 \x03(\x0b\x32\x1b.yandex.cloud.vpc.v1.Subnet\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x82\x01\n ListNetworkSecurityGroupsRequest\x12 \n\nnetwork_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"y\n!ListNetworkSecurityGroupsResponse\x12;\n\x0fsecurity_groups\x18\x01 \x03(\x0b\x32\".yandex.cloud.vpc.v1.SecurityGroup\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x7f\n\x1dListNetworkRouteTablesRequest\x12 \n\nnetwork_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"p\n\x1eListNetworkRouteTablesResponse\x12\x35\n\x0croute_tables\x18\x01 \x03(\x0b\x32\x1f.yandex.cloud.vpc.v1.RouteTable\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"~\n\x1cListNetworkOperationsRequest\x12 \n\nnetwork_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"o\n\x1dListNetworkOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"c\n\x12MoveNetworkRequest\x12 \n\nnetwork_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12+\n\x15\x64\x65stination_folder_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\")\n\x13MoveNetworkMetadata\x12\x12\n\nnetwork_id\x18\x01 \x01(\t2\xce\x0c\n\x0eNetworkService\x12r\n\x03Get\x12&.yandex.cloud.vpc.v1.GetNetworkRequest\x1a\x1c.yandex.cloud.vpc.v1.Network\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/vpc/v1/networks/{network_id}\x12u\n\x04List\x12(.yandex.cloud.vpc.v1.ListNetworksRequest\x1a).yandex.cloud.vpc.v1.ListNetworksResponse\"\x18\x82\xd3\xe4\x93\x02\x12\x12\x10/vpc/v1/networks\x12\x97\x01\n\x06\x43reate\x12).yandex.cloud.vpc.v1.CreateNetworkRequest\x1a!.yandex.cloud.operation.Operation\"?\xb2\xd2* \n\x15\x43reateNetworkMetadata\x12\x07Network\x82\xd3\xe4\x93\x02\x15\"\x10/vpc/v1/networks:\x01*\x12\xa4\x01\n\x06Update\x12).yandex.cloud.vpc.v1.UpdateNetworkRequest\x1a!.yandex.cloud.operation.Operation\"L\xb2\xd2* \n\x15UpdateNetworkMetadata\x12\x07Network\x82\xd3\xe4\x93\x02\"2\x1d/vpc/v1/networks/{network_id}:\x01*\x12\xaf\x01\n\x06\x44\x65lete\x12).yandex.cloud.vpc.v1.DeleteNetworkRequest\x1a!.yandex.cloud.operation.Operation\"W\xb2\xd2*.\n\x15\x44\x65leteNetworkMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x1f*\x1d/vpc/v1/networks/{network_id}\x12\x9d\x01\n\x0bListSubnets\x12..yandex.cloud.vpc.v1.ListNetworkSubnetsRequest\x1a/.yandex.cloud.vpc.v1.ListNetworkSubnetsResponse\"-\x82\xd3\xe4\x93\x02\'\x12%/vpc/v1/networks/{network_id}/subnets\x12\xba\x01\n\x12ListSecurityGroups\x12\x35.yandex.cloud.vpc.v1.ListNetworkSecurityGroupsRequest\x1a\x36.yandex.cloud.vpc.v1.ListNetworkSecurityGroupsResponse\"5\x82\xd3\xe4\x93\x02/\x12-/vpc/v1/networks/{network_id}/security_groups\x12\xae\x01\n\x0fListRouteTables\x12\x32.yandex.cloud.vpc.v1.ListNetworkRouteTablesRequest\x1a\x33.yandex.cloud.vpc.v1.ListNetworkRouteTablesResponse\"2\x82\xd3\xe4\x93\x02,\x12*/vpc/v1/networks/{network_id}/route_tables\x12\xa9\x01\n\x0eListOperations\x12\x31.yandex.cloud.vpc.v1.ListNetworkOperationsRequest\x1a\x32.yandex.cloud.vpc.v1.ListNetworkOperationsResponse\"0\x82\xd3\xe4\x93\x02*\x12(/vpc/v1/networks/{network_id}/operations\x12\xa3\x01\n\x04Move\x12\'.yandex.cloud.vpc.v1.MoveNetworkRequest\x1a!.yandex.cloud.operation.Operation\"O\xb2\xd2*\x1e\n\x13MoveNetworkMetadata\x12\x07Network\x82\xd3\xe4\x93\x02\'\"\"/vpc/v1/networks/{network_id}:move:\x01*BV\n\x17yandex.cloud.api.vpc.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/vpc/v1;vpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.vpc.v1.network_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027yandex.cloud.api.vpc.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/vpc/v1;vpc'
  _globals['_GETNETWORKREQUEST'].fields_by_name['network_id']._loaded_options = None
  _globals['_GETNETWORKREQUEST'].fields_by_name['network_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTNETWORKSREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_LISTNETWORKSREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTNETWORKSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTNETWORKSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTNETWORKSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTNETWORKSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTNETWORKSREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTNETWORKSREQUEST'].fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _globals['_CREATENETWORKREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_CREATENETWORKREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_CREATENETWORKREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_CREATENETWORKREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_CREATENETWORKREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_CREATENETWORKREQUEST'].fields_by_name['name']._serialized_options = b'\362\3071*|[a-zA-Z]([-_a-zA-Z0-9]{0,61}[a-zA-Z0-9])?'
  _globals['_CREATENETWORKREQUEST'].fields_by_name['description']._loaded_options = None
  _globals['_CREATENETWORKREQUEST'].fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _globals['_CREATENETWORKREQUEST'].fields_by_name['labels']._loaded_options = None
  _globals['_CREATENETWORKREQUEST'].fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\0041-63'
  _globals['_UPDATENETWORKREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_UPDATENETWORKREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_UPDATENETWORKREQUEST'].fields_by_name['network_id']._loaded_options = None
  _globals['_UPDATENETWORKREQUEST'].fields_by_name['network_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_UPDATENETWORKREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_UPDATENETWORKREQUEST'].fields_by_name['name']._serialized_options = b'\362\3071*|[a-zA-Z]([-_a-zA-Z0-9]{0,61}[a-zA-Z0-9])?'
  _globals['_UPDATENETWORKREQUEST'].fields_by_name['description']._loaded_options = None
  _globals['_UPDATENETWORKREQUEST'].fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _globals['_UPDATENETWORKREQUEST'].fields_by_name['labels']._loaded_options = None
  _globals['_UPDATENETWORKREQUEST'].fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\0041-63'
  _globals['_DELETENETWORKREQUEST'].fields_by_name['network_id']._loaded_options = None
  _globals['_DELETENETWORKREQUEST'].fields_by_name['network_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTNETWORKSUBNETSREQUEST'].fields_by_name['network_id']._loaded_options = None
  _globals['_LISTNETWORKSUBNETSREQUEST'].fields_by_name['network_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTNETWORKSUBNETSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTNETWORKSUBNETSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTNETWORKSUBNETSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTNETWORKSUBNETSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTNETWORKSECURITYGROUPSREQUEST'].fields_by_name['network_id']._loaded_options = None
  _globals['_LISTNETWORKSECURITYGROUPSREQUEST'].fields_by_name['network_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTNETWORKSECURITYGROUPSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTNETWORKSECURITYGROUPSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTNETWORKSECURITYGROUPSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTNETWORKSECURITYGROUPSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTNETWORKROUTETABLESREQUEST'].fields_by_name['network_id']._loaded_options = None
  _globals['_LISTNETWORKROUTETABLESREQUEST'].fields_by_name['network_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTNETWORKROUTETABLESREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTNETWORKROUTETABLESREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTNETWORKROUTETABLESREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTNETWORKROUTETABLESREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTNETWORKOPERATIONSREQUEST'].fields_by_name['network_id']._loaded_options = None
  _globals['_LISTNETWORKOPERATIONSREQUEST'].fields_by_name['network_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTNETWORKOPERATIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTNETWORKOPERATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTNETWORKOPERATIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTNETWORKOPERATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_MOVENETWORKREQUEST'].fields_by_name['network_id']._loaded_options = None
  _globals['_MOVENETWORKREQUEST'].fields_by_name['network_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_MOVENETWORKREQUEST'].fields_by_name['destination_folder_id']._loaded_options = None
  _globals['_MOVENETWORKREQUEST'].fields_by_name['destination_folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_NETWORKSERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_NETWORKSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\037\022\035/vpc/v1/networks/{network_id}'
  _globals['_NETWORKSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_NETWORKSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002\022\022\020/vpc/v1/networks'
  _globals['_NETWORKSERVICE'].methods_by_name['Create']._loaded_options = None
  _globals['_NETWORKSERVICE'].methods_by_name['Create']._serialized_options = b'\262\322* \n\025CreateNetworkMetadata\022\007Network\202\323\344\223\002\025\"\020/vpc/v1/networks:\001*'
  _globals['_NETWORKSERVICE'].methods_by_name['Update']._loaded_options = None
  _globals['_NETWORKSERVICE'].methods_by_name['Update']._serialized_options = b'\262\322* \n\025UpdateNetworkMetadata\022\007Network\202\323\344\223\002\"2\035/vpc/v1/networks/{network_id}:\001*'
  _globals['_NETWORKSERVICE'].methods_by_name['Delete']._loaded_options = None
  _globals['_NETWORKSERVICE'].methods_by_name['Delete']._serialized_options = b'\262\322*.\n\025DeleteNetworkMetadata\022\025google.protobuf.Empty\202\323\344\223\002\037*\035/vpc/v1/networks/{network_id}'
  _globals['_NETWORKSERVICE'].methods_by_name['ListSubnets']._loaded_options = None
  _globals['_NETWORKSERVICE'].methods_by_name['ListSubnets']._serialized_options = b'\202\323\344\223\002\'\022%/vpc/v1/networks/{network_id}/subnets'
  _globals['_NETWORKSERVICE'].methods_by_name['ListSecurityGroups']._loaded_options = None
  _globals['_NETWORKSERVICE'].methods_by_name['ListSecurityGroups']._serialized_options = b'\202\323\344\223\002/\022-/vpc/v1/networks/{network_id}/security_groups'
  _globals['_NETWORKSERVICE'].methods_by_name['ListRouteTables']._loaded_options = None
  _globals['_NETWORKSERVICE'].methods_by_name['ListRouteTables']._serialized_options = b'\202\323\344\223\002,\022*/vpc/v1/networks/{network_id}/route_tables'
  _globals['_NETWORKSERVICE'].methods_by_name['ListOperations']._loaded_options = None
  _globals['_NETWORKSERVICE'].methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\002*\022(/vpc/v1/networks/{network_id}/operations'
  _globals['_NETWORKSERVICE'].methods_by_name['Move']._loaded_options = None
  _globals['_NETWORKSERVICE'].methods_by_name['Move']._serialized_options = b'\262\322*\036\n\023MoveNetworkMetadata\022\007Network\202\323\344\223\002\'\"\"/vpc/v1/networks/{network_id}:move:\001*'
  _globals['_GETNETWORKREQUEST']._serialized_start=385
  _globals['_GETNETWORKREQUEST']._serialized_end=438
  _globals['_LISTNETWORKSREQUEST']._serialized_start=441
  _globals['_LISTNETWORKSREQUEST']._serialized_end=585
  _globals['_LISTNETWORKSRESPONSE']._serialized_start=587
  _globals['_LISTNETWORKSRESPONSE']._serialized_end=682
  _globals['_CREATENETWORKREQUEST']._serialized_start=685
  _globals['_CREATENETWORKREQUEST']._serialized_end=1014
  _globals['_CREATENETWORKREQUEST_LABELSENTRY']._serialized_start=969
  _globals['_CREATENETWORKREQUEST_LABELSENTRY']._serialized_end=1014
  _globals['_CREATENETWORKMETADATA']._serialized_start=1016
  _globals['_CREATENETWORKMETADATA']._serialized_end=1059
  _globals['_UPDATENETWORKREQUEST']._serialized_start=1062
  _globals['_UPDATENETWORKREQUEST']._serialized_end=1441
  _globals['_UPDATENETWORKREQUEST_LABELSENTRY']._serialized_start=969
  _globals['_UPDATENETWORKREQUEST_LABELSENTRY']._serialized_end=1014
  _globals['_UPDATENETWORKMETADATA']._serialized_start=1443
  _globals['_UPDATENETWORKMETADATA']._serialized_end=1486
  _globals['_DELETENETWORKREQUEST']._serialized_start=1488
  _globals['_DELETENETWORKREQUEST']._serialized_end=1544
  _globals['_DELETENETWORKMETADATA']._serialized_start=1546
  _globals['_DELETENETWORKMETADATA']._serialized_end=1589
  _globals['_LISTNETWORKSUBNETSREQUEST']._serialized_start=1591
  _globals['_LISTNETWORKSUBNETSREQUEST']._serialized_end=1714
  _globals['_LISTNETWORKSUBNETSRESPONSE']._serialized_start=1716
  _globals['_LISTNETWORKSUBNETSRESPONSE']._serialized_end=1815
  _globals['_LISTNETWORKSECURITYGROUPSREQUEST']._serialized_start=1818
  _globals['_LISTNETWORKSECURITYGROUPSREQUEST']._serialized_end=1948
  _globals['_LISTNETWORKSECURITYGROUPSRESPONSE']._serialized_start=1950
  _globals['_LISTNETWORKSECURITYGROUPSRESPONSE']._serialized_end=2071
  _globals['_LISTNETWORKROUTETABLESREQUEST']._serialized_start=2073
  _globals['_LISTNETWORKROUTETABLESREQUEST']._serialized_end=2200
  _globals['_LISTNETWORKROUTETABLESRESPONSE']._serialized_start=2202
  _globals['_LISTNETWORKROUTETABLESRESPONSE']._serialized_end=2314
  _globals['_LISTNETWORKOPERATIONSREQUEST']._serialized_start=2316
  _globals['_LISTNETWORKOPERATIONSREQUEST']._serialized_end=2442
  _globals['_LISTNETWORKOPERATIONSRESPONSE']._serialized_start=2444
  _globals['_LISTNETWORKOPERATIONSRESPONSE']._serialized_end=2555
  _globals['_MOVENETWORKREQUEST']._serialized_start=2557
  _globals['_MOVENETWORKREQUEST']._serialized_end=2656
  _globals['_MOVENETWORKMETADATA']._serialized_start=2658
  _globals['_MOVENETWORKMETADATA']._serialized_end=2699
  _globals['_NETWORKSERVICE']._serialized_start=2702
  _globals['_NETWORKSERVICE']._serialized_end=4316
# @@protoc_insertion_point(module_scope)
