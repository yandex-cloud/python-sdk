# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/backup/v1/resource_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.backup.v1 import resource_pb2 as yandex_dot_cloud_dot_backup_dot_v1_dot_resource__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-yandex/cloud/backup/v1/resource_service.proto\x12\x16yandex.cloud.backup.v1\x1a\x1cgoogle/api/annotations.proto\x1a yandex/cloud/api/operation.proto\x1a%yandex/cloud/backup/v1/resource.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"u\n\x14ListResourcesRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"e\n\x15ListResourcesResponse\x12\x33\n\tresources\x18\x01 \x03(\x0b\x32 .yandex.cloud.backup.v1.Resource\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"?\n\x12GetResourceRequest\x12)\n\x13\x63ompute_instance_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"I\n\x13GetResourceResponse\x12\x32\n\x08resource\x18\x01 \x01(\x0b\x32 .yandex.cloud.backup.v1.Resource\"]\n\x15\x44\x65leteResourceRequest\x12)\n\x13\x63ompute_instance_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x19\n\x0bresource_id\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\"5\n\x16\x44\x65leteResourceMetadata\x12\x1b\n\x13\x63ompute_instance_id\x18\x01 \x01(\t\"{\n\x10ListTasksRequest\x12)\n\x13\x63ompute_instance_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"Y\n\x11ListTasksResponse\x12+\n\x05tasks\x18\x01 \x03(\x0b\x32\x1c.yandex.cloud.backup.v1.Task\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"n\n\x14ListDirectoryRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12!\n\x13\x63ompute_instance_id\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x12\n\x04path\x18\x03 \x01(\tB\x04\xe8\xc7\x31\x00\"\xfd\x02\n\x15ListDirectoryResponse\x12K\n\x05items\x18\x01 \x03(\x0b\x32<.yandex.cloud.backup.v1.ListDirectoryResponse.FilesystemItem\x1a\x96\x02\n\x0e\x46ilesystemItem\x12\x0c\n\x04name\x18\x01 \x01(\t\x12O\n\x04type\x18\x02 \x01(\x0e\x32\x41.yandex.cloud.backup.v1.ListDirectoryResponse.FilesystemItem.Type\x12T\n\tfile_type\x18\x03 \x01(\x0e\x32\x41.yandex.cloud.backup.v1.ListDirectoryResponse.FilesystemItem.Type\x12\x0c\n\x04size\x18\x04 \x01(\x03\"A\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06VOLUME\x10\x01\x12\r\n\tDIRECTORY\x10\x02\x12\x08\n\x04\x46ILE\x10\x03\"p\n\x16\x43reateDirectoryRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12!\n\x13\x63ompute_instance_id\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x12\n\x04path\x18\x03 \x01(\tB\x04\xe8\xc7\x31\x01\"D\n\x17\x43reateDirectoryMetadata\x12\x1b\n\x13\x63ompute_instance_id\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\"\x88\x01\n\x1dListResourceOperationsRequest\x12)\n\x13\x63ompute_instance_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"p\n\x1eListResourceOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\x97\x08\n\x0fResourceService\x12\x81\x01\n\x04List\x12,.yandex.cloud.backup.v1.ListResourcesRequest\x1a-.yandex.cloud.backup.v1.ListResourcesResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/backup/v1/resources\x12\x92\x01\n\x03Get\x12*.yandex.cloud.backup.v1.GetResourceRequest\x1a+.yandex.cloud.backup.v1.GetResourceResponse\"2\x82\xd3\xe4\x93\x02,\x12*/backup/v1/resources/{compute_instance_id}\x12\xc1\x01\n\x06\x44\x65lete\x12-.yandex.cloud.backup.v1.DeleteResourceRequest\x1a!.yandex.cloud.operation.Operation\"e\xb2\xd2*/\n\x16\x44\x65leteResourceMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02,**/backup/v1/resources/{compute_instance_id}\x12\x9a\x01\n\tListTasks\x12(.yandex.cloud.backup.v1.ListTasksRequest\x1a).yandex.cloud.backup.v1.ListTasksResponse\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/backup/v1/resources/{compute_instance_id}/tasks\x12l\n\rListDirectory\x12,.yandex.cloud.backup.v1.ListDirectoryRequest\x1a-.yandex.cloud.backup.v1.ListDirectoryResponse\x12\x9a\x01\n\x0f\x43reateDirectory\x12..yandex.cloud.backup.v1.CreateDirectoryRequest\x1a!.yandex.cloud.operation.Operation\"4\xb2\xd2*0\n\x17\x43reateDirectoryMetadata\x12\x15google.protobuf.Empty\x12\x7f\n\x0eListOperations\x12\x35.yandex.cloud.backup.v1.ListResourceOperationsRequest\x1a\x36.yandex.cloud.backup.v1.ListResourceOperationsResponseB_\n\x1ayandex.cloud.api.backup.v1ZAgithub.com/yandex-cloud/go-genproto/yandex/cloud/backup/v1;backupb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.backup.v1.resource_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032yandex.cloud.api.backup.v1ZAgithub.com/yandex-cloud/go-genproto/yandex/cloud/backup/v1;backup'
  _globals['_LISTRESOURCESREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_LISTRESOURCESREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTRESOURCESREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTRESOURCESREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTRESOURCESREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTRESOURCESREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_GETRESOURCEREQUEST'].fields_by_name['compute_instance_id']._loaded_options = None
  _globals['_GETRESOURCEREQUEST'].fields_by_name['compute_instance_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_DELETERESOURCEREQUEST'].fields_by_name['compute_instance_id']._loaded_options = None
  _globals['_DELETERESOURCEREQUEST'].fields_by_name['compute_instance_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_DELETERESOURCEREQUEST'].fields_by_name['resource_id']._loaded_options = None
  _globals['_DELETERESOURCEREQUEST'].fields_by_name['resource_id']._serialized_options = b'\350\3071\001'
  _globals['_LISTTASKSREQUEST'].fields_by_name['compute_instance_id']._loaded_options = None
  _globals['_LISTTASKSREQUEST'].fields_by_name['compute_instance_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTTASKSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTTASKSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTTASKSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTTASKSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTDIRECTORYREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_LISTDIRECTORYREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTDIRECTORYREQUEST'].fields_by_name['compute_instance_id']._loaded_options = None
  _globals['_LISTDIRECTORYREQUEST'].fields_by_name['compute_instance_id']._serialized_options = b'\350\3071\001'
  _globals['_LISTDIRECTORYREQUEST'].fields_by_name['path']._loaded_options = None
  _globals['_LISTDIRECTORYREQUEST'].fields_by_name['path']._serialized_options = b'\350\3071\000'
  _globals['_CREATEDIRECTORYREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_CREATEDIRECTORYREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_CREATEDIRECTORYREQUEST'].fields_by_name['compute_instance_id']._loaded_options = None
  _globals['_CREATEDIRECTORYREQUEST'].fields_by_name['compute_instance_id']._serialized_options = b'\350\3071\001'
  _globals['_CREATEDIRECTORYREQUEST'].fields_by_name['path']._loaded_options = None
  _globals['_CREATEDIRECTORYREQUEST'].fields_by_name['path']._serialized_options = b'\350\3071\001'
  _globals['_LISTRESOURCEOPERATIONSREQUEST'].fields_by_name['compute_instance_id']._loaded_options = None
  _globals['_LISTRESOURCEOPERATIONSREQUEST'].fields_by_name['compute_instance_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTRESOURCEOPERATIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTRESOURCEOPERATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTRESOURCEOPERATIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTRESOURCEOPERATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_RESOURCESERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_RESOURCESERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002\026\022\024/backup/v1/resources'
  _globals['_RESOURCESERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_RESOURCESERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002,\022*/backup/v1/resources/{compute_instance_id}'
  _globals['_RESOURCESERVICE'].methods_by_name['Delete']._loaded_options = None
  _globals['_RESOURCESERVICE'].methods_by_name['Delete']._serialized_options = b'\262\322*/\n\026DeleteResourceMetadata\022\025google.protobuf.Empty\202\323\344\223\002,**/backup/v1/resources/{compute_instance_id}'
  _globals['_RESOURCESERVICE'].methods_by_name['ListTasks']._loaded_options = None
  _globals['_RESOURCESERVICE'].methods_by_name['ListTasks']._serialized_options = b'\202\323\344\223\0022\0220/backup/v1/resources/{compute_instance_id}/tasks'
  _globals['_RESOURCESERVICE'].methods_by_name['CreateDirectory']._loaded_options = None
  _globals['_RESOURCESERVICE'].methods_by_name['CreateDirectory']._serialized_options = b'\262\322*0\n\027CreateDirectoryMetadata\022\025google.protobuf.Empty'
  _globals['_LISTRESOURCESREQUEST']._serialized_start=247
  _globals['_LISTRESOURCESREQUEST']._serialized_end=364
  _globals['_LISTRESOURCESRESPONSE']._serialized_start=366
  _globals['_LISTRESOURCESRESPONSE']._serialized_end=467
  _globals['_GETRESOURCEREQUEST']._serialized_start=469
  _globals['_GETRESOURCEREQUEST']._serialized_end=532
  _globals['_GETRESOURCERESPONSE']._serialized_start=534
  _globals['_GETRESOURCERESPONSE']._serialized_end=607
  _globals['_DELETERESOURCEREQUEST']._serialized_start=609
  _globals['_DELETERESOURCEREQUEST']._serialized_end=702
  _globals['_DELETERESOURCEMETADATA']._serialized_start=704
  _globals['_DELETERESOURCEMETADATA']._serialized_end=757
  _globals['_LISTTASKSREQUEST']._serialized_start=759
  _globals['_LISTTASKSREQUEST']._serialized_end=882
  _globals['_LISTTASKSRESPONSE']._serialized_start=884
  _globals['_LISTTASKSRESPONSE']._serialized_end=973
  _globals['_LISTDIRECTORYREQUEST']._serialized_start=975
  _globals['_LISTDIRECTORYREQUEST']._serialized_end=1085
  _globals['_LISTDIRECTORYRESPONSE']._serialized_start=1088
  _globals['_LISTDIRECTORYRESPONSE']._serialized_end=1469
  _globals['_LISTDIRECTORYRESPONSE_FILESYSTEMITEM']._serialized_start=1191
  _globals['_LISTDIRECTORYRESPONSE_FILESYSTEMITEM']._serialized_end=1469
  _globals['_LISTDIRECTORYRESPONSE_FILESYSTEMITEM_TYPE']._serialized_start=1404
  _globals['_LISTDIRECTORYRESPONSE_FILESYSTEMITEM_TYPE']._serialized_end=1469
  _globals['_CREATEDIRECTORYREQUEST']._serialized_start=1471
  _globals['_CREATEDIRECTORYREQUEST']._serialized_end=1583
  _globals['_CREATEDIRECTORYMETADATA']._serialized_start=1585
  _globals['_CREATEDIRECTORYMETADATA']._serialized_end=1653
  _globals['_LISTRESOURCEOPERATIONSREQUEST']._serialized_start=1656
  _globals['_LISTRESOURCEOPERATIONSREQUEST']._serialized_end=1792
  _globals['_LISTRESOURCEOPERATIONSRESPONSE']._serialized_start=1794
  _globals['_LISTRESOURCEOPERATIONSRESPONSE']._serialized_end=1906
  _globals['_RESOURCESERVICE']._serialized_start=1909
  _globals['_RESOURCESERVICE']._serialized_end=2956
# @@protoc_insertion_point(module_scope)
