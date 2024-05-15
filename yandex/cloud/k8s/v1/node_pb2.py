# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/k8s/v1/node.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eyandex/cloud/k8s/v1/node.proto\x12\x13yandex.cloud.k8s.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dyandex/cloud/validation.proto\"\xe2\x05\n\x04Node\x12\x30\n\x06status\x18\x01 \x01(\x0e\x32 .yandex.cloud.k8s.v1.Node.Status\x12,\n\x04spec\x18\x02 \x01(\x0b\x32\x1e.yandex.cloud.k8s.v1.Node.Spec\x12;\n\x0c\x63loud_status\x18\x03 \x01(\x0b\x32%.yandex.cloud.k8s.v1.Node.CloudStatus\x12\x45\n\x11kubernetes_status\x18\x04 \x01(\x0b\x32*.yandex.cloud.k8s.v1.Node.KubernetesStatus\x1a\xbd\x01\n\x10KubernetesStatus\x12\n\n\x02id\x18\x01 \x01(\t\x12\x32\n\nconditions\x18\x02 \x03(\x0b\x32\x1e.yandex.cloud.k8s.v1.Condition\x12*\n\x06taints\x18\x03 \x03(\x0b\x32\x1a.yandex.cloud.k8s.v1.Taint\x12=\n\x10\x61ttached_volumes\x18\x04 \x03(\x0b\x32#.yandex.cloud.k8s.v1.AttachedVolume\x1a\x41\n\x0b\x43loudStatus\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\x16\n\x0estatus_message\x18\x03 \x01(\t\x1aj\n\x04Spec\x12\x35\n\tresources\x18\x01 \x01(\x0b\x32\".yandex.cloud.k8s.v1.ResourcesSpec\x12+\n\x04\x64isk\x18\x02 \x01(\x0b\x32\x1d.yandex.cloud.k8s.v1.DiskSpec\"\x86\x01\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x10\n\x0cPROVISIONING\x10\x01\x12\x11\n\rNOT_CONNECTED\x10\x02\x12\r\n\tNOT_READY\x10\x03\x12\t\n\x05READY\x10\x04\x12\x0b\n\x07MISSING\x10\x05\x12\x0b\n\x07STOPPED\x10\x06\x12\x0b\n\x07UNKNOWN\x10\x07\"\xad\x01\n\tCondition\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\x37\n\x13last_heartbeat_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x38\n\x14last_transition_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xb1\x01\n\x05Taint\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x31\n\x06\x65\x66\x66\x65\x63t\x18\x03 \x01(\x0e\x32!.yandex.cloud.k8s.v1.Taint.Effect\"Y\n\x06\x45\x66\x66\x65\x63t\x12\x16\n\x12\x45\x46\x46\x45\x43T_UNSPECIFIED\x10\x00\x12\x0f\n\x0bNO_SCHEDULE\x10\x01\x12\x16\n\x12PREFER_NO_SCHEDULE\x10\x02\x12\x0e\n\nNO_EXECUTE\x10\x03\"<\n\x0e\x41ttachedVolume\x12\x13\n\x0b\x64river_name\x18\x01 \x01(\t\x12\x15\n\rvolume_handle\x18\x02 \x01(\t\"\xcb\x0b\n\x0cNodeTemplate\x12\x17\n\x04name\x18\r \x01(\tB\t\x8a\xc8\x31\x05<=128\x12p\n\x06labels\x18\x0f \x03(\x0b\x32-.yandex.cloud.k8s.v1.NodeTemplate.LabelsEntryB1\x82\xc8\x31\x04<=32\x8a\xc8\x31\x05<=128\xb2\xc8\x31\x1c\x12\x14[a-z][-_./\\@0-9a-z]*\x1a\x04\x31-63\x12\x13\n\x0bplatform_id\x18\x01 \x01(\t\x12:\n\x0eresources_spec\x18\x02 \x01(\x0b\x32\".yandex.cloud.k8s.v1.ResourcesSpec\x12\x35\n\x0e\x62oot_disk_spec\x18\x03 \x01(\x0b\x32\x1d.yandex.cloud.k8s.v1.DiskSpec\x12s\n\x08metadata\x18\x04 \x03(\x0b\x32/.yandex.cloud.k8s.v1.NodeTemplate.MetadataEntryB0\x82\xc8\x31\x04<=64\x8a\xc8\x31\x08<=131072\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04\x31-63\x12\x41\n\x0fv4_address_spec\x18\x05 \x01(\x0b\x32$.yandex.cloud.k8s.v1.NodeAddressSpecB\x02\x18\x01\x12@\n\x11scheduling_policy\x18\x06 \x01(\x0b\x32%.yandex.cloud.k8s.v1.SchedulingPolicy\x12J\n\x17network_interface_specs\x18\x07 \x03(\x0b\x32).yandex.cloud.k8s.v1.NetworkInterfaceSpec\x12>\n\x10placement_policy\x18\n \x01(\x0b\x32$.yandex.cloud.k8s.v1.PlacementPolicy\x12K\n\x10network_settings\x18\x0b \x01(\x0b\x32\x31.yandex.cloud.k8s.v1.NodeTemplate.NetworkSettings\x12^\n\x1a\x63ontainer_runtime_settings\x18\x0c \x01(\x0b\x32:.yandex.cloud.k8s.v1.NodeTemplate.ContainerRuntimeSettings\x12^\n\x1a\x63ontainer_network_settings\x18\x10 \x01(\x0b\x32:.yandex.cloud.k8s.v1.NodeTemplate.ContainerNetworkSettings\x12\x36\n\x0cgpu_settings\x18\x12 \x01(\x0b\x32 .yandex.cloud.k8s.v1.GpuSettings\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\xa3\x01\n\x0fNetworkSettings\x12J\n\x04type\x18\x01 \x01(\x0e\x32\x36.yandex.cloud.k8s.v1.NodeTemplate.NetworkSettings.TypeB\x04\xe8\xc7\x31\x01\"D\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0c\n\x08STANDARD\x10\x01\x12\x18\n\x14SOFTWARE_ACCELERATED\x10\x02\x1a\xa9\x01\n\x18\x43ontainerRuntimeSettings\x12S\n\x04type\x18\x01 \x01(\x0e\x32?.yandex.cloud.k8s.v1.NodeTemplate.ContainerRuntimeSettings.TypeB\x04\xe8\xc7\x31\x01\"8\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06\x44OCKER\x10\x01\x12\x0e\n\nCONTAINERD\x10\x02\x1a+\n\x18\x43ontainerNetworkSettings\x12\x0f\n\x07pod_mtu\x18\x01 \x01(\x03\"\xc3\x01\n\x0bGpuSettings\x12\x16\n\x0egpu_cluster_id\x18\x01 \x01(\t\x12H\n\x0fgpu_environment\x18\x02 \x01(\x0e\x32/.yandex.cloud.k8s.v1.GpuSettings.GpuEnvironment\"R\n\x0eGpuEnvironment\x12\x1f\n\x1bGPU_ENVIRONMENT_UNSPECIFIED\x10\x00\x12\x15\n\x11RUNC_DRIVERS_CUDA\x10\x01\x12\x08\n\x04RUNC\x10\x02\"\xd4\x01\n\x14NetworkInterfaceSpec\x12\x12\n\nsubnet_ids\x18\x02 \x03(\t\x12\x45\n\x17primary_v4_address_spec\x18\x03 \x01(\x0b\x32$.yandex.cloud.k8s.v1.NodeAddressSpec\x12\x45\n\x17primary_v6_address_spec\x18\x04 \x01(\x0b\x32$.yandex.cloud.k8s.v1.NodeAddressSpec\x12\x1a\n\x12security_group_ids\x18\x05 \x03(\t\"\x92\x01\n\x0fNodeAddressSpec\x12\x41\n\x13one_to_one_nat_spec\x18\x01 \x01(\x0b\x32$.yandex.cloud.k8s.v1.OneToOneNatSpec\x12<\n\x10\x64ns_record_specs\x18\x02 \x03(\x0b\x32\".yandex.cloud.k8s.v1.DnsRecordSpec\"_\n\rDnsRecordSpec\x12\x12\n\x04\x66qdn\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x13\n\x0b\x64ns_zone_id\x18\x02 \x01(\t\x12\x18\n\x03ttl\x18\x03 \x01(\x03\x42\x0b\xfa\xc7\x31\x07\x30-86400\x12\x0b\n\x03ptr\x18\x04 \x01(\x08\"E\n\x0fOneToOneNatSpec\x12\x32\n\nip_version\x18\x01 \x01(\x0e\x32\x1e.yandex.cloud.k8s.v1.IpVersion\"y\n\rResourcesSpec\x12\x17\n\x06memory\x18\x01 \x01(\x03\x42\x07\xfa\xc7\x31\x03>=0\x12\x16\n\x05\x63ores\x18\x02 \x01(\x03\x42\x07\xfa\xc7\x31\x03>=0\x12 \n\rcore_fraction\x18\x03 \x01(\x03\x42\t\xfa\xc7\x31\x05\x30-100\x12\x15\n\x04gpus\x18\x04 \x01(\x03\x42\x07\xfa\xc7\x31\x03>=0\"\x92\x01\n\x08\x44iskSpec\x12^\n\x0c\x64isk_type_id\x18\x01 \x01(\tBH\xf2\xc7\x31\x44|network-ssd|network-hdd|network-ssd-nonreplicated|network-ssd-io-m3\x12&\n\tdisk_size\x18\x02 \x01(\x03\x42\x13\xfa\xc7\x31\x0f\x30-4398046511104\"\'\n\x10SchedulingPolicy\x12\x13\n\x0bpreemptible\x18\x01 \x01(\x08\"-\n\x0fPlacementPolicy\x12\x1a\n\x12placement_group_id\x18\x01 \x01(\t*;\n\tIpVersion\x12\x1a\n\x16IP_VERSION_UNSPECIFIED\x10\x00\x12\x08\n\x04IPV4\x10\x01\x12\x08\n\x04IPV6\x10\x02\x42V\n\x17yandex.cloud.api.k8s.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/k8s/v1;k8sb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.k8s.v1.node_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027yandex.cloud.api.k8s.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/k8s/v1;k8s'
  _globals['_NODETEMPLATE_LABELSENTRY']._loaded_options = None
  _globals['_NODETEMPLATE_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_NODETEMPLATE_METADATAENTRY']._loaded_options = None
  _globals['_NODETEMPLATE_METADATAENTRY']._serialized_options = b'8\001'
  _globals['_NODETEMPLATE_NETWORKSETTINGS'].fields_by_name['type']._loaded_options = None
  _globals['_NODETEMPLATE_NETWORKSETTINGS'].fields_by_name['type']._serialized_options = b'\350\3071\001'
  _globals['_NODETEMPLATE_CONTAINERRUNTIMESETTINGS'].fields_by_name['type']._loaded_options = None
  _globals['_NODETEMPLATE_CONTAINERRUNTIMESETTINGS'].fields_by_name['type']._serialized_options = b'\350\3071\001'
  _globals['_NODETEMPLATE'].fields_by_name['name']._loaded_options = None
  _globals['_NODETEMPLATE'].fields_by_name['name']._serialized_options = b'\212\3101\005<=128'
  _globals['_NODETEMPLATE'].fields_by_name['labels']._loaded_options = None
  _globals['_NODETEMPLATE'].fields_by_name['labels']._serialized_options = b'\202\3101\004<=32\212\3101\005<=128\262\3101\034\022\024[a-z][-_./\\@0-9a-z]*\032\0041-63'
  _globals['_NODETEMPLATE'].fields_by_name['metadata']._loaded_options = None
  _globals['_NODETEMPLATE'].fields_by_name['metadata']._serialized_options = b'\202\3101\004<=64\212\3101\010<=131072\262\3101\030\022\020[a-z][-_0-9a-z]*\032\0041-63'
  _globals['_NODETEMPLATE'].fields_by_name['v4_address_spec']._loaded_options = None
  _globals['_NODETEMPLATE'].fields_by_name['v4_address_spec']._serialized_options = b'\030\001'
  _globals['_DNSRECORDSPEC'].fields_by_name['fqdn']._loaded_options = None
  _globals['_DNSRECORDSPEC'].fields_by_name['fqdn']._serialized_options = b'\350\3071\001'
  _globals['_DNSRECORDSPEC'].fields_by_name['ttl']._loaded_options = None
  _globals['_DNSRECORDSPEC'].fields_by_name['ttl']._serialized_options = b'\372\3071\0070-86400'
  _globals['_RESOURCESSPEC'].fields_by_name['memory']._loaded_options = None
  _globals['_RESOURCESSPEC'].fields_by_name['memory']._serialized_options = b'\372\3071\003>=0'
  _globals['_RESOURCESSPEC'].fields_by_name['cores']._loaded_options = None
  _globals['_RESOURCESSPEC'].fields_by_name['cores']._serialized_options = b'\372\3071\003>=0'
  _globals['_RESOURCESSPEC'].fields_by_name['core_fraction']._loaded_options = None
  _globals['_RESOURCESSPEC'].fields_by_name['core_fraction']._serialized_options = b'\372\3071\0050-100'
  _globals['_RESOURCESSPEC'].fields_by_name['gpus']._loaded_options = None
  _globals['_RESOURCESSPEC'].fields_by_name['gpus']._serialized_options = b'\372\3071\003>=0'
  _globals['_DISKSPEC'].fields_by_name['disk_type_id']._loaded_options = None
  _globals['_DISKSPEC'].fields_by_name['disk_type_id']._serialized_options = b'\362\3071D|network-ssd|network-hdd|network-ssd-nonreplicated|network-ssd-io-m3'
  _globals['_DISKSPEC'].fields_by_name['disk_size']._loaded_options = None
  _globals['_DISKSPEC'].fields_by_name['disk_size']._serialized_options = b'\372\3071\0170-4398046511104'
  _globals['_IPVERSION']._serialized_start=3854
  _globals['_IPVERSION']._serialized_end=3913
  _globals['_NODE']._serialized_start=120
  _globals['_NODE']._serialized_end=858
  _globals['_NODE_KUBERNETESSTATUS']._serialized_start=357
  _globals['_NODE_KUBERNETESSTATUS']._serialized_end=546
  _globals['_NODE_CLOUDSTATUS']._serialized_start=548
  _globals['_NODE_CLOUDSTATUS']._serialized_end=613
  _globals['_NODE_SPEC']._serialized_start=615
  _globals['_NODE_SPEC']._serialized_end=721
  _globals['_NODE_STATUS']._serialized_start=724
  _globals['_NODE_STATUS']._serialized_end=858
  _globals['_CONDITION']._serialized_start=861
  _globals['_CONDITION']._serialized_end=1034
  _globals['_TAINT']._serialized_start=1037
  _globals['_TAINT']._serialized_end=1214
  _globals['_TAINT_EFFECT']._serialized_start=1125
  _globals['_TAINT_EFFECT']._serialized_end=1214
  _globals['_ATTACHEDVOLUME']._serialized_start=1216
  _globals['_ATTACHEDVOLUME']._serialized_end=1276
  _globals['_NODETEMPLATE']._serialized_start=1279
  _globals['_NODETEMPLATE']._serialized_end=2762
  _globals['_NODETEMPLATE_LABELSENTRY']._serialized_start=2285
  _globals['_NODETEMPLATE_LABELSENTRY']._serialized_end=2330
  _globals['_NODETEMPLATE_METADATAENTRY']._serialized_start=2332
  _globals['_NODETEMPLATE_METADATAENTRY']._serialized_end=2379
  _globals['_NODETEMPLATE_NETWORKSETTINGS']._serialized_start=2382
  _globals['_NODETEMPLATE_NETWORKSETTINGS']._serialized_end=2545
  _globals['_NODETEMPLATE_NETWORKSETTINGS_TYPE']._serialized_start=2477
  _globals['_NODETEMPLATE_NETWORKSETTINGS_TYPE']._serialized_end=2545
  _globals['_NODETEMPLATE_CONTAINERRUNTIMESETTINGS']._serialized_start=2548
  _globals['_NODETEMPLATE_CONTAINERRUNTIMESETTINGS']._serialized_end=2717
  _globals['_NODETEMPLATE_CONTAINERRUNTIMESETTINGS_TYPE']._serialized_start=2661
  _globals['_NODETEMPLATE_CONTAINERRUNTIMESETTINGS_TYPE']._serialized_end=2717
  _globals['_NODETEMPLATE_CONTAINERNETWORKSETTINGS']._serialized_start=2719
  _globals['_NODETEMPLATE_CONTAINERNETWORKSETTINGS']._serialized_end=2762
  _globals['_GPUSETTINGS']._serialized_start=2765
  _globals['_GPUSETTINGS']._serialized_end=2960
  _globals['_GPUSETTINGS_GPUENVIRONMENT']._serialized_start=2878
  _globals['_GPUSETTINGS_GPUENVIRONMENT']._serialized_end=2960
  _globals['_NETWORKINTERFACESPEC']._serialized_start=2963
  _globals['_NETWORKINTERFACESPEC']._serialized_end=3175
  _globals['_NODEADDRESSSPEC']._serialized_start=3178
  _globals['_NODEADDRESSSPEC']._serialized_end=3324
  _globals['_DNSRECORDSPEC']._serialized_start=3326
  _globals['_DNSRECORDSPEC']._serialized_end=3421
  _globals['_ONETOONENATSPEC']._serialized_start=3423
  _globals['_ONETOONENATSPEC']._serialized_end=3492
  _globals['_RESOURCESSPEC']._serialized_start=3494
  _globals['_RESOURCESSPEC']._serialized_end=3615
  _globals['_DISKSPEC']._serialized_start=3618
  _globals['_DISKSPEC']._serialized_end=3764
  _globals['_SCHEDULINGPOLICY']._serialized_start=3766
  _globals['_SCHEDULINGPOLICY']._serialized_end=3805
  _globals['_PLACEMENTPOLICY']._serialized_start=3807
  _globals['_PLACEMENTPOLICY']._serialized_end=3852
# @@protoc_insertion_point(module_scope)
