# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/mdb/opensearch/v1/backup_service.proto
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
    'yandex/cloud/mdb/opensearch/v1/backup_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.mdb.opensearch.v1 import backup_pb2 as yandex_dot_cloud_dot_mdb_dot_opensearch_dot_v1_dot_backup__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3yandex/cloud/mdb/opensearch/v1/backup_service.proto\x12\x1eyandex.cloud.mdb.opensearch.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1dyandex/cloud/validation.proto\x1a+yandex/cloud/mdb/opensearch/v1/backup.proto\"+\n\x10GetBackupRequest\x12\x17\n\tbackup_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"s\n\x12ListBackupsRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"g\n\x13ListBackupsResponse\x12\x37\n\x07\x62\x61\x63kups\x18\x01 \x03(\x0b\x32&.yandex.cloud.mdb.opensearch.v1.Backup\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xbf\x02\n\rBackupService\x12\x93\x01\n\x03Get\x12\x30.yandex.cloud.mdb.opensearch.v1.GetBackupRequest\x1a&.yandex.cloud.mdb.opensearch.v1.Backup\"2\x82\xd3\xe4\x93\x02,\x12*/managed-opensearch/v1/backups/{backup_id}\x12\x97\x01\n\x04List\x12\x32.yandex.cloud.mdb.opensearch.v1.ListBackupsRequest\x1a\x33.yandex.cloud.mdb.opensearch.v1.ListBackupsResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/managed-opensearch/v1/backupsBs\n\"yandex.cloud.api.mdb.opensearch.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/opensearch/v1;opensearchb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.opensearch.v1.backup_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"yandex.cloud.api.mdb.opensearch.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/opensearch/v1;opensearch'
  _globals['_GETBACKUPREQUEST'].fields_by_name['backup_id']._loaded_options = None
  _globals['_GETBACKUPREQUEST'].fields_by_name['backup_id']._serialized_options = b'\350\3071\001'
  _globals['_LISTBACKUPSREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_LISTBACKUPSREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTBACKUPSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTBACKUPSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _globals['_LISTBACKUPSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTBACKUPSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_BACKUPSERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_BACKUPSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002,\022*/managed-opensearch/v1/backups/{backup_id}'
  _globals['_BACKUPSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_BACKUPSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002 \022\036/managed-opensearch/v1/backups'
  _globals['_GETBACKUPREQUEST']._serialized_start=193
  _globals['_GETBACKUPREQUEST']._serialized_end=236
  _globals['_LISTBACKUPSREQUEST']._serialized_start=238
  _globals['_LISTBACKUPSREQUEST']._serialized_end=353
  _globals['_LISTBACKUPSRESPONSE']._serialized_start=355
  _globals['_LISTBACKUPSRESPONSE']._serialized_end=458
  _globals['_BACKUPSERVICE']._serialized_start=461
  _globals['_BACKUPSERVICE']._serialized_end=780
# @@protoc_insertion_point(module_scope)
