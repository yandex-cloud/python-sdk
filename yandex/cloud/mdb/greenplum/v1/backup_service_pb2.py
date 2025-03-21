# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/mdb/greenplum/v1/backup_service.proto
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
    'yandex/cloud/mdb/greenplum/v1/backup_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.mdb.greenplum.v1 import backup_pb2 as yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_backup__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2yandex/cloud/mdb/greenplum/v1/backup_service.proto\x12\x1dyandex.cloud.mdb.greenplum.v1\x1a\x1cgoogle/api/annotations.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\x1a*yandex/cloud/mdb/greenplum/v1/backup.proto\"+\n\x10GetBackupRequest\x12\x17\n\tbackup_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"s\n\x12ListBackupsRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"f\n\x13ListBackupsResponse\x12\x36\n\x07\x62\x61\x63kups\x18\x01 \x03(\x0b\x32%.yandex.cloud.mdb.greenplum.v1.Backup\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\".\n\x13\x44\x65leteBackupRequest\x12\x17\n\tbackup_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"G\n\x14\x44\x65leteBackupMetadata\x12\x11\n\tbackup_id\x18\x01 \x01(\t\x12\x1c\n\ncluster_id\x18\x02 \x01(\tB\x08\x8a\xc8\x31\x04<=502\xff\x03\n\rBackupService\x12\x90\x01\n\x03Get\x12/.yandex.cloud.mdb.greenplum.v1.GetBackupRequest\x1a%.yandex.cloud.mdb.greenplum.v1.Backup\"1\x82\xd3\xe4\x93\x02+\x12)/managed-greenplum/v1/backups/{backup_id}\x12\x94\x01\n\x04List\x12\x31.yandex.cloud.mdb.greenplum.v1.ListBackupsRequest\x1a\x32.yandex.cloud.mdb.greenplum.v1.ListBackupsResponse\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/managed-greenplum/v1/backups\x12\xc3\x01\n\x06\x44\x65lete\x12\x32.yandex.cloud.mdb.greenplum.v1.DeleteBackupRequest\x1a!.yandex.cloud.operation.Operation\"b\xb2\xd2*-\n\x14\x44\x65leteBackupMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02+*)/managed-greenplum/v1/backups/{backup_id}Bp\n!yandex.cloud.api.mdb.greenplum.v1ZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/greenplum/v1;greenplumb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.greenplum.v1.backup_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!yandex.cloud.api.mdb.greenplum.v1ZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/greenplum/v1;greenplum'
  _globals['_GETBACKUPREQUEST'].fields_by_name['backup_id']._loaded_options = None
  _globals['_GETBACKUPREQUEST'].fields_by_name['backup_id']._serialized_options = b'\350\3071\001'
  _globals['_LISTBACKUPSREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_LISTBACKUPSREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTBACKUPSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTBACKUPSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _globals['_LISTBACKUPSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTBACKUPSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_DELETEBACKUPREQUEST'].fields_by_name['backup_id']._loaded_options = None
  _globals['_DELETEBACKUPREQUEST'].fields_by_name['backup_id']._serialized_options = b'\350\3071\001'
  _globals['_DELETEBACKUPMETADATA'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_DELETEBACKUPMETADATA'].fields_by_name['cluster_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_BACKUPSERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_BACKUPSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002+\022)/managed-greenplum/v1/backups/{backup_id}'
  _globals['_BACKUPSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_BACKUPSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002\037\022\035/managed-greenplum/v1/backups'
  _globals['_BACKUPSERVICE'].methods_by_name['Delete']._loaded_options = None
  _globals['_BACKUPSERVICE'].methods_by_name['Delete']._serialized_options = b'\262\322*-\n\024DeleteBackupMetadata\022\025google.protobuf.Empty\202\323\344\223\002+*)/managed-greenplum/v1/backups/{backup_id}'
  _globals['_GETBACKUPREQUEST']._serialized_start=264
  _globals['_GETBACKUPREQUEST']._serialized_end=307
  _globals['_LISTBACKUPSREQUEST']._serialized_start=309
  _globals['_LISTBACKUPSREQUEST']._serialized_end=424
  _globals['_LISTBACKUPSRESPONSE']._serialized_start=426
  _globals['_LISTBACKUPSRESPONSE']._serialized_end=528
  _globals['_DELETEBACKUPREQUEST']._serialized_start=530
  _globals['_DELETEBACKUPREQUEST']._serialized_end=576
  _globals['_DELETEBACKUPMETADATA']._serialized_start=578
  _globals['_DELETEBACKUPMETADATA']._serialized_end=649
  _globals['_BACKUPSERVICE']._serialized_start=652
  _globals['_BACKUPSERVICE']._serialized_end=1163
# @@protoc_insertion_point(module_scope)
