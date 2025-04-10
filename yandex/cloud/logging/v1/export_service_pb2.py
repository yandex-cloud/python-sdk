# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/logging/v1/export_service.proto
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
    'yandex/cloud/logging/v1/export_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.logging.v1 import export_pb2 as yandex_dot_cloud_dot_logging_dot_v1_dot_export__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,yandex/cloud/logging/v1/export_service.proto\x12\x17yandex.cloud.logging.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a yandex/cloud/access/access.proto\x1a yandex/cloud/api/operation.proto\x1a$yandex/cloud/logging/v1/export.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"\x8f\x02\n\x10RunExportRequest\x12\x1e\n\x08group_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=64\x12\x1d\n\x07sink_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=64\x12;\n\x06params\x18\x03 \x01(\x0b\x32%.yandex.cloud.logging.v1.ExportParamsB\x04\xe8\xc7\x31\x01\x12\x1d\n\x0fresult_filename\x18\x04 \x01(\tB\x04\xe8\xc7\x31\x01\x12/\n\x05since\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe8\xc7\x31\x01\x12/\n\x05until\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe8\xc7\x31\x01\"\xdb\x01\n\x10RunExportDetails\x12\x10\n\x08group_id\x18\x01 \x01(\t\x12\x0f\n\x07sink_id\x18\x02 \x01(\t\x12\x35\n\x06params\x18\x03 \x01(\x0b\x32%.yandex.cloud.logging.v1.ExportParams\x12\x17\n\x0fresult_filename\x18\x04 \x01(\t\x12)\n\x05since\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12)\n\x05until\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"O\n\x11RunExportMetadata\x12\x10\n\x08group_id\x18\x01 \x01(\t\x12\x0f\n\x07sink_id\x18\x02 \x01(\t\x12\x17\n\x0fresult_filename\x18\x03 \x01(\t\"3\n\x10GetExportRequest\x12\x1f\n\texport_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=64\"\x89\x01\n\x12ListExportsRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=64\x12\x11\n\tpage_size\x18\x03 \x01(\x03\x12\x1d\n\npage_token\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x05 \x01(\tB\n\x8a\xc8\x31\x06<=1000J\x04\x08\x02\x10\x03\"`\n\x13ListExportsResponse\x12\x30\n\x07\x65xports\x18\x01 \x03(\x0b\x32\x1f.yandex.cloud.logging.v1.Export\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xba\x03\n\x13\x43reateExportRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=64\x12/\n\x04name\x18\x02 \x01(\tB!\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x85\x01\n\x06labels\x18\x04 \x03(\x0b\x32\x38.yandex.cloud.logging.v1.CreateExportRequest.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04\x31-63\x12\x1e\n\x08group_id\x18\x05 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=64\x12\x1d\n\x07sink_id\x18\x06 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=64\x12;\n\x06params\x18\x07 \x01(\x0b\x32%.yandex.cloud.logging.v1.ExportParamsB\x04\xe8\xc7\x31\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\")\n\x14\x43reateExportMetadata\x12\x11\n\texport_id\x18\x01 \x01(\t\"\xeb\x03\n\x13UpdateExportRequest\x12\x1f\n\texport_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=64\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12/\n\x04name\x18\x03 \x01(\tB!\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x85\x01\n\x06labels\x18\x05 \x03(\x0b\x32\x38.yandex.cloud.logging.v1.UpdateExportRequest.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04\x31-63\x12\x1e\n\x08group_id\x18\x06 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=64\x12\x1d\n\x07sink_id\x18\x07 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=64\x12;\n\x06params\x18\x08 \x01(\x0b\x32%.yandex.cloud.logging.v1.ExportParamsB\x04\xe8\xc7\x31\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\")\n\x14UpdateExportMetadata\x12\x11\n\texport_id\x18\x01 \x01(\t\"6\n\x13\x44\x65leteExportRequest\x12\x1f\n\texport_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=64\")\n\x14\x44\x65leteExportMetadata\x12\x11\n\texport_id\x18\x01 \x01(\t\"\x98\x01\n\x1bListExportOperationsRequest\x12\x1f\n\texport_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=64\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"n\n\x1cListExportOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xec\r\n\rExportService\x12\x9f\x01\n\x03Run\x12).yandex.cloud.logging.v1.RunExportRequest\x1a!.yandex.cloud.operation.Operation\"J\xb2\xd2*%\n\x11RunExportMetadata\x12\x10RunExportDetails\x82\xd3\xe4\x93\x02\x1b\"\x16/logging/v1/run-export:\x01*\x12z\n\x03Get\x12).yandex.cloud.logging.v1.GetExportRequest\x1a\x1f.yandex.cloud.logging.v1.Export\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/logging/v1/exports/{export_id}\x12~\n\x04List\x12+.yandex.cloud.logging.v1.ListExportsRequest\x1a,.yandex.cloud.logging.v1.ListExportsResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\x12\x13/logging/v1/exports\x12\x9b\x01\n\x06\x43reate\x12,.yandex.cloud.logging.v1.CreateExportRequest\x1a!.yandex.cloud.operation.Operation\"@\xb2\xd2*\x1e\n\x14\x43reateExportMetadata\x12\x06\x45xport\x82\xd3\xe4\x93\x02\x18\"\x13/logging/v1/exports:\x01*\x12\xa7\x01\n\x06Update\x12,.yandex.cloud.logging.v1.UpdateExportRequest\x1a!.yandex.cloud.operation.Operation\"L\xb2\xd2*\x1e\n\x14UpdateExportMetadata\x12\x06\x45xport\x82\xd3\xe4\x93\x02$2\x1f/logging/v1/exports/{export_id}:\x01*\x12\xb3\x01\n\x06\x44\x65lete\x12,.yandex.cloud.logging.v1.DeleteExportRequest\x1a!.yandex.cloud.operation.Operation\"X\xb2\xd2*-\n\x14\x44\x65leteExportMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02!*\x1f/logging/v1/exports/{export_id}\x12\xb1\x01\n\x0eListOperations\x12\x34.yandex.cloud.logging.v1.ListExportOperationsRequest\x1a\x35.yandex.cloud.logging.v1.ListExportOperationsResponse\"2\x82\xd3\xe4\x93\x02,\x12*/logging/v1/exports/{export_id}/operations\x12\xb3\x01\n\x12ListAccessBindings\x12..yandex.cloud.access.ListAccessBindingsRequest\x1a/.yandex.cloud.access.ListAccessBindingsResponse\"<\x82\xd3\xe4\x93\x02\x36\x12\x34/logging/v1/exports/{resource_id}:listAccessBindings\x12\xe2\x01\n\x11SetAccessBindings\x12-.yandex.cloud.access.SetAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"{\xb2\xd2*9\n access.SetAccessBindingsMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x38\"3/logging/v1/exports/{resource_id}:setAccessBindings:\x01*\x12\xef\x01\n\x14UpdateAccessBindings\x12\x30.yandex.cloud.access.UpdateAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x81\x01\xb2\xd2*<\n#access.UpdateAccessBindingsMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02;26/logging/v1/exports/{resource_id}:updateAccessBindings:\x01*Bb\n\x1byandex.cloud.api.logging.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/logging/v1;loggingb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.logging.v1.export_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033yandex.cloud.api.logging.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/logging/v1;logging'
  _globals['_RUNEXPORTREQUEST'].fields_by_name['group_id']._loaded_options = None
  _globals['_RUNEXPORTREQUEST'].fields_by_name['group_id']._serialized_options = b'\350\3071\001\212\3101\004<=64'
  _globals['_RUNEXPORTREQUEST'].fields_by_name['sink_id']._loaded_options = None
  _globals['_RUNEXPORTREQUEST'].fields_by_name['sink_id']._serialized_options = b'\350\3071\001\212\3101\004<=64'
  _globals['_RUNEXPORTREQUEST'].fields_by_name['params']._loaded_options = None
  _globals['_RUNEXPORTREQUEST'].fields_by_name['params']._serialized_options = b'\350\3071\001'
  _globals['_RUNEXPORTREQUEST'].fields_by_name['result_filename']._loaded_options = None
  _globals['_RUNEXPORTREQUEST'].fields_by_name['result_filename']._serialized_options = b'\350\3071\001'
  _globals['_RUNEXPORTREQUEST'].fields_by_name['since']._loaded_options = None
  _globals['_RUNEXPORTREQUEST'].fields_by_name['since']._serialized_options = b'\350\3071\001'
  _globals['_RUNEXPORTREQUEST'].fields_by_name['until']._loaded_options = None
  _globals['_RUNEXPORTREQUEST'].fields_by_name['until']._serialized_options = b'\350\3071\001'
  _globals['_GETEXPORTREQUEST'].fields_by_name['export_id']._loaded_options = None
  _globals['_GETEXPORTREQUEST'].fields_by_name['export_id']._serialized_options = b'\350\3071\001\212\3101\004<=64'
  _globals['_LISTEXPORTSREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_LISTEXPORTSREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=64'
  _globals['_LISTEXPORTSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTEXPORTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTEXPORTSREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTEXPORTSREQUEST'].fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _globals['_CREATEEXPORTREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_CREATEEXPORTREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_CREATEEXPORTREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_CREATEEXPORTREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=64'
  _globals['_CREATEEXPORTREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_CREATEEXPORTREQUEST'].fields_by_name['name']._serialized_options = b'\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _globals['_CREATEEXPORTREQUEST'].fields_by_name['description']._loaded_options = None
  _globals['_CREATEEXPORTREQUEST'].fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _globals['_CREATEEXPORTREQUEST'].fields_by_name['labels']._loaded_options = None
  _globals['_CREATEEXPORTREQUEST'].fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\0041-63'
  _globals['_CREATEEXPORTREQUEST'].fields_by_name['group_id']._loaded_options = None
  _globals['_CREATEEXPORTREQUEST'].fields_by_name['group_id']._serialized_options = b'\350\3071\001\212\3101\004<=64'
  _globals['_CREATEEXPORTREQUEST'].fields_by_name['sink_id']._loaded_options = None
  _globals['_CREATEEXPORTREQUEST'].fields_by_name['sink_id']._serialized_options = b'\350\3071\001\212\3101\004<=64'
  _globals['_CREATEEXPORTREQUEST'].fields_by_name['params']._loaded_options = None
  _globals['_CREATEEXPORTREQUEST'].fields_by_name['params']._serialized_options = b'\350\3071\001'
  _globals['_UPDATEEXPORTREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_UPDATEEXPORTREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_UPDATEEXPORTREQUEST'].fields_by_name['export_id']._loaded_options = None
  _globals['_UPDATEEXPORTREQUEST'].fields_by_name['export_id']._serialized_options = b'\350\3071\001\212\3101\004<=64'
  _globals['_UPDATEEXPORTREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_UPDATEEXPORTREQUEST'].fields_by_name['name']._serialized_options = b'\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _globals['_UPDATEEXPORTREQUEST'].fields_by_name['description']._loaded_options = None
  _globals['_UPDATEEXPORTREQUEST'].fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _globals['_UPDATEEXPORTREQUEST'].fields_by_name['labels']._loaded_options = None
  _globals['_UPDATEEXPORTREQUEST'].fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\0041-63'
  _globals['_UPDATEEXPORTREQUEST'].fields_by_name['group_id']._loaded_options = None
  _globals['_UPDATEEXPORTREQUEST'].fields_by_name['group_id']._serialized_options = b'\350\3071\001\212\3101\004<=64'
  _globals['_UPDATEEXPORTREQUEST'].fields_by_name['sink_id']._loaded_options = None
  _globals['_UPDATEEXPORTREQUEST'].fields_by_name['sink_id']._serialized_options = b'\350\3071\001\212\3101\004<=64'
  _globals['_UPDATEEXPORTREQUEST'].fields_by_name['params']._loaded_options = None
  _globals['_UPDATEEXPORTREQUEST'].fields_by_name['params']._serialized_options = b'\350\3071\001'
  _globals['_DELETEEXPORTREQUEST'].fields_by_name['export_id']._loaded_options = None
  _globals['_DELETEEXPORTREQUEST'].fields_by_name['export_id']._serialized_options = b'\350\3071\001\212\3101\004<=64'
  _globals['_LISTEXPORTOPERATIONSREQUEST'].fields_by_name['export_id']._loaded_options = None
  _globals['_LISTEXPORTOPERATIONSREQUEST'].fields_by_name['export_id']._serialized_options = b'\350\3071\001\212\3101\004<=64'
  _globals['_LISTEXPORTOPERATIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTEXPORTOPERATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _globals['_LISTEXPORTOPERATIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTEXPORTOPERATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTEXPORTOPERATIONSREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTEXPORTOPERATIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _globals['_EXPORTSERVICE'].methods_by_name['Run']._loaded_options = None
  _globals['_EXPORTSERVICE'].methods_by_name['Run']._serialized_options = b'\262\322*%\n\021RunExportMetadata\022\020RunExportDetails\202\323\344\223\002\033\"\026/logging/v1/run-export:\001*'
  _globals['_EXPORTSERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_EXPORTSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002!\022\037/logging/v1/exports/{export_id}'
  _globals['_EXPORTSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_EXPORTSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002\025\022\023/logging/v1/exports'
  _globals['_EXPORTSERVICE'].methods_by_name['Create']._loaded_options = None
  _globals['_EXPORTSERVICE'].methods_by_name['Create']._serialized_options = b'\262\322*\036\n\024CreateExportMetadata\022\006Export\202\323\344\223\002\030\"\023/logging/v1/exports:\001*'
  _globals['_EXPORTSERVICE'].methods_by_name['Update']._loaded_options = None
  _globals['_EXPORTSERVICE'].methods_by_name['Update']._serialized_options = b'\262\322*\036\n\024UpdateExportMetadata\022\006Export\202\323\344\223\002$2\037/logging/v1/exports/{export_id}:\001*'
  _globals['_EXPORTSERVICE'].methods_by_name['Delete']._loaded_options = None
  _globals['_EXPORTSERVICE'].methods_by_name['Delete']._serialized_options = b'\262\322*-\n\024DeleteExportMetadata\022\025google.protobuf.Empty\202\323\344\223\002!*\037/logging/v1/exports/{export_id}'
  _globals['_EXPORTSERVICE'].methods_by_name['ListOperations']._loaded_options = None
  _globals['_EXPORTSERVICE'].methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\002,\022*/logging/v1/exports/{export_id}/operations'
  _globals['_EXPORTSERVICE'].methods_by_name['ListAccessBindings']._loaded_options = None
  _globals['_EXPORTSERVICE'].methods_by_name['ListAccessBindings']._serialized_options = b'\202\323\344\223\0026\0224/logging/v1/exports/{resource_id}:listAccessBindings'
  _globals['_EXPORTSERVICE'].methods_by_name['SetAccessBindings']._loaded_options = None
  _globals['_EXPORTSERVICE'].methods_by_name['SetAccessBindings']._serialized_options = b'\262\322*9\n access.SetAccessBindingsMetadata\022\025google.protobuf.Empty\202\323\344\223\0028\"3/logging/v1/exports/{resource_id}:setAccessBindings:\001*'
  _globals['_EXPORTSERVICE'].methods_by_name['UpdateAccessBindings']._loaded_options = None
  _globals['_EXPORTSERVICE'].methods_by_name['UpdateAccessBindings']._serialized_options = b'\262\322*<\n#access.UpdateAccessBindingsMetadata\022\025google.protobuf.Empty\202\323\344\223\002;26/logging/v1/exports/{resource_id}:updateAccessBindings:\001*'
  _globals['_RUNEXPORTREQUEST']._serialized_start=348
  _globals['_RUNEXPORTREQUEST']._serialized_end=619
  _globals['_RUNEXPORTDETAILS']._serialized_start=622
  _globals['_RUNEXPORTDETAILS']._serialized_end=841
  _globals['_RUNEXPORTMETADATA']._serialized_start=843
  _globals['_RUNEXPORTMETADATA']._serialized_end=922
  _globals['_GETEXPORTREQUEST']._serialized_start=924
  _globals['_GETEXPORTREQUEST']._serialized_end=975
  _globals['_LISTEXPORTSREQUEST']._serialized_start=978
  _globals['_LISTEXPORTSREQUEST']._serialized_end=1115
  _globals['_LISTEXPORTSRESPONSE']._serialized_start=1117
  _globals['_LISTEXPORTSRESPONSE']._serialized_end=1213
  _globals['_CREATEEXPORTREQUEST']._serialized_start=1216
  _globals['_CREATEEXPORTREQUEST']._serialized_end=1658
  _globals['_CREATEEXPORTREQUEST_LABELSENTRY']._serialized_start=1613
  _globals['_CREATEEXPORTREQUEST_LABELSENTRY']._serialized_end=1658
  _globals['_CREATEEXPORTMETADATA']._serialized_start=1660
  _globals['_CREATEEXPORTMETADATA']._serialized_end=1701
  _globals['_UPDATEEXPORTREQUEST']._serialized_start=1704
  _globals['_UPDATEEXPORTREQUEST']._serialized_end=2195
  _globals['_UPDATEEXPORTREQUEST_LABELSENTRY']._serialized_start=1613
  _globals['_UPDATEEXPORTREQUEST_LABELSENTRY']._serialized_end=1658
  _globals['_UPDATEEXPORTMETADATA']._serialized_start=2197
  _globals['_UPDATEEXPORTMETADATA']._serialized_end=2238
  _globals['_DELETEEXPORTREQUEST']._serialized_start=2240
  _globals['_DELETEEXPORTREQUEST']._serialized_end=2294
  _globals['_DELETEEXPORTMETADATA']._serialized_start=2296
  _globals['_DELETEEXPORTMETADATA']._serialized_end=2337
  _globals['_LISTEXPORTOPERATIONSREQUEST']._serialized_start=2340
  _globals['_LISTEXPORTOPERATIONSREQUEST']._serialized_end=2492
  _globals['_LISTEXPORTOPERATIONSRESPONSE']._serialized_start=2494
  _globals['_LISTEXPORTOPERATIONSRESPONSE']._serialized_end=2604
  _globals['_EXPORTSERVICE']._serialized_start=2607
  _globals['_EXPORTSERVICE']._serialized_end=4379
# @@protoc_insertion_point(module_scope)
