# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/mdb/sqlserver/v1/user.proto
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
    'yandex/cloud/mdb/sqlserver/v1/user.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(yandex/cloud/mdb/sqlserver/v1/user.proto\x12\x1dyandex.cloud.mdb.sqlserver.v1\x1a\x1dyandex/cloud/validation.proto\"\xa9\x01\n\x04User\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ncluster_id\x18\x02 \x01(\t\x12>\n\x0bpermissions\x18\x03 \x03(\x0b\x32).yandex.cloud.mdb.sqlserver.v1.Permission\x12?\n\x0cserver_roles\x18\x04 \x03(\x0e\x32).yandex.cloud.mdb.sqlserver.v1.ServerRole\"\xbe\x02\n\nPermission\x12\x15\n\rdatabase_name\x18\x01 \x01(\t\x12\x46\n\x05roles\x18\x02 \x03(\x0e\x32..yandex.cloud.mdb.sqlserver.v1.Permission.RoleB\x07\x82\xc8\x31\x03>=1\"\xd0\x01\n\x04Role\x12\x14\n\x10ROLE_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x44\x42_OWNER\x10\x01\x12\x14\n\x10\x44\x42_SECURITYADMIN\x10\x02\x12\x12\n\x0e\x44\x42_ACCESSADMIN\x10\x03\x12\x15\n\x11\x44\x42_BACKUPOPERATOR\x10\x04\x12\x0f\n\x0b\x44\x42_DDLADMIN\x10\x05\x12\x11\n\rDB_DATAWRITER\x10\x06\x12\x11\n\rDB_DATAREADER\x10\x07\x12\x15\n\x11\x44\x42_DENYDATAWRITER\x10\x08\x12\x15\n\x11\x44\x42_DENYDATAREADER\x10\t\"\xd9\x01\n\x08UserSpec\x12+\n\x04name\x18\x01 \x01(\tB\x1d\xe8\xc7\x31\x01\xf2\xc7\x31\r[a-zA-Z0-9_]*\x8a\xc8\x31\x04<=32\x12\x1f\n\x08password\x18\x02 \x01(\tB\r\xe8\xc7\x31\x01\x8a\xc8\x31\x05\x38-128\x12>\n\x0bpermissions\x18\x03 \x03(\x0b\x32).yandex.cloud.mdb.sqlserver.v1.Permission\x12?\n\x0cserver_roles\x18\x04 \x03(\x0e\x32).yandex.cloud.mdb.sqlserver.v1.ServerRole*:\n\nServerRole\x12\x1b\n\x17SERVER_ROLE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bMDB_MONITOR\x10\x01\x42u\n!yandex.cloud.api.mdb.sqlserver.v1B\x03PSUZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/sqlserver/v1;sqlserverb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.sqlserver.v1.user_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!yandex.cloud.api.mdb.sqlserver.v1B\003PSUZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/sqlserver/v1;sqlserver'
  _globals['_PERMISSION'].fields_by_name['roles']._loaded_options = None
  _globals['_PERMISSION'].fields_by_name['roles']._serialized_options = b'\202\3101\003>=1'
  _globals['_USERSPEC'].fields_by_name['name']._loaded_options = None
  _globals['_USERSPEC'].fields_by_name['name']._serialized_options = b'\350\3071\001\362\3071\r[a-zA-Z0-9_]*\212\3101\004<=32'
  _globals['_USERSPEC'].fields_by_name['password']._loaded_options = None
  _globals['_USERSPEC'].fields_by_name['password']._serialized_options = b'\350\3071\001\212\3101\0058-128'
  _globals['_SERVERROLE']._serialized_start=819
  _globals['_SERVERROLE']._serialized_end=877
  _globals['_USER']._serialized_start=107
  _globals['_USER']._serialized_end=276
  _globals['_PERMISSION']._serialized_start=279
  _globals['_PERMISSION']._serialized_end=597
  _globals['_PERMISSION_ROLE']._serialized_start=389
  _globals['_PERMISSION_ROLE']._serialized_end=597
  _globals['_USERSPEC']._serialized_start=600
  _globals['_USERSPEC']._serialized_end=817
# @@protoc_insertion_point(module_scope)
