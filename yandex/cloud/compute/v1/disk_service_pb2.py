# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/compute/v1/disk_service.proto
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
    'yandex/cloud/compute/v1/disk_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.compute.v1 import disk_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_disk__pb2
from yandex.cloud.compute.v1 import hardware_generation_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_hardware__generation__pb2
from yandex.cloud.compute.v1 import snapshot_schedule_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*yandex/cloud/compute/v1/disk_service.proto\x12\x17yandex.cloud.compute.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/access/access.proto\x1a yandex/cloud/api/operation.proto\x1a\"yandex/cloud/compute/v1/disk.proto\x1a\x31yandex/cloud/compute/v1/hardware_generation.proto\x1a/yandex/cloud/compute/v1/snapshot_schedule.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"/\n\x0eGetDiskRequest\x12\x1d\n\x07\x64isk_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\xaa\x01\n\x10ListDisksRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\x12\x1b\n\x08order_by\x18\x05 \x01(\tB\t\x8a\xc8\x31\x05<=100\"Z\n\x11ListDisksResponse\x12,\n\x05\x64isks\x18\x01 \x03(\x0b\x32\x1d.yandex.cloud.compute.v1.Disk\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xdf\x05\n\x11\x43reateDiskRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x33\n\x04name\x18\x02 \x01(\tB%\xf2\xc7\x31!|[a-z]([-_a-z0-9]{0,61}[a-z0-9])?\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x8b\x01\n\x06labels\x18\x04 \x03(\x0b\x32\x36.yandex.cloud.compute.v1.CreateDiskRequest.LabelsEntryBC\xf2\xc7\x31\x0f[-_./\\@0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x1c\x12\x14[a-z][-_./\\@0-9a-z]*\x1a\x04\x31-63\x12\x19\n\x07type_id\x18\x05 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x1d\n\x07zone_id\x18\x06 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12,\n\x04size\x18\x07 \x01(\x03\x42\x1e\xe8\xc7\x31\x01\xfa\xc7\x31\x16\x34\x31\x39\x34\x33\x30\x34-28587302322176\x12\x1c\n\x08image_id\x18\x08 \x01(\tB\x08\x8a\xc8\x31\x04<=50H\x00\x12\x1f\n\x0bsnapshot_id\x18\t \x01(\tB\x08\x8a\xc8\x31\x04<=50H\x00\x12\x12\n\nblock_size\x18\n \x01(\x03\x12K\n\x15\x64isk_placement_policy\x18\x0b \x01(\x0b\x32,.yandex.cloud.compute.v1.DiskPlacementPolicy\x12\x1d\n\x15snapshot_schedule_ids\x18\x0c \x03(\t\x12H\n\x13hardware_generation\x18\r \x01(\x0b\x32+.yandex.cloud.compute.v1.HardwareGeneration\x12\x1c\n\nkms_key_id\x18\x0e \x01(\tB\x08\x8a\xc8\x31\x04<=50\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x08\n\x06source\"%\n\x12\x43reateDiskMetadata\x12\x0f\n\x07\x64isk_id\x18\x01 \x01(\t\"\xeb\x03\n\x11UpdateDiskRequest\x12\x1d\n\x07\x64isk_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x33\n\x04name\x18\x03 \x01(\tB%\xf2\xc7\x31!|[a-z]([-_a-z0-9]{0,61}[a-z0-9])?\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x8b\x01\n\x06labels\x18\x05 \x03(\x0b\x32\x36.yandex.cloud.compute.v1.UpdateDiskRequest.LabelsEntryBC\xf2\xc7\x31\x0f[-_./\\@0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x1c\x12\x14[a-z][-_./\\@0-9a-z]*\x1a\x04\x31-63\x12\'\n\x04size\x18\x06 \x01(\x03\x42\x19\xfa\xc7\x31\x15\x34\x31\x39\x34\x33\x30\x34-4398046511104\x12K\n\x15\x64isk_placement_policy\x18\x07 \x01(\x0b\x32,.yandex.cloud.compute.v1.DiskPlacementPolicy\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"%\n\x12UpdateDiskMetadata\x12\x0f\n\x07\x64isk_id\x18\x01 \x01(\t\"2\n\x11\x44\x65leteDiskRequest\x12\x1d\n\x07\x64isk_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"%\n\x12\x44\x65leteDiskMetadata\x12\x0f\n\x07\x64isk_id\x18\x01 \x01(\t\"x\n\x19ListDiskOperationsRequest\x12\x1d\n\x07\x64isk_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"l\n\x1aListDiskOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"]\n\x0fMoveDiskRequest\x12\x1d\n\x07\x64isk_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12+\n\x15\x64\x65stination_folder_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\\\n\x10MoveDiskMetadata\x12\x0f\n\x07\x64isk_id\x18\x01 \x01(\t\x12\x18\n\x10source_folder_id\x18\x02 \x01(\t\x12\x1d\n\x15\x64\x65stination_folder_id\x18\x03 \x01(\t\"\xac\x01\n\x13RelocateDiskRequest\x12\x1d\n\x07\x64isk_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12)\n\x13\x64\x65stination_zone_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12K\n\x15\x64isk_placement_policy\x18\x03 \x01(\x0b\x32,.yandex.cloud.compute.v1.DiskPlacementPolicy\"\\\n\x14RelocateDiskMetadata\x12\x0f\n\x07\x64isk_id\x18\x01 \x01(\t\x12\x16\n\x0esource_zone_id\x18\x02 \x01(\t\x12\x1b\n\x13\x64\x65stination_zone_id\x18\x03 \x01(\t\"Z\n ListDiskSnapshotSchedulesRequest\x12\x0f\n\x07\x64isk_id\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x03\x12\x12\n\npage_token\x18\x03 \x01(\t\"\x83\x01\n!ListDiskSnapshotSchedulesResponse\x12\x45\n\x12snapshot_schedules\x18\x01 \x03(\x0b\x32).yandex.cloud.compute.v1.SnapshotSchedule\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\x90\x10\n\x0b\x44iskService\x12r\n\x03Get\x12\'.yandex.cloud.compute.v1.GetDiskRequest\x1a\x1d.yandex.cloud.compute.v1.Disk\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/compute/v1/disks/{disk_id}\x12x\n\x04List\x12).yandex.cloud.compute.v1.ListDisksRequest\x1a*.yandex.cloud.compute.v1.ListDisksResponse\"\x19\x82\xd3\xe4\x93\x02\x13\x12\x11/compute/v1/disks\x12\x93\x01\n\x06\x43reate\x12*.yandex.cloud.compute.v1.CreateDiskRequest\x1a!.yandex.cloud.operation.Operation\":\xb2\xd2*\x1a\n\x12\x43reateDiskMetadata\x12\x04\x44isk\x82\xd3\xe4\x93\x02\x16\"\x11/compute/v1/disks:\x01*\x12\x9d\x01\n\x06Update\x12*.yandex.cloud.compute.v1.UpdateDiskRequest\x1a!.yandex.cloud.operation.Operation\"D\xb2\xd2*\x1a\n\x12UpdateDiskMetadata\x12\x04\x44isk\x82\xd3\xe4\x93\x02 2\x1b/compute/v1/disks/{disk_id}:\x01*\x12\xab\x01\n\x06\x44\x65lete\x12*.yandex.cloud.compute.v1.DeleteDiskRequest\x1a!.yandex.cloud.operation.Operation\"R\xb2\xd2*+\n\x12\x44\x65leteDiskMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x1d*\x1b/compute/v1/disks/{disk_id}\x12\xa9\x01\n\x0eListOperations\x12\x32.yandex.cloud.compute.v1.ListDiskOperationsRequest\x1a\x33.yandex.cloud.compute.v1.ListDiskOperationsResponse\".\x82\xd3\xe4\x93\x02(\x12&/compute/v1/disks/{disk_id}/operations\x12\x9c\x01\n\x04Move\x12(.yandex.cloud.compute.v1.MoveDiskRequest\x1a!.yandex.cloud.operation.Operation\"G\xb2\xd2*\x18\n\x10MoveDiskMetadata\x12\x04\x44isk\x82\xd3\xe4\x93\x02%\" /compute/v1/disks/{disk_id}:move:\x01*\x12\xac\x01\n\x08Relocate\x12,.yandex.cloud.compute.v1.RelocateDiskRequest\x1a!.yandex.cloud.operation.Operation\"O\xb2\xd2*\x1c\n\x14RelocateDiskMetadata\x12\x04\x44isk\x82\xd3\xe4\x93\x02)\"$/compute/v1/disks/{disk_id}:relocate:\x01*\x12\x8e\x01\n\x15ListSnapshotSchedules\x12\x39.yandex.cloud.compute.v1.ListDiskSnapshotSchedulesRequest\x1a:.yandex.cloud.compute.v1.ListDiskSnapshotSchedulesResponse\x12\xb1\x01\n\x12ListAccessBindings\x12..yandex.cloud.access.ListAccessBindingsRequest\x1a/.yandex.cloud.access.ListAccessBindingsResponse\":\x82\xd3\xe4\x93\x02\x34\x12\x32/compute/v1/disks/{resource_id}:listAccessBindings\x12\xf0\x01\n\x11SetAccessBindings\x12-.yandex.cloud.access.SetAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x88\x01\xb2\xd2*H\n access.SetAccessBindingsMetadata\x12$access.AccessBindingsOperationResult\x82\xd3\xe4\x93\x02\x36\"1/compute/v1/disks/{resource_id}:setAccessBindings:\x01*\x12\xfc\x01\n\x14UpdateAccessBindings\x12\x30.yandex.cloud.access.UpdateAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x8e\x01\xb2\xd2*K\n#access.UpdateAccessBindingsMetadata\x12$access.AccessBindingsOperationResult\x82\xd3\xe4\x93\x02\x39\"4/compute/v1/disks/{resource_id}:updateAccessBindings:\x01*Bb\n\x1byandex.cloud.api.compute.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;computeb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.compute.v1.disk_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033yandex.cloud.api.compute.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;compute'
  _globals['_GETDISKREQUEST'].fields_by_name['disk_id']._loaded_options = None
  _globals['_GETDISKREQUEST'].fields_by_name['disk_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTDISKSREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_LISTDISKSREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTDISKSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTDISKSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTDISKSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTDISKSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTDISKSREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTDISKSREQUEST'].fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _globals['_LISTDISKSREQUEST'].fields_by_name['order_by']._loaded_options = None
  _globals['_LISTDISKSREQUEST'].fields_by_name['order_by']._serialized_options = b'\212\3101\005<=100'
  _globals['_CREATEDISKREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_CREATEDISKREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_CREATEDISKREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_CREATEDISKREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_CREATEDISKREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_CREATEDISKREQUEST'].fields_by_name['name']._serialized_options = b'\362\3071!|[a-z]([-_a-z0-9]{0,61}[a-z0-9])?'
  _globals['_CREATEDISKREQUEST'].fields_by_name['description']._loaded_options = None
  _globals['_CREATEDISKREQUEST'].fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _globals['_CREATEDISKREQUEST'].fields_by_name['labels']._loaded_options = None
  _globals['_CREATEDISKREQUEST'].fields_by_name['labels']._serialized_options = b'\362\3071\017[-_./\\@0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\034\022\024[a-z][-_./\\@0-9a-z]*\032\0041-63'
  _globals['_CREATEDISKREQUEST'].fields_by_name['type_id']._loaded_options = None
  _globals['_CREATEDISKREQUEST'].fields_by_name['type_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_CREATEDISKREQUEST'].fields_by_name['zone_id']._loaded_options = None
  _globals['_CREATEDISKREQUEST'].fields_by_name['zone_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_CREATEDISKREQUEST'].fields_by_name['size']._loaded_options = None
  _globals['_CREATEDISKREQUEST'].fields_by_name['size']._serialized_options = b'\350\3071\001\372\3071\0264194304-28587302322176'
  _globals['_CREATEDISKREQUEST'].fields_by_name['image_id']._loaded_options = None
  _globals['_CREATEDISKREQUEST'].fields_by_name['image_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_CREATEDISKREQUEST'].fields_by_name['snapshot_id']._loaded_options = None
  _globals['_CREATEDISKREQUEST'].fields_by_name['snapshot_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_CREATEDISKREQUEST'].fields_by_name['kms_key_id']._loaded_options = None
  _globals['_CREATEDISKREQUEST'].fields_by_name['kms_key_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_UPDATEDISKREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_UPDATEDISKREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_UPDATEDISKREQUEST'].fields_by_name['disk_id']._loaded_options = None
  _globals['_UPDATEDISKREQUEST'].fields_by_name['disk_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_UPDATEDISKREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_UPDATEDISKREQUEST'].fields_by_name['name']._serialized_options = b'\362\3071!|[a-z]([-_a-z0-9]{0,61}[a-z0-9])?'
  _globals['_UPDATEDISKREQUEST'].fields_by_name['description']._loaded_options = None
  _globals['_UPDATEDISKREQUEST'].fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _globals['_UPDATEDISKREQUEST'].fields_by_name['labels']._loaded_options = None
  _globals['_UPDATEDISKREQUEST'].fields_by_name['labels']._serialized_options = b'\362\3071\017[-_./\\@0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\034\022\024[a-z][-_./\\@0-9a-z]*\032\0041-63'
  _globals['_UPDATEDISKREQUEST'].fields_by_name['size']._loaded_options = None
  _globals['_UPDATEDISKREQUEST'].fields_by_name['size']._serialized_options = b'\372\3071\0254194304-4398046511104'
  _globals['_DELETEDISKREQUEST'].fields_by_name['disk_id']._loaded_options = None
  _globals['_DELETEDISKREQUEST'].fields_by_name['disk_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTDISKOPERATIONSREQUEST'].fields_by_name['disk_id']._loaded_options = None
  _globals['_LISTDISKOPERATIONSREQUEST'].fields_by_name['disk_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTDISKOPERATIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTDISKOPERATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTDISKOPERATIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTDISKOPERATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_MOVEDISKREQUEST'].fields_by_name['disk_id']._loaded_options = None
  _globals['_MOVEDISKREQUEST'].fields_by_name['disk_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_MOVEDISKREQUEST'].fields_by_name['destination_folder_id']._loaded_options = None
  _globals['_MOVEDISKREQUEST'].fields_by_name['destination_folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_RELOCATEDISKREQUEST'].fields_by_name['disk_id']._loaded_options = None
  _globals['_RELOCATEDISKREQUEST'].fields_by_name['disk_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_RELOCATEDISKREQUEST'].fields_by_name['destination_zone_id']._loaded_options = None
  _globals['_RELOCATEDISKREQUEST'].fields_by_name['destination_zone_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_DISKSERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_DISKSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\035\022\033/compute/v1/disks/{disk_id}'
  _globals['_DISKSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_DISKSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002\023\022\021/compute/v1/disks'
  _globals['_DISKSERVICE'].methods_by_name['Create']._loaded_options = None
  _globals['_DISKSERVICE'].methods_by_name['Create']._serialized_options = b'\262\322*\032\n\022CreateDiskMetadata\022\004Disk\202\323\344\223\002\026\"\021/compute/v1/disks:\001*'
  _globals['_DISKSERVICE'].methods_by_name['Update']._loaded_options = None
  _globals['_DISKSERVICE'].methods_by_name['Update']._serialized_options = b'\262\322*\032\n\022UpdateDiskMetadata\022\004Disk\202\323\344\223\002 2\033/compute/v1/disks/{disk_id}:\001*'
  _globals['_DISKSERVICE'].methods_by_name['Delete']._loaded_options = None
  _globals['_DISKSERVICE'].methods_by_name['Delete']._serialized_options = b'\262\322*+\n\022DeleteDiskMetadata\022\025google.protobuf.Empty\202\323\344\223\002\035*\033/compute/v1/disks/{disk_id}'
  _globals['_DISKSERVICE'].methods_by_name['ListOperations']._loaded_options = None
  _globals['_DISKSERVICE'].methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\002(\022&/compute/v1/disks/{disk_id}/operations'
  _globals['_DISKSERVICE'].methods_by_name['Move']._loaded_options = None
  _globals['_DISKSERVICE'].methods_by_name['Move']._serialized_options = b'\262\322*\030\n\020MoveDiskMetadata\022\004Disk\202\323\344\223\002%\" /compute/v1/disks/{disk_id}:move:\001*'
  _globals['_DISKSERVICE'].methods_by_name['Relocate']._loaded_options = None
  _globals['_DISKSERVICE'].methods_by_name['Relocate']._serialized_options = b'\262\322*\034\n\024RelocateDiskMetadata\022\004Disk\202\323\344\223\002)\"$/compute/v1/disks/{disk_id}:relocate:\001*'
  _globals['_DISKSERVICE'].methods_by_name['ListAccessBindings']._loaded_options = None
  _globals['_DISKSERVICE'].methods_by_name['ListAccessBindings']._serialized_options = b'\202\323\344\223\0024\0222/compute/v1/disks/{resource_id}:listAccessBindings'
  _globals['_DISKSERVICE'].methods_by_name['SetAccessBindings']._loaded_options = None
  _globals['_DISKSERVICE'].methods_by_name['SetAccessBindings']._serialized_options = b'\262\322*H\n access.SetAccessBindingsMetadata\022$access.AccessBindingsOperationResult\202\323\344\223\0026\"1/compute/v1/disks/{resource_id}:setAccessBindings:\001*'
  _globals['_DISKSERVICE'].methods_by_name['UpdateAccessBindings']._loaded_options = None
  _globals['_DISKSERVICE'].methods_by_name['UpdateAccessBindings']._serialized_options = b'\262\322*K\n#access.UpdateAccessBindingsMetadata\022$access.AccessBindingsOperationResult\202\323\344\223\0029\"4/compute/v1/disks/{resource_id}:updateAccessBindings:\001*'
  _globals['_GETDISKREQUEST']._serialized_start=410
  _globals['_GETDISKREQUEST']._serialized_end=457
  _globals['_LISTDISKSREQUEST']._serialized_start=460
  _globals['_LISTDISKSREQUEST']._serialized_end=630
  _globals['_LISTDISKSRESPONSE']._serialized_start=632
  _globals['_LISTDISKSRESPONSE']._serialized_end=722
  _globals['_CREATEDISKREQUEST']._serialized_start=725
  _globals['_CREATEDISKREQUEST']._serialized_end=1460
  _globals['_CREATEDISKREQUEST_LABELSENTRY']._serialized_start=1405
  _globals['_CREATEDISKREQUEST_LABELSENTRY']._serialized_end=1450
  _globals['_CREATEDISKMETADATA']._serialized_start=1462
  _globals['_CREATEDISKMETADATA']._serialized_end=1499
  _globals['_UPDATEDISKREQUEST']._serialized_start=1502
  _globals['_UPDATEDISKREQUEST']._serialized_end=1993
  _globals['_UPDATEDISKREQUEST_LABELSENTRY']._serialized_start=1405
  _globals['_UPDATEDISKREQUEST_LABELSENTRY']._serialized_end=1450
  _globals['_UPDATEDISKMETADATA']._serialized_start=1995
  _globals['_UPDATEDISKMETADATA']._serialized_end=2032
  _globals['_DELETEDISKREQUEST']._serialized_start=2034
  _globals['_DELETEDISKREQUEST']._serialized_end=2084
  _globals['_DELETEDISKMETADATA']._serialized_start=2086
  _globals['_DELETEDISKMETADATA']._serialized_end=2123
  _globals['_LISTDISKOPERATIONSREQUEST']._serialized_start=2125
  _globals['_LISTDISKOPERATIONSREQUEST']._serialized_end=2245
  _globals['_LISTDISKOPERATIONSRESPONSE']._serialized_start=2247
  _globals['_LISTDISKOPERATIONSRESPONSE']._serialized_end=2355
  _globals['_MOVEDISKREQUEST']._serialized_start=2357
  _globals['_MOVEDISKREQUEST']._serialized_end=2450
  _globals['_MOVEDISKMETADATA']._serialized_start=2452
  _globals['_MOVEDISKMETADATA']._serialized_end=2544
  _globals['_RELOCATEDISKREQUEST']._serialized_start=2547
  _globals['_RELOCATEDISKREQUEST']._serialized_end=2719
  _globals['_RELOCATEDISKMETADATA']._serialized_start=2721
  _globals['_RELOCATEDISKMETADATA']._serialized_end=2813
  _globals['_LISTDISKSNAPSHOTSCHEDULESREQUEST']._serialized_start=2815
  _globals['_LISTDISKSNAPSHOTSCHEDULESREQUEST']._serialized_end=2905
  _globals['_LISTDISKSNAPSHOTSCHEDULESRESPONSE']._serialized_start=2908
  _globals['_LISTDISKSNAPSHOTSCHEDULESRESPONSE']._serialized_end=3039
  _globals['_DISKSERVICE']._serialized_start=3042
  _globals['_DISKSERVICE']._serialized_end=5106
# @@protoc_insertion_point(module_scope)
