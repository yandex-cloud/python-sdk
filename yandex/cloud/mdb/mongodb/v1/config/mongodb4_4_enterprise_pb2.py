# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/mongodb/v1/config/mongodb4_4_enterprise.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>yandex/cloud/mdb/mongodb/v1/config/mongodb4_4_enterprise.proto\x12\"yandex.cloud.mdb.mongodb.v1.config\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dyandex/cloud/validation.proto\"\x9d\x16\n\x1aMongodConfig4_4_enterprise\x12W\n\x07storage\x18\x01 \x01(\x0b\x32\x46.yandex.cloud.mdb.mongodb.v1.config.MongodConfig4_4_enterprise.Storage\x12n\n\x13operation_profiling\x18\x02 \x01(\x0b\x32Q.yandex.cloud.mdb.mongodb.v1.config.MongodConfig4_4_enterprise.OperationProfiling\x12S\n\x03net\x18\x03 \x01(\x0b\x32\x46.yandex.cloud.mdb.mongodb.v1.config.MongodConfig4_4_enterprise.Network\x12Y\n\x08security\x18\x04 \x01(\x0b\x32G.yandex.cloud.mdb.mongodb.v1.config.MongodConfig4_4_enterprise.Security\x12Z\n\taudit_log\x18\x05 \x01(\x0b\x32G.yandex.cloud.mdb.mongodb.v1.config.MongodConfig4_4_enterprise.AuditLog\x12\x62\n\rset_parameter\x18\x06 \x01(\x0b\x32K.yandex.cloud.mdb.mongodb.v1.config.MongodConfig4_4_enterprise.SetParameter\x1a\x97\x08\n\x07Storage\x12\x66\n\x0bwired_tiger\x18\x01 \x01(\x0b\x32Q.yandex.cloud.mdb.mongodb.v1.config.MongodConfig4_4_enterprise.Storage.WiredTiger\x12_\n\x07journal\x18\x02 \x01(\x0b\x32N.yandex.cloud.mdb.mongodb.v1.config.MongodConfig4_4_enterprise.Storage.Journal\x1a\xf6\x05\n\nWiredTiger\x12u\n\rengine_config\x18\x01 \x01(\x0b\x32^.yandex.cloud.mdb.mongodb.v1.config.MongodConfig4_4_enterprise.Storage.WiredTiger.EngineConfig\x12}\n\x11\x63ollection_config\x18\x02 \x01(\x0b\x32\x62.yandex.cloud.mdb.mongodb.v1.config.MongodConfig4_4_enterprise.Storage.WiredTiger.CollectionConfig\x12s\n\x0cindex_config\x18\x03 \x01(\x0b\x32].yandex.cloud.mdb.mongodb.v1.config.MongodConfig4_4_enterprise.Storage.WiredTiger.IndexConfig\x1a\x43\n\x0c\x45ngineConfig\x12\x33\n\rcache_size_gb\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x1a\xf0\x01\n\x10\x43ollectionConfig\x12\x87\x01\n\x10\x62lock_compressor\x18\x01 \x01(\x0e\x32m.yandex.cloud.mdb.mongodb.v1.config.MongodConfig4_4_enterprise.Storage.WiredTiger.CollectionConfig.Compressor\"R\n\nCompressor\x12\x1a\n\x16\x43OMPRESSOR_UNSPECIFIED\x10\x00\x12\x08\n\x04NONE\x10\x01\x12\n\n\x06SNAPPY\x10\x02\x12\x08\n\x04ZLIB\x10\x03\x12\x08\n\x04ZSTD\x10\x04\x1a\x45\n\x0bIndexConfig\x12\x36\n\x12prefix_compression\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x1aJ\n\x07Journal\x12?\n\x0f\x63ommit_interval\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\t\xfa\xc7\x31\x05\x31-500\x1a\xbb\x02\n\x12OperationProfiling\x12\x64\n\x04mode\x18\x01 \x01(\x0e\x32V.yandex.cloud.mdb.mongodb.v1.config.MongodConfig4_4_enterprise.OperationProfiling.Mode\x12>\n\x11slow_op_threshold\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x06\xfa\xc7\x31\x02>0\x12\x42\n\x13slow_op_sample_rate\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueB\x07\xfa\xc7\x31\x03\x30-1\";\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\x07\n\x03OFF\x10\x01\x12\x0b\n\x07SLOW_OP\x10\x02\x12\x07\n\x03\x41LL\x10\x03\x1a\x96\x03\n\x07Network\x12K\n\x18max_incoming_connections\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0c\xfa\xc7\x31\x08\x31\x30-16384\x12g\n\x0b\x63ompression\x18\x02 \x01(\x0b\x32R.yandex.cloud.mdb.mongodb.v1.config.MongodConfig4_4_enterprise.Network.Compression\x1a\xd4\x01\n\x0b\x43ompression\x12{\n\x0b\x63ompressors\x18\x01 \x03(\x0e\x32].yandex.cloud.mdb.mongodb.v1.config.MongodConfig4_4_enterprise.Network.Compression.CompressorB\x07\x82\xc8\x31\x03\x30-3\"H\n\nCompressor\x12\x1a\n\x16\x43OMPRESSOR_UNSPECIFIED\x10\x00\x12\n\n\x06SNAPPY\x10\x01\x12\x08\n\x04ZLIB\x10\x02\x12\x08\n\x04ZSTD\x10\x03\x1a\xad\x02\n\x08Security\x12\x35\n\x11\x65nable_encryption\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12Z\n\x04kmip\x18\x02 \x01(\x0b\x32L.yandex.cloud.mdb.mongodb.v1.config.MongodConfig4_4_enterprise.Security.KMIP\x1a\x8d\x01\n\x04KMIP\x12\x13\n\x0bserver_name\x18\x01 \x01(\t\x12)\n\x04port\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x11\n\tserver_ca\x18\x03 \x01(\t\x12\x1a\n\x12\x63lient_certificate\x18\x04 \x01(\t\x12\x16\n\x0ekey_identifier\x18\x05 \x01(\t\x1a\x1a\n\x08\x41uditLog\x12\x0e\n\x06\x66ilter\x18\x01 \x01(\t\x1a\x88\x01\n\x0cSetParameter\x12?\n\x1b\x61udit_authorization_success\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x37\n\x13\x65nable_flow_control\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"\xd9\x07\n\x1cMongoCfgConfig4_4_enterprise\x12Y\n\x07storage\x18\x01 \x01(\x0b\x32H.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig4_4_enterprise.Storage\x12p\n\x13operation_profiling\x18\x02 \x01(\x0b\x32S.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig4_4_enterprise.OperationProfiling\x12U\n\x03net\x18\x03 \x01(\x0b\x32H.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig4_4_enterprise.Network\x1a\xc0\x02\n\x07Storage\x12h\n\x0bwired_tiger\x18\x01 \x01(\x0b\x32S.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig4_4_enterprise.Storage.WiredTiger\x1a\xca\x01\n\nWiredTiger\x12w\n\rengine_config\x18\x01 \x01(\x0b\x32`.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig4_4_enterprise.Storage.WiredTiger.EngineConfig\x1a\x43\n\x0c\x45ngineConfig\x12\x33\n\rcache_size_gb\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x1a\xf9\x01\n\x12OperationProfiling\x12\x66\n\x04mode\x18\x01 \x01(\x0e\x32X.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig4_4_enterprise.OperationProfiling.Mode\x12>\n\x11slow_op_threshold\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x06\xfa\xc7\x31\x02>0\";\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\x07\n\x03OFF\x10\x01\x12\x0b\n\x07SLOW_OP\x10\x02\x12\x07\n\x03\x41LL\x10\x03\x1aV\n\x07Network\x12K\n\x18max_incoming_connections\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0c\xfa\xc7\x31\x08\x31\x30-16384\"\x8a\x04\n\x1aMongosConfig4_4_enterprise\x12S\n\x03net\x18\x01 \x01(\x0b\x32\x46.yandex.cloud.mdb.mongodb.v1.config.MongosConfig4_4_enterprise.Network\x1a\x96\x03\n\x07Network\x12K\n\x18max_incoming_connections\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0c\xfa\xc7\x31\x08\x31\x30-16384\x12g\n\x0b\x63ompression\x18\x02 \x01(\x0b\x32R.yandex.cloud.mdb.mongodb.v1.config.MongosConfig4_4_enterprise.Network.Compression\x1a\xd4\x01\n\x0b\x43ompression\x12{\n\x0b\x63ompressors\x18\x01 \x03(\x0e\x32].yandex.cloud.mdb.mongodb.v1.config.MongosConfig4_4_enterprise.Network.Compression.CompressorB\x07\x82\xc8\x31\x03\x30-3\"H\n\nCompressor\x12\x1a\n\x16\x43OMPRESSOR_UNSPECIFIED\x10\x00\x12\n\n\x06SNAPPY\x10\x01\x12\x08\n\x04ZLIB\x10\x02\x12\x08\n\x04ZSTD\x10\x03\"\xa6\x02\n\x1dMongodConfigSet4_4_enterprise\x12X\n\x10\x65\x66\x66\x65\x63tive_config\x18\x01 \x01(\x0b\x32>.yandex.cloud.mdb.mongodb.v1.config.MongodConfig4_4_enterprise\x12S\n\x0buser_config\x18\x02 \x01(\x0b\x32>.yandex.cloud.mdb.mongodb.v1.config.MongodConfig4_4_enterprise\x12V\n\x0e\x64\x65\x66\x61ult_config\x18\x03 \x01(\x0b\x32>.yandex.cloud.mdb.mongodb.v1.config.MongodConfig4_4_enterprise\"\xae\x02\n\x1fMongoCfgConfigSet4_4_enterprise\x12Z\n\x10\x65\x66\x66\x65\x63tive_config\x18\x01 \x01(\x0b\x32@.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig4_4_enterprise\x12U\n\x0buser_config\x18\x02 \x01(\x0b\x32@.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig4_4_enterprise\x12X\n\x0e\x64\x65\x66\x61ult_config\x18\x03 \x01(\x0b\x32@.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig4_4_enterprise\"\xa6\x02\n\x1dMongosConfigSet4_4_enterprise\x12X\n\x10\x65\x66\x66\x65\x63tive_config\x18\x01 \x01(\x0b\x32>.yandex.cloud.mdb.mongodb.v1.config.MongosConfig4_4_enterprise\x12S\n\x0buser_config\x18\x02 \x01(\x0b\x32>.yandex.cloud.mdb.mongodb.v1.config.MongosConfig4_4_enterprise\x12V\n\x0e\x64\x65\x66\x61ult_config\x18\x03 \x01(\x0b\x32>.yandex.cloud.mdb.mongodb.v1.config.MongosConfig4_4_enterpriseBx\n&yandex.cloud.api.mdb.mongodb.v1.configZNgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mongodb/v1/config;mongodbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.mongodb.v1.config.mongodb4_4_enterprise_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n&yandex.cloud.api.mdb.mongodb.v1.configZNgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mongodb/v1/config;mongodb'
  _MONGODCONFIG4_4_ENTERPRISE_STORAGE_JOURNAL.fields_by_name['commit_interval']._options = None
  _MONGODCONFIG4_4_ENTERPRISE_STORAGE_JOURNAL.fields_by_name['commit_interval']._serialized_options = b'\372\3071\0051-500'
  _MONGODCONFIG4_4_ENTERPRISE_OPERATIONPROFILING.fields_by_name['slow_op_threshold']._options = None
  _MONGODCONFIG4_4_ENTERPRISE_OPERATIONPROFILING.fields_by_name['slow_op_threshold']._serialized_options = b'\372\3071\002>0'
  _MONGODCONFIG4_4_ENTERPRISE_OPERATIONPROFILING.fields_by_name['slow_op_sample_rate']._options = None
  _MONGODCONFIG4_4_ENTERPRISE_OPERATIONPROFILING.fields_by_name['slow_op_sample_rate']._serialized_options = b'\372\3071\0030-1'
  _MONGODCONFIG4_4_ENTERPRISE_NETWORK_COMPRESSION.fields_by_name['compressors']._options = None
  _MONGODCONFIG4_4_ENTERPRISE_NETWORK_COMPRESSION.fields_by_name['compressors']._serialized_options = b'\202\3101\0030-3'
  _MONGODCONFIG4_4_ENTERPRISE_NETWORK.fields_by_name['max_incoming_connections']._options = None
  _MONGODCONFIG4_4_ENTERPRISE_NETWORK.fields_by_name['max_incoming_connections']._serialized_options = b'\372\3071\01010-16384'
  _MONGOCFGCONFIG4_4_ENTERPRISE_OPERATIONPROFILING.fields_by_name['slow_op_threshold']._options = None
  _MONGOCFGCONFIG4_4_ENTERPRISE_OPERATIONPROFILING.fields_by_name['slow_op_threshold']._serialized_options = b'\372\3071\002>0'
  _MONGOCFGCONFIG4_4_ENTERPRISE_NETWORK.fields_by_name['max_incoming_connections']._options = None
  _MONGOCFGCONFIG4_4_ENTERPRISE_NETWORK.fields_by_name['max_incoming_connections']._serialized_options = b'\372\3071\01010-16384'
  _MONGOSCONFIG4_4_ENTERPRISE_NETWORK_COMPRESSION.fields_by_name['compressors']._options = None
  _MONGOSCONFIG4_4_ENTERPRISE_NETWORK_COMPRESSION.fields_by_name['compressors']._serialized_options = b'\202\3101\0030-3'
  _MONGOSCONFIG4_4_ENTERPRISE_NETWORK.fields_by_name['max_incoming_connections']._options = None
  _MONGOSCONFIG4_4_ENTERPRISE_NETWORK.fields_by_name['max_incoming_connections']._serialized_options = b'\372\3071\01010-16384'
  _globals['_MONGODCONFIG4_4_ENTERPRISE']._serialized_start=166
  _globals['_MONGODCONFIG4_4_ENTERPRISE']._serialized_end=3011
  _globals['_MONGODCONFIG4_4_ENTERPRISE_STORAGE']._serialized_start=766
  _globals['_MONGODCONFIG4_4_ENTERPRISE_STORAGE']._serialized_end=1813
  _globals['_MONGODCONFIG4_4_ENTERPRISE_STORAGE_WIREDTIGER']._serialized_start=979
  _globals['_MONGODCONFIG4_4_ENTERPRISE_STORAGE_WIREDTIGER']._serialized_end=1737
  _globals['_MONGODCONFIG4_4_ENTERPRISE_STORAGE_WIREDTIGER_ENGINECONFIG']._serialized_start=1356
  _globals['_MONGODCONFIG4_4_ENTERPRISE_STORAGE_WIREDTIGER_ENGINECONFIG']._serialized_end=1423
  _globals['_MONGODCONFIG4_4_ENTERPRISE_STORAGE_WIREDTIGER_COLLECTIONCONFIG']._serialized_start=1426
  _globals['_MONGODCONFIG4_4_ENTERPRISE_STORAGE_WIREDTIGER_COLLECTIONCONFIG']._serialized_end=1666
  _globals['_MONGODCONFIG4_4_ENTERPRISE_STORAGE_WIREDTIGER_COLLECTIONCONFIG_COMPRESSOR']._serialized_start=1584
  _globals['_MONGODCONFIG4_4_ENTERPRISE_STORAGE_WIREDTIGER_COLLECTIONCONFIG_COMPRESSOR']._serialized_end=1666
  _globals['_MONGODCONFIG4_4_ENTERPRISE_STORAGE_WIREDTIGER_INDEXCONFIG']._serialized_start=1668
  _globals['_MONGODCONFIG4_4_ENTERPRISE_STORAGE_WIREDTIGER_INDEXCONFIG']._serialized_end=1737
  _globals['_MONGODCONFIG4_4_ENTERPRISE_STORAGE_JOURNAL']._serialized_start=1739
  _globals['_MONGODCONFIG4_4_ENTERPRISE_STORAGE_JOURNAL']._serialized_end=1813
  _globals['_MONGODCONFIG4_4_ENTERPRISE_OPERATIONPROFILING']._serialized_start=1816
  _globals['_MONGODCONFIG4_4_ENTERPRISE_OPERATIONPROFILING']._serialized_end=2131
  _globals['_MONGODCONFIG4_4_ENTERPRISE_OPERATIONPROFILING_MODE']._serialized_start=2072
  _globals['_MONGODCONFIG4_4_ENTERPRISE_OPERATIONPROFILING_MODE']._serialized_end=2131
  _globals['_MONGODCONFIG4_4_ENTERPRISE_NETWORK']._serialized_start=2134
  _globals['_MONGODCONFIG4_4_ENTERPRISE_NETWORK']._serialized_end=2540
  _globals['_MONGODCONFIG4_4_ENTERPRISE_NETWORK_COMPRESSION']._serialized_start=2328
  _globals['_MONGODCONFIG4_4_ENTERPRISE_NETWORK_COMPRESSION']._serialized_end=2540
  _globals['_MONGODCONFIG4_4_ENTERPRISE_NETWORK_COMPRESSION_COMPRESSOR']._serialized_start=2468
  _globals['_MONGODCONFIG4_4_ENTERPRISE_NETWORK_COMPRESSION_COMPRESSOR']._serialized_end=2540
  _globals['_MONGODCONFIG4_4_ENTERPRISE_SECURITY']._serialized_start=2543
  _globals['_MONGODCONFIG4_4_ENTERPRISE_SECURITY']._serialized_end=2844
  _globals['_MONGODCONFIG4_4_ENTERPRISE_SECURITY_KMIP']._serialized_start=2703
  _globals['_MONGODCONFIG4_4_ENTERPRISE_SECURITY_KMIP']._serialized_end=2844
  _globals['_MONGODCONFIG4_4_ENTERPRISE_AUDITLOG']._serialized_start=2846
  _globals['_MONGODCONFIG4_4_ENTERPRISE_AUDITLOG']._serialized_end=2872
  _globals['_MONGODCONFIG4_4_ENTERPRISE_SETPARAMETER']._serialized_start=2875
  _globals['_MONGODCONFIG4_4_ENTERPRISE_SETPARAMETER']._serialized_end=3011
  _globals['_MONGOCFGCONFIG4_4_ENTERPRISE']._serialized_start=3014
  _globals['_MONGOCFGCONFIG4_4_ENTERPRISE']._serialized_end=3999
  _globals['_MONGOCFGCONFIG4_4_ENTERPRISE_STORAGE']._serialized_start=3339
  _globals['_MONGOCFGCONFIG4_4_ENTERPRISE_STORAGE']._serialized_end=3659
  _globals['_MONGOCFGCONFIG4_4_ENTERPRISE_STORAGE_WIREDTIGER']._serialized_start=3457
  _globals['_MONGOCFGCONFIG4_4_ENTERPRISE_STORAGE_WIREDTIGER']._serialized_end=3659
  _globals['_MONGOCFGCONFIG4_4_ENTERPRISE_STORAGE_WIREDTIGER_ENGINECONFIG']._serialized_start=1356
  _globals['_MONGOCFGCONFIG4_4_ENTERPRISE_STORAGE_WIREDTIGER_ENGINECONFIG']._serialized_end=1423
  _globals['_MONGOCFGCONFIG4_4_ENTERPRISE_OPERATIONPROFILING']._serialized_start=3662
  _globals['_MONGOCFGCONFIG4_4_ENTERPRISE_OPERATIONPROFILING']._serialized_end=3911
  _globals['_MONGOCFGCONFIG4_4_ENTERPRISE_OPERATIONPROFILING_MODE']._serialized_start=2072
  _globals['_MONGOCFGCONFIG4_4_ENTERPRISE_OPERATIONPROFILING_MODE']._serialized_end=2131
  _globals['_MONGOCFGCONFIG4_4_ENTERPRISE_NETWORK']._serialized_start=2134
  _globals['_MONGOCFGCONFIG4_4_ENTERPRISE_NETWORK']._serialized_end=2220
  _globals['_MONGOSCONFIG4_4_ENTERPRISE']._serialized_start=4002
  _globals['_MONGOSCONFIG4_4_ENTERPRISE']._serialized_end=4524
  _globals['_MONGOSCONFIG4_4_ENTERPRISE_NETWORK']._serialized_start=4118
  _globals['_MONGOSCONFIG4_4_ENTERPRISE_NETWORK']._serialized_end=4524
  _globals['_MONGOSCONFIG4_4_ENTERPRISE_NETWORK_COMPRESSION']._serialized_start=4312
  _globals['_MONGOSCONFIG4_4_ENTERPRISE_NETWORK_COMPRESSION']._serialized_end=4524
  _globals['_MONGOSCONFIG4_4_ENTERPRISE_NETWORK_COMPRESSION_COMPRESSOR']._serialized_start=2468
  _globals['_MONGOSCONFIG4_4_ENTERPRISE_NETWORK_COMPRESSION_COMPRESSOR']._serialized_end=2540
  _globals['_MONGODCONFIGSET4_4_ENTERPRISE']._serialized_start=4527
  _globals['_MONGODCONFIGSET4_4_ENTERPRISE']._serialized_end=4821
  _globals['_MONGOCFGCONFIGSET4_4_ENTERPRISE']._serialized_start=4824
  _globals['_MONGOCFGCONFIGSET4_4_ENTERPRISE']._serialized_end=5126
  _globals['_MONGOSCONFIGSET4_4_ENTERPRISE']._serialized_start=5129
  _globals['_MONGOSCONFIGSET4_4_ENTERPRISE']._serialized_end=5423
# @@protoc_insertion_point(module_scope)
