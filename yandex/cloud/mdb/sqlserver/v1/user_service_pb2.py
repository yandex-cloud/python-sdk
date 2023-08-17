# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/sqlserver/v1/user_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.mdb.sqlserver.v1 import user_pb2 as yandex_dot_cloud_dot_mdb_dot_sqlserver_dot_v1_dot_user__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0yandex/cloud/mdb/sqlserver/v1/user_service.proto\x12\x1dyandex.cloud.mdb.sqlserver.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\x1a(yandex/cloud/mdb/sqlserver/v1/user.proto\"d\n\x0eGetUserRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x30\n\tuser_name\x18\x02 \x01(\tB\x1d\xe8\xc7\x31\x01\xf2\xc7\x31\r[a-zA-Z0-9_]*\x8a\xc8\x31\x04<=63\"r\n\x10ListUsersRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"`\n\x11ListUsersResponse\x12\x32\n\x05users\x18\x01 \x03(\x0b\x32#.yandex.cloud.mdb.sqlserver.v1.User\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"w\n\x11\x43reateUserRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12@\n\tuser_spec\x18\x02 \x01(\x0b\x32\'.yandex.cloud.mdb.sqlserver.v1.UserSpecB\x04\xe8\xc7\x31\x01\";\n\x12\x43reateUserMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t\"\xb6\x02\n\x11UpdateUserRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x30\n\tuser_name\x18\x02 \x01(\tB\x1d\xe8\xc7\x31\x01\xf2\xc7\x31\r[a-zA-Z0-9_]*\x8a\xc8\x31\x04<=63\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1b\n\x08password\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05\x38-128\x12>\n\x0bpermissions\x18\x05 \x03(\x0b\x32).yandex.cloud.mdb.sqlserver.v1.Permission\x12?\n\x0cserver_roles\x18\x06 \x03(\x0e\x32).yandex.cloud.mdb.sqlserver.v1.ServerRole\";\n\x12UpdateUserMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t\"g\n\x11\x44\x65leteUserRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x30\n\tuser_name\x18\x02 \x01(\tB\x1d\xe8\xc7\x31\x01\xf2\xc7\x31\r[a-zA-Z0-9_]*\x8a\xc8\x31\x04<=63\";\n\x12\x44\x65leteUserMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t\"\xb5\x01\n\x1aGrantUserPermissionRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x30\n\tuser_name\x18\x02 \x01(\tB\x1d\xe8\xc7\x31\x01\xf2\xc7\x31\r[a-zA-Z0-9_]*\x8a\xc8\x31\x04<=63\x12\x43\n\npermission\x18\x03 \x01(\x0b\x32).yandex.cloud.mdb.sqlserver.v1.PermissionB\x04\xe8\xc7\x31\x01\"D\n\x1bGrantUserPermissionMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t\"\xb6\x01\n\x1bRevokeUserPermissionRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x30\n\tuser_name\x18\x02 \x01(\tB\x1d\xe8\xc7\x31\x01\xf2\xc7\x31\r[a-zA-Z0-9_]*\x8a\xc8\x31\x04<=63\x12\x43\n\npermission\x18\x03 \x01(\x0b\x32).yandex.cloud.mdb.sqlserver.v1.PermissionB\x04\xe8\xc7\x31\x01\"E\n\x1cRevokeUserPermissionMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t2\xff\n\n\x0bUserService\x12\x9c\x01\n\x03Get\x12-.yandex.cloud.mdb.sqlserver.v1.GetUserRequest\x1a#.yandex.cloud.mdb.sqlserver.v1.User\"A\x82\xd3\xe4\x93\x02;\x12\x39/mdb/sqlserver/v1/clusters/{cluster_id}/users/{user_name}\x12\xa0\x01\n\x04List\x12/.yandex.cloud.mdb.sqlserver.v1.ListUsersRequest\x1a\x30.yandex.cloud.mdb.sqlserver.v1.ListUsersResponse\"5\x82\xd3\xe4\x93\x02/\x12-/mdb/sqlserver/v1/clusters/{cluster_id}/users\x12\xb5\x01\n\x06\x43reate\x12\x30.yandex.cloud.mdb.sqlserver.v1.CreateUserRequest\x1a!.yandex.cloud.operation.Operation\"V\xb2\xd2*\x1a\n\x12\x43reateUserMetadata\x12\x04User\x82\xd3\xe4\x93\x02\x32\"-/mdb/sqlserver/v1/clusters/{cluster_id}/users:\x01*\x12\xc1\x01\n\x06Update\x12\x30.yandex.cloud.mdb.sqlserver.v1.UpdateUserRequest\x1a!.yandex.cloud.operation.Operation\"b\xb2\xd2*\x1a\n\x12UpdateUserMetadata\x12\x04User\x82\xd3\xe4\x93\x02>29/mdb/sqlserver/v1/clusters/{cluster_id}/users/{user_name}:\x01*\x12\xcf\x01\n\x06\x44\x65lete\x12\x30.yandex.cloud.mdb.sqlserver.v1.DeleteUserRequest\x1a!.yandex.cloud.operation.Operation\"p\xb2\xd2*+\n\x12\x44\x65leteUserMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02;*9/mdb/sqlserver/v1/clusters/{cluster_id}/users/{user_name}\x12\xec\x01\n\x0fGrantPermission\x12\x39.yandex.cloud.mdb.sqlserver.v1.GrantUserPermissionRequest\x1a!.yandex.cloud.operation.Operation\"{\xb2\xd2*#\n\x1bGrantUserPermissionMetadata\x12\x04User\x82\xd3\xe4\x93\x02N\"I/mdb/sqlserver/v1/clusters/{cluster_id}/users/{user_name}:grantPermission:\x01*\x12\xf0\x01\n\x10RevokePermission\x12:.yandex.cloud.mdb.sqlserver.v1.RevokeUserPermissionRequest\x1a!.yandex.cloud.operation.Operation\"}\xb2\xd2*$\n\x1cRevokeUserPermissionMetadata\x12\x04User\x82\xd3\xe4\x93\x02O\"J/mdb/sqlserver/v1/clusters/{cluster_id}/users/{user_name}:revokePermission:\x01*Bv\n!yandex.cloud.api.mdb.sqlserver.v1B\x04PSUSZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/sqlserver/v1;sqlserverb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.sqlserver.v1.user_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!yandex.cloud.api.mdb.sqlserver.v1B\004PSUSZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/sqlserver/v1;sqlserver'
  _GETUSERREQUEST.fields_by_name['cluster_id']._options = None
  _GETUSERREQUEST.fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _GETUSERREQUEST.fields_by_name['user_name']._options = None
  _GETUSERREQUEST.fields_by_name['user_name']._serialized_options = b'\350\3071\001\362\3071\r[a-zA-Z0-9_]*\212\3101\004<=63'
  _LISTUSERSREQUEST.fields_by_name['cluster_id']._options = None
  _LISTUSERSREQUEST.fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTUSERSREQUEST.fields_by_name['page_size']._options = None
  _LISTUSERSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _LISTUSERSREQUEST.fields_by_name['page_token']._options = None
  _LISTUSERSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _CREATEUSERREQUEST.fields_by_name['cluster_id']._options = None
  _CREATEUSERREQUEST.fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _CREATEUSERREQUEST.fields_by_name['user_spec']._options = None
  _CREATEUSERREQUEST.fields_by_name['user_spec']._serialized_options = b'\350\3071\001'
  _UPDATEUSERREQUEST.fields_by_name['cluster_id']._options = None
  _UPDATEUSERREQUEST.fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _UPDATEUSERREQUEST.fields_by_name['user_name']._options = None
  _UPDATEUSERREQUEST.fields_by_name['user_name']._serialized_options = b'\350\3071\001\362\3071\r[a-zA-Z0-9_]*\212\3101\004<=63'
  _UPDATEUSERREQUEST.fields_by_name['password']._options = None
  _UPDATEUSERREQUEST.fields_by_name['password']._serialized_options = b'\212\3101\0058-128'
  _DELETEUSERREQUEST.fields_by_name['cluster_id']._options = None
  _DELETEUSERREQUEST.fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _DELETEUSERREQUEST.fields_by_name['user_name']._options = None
  _DELETEUSERREQUEST.fields_by_name['user_name']._serialized_options = b'\350\3071\001\362\3071\r[a-zA-Z0-9_]*\212\3101\004<=63'
  _GRANTUSERPERMISSIONREQUEST.fields_by_name['cluster_id']._options = None
  _GRANTUSERPERMISSIONREQUEST.fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _GRANTUSERPERMISSIONREQUEST.fields_by_name['user_name']._options = None
  _GRANTUSERPERMISSIONREQUEST.fields_by_name['user_name']._serialized_options = b'\350\3071\001\362\3071\r[a-zA-Z0-9_]*\212\3101\004<=63'
  _GRANTUSERPERMISSIONREQUEST.fields_by_name['permission']._options = None
  _GRANTUSERPERMISSIONREQUEST.fields_by_name['permission']._serialized_options = b'\350\3071\001'
  _REVOKEUSERPERMISSIONREQUEST.fields_by_name['cluster_id']._options = None
  _REVOKEUSERPERMISSIONREQUEST.fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _REVOKEUSERPERMISSIONREQUEST.fields_by_name['user_name']._options = None
  _REVOKEUSERPERMISSIONREQUEST.fields_by_name['user_name']._serialized_options = b'\350\3071\001\362\3071\r[a-zA-Z0-9_]*\212\3101\004<=63'
  _REVOKEUSERPERMISSIONREQUEST.fields_by_name['permission']._options = None
  _REVOKEUSERPERMISSIONREQUEST.fields_by_name['permission']._serialized_options = b'\350\3071\001'
  _USERSERVICE.methods_by_name['Get']._options = None
  _USERSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002;\0229/mdb/sqlserver/v1/clusters/{cluster_id}/users/{user_name}'
  _USERSERVICE.methods_by_name['List']._options = None
  _USERSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002/\022-/mdb/sqlserver/v1/clusters/{cluster_id}/users'
  _USERSERVICE.methods_by_name['Create']._options = None
  _USERSERVICE.methods_by_name['Create']._serialized_options = b'\262\322*\032\n\022CreateUserMetadata\022\004User\202\323\344\223\0022\"-/mdb/sqlserver/v1/clusters/{cluster_id}/users:\001*'
  _USERSERVICE.methods_by_name['Update']._options = None
  _USERSERVICE.methods_by_name['Update']._serialized_options = b'\262\322*\032\n\022UpdateUserMetadata\022\004User\202\323\344\223\002>29/mdb/sqlserver/v1/clusters/{cluster_id}/users/{user_name}:\001*'
  _USERSERVICE.methods_by_name['Delete']._options = None
  _USERSERVICE.methods_by_name['Delete']._serialized_options = b'\262\322*+\n\022DeleteUserMetadata\022\025google.protobuf.Empty\202\323\344\223\002;*9/mdb/sqlserver/v1/clusters/{cluster_id}/users/{user_name}'
  _USERSERVICE.methods_by_name['GrantPermission']._options = None
  _USERSERVICE.methods_by_name['GrantPermission']._serialized_options = b'\262\322*#\n\033GrantUserPermissionMetadata\022\004User\202\323\344\223\002N\"I/mdb/sqlserver/v1/clusters/{cluster_id}/users/{user_name}:grantPermission:\001*'
  _USERSERVICE.methods_by_name['RevokePermission']._options = None
  _USERSERVICE.methods_by_name['RevokePermission']._serialized_options = b'\262\322*$\n\034RevokeUserPermissionMetadata\022\004User\202\323\344\223\002O\"J/mdb/sqlserver/v1/clusters/{cluster_id}/users/{user_name}:revokePermission:\001*'
  _globals['_GETUSERREQUEST']._serialized_start=294
  _globals['_GETUSERREQUEST']._serialized_end=394
  _globals['_LISTUSERSREQUEST']._serialized_start=396
  _globals['_LISTUSERSREQUEST']._serialized_end=510
  _globals['_LISTUSERSRESPONSE']._serialized_start=512
  _globals['_LISTUSERSRESPONSE']._serialized_end=608
  _globals['_CREATEUSERREQUEST']._serialized_start=610
  _globals['_CREATEUSERREQUEST']._serialized_end=729
  _globals['_CREATEUSERMETADATA']._serialized_start=731
  _globals['_CREATEUSERMETADATA']._serialized_end=790
  _globals['_UPDATEUSERREQUEST']._serialized_start=793
  _globals['_UPDATEUSERREQUEST']._serialized_end=1103
  _globals['_UPDATEUSERMETADATA']._serialized_start=1105
  _globals['_UPDATEUSERMETADATA']._serialized_end=1164
  _globals['_DELETEUSERREQUEST']._serialized_start=1166
  _globals['_DELETEUSERREQUEST']._serialized_end=1269
  _globals['_DELETEUSERMETADATA']._serialized_start=1271
  _globals['_DELETEUSERMETADATA']._serialized_end=1330
  _globals['_GRANTUSERPERMISSIONREQUEST']._serialized_start=1333
  _globals['_GRANTUSERPERMISSIONREQUEST']._serialized_end=1514
  _globals['_GRANTUSERPERMISSIONMETADATA']._serialized_start=1516
  _globals['_GRANTUSERPERMISSIONMETADATA']._serialized_end=1584
  _globals['_REVOKEUSERPERMISSIONREQUEST']._serialized_start=1587
  _globals['_REVOKEUSERPERMISSIONREQUEST']._serialized_end=1769
  _globals['_REVOKEUSERPERMISSIONMETADATA']._serialized_start=1771
  _globals['_REVOKEUSERPERMISSIONMETADATA']._serialized_end=1840
  _globals['_USERSERVICE']._serialized_start=1843
  _globals['_USERSERVICE']._serialized_end=3250
# @@protoc_insertion_point(module_scope)
