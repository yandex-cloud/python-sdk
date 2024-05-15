# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/opensearch/v1/cluster.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud.mdb.opensearch.v1 import maintenance_pb2 as yandex_dot_cloud_dot_mdb_dot_opensearch_dot_v1_dot_maintenance__pb2
from yandex.cloud.mdb.opensearch.v1.config import opensearch_pb2 as yandex_dot_cloud_dot_mdb_dot_opensearch_dot_v1_dot_config_dot_opensearch__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,yandex/cloud/mdb/opensearch/v1/cluster.proto\x12\x1eyandex.cloud.mdb.opensearch.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x30yandex/cloud/mdb/opensearch/v1/maintenance.proto\x1a\x36yandex/cloud/mdb/opensearch/v1/config/opensearch.proto\"\xc8\x08\n\x07\x43luster\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x43\n\x06labels\x18\x06 \x03(\x0b\x32\x33.yandex.cloud.mdb.opensearch.v1.Cluster.LabelsEntry\x12H\n\x0b\x65nvironment\x18\x07 \x01(\x0e\x32\x33.yandex.cloud.mdb.opensearch.v1.Cluster.Environment\x12>\n\nmonitoring\x18\x08 \x03(\x0b\x32*.yandex.cloud.mdb.opensearch.v1.Monitoring\x12=\n\x06\x63onfig\x18\t \x01(\x0b\x32-.yandex.cloud.mdb.opensearch.v1.ClusterConfig\x12\x12\n\nnetwork_id\x18\n \x01(\t\x12>\n\x06health\x18\x0b \x01(\x0e\x32..yandex.cloud.mdb.opensearch.v1.Cluster.Health\x12>\n\x06status\x18\x0c \x01(\x0e\x32..yandex.cloud.mdb.opensearch.v1.Cluster.Status\x12\x1a\n\x12security_group_ids\x18\r \x03(\t\x12\x1a\n\x12service_account_id\x18\x0e \x01(\t\x12\x1b\n\x13\x64\x65letion_protection\x18\x0f \x01(\x08\x12M\n\x12maintenance_window\x18\x10 \x01(\x0b\x32\x31.yandex.cloud.mdb.opensearch.v1.MaintenanceWindow\x12O\n\x11planned_operation\x18\x11 \x01(\x0b\x32\x34.yandex.cloud.mdb.opensearch.v1.MaintenanceOperation\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"I\n\x0b\x45nvironment\x12\x1b\n\x17\x45NVIRONMENT_UNSPECIFIED\x10\x00\x12\x0e\n\nPRODUCTION\x10\x01\x12\r\n\tPRESTABLE\x10\x02\"?\n\x06Health\x12\x12\n\x0eHEALTH_UNKNOWN\x10\x00\x12\t\n\x05\x41LIVE\x10\x01\x12\x08\n\x04\x44\x45\x41\x44\x10\x02\x12\x0c\n\x08\x44\x45GRADED\x10\x03\"y\n\x06Status\x12\x12\n\x0eSTATUS_UNKNOWN\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x12\x0c\n\x08UPDATING\x10\x04\x12\x0c\n\x08STOPPING\x10\x05\x12\x0b\n\x07STOPPED\x10\x06\x12\x0c\n\x08STARTING\x10\x07\"=\n\nMonitoring\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0c\n\x04link\x18\x03 \x01(\t\"\xd8\x01\n\rClusterConfig\x12\x0f\n\x07version\x18\x01 \x01(\t\x12>\n\nopensearch\x18\x02 \x01(\x0b\x32*.yandex.cloud.mdb.opensearch.v1.OpenSearch\x12>\n\ndashboards\x18\x03 \x01(\x0b\x32*.yandex.cloud.mdb.opensearch.v1.Dashboards\x12\x36\n\x06\x61\x63\x63\x65ss\x18\x04 \x01(\x0b\x32&.yandex.cloud.mdb.opensearch.v1.Access\"\x9d\x04\n\nOpenSearch\x12\x0f\n\x07plugins\x18\x01 \x03(\t\x12I\n\x0bnode_groups\x18\x02 \x03(\x0b\x32\x34.yandex.cloud.mdb.opensearch.v1.OpenSearch.NodeGroup\x12u\n\x17opensearch_config_set_2\x18\x03 \x01(\x0b\x32;.yandex.cloud.mdb.opensearch.v1.config.OpenSearchConfigSet2H\x00R\x15opensearchConfigSet_2\x1a\xf1\x01\n\tNodeGroup\x12\x0c\n\x04name\x18\x01 \x01(\t\x12<\n\tresources\x18\x02 \x01(\x0b\x32).yandex.cloud.mdb.opensearch.v1.Resources\x12\x13\n\x0bhosts_count\x18\x03 \x01(\x03\x12\x10\n\x08zone_ids\x18\x04 \x03(\t\x12\x12\n\nsubnet_ids\x18\x05 \x03(\t\x12\x18\n\x10\x61ssign_public_ip\x18\x06 \x01(\x08\x12\x43\n\x05roles\x18\x07 \x03(\x0e\x32\x34.yandex.cloud.mdb.opensearch.v1.OpenSearch.GroupRole\">\n\tGroupRole\x12\x1a\n\x16GROUP_ROLE_UNSPECIFIED\x10\x00\x12\x08\n\x04\x44\x41TA\x10\x01\x12\x0b\n\x07MANAGER\x10\x02\x42\x08\n\x06\x63onfig\"\x86\x02\n\nDashboards\x12I\n\x0bnode_groups\x18\x02 \x03(\x0b\x32\x34.yandex.cloud.mdb.opensearch.v1.Dashboards.NodeGroup\x1a\xac\x01\n\tNodeGroup\x12\x0c\n\x04name\x18\x01 \x01(\t\x12<\n\tresources\x18\x02 \x01(\x0b\x32).yandex.cloud.mdb.opensearch.v1.Resources\x12\x13\n\x0bhosts_count\x18\x03 \x01(\x03\x12\x10\n\x08zone_ids\x18\x04 \x03(\t\x12\x12\n\nsubnet_ids\x18\x05 \x03(\t\x12\x18\n\x10\x61ssign_public_ip\x18\x06 \x01(\x08\"P\n\tResources\x12\x1a\n\x12resource_preset_id\x18\x01 \x01(\t\x12\x11\n\tdisk_size\x18\x02 \x01(\x03\x12\x14\n\x0c\x64isk_type_id\x18\x03 \x01(\t\"\xac\x07\n\x04Host\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ncluster_id\x18\x02 \x01(\t\x12\x0f\n\x07zone_id\x18\x03 \x01(\t\x12<\n\tresources\x18\x04 \x01(\x0b\x32).yandex.cloud.mdb.opensearch.v1.Resources\x12\x37\n\x04type\x18\x05 \x01(\x0e\x32).yandex.cloud.mdb.opensearch.v1.Host.Type\x12;\n\x06health\x18\x06 \x01(\x0e\x32+.yandex.cloud.mdb.opensearch.v1.Host.Health\x12\x11\n\tsubnet_id\x18\x08 \x01(\t\x12\x18\n\x10\x61ssign_public_ip\x18\t \x01(\x08\x12\x42\n\x06system\x18\n \x01(\x0b\x32\x32.yandex.cloud.mdb.opensearch.v1.Host.SystemMetrics\x12\x12\n\nnode_group\x18\x0b \x01(\t\x12\x43\n\x05roles\x18\x0c \x03(\x0e\x32\x34.yandex.cloud.mdb.opensearch.v1.OpenSearch.GroupRole\x1a,\n\tCPUMetric\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12\x0c\n\x04used\x18\x02 \x01(\x01\x1a>\n\x0cMemoryMetric\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12\x0c\n\x04used\x18\x02 \x01(\x03\x12\r\n\x05total\x18\x03 \x01(\x03\x1a<\n\nDiskMetric\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12\x0c\n\x04used\x18\x02 \x01(\x03\x12\r\n\x05total\x18\x03 \x01(\x03\x1a\xce\x01\n\rSystemMetrics\x12;\n\x03\x63pu\x18\x01 \x01(\x0b\x32..yandex.cloud.mdb.opensearch.v1.Host.CPUMetric\x12\x41\n\x06memory\x18\x02 \x01(\x0b\x32\x31.yandex.cloud.mdb.opensearch.v1.Host.MemoryMetric\x12=\n\x04\x64isk\x18\x03 \x01(\x0b\x32/.yandex.cloud.mdb.opensearch.v1.Host.DiskMetric\"8\n\x06Health\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05\x41LIVE\x10\x01\x12\x08\n\x04\x44\x45\x41\x44\x10\x02\x12\x0c\n\x08\x44\x45GRADED\x10\x03\"<\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nOPENSEARCH\x10\x01\x12\x0e\n\nDASHBOARDS\x10\x02\"3\n\x06\x41\x63\x63\x65ss\x12\x15\n\rdata_transfer\x18\x01 \x01(\x08\x12\x12\n\nserverless\x18\x02 \x01(\x08\x42s\n\"yandex.cloud.api.mdb.opensearch.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/opensearch/v1;opensearchb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.opensearch.v1.cluster_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"yandex.cloud.api.mdb.opensearch.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/opensearch/v1;opensearch'
  _CLUSTER_LABELSENTRY._options = None
  _CLUSTER_LABELSENTRY._serialized_options = b'8\001'
  _globals['_CLUSTER']._serialized_start=220
  _globals['_CLUSTER']._serialized_end=1316
  _globals['_CLUSTER_LABELSENTRY']._serialized_start=1008
  _globals['_CLUSTER_LABELSENTRY']._serialized_end=1053
  _globals['_CLUSTER_ENVIRONMENT']._serialized_start=1055
  _globals['_CLUSTER_ENVIRONMENT']._serialized_end=1128
  _globals['_CLUSTER_HEALTH']._serialized_start=1130
  _globals['_CLUSTER_HEALTH']._serialized_end=1193
  _globals['_CLUSTER_STATUS']._serialized_start=1195
  _globals['_CLUSTER_STATUS']._serialized_end=1316
  _globals['_MONITORING']._serialized_start=1318
  _globals['_MONITORING']._serialized_end=1379
  _globals['_CLUSTERCONFIG']._serialized_start=1382
  _globals['_CLUSTERCONFIG']._serialized_end=1598
  _globals['_OPENSEARCH']._serialized_start=1601
  _globals['_OPENSEARCH']._serialized_end=2142
  _globals['_OPENSEARCH_NODEGROUP']._serialized_start=1827
  _globals['_OPENSEARCH_NODEGROUP']._serialized_end=2068
  _globals['_OPENSEARCH_GROUPROLE']._serialized_start=2070
  _globals['_OPENSEARCH_GROUPROLE']._serialized_end=2132
  _globals['_DASHBOARDS']._serialized_start=2145
  _globals['_DASHBOARDS']._serialized_end=2407
  _globals['_DASHBOARDS_NODEGROUP']._serialized_start=1827
  _globals['_DASHBOARDS_NODEGROUP']._serialized_end=1999
  _globals['_RESOURCES']._serialized_start=2409
  _globals['_RESOURCES']._serialized_end=2489
  _globals['_HOST']._serialized_start=2492
  _globals['_HOST']._serialized_end=3432
  _globals['_HOST_CPUMETRIC']._serialized_start=2933
  _globals['_HOST_CPUMETRIC']._serialized_end=2977
  _globals['_HOST_MEMORYMETRIC']._serialized_start=2979
  _globals['_HOST_MEMORYMETRIC']._serialized_end=3041
  _globals['_HOST_DISKMETRIC']._serialized_start=3043
  _globals['_HOST_DISKMETRIC']._serialized_end=3103
  _globals['_HOST_SYSTEMMETRICS']._serialized_start=3106
  _globals['_HOST_SYSTEMMETRICS']._serialized_end=3312
  _globals['_HOST_HEALTH']._serialized_start=3314
  _globals['_HOST_HEALTH']._serialized_end=3370
  _globals['_HOST_TYPE']._serialized_start=3372
  _globals['_HOST_TYPE']._serialized_end=3432
  _globals['_ACCESS']._serialized_start=3434
  _globals['_ACCESS']._serialized_end=3485
# @@protoc_insertion_point(module_scope)
