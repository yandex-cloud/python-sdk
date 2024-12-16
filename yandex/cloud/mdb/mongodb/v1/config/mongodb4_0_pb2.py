# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/mdb/mongodb/v1/config/mongodb4_0.proto
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
    'yandex/cloud/mdb/mongodb/v1/config/mongodb4_0.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3yandex/cloud/mdb/mongodb/v1/config/mongodb4_0.proto\x12\"yandex.cloud.mdb.mongodb.v1.config\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dyandex/cloud/validation.proto\"\xf1\n\n\x0fMongodConfig4_0\x12L\n\x07storage\x18\x01 \x01(\x0b\x32;.yandex.cloud.mdb.mongodb.v1.config.MongodConfig4_0.Storage\x12\x63\n\x13operation_profiling\x18\x02 \x01(\x0b\x32\x46.yandex.cloud.mdb.mongodb.v1.config.MongodConfig4_0.OperationProfiling\x12H\n\x03net\x18\x03 \x01(\x0b\x32;.yandex.cloud.mdb.mongodb.v1.config.MongodConfig4_0.Network\x1a\x99\x06\n\x07Storage\x12[\n\x0bwired_tiger\x18\x01 \x01(\x0b\x32\x46.yandex.cloud.mdb.mongodb.v1.config.MongodConfig4_0.Storage.WiredTiger\x12T\n\x07journal\x18\x02 \x01(\x0b\x32\x43.yandex.cloud.mdb.mongodb.v1.config.MongodConfig4_0.Storage.Journal\x1a\x8e\x04\n\nWiredTiger\x12j\n\rengine_config\x18\x01 \x01(\x0b\x32S.yandex.cloud.mdb.mongodb.v1.config.MongodConfig4_0.Storage.WiredTiger.EngineConfig\x12r\n\x11\x63ollection_config\x18\x02 \x01(\x0b\x32W.yandex.cloud.mdb.mongodb.v1.config.MongodConfig4_0.Storage.WiredTiger.CollectionConfig\x1a\x43\n\x0c\x45ngineConfig\x12\x33\n\rcache_size_gb\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x1a\xda\x01\n\x10\x43ollectionConfig\x12|\n\x10\x62lock_compressor\x18\x01 \x01(\x0e\x32\x62.yandex.cloud.mdb.mongodb.v1.config.MongodConfig4_0.Storage.WiredTiger.CollectionConfig.Compressor\"H\n\nCompressor\x12\x1a\n\x16\x43OMPRESSOR_UNSPECIFIED\x10\x00\x12\x08\n\x04NONE\x10\x01\x12\n\n\x06SNAPPY\x10\x02\x12\x08\n\x04ZLIB\x10\x03\x1aJ\n\x07Journal\x12?\n\x0f\x63ommit_interval\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\t\xfa\xc7\x31\x05\x31-500\x1a\xec\x01\n\x12OperationProfiling\x12Y\n\x04mode\x18\x01 \x01(\x0e\x32K.yandex.cloud.mdb.mongodb.v1.config.MongodConfig4_0.OperationProfiling.Mode\x12>\n\x11slow_op_threshold\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x06\xfa\xc7\x31\x02>0\";\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\x07\n\x03OFF\x10\x01\x12\x0b\n\x07SLOW_OP\x10\x02\x12\x07\n\x03\x41LL\x10\x03\x1aV\n\x07Network\x12K\n\x18max_incoming_connections\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0c\xfa\xc7\x31\x08\x31\x30-16384\"\x8c\x07\n\x11MongoCfgConfig4_0\x12N\n\x07storage\x18\x01 \x01(\x0b\x32=.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig4_0.Storage\x12\x65\n\x13operation_profiling\x18\x02 \x01(\x0b\x32H.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig4_0.OperationProfiling\x12J\n\x03net\x18\x03 \x01(\x0b\x32=.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig4_0.Network\x1a\xaa\x02\n\x07Storage\x12]\n\x0bwired_tiger\x18\x01 \x01(\x0b\x32H.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig4_0.Storage.WiredTiger\x1a\xbf\x01\n\nWiredTiger\x12l\n\rengine_config\x18\x01 \x01(\x0b\x32U.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig4_0.Storage.WiredTiger.EngineConfig\x1a\x43\n\x0c\x45ngineConfig\x12\x33\n\rcache_size_gb\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x1a\xee\x01\n\x12OperationProfiling\x12[\n\x04mode\x18\x01 \x01(\x0e\x32M.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig4_0.OperationProfiling.Mode\x12>\n\x11slow_op_threshold\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x06\xfa\xc7\x31\x02>0\";\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\x07\n\x03OFF\x10\x01\x12\x0b\n\x07SLOW_OP\x10\x02\x12\x07\n\x03\x41LL\x10\x03\x1aV\n\x07Network\x12K\n\x18max_incoming_connections\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0c\xfa\xc7\x31\x08\x31\x30-16384\"\xb3\x01\n\x0fMongosConfig4_0\x12H\n\x03net\x18\x01 \x01(\x0b\x32;.yandex.cloud.mdb.mongodb.v1.config.MongosConfig4_0.Network\x1aV\n\x07Network\x12K\n\x18max_incoming_connections\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0c\xfa\xc7\x31\x08\x31\x30-16384\"\xfa\x01\n\x12MongodConfigSet4_0\x12M\n\x10\x65\x66\x66\x65\x63tive_config\x18\x01 \x01(\x0b\x32\x33.yandex.cloud.mdb.mongodb.v1.config.MongodConfig4_0\x12H\n\x0buser_config\x18\x02 \x01(\x0b\x32\x33.yandex.cloud.mdb.mongodb.v1.config.MongodConfig4_0\x12K\n\x0e\x64\x65\x66\x61ult_config\x18\x03 \x01(\x0b\x32\x33.yandex.cloud.mdb.mongodb.v1.config.MongodConfig4_0\"\x82\x02\n\x14MongoCfgConfigSet4_0\x12O\n\x10\x65\x66\x66\x65\x63tive_config\x18\x01 \x01(\x0b\x32\x35.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig4_0\x12J\n\x0buser_config\x18\x02 \x01(\x0b\x32\x35.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig4_0\x12M\n\x0e\x64\x65\x66\x61ult_config\x18\x03 \x01(\x0b\x32\x35.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig4_0\"\xfa\x01\n\x12MongosConfigSet4_0\x12M\n\x10\x65\x66\x66\x65\x63tive_config\x18\x01 \x01(\x0b\x32\x33.yandex.cloud.mdb.mongodb.v1.config.MongosConfig4_0\x12H\n\x0buser_config\x18\x02 \x01(\x0b\x32\x33.yandex.cloud.mdb.mongodb.v1.config.MongosConfig4_0\x12K\n\x0e\x64\x65\x66\x61ult_config\x18\x03 \x01(\x0b\x32\x33.yandex.cloud.mdb.mongodb.v1.config.MongosConfig4_0Bx\n&yandex.cloud.api.mdb.mongodb.v1.configZNgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mongodb/v1/config;mongodbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.mongodb.v1.config.mongodb4_0_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n&yandex.cloud.api.mdb.mongodb.v1.configZNgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mongodb/v1/config;mongodb'
  _globals['_MONGODCONFIG4_0_STORAGE_JOURNAL'].fields_by_name['commit_interval']._loaded_options = None
  _globals['_MONGODCONFIG4_0_STORAGE_JOURNAL'].fields_by_name['commit_interval']._serialized_options = b'\372\3071\0051-500'
  _globals['_MONGODCONFIG4_0_OPERATIONPROFILING'].fields_by_name['slow_op_threshold']._loaded_options = None
  _globals['_MONGODCONFIG4_0_OPERATIONPROFILING'].fields_by_name['slow_op_threshold']._serialized_options = b'\372\3071\002>0'
  _globals['_MONGODCONFIG4_0_NETWORK'].fields_by_name['max_incoming_connections']._loaded_options = None
  _globals['_MONGODCONFIG4_0_NETWORK'].fields_by_name['max_incoming_connections']._serialized_options = b'\372\3071\01010-16384'
  _globals['_MONGOCFGCONFIG4_0_OPERATIONPROFILING'].fields_by_name['slow_op_threshold']._loaded_options = None
  _globals['_MONGOCFGCONFIG4_0_OPERATIONPROFILING'].fields_by_name['slow_op_threshold']._serialized_options = b'\372\3071\002>0'
  _globals['_MONGOCFGCONFIG4_0_NETWORK'].fields_by_name['max_incoming_connections']._loaded_options = None
  _globals['_MONGOCFGCONFIG4_0_NETWORK'].fields_by_name['max_incoming_connections']._serialized_options = b'\372\3071\01010-16384'
  _globals['_MONGOSCONFIG4_0_NETWORK'].fields_by_name['max_incoming_connections']._loaded_options = None
  _globals['_MONGOSCONFIG4_0_NETWORK'].fields_by_name['max_incoming_connections']._serialized_options = b'\372\3071\01010-16384'
  _globals['_MONGODCONFIG4_0']._serialized_start=155
  _globals['_MONGODCONFIG4_0']._serialized_end=1548
  _globals['_MONGODCONFIG4_0_STORAGE']._serialized_start=428
  _globals['_MONGODCONFIG4_0_STORAGE']._serialized_end=1221
  _globals['_MONGODCONFIG4_0_STORAGE_WIREDTIGER']._serialized_start=619
  _globals['_MONGODCONFIG4_0_STORAGE_WIREDTIGER']._serialized_end=1145
  _globals['_MONGODCONFIG4_0_STORAGE_WIREDTIGER_ENGINECONFIG']._serialized_start=857
  _globals['_MONGODCONFIG4_0_STORAGE_WIREDTIGER_ENGINECONFIG']._serialized_end=924
  _globals['_MONGODCONFIG4_0_STORAGE_WIREDTIGER_COLLECTIONCONFIG']._serialized_start=927
  _globals['_MONGODCONFIG4_0_STORAGE_WIREDTIGER_COLLECTIONCONFIG']._serialized_end=1145
  _globals['_MONGODCONFIG4_0_STORAGE_WIREDTIGER_COLLECTIONCONFIG_COMPRESSOR']._serialized_start=1073
  _globals['_MONGODCONFIG4_0_STORAGE_WIREDTIGER_COLLECTIONCONFIG_COMPRESSOR']._serialized_end=1145
  _globals['_MONGODCONFIG4_0_STORAGE_JOURNAL']._serialized_start=1147
  _globals['_MONGODCONFIG4_0_STORAGE_JOURNAL']._serialized_end=1221
  _globals['_MONGODCONFIG4_0_OPERATIONPROFILING']._serialized_start=1224
  _globals['_MONGODCONFIG4_0_OPERATIONPROFILING']._serialized_end=1460
  _globals['_MONGODCONFIG4_0_OPERATIONPROFILING_MODE']._serialized_start=1401
  _globals['_MONGODCONFIG4_0_OPERATIONPROFILING_MODE']._serialized_end=1460
  _globals['_MONGODCONFIG4_0_NETWORK']._serialized_start=1462
  _globals['_MONGODCONFIG4_0_NETWORK']._serialized_end=1548
  _globals['_MONGOCFGCONFIG4_0']._serialized_start=1551
  _globals['_MONGOCFGCONFIG4_0']._serialized_end=2459
  _globals['_MONGOCFGCONFIG4_0_STORAGE']._serialized_start=1832
  _globals['_MONGOCFGCONFIG4_0_STORAGE']._serialized_end=2130
  _globals['_MONGOCFGCONFIG4_0_STORAGE_WIREDTIGER']._serialized_start=1939
  _globals['_MONGOCFGCONFIG4_0_STORAGE_WIREDTIGER']._serialized_end=2130
  _globals['_MONGOCFGCONFIG4_0_STORAGE_WIREDTIGER_ENGINECONFIG']._serialized_start=857
  _globals['_MONGOCFGCONFIG4_0_STORAGE_WIREDTIGER_ENGINECONFIG']._serialized_end=924
  _globals['_MONGOCFGCONFIG4_0_OPERATIONPROFILING']._serialized_start=2133
  _globals['_MONGOCFGCONFIG4_0_OPERATIONPROFILING']._serialized_end=2371
  _globals['_MONGOCFGCONFIG4_0_OPERATIONPROFILING_MODE']._serialized_start=1401
  _globals['_MONGOCFGCONFIG4_0_OPERATIONPROFILING_MODE']._serialized_end=1460
  _globals['_MONGOCFGCONFIG4_0_NETWORK']._serialized_start=1462
  _globals['_MONGOCFGCONFIG4_0_NETWORK']._serialized_end=1548
  _globals['_MONGOSCONFIG4_0']._serialized_start=2462
  _globals['_MONGOSCONFIG4_0']._serialized_end=2641
  _globals['_MONGOSCONFIG4_0_NETWORK']._serialized_start=1462
  _globals['_MONGOSCONFIG4_0_NETWORK']._serialized_end=1548
  _globals['_MONGODCONFIGSET4_0']._serialized_start=2644
  _globals['_MONGODCONFIGSET4_0']._serialized_end=2894
  _globals['_MONGOCFGCONFIGSET4_0']._serialized_start=2897
  _globals['_MONGOCFGCONFIGSET4_0']._serialized_end=3155
  _globals['_MONGOSCONFIGSET4_0']._serialized_start=3158
  _globals['_MONGOSCONFIGSET4_0']._serialized_end=3408
# @@protoc_insertion_point(module_scope)
