# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/sqlserver/v1/config/sqlserver2019.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8yandex/cloud/mdb/sqlserver/v1/config/sqlserver2019.proto\x12$yandex.cloud.mdb.sqlserver.v1.config\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dyandex/cloud/validation.proto\"\xf7\x02\n\x16SQLServerConfig2019std\x12H\n\x19max_degree_of_parallelism\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x08\xfa\xc7\x31\x04\x31-99\x12P\n\x1e\x63ost_threshold_for_parallelism\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0b\xfa\xc7\x31\x07\x35-32767\x12\x39\n\x0b\x61udit_level\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03\x30-3\x12\x43\n\x13\x66ill_factor_percent\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\t\xfa\xc7\x31\x05\x30-100\x12\x41\n\x1doptimize_for_ad_hoc_workloads\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"\x9c\x02\n\x19SQLServerConfigSet2019std\x12V\n\x10\x65\x66\x66\x65\x63tive_config\x18\x01 \x01(\x0b\x32<.yandex.cloud.mdb.sqlserver.v1.config.SQLServerConfig2019std\x12Q\n\x0buser_config\x18\x02 \x01(\x0b\x32<.yandex.cloud.mdb.sqlserver.v1.config.SQLServerConfig2019std\x12T\n\x0e\x64\x65\x66\x61ult_config\x18\x03 \x01(\x0b\x32<.yandex.cloud.mdb.sqlserver.v1.config.SQLServerConfig2019std\"\xf7\x02\n\x16SQLServerConfig2019ent\x12H\n\x19max_degree_of_parallelism\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x08\xfa\xc7\x31\x04\x31-99\x12P\n\x1e\x63ost_threshold_for_parallelism\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0b\xfa\xc7\x31\x07\x35-32767\x12\x39\n\x0b\x61udit_level\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03\x30-3\x12\x43\n\x13\x66ill_factor_percent\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\t\xfa\xc7\x31\x05\x30-100\x12\x41\n\x1doptimize_for_ad_hoc_workloads\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"\x9c\x02\n\x19SQLServerConfigSet2019ent\x12V\n\x10\x65\x66\x66\x65\x63tive_config\x18\x01 \x01(\x0b\x32<.yandex.cloud.mdb.sqlserver.v1.config.SQLServerConfig2019ent\x12Q\n\x0buser_config\x18\x02 \x01(\x0b\x32<.yandex.cloud.mdb.sqlserver.v1.config.SQLServerConfig2019ent\x12T\n\x0e\x64\x65\x66\x61ult_config\x18\x03 \x01(\x0b\x32<.yandex.cloud.mdb.sqlserver.v1.config.SQLServerConfig2019entB~\n(yandex.cloud.api.mdb.sqlserver.v1.configZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/sqlserver/v1/config;sqlserverb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.sqlserver.v1.config.sqlserver2019_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n(yandex.cloud.api.mdb.sqlserver.v1.configZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/sqlserver/v1/config;sqlserver'
  _globals['_SQLSERVERCONFIG2019STD'].fields_by_name['max_degree_of_parallelism']._loaded_options = None
  _globals['_SQLSERVERCONFIG2019STD'].fields_by_name['max_degree_of_parallelism']._serialized_options = b'\372\3071\0041-99'
  _globals['_SQLSERVERCONFIG2019STD'].fields_by_name['cost_threshold_for_parallelism']._loaded_options = None
  _globals['_SQLSERVERCONFIG2019STD'].fields_by_name['cost_threshold_for_parallelism']._serialized_options = b'\372\3071\0075-32767'
  _globals['_SQLSERVERCONFIG2019STD'].fields_by_name['audit_level']._loaded_options = None
  _globals['_SQLSERVERCONFIG2019STD'].fields_by_name['audit_level']._serialized_options = b'\372\3071\0030-3'
  _globals['_SQLSERVERCONFIG2019STD'].fields_by_name['fill_factor_percent']._loaded_options = None
  _globals['_SQLSERVERCONFIG2019STD'].fields_by_name['fill_factor_percent']._serialized_options = b'\372\3071\0050-100'
  _globals['_SQLSERVERCONFIG2019ENT'].fields_by_name['max_degree_of_parallelism']._loaded_options = None
  _globals['_SQLSERVERCONFIG2019ENT'].fields_by_name['max_degree_of_parallelism']._serialized_options = b'\372\3071\0041-99'
  _globals['_SQLSERVERCONFIG2019ENT'].fields_by_name['cost_threshold_for_parallelism']._loaded_options = None
  _globals['_SQLSERVERCONFIG2019ENT'].fields_by_name['cost_threshold_for_parallelism']._serialized_options = b'\372\3071\0075-32767'
  _globals['_SQLSERVERCONFIG2019ENT'].fields_by_name['audit_level']._loaded_options = None
  _globals['_SQLSERVERCONFIG2019ENT'].fields_by_name['audit_level']._serialized_options = b'\372\3071\0030-3'
  _globals['_SQLSERVERCONFIG2019ENT'].fields_by_name['fill_factor_percent']._loaded_options = None
  _globals['_SQLSERVERCONFIG2019ENT'].fields_by_name['fill_factor_percent']._serialized_options = b'\372\3071\0050-100'
  _globals['_SQLSERVERCONFIG2019STD']._serialized_start=162
  _globals['_SQLSERVERCONFIG2019STD']._serialized_end=537
  _globals['_SQLSERVERCONFIGSET2019STD']._serialized_start=540
  _globals['_SQLSERVERCONFIGSET2019STD']._serialized_end=824
  _globals['_SQLSERVERCONFIG2019ENT']._serialized_start=827
  _globals['_SQLSERVERCONFIG2019ENT']._serialized_end=1202
  _globals['_SQLSERVERCONFIGSET2019ENT']._serialized_start=1205
  _globals['_SQLSERVERCONFIGSET2019ENT']._serialized_end=1489
# @@protoc_insertion_point(module_scope)
