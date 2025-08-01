# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/dataproc/v1/cluster_service.proto
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
    'yandex/cloud/dataproc/v1/cluster_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.dataproc.v1 import cluster_pb2 as yandex_dot_cloud_dot_dataproc_dot_v1_dot_cluster__pb2
from yandex.cloud.dataproc.v1 import common_pb2 as yandex_dot_cloud_dot_dataproc_dot_v1_dot_common__pb2
from yandex.cloud.dataproc.v1 import subcluster_pb2 as yandex_dot_cloud_dot_dataproc_dot_v1_dot_subcluster__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.yandex/cloud/dataproc/v1/cluster_service.proto\x12\x18yandex.cloud.dataproc.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/dataproc/v1/cluster.proto\x1a%yandex/cloud/dataproc/v1/common.proto\x1a)yandex/cloud/dataproc/v1/subcluster.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"5\n\x11GetClusterRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\x90\x01\n\x13ListClustersRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"d\n\x14ListClustersResponse\x12\x33\n\x08\x63lusters\x18\x01 \x03(\x0b\x32!.yandex.cloud.dataproc.v1.Cluster\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xe1\x02\n\x1a\x43reateSubclusterConfigSpec\x12/\n\x04name\x18\x01 \x01(\tB!\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x32\n\x04role\x18\x02 \x01(\x0e\x32\x1e.yandex.cloud.dataproc.v1.RoleB\x04\xe8\xc7\x31\x01\x12<\n\tresources\x18\x03 \x01(\x0b\x32#.yandex.cloud.dataproc.v1.ResourcesB\x04\xe8\xc7\x31\x01\x12\x1f\n\tsubnet_id\x18\x04 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1c\n\x0bhosts_count\x18\x05 \x01(\x03\x42\x07\xfa\xc7\x31\x03>=1\x12\x18\n\x10\x61ssign_public_ip\x18\x06 \x01(\x08\x12G\n\x12\x61utoscaling_config\x18\x07 \x01(\x0b\x32+.yandex.cloud.dataproc.v1.AutoscalingConfig\"\xf8\x01\n\x1aUpdateSubclusterConfigSpec\x12\n\n\x02id\x18\x01 \x01(\t\x12/\n\x04name\x18\x02 \x01(\tB!\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x36\n\tresources\x18\x03 \x01(\x0b\x32#.yandex.cloud.dataproc.v1.Resources\x12\x1c\n\x0bhosts_count\x18\x04 \x01(\x03\x42\x07\xfa\xc7\x31\x03>=1\x12G\n\x12\x61utoscaling_config\x18\x05 \x01(\x0b\x32+.yandex.cloud.dataproc.v1.AutoscalingConfig\"\xb5\x01\n\x17\x43reateClusterConfigSpec\x12\x12\n\nversion_id\x18\x01 \x01(\t\x12\x36\n\x06hadoop\x18\x02 \x01(\x0b\x32&.yandex.cloud.dataproc.v1.HadoopConfig\x12N\n\x10subclusters_spec\x18\x03 \x03(\x0b\x32\x34.yandex.cloud.dataproc.v1.CreateSubclusterConfigSpec\"\xa1\x01\n\x17UpdateClusterConfigSpec\x12N\n\x10subclusters_spec\x18\x01 \x03(\x0b\x32\x34.yandex.cloud.dataproc.v1.UpdateSubclusterConfigSpec\x12\x36\n\x06hadoop\x18\x02 \x01(\x0b\x32&.yandex.cloud.dataproc.v1.HadoopConfig\"\xcb\x05\n\x14\x43reateClusterRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x04name\x18\x02 \x01(\tB!\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x87\x01\n\x06labels\x18\x04 \x03(\x0b\x32:.yandex.cloud.dataproc.v1.CreateClusterRequest.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04\x31-63\x12L\n\x0b\x63onfig_spec\x18\x06 \x01(\x0b\x32\x31.yandex.cloud.dataproc.v1.CreateClusterConfigSpecB\x04\xe8\xc7\x31\x01\x12\x1d\n\x07zone_id\x18\x07 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12 \n\x12service_account_id\x18\x08 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x0e\n\x06\x62ucket\x18\t \x01(\t\x12\x10\n\x08ui_proxy\x18\n \x01(\x08\x12\x1a\n\x12security_group_ids\x18\x0b \x03(\t\x12\x16\n\x0ehost_group_ids\x18\x0c \x03(\t\x12\x1b\n\x13\x64\x65letion_protection\x18\r \x01(\x08\x12\x14\n\x0clog_group_id\x18\x0e \x01(\t\x12\x42\n\x0b\x65nvironment\x18\x0f \x01(\x0e\x32-.yandex.cloud.dataproc.v1.Cluster.Environment\x12&\n\x1e\x61utoscaling_service_account_id\x18\x10 \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01J\x04\x08\x05\x10\x06\"+\n\x15\x43reateClusterMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\"\x97\x05\n\x14UpdateClusterRequest\x12\x1c\n\ncluster_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x87\x01\n\x06labels\x18\x04 \x03(\x0b\x32:.yandex.cloud.dataproc.v1.UpdateClusterRequest.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04\x31-63\x12\x46\n\x0b\x63onfig_spec\x18\x05 \x01(\x0b\x32\x31.yandex.cloud.dataproc.v1.UpdateClusterConfigSpec\x12/\n\x04name\x18\x06 \x01(\tB!\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x1a\n\x12service_account_id\x18\x07 \x01(\t\x12\x0e\n\x06\x62ucket\x18\x08 \x01(\t\x12)\n\x14\x64\x65\x63ommission_timeout\x18\t \x01(\x03\x42\x0b\xfa\xc7\x31\x07\x30-86400\x12\x10\n\x08ui_proxy\x18\n \x01(\x08\x12\x1a\n\x12security_group_ids\x18\x0b \x03(\t\x12\x1b\n\x13\x64\x65letion_protection\x18\x0c \x01(\x08\x12\x14\n\x0clog_group_id\x18\r \x01(\t\x12&\n\x1e\x61utoscaling_service_account_id\x18\x0e \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"+\n\x15UpdateClusterMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\"c\n\x14\x44\x65leteClusterRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12)\n\x14\x64\x65\x63ommission_timeout\x18\x02 \x01(\x03\x42\x0b\xfa\xc7\x31\x07\x30-86400\"+\n\x15\x44\x65leteClusterMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\"7\n\x13StartClusterRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"*\n\x14StartClusterMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\"a\n\x12StopClusterRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12)\n\x14\x64\x65\x63ommission_timeout\x18\x02 \x01(\x03\x42\x0b\xfa\xc7\x31\x07\x30-86400\")\n\x13StopClusterMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\"~\n\x1cListClusterOperationsRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"o\n\x1dListClusterOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x91\x01\n\x17ListClusterHostsRequest\x12\x1c\n\ncluster_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"b\n\x18ListClusterHostsResponse\x12-\n\x05hosts\x18\x01 \x03(\x0b\x32\x1e.yandex.cloud.dataproc.v1.Host\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"2\n\x12ListUILinksRequest\x12\x1c\n\ncluster_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\"#\n\x06UILink\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\"F\n\x13ListUILinksResponse\x12/\n\x05links\x18\x01 \x03(\x0b\x32 .yandex.cloud.dataproc.v1.UILink2\x91\r\n\x0e\x43lusterService\x12\x81\x01\n\x03Get\x12+.yandex.cloud.dataproc.v1.GetClusterRequest\x1a!.yandex.cloud.dataproc.v1.Cluster\"*\x82\xd3\xe4\x93\x02$\x12\"/dataproc/v1/clusters/{cluster_id}\x12\x84\x01\n\x04List\x12-.yandex.cloud.dataproc.v1.ListClustersRequest\x1a..yandex.cloud.dataproc.v1.ListClustersResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/dataproc/v1/clusters\x12\xa1\x01\n\x06\x43reate\x12..yandex.cloud.dataproc.v1.CreateClusterRequest\x1a!.yandex.cloud.operation.Operation\"D\xb2\xd2* \n\x15\x43reateClusterMetadata\x12\x07\x43luster\x82\xd3\xe4\x93\x02\x1a\"\x15/dataproc/v1/clusters:\x01*\x12\xae\x01\n\x06Update\x12..yandex.cloud.dataproc.v1.UpdateClusterRequest\x1a!.yandex.cloud.operation.Operation\"Q\xb2\xd2* \n\x15UpdateClusterMetadata\x12\x07\x43luster\x82\xd3\xe4\x93\x02\'2\"/dataproc/v1/clusters/{cluster_id}:\x01*\x12\xb9\x01\n\x06\x44\x65lete\x12..yandex.cloud.dataproc.v1.DeleteClusterRequest\x1a!.yandex.cloud.operation.Operation\"\\\xb2\xd2*.\n\x15\x44\x65leteClusterMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02$*\"/dataproc/v1/clusters/{cluster_id}\x12\xae\x01\n\x05Start\x12-.yandex.cloud.dataproc.v1.StartClusterRequest\x1a!.yandex.cloud.operation.Operation\"S\xb2\xd2*\x1f\n\x14StartClusterMetadata\x12\x07\x43luster\x82\xd3\xe4\x93\x02*\"(/dataproc/v1/clusters/{cluster_id}:start\x12\xad\x01\n\x04Stop\x12,.yandex.cloud.dataproc.v1.StopClusterRequest\x1a!.yandex.cloud.operation.Operation\"T\xb2\xd2*\x1e\n\x13StopClusterMetadata\x12\x07\x43luster\x82\xd3\xe4\x93\x02,\"\'/dataproc/v1/clusters/{cluster_id}:stop:\x01*\x12\xb8\x01\n\x0eListOperations\x12\x36.yandex.cloud.dataproc.v1.ListClusterOperationsRequest\x1a\x37.yandex.cloud.dataproc.v1.ListClusterOperationsResponse\"5\x82\xd3\xe4\x93\x02/\x12-/dataproc/v1/clusters/{cluster_id}/operations\x12\xa4\x01\n\tListHosts\x12\x31.yandex.cloud.dataproc.v1.ListClusterHostsRequest\x1a\x32.yandex.cloud.dataproc.v1.ListClusterHostsResponse\"0\x82\xd3\xe4\x93\x02*\x12(/dataproc/v1/clusters/{cluster_id}/hosts\x12\x9f\x01\n\x0bListUILinks\x12,.yandex.cloud.dataproc.v1.ListUILinksRequest\x1a-.yandex.cloud.dataproc.v1.ListUILinksResponse\"3\x82\xd3\xe4\x93\x02-\x12+/dataproc/v1/clusters/{cluster_id}/ui_linksBe\n\x1cyandex.cloud.api.dataproc.v1ZEgithub.com/yandex-cloud/go-genproto/yandex/cloud/dataproc/v1;dataprocb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.dataproc.v1.cluster_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034yandex.cloud.api.dataproc.v1ZEgithub.com/yandex-cloud/go-genproto/yandex/cloud/dataproc/v1;dataproc'
  _globals['_GETCLUSTERREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_GETCLUSTERREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTCLUSTERSREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_LISTCLUSTERSREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTCLUSTERSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTCLUSTERSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTCLUSTERSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTCLUSTERSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTCLUSTERSREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTCLUSTERSREQUEST'].fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _globals['_CREATESUBCLUSTERCONFIGSPEC'].fields_by_name['name']._loaded_options = None
  _globals['_CREATESUBCLUSTERCONFIGSPEC'].fields_by_name['name']._serialized_options = b'\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _globals['_CREATESUBCLUSTERCONFIGSPEC'].fields_by_name['role']._loaded_options = None
  _globals['_CREATESUBCLUSTERCONFIGSPEC'].fields_by_name['role']._serialized_options = b'\350\3071\001'
  _globals['_CREATESUBCLUSTERCONFIGSPEC'].fields_by_name['resources']._loaded_options = None
  _globals['_CREATESUBCLUSTERCONFIGSPEC'].fields_by_name['resources']._serialized_options = b'\350\3071\001'
  _globals['_CREATESUBCLUSTERCONFIGSPEC'].fields_by_name['subnet_id']._loaded_options = None
  _globals['_CREATESUBCLUSTERCONFIGSPEC'].fields_by_name['subnet_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_CREATESUBCLUSTERCONFIGSPEC'].fields_by_name['hosts_count']._loaded_options = None
  _globals['_CREATESUBCLUSTERCONFIGSPEC'].fields_by_name['hosts_count']._serialized_options = b'\372\3071\003>=1'
  _globals['_UPDATESUBCLUSTERCONFIGSPEC'].fields_by_name['name']._loaded_options = None
  _globals['_UPDATESUBCLUSTERCONFIGSPEC'].fields_by_name['name']._serialized_options = b'\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _globals['_UPDATESUBCLUSTERCONFIGSPEC'].fields_by_name['hosts_count']._loaded_options = None
  _globals['_UPDATESUBCLUSTERCONFIGSPEC'].fields_by_name['hosts_count']._serialized_options = b'\372\3071\003>=1'
  _globals['_CREATECLUSTERREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_CREATECLUSTERREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['name']._serialized_options = b'\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['description']._loaded_options = None
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['labels']._loaded_options = None
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\0041-63'
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['config_spec']._loaded_options = None
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['config_spec']._serialized_options = b'\350\3071\001'
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['zone_id']._loaded_options = None
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['zone_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['service_account_id']._loaded_options = None
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['service_account_id']._serialized_options = b'\350\3071\001'
  _globals['_UPDATECLUSTERREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_UPDATECLUSTERREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_UPDATECLUSTERREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_UPDATECLUSTERREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_UPDATECLUSTERREQUEST'].fields_by_name['description']._loaded_options = None
  _globals['_UPDATECLUSTERREQUEST'].fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _globals['_UPDATECLUSTERREQUEST'].fields_by_name['labels']._loaded_options = None
  _globals['_UPDATECLUSTERREQUEST'].fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\0041-63'
  _globals['_UPDATECLUSTERREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_UPDATECLUSTERREQUEST'].fields_by_name['name']._serialized_options = b'\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _globals['_UPDATECLUSTERREQUEST'].fields_by_name['decommission_timeout']._loaded_options = None
  _globals['_UPDATECLUSTERREQUEST'].fields_by_name['decommission_timeout']._serialized_options = b'\372\3071\0070-86400'
  _globals['_DELETECLUSTERREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_DELETECLUSTERREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_DELETECLUSTERREQUEST'].fields_by_name['decommission_timeout']._loaded_options = None
  _globals['_DELETECLUSTERREQUEST'].fields_by_name['decommission_timeout']._serialized_options = b'\372\3071\0070-86400'
  _globals['_STARTCLUSTERREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_STARTCLUSTERREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_STOPCLUSTERREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_STOPCLUSTERREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_STOPCLUSTERREQUEST'].fields_by_name['decommission_timeout']._loaded_options = None
  _globals['_STOPCLUSTERREQUEST'].fields_by_name['decommission_timeout']._serialized_options = b'\372\3071\0070-86400'
  _globals['_LISTCLUSTEROPERATIONSREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_LISTCLUSTEROPERATIONSREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTCLUSTEROPERATIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTCLUSTEROPERATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTCLUSTEROPERATIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTCLUSTEROPERATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTCLUSTERHOSTSREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_LISTCLUSTERHOSTSREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_LISTCLUSTERHOSTSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTCLUSTERHOSTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTCLUSTERHOSTSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTCLUSTERHOSTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTCLUSTERHOSTSREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTCLUSTERHOSTSREQUEST'].fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _globals['_LISTUILINKSREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_LISTUILINKSREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_CLUSTERSERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002$\022\"/dataproc/v1/clusters/{cluster_id}'
  _globals['_CLUSTERSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002\027\022\025/dataproc/v1/clusters'
  _globals['_CLUSTERSERVICE'].methods_by_name['Create']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['Create']._serialized_options = b'\262\322* \n\025CreateClusterMetadata\022\007Cluster\202\323\344\223\002\032\"\025/dataproc/v1/clusters:\001*'
  _globals['_CLUSTERSERVICE'].methods_by_name['Update']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['Update']._serialized_options = b'\262\322* \n\025UpdateClusterMetadata\022\007Cluster\202\323\344\223\002\'2\"/dataproc/v1/clusters/{cluster_id}:\001*'
  _globals['_CLUSTERSERVICE'].methods_by_name['Delete']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['Delete']._serialized_options = b'\262\322*.\n\025DeleteClusterMetadata\022\025google.protobuf.Empty\202\323\344\223\002$*\"/dataproc/v1/clusters/{cluster_id}'
  _globals['_CLUSTERSERVICE'].methods_by_name['Start']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['Start']._serialized_options = b'\262\322*\037\n\024StartClusterMetadata\022\007Cluster\202\323\344\223\002*\"(/dataproc/v1/clusters/{cluster_id}:start'
  _globals['_CLUSTERSERVICE'].methods_by_name['Stop']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['Stop']._serialized_options = b'\262\322*\036\n\023StopClusterMetadata\022\007Cluster\202\323\344\223\002,\"\'/dataproc/v1/clusters/{cluster_id}:stop:\001*'
  _globals['_CLUSTERSERVICE'].methods_by_name['ListOperations']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\002/\022-/dataproc/v1/clusters/{cluster_id}/operations'
  _globals['_CLUSTERSERVICE'].methods_by_name['ListHosts']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['ListHosts']._serialized_options = b'\202\323\344\223\002*\022(/dataproc/v1/clusters/{cluster_id}/hosts'
  _globals['_CLUSTERSERVICE'].methods_by_name['ListUILinks']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['ListUILinks']._serialized_options = b'\202\323\344\223\002-\022+/dataproc/v1/clusters/{cluster_id}/ui_links'
  _globals['_GETCLUSTERREQUEST']._serialized_start=367
  _globals['_GETCLUSTERREQUEST']._serialized_end=420
  _globals['_LISTCLUSTERSREQUEST']._serialized_start=423
  _globals['_LISTCLUSTERSREQUEST']._serialized_end=567
  _globals['_LISTCLUSTERSRESPONSE']._serialized_start=569
  _globals['_LISTCLUSTERSRESPONSE']._serialized_end=669
  _globals['_CREATESUBCLUSTERCONFIGSPEC']._serialized_start=672
  _globals['_CREATESUBCLUSTERCONFIGSPEC']._serialized_end=1025
  _globals['_UPDATESUBCLUSTERCONFIGSPEC']._serialized_start=1028
  _globals['_UPDATESUBCLUSTERCONFIGSPEC']._serialized_end=1276
  _globals['_CREATECLUSTERCONFIGSPEC']._serialized_start=1279
  _globals['_CREATECLUSTERCONFIGSPEC']._serialized_end=1460
  _globals['_UPDATECLUSTERCONFIGSPEC']._serialized_start=1463
  _globals['_UPDATECLUSTERCONFIGSPEC']._serialized_end=1624
  _globals['_CREATECLUSTERREQUEST']._serialized_start=1627
  _globals['_CREATECLUSTERREQUEST']._serialized_end=2342
  _globals['_CREATECLUSTERREQUEST_LABELSENTRY']._serialized_start=2291
  _globals['_CREATECLUSTERREQUEST_LABELSENTRY']._serialized_end=2336
  _globals['_CREATECLUSTERMETADATA']._serialized_start=2344
  _globals['_CREATECLUSTERMETADATA']._serialized_end=2387
  _globals['_UPDATECLUSTERREQUEST']._serialized_start=2390
  _globals['_UPDATECLUSTERREQUEST']._serialized_end=3053
  _globals['_UPDATECLUSTERREQUEST_LABELSENTRY']._serialized_start=2291
  _globals['_UPDATECLUSTERREQUEST_LABELSENTRY']._serialized_end=2336
  _globals['_UPDATECLUSTERMETADATA']._serialized_start=3055
  _globals['_UPDATECLUSTERMETADATA']._serialized_end=3098
  _globals['_DELETECLUSTERREQUEST']._serialized_start=3100
  _globals['_DELETECLUSTERREQUEST']._serialized_end=3199
  _globals['_DELETECLUSTERMETADATA']._serialized_start=3201
  _globals['_DELETECLUSTERMETADATA']._serialized_end=3244
  _globals['_STARTCLUSTERREQUEST']._serialized_start=3246
  _globals['_STARTCLUSTERREQUEST']._serialized_end=3301
  _globals['_STARTCLUSTERMETADATA']._serialized_start=3303
  _globals['_STARTCLUSTERMETADATA']._serialized_end=3345
  _globals['_STOPCLUSTERREQUEST']._serialized_start=3347
  _globals['_STOPCLUSTERREQUEST']._serialized_end=3444
  _globals['_STOPCLUSTERMETADATA']._serialized_start=3446
  _globals['_STOPCLUSTERMETADATA']._serialized_end=3487
  _globals['_LISTCLUSTEROPERATIONSREQUEST']._serialized_start=3489
  _globals['_LISTCLUSTEROPERATIONSREQUEST']._serialized_end=3615
  _globals['_LISTCLUSTEROPERATIONSRESPONSE']._serialized_start=3617
  _globals['_LISTCLUSTEROPERATIONSRESPONSE']._serialized_end=3728
  _globals['_LISTCLUSTERHOSTSREQUEST']._serialized_start=3731
  _globals['_LISTCLUSTERHOSTSREQUEST']._serialized_end=3876
  _globals['_LISTCLUSTERHOSTSRESPONSE']._serialized_start=3878
  _globals['_LISTCLUSTERHOSTSRESPONSE']._serialized_end=3976
  _globals['_LISTUILINKSREQUEST']._serialized_start=3978
  _globals['_LISTUILINKSREQUEST']._serialized_end=4028
  _globals['_UILINK']._serialized_start=4030
  _globals['_UILINK']._serialized_end=4065
  _globals['_LISTUILINKSRESPONSE']._serialized_start=4067
  _globals['_LISTUILINKSRESPONSE']._serialized_end=4137
  _globals['_CLUSTERSERVICE']._serialized_start=4140
  _globals['_CLUSTERSERVICE']._serialized_end=5821
# @@protoc_insertion_point(module_scope)
