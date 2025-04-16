# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/mdb/greenplum/v1/user_service.proto
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
    'yandex/cloud/mdb/greenplum/v1/user_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.mdb.greenplum.v1 import user_pb2 as yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_user__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0yandex/cloud/mdb/greenplum/v1/user_service.proto\x12\x1dyandex.cloud.mdb.greenplum.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/api/operation.proto\x1a\x1dyandex/cloud/validation.proto\x1a&yandex/cloud/operation/operation.proto\x1a(yandex/cloud/mdb/greenplum/v1/user.proto\"x\n\x12\x43reateUserMetadata\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12@\n\tuser_name\x18\x02 \x01(\tB-\xe8\xc7\x31\x01\xf2\xc7\x31\x1d^[a-zA-Z_][a-zA-Z0-9_]{0,62}$\x8a\xc8\x31\x04\x31-63\"x\n\x12UpdateUserMetadata\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12@\n\tuser_name\x18\x02 \x01(\tB-\xe8\xc7\x31\x01\xf2\xc7\x31\x1d^[a-zA-Z_][a-zA-Z0-9_]{0,62}$\x8a\xc8\x31\x04\x31-63\"x\n\x12\x44\x65leteUserMetadata\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12@\n\tuser_name\x18\x02 \x01(\tB-\xe8\xc7\x31\x01\xf2\xc7\x31\x1d^[a-zA-Z_][a-zA-Z0-9_]{0,62}$\x8a\xc8\x31\x04\x31-63\"4\n\x10ListUsersRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"G\n\x11ListUsersResponse\x12\x32\n\x05users\x18\x01 \x03(\x0b\x32#.yandex.cloud.mdb.greenplum.v1.User\"\x98\x01\n\x18GetUserAtRevisionRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x18\n\x08revision\x18\x02 \x01(\x03\x42\x06\xfa\xc7\x31\x02>0\x12@\n\tuser_name\x18\x03 \x01(\tB-\xe8\xc7\x31\x01\xf2\xc7\x31\x1d^[a-zA-Z_][a-zA-Z0-9_]{0,62}$\x8a\xc8\x31\x04\x31-63\"n\n\x11\x43reateUserRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x37\n\x04user\x18\x02 \x01(\x0b\x32#.yandex.cloud.mdb.greenplum.v1.UserB\x04\xe8\xc7\x31\x01\"\x9f\x01\n\x11UpdateUserRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x37\n\x04user\x18\x03 \x01(\x0b\x32#.yandex.cloud.mdb.greenplum.v1.UserB\x04\xe8\xc7\x31\x01\"w\n\x11\x44\x65leteUserRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12@\n\tuser_name\x18\x02 \x01(\tB-\xe8\xc7\x31\x01\xf2\xc7\x31\x1d^[a-zA-Z_][a-zA-Z0-9_]{0,62}$\x8a\xc8\x31\x04\x31-632\x8e\x06\n\x0bUserService\x12\xa4\x01\n\x04List\x12/.yandex.cloud.mdb.greenplum.v1.ListUsersRequest\x1a\x30.yandex.cloud.mdb.greenplum.v1.ListUsersResponse\"9\x82\xd3\xe4\x93\x02\x33\x12\x31/managed-greenplum/v1/clusters/{cluster_id}/users\x12\xb9\x01\n\x06\x43reate\x12\x30.yandex.cloud.mdb.greenplum.v1.CreateUserRequest\x1a!.yandex.cloud.operation.Operation\"Z\xb2\xd2*\x1a\n\x12\x43reateUserMetadata\x12\x04User\x82\xd3\xe4\x93\x02\x36\"1/managed-greenplum/v1/clusters/{cluster_id}/users:\x01*\x12\xc5\x01\n\x06Update\x12\x30.yandex.cloud.mdb.greenplum.v1.UpdateUserRequest\x1a!.yandex.cloud.operation.Operation\"f\xb2\xd2*\x1a\n\x12UpdateUserMetadata\x12\x04User\x82\xd3\xe4\x93\x02\x42\x32=/managed-greenplum/v1/clusters/{cluster_id}/users/{user.name}:\x01*\x12\xd3\x01\n\x06\x44\x65lete\x12\x30.yandex.cloud.mdb.greenplum.v1.DeleteUserRequest\x1a!.yandex.cloud.operation.Operation\"t\xb2\xd2*+\n\x12\x44\x65leteUserMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02?*=/managed-greenplum/v1/clusters/{cluster_id}/users/{user_name}Bp\n!yandex.cloud.api.mdb.greenplum.v1ZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/greenplum/v1;greenplumb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.greenplum.v1.user_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!yandex.cloud.api.mdb.greenplum.v1ZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/greenplum/v1;greenplum'
  _globals['_CREATEUSERMETADATA'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_CREATEUSERMETADATA'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_CREATEUSERMETADATA'].fields_by_name['user_name']._loaded_options = None
  _globals['_CREATEUSERMETADATA'].fields_by_name['user_name']._serialized_options = b'\350\3071\001\362\3071\035^[a-zA-Z_][a-zA-Z0-9_]{0,62}$\212\3101\0041-63'
  _globals['_UPDATEUSERMETADATA'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_UPDATEUSERMETADATA'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_UPDATEUSERMETADATA'].fields_by_name['user_name']._loaded_options = None
  _globals['_UPDATEUSERMETADATA'].fields_by_name['user_name']._serialized_options = b'\350\3071\001\362\3071\035^[a-zA-Z_][a-zA-Z0-9_]{0,62}$\212\3101\0041-63'
  _globals['_DELETEUSERMETADATA'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_DELETEUSERMETADATA'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_DELETEUSERMETADATA'].fields_by_name['user_name']._loaded_options = None
  _globals['_DELETEUSERMETADATA'].fields_by_name['user_name']._serialized_options = b'\350\3071\001\362\3071\035^[a-zA-Z_][a-zA-Z0-9_]{0,62}$\212\3101\0041-63'
  _globals['_LISTUSERSREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_LISTUSERSREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_GETUSERATREVISIONREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_GETUSERATREVISIONREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_GETUSERATREVISIONREQUEST'].fields_by_name['revision']._loaded_options = None
  _globals['_GETUSERATREVISIONREQUEST'].fields_by_name['revision']._serialized_options = b'\372\3071\002>0'
  _globals['_GETUSERATREVISIONREQUEST'].fields_by_name['user_name']._loaded_options = None
  _globals['_GETUSERATREVISIONREQUEST'].fields_by_name['user_name']._serialized_options = b'\350\3071\001\362\3071\035^[a-zA-Z_][a-zA-Z0-9_]{0,62}$\212\3101\0041-63'
  _globals['_CREATEUSERREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_CREATEUSERREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_CREATEUSERREQUEST'].fields_by_name['user']._loaded_options = None
  _globals['_CREATEUSERREQUEST'].fields_by_name['user']._serialized_options = b'\350\3071\001'
  _globals['_UPDATEUSERREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_UPDATEUSERREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_UPDATEUSERREQUEST'].fields_by_name['user']._loaded_options = None
  _globals['_UPDATEUSERREQUEST'].fields_by_name['user']._serialized_options = b'\350\3071\001'
  _globals['_DELETEUSERREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_DELETEUSERREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_DELETEUSERREQUEST'].fields_by_name['user_name']._loaded_options = None
  _globals['_DELETEUSERREQUEST'].fields_by_name['user_name']._serialized_options = b'\350\3071\001\362\3071\035^[a-zA-Z_][a-zA-Z0-9_]{0,62}$\212\3101\0041-63'
  _globals['_USERSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_USERSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\0023\0221/managed-greenplum/v1/clusters/{cluster_id}/users'
  _globals['_USERSERVICE'].methods_by_name['Create']._loaded_options = None
  _globals['_USERSERVICE'].methods_by_name['Create']._serialized_options = b'\262\322*\032\n\022CreateUserMetadata\022\004User\202\323\344\223\0026\"1/managed-greenplum/v1/clusters/{cluster_id}/users:\001*'
  _globals['_USERSERVICE'].methods_by_name['Update']._loaded_options = None
  _globals['_USERSERVICE'].methods_by_name['Update']._serialized_options = b'\262\322*\032\n\022UpdateUserMetadata\022\004User\202\323\344\223\002B2=/managed-greenplum/v1/clusters/{cluster_id}/users/{user.name}:\001*'
  _globals['_USERSERVICE'].methods_by_name['Delete']._loaded_options = None
  _globals['_USERSERVICE'].methods_by_name['Delete']._serialized_options = b'\262\322*+\n\022DeleteUserMetadata\022\025google.protobuf.Empty\202\323\344\223\002?*=/managed-greenplum/v1/clusters/{cluster_id}/users/{user_name}'
  _globals['_CREATEUSERMETADATA']._serialized_start=294
  _globals['_CREATEUSERMETADATA']._serialized_end=414
  _globals['_UPDATEUSERMETADATA']._serialized_start=416
  _globals['_UPDATEUSERMETADATA']._serialized_end=536
  _globals['_DELETEUSERMETADATA']._serialized_start=538
  _globals['_DELETEUSERMETADATA']._serialized_end=658
  _globals['_LISTUSERSREQUEST']._serialized_start=660
  _globals['_LISTUSERSREQUEST']._serialized_end=712
  _globals['_LISTUSERSRESPONSE']._serialized_start=714
  _globals['_LISTUSERSRESPONSE']._serialized_end=785
  _globals['_GETUSERATREVISIONREQUEST']._serialized_start=788
  _globals['_GETUSERATREVISIONREQUEST']._serialized_end=940
  _globals['_CREATEUSERREQUEST']._serialized_start=942
  _globals['_CREATEUSERREQUEST']._serialized_end=1052
  _globals['_UPDATEUSERREQUEST']._serialized_start=1055
  _globals['_UPDATEUSERREQUEST']._serialized_end=1214
  _globals['_DELETEUSERREQUEST']._serialized_start=1216
  _globals['_DELETEUSERREQUEST']._serialized_end=1335
  _globals['_USERSERVICE']._serialized_start=1338
  _globals['_USERSERVICE']._serialized_end=2120
# @@protoc_insertion_point(module_scope)
