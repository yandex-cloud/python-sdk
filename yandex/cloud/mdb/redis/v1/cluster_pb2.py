# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/redis/v1/cluster.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.type import timeofday_pb2 as google_dot_type_dot_timeofday__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.mdb.redis.v1.config import redis_pb2 as yandex_dot_cloud_dot_mdb_dot_redis_dot_v1_dot_config_dot_redis__pb2
from yandex.cloud.mdb.redis.v1.config import redis5_0_pb2 as yandex_dot_cloud_dot_mdb_dot_redis_dot_v1_dot_config_dot_redis5__0__pb2
from yandex.cloud.mdb.redis.v1.config import redis6_0_pb2 as yandex_dot_cloud_dot_mdb_dot_redis_dot_v1_dot_config_dot_redis6__0__pb2
from yandex.cloud.mdb.redis.v1.config import redis6_2_pb2 as yandex_dot_cloud_dot_mdb_dot_redis_dot_v1_dot_config_dot_redis6__2__pb2
from yandex.cloud.mdb.redis.v1.config import redis7_0_pb2 as yandex_dot_cloud_dot_mdb_dot_redis_dot_v1_dot_config_dot_redis7__0__pb2
from yandex.cloud.mdb.redis.v1 import maintenance_pb2 as yandex_dot_cloud_dot_mdb_dot_redis_dot_v1_dot_maintenance__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'yandex/cloud/mdb/redis/v1/cluster.proto\x12\x19yandex.cloud.mdb.redis.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1bgoogle/type/timeofday.proto\x1a\x1dyandex/cloud/validation.proto\x1a,yandex/cloud/mdb/redis/v1/config/redis.proto\x1a/yandex/cloud/mdb/redis/v1/config/redis5_0.proto\x1a/yandex/cloud/mdb/redis/v1/config/redis6_0.proto\x1a/yandex/cloud/mdb/redis/v1/config/redis6_2.proto\x1a/yandex/cloud/mdb/redis/v1/config/redis7_0.proto\x1a+yandex/cloud/mdb/redis/v1/maintenance.proto\"\xb8\t\n\x07\x43luster\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12>\n\x06labels\x18\x06 \x03(\x0b\x32..yandex.cloud.mdb.redis.v1.Cluster.LabelsEntry\x12\x43\n\x0b\x65nvironment\x18\x07 \x01(\x0e\x32..yandex.cloud.mdb.redis.v1.Cluster.Environment\x12\x39\n\nmonitoring\x18\x08 \x03(\x0b\x32%.yandex.cloud.mdb.redis.v1.Monitoring\x12\x38\n\x06\x63onfig\x18\t \x01(\x0b\x32(.yandex.cloud.mdb.redis.v1.ClusterConfig\x12\x12\n\nnetwork_id\x18\n \x01(\t\x12\x39\n\x06health\x18\x0b \x01(\x0e\x32).yandex.cloud.mdb.redis.v1.Cluster.Health\x12\x39\n\x06status\x18\x0c \x01(\x0e\x32).yandex.cloud.mdb.redis.v1.Cluster.Status\x12\x0f\n\x07sharded\x18\r \x01(\x08\x12H\n\x12maintenance_window\x18\x0e \x01(\x0b\x32,.yandex.cloud.mdb.redis.v1.MaintenanceWindow\x12J\n\x11planned_operation\x18\x0f \x01(\x0b\x32/.yandex.cloud.mdb.redis.v1.MaintenanceOperation\x12\x1a\n\x12security_group_ids\x18\x10 \x03(\t\x12\x13\n\x0btls_enabled\x18\x11 \x01(\x08\x12\x1b\n\x13\x64\x65letion_protection\x18\x12 \x01(\x08\x12L\n\x10persistence_mode\x18\x13 \x01(\x0e\x32\x32.yandex.cloud.mdb.redis.v1.Cluster.PersistenceMode\x12\x1a\n\x12\x61nnounce_hostnames\x18\x14 \x01(\x08\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"I\n\x0b\x45nvironment\x12\x1b\n\x17\x45NVIRONMENT_UNSPECIFIED\x10\x00\x12\x0e\n\nPRODUCTION\x10\x01\x12\r\n\tPRESTABLE\x10\x02\"?\n\x06Health\x12\x12\n\x0eHEALTH_UNKNOWN\x10\x00\x12\t\n\x05\x41LIVE\x10\x01\x12\x08\n\x04\x44\x45\x41\x44\x10\x02\x12\x0c\n\x08\x44\x45GRADED\x10\x03\"y\n\x06Status\x12\x12\n\x0eSTATUS_UNKNOWN\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x12\x0c\n\x08UPDATING\x10\x04\x12\x0c\n\x08STOPPING\x10\x05\x12\x0b\n\x07STOPPED\x10\x06\x12\x0c\n\x08STARTING\x10\x07\"\"\n\x0fPersistenceMode\x12\x06\n\x02ON\x10\x00\x12\x07\n\x03OFF\x10\x01\"=\n\nMonitoring\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0c\n\x04link\x18\x03 \x01(\t\"\xe9\x05\n\rClusterConfig\x12\x0f\n\x07version\x18\x01 \x01(\t\x12`\n\x10redis_config_5_0\x18\x02 \x01(\x0b\x32\x33.yandex.cloud.mdb.redis.v1.config.RedisConfigSet5_0H\x00R\x0fredisConfig_5_0\x12`\n\x10redis_config_6_0\x18\x06 \x01(\x0b\x32\x33.yandex.cloud.mdb.redis.v1.config.RedisConfigSet6_0H\x00R\x0fredisConfig_6_0\x12`\n\x10redis_config_6_2\x18\x07 \x01(\x0b\x32\x33.yandex.cloud.mdb.redis.v1.config.RedisConfigSet6_2H\x00R\x0fredisConfig_6_2\x12`\n\x10redis_config_7_0\x18\x08 \x01(\x0b\x32\x33.yandex.cloud.mdb.redis.v1.config.RedisConfigSet7_0H\x00R\x0fredisConfig_7_0\x12\x37\n\tresources\x18\x03 \x01(\x0b\x32$.yandex.cloud.mdb.redis.v1.Resources\x12\x33\n\x13\x62\x61\x63kup_window_start\x18\x04 \x01(\x0b\x32\x16.google.type.TimeOfDay\x12\x31\n\x06\x61\x63\x63\x65ss\x18\x05 \x01(\x0b\x32!.yandex.cloud.mdb.redis.v1.Access\x12?\n\x05redis\x18\t \x01(\x0b\x32\x30.yandex.cloud.mdb.redis.v1.config.RedisConfigSet\x12M\n\x15\x64isk_size_autoscaling\x18\n \x01(\x0b\x32..yandex.cloud.mdb.redis.v1.DiskSizeAutoscalingB\x0e\n\x0credis_config\")\n\x05Shard\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ncluster_id\x18\x02 \x01(\t\"\x80\x04\n\x04Host\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ncluster_id\x18\x02 \x01(\t\x12\x0f\n\x07zone_id\x18\x03 \x01(\t\x12\x11\n\tsubnet_id\x18\x04 \x01(\t\x12\x37\n\tresources\x18\x05 \x01(\x0b\x32$.yandex.cloud.mdb.redis.v1.Resources\x12\x32\n\x04role\x18\x06 \x01(\x0e\x32$.yandex.cloud.mdb.redis.v1.Host.Role\x12\x36\n\x06health\x18\x07 \x01(\x0e\x32&.yandex.cloud.mdb.redis.v1.Host.Health\x12\x34\n\x08services\x18\x08 \x03(\x0b\x32\".yandex.cloud.mdb.redis.v1.Service\x12\x12\n\nshard_name\x18\t \x01(\t\x12\x35\n\x10replica_priority\x18\n \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x18\n\x10\x61ssign_public_ip\x18\x0b \x01(\x08\"1\n\x04Role\x12\x10\n\x0cROLE_UNKNOWN\x10\x00\x12\n\n\x06MASTER\x10\x01\x12\x0b\n\x07REPLICA\x10\x02\"?\n\x06Health\x12\x12\n\x0eHEALTH_UNKNOWN\x10\x00\x12\t\n\x05\x41LIVE\x10\x01\x12\x08\n\x04\x44\x45\x41\x44\x10\x02\x12\x0c\n\x08\x44\x45GRADED\x10\x03\"\xf7\x01\n\x07Service\x12\x35\n\x04type\x18\x01 \x01(\x0e\x32\'.yandex.cloud.mdb.redis.v1.Service.Type\x12\x39\n\x06health\x18\x02 \x01(\x0e\x32).yandex.cloud.mdb.redis.v1.Service.Health\"G\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05REDIS\x10\x01\x12\x0b\n\x07\x41RBITER\x10\x02\x12\x11\n\rREDIS_CLUSTER\x10\x03\"1\n\x06Health\x12\x12\n\x0eHEALTH_UNKNOWN\x10\x00\x12\t\n\x05\x41LIVE\x10\x01\x12\x08\n\x04\x44\x45\x41\x44\x10\x02\"P\n\tResources\x12\x1a\n\x12resource_preset_id\x18\x01 \x01(\t\x12\x11\n\tdisk_size\x18\x02 \x01(\x03\x12\x14\n\x0c\x64isk_type_id\x18\x03 \x01(\t\"\x1b\n\x06\x41\x63\x63\x65ss\x12\x11\n\tdata_lens\x18\x01 \x01(\x08\"\xe7\x01\n\x13\x44iskSizeAutoscaling\x12K\n\x17planned_usage_threshold\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\r\xe8\xc7\x31\x00\xfa\xc7\x31\x05\x30-100\x12M\n\x19\x65mergency_usage_threshold\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\r\xe8\xc7\x31\x00\xfa\xc7\x31\x05\x30-100\x12\x34\n\x0f\x64isk_size_limit\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueBd\n\x1dyandex.cloud.api.mdb.redis.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/redis/v1;redisb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.redis.v1.cluster_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\035yandex.cloud.api.mdb.redis.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/redis/v1;redis'
  _CLUSTER_LABELSENTRY._options = None
  _CLUSTER_LABELSENTRY._serialized_options = b'8\001'
  _DISKSIZEAUTOSCALING.fields_by_name['planned_usage_threshold']._options = None
  _DISKSIZEAUTOSCALING.fields_by_name['planned_usage_threshold']._serialized_options = b'\350\3071\000\372\3071\0050-100'
  _DISKSIZEAUTOSCALING.fields_by_name['emergency_usage_threshold']._options = None
  _DISKSIZEAUTOSCALING.fields_by_name['emergency_usage_threshold']._serialized_options = b'\350\3071\000\372\3071\0050-100'
  _globals['_CLUSTER']._serialized_start=483
  _globals['_CLUSTER']._serialized_end=1691
  _globals['_CLUSTER_LABELSENTRY']._serialized_start=1347
  _globals['_CLUSTER_LABELSENTRY']._serialized_end=1392
  _globals['_CLUSTER_ENVIRONMENT']._serialized_start=1394
  _globals['_CLUSTER_ENVIRONMENT']._serialized_end=1467
  _globals['_CLUSTER_HEALTH']._serialized_start=1469
  _globals['_CLUSTER_HEALTH']._serialized_end=1532
  _globals['_CLUSTER_STATUS']._serialized_start=1534
  _globals['_CLUSTER_STATUS']._serialized_end=1655
  _globals['_CLUSTER_PERSISTENCEMODE']._serialized_start=1657
  _globals['_CLUSTER_PERSISTENCEMODE']._serialized_end=1691
  _globals['_MONITORING']._serialized_start=1693
  _globals['_MONITORING']._serialized_end=1754
  _globals['_CLUSTERCONFIG']._serialized_start=1757
  _globals['_CLUSTERCONFIG']._serialized_end=2502
  _globals['_SHARD']._serialized_start=2504
  _globals['_SHARD']._serialized_end=2545
  _globals['_HOST']._serialized_start=2548
  _globals['_HOST']._serialized_end=3060
  _globals['_HOST_ROLE']._serialized_start=2946
  _globals['_HOST_ROLE']._serialized_end=2995
  _globals['_HOST_HEALTH']._serialized_start=1469
  _globals['_HOST_HEALTH']._serialized_end=1532
  _globals['_SERVICE']._serialized_start=3063
  _globals['_SERVICE']._serialized_end=3310
  _globals['_SERVICE_TYPE']._serialized_start=3188
  _globals['_SERVICE_TYPE']._serialized_end=3259
  _globals['_SERVICE_HEALTH']._serialized_start=1469
  _globals['_SERVICE_HEALTH']._serialized_end=1518
  _globals['_RESOURCES']._serialized_start=3312
  _globals['_RESOURCES']._serialized_end=3392
  _globals['_ACCESS']._serialized_start=3394
  _globals['_ACCESS']._serialized_end=3421
  _globals['_DISKSIZEAUTOSCALING']._serialized_start=3424
  _globals['_DISKSIZEAUTOSCALING']._serialized_end=3655
# @@protoc_insertion_point(module_scope)
