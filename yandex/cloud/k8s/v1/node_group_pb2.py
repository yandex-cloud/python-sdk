# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/k8s/v1/node_group.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud.k8s.v1 import maintenance_pb2 as yandex_dot_cloud_dot_k8s_dot_v1_dot_maintenance__pb2
from yandex.cloud.k8s.v1 import node_pb2 as yandex_dot_cloud_dot_k8s_dot_v1_dot_node__pb2
from yandex.cloud.k8s.v1 import version_pb2 as yandex_dot_cloud_dot_k8s_dot_v1_dot_version__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$yandex/cloud/k8s/v1/node_group.proto\x12\x13yandex.cloud.k8s.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a%yandex/cloud/k8s/v1/maintenance.proto\x1a\x1eyandex/cloud/k8s/v1/node.proto\x1a!yandex/cloud/k8s/v1/version.proto\x1a\x1dyandex/cloud/validation.proto\"\xa0\x08\n\tNodeGroup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ncluster_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12:\n\x06labels\x18\x06 \x03(\x0b\x32*.yandex.cloud.k8s.v1.NodeGroup.LabelsEntry\x12\x35\n\x06status\x18\x07 \x01(\x0e\x32%.yandex.cloud.k8s.v1.NodeGroup.Status\x12\x38\n\rnode_template\x18\x08 \x01(\x0b\x32!.yandex.cloud.k8s.v1.NodeTemplate\x12\x36\n\x0cscale_policy\x18\t \x01(\x0b\x32 .yandex.cloud.k8s.v1.ScalePolicy\x12I\n\x11\x61llocation_policy\x18\n \x01(\x0b\x32..yandex.cloud.k8s.v1.NodeGroupAllocationPolicy\x12\x38\n\rdeploy_policy\x18\x12 \x01(\x0b\x32!.yandex.cloud.k8s.v1.DeployPolicy\x12\x19\n\x11instance_group_id\x18\x0b \x01(\t\x12\x14\n\x0cnode_version\x18\x0c \x01(\t\x12\x36\n\x0cversion_info\x18\r \x01(\x0b\x32 .yandex.cloud.k8s.v1.VersionInfo\x12K\n\x12maintenance_policy\x18\x0e \x01(\x0b\x32/.yandex.cloud.k8s.v1.NodeGroupMaintenancePolicy\x12\x1e\n\x16\x61llowed_unsafe_sysctls\x18\x0f \x03(\t\x12/\n\x0bnode_taints\x18\x10 \x03(\x0b\x32\x1a.yandex.cloud.k8s.v1.Taint\x12\x43\n\x0bnode_labels\x18\x11 \x03(\x0b\x32..yandex.cloud.k8s.v1.NodeGroup.NodeLabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x31\n\x0fNodeLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x87\x01\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x10\n\x0cPROVISIONING\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\x0f\n\x0bRECONCILING\x10\x03\x12\x0c\n\x08STOPPING\x10\x04\x12\x0b\n\x07STOPPED\x10\x05\x12\x0c\n\x08\x44\x45LETING\x10\x06\x12\x0c\n\x08STARTING\x10\x07\"\xb6\x02\n\x0bScalePolicy\x12\x42\n\x0b\x66ixed_scale\x18\x01 \x01(\x0b\x32+.yandex.cloud.k8s.v1.ScalePolicy.FixedScaleH\x00\x12@\n\nauto_scale\x18\x02 \x01(\x0b\x32*.yandex.cloud.k8s.v1.ScalePolicy.AutoScaleH\x00\x1a%\n\nFixedScale\x12\x17\n\x04size\x18\x01 \x01(\x03\x42\t\xfa\xc7\x31\x05\x30-100\x1a\x66\n\tAutoScale\x12\x1b\n\x08min_size\x18\x01 \x01(\x03\x42\t\xfa\xc7\x31\x05\x30-100\x12\x1b\n\x08max_size\x18\x02 \x01(\x03\x42\t\xfa\xc7\x31\x05\x30-100\x12\x1f\n\x0cinitial_size\x18\x03 \x01(\x03\x42\t\xfa\xc7\x31\x05\x30-100B\x12\n\nscale_type\x12\x04\xc0\xc1\x31\x01\"V\n\x19NodeGroupAllocationPolicy\x12\x39\n\tlocations\x18\x01 \x03(\x0b\x32&.yandex.cloud.k8s.v1.NodeGroupLocation\"=\n\x11NodeGroupLocation\x12\x15\n\x07zone_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x11\n\tsubnet_id\x18\x02 \x01(\t\"\x8b\x01\n\x1aNodeGroupMaintenancePolicy\x12\x14\n\x0c\x61uto_upgrade\x18\x01 \x01(\x08\x12\x13\n\x0b\x61uto_repair\x18\x02 \x01(\x08\x12\x42\n\x12maintenance_window\x18\x03 \x01(\x0b\x32&.yandex.cloud.k8s.v1.MaintenanceWindow\"T\n\x0c\x44\x65ployPolicy\x12\"\n\x0fmax_unavailable\x18\x01 \x01(\x03\x42\t\xfa\xc7\x31\x05\x30-100\x12 \n\rmax_expansion\x18\x02 \x01(\x03\x42\t\xfa\xc7\x31\x05\x30-100BV\n\x17yandex.cloud.api.k8s.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/k8s/v1;k8sb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.k8s.v1.node_group_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027yandex.cloud.api.k8s.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/k8s/v1;k8s'
  _NODEGROUP_LABELSENTRY._options = None
  _NODEGROUP_LABELSENTRY._serialized_options = b'8\001'
  _NODEGROUP_NODELABELSENTRY._options = None
  _NODEGROUP_NODELABELSENTRY._serialized_options = b'8\001'
  _SCALEPOLICY_FIXEDSCALE.fields_by_name['size']._options = None
  _SCALEPOLICY_FIXEDSCALE.fields_by_name['size']._serialized_options = b'\372\3071\0050-100'
  _SCALEPOLICY_AUTOSCALE.fields_by_name['min_size']._options = None
  _SCALEPOLICY_AUTOSCALE.fields_by_name['min_size']._serialized_options = b'\372\3071\0050-100'
  _SCALEPOLICY_AUTOSCALE.fields_by_name['max_size']._options = None
  _SCALEPOLICY_AUTOSCALE.fields_by_name['max_size']._serialized_options = b'\372\3071\0050-100'
  _SCALEPOLICY_AUTOSCALE.fields_by_name['initial_size']._options = None
  _SCALEPOLICY_AUTOSCALE.fields_by_name['initial_size']._serialized_options = b'\372\3071\0050-100'
  _SCALEPOLICY.oneofs_by_name['scale_type']._options = None
  _SCALEPOLICY.oneofs_by_name['scale_type']._serialized_options = b'\300\3011\001'
  _NODEGROUPLOCATION.fields_by_name['zone_id']._options = None
  _NODEGROUPLOCATION.fields_by_name['zone_id']._serialized_options = b'\350\3071\001'
  _DEPLOYPOLICY.fields_by_name['max_unavailable']._options = None
  _DEPLOYPOLICY.fields_by_name['max_unavailable']._serialized_options = b'\372\3071\0050-100'
  _DEPLOYPOLICY.fields_by_name['max_expansion']._options = None
  _DEPLOYPOLICY.fields_by_name['max_expansion']._serialized_options = b'\372\3071\0050-100'
  _globals['_NODEGROUP']._serialized_start=232
  _globals['_NODEGROUP']._serialized_end=1288
  _globals['_NODEGROUP_LABELSENTRY']._serialized_start=1054
  _globals['_NODEGROUP_LABELSENTRY']._serialized_end=1099
  _globals['_NODEGROUP_NODELABELSENTRY']._serialized_start=1101
  _globals['_NODEGROUP_NODELABELSENTRY']._serialized_end=1150
  _globals['_NODEGROUP_STATUS']._serialized_start=1153
  _globals['_NODEGROUP_STATUS']._serialized_end=1288
  _globals['_SCALEPOLICY']._serialized_start=1291
  _globals['_SCALEPOLICY']._serialized_end=1601
  _globals['_SCALEPOLICY_FIXEDSCALE']._serialized_start=1440
  _globals['_SCALEPOLICY_FIXEDSCALE']._serialized_end=1477
  _globals['_SCALEPOLICY_AUTOSCALE']._serialized_start=1479
  _globals['_SCALEPOLICY_AUTOSCALE']._serialized_end=1581
  _globals['_NODEGROUPALLOCATIONPOLICY']._serialized_start=1603
  _globals['_NODEGROUPALLOCATIONPOLICY']._serialized_end=1689
  _globals['_NODEGROUPLOCATION']._serialized_start=1691
  _globals['_NODEGROUPLOCATION']._serialized_end=1752
  _globals['_NODEGROUPMAINTENANCEPOLICY']._serialized_start=1755
  _globals['_NODEGROUPMAINTENANCEPOLICY']._serialized_end=1894
  _globals['_DEPLOYPOLICY']._serialized_start=1896
  _globals['_DEPLOYPOLICY']._serialized_end=1980
# @@protoc_insertion_point(module_scope)
