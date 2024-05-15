# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/mongodb/v1/database_service.proto
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
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.mdb.mongodb.v1 import database_pb2 as yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_database__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2yandex/cloud/mdb/mongodb/v1/database_service.proto\x12\x1byandex.cloud.mdb.mongodb.v1\x1a\x1cgoogle/api/annotations.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\x1a*yandex/cloud/mdb/mongodb/v1/database.proto\"m\n\x12GetDatabaseRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x35\n\rdatabase_name\x18\x02 \x01(\tB\x1e\xe8\xc7\x31\x01\xf2\xc7\x31\x0e[a-zA-Z0-9_-]*\x8a\xc8\x31\x04<=63\"v\n\x14ListDatabasesRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"j\n\x15ListDatabasesResponse\x12\x38\n\tdatabases\x18\x01 \x03(\x0b\x32%.yandex.cloud.mdb.mongodb.v1.Database\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x81\x01\n\x15\x43reateDatabaseRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x46\n\rdatabase_spec\x18\x02 \x01(\x0b\x32).yandex.cloud.mdb.mongodb.v1.DatabaseSpecB\x04\xe8\xc7\x31\x01\"C\n\x16\x43reateDatabaseMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x15\n\rdatabase_name\x18\x02 \x01(\t\"p\n\x15\x44\x65leteDatabaseRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x35\n\rdatabase_name\x18\x02 \x01(\tB\x1e\xe8\xc7\x31\x01\xf2\xc7\x31\x0e[a-zA-Z0-9_-]*\x8a\xc8\x31\x04<=63\"C\n\x16\x44\x65leteDatabaseMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x15\n\rdatabase_name\x18\x02 \x01(\t2\x95\x06\n\x0f\x44\x61tabaseService\x12\xaa\x01\n\x03Get\x12/.yandex.cloud.mdb.mongodb.v1.GetDatabaseRequest\x1a%.yandex.cloud.mdb.mongodb.v1.Database\"K\x82\xd3\xe4\x93\x02\x45\x12\x43/managed-mongodb/v1/clusters/{cluster_id}/databases/{database_name}\x12\xaa\x01\n\x04List\x12\x31.yandex.cloud.mdb.mongodb.v1.ListDatabasesRequest\x1a\x32.yandex.cloud.mdb.mongodb.v1.ListDatabasesResponse\";\x82\xd3\xe4\x93\x02\x35\x12\x33/managed-mongodb/v1/clusters/{cluster_id}/databases\x12\xc5\x01\n\x06\x43reate\x12\x32.yandex.cloud.mdb.mongodb.v1.CreateDatabaseRequest\x1a!.yandex.cloud.operation.Operation\"d\xb2\xd2*\"\n\x16\x43reateDatabaseMetadata\x12\x08\x44\x61tabase\x82\xd3\xe4\x93\x02\x38\"3/managed-mongodb/v1/clusters/{cluster_id}/databases:\x01*\x12\xdf\x01\n\x06\x44\x65lete\x12\x32.yandex.cloud.mdb.mongodb.v1.DeleteDatabaseRequest\x1a!.yandex.cloud.operation.Operation\"~\xb2\xd2*/\n\x16\x44\x65leteDatabaseMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x45*C/managed-mongodb/v1/clusters/{cluster_id}/databases/{database_name}Bj\n\x1fyandex.cloud.api.mdb.mongodb.v1ZGgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mongodb/v1;mongodbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.mongodb.v1.database_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037yandex.cloud.api.mdb.mongodb.v1ZGgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mongodb/v1;mongodb'
  _globals['_GETDATABASEREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_GETDATABASEREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_GETDATABASEREQUEST'].fields_by_name['database_name']._loaded_options = None
  _globals['_GETDATABASEREQUEST'].fields_by_name['database_name']._serialized_options = b'\350\3071\001\362\3071\016[a-zA-Z0-9_-]*\212\3101\004<=63'
  _globals['_LISTDATABASESREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_LISTDATABASESREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTDATABASESREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTDATABASESREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTDATABASESREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTDATABASESREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_CREATEDATABASEREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_CREATEDATABASEREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_CREATEDATABASEREQUEST'].fields_by_name['database_spec']._loaded_options = None
  _globals['_CREATEDATABASEREQUEST'].fields_by_name['database_spec']._serialized_options = b'\350\3071\001'
  _globals['_DELETEDATABASEREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_DELETEDATABASEREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_DELETEDATABASEREQUEST'].fields_by_name['database_name']._loaded_options = None
  _globals['_DELETEDATABASEREQUEST'].fields_by_name['database_name']._serialized_options = b'\350\3071\001\362\3071\016[a-zA-Z0-9_-]*\212\3101\004<=63'
  _globals['_DATABASESERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_DATABASESERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002E\022C/managed-mongodb/v1/clusters/{cluster_id}/databases/{database_name}'
  _globals['_DATABASESERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_DATABASESERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\0025\0223/managed-mongodb/v1/clusters/{cluster_id}/databases'
  _globals['_DATABASESERVICE'].methods_by_name['Create']._loaded_options = None
  _globals['_DATABASESERVICE'].methods_by_name['Create']._serialized_options = b'\262\322*\"\n\026CreateDatabaseMetadata\022\010Database\202\323\344\223\0028\"3/managed-mongodb/v1/clusters/{cluster_id}/databases:\001*'
  _globals['_DATABASESERVICE'].methods_by_name['Delete']._loaded_options = None
  _globals['_DATABASESERVICE'].methods_by_name['Delete']._serialized_options = b'\262\322*/\n\026DeleteDatabaseMetadata\022\025google.protobuf.Empty\202\323\344\223\002E*C/managed-mongodb/v1/clusters/{cluster_id}/databases/{database_name}'
  _globals['_GETDATABASEREQUEST']._serialized_start=262
  _globals['_GETDATABASEREQUEST']._serialized_end=371
  _globals['_LISTDATABASESREQUEST']._serialized_start=373
  _globals['_LISTDATABASESREQUEST']._serialized_end=491
  _globals['_LISTDATABASESRESPONSE']._serialized_start=493
  _globals['_LISTDATABASESRESPONSE']._serialized_end=599
  _globals['_CREATEDATABASEREQUEST']._serialized_start=602
  _globals['_CREATEDATABASEREQUEST']._serialized_end=731
  _globals['_CREATEDATABASEMETADATA']._serialized_start=733
  _globals['_CREATEDATABASEMETADATA']._serialized_end=800
  _globals['_DELETEDATABASEREQUEST']._serialized_start=802
  _globals['_DELETEDATABASEREQUEST']._serialized_end=914
  _globals['_DELETEDATABASEMETADATA']._serialized_start=916
  _globals['_DELETEDATABASEMETADATA']._serialized_end=983
  _globals['_DATABASESERVICE']._serialized_start=986
  _globals['_DATABASESERVICE']._serialized_end=1775
# @@protoc_insertion_point(module_scope)
