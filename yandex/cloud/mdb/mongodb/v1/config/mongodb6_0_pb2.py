# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/mongodb/v1/config/mongodb6_0.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3yandex/cloud/mdb/mongodb/v1/config/mongodb6_0.proto\x12\"yandex.cloud.mdb.mongodb.v1.config\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dyandex/cloud/validation.proto\"\xa1\x11\n\x0fMongodConfig6_0\x12L\n\x07storage\x18\x01 \x01(\x0b\x32;.yandex.cloud.mdb.mongodb.v1.config.MongodConfig6_0.Storage\x12\x63\n\x13operation_profiling\x18\x02 \x01(\x0b\x32\x46.yandex.cloud.mdb.mongodb.v1.config.MongodConfig6_0.OperationProfiling\x12H\n\x03net\x18\x03 \x01(\x0b\x32;.yandex.cloud.mdb.mongodb.v1.config.MongodConfig6_0.Network\x12W\n\rset_parameter\x18\x04 \x01(\x0b\x32@.yandex.cloud.mdb.mongodb.v1.config.MongodConfig6_0.SetParameter\x1a\xd4\x07\n\x07Storage\x12[\n\x0bwired_tiger\x18\x01 \x01(\x0b\x32\x46.yandex.cloud.mdb.mongodb.v1.config.MongodConfig6_0.Storage.WiredTiger\x12T\n\x07journal\x18\x02 \x01(\x0b\x32\x43.yandex.cloud.mdb.mongodb.v1.config.MongodConfig6_0.Storage.Journal\x1a\xc9\x05\n\nWiredTiger\x12j\n\rengine_config\x18\x01 \x01(\x0b\x32S.yandex.cloud.mdb.mongodb.v1.config.MongodConfig6_0.Storage.WiredTiger.EngineConfig\x12r\n\x11\x63ollection_config\x18\x02 \x01(\x0b\x32W.yandex.cloud.mdb.mongodb.v1.config.MongodConfig6_0.Storage.WiredTiger.CollectionConfig\x12h\n\x0cindex_config\x18\x03 \x01(\x0b\x32R.yandex.cloud.mdb.mongodb.v1.config.MongodConfig6_0.Storage.WiredTiger.IndexConfig\x1a\x43\n\x0c\x45ngineConfig\x12\x33\n\rcache_size_gb\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x1a\xe4\x01\n\x10\x43ollectionConfig\x12|\n\x10\x62lock_compressor\x18\x01 \x01(\x0e\x32\x62.yandex.cloud.mdb.mongodb.v1.config.MongodConfig6_0.Storage.WiredTiger.CollectionConfig.Compressor\"R\n\nCompressor\x12\x1a\n\x16\x43OMPRESSOR_UNSPECIFIED\x10\x00\x12\x08\n\x04NONE\x10\x01\x12\n\n\x06SNAPPY\x10\x02\x12\x08\n\x04ZLIB\x10\x03\x12\x08\n\x04ZSTD\x10\x04\x1a\x45\n\x0bIndexConfig\x12\x36\n\x12prefix_compression\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x1aJ\n\x07Journal\x12?\n\x0f\x63ommit_interval\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\t\xfa\xc7\x31\x05\x31-500\x1a\xb0\x02\n\x12OperationProfiling\x12Y\n\x04mode\x18\x01 \x01(\x0e\x32K.yandex.cloud.mdb.mongodb.v1.config.MongodConfig6_0.OperationProfiling.Mode\x12>\n\x11slow_op_threshold\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x06\xfa\xc7\x31\x02>0\x12\x42\n\x13slow_op_sample_rate\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueB\x07\xfa\xc7\x31\x03\x30-1\";\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\x07\n\x03OFF\x10\x01\x12\x0b\n\x07SLOW_OP\x10\x02\x12\x07\n\x03\x41LL\x10\x03\x1a\x8e\x03\n\x07Network\x12K\n\x18max_incoming_connections\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0c\xfa\xc7\x31\x08\x31\x30-16384\x12\\\n\x0b\x63ompression\x18\x02 \x01(\x0b\x32G.yandex.cloud.mdb.mongodb.v1.config.MongodConfig6_0.Network.Compression\x1a\xd7\x01\n\x0b\x43ompression\x12p\n\x0b\x63ompressors\x18\x01 \x03(\x0e\x32R.yandex.cloud.mdb.mongodb.v1.config.MongodConfig6_0.Network.Compression.CompressorB\x07\x82\xc8\x31\x03\x31-3\"V\n\nCompressor\x12\x1a\n\x16\x43OMPRESSOR_UNSPECIFIED\x10\x00\x12\n\n\x06SNAPPY\x10\x01\x12\x08\n\x04ZLIB\x10\x02\x12\x08\n\x04ZSTD\x10\x03\x12\x0c\n\x08\x44ISABLED\x10\x04\x1a\x9c\x01\n\x0cSetParameter\x12\x37\n\x13\x65nable_flow_control\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12S\n&min_snapshot_history_window_in_seconds\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x06\xfa\xc7\x31\x02>0\"\x8c\x07\n\x11MongoCfgConfig6_0\x12N\n\x07storage\x18\x01 \x01(\x0b\x32=.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig6_0.Storage\x12\x65\n\x13operation_profiling\x18\x02 \x01(\x0b\x32H.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig6_0.OperationProfiling\x12J\n\x03net\x18\x03 \x01(\x0b\x32=.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig6_0.Network\x1a\xaa\x02\n\x07Storage\x12]\n\x0bwired_tiger\x18\x01 \x01(\x0b\x32H.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig6_0.Storage.WiredTiger\x1a\xbf\x01\n\nWiredTiger\x12l\n\rengine_config\x18\x01 \x01(\x0b\x32U.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig6_0.Storage.WiredTiger.EngineConfig\x1a\x43\n\x0c\x45ngineConfig\x12\x33\n\rcache_size_gb\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x1a\xee\x01\n\x12OperationProfiling\x12[\n\x04mode\x18\x01 \x01(\x0e\x32M.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig6_0.OperationProfiling.Mode\x12>\n\x11slow_op_threshold\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x06\xfa\xc7\x31\x02>0\";\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\x07\n\x03OFF\x10\x01\x12\x0b\n\x07SLOW_OP\x10\x02\x12\x07\n\x03\x41LL\x10\x03\x1aV\n\x07Network\x12K\n\x18max_incoming_connections\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0c\xfa\xc7\x31\x08\x31\x30-16384\"\xec\x03\n\x0fMongosConfig6_0\x12H\n\x03net\x18\x03 \x01(\x0b\x32;.yandex.cloud.mdb.mongodb.v1.config.MongosConfig6_0.Network\x1a\x8e\x03\n\x07Network\x12K\n\x18max_incoming_connections\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0c\xfa\xc7\x31\x08\x31\x30-16384\x12\\\n\x0b\x63ompression\x18\x02 \x01(\x0b\x32G.yandex.cloud.mdb.mongodb.v1.config.MongosConfig6_0.Network.Compression\x1a\xd7\x01\n\x0b\x43ompression\x12p\n\x0b\x63ompressors\x18\x01 \x03(\x0e\x32R.yandex.cloud.mdb.mongodb.v1.config.MongosConfig6_0.Network.Compression.CompressorB\x07\x82\xc8\x31\x03\x31-3\"V\n\nCompressor\x12\x1a\n\x16\x43OMPRESSOR_UNSPECIFIED\x10\x00\x12\n\n\x06SNAPPY\x10\x01\x12\x08\n\x04ZLIB\x10\x02\x12\x08\n\x04ZSTD\x10\x03\x12\x0c\n\x08\x44ISABLED\x10\x04\"\xfa\x01\n\x12MongodConfigSet6_0\x12M\n\x10\x65\x66\x66\x65\x63tive_config\x18\x01 \x01(\x0b\x32\x33.yandex.cloud.mdb.mongodb.v1.config.MongodConfig6_0\x12H\n\x0buser_config\x18\x02 \x01(\x0b\x32\x33.yandex.cloud.mdb.mongodb.v1.config.MongodConfig6_0\x12K\n\x0e\x64\x65\x66\x61ult_config\x18\x03 \x01(\x0b\x32\x33.yandex.cloud.mdb.mongodb.v1.config.MongodConfig6_0\"\x82\x02\n\x14MongoCfgConfigSet6_0\x12O\n\x10\x65\x66\x66\x65\x63tive_config\x18\x01 \x01(\x0b\x32\x35.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig6_0\x12J\n\x0buser_config\x18\x02 \x01(\x0b\x32\x35.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig6_0\x12M\n\x0e\x64\x65\x66\x61ult_config\x18\x03 \x01(\x0b\x32\x35.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig6_0\"\xfa\x01\n\x12MongosConfigSet6_0\x12M\n\x10\x65\x66\x66\x65\x63tive_config\x18\x01 \x01(\x0b\x32\x33.yandex.cloud.mdb.mongodb.v1.config.MongosConfig6_0\x12H\n\x0buser_config\x18\x02 \x01(\x0b\x32\x33.yandex.cloud.mdb.mongodb.v1.config.MongosConfig6_0\x12K\n\x0e\x64\x65\x66\x61ult_config\x18\x03 \x01(\x0b\x32\x33.yandex.cloud.mdb.mongodb.v1.config.MongosConfig6_0Bx\n&yandex.cloud.api.mdb.mongodb.v1.configZNgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mongodb/v1/config;mongodbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.mongodb.v1.config.mongodb6_0_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n&yandex.cloud.api.mdb.mongodb.v1.configZNgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mongodb/v1/config;mongodb'
  _MONGODCONFIG6_0_STORAGE_JOURNAL.fields_by_name['commit_interval']._options = None
  _MONGODCONFIG6_0_STORAGE_JOURNAL.fields_by_name['commit_interval']._serialized_options = b'\372\3071\0051-500'
  _MONGODCONFIG6_0_OPERATIONPROFILING.fields_by_name['slow_op_threshold']._options = None
  _MONGODCONFIG6_0_OPERATIONPROFILING.fields_by_name['slow_op_threshold']._serialized_options = b'\372\3071\002>0'
  _MONGODCONFIG6_0_OPERATIONPROFILING.fields_by_name['slow_op_sample_rate']._options = None
  _MONGODCONFIG6_0_OPERATIONPROFILING.fields_by_name['slow_op_sample_rate']._serialized_options = b'\372\3071\0030-1'
  _MONGODCONFIG6_0_NETWORK_COMPRESSION.fields_by_name['compressors']._options = None
  _MONGODCONFIG6_0_NETWORK_COMPRESSION.fields_by_name['compressors']._serialized_options = b'\202\3101\0031-3'
  _MONGODCONFIG6_0_NETWORK.fields_by_name['max_incoming_connections']._options = None
  _MONGODCONFIG6_0_NETWORK.fields_by_name['max_incoming_connections']._serialized_options = b'\372\3071\01010-16384'
  _MONGODCONFIG6_0_SETPARAMETER.fields_by_name['min_snapshot_history_window_in_seconds']._options = None
  _MONGODCONFIG6_0_SETPARAMETER.fields_by_name['min_snapshot_history_window_in_seconds']._serialized_options = b'\372\3071\002>0'
  _MONGOCFGCONFIG6_0_OPERATIONPROFILING.fields_by_name['slow_op_threshold']._options = None
  _MONGOCFGCONFIG6_0_OPERATIONPROFILING.fields_by_name['slow_op_threshold']._serialized_options = b'\372\3071\002>0'
  _MONGOCFGCONFIG6_0_NETWORK.fields_by_name['max_incoming_connections']._options = None
  _MONGOCFGCONFIG6_0_NETWORK.fields_by_name['max_incoming_connections']._serialized_options = b'\372\3071\01010-16384'
  _MONGOSCONFIG6_0_NETWORK_COMPRESSION.fields_by_name['compressors']._options = None
  _MONGOSCONFIG6_0_NETWORK_COMPRESSION.fields_by_name['compressors']._serialized_options = b'\202\3101\0031-3'
  _MONGOSCONFIG6_0_NETWORK.fields_by_name['max_incoming_connections']._options = None
  _MONGOSCONFIG6_0_NETWORK.fields_by_name['max_incoming_connections']._serialized_options = b'\372\3071\01010-16384'
  _globals['_MONGODCONFIG6_0']._serialized_start=155
  _globals['_MONGODCONFIG6_0']._serialized_end=2364
  _globals['_MONGODCONFIG6_0_STORAGE']._serialized_start=517
  _globals['_MONGODCONFIG6_0_STORAGE']._serialized_end=1497
  _globals['_MONGODCONFIG6_0_STORAGE_WIREDTIGER']._serialized_start=708
  _globals['_MONGODCONFIG6_0_STORAGE_WIREDTIGER']._serialized_end=1421
  _globals['_MONGODCONFIG6_0_STORAGE_WIREDTIGER_ENGINECONFIG']._serialized_start=1052
  _globals['_MONGODCONFIG6_0_STORAGE_WIREDTIGER_ENGINECONFIG']._serialized_end=1119
  _globals['_MONGODCONFIG6_0_STORAGE_WIREDTIGER_COLLECTIONCONFIG']._serialized_start=1122
  _globals['_MONGODCONFIG6_0_STORAGE_WIREDTIGER_COLLECTIONCONFIG']._serialized_end=1350
  _globals['_MONGODCONFIG6_0_STORAGE_WIREDTIGER_COLLECTIONCONFIG_COMPRESSOR']._serialized_start=1268
  _globals['_MONGODCONFIG6_0_STORAGE_WIREDTIGER_COLLECTIONCONFIG_COMPRESSOR']._serialized_end=1350
  _globals['_MONGODCONFIG6_0_STORAGE_WIREDTIGER_INDEXCONFIG']._serialized_start=1352
  _globals['_MONGODCONFIG6_0_STORAGE_WIREDTIGER_INDEXCONFIG']._serialized_end=1421
  _globals['_MONGODCONFIG6_0_STORAGE_JOURNAL']._serialized_start=1423
  _globals['_MONGODCONFIG6_0_STORAGE_JOURNAL']._serialized_end=1497
  _globals['_MONGODCONFIG6_0_OPERATIONPROFILING']._serialized_start=1500
  _globals['_MONGODCONFIG6_0_OPERATIONPROFILING']._serialized_end=1804
  _globals['_MONGODCONFIG6_0_OPERATIONPROFILING_MODE']._serialized_start=1745
  _globals['_MONGODCONFIG6_0_OPERATIONPROFILING_MODE']._serialized_end=1804
  _globals['_MONGODCONFIG6_0_NETWORK']._serialized_start=1807
  _globals['_MONGODCONFIG6_0_NETWORK']._serialized_end=2205
  _globals['_MONGODCONFIG6_0_NETWORK_COMPRESSION']._serialized_start=1990
  _globals['_MONGODCONFIG6_0_NETWORK_COMPRESSION']._serialized_end=2205
  _globals['_MONGODCONFIG6_0_NETWORK_COMPRESSION_COMPRESSOR']._serialized_start=2119
  _globals['_MONGODCONFIG6_0_NETWORK_COMPRESSION_COMPRESSOR']._serialized_end=2205
  _globals['_MONGODCONFIG6_0_SETPARAMETER']._serialized_start=2208
  _globals['_MONGODCONFIG6_0_SETPARAMETER']._serialized_end=2364
  _globals['_MONGOCFGCONFIG6_0']._serialized_start=2367
  _globals['_MONGOCFGCONFIG6_0']._serialized_end=3275
  _globals['_MONGOCFGCONFIG6_0_STORAGE']._serialized_start=2648
  _globals['_MONGOCFGCONFIG6_0_STORAGE']._serialized_end=2946
  _globals['_MONGOCFGCONFIG6_0_STORAGE_WIREDTIGER']._serialized_start=2755
  _globals['_MONGOCFGCONFIG6_0_STORAGE_WIREDTIGER']._serialized_end=2946
  _globals['_MONGOCFGCONFIG6_0_STORAGE_WIREDTIGER_ENGINECONFIG']._serialized_start=1052
  _globals['_MONGOCFGCONFIG6_0_STORAGE_WIREDTIGER_ENGINECONFIG']._serialized_end=1119
  _globals['_MONGOCFGCONFIG6_0_OPERATIONPROFILING']._serialized_start=2949
  _globals['_MONGOCFGCONFIG6_0_OPERATIONPROFILING']._serialized_end=3187
  _globals['_MONGOCFGCONFIG6_0_OPERATIONPROFILING_MODE']._serialized_start=1745
  _globals['_MONGOCFGCONFIG6_0_OPERATIONPROFILING_MODE']._serialized_end=1804
  _globals['_MONGOCFGCONFIG6_0_NETWORK']._serialized_start=1807
  _globals['_MONGOCFGCONFIG6_0_NETWORK']._serialized_end=1893
  _globals['_MONGOSCONFIG6_0']._serialized_start=3278
  _globals['_MONGOSCONFIG6_0']._serialized_end=3770
  _globals['_MONGOSCONFIG6_0_NETWORK']._serialized_start=3372
  _globals['_MONGOSCONFIG6_0_NETWORK']._serialized_end=3770
  _globals['_MONGOSCONFIG6_0_NETWORK_COMPRESSION']._serialized_start=3555
  _globals['_MONGOSCONFIG6_0_NETWORK_COMPRESSION']._serialized_end=3770
  _globals['_MONGOSCONFIG6_0_NETWORK_COMPRESSION_COMPRESSOR']._serialized_start=2119
  _globals['_MONGOSCONFIG6_0_NETWORK_COMPRESSION_COMPRESSOR']._serialized_end=2205
  _globals['_MONGODCONFIGSET6_0']._serialized_start=3773
  _globals['_MONGODCONFIGSET6_0']._serialized_end=4023
  _globals['_MONGOCFGCONFIGSET6_0']._serialized_start=4026
  _globals['_MONGOCFGCONFIGSET6_0']._serialized_end=4284
  _globals['_MONGOSCONFIGSET6_0']._serialized_start=4287
  _globals['_MONGOSCONFIGSET6_0']._serialized_end=4537
# @@protoc_insertion_point(module_scope)
