# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/mdb/postgresql/v1/user_service.proto
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
    'yandex/cloud/mdb/postgresql/v1/user_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.mdb.postgresql.v1 import user_pb2 as yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_user__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1yandex/cloud/mdb/postgresql/v1/user_service.proto\x12\x1eyandex.cloud.mdb.postgresql.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\x1a)yandex/cloud/mdb/postgresql/v1/user.proto\x1a yandex/cloud/api/operation.proto\"e\n\x0eGetUserRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x31\n\tuser_name\x18\x02 \x01(\tB\x1e\xe8\xc7\x31\x01\xf2\xc7\x31\x0e[a-zA-Z0-9_-]*\x8a\xc8\x31\x04<=63\"r\n\x10ListUsersRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"a\n\x11ListUsersResponse\x12\x33\n\x05users\x18\x01 \x03(\x0b\x32$.yandex.cloud.mdb.postgresql.v1.User\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"x\n\x11\x43reateUserRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x41\n\tuser_spec\x18\x02 \x01(\x0b\x32(.yandex.cloud.mdb.postgresql.v1.UserSpecB\x04\xe8\xc7\x31\x01\";\n\x12\x43reateUserMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t\"\xbe\x04\n\x11UpdateUserRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x31\n\tuser_name\x18\x02 \x01(\tB\x1e\xe8\xc7\x31\x01\xf2\xc7\x31\x0e[a-zA-Z0-9_-]*\x8a\xc8\x31\x04<=63\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1b\n\x08password\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05\x38-128\x12?\n\x0bpermissions\x18\x05 \x03(\x0b\x32*.yandex.cloud.mdb.postgresql.v1.Permission\x12\x1c\n\nconn_limit\x18\x06 \x01(\x03\x42\x08\xfa\xc7\x31\x04>=10\x12>\n\x08settings\x18\x07 \x01(\x0b\x32,.yandex.cloud.mdb.postgresql.v1.UserSettings\x12)\n\x05login\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12)\n\x06grants\x18\t \x03(\tB\x19\xf2\xc7\x31\r[a-zA-Z0-9_]*\x8a\xc8\x31\x04<=63\x12\x37\n\x13\x64\x65letion_protection\x18\n \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12X\n\x18user_password_encryption\x18\x0b \x01(\x0e\x32\x36.yandex.cloud.mdb.postgresql.v1.UserPasswordEncryption\";\n\x12UpdateUserMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t\"h\n\x11\x44\x65leteUserRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x31\n\tuser_name\x18\x02 \x01(\tB\x1e\xe8\xc7\x31\x01\xf2\xc7\x31\x0e[a-zA-Z0-9_-]*\x8a\xc8\x31\x04<=63\";\n\x12\x44\x65leteUserMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t\"\xb7\x01\n\x1aGrantUserPermissionRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x31\n\tuser_name\x18\x02 \x01(\tB\x1e\xe8\xc7\x31\x01\xf2\xc7\x31\x0e[a-zA-Z0-9_-]*\x8a\xc8\x31\x04<=63\x12\x44\n\npermission\x18\x03 \x01(\x0b\x32*.yandex.cloud.mdb.postgresql.v1.PermissionB\x04\xe8\xc7\x31\x01\"D\n\x1bGrantUserPermissionMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t\"\xa9\x01\n\x1bRevokeUserPermissionRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x31\n\tuser_name\x18\x02 \x01(\tB\x1e\xe8\xc7\x31\x01\xf2\xc7\x31\x0e[a-zA-Z0-9_-]*\x8a\xc8\x31\x04<=63\x12\x35\n\rdatabase_name\x18\x03 \x01(\tB\x1e\xe8\xc7\x31\x01\xf2\xc7\x31\x0e[a-zA-Z0-9_-]*\x8a\xc8\x31\x04<=63\"E\n\x1cRevokeUserPermissionMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t2\xad\x0b\n\x0bUserService\x12\xa3\x01\n\x03Get\x12..yandex.cloud.mdb.postgresql.v1.GetUserRequest\x1a$.yandex.cloud.mdb.postgresql.v1.User\"F\x82\xd3\xe4\x93\x02@\x12>/managed-postgresql/v1/clusters/{cluster_id}/users/{user_name}\x12\xa7\x01\n\x04List\x12\x30.yandex.cloud.mdb.postgresql.v1.ListUsersRequest\x1a\x31.yandex.cloud.mdb.postgresql.v1.ListUsersResponse\":\x82\xd3\xe4\x93\x02\x34\x12\x32/managed-postgresql/v1/clusters/{cluster_id}/users\x12\xbb\x01\n\x06\x43reate\x12\x31.yandex.cloud.mdb.postgresql.v1.CreateUserRequest\x1a!.yandex.cloud.operation.Operation\"[\xb2\xd2*\x1a\n\x12\x43reateUserMetadata\x12\x04User\x82\xd3\xe4\x93\x02\x37\"2/managed-postgresql/v1/clusters/{cluster_id}/users:\x01*\x12\xc7\x01\n\x06Update\x12\x31.yandex.cloud.mdb.postgresql.v1.UpdateUserRequest\x1a!.yandex.cloud.operation.Operation\"g\xb2\xd2*\x1a\n\x12UpdateUserMetadata\x12\x04User\x82\xd3\xe4\x93\x02\x43\x32>/managed-postgresql/v1/clusters/{cluster_id}/users/{user_name}:\x01*\x12\xd5\x01\n\x06\x44\x65lete\x12\x31.yandex.cloud.mdb.postgresql.v1.DeleteUserRequest\x1a!.yandex.cloud.operation.Operation\"u\xb2\xd2*+\n\x12\x44\x65leteUserMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02@*>/managed-postgresql/v1/clusters/{cluster_id}/users/{user_name}\x12\xf3\x01\n\x0fGrantPermission\x12:.yandex.cloud.mdb.postgresql.v1.GrantUserPermissionRequest\x1a!.yandex.cloud.operation.Operation\"\x80\x01\xb2\xd2*#\n\x1bGrantUserPermissionMetadata\x12\x04User\x82\xd3\xe4\x93\x02S\"N/managed-postgresql/v1/clusters/{cluster_id}/users/{user_name}:grantPermission:\x01*\x12\xf7\x01\n\x10RevokePermission\x12;.yandex.cloud.mdb.postgresql.v1.RevokeUserPermissionRequest\x1a!.yandex.cloud.operation.Operation\"\x82\x01\xb2\xd2*$\n\x1cRevokeUserPermissionMetadata\x12\x04User\x82\xd3\xe4\x93\x02T\"O/managed-postgresql/v1/clusters/{cluster_id}/users/{user_name}:revokePermission:\x01*Bs\n\"yandex.cloud.api.mdb.postgresql.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/postgresql/v1;postgresqlb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.postgresql.v1.user_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"yandex.cloud.api.mdb.postgresql.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/postgresql/v1;postgresql'
  _globals['_GETUSERREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_GETUSERREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_GETUSERREQUEST'].fields_by_name['user_name']._loaded_options = None
  _globals['_GETUSERREQUEST'].fields_by_name['user_name']._serialized_options = b'\350\3071\001\362\3071\016[a-zA-Z0-9_-]*\212\3101\004<=63'
  _globals['_LISTUSERSREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_LISTUSERSREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTUSERSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTUSERSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTUSERSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTUSERSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_CREATEUSERREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_CREATEUSERREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_CREATEUSERREQUEST'].fields_by_name['user_spec']._loaded_options = None
  _globals['_CREATEUSERREQUEST'].fields_by_name['user_spec']._serialized_options = b'\350\3071\001'
  _globals['_UPDATEUSERREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_UPDATEUSERREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_UPDATEUSERREQUEST'].fields_by_name['user_name']._loaded_options = None
  _globals['_UPDATEUSERREQUEST'].fields_by_name['user_name']._serialized_options = b'\350\3071\001\362\3071\016[a-zA-Z0-9_-]*\212\3101\004<=63'
  _globals['_UPDATEUSERREQUEST'].fields_by_name['password']._loaded_options = None
  _globals['_UPDATEUSERREQUEST'].fields_by_name['password']._serialized_options = b'\212\3101\0058-128'
  _globals['_UPDATEUSERREQUEST'].fields_by_name['conn_limit']._loaded_options = None
  _globals['_UPDATEUSERREQUEST'].fields_by_name['conn_limit']._serialized_options = b'\372\3071\004>=10'
  _globals['_UPDATEUSERREQUEST'].fields_by_name['grants']._loaded_options = None
  _globals['_UPDATEUSERREQUEST'].fields_by_name['grants']._serialized_options = b'\362\3071\r[a-zA-Z0-9_]*\212\3101\004<=63'
  _globals['_DELETEUSERREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_DELETEUSERREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_DELETEUSERREQUEST'].fields_by_name['user_name']._loaded_options = None
  _globals['_DELETEUSERREQUEST'].fields_by_name['user_name']._serialized_options = b'\350\3071\001\362\3071\016[a-zA-Z0-9_-]*\212\3101\004<=63'
  _globals['_GRANTUSERPERMISSIONREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_GRANTUSERPERMISSIONREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_GRANTUSERPERMISSIONREQUEST'].fields_by_name['user_name']._loaded_options = None
  _globals['_GRANTUSERPERMISSIONREQUEST'].fields_by_name['user_name']._serialized_options = b'\350\3071\001\362\3071\016[a-zA-Z0-9_-]*\212\3101\004<=63'
  _globals['_GRANTUSERPERMISSIONREQUEST'].fields_by_name['permission']._loaded_options = None
  _globals['_GRANTUSERPERMISSIONREQUEST'].fields_by_name['permission']._serialized_options = b'\350\3071\001'
  _globals['_REVOKEUSERPERMISSIONREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_REVOKEUSERPERMISSIONREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_REVOKEUSERPERMISSIONREQUEST'].fields_by_name['user_name']._loaded_options = None
  _globals['_REVOKEUSERPERMISSIONREQUEST'].fields_by_name['user_name']._serialized_options = b'\350\3071\001\362\3071\016[a-zA-Z0-9_-]*\212\3101\004<=63'
  _globals['_REVOKEUSERPERMISSIONREQUEST'].fields_by_name['database_name']._loaded_options = None
  _globals['_REVOKEUSERPERMISSIONREQUEST'].fields_by_name['database_name']._serialized_options = b'\350\3071\001\362\3071\016[a-zA-Z0-9_-]*\212\3101\004<=63'
  _globals['_USERSERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_USERSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002@\022>/managed-postgresql/v1/clusters/{cluster_id}/users/{user_name}'
  _globals['_USERSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_USERSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\0024\0222/managed-postgresql/v1/clusters/{cluster_id}/users'
  _globals['_USERSERVICE'].methods_by_name['Create']._loaded_options = None
  _globals['_USERSERVICE'].methods_by_name['Create']._serialized_options = b'\262\322*\032\n\022CreateUserMetadata\022\004User\202\323\344\223\0027\"2/managed-postgresql/v1/clusters/{cluster_id}/users:\001*'
  _globals['_USERSERVICE'].methods_by_name['Update']._loaded_options = None
  _globals['_USERSERVICE'].methods_by_name['Update']._serialized_options = b'\262\322*\032\n\022UpdateUserMetadata\022\004User\202\323\344\223\002C2>/managed-postgresql/v1/clusters/{cluster_id}/users/{user_name}:\001*'
  _globals['_USERSERVICE'].methods_by_name['Delete']._loaded_options = None
  _globals['_USERSERVICE'].methods_by_name['Delete']._serialized_options = b'\262\322*+\n\022DeleteUserMetadata\022\025google.protobuf.Empty\202\323\344\223\002@*>/managed-postgresql/v1/clusters/{cluster_id}/users/{user_name}'
  _globals['_USERSERVICE'].methods_by_name['GrantPermission']._loaded_options = None
  _globals['_USERSERVICE'].methods_by_name['GrantPermission']._serialized_options = b'\262\322*#\n\033GrantUserPermissionMetadata\022\004User\202\323\344\223\002S\"N/managed-postgresql/v1/clusters/{cluster_id}/users/{user_name}:grantPermission:\001*'
  _globals['_USERSERVICE'].methods_by_name['RevokePermission']._loaded_options = None
  _globals['_USERSERVICE'].methods_by_name['RevokePermission']._serialized_options = b'\262\322*$\n\034RevokeUserPermissionMetadata\022\004User\202\323\344\223\002T\"O/managed-postgresql/v1/clusters/{cluster_id}/users/{user_name}:revokePermission:\001*'
  _globals['_GETUSERREQUEST']._serialized_start=329
  _globals['_GETUSERREQUEST']._serialized_end=430
  _globals['_LISTUSERSREQUEST']._serialized_start=432
  _globals['_LISTUSERSREQUEST']._serialized_end=546
  _globals['_LISTUSERSRESPONSE']._serialized_start=548
  _globals['_LISTUSERSRESPONSE']._serialized_end=645
  _globals['_CREATEUSERREQUEST']._serialized_start=647
  _globals['_CREATEUSERREQUEST']._serialized_end=767
  _globals['_CREATEUSERMETADATA']._serialized_start=769
  _globals['_CREATEUSERMETADATA']._serialized_end=828
  _globals['_UPDATEUSERREQUEST']._serialized_start=831
  _globals['_UPDATEUSERREQUEST']._serialized_end=1405
  _globals['_UPDATEUSERMETADATA']._serialized_start=1407
  _globals['_UPDATEUSERMETADATA']._serialized_end=1466
  _globals['_DELETEUSERREQUEST']._serialized_start=1468
  _globals['_DELETEUSERREQUEST']._serialized_end=1572
  _globals['_DELETEUSERMETADATA']._serialized_start=1574
  _globals['_DELETEUSERMETADATA']._serialized_end=1633
  _globals['_GRANTUSERPERMISSIONREQUEST']._serialized_start=1636
  _globals['_GRANTUSERPERMISSIONREQUEST']._serialized_end=1819
  _globals['_GRANTUSERPERMISSIONMETADATA']._serialized_start=1821
  _globals['_GRANTUSERPERMISSIONMETADATA']._serialized_end=1889
  _globals['_REVOKEUSERPERMISSIONREQUEST']._serialized_start=1892
  _globals['_REVOKEUSERPERMISSIONREQUEST']._serialized_end=2061
  _globals['_REVOKEUSERPERMISSIONMETADATA']._serialized_start=2063
  _globals['_REVOKEUSERPERMISSIONMETADATA']._serialized_end=2132
  _globals['_USERSERVICE']._serialized_start=2135
  _globals['_USERSERVICE']._serialized_end=3588
# @@protoc_insertion_point(module_scope)
