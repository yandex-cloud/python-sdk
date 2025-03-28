# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/mdb/spqr/v1/config.proto
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
    'yandex/cloud/mdb/spqr/v1/config.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%yandex/cloud/mdb/spqr/v1/config.proto\x12\x18yandex.cloud.mdb.spqr.v1\x1a\x1dyandex/cloud/validation.proto\x1a\x1egoogle/protobuf/wrappers.proto\")\n\rMDBPostgreSQL\x12\x18\n\ncluster_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"\xf7\x02\n\nSPQRConfig\x12\x36\n\x06router\x18\x01 \x01(\x0b\x32&.yandex.cloud.mdb.spqr.v1.RouterConfig\x12@\n\x0b\x63oordinator\x18\x02 \x01(\x0b\x32+.yandex.cloud.mdb.spqr.v1.CoordinatorConfig\x12>\n\npostgresql\x18\x03 \x01(\x0b\x32*.yandex.cloud.mdb.spqr.v1.PostgreSQLConfig\x12\x34\n\x05infra\x18\x05 \x01(\x0b\x32%.yandex.cloud.mdb.spqr.v1.InfraConfig\x12\x35\n\tlog_level\x18\x06 \x01(\x0e\x32\".yandex.cloud.mdb.spqr.v1.LogLevel\x12<\n\x08\x62\x61lancer\x18\x07 \x01(\x0b\x32*.yandex.cloud.mdb.spqr.v1.BalancerSettingsJ\x04\x08\x04\x10\x05\"\x80\x01\n\x0cRouterConfig\x12\x38\n\x06\x63onfig\x18\x01 \x01(\x0b\x32(.yandex.cloud.mdb.spqr.v1.RouterSettings\x12\x36\n\tresources\x18\x02 \x01(\x0b\x32#.yandex.cloud.mdb.spqr.v1.Resources\"\x8a\x01\n\x11\x43oordinatorConfig\x12=\n\x06\x63onfig\x18\x01 \x01(\x0b\x32-.yandex.cloud.mdb.spqr.v1.CoordinatorSettings\x12\x36\n\tresources\x18\x02 \x01(\x0b\x32#.yandex.cloud.mdb.spqr.v1.Resources\"\x88\x01\n\x10PostgreSQLConfig\x12<\n\x06\x63onfig\x18\x01 \x01(\x0b\x32,.yandex.cloud.mdb.spqr.v1.PostgreSQLSettings\x12\x36\n\tresources\x18\x02 \x01(\x0b\x32#.yandex.cloud.mdb.spqr.v1.Resources\"\xc3\x01\n\x0bInfraConfig\x12\x36\n\tresources\x18\x02 \x01(\x0b\x32#.yandex.cloud.mdb.spqr.v1.Resources\x12\x38\n\x06router\x18\x03 \x01(\x0b\x32(.yandex.cloud.mdb.spqr.v1.RouterSettings\x12\x42\n\x0b\x63oordinator\x18\x04 \x01(\x0b\x32-.yandex.cloud.mdb.spqr.v1.CoordinatorSettings\"\xcd\x02\n\x10\x42\x61lancerSettings\x12\x33\n\rcpu_threshold\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x35\n\x0fspace_threshold\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x36\n\x11stat_interval_sec\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x33\n\x0emax_move_count\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x32\n\rkeys_per_move\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12,\n\x07timeout\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\"\xe0\x02\n\x0eRouterSettings\x12\x38\n\x14show_notice_messages\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x16\n\x0etime_quantiles\x18\x02 \x03(\x01\x12]\n\x16\x64\x65\x66\x61ult_route_behavior\x18\x04 \x01(\x0e\x32=.yandex.cloud.mdb.spqr.v1.RouterSettings.DefaultRouteBehavior\x12\x41\n\x1dprefer_same_availability_zone\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"T\n\x14\x44\x65\x66\x61ultRouteBehavior\x12&\n\"DEFAULT_ROUTE_BEHAVIOR_UNSPECIFIED\x10\x00\x12\t\n\x05\x42LOCK\x10\x01\x12\t\n\x05\x41LLOW\x10\x02J\x04\x08\x03\x10\x04\"\x15\n\x13\x43oordinatorSettings\"\x14\n\x12PostgreSQLSettings\"P\n\tResources\x12\x1a\n\x12resource_preset_id\x18\x01 \x01(\t\x12\x11\n\tdisk_size\x18\x02 \x01(\x03\x12\x14\n\x0c\x64isk_type_id\x18\x03 \x01(\t*h\n\x08LogLevel\x12\x19\n\x15LOG_LEVEL_UNSPECIFIED\x10\x00\x12\t\n\x05\x44\x45\x42UG\x10\x01\x12\x08\n\x04INFO\x10\x02\x12\x0b\n\x07WARNING\x10\x03\x12\t\n\x05\x45RROR\x10\x04\x12\t\n\x05\x46\x41TAL\x10\x05\x12\t\n\x05PANIC\x10\x06\x42\x61\n\x1cyandex.cloud.api.mdb.spqr.v1ZAgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/spqr/v1;spqrb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.spqr.v1.config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034yandex.cloud.api.mdb.spqr.v1ZAgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/spqr/v1;spqr'
  _globals['_MDBPOSTGRESQL'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_MDBPOSTGRESQL'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001'
  _globals['_LOGLEVEL']._serialized_start=1978
  _globals['_LOGLEVEL']._serialized_end=2082
  _globals['_MDBPOSTGRESQL']._serialized_start=130
  _globals['_MDBPOSTGRESQL']._serialized_end=171
  _globals['_SPQRCONFIG']._serialized_start=174
  _globals['_SPQRCONFIG']._serialized_end=549
  _globals['_ROUTERCONFIG']._serialized_start=552
  _globals['_ROUTERCONFIG']._serialized_end=680
  _globals['_COORDINATORCONFIG']._serialized_start=683
  _globals['_COORDINATORCONFIG']._serialized_end=821
  _globals['_POSTGRESQLCONFIG']._serialized_start=824
  _globals['_POSTGRESQLCONFIG']._serialized_end=960
  _globals['_INFRACONFIG']._serialized_start=963
  _globals['_INFRACONFIG']._serialized_end=1158
  _globals['_BALANCERSETTINGS']._serialized_start=1161
  _globals['_BALANCERSETTINGS']._serialized_end=1494
  _globals['_ROUTERSETTINGS']._serialized_start=1497
  _globals['_ROUTERSETTINGS']._serialized_end=1849
  _globals['_ROUTERSETTINGS_DEFAULTROUTEBEHAVIOR']._serialized_start=1759
  _globals['_ROUTERSETTINGS_DEFAULTROUTEBEHAVIOR']._serialized_end=1843
  _globals['_COORDINATORSETTINGS']._serialized_start=1851
  _globals['_COORDINATORSETTINGS']._serialized_end=1872
  _globals['_POSTGRESQLSETTINGS']._serialized_start=1874
  _globals['_POSTGRESQLSETTINGS']._serialized_end=1894
  _globals['_RESOURCES']._serialized_start=1896
  _globals['_RESOURCES']._serialized_end=1976
# @@protoc_insertion_point(module_scope)
