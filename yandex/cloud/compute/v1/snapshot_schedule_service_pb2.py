# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/compute/v1/snapshot_schedule_service.proto
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
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.compute.v1 import disk_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_disk__pb2
from yandex.cloud.compute.v1 import snapshot_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__pb2
from yandex.cloud.compute.v1 import snapshot_schedule_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_snapshot__schedule__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7yandex/cloud/compute/v1/snapshot_schedule_service.proto\x12\x17yandex.cloud.compute.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x1egoogle/protobuf/duration.proto\x1a yandex/cloud/access/access.proto\x1a yandex/cloud/api/operation.proto\x1a\"yandex/cloud/compute/v1/disk.proto\x1a&yandex/cloud/compute/v1/snapshot.proto\x1a/yandex/cloud/compute/v1/snapshot_schedule.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\":\n\x1aGetSnapshotScheduleRequest\x12\x1c\n\x14snapshot_schedule_id\x18\x01 \x01(\t\"\xb6\x01\n\x1cListSnapshotSchedulesRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\x12\x1b\n\x08order_by\x18\x05 \x01(\tB\t\x8a\xc8\x31\x05<=100\"\x7f\n\x1dListSnapshotSchedulesResponse\x12\x45\n\x12snapshot_schedules\x18\x01 \x03(\x0b\x32).yandex.cloud.compute.v1.SnapshotSchedule\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xcf\x03\n\x1d\x43reateSnapshotScheduleRequest\x12\x11\n\tfolder_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12R\n\x06labels\x18\x04 \x03(\x0b\x32\x42.yandex.cloud.compute.v1.CreateSnapshotScheduleRequest.LabelsEntry\x12@\n\x0fschedule_policy\x18\x05 \x01(\x0b\x32\'.yandex.cloud.compute.v1.SchedulePolicy\x12\x35\n\x10retention_period\x18\x06 \x01(\x0b\x32\x19.google.protobuf.DurationH\x00\x12\x18\n\x0esnapshot_count\x18\x07 \x01(\x03H\x00\x12<\n\rsnapshot_spec\x18\x08 \x01(\x0b\x32%.yandex.cloud.compute.v1.SnapshotSpec\x12\x10\n\x08\x64isk_ids\x18\t \x03(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x12\n\x10retention_policy\">\n\x1e\x43reateSnapshotScheduleMetadata\x12\x1c\n\x14snapshot_schedule_id\x18\x01 \x01(\t\"\xf9\x03\n\x1dUpdateSnapshotScheduleRequest\x12\x1c\n\x14snapshot_schedule_id\x18\x01 \x01(\t\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12R\n\x06labels\x18\x05 \x03(\x0b\x32\x42.yandex.cloud.compute.v1.UpdateSnapshotScheduleRequest.LabelsEntry\x12@\n\x0fschedule_policy\x18\x06 \x01(\x0b\x32\'.yandex.cloud.compute.v1.SchedulePolicy\x12\x35\n\x10retention_period\x18\x07 \x01(\x0b\x32\x19.google.protobuf.DurationH\x00\x12\x18\n\x0esnapshot_count\x18\x08 \x01(\x03H\x00\x12<\n\rsnapshot_spec\x18\t \x01(\x0b\x32%.yandex.cloud.compute.v1.SnapshotSpec\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x12\n\x10retention_policy\">\n\x1eUpdateSnapshotScheduleMetadata\x12\x1c\n\x14snapshot_schedule_id\x18\x01 \x01(\t\"=\n\x1d\x44\x65leteSnapshotScheduleRequest\x12\x1c\n\x14snapshot_schedule_id\x18\x01 \x01(\t\">\n\x1e\x44\x65leteSnapshotScheduleMetadata\x12\x1c\n\x14snapshot_schedule_id\x18\x01 \x01(\t\">\n\x1e\x44isableSnapshotScheduleRequest\x12\x1c\n\x14snapshot_schedule_id\x18\x01 \x01(\t\"?\n\x1f\x44isableSnapshotScheduleMetadata\x12\x1c\n\x14snapshot_schedule_id\x18\x01 \x01(\t\"=\n\x1d\x45nableSnapshotScheduleRequest\x12\x1c\n\x14snapshot_schedule_id\x18\x01 \x01(\t\">\n\x1e\x45nableSnapshotScheduleMetadata\x12\x1c\n\x14snapshot_schedule_id\x18\x01 \x01(\t\"l\n%ListSnapshotScheduleOperationsRequest\x12\x1c\n\x14snapshot_schedule_id\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x03\x12\x12\n\npage_token\x18\x03 \x01(\t\"x\n&ListSnapshotScheduleOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"k\n$ListSnapshotScheduleSnapshotsRequest\x12\x1c\n\x14snapshot_schedule_id\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x03\x12\x12\n\npage_token\x18\x03 \x01(\t\"v\n%ListSnapshotScheduleSnapshotsResponse\x12\x34\n\tsnapshots\x18\x01 \x03(\x0b\x32!.yandex.cloud.compute.v1.Snapshot\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"g\n ListSnapshotScheduleDisksRequest\x12\x1c\n\x14snapshot_schedule_id\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x03\x12\x12\n\npage_token\x18\x03 \x01(\t\"j\n!ListSnapshotScheduleDisksResponse\x12,\n\x05\x64isks\x18\x01 \x03(\x0b\x32\x1d.yandex.cloud.compute.v1.Disk\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"_\n\"UpdateSnapshotScheduleDisksRequest\x12\x1c\n\x14snapshot_schedule_id\x18\x01 \x01(\t\x12\x0e\n\x06remove\x18\x02 \x03(\t\x12\x0b\n\x03\x61\x64\x64\x18\x03 \x03(\t\"C\n#UpdateSnapshotScheduleDisksMetadata\x12\x1c\n\x14snapshot_schedule_id\x18\x01 \x01(\t2\xee\x17\n\x17SnapshotScheduleService\x12\xa3\x01\n\x03Get\x12\x33.yandex.cloud.compute.v1.GetSnapshotScheduleRequest\x1a).yandex.cloud.compute.v1.SnapshotSchedule\"<\x82\xd3\xe4\x93\x02\x36\x12\x34/compute/v1/snapshotSchedules/{snapshot_schedule_id}\x12\x9c\x01\n\x04List\x12\x35.yandex.cloud.compute.v1.ListSnapshotSchedulesRequest\x1a\x36.yandex.cloud.compute.v1.ListSnapshotSchedulesResponse\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/compute/v1/snapshotSchedules\x12\xc3\x01\n\x06\x43reate\x12\x36.yandex.cloud.compute.v1.CreateSnapshotScheduleRequest\x1a!.yandex.cloud.operation.Operation\"^\xb2\xd2*2\n\x1e\x43reateSnapshotScheduleMetadata\x12\x10SnapshotSchedule\x82\xd3\xe4\x93\x02\"\"\x1d/compute/v1/snapshotSchedules:\x01*\x12\xda\x01\n\x06Update\x12\x36.yandex.cloud.compute.v1.UpdateSnapshotScheduleRequest\x1a!.yandex.cloud.operation.Operation\"u\xb2\xd2*2\n\x1eUpdateSnapshotScheduleMetadata\x12\x10SnapshotSchedule\x82\xd3\xe4\x93\x02\x39\x32\x34/compute/v1/snapshotSchedules/{snapshot_schedule_id}:\x01*\x12\xdc\x01\n\x06\x44\x65lete\x12\x36.yandex.cloud.compute.v1.DeleteSnapshotScheduleRequest\x1a!.yandex.cloud.operation.Operation\"w\xb2\xd2*7\n\x1e\x44\x65leteSnapshotScheduleMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x36*4/compute/v1/snapshotSchedules/{snapshot_schedule_id}\x12\xf6\x01\n\x0bUpdateDisks\x12;.yandex.cloud.compute.v1.UpdateSnapshotScheduleDisksRequest\x1a!.yandex.cloud.operation.Operation\"\x86\x01\xb2\xd2*7\n#UpdateSnapshotScheduleDisksMetadata\x12\x10SnapshotSchedule\x82\xd3\xe4\x93\x02\x45\x32@/compute/v1/snapshotSchedules/{snapshot_schedule_id}:updateDisks:\x01*\x12\xe5\x01\n\x07\x44isable\x12\x37.yandex.cloud.compute.v1.DisableSnapshotScheduleRequest\x1a!.yandex.cloud.operation.Operation\"~\xb2\xd2*3\n\x1f\x44isableSnapshotScheduleMetadata\x12\x10SnapshotSchedule\x82\xd3\xe4\x93\x02\x41\"</compute/v1/snapshotSchedules/{snapshot_schedule_id}:disable:\x01*\x12\xe1\x01\n\x06\x45nable\x12\x36.yandex.cloud.compute.v1.EnableSnapshotScheduleRequest\x1a!.yandex.cloud.operation.Operation\"|\xb2\xd2*2\n\x1e\x45nableSnapshotScheduleMetadata\x12\x10SnapshotSchedule\x82\xd3\xe4\x93\x02@\";/compute/v1/snapshotSchedules/{snapshot_schedule_id}:enable:\x01*\x12\xda\x01\n\x0eListOperations\x12>.yandex.cloud.compute.v1.ListSnapshotScheduleOperationsRequest\x1a?.yandex.cloud.compute.v1.ListSnapshotScheduleOperationsResponse\"G\x82\xd3\xe4\x93\x02\x41\x12?/compute/v1/snapshotSchedules/{snapshot_schedule_id}/operations\x12\xd6\x01\n\rListSnapshots\x12=.yandex.cloud.compute.v1.ListSnapshotScheduleSnapshotsRequest\x1a>.yandex.cloud.compute.v1.ListSnapshotScheduleSnapshotsResponse\"F\x82\xd3\xe4\x93\x02@\x12>/compute/v1/snapshotSchedules/{snapshot_schedule_id}/snapshots\x12\xc6\x01\n\tListDisks\x12\x39.yandex.cloud.compute.v1.ListSnapshotScheduleDisksRequest\x1a:.yandex.cloud.compute.v1.ListSnapshotScheduleDisksResponse\"B\x82\xd3\xe4\x93\x02<\x12:/compute/v1/snapshotSchedules/{snapshot_schedule_id}/disks\x12\xbd\x01\n\x12ListAccessBindings\x12..yandex.cloud.access.ListAccessBindingsRequest\x1a/.yandex.cloud.access.ListAccessBindingsResponse\"F\x82\xd3\xe4\x93\x02@\x12>/compute/v1/snapshotSchedules/{resource_id}:listAccessBindings\x12\xfc\x01\n\x11SetAccessBindings\x12-.yandex.cloud.access.SetAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x94\x01\xb2\xd2*H\n access.SetAccessBindingsMetadata\x12$access.AccessBindingsOperationResult\x82\xd3\xe4\x93\x02\x42\"=/compute/v1/snapshotSchedules/{resource_id}:setAccessBindings:\x01*\x12\x88\x02\n\x14UpdateAccessBindings\x12\x30.yandex.cloud.access.UpdateAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x9a\x01\xb2\xd2*K\n#access.UpdateAccessBindingsMetadata\x12$access.AccessBindingsOperationResult\x82\xd3\xe4\x93\x02\x45\"@/compute/v1/snapshotSchedules/{resource_id}:updateAccessBindings:\x01*Bb\n\x1byandex.cloud.api.compute.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;computeb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.compute.v1.snapshot_schedule_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033yandex.cloud.api.compute.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;compute'
  _globals['_LISTSNAPSHOTSCHEDULESREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_LISTSNAPSHOTSCHEDULESREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTSNAPSHOTSCHEDULESREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTSNAPSHOTSCHEDULESREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTSNAPSHOTSCHEDULESREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTSNAPSHOTSCHEDULESREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTSNAPSHOTSCHEDULESREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTSNAPSHOTSCHEDULESREQUEST'].fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _globals['_LISTSNAPSHOTSCHEDULESREQUEST'].fields_by_name['order_by']._loaded_options = None
  _globals['_LISTSNAPSHOTSCHEDULESREQUEST'].fields_by_name['order_by']._serialized_options = b'\212\3101\005<=100'
  _globals['_CREATESNAPSHOTSCHEDULEREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_CREATESNAPSHOTSCHEDULEREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_UPDATESNAPSHOTSCHEDULEREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_UPDATESNAPSHOTSCHEDULEREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_SNAPSHOTSCHEDULESERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_SNAPSHOTSCHEDULESERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\0026\0224/compute/v1/snapshotSchedules/{snapshot_schedule_id}'
  _globals['_SNAPSHOTSCHEDULESERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_SNAPSHOTSCHEDULESERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002\037\022\035/compute/v1/snapshotSchedules'
  _globals['_SNAPSHOTSCHEDULESERVICE'].methods_by_name['Create']._loaded_options = None
  _globals['_SNAPSHOTSCHEDULESERVICE'].methods_by_name['Create']._serialized_options = b'\262\322*2\n\036CreateSnapshotScheduleMetadata\022\020SnapshotSchedule\202\323\344\223\002\"\"\035/compute/v1/snapshotSchedules:\001*'
  _globals['_SNAPSHOTSCHEDULESERVICE'].methods_by_name['Update']._loaded_options = None
  _globals['_SNAPSHOTSCHEDULESERVICE'].methods_by_name['Update']._serialized_options = b'\262\322*2\n\036UpdateSnapshotScheduleMetadata\022\020SnapshotSchedule\202\323\344\223\002924/compute/v1/snapshotSchedules/{snapshot_schedule_id}:\001*'
  _globals['_SNAPSHOTSCHEDULESERVICE'].methods_by_name['Delete']._loaded_options = None
  _globals['_SNAPSHOTSCHEDULESERVICE'].methods_by_name['Delete']._serialized_options = b'\262\322*7\n\036DeleteSnapshotScheduleMetadata\022\025google.protobuf.Empty\202\323\344\223\0026*4/compute/v1/snapshotSchedules/{snapshot_schedule_id}'
  _globals['_SNAPSHOTSCHEDULESERVICE'].methods_by_name['UpdateDisks']._loaded_options = None
  _globals['_SNAPSHOTSCHEDULESERVICE'].methods_by_name['UpdateDisks']._serialized_options = b'\262\322*7\n#UpdateSnapshotScheduleDisksMetadata\022\020SnapshotSchedule\202\323\344\223\002E2@/compute/v1/snapshotSchedules/{snapshot_schedule_id}:updateDisks:\001*'
  _globals['_SNAPSHOTSCHEDULESERVICE'].methods_by_name['Disable']._loaded_options = None
  _globals['_SNAPSHOTSCHEDULESERVICE'].methods_by_name['Disable']._serialized_options = b'\262\322*3\n\037DisableSnapshotScheduleMetadata\022\020SnapshotSchedule\202\323\344\223\002A\"</compute/v1/snapshotSchedules/{snapshot_schedule_id}:disable:\001*'
  _globals['_SNAPSHOTSCHEDULESERVICE'].methods_by_name['Enable']._loaded_options = None
  _globals['_SNAPSHOTSCHEDULESERVICE'].methods_by_name['Enable']._serialized_options = b'\262\322*2\n\036EnableSnapshotScheduleMetadata\022\020SnapshotSchedule\202\323\344\223\002@\";/compute/v1/snapshotSchedules/{snapshot_schedule_id}:enable:\001*'
  _globals['_SNAPSHOTSCHEDULESERVICE'].methods_by_name['ListOperations']._loaded_options = None
  _globals['_SNAPSHOTSCHEDULESERVICE'].methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\002A\022?/compute/v1/snapshotSchedules/{snapshot_schedule_id}/operations'
  _globals['_SNAPSHOTSCHEDULESERVICE'].methods_by_name['ListSnapshots']._loaded_options = None
  _globals['_SNAPSHOTSCHEDULESERVICE'].methods_by_name['ListSnapshots']._serialized_options = b'\202\323\344\223\002@\022>/compute/v1/snapshotSchedules/{snapshot_schedule_id}/snapshots'
  _globals['_SNAPSHOTSCHEDULESERVICE'].methods_by_name['ListDisks']._loaded_options = None
  _globals['_SNAPSHOTSCHEDULESERVICE'].methods_by_name['ListDisks']._serialized_options = b'\202\323\344\223\002<\022:/compute/v1/snapshotSchedules/{snapshot_schedule_id}/disks'
  _globals['_SNAPSHOTSCHEDULESERVICE'].methods_by_name['ListAccessBindings']._loaded_options = None
  _globals['_SNAPSHOTSCHEDULESERVICE'].methods_by_name['ListAccessBindings']._serialized_options = b'\202\323\344\223\002@\022>/compute/v1/snapshotSchedules/{resource_id}:listAccessBindings'
  _globals['_SNAPSHOTSCHEDULESERVICE'].methods_by_name['SetAccessBindings']._loaded_options = None
  _globals['_SNAPSHOTSCHEDULESERVICE'].methods_by_name['SetAccessBindings']._serialized_options = b'\262\322*H\n access.SetAccessBindingsMetadata\022$access.AccessBindingsOperationResult\202\323\344\223\002B\"=/compute/v1/snapshotSchedules/{resource_id}:setAccessBindings:\001*'
  _globals['_SNAPSHOTSCHEDULESERVICE'].methods_by_name['UpdateAccessBindings']._loaded_options = None
  _globals['_SNAPSHOTSCHEDULESERVICE'].methods_by_name['UpdateAccessBindings']._serialized_options = b'\262\322*K\n#access.UpdateAccessBindingsMetadata\022$access.AccessBindingsOperationResult\202\323\344\223\002E\"@/compute/v1/snapshotSchedules/{resource_id}:updateAccessBindings:\001*'
  _globals['_GETSNAPSHOTSCHEDULEREQUEST']._serialized_start=444
  _globals['_GETSNAPSHOTSCHEDULEREQUEST']._serialized_end=502
  _globals['_LISTSNAPSHOTSCHEDULESREQUEST']._serialized_start=505
  _globals['_LISTSNAPSHOTSCHEDULESREQUEST']._serialized_end=687
  _globals['_LISTSNAPSHOTSCHEDULESRESPONSE']._serialized_start=689
  _globals['_LISTSNAPSHOTSCHEDULESRESPONSE']._serialized_end=816
  _globals['_CREATESNAPSHOTSCHEDULEREQUEST']._serialized_start=819
  _globals['_CREATESNAPSHOTSCHEDULEREQUEST']._serialized_end=1282
  _globals['_CREATESNAPSHOTSCHEDULEREQUEST_LABELSENTRY']._serialized_start=1217
  _globals['_CREATESNAPSHOTSCHEDULEREQUEST_LABELSENTRY']._serialized_end=1262
  _globals['_CREATESNAPSHOTSCHEDULEMETADATA']._serialized_start=1284
  _globals['_CREATESNAPSHOTSCHEDULEMETADATA']._serialized_end=1346
  _globals['_UPDATESNAPSHOTSCHEDULEREQUEST']._serialized_start=1349
  _globals['_UPDATESNAPSHOTSCHEDULEREQUEST']._serialized_end=1854
  _globals['_UPDATESNAPSHOTSCHEDULEREQUEST_LABELSENTRY']._serialized_start=1217
  _globals['_UPDATESNAPSHOTSCHEDULEREQUEST_LABELSENTRY']._serialized_end=1262
  _globals['_UPDATESNAPSHOTSCHEDULEMETADATA']._serialized_start=1856
  _globals['_UPDATESNAPSHOTSCHEDULEMETADATA']._serialized_end=1918
  _globals['_DELETESNAPSHOTSCHEDULEREQUEST']._serialized_start=1920
  _globals['_DELETESNAPSHOTSCHEDULEREQUEST']._serialized_end=1981
  _globals['_DELETESNAPSHOTSCHEDULEMETADATA']._serialized_start=1983
  _globals['_DELETESNAPSHOTSCHEDULEMETADATA']._serialized_end=2045
  _globals['_DISABLESNAPSHOTSCHEDULEREQUEST']._serialized_start=2047
  _globals['_DISABLESNAPSHOTSCHEDULEREQUEST']._serialized_end=2109
  _globals['_DISABLESNAPSHOTSCHEDULEMETADATA']._serialized_start=2111
  _globals['_DISABLESNAPSHOTSCHEDULEMETADATA']._serialized_end=2174
  _globals['_ENABLESNAPSHOTSCHEDULEREQUEST']._serialized_start=2176
  _globals['_ENABLESNAPSHOTSCHEDULEREQUEST']._serialized_end=2237
  _globals['_ENABLESNAPSHOTSCHEDULEMETADATA']._serialized_start=2239
  _globals['_ENABLESNAPSHOTSCHEDULEMETADATA']._serialized_end=2301
  _globals['_LISTSNAPSHOTSCHEDULEOPERATIONSREQUEST']._serialized_start=2303
  _globals['_LISTSNAPSHOTSCHEDULEOPERATIONSREQUEST']._serialized_end=2411
  _globals['_LISTSNAPSHOTSCHEDULEOPERATIONSRESPONSE']._serialized_start=2413
  _globals['_LISTSNAPSHOTSCHEDULEOPERATIONSRESPONSE']._serialized_end=2533
  _globals['_LISTSNAPSHOTSCHEDULESNAPSHOTSREQUEST']._serialized_start=2535
  _globals['_LISTSNAPSHOTSCHEDULESNAPSHOTSREQUEST']._serialized_end=2642
  _globals['_LISTSNAPSHOTSCHEDULESNAPSHOTSRESPONSE']._serialized_start=2644
  _globals['_LISTSNAPSHOTSCHEDULESNAPSHOTSRESPONSE']._serialized_end=2762
  _globals['_LISTSNAPSHOTSCHEDULEDISKSREQUEST']._serialized_start=2764
  _globals['_LISTSNAPSHOTSCHEDULEDISKSREQUEST']._serialized_end=2867
  _globals['_LISTSNAPSHOTSCHEDULEDISKSRESPONSE']._serialized_start=2869
  _globals['_LISTSNAPSHOTSCHEDULEDISKSRESPONSE']._serialized_end=2975
  _globals['_UPDATESNAPSHOTSCHEDULEDISKSREQUEST']._serialized_start=2977
  _globals['_UPDATESNAPSHOTSCHEDULEDISKSREQUEST']._serialized_end=3072
  _globals['_UPDATESNAPSHOTSCHEDULEDISKSMETADATA']._serialized_start=3074
  _globals['_UPDATESNAPSHOTSCHEDULEDISKSMETADATA']._serialized_end=3141
  _globals['_SNAPSHOTSCHEDULESERVICE']._serialized_start=3144
  _globals['_SNAPSHOTSCHEDULESERVICE']._serialized_end=6198
# @@protoc_insertion_point(module_scope)
