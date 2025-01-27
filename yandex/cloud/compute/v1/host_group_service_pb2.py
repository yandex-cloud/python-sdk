# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/compute/v1/host_group_service.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'yandex/cloud/compute/v1/host_group_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.compute.v1 import instance_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_instance__pb2
from yandex.cloud.compute.v1 import host_group_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_host__group__pb2
from yandex.cloud.compute.v1 import maintenance_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_maintenance__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0yandex/cloud/compute/v1/host_group_service.proto\x12\x17yandex.cloud.compute.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a yandex/cloud/access/access.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/compute/v1/instance.proto\x1a(yandex/cloud/compute/v1/host_group.proto\x1a)yandex/cloud/compute/v1/maintenance.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\":\n\x13GetHostGroupRequest\x12#\n\rhost_group_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\xaf\x01\n\x15ListHostGroupsRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\x12\x1b\n\x08order_by\x18\x05 \x01(\tB\t\x8a\xc8\x31\x05<=100\"j\n\x16ListHostGroupsResponse\x12\x37\n\x0bhost_groups\x18\x01 \x03(\x0b\x32\".yandex.cloud.compute.v1.HostGroup\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x92\x04\n\x16\x43reateHostGroupRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x33\n\x04name\x18\x02 \x01(\tB%\xf2\xc7\x31!|[a-z]([-_a-z0-9]{0,61}[a-z0-9])?\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x90\x01\n\x06labels\x18\x04 \x03(\x0b\x32;.yandex.cloud.compute.v1.CreateHostGroupRequest.LabelsEntryBC\xf2\xc7\x31\x0f[-_./\\@0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x1c\x12\x14[a-z][-_./\\@0-9a-z]*\x1a\x04\x31-63\x12\x1d\n\x07zone_id\x18\x05 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\x07type_id\x18\x06 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x46\n\x12maintenance_policy\x18\x07 \x01(\x0e\x32*.yandex.cloud.compute.v1.MaintenancePolicy\x12:\n\x0cscale_policy\x18\x08 \x01(\x0b\x32$.yandex.cloud.compute.v1.ScalePolicy\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"0\n\x17\x43reateHostGroupMetadata\x12\x15\n\rhost_group_id\x18\x01 \x01(\t\"\x89\x04\n\x16UpdateHostGroupRequest\x12#\n\rhost_group_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x33\n\x04name\x18\x03 \x01(\tB%\xf2\xc7\x31!|[a-z]([-_a-z0-9]{0,61}[a-z0-9])?\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x90\x01\n\x06labels\x18\x05 \x03(\x0b\x32;.yandex.cloud.compute.v1.UpdateHostGroupRequest.LabelsEntryBC\xf2\xc7\x31\x0f[-_./\\@0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x1c\x12\x14[a-z][-_./\\@0-9a-z]*\x1a\x04\x31-63\x12\x46\n\x12maintenance_policy\x18\x06 \x01(\x0e\x32*.yandex.cloud.compute.v1.MaintenancePolicy\x12:\n\x0cscale_policy\x18\x07 \x01(\x0b\x32$.yandex.cloud.compute.v1.ScalePolicy\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"0\n\x17UpdateHostGroupMetadata\x12\x15\n\rhost_group_id\x18\x01 \x01(\t\"=\n\x16\x44\x65leteHostGroupRequest\x12#\n\rhost_group_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"0\n\x17\x44\x65leteHostGroupMetadata\x12\x15\n\rhost_group_id\x18\x01 \x01(\t\"\x9e\x01\n\x1dListHostGroupInstancesRequest\x12#\n\rhost_group_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"o\n\x1eListHostGroupInstancesResponse\x12\x34\n\tinstances\x18\x01 \x03(\x0b\x32!.yandex.cloud.compute.v1.Instance\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"~\n\x19ListHostGroupHostsRequest\x12#\n\rhost_group_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"c\n\x1aListHostGroupHostsResponse\x12,\n\x05hosts\x18\x01 \x03(\x0b\x32\x1d.yandex.cloud.compute.v1.Host\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xc2\x01\n\x1aUpdateHostGroupHostRequest\x12#\n\rhost_group_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\x07host_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12/\n\x0b\x64\x65\x61\x64line_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"E\n\x1bUpdateHostGroupHostMetadata\x12\x15\n\rhost_group_id\x18\x01 \x01(\t\x12\x0f\n\x07host_id\x18\x02 \x01(\t\"\x83\x01\n\x1eListHostGroupOperationsRequest\x12#\n\rhost_group_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"q\n\x1fListHostGroupOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xfe\x11\n\x10HostGroupService\x12\x87\x01\n\x03Get\x12,.yandex.cloud.compute.v1.GetHostGroupRequest\x1a\".yandex.cloud.compute.v1.HostGroup\".\x82\xd3\xe4\x93\x02(\x12&/compute/v1/hostGroups/{host_group_id}\x12\x87\x01\n\x04List\x12..yandex.cloud.compute.v1.ListHostGroupsRequest\x1a/.yandex.cloud.compute.v1.ListHostGroupsResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/compute/v1/hostGroups\x12\xa7\x01\n\x06\x43reate\x12/.yandex.cloud.compute.v1.CreateHostGroupRequest\x1a!.yandex.cloud.operation.Operation\"I\xb2\xd2*$\n\x17\x43reateHostGroupMetadata\x12\tHostGroup\x82\xd3\xe4\x93\x02\x1b\"\x16/compute/v1/hostGroups:\x01*\x12\xb7\x01\n\x06Update\x12/.yandex.cloud.compute.v1.UpdateHostGroupRequest\x1a!.yandex.cloud.operation.Operation\"Y\xb2\xd2*$\n\x17UpdateHostGroupMetadata\x12\tHostGroup\x82\xd3\xe4\x93\x02+2&/compute/v1/hostGroups/{host_group_id}:\x01*\x12\xc0\x01\n\x06\x44\x65lete\x12/.yandex.cloud.compute.v1.DeleteHostGroupRequest\x1a!.yandex.cloud.operation.Operation\"b\xb2\xd2*0\n\x17\x44\x65leteHostGroupMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02(*&/compute/v1/hostGroups/{host_group_id}\x12\xbe\x01\n\x0eListOperations\x12\x37.yandex.cloud.compute.v1.ListHostGroupOperationsRequest\x1a\x38.yandex.cloud.compute.v1.ListHostGroupOperationsResponse\"9\x82\xd3\xe4\x93\x02\x33\x12\x31/compute/v1/hostGroups/{host_group_id}/operations\x12\xba\x01\n\rListInstances\x12\x36.yandex.cloud.compute.v1.ListHostGroupInstancesRequest\x1a\x37.yandex.cloud.compute.v1.ListHostGroupInstancesResponse\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/compute/v1/hostGroups/{host_group_id}/instances\x12\xaa\x01\n\tListHosts\x12\x32.yandex.cloud.compute.v1.ListHostGroupHostsRequest\x1a\x33.yandex.cloud.compute.v1.ListHostGroupHostsResponse\"4\x82\xd3\xe4\x93\x02.\x12,/compute/v1/hostGroups/{host_group_id}/hosts\x12\xce\x01\n\nUpdateHost\x12\x33.yandex.cloud.compute.v1.UpdateHostGroupHostRequest\x1a!.yandex.cloud.operation.Operation\"h\xb2\xd2*#\n\x1bUpdateHostGroupHostMetadata\x12\x04Host\x82\xd3\xe4\x93\x02;26/compute/v1/hostGroups/{host_group_id}/hosts/{host_id}:\x01*\x12\xb6\x01\n\x12ListAccessBindings\x12..yandex.cloud.access.ListAccessBindingsRequest\x1a/.yandex.cloud.access.ListAccessBindingsResponse\"?\x82\xd3\xe4\x93\x02\x39\x12\x37/compute/v1/hostGroups/{resource_id}:listAccessBindings\x12\xf5\x01\n\x11SetAccessBindings\x12-.yandex.cloud.access.SetAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x8d\x01\xb2\xd2*H\n access.SetAccessBindingsMetadata\x12$access.AccessBindingsOperationResult\x82\xd3\xe4\x93\x02;\"6/compute/v1/hostGroups/{resource_id}:setAccessBindings:\x01*\x12\x81\x02\n\x14UpdateAccessBindings\x12\x30.yandex.cloud.access.UpdateAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x93\x01\xb2\xd2*K\n#access.UpdateAccessBindingsMetadata\x12$access.AccessBindingsOperationResult\x82\xd3\xe4\x93\x02>\"9/compute/v1/hostGroups/{resource_id}:updateAccessBindings:\x01*Bb\n\x1byandex.cloud.api.compute.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;computeb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.compute.v1.host_group_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033yandex.cloud.api.compute.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;compute'
  _globals['_GETHOSTGROUPREQUEST'].fields_by_name['host_group_id']._loaded_options = None
  _globals['_GETHOSTGROUPREQUEST'].fields_by_name['host_group_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTHOSTGROUPSREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_LISTHOSTGROUPSREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTHOSTGROUPSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTHOSTGROUPSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTHOSTGROUPSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTHOSTGROUPSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTHOSTGROUPSREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTHOSTGROUPSREQUEST'].fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _globals['_LISTHOSTGROUPSREQUEST'].fields_by_name['order_by']._loaded_options = None
  _globals['_LISTHOSTGROUPSREQUEST'].fields_by_name['order_by']._serialized_options = b'\212\3101\005<=100'
  _globals['_CREATEHOSTGROUPREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_CREATEHOSTGROUPREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_CREATEHOSTGROUPREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_CREATEHOSTGROUPREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_CREATEHOSTGROUPREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_CREATEHOSTGROUPREQUEST'].fields_by_name['name']._serialized_options = b'\362\3071!|[a-z]([-_a-z0-9]{0,61}[a-z0-9])?'
  _globals['_CREATEHOSTGROUPREQUEST'].fields_by_name['description']._loaded_options = None
  _globals['_CREATEHOSTGROUPREQUEST'].fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _globals['_CREATEHOSTGROUPREQUEST'].fields_by_name['labels']._loaded_options = None
  _globals['_CREATEHOSTGROUPREQUEST'].fields_by_name['labels']._serialized_options = b'\362\3071\017[-_./\\@0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\034\022\024[a-z][-_./\\@0-9a-z]*\032\0041-63'
  _globals['_CREATEHOSTGROUPREQUEST'].fields_by_name['zone_id']._loaded_options = None
  _globals['_CREATEHOSTGROUPREQUEST'].fields_by_name['zone_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_CREATEHOSTGROUPREQUEST'].fields_by_name['type_id']._loaded_options = None
  _globals['_CREATEHOSTGROUPREQUEST'].fields_by_name['type_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_UPDATEHOSTGROUPREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_UPDATEHOSTGROUPREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_UPDATEHOSTGROUPREQUEST'].fields_by_name['host_group_id']._loaded_options = None
  _globals['_UPDATEHOSTGROUPREQUEST'].fields_by_name['host_group_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_UPDATEHOSTGROUPREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_UPDATEHOSTGROUPREQUEST'].fields_by_name['name']._serialized_options = b'\362\3071!|[a-z]([-_a-z0-9]{0,61}[a-z0-9])?'
  _globals['_UPDATEHOSTGROUPREQUEST'].fields_by_name['description']._loaded_options = None
  _globals['_UPDATEHOSTGROUPREQUEST'].fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _globals['_UPDATEHOSTGROUPREQUEST'].fields_by_name['labels']._loaded_options = None
  _globals['_UPDATEHOSTGROUPREQUEST'].fields_by_name['labels']._serialized_options = b'\362\3071\017[-_./\\@0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\034\022\024[a-z][-_./\\@0-9a-z]*\032\0041-63'
  _globals['_DELETEHOSTGROUPREQUEST'].fields_by_name['host_group_id']._loaded_options = None
  _globals['_DELETEHOSTGROUPREQUEST'].fields_by_name['host_group_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTHOSTGROUPINSTANCESREQUEST'].fields_by_name['host_group_id']._loaded_options = None
  _globals['_LISTHOSTGROUPINSTANCESREQUEST'].fields_by_name['host_group_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTHOSTGROUPINSTANCESREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTHOSTGROUPINSTANCESREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTHOSTGROUPINSTANCESREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTHOSTGROUPINSTANCESREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTHOSTGROUPINSTANCESREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTHOSTGROUPINSTANCESREQUEST'].fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _globals['_LISTHOSTGROUPHOSTSREQUEST'].fields_by_name['host_group_id']._loaded_options = None
  _globals['_LISTHOSTGROUPHOSTSREQUEST'].fields_by_name['host_group_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTHOSTGROUPHOSTSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTHOSTGROUPHOSTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTHOSTGROUPHOSTSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTHOSTGROUPHOSTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_UPDATEHOSTGROUPHOSTREQUEST'].fields_by_name['host_group_id']._loaded_options = None
  _globals['_UPDATEHOSTGROUPHOSTREQUEST'].fields_by_name['host_group_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_UPDATEHOSTGROUPHOSTREQUEST'].fields_by_name['host_id']._loaded_options = None
  _globals['_UPDATEHOSTGROUPHOSTREQUEST'].fields_by_name['host_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTHOSTGROUPOPERATIONSREQUEST'].fields_by_name['host_group_id']._loaded_options = None
  _globals['_LISTHOSTGROUPOPERATIONSREQUEST'].fields_by_name['host_group_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTHOSTGROUPOPERATIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTHOSTGROUPOPERATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTHOSTGROUPOPERATIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTHOSTGROUPOPERATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_HOSTGROUPSERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_HOSTGROUPSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002(\022&/compute/v1/hostGroups/{host_group_id}'
  _globals['_HOSTGROUPSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_HOSTGROUPSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002\030\022\026/compute/v1/hostGroups'
  _globals['_HOSTGROUPSERVICE'].methods_by_name['Create']._loaded_options = None
  _globals['_HOSTGROUPSERVICE'].methods_by_name['Create']._serialized_options = b'\262\322*$\n\027CreateHostGroupMetadata\022\tHostGroup\202\323\344\223\002\033\"\026/compute/v1/hostGroups:\001*'
  _globals['_HOSTGROUPSERVICE'].methods_by_name['Update']._loaded_options = None
  _globals['_HOSTGROUPSERVICE'].methods_by_name['Update']._serialized_options = b'\262\322*$\n\027UpdateHostGroupMetadata\022\tHostGroup\202\323\344\223\002+2&/compute/v1/hostGroups/{host_group_id}:\001*'
  _globals['_HOSTGROUPSERVICE'].methods_by_name['Delete']._loaded_options = None
  _globals['_HOSTGROUPSERVICE'].methods_by_name['Delete']._serialized_options = b'\262\322*0\n\027DeleteHostGroupMetadata\022\025google.protobuf.Empty\202\323\344\223\002(*&/compute/v1/hostGroups/{host_group_id}'
  _globals['_HOSTGROUPSERVICE'].methods_by_name['ListOperations']._loaded_options = None
  _globals['_HOSTGROUPSERVICE'].methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\0023\0221/compute/v1/hostGroups/{host_group_id}/operations'
  _globals['_HOSTGROUPSERVICE'].methods_by_name['ListInstances']._loaded_options = None
  _globals['_HOSTGROUPSERVICE'].methods_by_name['ListInstances']._serialized_options = b'\202\323\344\223\0022\0220/compute/v1/hostGroups/{host_group_id}/instances'
  _globals['_HOSTGROUPSERVICE'].methods_by_name['ListHosts']._loaded_options = None
  _globals['_HOSTGROUPSERVICE'].methods_by_name['ListHosts']._serialized_options = b'\202\323\344\223\002.\022,/compute/v1/hostGroups/{host_group_id}/hosts'
  _globals['_HOSTGROUPSERVICE'].methods_by_name['UpdateHost']._loaded_options = None
  _globals['_HOSTGROUPSERVICE'].methods_by_name['UpdateHost']._serialized_options = b'\262\322*#\n\033UpdateHostGroupHostMetadata\022\004Host\202\323\344\223\002;26/compute/v1/hostGroups/{host_group_id}/hosts/{host_id}:\001*'
  _globals['_HOSTGROUPSERVICE'].methods_by_name['ListAccessBindings']._loaded_options = None
  _globals['_HOSTGROUPSERVICE'].methods_by_name['ListAccessBindings']._serialized_options = b'\202\323\344\223\0029\0227/compute/v1/hostGroups/{resource_id}:listAccessBindings'
  _globals['_HOSTGROUPSERVICE'].methods_by_name['SetAccessBindings']._loaded_options = None
  _globals['_HOSTGROUPSERVICE'].methods_by_name['SetAccessBindings']._serialized_options = b'\262\322*H\n access.SetAccessBindingsMetadata\022$access.AccessBindingsOperationResult\202\323\344\223\002;\"6/compute/v1/hostGroups/{resource_id}:setAccessBindings:\001*'
  _globals['_HOSTGROUPSERVICE'].methods_by_name['UpdateAccessBindings']._loaded_options = None
  _globals['_HOSTGROUPSERVICE'].methods_by_name['UpdateAccessBindings']._serialized_options = b'\262\322*K\n#access.UpdateAccessBindingsMetadata\022$access.AccessBindingsOperationResult\202\323\344\223\002>\"9/compute/v1/hostGroups/{resource_id}:updateAccessBindings:\001*'
  _globals['_GETHOSTGROUPREQUEST']._serialized_start=438
  _globals['_GETHOSTGROUPREQUEST']._serialized_end=496
  _globals['_LISTHOSTGROUPSREQUEST']._serialized_start=499
  _globals['_LISTHOSTGROUPSREQUEST']._serialized_end=674
  _globals['_LISTHOSTGROUPSRESPONSE']._serialized_start=676
  _globals['_LISTHOSTGROUPSRESPONSE']._serialized_end=782
  _globals['_CREATEHOSTGROUPREQUEST']._serialized_start=785
  _globals['_CREATEHOSTGROUPREQUEST']._serialized_end=1315
  _globals['_CREATEHOSTGROUPREQUEST_LABELSENTRY']._serialized_start=1270
  _globals['_CREATEHOSTGROUPREQUEST_LABELSENTRY']._serialized_end=1315
  _globals['_CREATEHOSTGROUPMETADATA']._serialized_start=1317
  _globals['_CREATEHOSTGROUPMETADATA']._serialized_end=1365
  _globals['_UPDATEHOSTGROUPREQUEST']._serialized_start=1368
  _globals['_UPDATEHOSTGROUPREQUEST']._serialized_end=1889
  _globals['_UPDATEHOSTGROUPREQUEST_LABELSENTRY']._serialized_start=1270
  _globals['_UPDATEHOSTGROUPREQUEST_LABELSENTRY']._serialized_end=1315
  _globals['_UPDATEHOSTGROUPMETADATA']._serialized_start=1891
  _globals['_UPDATEHOSTGROUPMETADATA']._serialized_end=1939
  _globals['_DELETEHOSTGROUPREQUEST']._serialized_start=1941
  _globals['_DELETEHOSTGROUPREQUEST']._serialized_end=2002
  _globals['_DELETEHOSTGROUPMETADATA']._serialized_start=2004
  _globals['_DELETEHOSTGROUPMETADATA']._serialized_end=2052
  _globals['_LISTHOSTGROUPINSTANCESREQUEST']._serialized_start=2055
  _globals['_LISTHOSTGROUPINSTANCESREQUEST']._serialized_end=2213
  _globals['_LISTHOSTGROUPINSTANCESRESPONSE']._serialized_start=2215
  _globals['_LISTHOSTGROUPINSTANCESRESPONSE']._serialized_end=2326
  _globals['_LISTHOSTGROUPHOSTSREQUEST']._serialized_start=2328
  _globals['_LISTHOSTGROUPHOSTSREQUEST']._serialized_end=2454
  _globals['_LISTHOSTGROUPHOSTSRESPONSE']._serialized_start=2456
  _globals['_LISTHOSTGROUPHOSTSRESPONSE']._serialized_end=2555
  _globals['_UPDATEHOSTGROUPHOSTREQUEST']._serialized_start=2558
  _globals['_UPDATEHOSTGROUPHOSTREQUEST']._serialized_end=2752
  _globals['_UPDATEHOSTGROUPHOSTMETADATA']._serialized_start=2754
  _globals['_UPDATEHOSTGROUPHOSTMETADATA']._serialized_end=2823
  _globals['_LISTHOSTGROUPOPERATIONSREQUEST']._serialized_start=2826
  _globals['_LISTHOSTGROUPOPERATIONSREQUEST']._serialized_end=2957
  _globals['_LISTHOSTGROUPOPERATIONSRESPONSE']._serialized_start=2959
  _globals['_LISTHOSTGROUPOPERATIONSRESPONSE']._serialized_end=3072
  _globals['_HOSTGROUPSERVICE']._serialized_start=3075
  _globals['_HOSTGROUPSERVICE']._serialized_end=5377
# @@protoc_insertion_point(module_scope)
