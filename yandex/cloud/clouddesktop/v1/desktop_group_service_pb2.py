# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/clouddesktop/v1/desktop_group_service.proto
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
    'yandex/cloud/clouddesktop/v1/desktop_group_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.clouddesktop.v1 import desktop_pb2 as yandex_dot_cloud_dot_clouddesktop_dot_v1_dot_desktop__pb2
from yandex.cloud.clouddesktop.v1 import desktop_group_pb2 as yandex_dot_cloud_dot_clouddesktop_dot_v1_dot_desktop__group__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.clouddesktop.v1 import disk_pb2 as yandex_dot_cloud_dot_clouddesktop_dot_v1_dot_disk__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8yandex/cloud/clouddesktop/v1/desktop_group_service.proto\x12 yandex.cloud.clouddesktop.v1.api\x1a\x1cgoogle/api/annotations.proto\x1a yandex/cloud/access/access.proto\x1a yandex/cloud/api/operation.proto\x1a*yandex/cloud/clouddesktop/v1/desktop.proto\x1a\x30yandex/cloud/clouddesktop/v1/desktop_group.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\x1a google/protobuf/field_mask.proto\x1a\'yandex/cloud/clouddesktop/v1/disk.proto\"@\n\x16GetDesktopGroupRequest\x12&\n\x10\x64\x65sktop_group_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\xb8\x01\n\x18ListDesktopGroupsRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x15 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x16 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x17 \x01(\tB\n\x8a\xc8\x31\x06<=1000\x12\x1b\n\x08order_by\x18\x18 \x01(\tB\t\x8a\xc8\x31\x05<=100J\x04\x08\x02\x10\x15\"\x82\x01\n\x19ListDesktopGroupsResponse\x12\x46\n\x0e\x64\x65sktop_groups\x18\x01 \x03(\x0b\x32..yandex.cloud.clouddesktop.v1.api.DesktopGroup\x12\x17\n\x0fnext_page_token\x18\x16 \x01(\tJ\x04\x08\x02\x10\x16\"\xc6\x01\n\x1fListDesktopGroupDesktopsRequest\x12&\n\x10\x64\x65sktop_group_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x15 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x16 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x17 \x01(\tB\n\x8a\xc8\x31\x06<=1000\x12\x1b\n\x08order_by\x18\x18 \x01(\tB\t\x8a\xc8\x31\x05<=100J\x04\x08\x02\x10\x15\"~\n ListDesktopGroupDesktopsResponse\x12;\n\x08\x64\x65sktops\x18\x01 \x03(\x0b\x32).yandex.cloud.clouddesktop.v1.api.Desktop\x12\x17\n\x0fnext_page_token\x18\x16 \x01(\tJ\x04\x08\x02\x10\x16\"\xab\x01\n!ListDesktopGroupOperationsRequest\x12&\n\x10\x64\x65sktop_group_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x15 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x16 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x17 \x01(\tB\n\x8a\xc8\x31\x06<=1000J\x04\x08\x02\x10\x15\"z\n\"ListDesktopGroupOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x16 \x01(\tJ\x04\x08\x02\x10\x16\"\x95\x07\n\x19UpdateDesktopGroupRequest\x12&\n\x10\x64\x65sktop_group_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\"\n\x10\x64\x65sktop_image_id\x18\x03 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x31\n\x04name\x18\x04 \x01(\tB#\xf2\xc7\x31\x1f|[a-z]([-a-z0-9]{0,61}[a-z0-9])\x12\x1f\n\x0b\x64\x65scription\x18\x05 \x01(\tB\n\x8a\xc8\x31\x06<=1024\x12\x94\x01\n\x06labels\x18\x06 \x03(\x0b\x32G.yandex.cloud.clouddesktop.v1.api.UpdateDesktopGroupRequest.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04\x31-63\x12G\n\x0eresources_spec\x18\x07 \x01(\x0b\x32/.yandex.cloud.clouddesktop.v1.api.ResourcesSpec\x12Q\n\x0cgroup_config\x18\n \x01(\x0b\x32;.yandex.cloud.clouddesktop.v1.api.DesktopGroupConfiguration\x12\x42\n\x0e\x62oot_disk_spec\x18\x0b \x01(\x0b\x32*.yandex.cloud.clouddesktop.v1.api.DiskSpec\x12\x42\n\x0e\x64\x61ta_disk_spec\x18\x0c \x01(\x0b\x32*.yandex.cloud.clouddesktop.v1.api.DiskSpec\x12P\n\x12\x61uto_update_policy\x18\r \x01(\x0b\x32\x32.yandex.cloud.clouddesktop.v1.api.AutoUpdatePolicyH\x00\x12T\n\x14manual_update_policy\x18\x0e \x01(\x0b\x32\x34.yandex.cloud.clouddesktop.v1.api.ManualUpdatePolicyH\x00\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x0f\n\rupdate_policyJ\x04\x08\x08\x10\n\"\xbf\x04\n\x19\x43reateDesktopGroupRequest\x12\x1f\n\tfolder_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12&\n\x10\x64\x65sktop_image_id\x18\x03 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x30\n\x04name\x18\x0b \x01(\tB\"\xf2\xc7\x31\x1e[a-z]([-a-z0-9]{0,61}[a-z0-9])\x12\x1f\n\x0b\x64\x65scription\x18\x0c \x01(\tB\n\x8a\xc8\x31\x06<=1024\x12G\n\x0eresources_spec\x18\x15 \x01(\x0b\x32/.yandex.cloud.clouddesktop.v1.api.ResourcesSpec\x12V\n\x16network_interface_spec\x18\x16 \x01(\x0b\x32\x36.yandex.cloud.clouddesktop.v1.api.NetworkInterfaceSpec\x12\x42\n\x0e\x62oot_disk_spec\x18\x17 \x01(\x0b\x32*.yandex.cloud.clouddesktop.v1.api.DiskSpec\x12\x42\n\x0e\x64\x61ta_disk_spec\x18\x18 \x01(\x0b\x32*.yandex.cloud.clouddesktop.v1.api.DiskSpec\x12Q\n\x0cgroup_config\x18\x19 \x01(\x0b\x32;.yandex.cloud.clouddesktop.v1.api.DesktopGroupConfigurationJ\x04\x08\r\x10\x15J\x04\x08\x04\x10\x0b\"6\n\x1a\x43reateDesktopGroupMetadata\x12\x18\n\x10\x64\x65sktop_group_id\x18\x01 \x01(\t\"C\n\x19\x44\x65leteDesktopGroupRequest\x12&\n\x10\x64\x65sktop_group_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"6\n\x1a\x44\x65leteDesktopGroupMetadata\x12\x18\n\x10\x64\x65sktop_group_id\x18\x01 \x01(\t\"6\n\x1aUpdateDesktopGroupMetadata\x12\x18\n\x10\x64\x65sktop_group_id\x18\x01 \x01(\t2\xe6\x10\n\x13\x44\x65sktopGroupService\x12\xab\x01\n\x03Get\x12\x38.yandex.cloud.clouddesktop.v1.api.GetDesktopGroupRequest\x1a..yandex.cloud.clouddesktop.v1.api.DesktopGroup\":\x82\xd3\xe4\x93\x02\x34\x12\x32/cloud-desktop/v1/desktopGroups/{desktop_group_id}\x12\xa8\x01\n\x04List\x12:.yandex.cloud.clouddesktop.v1.api.ListDesktopGroupsRequest\x1a;.yandex.cloud.clouddesktop.v1.api.ListDesktopGroupsResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/cloud-desktop/v1/desktopGroups\x12\xda\x01\n\x0cListDesktops\x12\x41.yandex.cloud.clouddesktop.v1.api.ListDesktopGroupDesktopsRequest\x1a\x42.yandex.cloud.clouddesktop.v1.api.ListDesktopGroupDesktopsResponse\"C\x82\xd3\xe4\x93\x02=\x12;/cloud-desktop/v1/desktopGroups/{desktop_group_id}/desktops\x12\xe2\x01\n\x0eListOperations\x12\x43.yandex.cloud.clouddesktop.v1.api.ListDesktopGroupOperationsRequest\x1a\x44.yandex.cloud.clouddesktop.v1.api.ListDesktopGroupOperationsResponse\"E\x82\xd3\xe4\x93\x02?\x12=/cloud-desktop/v1/desktopGroups/{desktop_group_id}/operations\x12\xc2\x01\n\x06\x43reate\x12;.yandex.cloud.clouddesktop.v1.api.CreateDesktopGroupRequest\x1a!.yandex.cloud.operation.Operation\"X\xb2\xd2**\n\x1a\x43reateDesktopGroupMetadata\x12\x0c\x44\x65sktopGroup\x82\xd3\xe4\x93\x02$\"\x1f/cloud-desktop/v1/desktopGroups:\x01*\x12\xde\x01\n\x06Update\x12;.yandex.cloud.clouddesktop.v1.api.UpdateDesktopGroupRequest\x1a!.yandex.cloud.operation.Operation\"t\xb2\xd2*3\n\x1aUpdateDesktopGroupMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x37\x32\x32/cloud-desktop/v1/desktopGroups/{desktop_group_id}:\x01*\x12\xdb\x01\n\x06\x44\x65lete\x12;.yandex.cloud.clouddesktop.v1.api.DeleteDesktopGroupRequest\x1a!.yandex.cloud.operation.Operation\"q\xb2\xd2*3\n\x1a\x44\x65leteDesktopGroupMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x34*2/cloud-desktop/v1/desktopGroups/{desktop_group_id}\x12\xbf\x01\n\x12ListAccessBindings\x12..yandex.cloud.access.ListAccessBindingsRequest\x1a/.yandex.cloud.access.ListAccessBindingsResponse\"H\x82\xd3\xe4\x93\x02\x42\x12@/cloud-desktop/v1/desktopGroups/{resource_id}:listAccessBindings\x12\xef\x01\n\x11SetAccessBindings\x12-.yandex.cloud.access.SetAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x87\x01\xb2\xd2*9\n access.SetAccessBindingsMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x44\"?/cloud-desktop/v1/desktopGroups/{resource_id}:setAccessBindings:\x01*\x12\xfb\x01\n\x14UpdateAccessBindings\x12\x30.yandex.cloud.access.UpdateAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x8d\x01\xb2\xd2*<\n#access.UpdateAccessBindingsMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02G\"B/cloud-desktop/v1/desktopGroups/{resource_id}:updateAccessBindings:\x01*Bq\n yandex.cloud.api.clouddesktop.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/clouddesktop/v1;clouddesktopb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.clouddesktop.v1.desktop_group_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n yandex.cloud.api.clouddesktop.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/clouddesktop/v1;clouddesktop'
  _globals['_GETDESKTOPGROUPREQUEST'].fields_by_name['desktop_group_id']._loaded_options = None
  _globals['_GETDESKTOPGROUPREQUEST'].fields_by_name['desktop_group_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTDESKTOPGROUPSREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_LISTDESKTOPGROUPSREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTDESKTOPGROUPSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTDESKTOPGROUPSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _globals['_LISTDESKTOPGROUPSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTDESKTOPGROUPSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTDESKTOPGROUPSREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTDESKTOPGROUPSREQUEST'].fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _globals['_LISTDESKTOPGROUPSREQUEST'].fields_by_name['order_by']._loaded_options = None
  _globals['_LISTDESKTOPGROUPSREQUEST'].fields_by_name['order_by']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTDESKTOPGROUPDESKTOPSREQUEST'].fields_by_name['desktop_group_id']._loaded_options = None
  _globals['_LISTDESKTOPGROUPDESKTOPSREQUEST'].fields_by_name['desktop_group_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTDESKTOPGROUPDESKTOPSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTDESKTOPGROUPDESKTOPSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _globals['_LISTDESKTOPGROUPDESKTOPSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTDESKTOPGROUPDESKTOPSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTDESKTOPGROUPDESKTOPSREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTDESKTOPGROUPDESKTOPSREQUEST'].fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _globals['_LISTDESKTOPGROUPDESKTOPSREQUEST'].fields_by_name['order_by']._loaded_options = None
  _globals['_LISTDESKTOPGROUPDESKTOPSREQUEST'].fields_by_name['order_by']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTDESKTOPGROUPOPERATIONSREQUEST'].fields_by_name['desktop_group_id']._loaded_options = None
  _globals['_LISTDESKTOPGROUPOPERATIONSREQUEST'].fields_by_name['desktop_group_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTDESKTOPGROUPOPERATIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTDESKTOPGROUPOPERATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _globals['_LISTDESKTOPGROUPOPERATIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTDESKTOPGROUPOPERATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTDESKTOPGROUPOPERATIONSREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTDESKTOPGROUPOPERATIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _globals['_UPDATEDESKTOPGROUPREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_UPDATEDESKTOPGROUPREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_UPDATEDESKTOPGROUPREQUEST'].fields_by_name['desktop_group_id']._loaded_options = None
  _globals['_UPDATEDESKTOPGROUPREQUEST'].fields_by_name['desktop_group_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_UPDATEDESKTOPGROUPREQUEST'].fields_by_name['desktop_image_id']._loaded_options = None
  _globals['_UPDATEDESKTOPGROUPREQUEST'].fields_by_name['desktop_image_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_UPDATEDESKTOPGROUPREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_UPDATEDESKTOPGROUPREQUEST'].fields_by_name['name']._serialized_options = b'\362\3071\037|[a-z]([-a-z0-9]{0,61}[a-z0-9])'
  _globals['_UPDATEDESKTOPGROUPREQUEST'].fields_by_name['description']._loaded_options = None
  _globals['_UPDATEDESKTOPGROUPREQUEST'].fields_by_name['description']._serialized_options = b'\212\3101\006<=1024'
  _globals['_UPDATEDESKTOPGROUPREQUEST'].fields_by_name['labels']._loaded_options = None
  _globals['_UPDATEDESKTOPGROUPREQUEST'].fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\0041-63'
  _globals['_CREATEDESKTOPGROUPREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_CREATEDESKTOPGROUPREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_CREATEDESKTOPGROUPREQUEST'].fields_by_name['desktop_image_id']._loaded_options = None
  _globals['_CREATEDESKTOPGROUPREQUEST'].fields_by_name['desktop_image_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_CREATEDESKTOPGROUPREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_CREATEDESKTOPGROUPREQUEST'].fields_by_name['name']._serialized_options = b'\362\3071\036[a-z]([-a-z0-9]{0,61}[a-z0-9])'
  _globals['_CREATEDESKTOPGROUPREQUEST'].fields_by_name['description']._loaded_options = None
  _globals['_CREATEDESKTOPGROUPREQUEST'].fields_by_name['description']._serialized_options = b'\212\3101\006<=1024'
  _globals['_DELETEDESKTOPGROUPREQUEST'].fields_by_name['desktop_group_id']._loaded_options = None
  _globals['_DELETEDESKTOPGROUPREQUEST'].fields_by_name['desktop_group_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_DESKTOPGROUPSERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_DESKTOPGROUPSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\0024\0222/cloud-desktop/v1/desktopGroups/{desktop_group_id}'
  _globals['_DESKTOPGROUPSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_DESKTOPGROUPSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002!\022\037/cloud-desktop/v1/desktopGroups'
  _globals['_DESKTOPGROUPSERVICE'].methods_by_name['ListDesktops']._loaded_options = None
  _globals['_DESKTOPGROUPSERVICE'].methods_by_name['ListDesktops']._serialized_options = b'\202\323\344\223\002=\022;/cloud-desktop/v1/desktopGroups/{desktop_group_id}/desktops'
  _globals['_DESKTOPGROUPSERVICE'].methods_by_name['ListOperations']._loaded_options = None
  _globals['_DESKTOPGROUPSERVICE'].methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\002?\022=/cloud-desktop/v1/desktopGroups/{desktop_group_id}/operations'
  _globals['_DESKTOPGROUPSERVICE'].methods_by_name['Create']._loaded_options = None
  _globals['_DESKTOPGROUPSERVICE'].methods_by_name['Create']._serialized_options = b'\262\322**\n\032CreateDesktopGroupMetadata\022\014DesktopGroup\202\323\344\223\002$\"\037/cloud-desktop/v1/desktopGroups:\001*'
  _globals['_DESKTOPGROUPSERVICE'].methods_by_name['Update']._loaded_options = None
  _globals['_DESKTOPGROUPSERVICE'].methods_by_name['Update']._serialized_options = b'\262\322*3\n\032UpdateDesktopGroupMetadata\022\025google.protobuf.Empty\202\323\344\223\002722/cloud-desktop/v1/desktopGroups/{desktop_group_id}:\001*'
  _globals['_DESKTOPGROUPSERVICE'].methods_by_name['Delete']._loaded_options = None
  _globals['_DESKTOPGROUPSERVICE'].methods_by_name['Delete']._serialized_options = b'\262\322*3\n\032DeleteDesktopGroupMetadata\022\025google.protobuf.Empty\202\323\344\223\0024*2/cloud-desktop/v1/desktopGroups/{desktop_group_id}'
  _globals['_DESKTOPGROUPSERVICE'].methods_by_name['ListAccessBindings']._loaded_options = None
  _globals['_DESKTOPGROUPSERVICE'].methods_by_name['ListAccessBindings']._serialized_options = b'\202\323\344\223\002B\022@/cloud-desktop/v1/desktopGroups/{resource_id}:listAccessBindings'
  _globals['_DESKTOPGROUPSERVICE'].methods_by_name['SetAccessBindings']._loaded_options = None
  _globals['_DESKTOPGROUPSERVICE'].methods_by_name['SetAccessBindings']._serialized_options = b'\262\322*9\n access.SetAccessBindingsMetadata\022\025google.protobuf.Empty\202\323\344\223\002D\"?/cloud-desktop/v1/desktopGroups/{resource_id}:setAccessBindings:\001*'
  _globals['_DESKTOPGROUPSERVICE'].methods_by_name['UpdateAccessBindings']._loaded_options = None
  _globals['_DESKTOPGROUPSERVICE'].methods_by_name['UpdateAccessBindings']._serialized_options = b'\262\322*<\n#access.UpdateAccessBindingsMetadata\022\025google.protobuf.Empty\202\323\344\223\002G\"B/cloud-desktop/v1/desktopGroups/{resource_id}:updateAccessBindings:\001*'
  _globals['_GETDESKTOPGROUPREQUEST']._serialized_start=432
  _globals['_GETDESKTOPGROUPREQUEST']._serialized_end=496
  _globals['_LISTDESKTOPGROUPSREQUEST']._serialized_start=499
  _globals['_LISTDESKTOPGROUPSREQUEST']._serialized_end=683
  _globals['_LISTDESKTOPGROUPSRESPONSE']._serialized_start=686
  _globals['_LISTDESKTOPGROUPSRESPONSE']._serialized_end=816
  _globals['_LISTDESKTOPGROUPDESKTOPSREQUEST']._serialized_start=819
  _globals['_LISTDESKTOPGROUPDESKTOPSREQUEST']._serialized_end=1017
  _globals['_LISTDESKTOPGROUPDESKTOPSRESPONSE']._serialized_start=1019
  _globals['_LISTDESKTOPGROUPDESKTOPSRESPONSE']._serialized_end=1145
  _globals['_LISTDESKTOPGROUPOPERATIONSREQUEST']._serialized_start=1148
  _globals['_LISTDESKTOPGROUPOPERATIONSREQUEST']._serialized_end=1319
  _globals['_LISTDESKTOPGROUPOPERATIONSRESPONSE']._serialized_start=1321
  _globals['_LISTDESKTOPGROUPOPERATIONSRESPONSE']._serialized_end=1443
  _globals['_UPDATEDESKTOPGROUPREQUEST']._serialized_start=1446
  _globals['_UPDATEDESKTOPGROUPREQUEST']._serialized_end=2363
  _globals['_UPDATEDESKTOPGROUPREQUEST_LABELSENTRY']._serialized_start=2295
  _globals['_UPDATEDESKTOPGROUPREQUEST_LABELSENTRY']._serialized_end=2340
  _globals['_CREATEDESKTOPGROUPREQUEST']._serialized_start=2366
  _globals['_CREATEDESKTOPGROUPREQUEST']._serialized_end=2941
  _globals['_CREATEDESKTOPGROUPMETADATA']._serialized_start=2943
  _globals['_CREATEDESKTOPGROUPMETADATA']._serialized_end=2997
  _globals['_DELETEDESKTOPGROUPREQUEST']._serialized_start=2999
  _globals['_DELETEDESKTOPGROUPREQUEST']._serialized_end=3066
  _globals['_DELETEDESKTOPGROUPMETADATA']._serialized_start=3068
  _globals['_DELETEDESKTOPGROUPMETADATA']._serialized_end=3122
  _globals['_UPDATEDESKTOPGROUPMETADATA']._serialized_start=3124
  _globals['_UPDATEDESKTOPGROUPMETADATA']._serialized_end=3178
  _globals['_DESKTOPGROUPSERVICE']._serialized_start=3181
  _globals['_DESKTOPGROUPSERVICE']._serialized_end=5331
# @@protoc_insertion_point(module_scope)
