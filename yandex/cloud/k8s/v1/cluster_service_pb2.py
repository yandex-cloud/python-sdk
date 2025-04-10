# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/k8s/v1/cluster_service.proto
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
    'yandex/cloud/k8s/v1/cluster_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.k8s.v1 import cluster_pb2 as yandex_dot_cloud_dot_k8s_dot_v1_dot_cluster__pb2
from yandex.cloud.k8s.v1 import node_pb2 as yandex_dot_cloud_dot_k8s_dot_v1_dot_node__pb2
from yandex.cloud.k8s.v1 import node_group_pb2 as yandex_dot_cloud_dot_k8s_dot_v1_dot_node__group__pb2
from yandex.cloud.k8s.v1 import version_pb2 as yandex_dot_cloud_dot_k8s_dot_v1_dot_version__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)yandex/cloud/k8s/v1/cluster_service.proto\x12\x13yandex.cloud.k8s.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/api/operation.proto\x1a!yandex/cloud/k8s/v1/cluster.proto\x1a\x1eyandex/cloud/k8s/v1/node.proto\x1a$yandex/cloud/k8s/v1/node_group.proto\x1a!yandex/cloud/k8s/v1/version.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"-\n\x11GetClusterRequest\x12\x18\n\ncluster_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"\x88\x01\n\x13ListClustersRequest\x12\x17\n\tfolder_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"_\n\x14ListClustersResponse\x12.\n\x08\x63lusters\x18\x01 \x03(\x0b\x32\x1c.yandex.cloud.k8s.v1.Cluster\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"0\n\x14\x44\x65leteClusterRequest\x12\x18\n\ncluster_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"+\n\x15\x44\x65leteClusterMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\".\n\x12StopClusterRequest\x12\x18\n\ncluster_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\")\n\x13StopClusterMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\"/\n\x13StartClusterRequest\x12\x18\n\ncluster_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"*\n\x14StartClusterMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\"\xab\x05\n\x14UpdateClusterRequest\x12\x18\n\ncluster_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x32\n\x04name\x18\x03 \x01(\tB$\xf2\xc7\x31 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x8a\x01\n\x06labels\x18\x05 \x03(\x0b\x32\x35.yandex.cloud.k8s.v1.UpdateClusterRequest.LabelsEntryBC\xf2\xc7\x31\x0f[-_./\\@0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x1c\x12\x14[a-z][-_./\\@0-9a-z]*\x1a\x04\x31-63\x12(\n\x14gateway_ipv4_address\x18\x06 \x01(\tB\x08\x8a\xc8\x31\x04<=15H\x00\x12:\n\x0bmaster_spec\x18\x07 \x01(\x0b\x32%.yandex.cloud.k8s.v1.MasterUpdateSpec\x12\x1a\n\x12service_account_id\x18\t \x01(\t\x12\x1f\n\x17node_service_account_id\x18\x08 \x01(\t\x12:\n\x0enetwork_policy\x18\n \x01(\x0b\x32\".yandex.cloud.k8s.v1.NetworkPolicy\x12\x45\n\x14ip_allocation_policy\x18\x0b \x01(\x0b\x32\'.yandex.cloud.k8s.v1.IPAllocationPolicy\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x12\n\x10internet_gateway\"\xb1\x03\n\x10MasterUpdateSpec\x12\x37\n\x07version\x18\x01 \x01(\x0b\x32&.yandex.cloud.k8s.v1.UpdateVersionSpec\x12H\n\x12maintenance_policy\x18\x02 \x01(\x0b\x32,.yandex.cloud.k8s.v1.MasterMaintenancePolicy\x12\x1a\n\x12security_group_ids\x18\x03 \x03(\t\x12:\n\x0emaster_logging\x18\x04 \x01(\x0b\x32\".yandex.cloud.k8s.v1.MasterLogging\x12\x34\n\tlocations\x18\x05 \x03(\x0b\x32!.yandex.cloud.k8s.v1.LocationSpec\x12J\n\x18\x65xternal_v6_address_spec\x18\x06 \x01(\x0b\x32(.yandex.cloud.k8s.v1.ExternalAddressSpec\x12@\n\x0cscale_policy\x18\x07 \x01(\x0b\x32*.yandex.cloud.k8s.v1.MasterScalePolicySpec\"+\n\x15UpdateClusterMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\"\xd4\x06\n\x14\x43reateClusterRequest\x12\x17\n\tfolder_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x32\n\x04name\x18\x02 \x01(\tB$\xf2\xc7\x31 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x8a\x01\n\x06labels\x18\x04 \x03(\x0b\x32\x35.yandex.cloud.k8s.v1.CreateClusterRequest.LabelsEntryBC\xf2\xc7\x31\x0f[-_./\\@0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x1c\x12\x14[a-z][-_./\\@0-9a-z]*\x1a\x04\x31-63\x12\x18\n\nnetwork_id\x18\x05 \x01(\tB\x04\xe8\xc7\x31\x01\x12:\n\x0bmaster_spec\x18\x06 \x01(\x0b\x32\x1f.yandex.cloud.k8s.v1.MasterSpecB\x04\xe8\xc7\x31\x01\x12\x45\n\x14ip_allocation_policy\x18\x07 \x01(\x0b\x32\'.yandex.cloud.k8s.v1.IPAllocationPolicy\x12\x1e\n\x14gateway_ipv4_address\x18\x08 \x01(\tH\x00\x12 \n\x12service_account_id\x18\t \x01(\tB\x04\xe8\xc7\x31\x01\x12%\n\x17node_service_account_id\x18\n \x01(\tB\x04\xe8\xc7\x31\x01\x12<\n\x0frelease_channel\x18\x0b \x01(\x0e\x32#.yandex.cloud.k8s.v1.ReleaseChannel\x12:\n\x0enetwork_policy\x18\x0c \x01(\x0b\x32\".yandex.cloud.k8s.v1.NetworkPolicy\x12\x36\n\x0ckms_provider\x18\r \x01(\x0b\x32 .yandex.cloud.k8s.v1.KMSProvider\x12-\n\x06\x63ilium\x18\x0e \x01(\x0b\x32\x1b.yandex.cloud.k8s.v1.CiliumH\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x12\n\x10internet_gatewayB\x18\n\x16network_implementation\"+\n\x15\x43reateClusterMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\"/\n\x19\x41utoUpgradeMasterMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\"\x92\x01\n\x1cListClusterOperationsRequest\x12\x18\n\ncluster_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"o\n\x1dListClusterOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x92\x01\n\x1cListClusterNodeGroupsRequest\x12\x18\n\ncluster_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"m\n\x1dListClusterNodeGroupsResponse\x12\x33\n\x0bnode_groups\x18\x01 \x03(\x0b\x32\x1e.yandex.cloud.k8s.v1.NodeGroup\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"q\n\x17ListClusterNodesRequest\x12\x18\n\ncluster_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"]\n\x18ListClusterNodesResponse\x12(\n\x05nodes\x18\x01 \x03(\x0b\x32\x19.yandex.cloud.k8s.v1.Node\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x96\x05\n\nMasterSpec\x12\x41\n\x11zonal_master_spec\x18\x01 \x01(\x0b\x32$.yandex.cloud.k8s.v1.ZonalMasterSpecH\x00\x12G\n\x14regional_master_spec\x18\x02 \x01(\x0b\x32\'.yandex.cloud.k8s.v1.RegionalMasterSpecH\x00\x12\x34\n\tlocations\x18\x08 \x03(\x0b\x32!.yandex.cloud.k8s.v1.LocationSpec\x12$\n\x11\x65tcd_cluster_size\x18\t \x01(\x03\x42\t\xfa\xc7\x31\x05\x30,1,3\x12J\n\x18\x65xternal_v4_address_spec\x18\n \x01(\x0b\x32(.yandex.cloud.k8s.v1.ExternalAddressSpec\x12J\n\x18\x65xternal_v6_address_spec\x18\x0b \x01(\x0b\x32(.yandex.cloud.k8s.v1.ExternalAddressSpec\x12\x0f\n\x07version\x18\x03 \x01(\t\x12H\n\x12maintenance_policy\x18\x04 \x01(\x0b\x32,.yandex.cloud.k8s.v1.MasterMaintenancePolicy\x12\x1a\n\x12security_group_ids\x18\x06 \x03(\t\x12:\n\x0emaster_logging\x18\x07 \x01(\x0b\x32\".yandex.cloud.k8s.v1.MasterLogging\x12@\n\x0cscale_policy\x18\x0c \x01(\x0b\x32*.yandex.cloud.k8s.v1.MasterScalePolicySpecB\r\n\x0bmaster_typeJ\x04\x08\x05\x10\x06\"\xc0\x01\n\x0fZonalMasterSpec\x12\x15\n\x07zone_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12J\n\x18internal_v4_address_spec\x18\x02 \x01(\x0b\x32(.yandex.cloud.k8s.v1.InternalAddressSpec\x12J\n\x18\x65xternal_v4_address_spec\x18\x03 \x01(\x0b\x32(.yandex.cloud.k8s.v1.ExternalAddressSpec\"\xfd\x01\n\x12RegionalMasterSpec\x12\x17\n\tregion_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x36\n\tlocations\x18\x02 \x03(\x0b\x32#.yandex.cloud.k8s.v1.MasterLocation\x12J\n\x18\x65xternal_v4_address_spec\x18\x03 \x01(\x0b\x32(.yandex.cloud.k8s.v1.ExternalAddressSpec\x12J\n\x18\x65xternal_v6_address_spec\x18\x04 \x01(\x0b\x32(.yandex.cloud.k8s.v1.ExternalAddressSpec\"(\n\x13InternalAddressSpec\x12\x11\n\tsubnet_id\x18\x02 \x01(\t\"&\n\x13\x45xternalAddressSpec\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"s\n\x0eMasterLocation\x12\x15\n\x07zone_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12J\n\x18internal_v4_address_spec\x18\x02 \x01(\x0b\x32(.yandex.cloud.k8s.v1.InternalAddressSpec\"8\n\x0cLocationSpec\x12\x15\n\x07zone_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x11\n\tsubnet_id\x18\x02 \x01(\t\"q\n\x1cRescheduleMaintenanceRequest\x12\x18\n\ncluster_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x37\n\rdelayed_until\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe8\xc7\x31\x01\"3\n\x1dRescheduleMaintenanceMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\"\xa8\x02\n\x15MasterScalePolicySpec\x12L\n\x0b\x66ixed_scale\x18\x01 \x01(\x0b\x32\x35.yandex.cloud.k8s.v1.MasterScalePolicySpec.FixedScaleH\x00\x12J\n\nauto_scale\x18\x02 \x01(\x0b\x32\x34.yandex.cloud.k8s.v1.MasterScalePolicySpec.AutoScaleH\x00\x1a.\n\nFixedScale\x12 \n\x12resource_preset_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x1a\x31\n\tAutoScale\x12$\n\x16min_resource_preset_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x42\x12\n\nscale_type\x12\x04\xc0\xc1\x31\x01\x32\xc1\x0f\n\x0e\x43lusterService\x12\x81\x01\n\x03Get\x12&.yandex.cloud.k8s.v1.GetClusterRequest\x1a\x1c.yandex.cloud.k8s.v1.Cluster\"4\x82\xd3\xe4\x93\x02.\x12,/managed-kubernetes/v1/clusters/{cluster_id}\x12\x84\x01\n\x04List\x12(.yandex.cloud.k8s.v1.ListClustersRequest\x1a).yandex.cloud.k8s.v1.ListClustersResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/managed-kubernetes/v1/clusters\x12\xa6\x01\n\x06\x43reate\x12).yandex.cloud.k8s.v1.CreateClusterRequest\x1a!.yandex.cloud.operation.Operation\"N\xb2\xd2* \n\x15\x43reateClusterMetadata\x12\x07\x43luster\x82\xd3\xe4\x93\x02$\"\x1f/managed-kubernetes/v1/clusters:\x01*\x12\xb3\x01\n\x06Update\x12).yandex.cloud.k8s.v1.UpdateClusterRequest\x1a!.yandex.cloud.operation.Operation\"[\xb2\xd2* \n\x15UpdateClusterMetadata\x12\x07\x43luster\x82\xd3\xe4\x93\x02\x31\x32,/managed-kubernetes/v1/clusters/{cluster_id}:\x01*\x12\xbe\x01\n\x06\x44\x65lete\x12).yandex.cloud.k8s.v1.DeleteClusterRequest\x1a!.yandex.cloud.operation.Operation\"f\xb2\xd2*.\n\x15\x44\x65leteClusterMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02.*,/managed-kubernetes/v1/clusters/{cluster_id}\x12\xb2\x01\n\x04Stop\x12\'.yandex.cloud.k8s.v1.StopClusterRequest\x1a!.yandex.cloud.operation.Operation\"^\xb2\xd2*\x1e\n\x13StopClusterMetadata\x12\x07\x43luster\x82\xd3\xe4\x93\x02\x36\"1/managed-kubernetes/v1/clusters/{cluster_id}:stop:\x01*\x12\xb6\x01\n\x05Start\x12(.yandex.cloud.k8s.v1.StartClusterRequest\x1a!.yandex.cloud.operation.Operation\"`\xb2\xd2*\x1f\n\x14StartClusterMetadata\x12\x07\x43luster\x82\xd3\xe4\x93\x02\x37\"2/managed-kubernetes/v1/clusters/{cluster_id}:start:\x01*\x12\xf8\x01\n\x15RescheduleMaintenance\x12\x31.yandex.cloud.k8s.v1.RescheduleMaintenanceRequest\x1a!.yandex.cloud.operation.Operation\"\x88\x01\xb2\xd2*6\n\x1dRescheduleMaintenanceMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02H\"C/managed-kubernetes/v1/clusters/{cluster_id}:reschedule-maintenance:\x01*\x12\xb8\x01\n\x0eListNodeGroups\x12\x31.yandex.cloud.k8s.v1.ListClusterNodeGroupsRequest\x1a\x32.yandex.cloud.k8s.v1.ListClusterNodeGroupsResponse\"?\x82\xd3\xe4\x93\x02\x39\x12\x37/managed-kubernetes/v1/clusters/{cluster_id}/nodeGroups\x12\xb8\x01\n\x0eListOperations\x12\x31.yandex.cloud.k8s.v1.ListClusterOperationsRequest\x1a\x32.yandex.cloud.k8s.v1.ListClusterOperationsResponse\"?\x82\xd3\xe4\x93\x02\x39\x12\x37/managed-kubernetes/v1/clusters/{cluster_id}/operations\x12\xa4\x01\n\tListNodes\x12,.yandex.cloud.k8s.v1.ListClusterNodesRequest\x1a-.yandex.cloud.k8s.v1.ListClusterNodesResponse\":\x82\xd3\xe4\x93\x02\x34\x12\x32/managed-kubernetes/v1/clusters/{cluster_id}/nodesBV\n\x17yandex.cloud.api.k8s.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/k8s/v1;k8sb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.k8s.v1.cluster_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027yandex.cloud.api.k8s.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/k8s/v1;k8s'
  _globals['_GETCLUSTERREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_GETCLUSTERREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001'
  _globals['_LISTCLUSTERSREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_LISTCLUSTERSREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001'
  _globals['_LISTCLUSTERSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTCLUSTERSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _globals['_LISTCLUSTERSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTCLUSTERSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTCLUSTERSREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTCLUSTERSREQUEST'].fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _globals['_DELETECLUSTERREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_DELETECLUSTERREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001'
  _globals['_STOPCLUSTERREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_STOPCLUSTERREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001'
  _globals['_STARTCLUSTERREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_STARTCLUSTERREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001'
  _globals['_UPDATECLUSTERREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_UPDATECLUSTERREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_UPDATECLUSTERREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_UPDATECLUSTERREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001'
  _globals['_UPDATECLUSTERREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_UPDATECLUSTERREQUEST'].fields_by_name['name']._serialized_options = b'\362\3071 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?'
  _globals['_UPDATECLUSTERREQUEST'].fields_by_name['description']._loaded_options = None
  _globals['_UPDATECLUSTERREQUEST'].fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _globals['_UPDATECLUSTERREQUEST'].fields_by_name['labels']._loaded_options = None
  _globals['_UPDATECLUSTERREQUEST'].fields_by_name['labels']._serialized_options = b'\362\3071\017[-_./\\@0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\034\022\024[a-z][-_./\\@0-9a-z]*\032\0041-63'
  _globals['_UPDATECLUSTERREQUEST'].fields_by_name['gateway_ipv4_address']._loaded_options = None
  _globals['_UPDATECLUSTERREQUEST'].fields_by_name['gateway_ipv4_address']._serialized_options = b'\212\3101\004<=15'
  _globals['_CREATECLUSTERREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_CREATECLUSTERREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001'
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['name']._serialized_options = b'\362\3071 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?'
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['description']._loaded_options = None
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['labels']._loaded_options = None
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['labels']._serialized_options = b'\362\3071\017[-_./\\@0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\034\022\024[a-z][-_./\\@0-9a-z]*\032\0041-63'
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['network_id']._loaded_options = None
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['network_id']._serialized_options = b'\350\3071\001'
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['master_spec']._loaded_options = None
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['master_spec']._serialized_options = b'\350\3071\001'
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['service_account_id']._loaded_options = None
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['service_account_id']._serialized_options = b'\350\3071\001'
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['node_service_account_id']._loaded_options = None
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['node_service_account_id']._serialized_options = b'\350\3071\001'
  _globals['_LISTCLUSTEROPERATIONSREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_LISTCLUSTEROPERATIONSREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001'
  _globals['_LISTCLUSTEROPERATIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTCLUSTEROPERATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _globals['_LISTCLUSTEROPERATIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTCLUSTEROPERATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTCLUSTEROPERATIONSREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTCLUSTEROPERATIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _globals['_LISTCLUSTERNODEGROUPSREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_LISTCLUSTERNODEGROUPSREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001'
  _globals['_LISTCLUSTERNODEGROUPSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTCLUSTERNODEGROUPSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _globals['_LISTCLUSTERNODEGROUPSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTCLUSTERNODEGROUPSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTCLUSTERNODEGROUPSREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTCLUSTERNODEGROUPSREQUEST'].fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _globals['_LISTCLUSTERNODESREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_LISTCLUSTERNODESREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001'
  _globals['_LISTCLUSTERNODESREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTCLUSTERNODESREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _globals['_LISTCLUSTERNODESREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTCLUSTERNODESREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_MASTERSPEC'].fields_by_name['etcd_cluster_size']._loaded_options = None
  _globals['_MASTERSPEC'].fields_by_name['etcd_cluster_size']._serialized_options = b'\372\3071\0050,1,3'
  _globals['_ZONALMASTERSPEC'].fields_by_name['zone_id']._loaded_options = None
  _globals['_ZONALMASTERSPEC'].fields_by_name['zone_id']._serialized_options = b'\350\3071\001'
  _globals['_REGIONALMASTERSPEC'].fields_by_name['region_id']._loaded_options = None
  _globals['_REGIONALMASTERSPEC'].fields_by_name['region_id']._serialized_options = b'\350\3071\001'
  _globals['_MASTERLOCATION'].fields_by_name['zone_id']._loaded_options = None
  _globals['_MASTERLOCATION'].fields_by_name['zone_id']._serialized_options = b'\350\3071\001'
  _globals['_LOCATIONSPEC'].fields_by_name['zone_id']._loaded_options = None
  _globals['_LOCATIONSPEC'].fields_by_name['zone_id']._serialized_options = b'\350\3071\001'
  _globals['_RESCHEDULEMAINTENANCEREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_RESCHEDULEMAINTENANCEREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001'
  _globals['_RESCHEDULEMAINTENANCEREQUEST'].fields_by_name['delayed_until']._loaded_options = None
  _globals['_RESCHEDULEMAINTENANCEREQUEST'].fields_by_name['delayed_until']._serialized_options = b'\350\3071\001'
  _globals['_MASTERSCALEPOLICYSPEC_FIXEDSCALE'].fields_by_name['resource_preset_id']._loaded_options = None
  _globals['_MASTERSCALEPOLICYSPEC_FIXEDSCALE'].fields_by_name['resource_preset_id']._serialized_options = b'\350\3071\001'
  _globals['_MASTERSCALEPOLICYSPEC_AUTOSCALE'].fields_by_name['min_resource_preset_id']._loaded_options = None
  _globals['_MASTERSCALEPOLICYSPEC_AUTOSCALE'].fields_by_name['min_resource_preset_id']._serialized_options = b'\350\3071\001'
  _globals['_MASTERSCALEPOLICYSPEC'].oneofs_by_name['scale_type']._loaded_options = None
  _globals['_MASTERSCALEPOLICYSPEC'].oneofs_by_name['scale_type']._serialized_options = b'\300\3011\001'
  _globals['_CLUSTERSERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002.\022,/managed-kubernetes/v1/clusters/{cluster_id}'
  _globals['_CLUSTERSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002!\022\037/managed-kubernetes/v1/clusters'
  _globals['_CLUSTERSERVICE'].methods_by_name['Create']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['Create']._serialized_options = b'\262\322* \n\025CreateClusterMetadata\022\007Cluster\202\323\344\223\002$\"\037/managed-kubernetes/v1/clusters:\001*'
  _globals['_CLUSTERSERVICE'].methods_by_name['Update']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['Update']._serialized_options = b'\262\322* \n\025UpdateClusterMetadata\022\007Cluster\202\323\344\223\00212,/managed-kubernetes/v1/clusters/{cluster_id}:\001*'
  _globals['_CLUSTERSERVICE'].methods_by_name['Delete']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['Delete']._serialized_options = b'\262\322*.\n\025DeleteClusterMetadata\022\025google.protobuf.Empty\202\323\344\223\002.*,/managed-kubernetes/v1/clusters/{cluster_id}'
  _globals['_CLUSTERSERVICE'].methods_by_name['Stop']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['Stop']._serialized_options = b'\262\322*\036\n\023StopClusterMetadata\022\007Cluster\202\323\344\223\0026\"1/managed-kubernetes/v1/clusters/{cluster_id}:stop:\001*'
  _globals['_CLUSTERSERVICE'].methods_by_name['Start']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['Start']._serialized_options = b'\262\322*\037\n\024StartClusterMetadata\022\007Cluster\202\323\344\223\0027\"2/managed-kubernetes/v1/clusters/{cluster_id}:start:\001*'
  _globals['_CLUSTERSERVICE'].methods_by_name['RescheduleMaintenance']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['RescheduleMaintenance']._serialized_options = b'\262\322*6\n\035RescheduleMaintenanceMetadata\022\025google.protobuf.Empty\202\323\344\223\002H\"C/managed-kubernetes/v1/clusters/{cluster_id}:reschedule-maintenance:\001*'
  _globals['_CLUSTERSERVICE'].methods_by_name['ListNodeGroups']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['ListNodeGroups']._serialized_options = b'\202\323\344\223\0029\0227/managed-kubernetes/v1/clusters/{cluster_id}/nodeGroups'
  _globals['_CLUSTERSERVICE'].methods_by_name['ListOperations']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\0029\0227/managed-kubernetes/v1/clusters/{cluster_id}/operations'
  _globals['_CLUSTERSERVICE'].methods_by_name['ListNodes']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['ListNodes']._serialized_options = b'\202\323\344\223\0024\0222/managed-kubernetes/v1/clusters/{cluster_id}/nodes'
  _globals['_GETCLUSTERREQUEST']._serialized_start=408
  _globals['_GETCLUSTERREQUEST']._serialized_end=453
  _globals['_LISTCLUSTERSREQUEST']._serialized_start=456
  _globals['_LISTCLUSTERSREQUEST']._serialized_end=592
  _globals['_LISTCLUSTERSRESPONSE']._serialized_start=594
  _globals['_LISTCLUSTERSRESPONSE']._serialized_end=689
  _globals['_DELETECLUSTERREQUEST']._serialized_start=691
  _globals['_DELETECLUSTERREQUEST']._serialized_end=739
  _globals['_DELETECLUSTERMETADATA']._serialized_start=741
  _globals['_DELETECLUSTERMETADATA']._serialized_end=784
  _globals['_STOPCLUSTERREQUEST']._serialized_start=786
  _globals['_STOPCLUSTERREQUEST']._serialized_end=832
  _globals['_STOPCLUSTERMETADATA']._serialized_start=834
  _globals['_STOPCLUSTERMETADATA']._serialized_end=875
  _globals['_STARTCLUSTERREQUEST']._serialized_start=877
  _globals['_STARTCLUSTERREQUEST']._serialized_end=924
  _globals['_STARTCLUSTERMETADATA']._serialized_start=926
  _globals['_STARTCLUSTERMETADATA']._serialized_end=968
  _globals['_UPDATECLUSTERREQUEST']._serialized_start=971
  _globals['_UPDATECLUSTERREQUEST']._serialized_end=1654
  _globals['_UPDATECLUSTERREQUEST_LABELSENTRY']._serialized_start=1589
  _globals['_UPDATECLUSTERREQUEST_LABELSENTRY']._serialized_end=1634
  _globals['_MASTERUPDATESPEC']._serialized_start=1657
  _globals['_MASTERUPDATESPEC']._serialized_end=2090
  _globals['_UPDATECLUSTERMETADATA']._serialized_start=2092
  _globals['_UPDATECLUSTERMETADATA']._serialized_end=2135
  _globals['_CREATECLUSTERREQUEST']._serialized_start=2138
  _globals['_CREATECLUSTERREQUEST']._serialized_end=2990
  _globals['_CREATECLUSTERREQUEST_LABELSENTRY']._serialized_start=1589
  _globals['_CREATECLUSTERREQUEST_LABELSENTRY']._serialized_end=1634
  _globals['_CREATECLUSTERMETADATA']._serialized_start=2992
  _globals['_CREATECLUSTERMETADATA']._serialized_end=3035
  _globals['_AUTOUPGRADEMASTERMETADATA']._serialized_start=3037
  _globals['_AUTOUPGRADEMASTERMETADATA']._serialized_end=3084
  _globals['_LISTCLUSTEROPERATIONSREQUEST']._serialized_start=3087
  _globals['_LISTCLUSTEROPERATIONSREQUEST']._serialized_end=3233
  _globals['_LISTCLUSTEROPERATIONSRESPONSE']._serialized_start=3235
  _globals['_LISTCLUSTEROPERATIONSRESPONSE']._serialized_end=3346
  _globals['_LISTCLUSTERNODEGROUPSREQUEST']._serialized_start=3349
  _globals['_LISTCLUSTERNODEGROUPSREQUEST']._serialized_end=3495
  _globals['_LISTCLUSTERNODEGROUPSRESPONSE']._serialized_start=3497
  _globals['_LISTCLUSTERNODEGROUPSRESPONSE']._serialized_end=3606
  _globals['_LISTCLUSTERNODESREQUEST']._serialized_start=3608
  _globals['_LISTCLUSTERNODESREQUEST']._serialized_end=3721
  _globals['_LISTCLUSTERNODESRESPONSE']._serialized_start=3723
  _globals['_LISTCLUSTERNODESRESPONSE']._serialized_end=3816
  _globals['_MASTERSPEC']._serialized_start=3819
  _globals['_MASTERSPEC']._serialized_end=4481
  _globals['_ZONALMASTERSPEC']._serialized_start=4484
  _globals['_ZONALMASTERSPEC']._serialized_end=4676
  _globals['_REGIONALMASTERSPEC']._serialized_start=4679
  _globals['_REGIONALMASTERSPEC']._serialized_end=4932
  _globals['_INTERNALADDRESSSPEC']._serialized_start=4934
  _globals['_INTERNALADDRESSSPEC']._serialized_end=4974
  _globals['_EXTERNALADDRESSSPEC']._serialized_start=4976
  _globals['_EXTERNALADDRESSSPEC']._serialized_end=5014
  _globals['_MASTERLOCATION']._serialized_start=5016
  _globals['_MASTERLOCATION']._serialized_end=5131
  _globals['_LOCATIONSPEC']._serialized_start=5133
  _globals['_LOCATIONSPEC']._serialized_end=5189
  _globals['_RESCHEDULEMAINTENANCEREQUEST']._serialized_start=5191
  _globals['_RESCHEDULEMAINTENANCEREQUEST']._serialized_end=5304
  _globals['_RESCHEDULEMAINTENANCEMETADATA']._serialized_start=5306
  _globals['_RESCHEDULEMAINTENANCEMETADATA']._serialized_end=5357
  _globals['_MASTERSCALEPOLICYSPEC']._serialized_start=5360
  _globals['_MASTERSCALEPOLICYSPEC']._serialized_end=5656
  _globals['_MASTERSCALEPOLICYSPEC_FIXEDSCALE']._serialized_start=5539
  _globals['_MASTERSCALEPOLICYSPEC_FIXEDSCALE']._serialized_end=5585
  _globals['_MASTERSCALEPOLICYSPEC_AUTOSCALE']._serialized_start=5587
  _globals['_MASTERSCALEPOLICYSPEC_AUTOSCALE']._serialized_end=5636
  _globals['_CLUSTERSERVICE']._serialized_start=5659
  _globals['_CLUSTERSERVICE']._serialized_end=7644
# @@protoc_insertion_point(module_scope)
