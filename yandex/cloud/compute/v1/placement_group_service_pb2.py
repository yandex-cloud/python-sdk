# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/compute/v1/placement_group_service.proto
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
from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.compute.v1 import instance_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_instance__pb2
from yandex.cloud.compute.v1 import placement_group_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_placement__group__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5yandex/cloud/compute/v1/placement_group_service.proto\x12\x17yandex.cloud.compute.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/access/access.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/compute/v1/instance.proto\x1a-yandex/cloud/compute/v1/placement_group.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"6\n\x18GetPlacementGroupRequest\x12\x1a\n\x12placement_group_id\x18\x01 \x01(\t\"\xb4\x01\n\x1aListPlacementGroupsRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\x12\x1b\n\x08order_by\x18\x05 \x01(\tB\t\x8a\xc8\x31\x05<=100\"y\n\x1bListPlacementGroupsResponse\x12\x41\n\x10placement_groups\x18\x01 \x03(\x0b\x32\'.yandex.cloud.compute.v1.PlacementGroup\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xa4\x03\n\x1b\x43reatePlacementGroupRequest\x12\x11\n\tfolder_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12P\n\x06labels\x18\x04 \x03(\x0b\x32@.yandex.cloud.compute.v1.CreatePlacementGroupRequest.LabelsEntry\x12U\n\x19spread_placement_strategy\x18\x05 \x01(\x0b\x32\x30.yandex.cloud.compute.v1.SpreadPlacementStrategyH\x00\x12[\n\x1cpartition_placement_strategy\x18\x06 \x01(\x0b\x32\x33.yandex.cloud.compute.v1.PartitionPlacementStrategyH\x00\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x1a\n\x12placement_strategy\x12\x04\xc0\xc1\x31\x01\":\n\x1c\x43reatePlacementGroupMetadata\x12\x1a\n\x12placement_group_id\x18\x01 \x01(\t\"\x8e\x02\n\x1bUpdatePlacementGroupRequest\x12\x1a\n\x12placement_group_id\x18\x01 \x01(\t\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12P\n\x06labels\x18\x05 \x03(\x0b\x32@.yandex.cloud.compute.v1.UpdatePlacementGroupRequest.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\":\n\x1cUpdatePlacementGroupMetadata\x12\x1a\n\x12placement_group_id\x18\x01 \x01(\t\"9\n\x1b\x44\x65letePlacementGroupRequest\x12\x1a\n\x12placement_group_id\x18\x01 \x01(\t\":\n\x1c\x44\x65letePlacementGroupMetadata\x12\x1a\n\x12placement_group_id\x18\x01 \x01(\t\"g\n\"ListPlacementGroupInstancesRequest\x12\x1a\n\x12placement_group_id\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x03\x12\x12\n\npage_token\x18\x03 \x01(\t\"t\n#ListPlacementGroupInstancesResponse\x12\x34\n\tinstances\x18\x01 \x03(\x0b\x32!.yandex.cloud.compute.v1.Instance\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"h\n#ListPlacementGroupOperationsRequest\x12\x1a\n\x12placement_group_id\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x03\x12\x12\n\npage_token\x18\x03 \x01(\t\"v\n$ListPlacementGroupOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xa0\x10\n\x15PlacementGroupService\x12\x9b\x01\n\x03Get\x12\x31.yandex.cloud.compute.v1.GetPlacementGroupRequest\x1a\'.yandex.cloud.compute.v1.PlacementGroup\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/compute/v1/placementGroups/{placement_group_id}\x12\x96\x01\n\x04List\x12\x33.yandex.cloud.compute.v1.ListPlacementGroupsRequest\x1a\x34.yandex.cloud.compute.v1.ListPlacementGroupsResponse\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/compute/v1/placementGroups\x12\xbb\x01\n\x06\x43reate\x12\x34.yandex.cloud.compute.v1.CreatePlacementGroupRequest\x1a!.yandex.cloud.operation.Operation\"X\xb2\xd2*.\n\x1c\x43reatePlacementGroupMetadata\x12\x0ePlacementGroup\x82\xd3\xe4\x93\x02 \"\x1b/compute/v1/placementGroups:\x01*\x12\xd0\x01\n\x06Update\x12\x34.yandex.cloud.compute.v1.UpdatePlacementGroupRequest\x1a!.yandex.cloud.operation.Operation\"m\xb2\xd2*.\n\x1cUpdatePlacementGroupMetadata\x12\x0ePlacementGroup\x82\xd3\xe4\x93\x02\x35\x32\x30/compute/v1/placementGroups/{placement_group_id}:\x01*\x12\xd4\x01\n\x06\x44\x65lete\x12\x34.yandex.cloud.compute.v1.DeletePlacementGroupRequest\x1a!.yandex.cloud.operation.Operation\"q\xb2\xd2*5\n\x1c\x44\x65letePlacementGroupMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x32*0/compute/v1/placementGroups/{placement_group_id}\x12\xce\x01\n\rListInstances\x12;.yandex.cloud.compute.v1.ListPlacementGroupInstancesRequest\x1a<.yandex.cloud.compute.v1.ListPlacementGroupInstancesResponse\"B\x82\xd3\xe4\x93\x02<\x12:/compute/v1/placementGroups/{placement_group_id}/instances\x12\xd2\x01\n\x0eListOperations\x12<.yandex.cloud.compute.v1.ListPlacementGroupOperationsRequest\x1a=.yandex.cloud.compute.v1.ListPlacementGroupOperationsResponse\"C\x82\xd3\xe4\x93\x02=\x12;/compute/v1/placementGroups/{placement_group_id}/operations\x12\xbb\x01\n\x12ListAccessBindings\x12..yandex.cloud.access.ListAccessBindingsRequest\x1a/.yandex.cloud.access.ListAccessBindingsResponse\"D\x82\xd3\xe4\x93\x02>\x12</compute/v1/placementGroups/{resource_id}:listAccessBindings\x12\xfa\x01\n\x11SetAccessBindings\x12-.yandex.cloud.access.SetAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x92\x01\xb2\xd2*H\n access.SetAccessBindingsMetadata\x12$access.AccessBindingsOperationResult\x82\xd3\xe4\x93\x02@\";/compute/v1/placementGroups/{resource_id}:setAccessBindings:\x01*\x12\x86\x02\n\x14UpdateAccessBindings\x12\x30.yandex.cloud.access.UpdateAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x98\x01\xb2\xd2*K\n#access.UpdateAccessBindingsMetadata\x12$access.AccessBindingsOperationResult\x82\xd3\xe4\x93\x02\x43\">/compute/v1/placementGroups/{resource_id}:updateAccessBindings:\x01*Bb\n\x1byandex.cloud.api.compute.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;computeb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.compute.v1.placement_group_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033yandex.cloud.api.compute.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;compute'
  _globals['_LISTPLACEMENTGROUPSREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_LISTPLACEMENTGROUPSREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTPLACEMENTGROUPSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTPLACEMENTGROUPSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTPLACEMENTGROUPSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTPLACEMENTGROUPSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTPLACEMENTGROUPSREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTPLACEMENTGROUPSREQUEST'].fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _globals['_LISTPLACEMENTGROUPSREQUEST'].fields_by_name['order_by']._loaded_options = None
  _globals['_LISTPLACEMENTGROUPSREQUEST'].fields_by_name['order_by']._serialized_options = b'\212\3101\005<=100'
  _globals['_CREATEPLACEMENTGROUPREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_CREATEPLACEMENTGROUPREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_CREATEPLACEMENTGROUPREQUEST'].oneofs_by_name['placement_strategy']._loaded_options = None
  _globals['_CREATEPLACEMENTGROUPREQUEST'].oneofs_by_name['placement_strategy']._serialized_options = b'\300\3011\001'
  _globals['_UPDATEPLACEMENTGROUPREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_UPDATEPLACEMENTGROUPREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_PLACEMENTGROUPSERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_PLACEMENTGROUPSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\0022\0220/compute/v1/placementGroups/{placement_group_id}'
  _globals['_PLACEMENTGROUPSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_PLACEMENTGROUPSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002\035\022\033/compute/v1/placementGroups'
  _globals['_PLACEMENTGROUPSERVICE'].methods_by_name['Create']._loaded_options = None
  _globals['_PLACEMENTGROUPSERVICE'].methods_by_name['Create']._serialized_options = b'\262\322*.\n\034CreatePlacementGroupMetadata\022\016PlacementGroup\202\323\344\223\002 \"\033/compute/v1/placementGroups:\001*'
  _globals['_PLACEMENTGROUPSERVICE'].methods_by_name['Update']._loaded_options = None
  _globals['_PLACEMENTGROUPSERVICE'].methods_by_name['Update']._serialized_options = b'\262\322*.\n\034UpdatePlacementGroupMetadata\022\016PlacementGroup\202\323\344\223\002520/compute/v1/placementGroups/{placement_group_id}:\001*'
  _globals['_PLACEMENTGROUPSERVICE'].methods_by_name['Delete']._loaded_options = None
  _globals['_PLACEMENTGROUPSERVICE'].methods_by_name['Delete']._serialized_options = b'\262\322*5\n\034DeletePlacementGroupMetadata\022\025google.protobuf.Empty\202\323\344\223\0022*0/compute/v1/placementGroups/{placement_group_id}'
  _globals['_PLACEMENTGROUPSERVICE'].methods_by_name['ListInstances']._loaded_options = None
  _globals['_PLACEMENTGROUPSERVICE'].methods_by_name['ListInstances']._serialized_options = b'\202\323\344\223\002<\022:/compute/v1/placementGroups/{placement_group_id}/instances'
  _globals['_PLACEMENTGROUPSERVICE'].methods_by_name['ListOperations']._loaded_options = None
  _globals['_PLACEMENTGROUPSERVICE'].methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\002=\022;/compute/v1/placementGroups/{placement_group_id}/operations'
  _globals['_PLACEMENTGROUPSERVICE'].methods_by_name['ListAccessBindings']._loaded_options = None
  _globals['_PLACEMENTGROUPSERVICE'].methods_by_name['ListAccessBindings']._serialized_options = b'\202\323\344\223\002>\022</compute/v1/placementGroups/{resource_id}:listAccessBindings'
  _globals['_PLACEMENTGROUPSERVICE'].methods_by_name['SetAccessBindings']._loaded_options = None
  _globals['_PLACEMENTGROUPSERVICE'].methods_by_name['SetAccessBindings']._serialized_options = b'\262\322*H\n access.SetAccessBindingsMetadata\022$access.AccessBindingsOperationResult\202\323\344\223\002@\";/compute/v1/placementGroups/{resource_id}:setAccessBindings:\001*'
  _globals['_PLACEMENTGROUPSERVICE'].methods_by_name['UpdateAccessBindings']._loaded_options = None
  _globals['_PLACEMENTGROUPSERVICE'].methods_by_name['UpdateAccessBindings']._serialized_options = b'\262\322*K\n#access.UpdateAccessBindingsMetadata\022$access.AccessBindingsOperationResult\202\323\344\223\002C\">/compute/v1/placementGroups/{resource_id}:updateAccessBindings:\001*'
  _globals['_GETPLACEMENTGROUPREQUEST']._serialized_start=372
  _globals['_GETPLACEMENTGROUPREQUEST']._serialized_end=426
  _globals['_LISTPLACEMENTGROUPSREQUEST']._serialized_start=429
  _globals['_LISTPLACEMENTGROUPSREQUEST']._serialized_end=609
  _globals['_LISTPLACEMENTGROUPSRESPONSE']._serialized_start=611
  _globals['_LISTPLACEMENTGROUPSRESPONSE']._serialized_end=732
  _globals['_CREATEPLACEMENTGROUPREQUEST']._serialized_start=735
  _globals['_CREATEPLACEMENTGROUPREQUEST']._serialized_end=1155
  _globals['_CREATEPLACEMENTGROUPREQUEST_LABELSENTRY']._serialized_start=1082
  _globals['_CREATEPLACEMENTGROUPREQUEST_LABELSENTRY']._serialized_end=1127
  _globals['_CREATEPLACEMENTGROUPMETADATA']._serialized_start=1157
  _globals['_CREATEPLACEMENTGROUPMETADATA']._serialized_end=1215
  _globals['_UPDATEPLACEMENTGROUPREQUEST']._serialized_start=1218
  _globals['_UPDATEPLACEMENTGROUPREQUEST']._serialized_end=1488
  _globals['_UPDATEPLACEMENTGROUPREQUEST_LABELSENTRY']._serialized_start=1082
  _globals['_UPDATEPLACEMENTGROUPREQUEST_LABELSENTRY']._serialized_end=1127
  _globals['_UPDATEPLACEMENTGROUPMETADATA']._serialized_start=1490
  _globals['_UPDATEPLACEMENTGROUPMETADATA']._serialized_end=1548
  _globals['_DELETEPLACEMENTGROUPREQUEST']._serialized_start=1550
  _globals['_DELETEPLACEMENTGROUPREQUEST']._serialized_end=1607
  _globals['_DELETEPLACEMENTGROUPMETADATA']._serialized_start=1609
  _globals['_DELETEPLACEMENTGROUPMETADATA']._serialized_end=1667
  _globals['_LISTPLACEMENTGROUPINSTANCESREQUEST']._serialized_start=1669
  _globals['_LISTPLACEMENTGROUPINSTANCESREQUEST']._serialized_end=1772
  _globals['_LISTPLACEMENTGROUPINSTANCESRESPONSE']._serialized_start=1774
  _globals['_LISTPLACEMENTGROUPINSTANCESRESPONSE']._serialized_end=1890
  _globals['_LISTPLACEMENTGROUPOPERATIONSREQUEST']._serialized_start=1892
  _globals['_LISTPLACEMENTGROUPOPERATIONSREQUEST']._serialized_end=1996
  _globals['_LISTPLACEMENTGROUPOPERATIONSRESPONSE']._serialized_start=1998
  _globals['_LISTPLACEMENTGROUPOPERATIONSRESPONSE']._serialized_end=2116
  _globals['_PLACEMENTGROUPSERVICE']._serialized_start=2119
  _globals['_PLACEMENTGROUPSERVICE']._serialized_end=4199
# @@protoc_insertion_point(module_scope)
