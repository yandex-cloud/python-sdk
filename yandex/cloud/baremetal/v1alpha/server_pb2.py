# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/baremetal/v1alpha/server.proto
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
    'yandex/cloud/baremetal/v1alpha/server.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud.baremetal.v1alpha import disk_pb2 as yandex_dot_cloud_dot_baremetal_dot_v1alpha_dot_disk__pb2
from yandex.cloud.baremetal.v1alpha import storage_pb2 as yandex_dot_cloud_dot_baremetal_dot_v1alpha_dot_storage__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+yandex/cloud/baremetal/v1alpha/server.proto\x12\x1eyandex.cloud.baremetal.v1alpha\x1a\x1fgoogle/protobuf/timestamp.proto\x1a)yandex/cloud/baremetal/v1alpha/disk.proto\x1a,yandex/cloud/baremetal/v1alpha/storage.proto\"\xe2\x06\n\x06Server\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08\x63loud_id\x18\x02 \x01(\t\x12\x11\n\tfolder_id\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x0f\n\x07zone_id\x18\x06 \x01(\t\x12\x18\n\x10hardware_pool_id\x18\x07 \x01(\t\x12=\n\x06status\x18\t \x01(\x0e\x32-.yandex.cloud.baremetal.v1alpha.Server.Status\x12?\n\x0bos_settings\x18\n \x01(\x0b\x32*.yandex.cloud.baremetal.v1alpha.OsSettings\x12L\n\x12network_interfaces\x18\x12 \x03(\x0b\x32\x30.yandex.cloud.baremetal.v1alpha.NetworkInterface\x12\x18\n\x10\x63onfiguration_id\x18\x14 \x01(\t\x12\x33\n\x05\x64isks\x18\x15 \x03(\x0b\x32$.yandex.cloud.baremetal.v1alpha.Disk\x12.\n\ncreated_at\x18\x64 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x43\n\x06labels\x18\xc8\x01 \x03(\x0b\x32\x32.yandex.cloud.baremetal.v1alpha.Server.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xd4\x01\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x10\n\x0cPROVISIONING\x10\x01\x12\x0c\n\x08STOPPING\x10\x03\x12\x0b\n\x07STOPPED\x10\x04\x12\x0c\n\x08STARTING\x10\x05\x12\x0e\n\nRESTARTING\x10\x06\x12\t\n\x05\x45RROR\x10\x07\x12\x0c\n\x08\x44\x45LETING\x10\x08\x12\x10\n\x0cREINSTALLING\x10\t\x12\x0c\n\x08UPDATING\x10\n\x12\x0f\n\x0bQUARANTINED\x10\x0c\x12\x0b\n\x07RUNNING\x10\x0e\"\x04\x08\x02\x10\x02\"\x04\x08\x0b\x10\x0b\"\x04\x08\r\x10\rJ\x04\x08\x08\x10\tJ\x04\x08\x0b\x10\x0cJ\x04\x08\x0c\x10\rJ\x04\x08\x0f\x10\x12J\x04\x08\x13\x10\x14J\x04\x08\x16\x10\x17J\x04\x08\x17\x10\x18J\x04\x08\r\x10\x0eJ\x04\x08\x0e\x10\x0fJ\x04\x08\x18\x10\x64J\x05\x08\x65\x10\xc8\x01\"\x87\x02\n\x10NetworkInterface\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0bmac_address\x18\x02 \x01(\t\x12\x12\n\nip_address\x18\x03 \x01(\t\x12W\n\x0eprivate_subnet\x18\x07 \x01(\x0b\x32=.yandex.cloud.baremetal.v1alpha.PrivateSubnetNetworkInterfaceH\x00\x12U\n\rpublic_subnet\x18\x08 \x01(\x0b\x32<.yandex.cloud.baremetal.v1alpha.PublicSubnetNetworkInterfaceH\x00\x42\x08\n\x06subnetJ\x04\x08\x04\x10\x07\":\n\x1dPrivateSubnetNetworkInterface\x12\x19\n\x11private_subnet_id\x18\x01 \x01(\t\"8\n\x1cPublicSubnetNetworkInterface\x12\x18\n\x10public_subnet_id\x18\x01 \x01(\t\"q\n\nOsSettings\x12\x10\n\x08image_id\x18\x01 \x01(\t\x12\x16\n\x0essh_public_key\x18\x02 \x01(\t\x12\x39\n\x08storages\x18\x03 \x03(\x0b\x32\'.yandex.cloud.baremetal.v1alpha.StorageBr\n\"yandex.cloud.api.baremetal.v1alphaZLgithub.com/yandex-cloud/go-genproto/yandex/cloud/baremetal/v1alpha;baremetalb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.baremetal.v1alpha.server_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"yandex.cloud.api.baremetal.v1alphaZLgithub.com/yandex-cloud/go-genproto/yandex/cloud/baremetal/v1alpha;baremetal'
  _globals['_SERVER_LABELSENTRY']._loaded_options = None
  _globals['_SERVER_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_SERVER']._serialized_start=202
  _globals['_SERVER']._serialized_end=1068
  _globals['_SERVER_LABELSENTRY']._serialized_start=741
  _globals['_SERVER_LABELSENTRY']._serialized_end=786
  _globals['_SERVER_STATUS']._serialized_start=789
  _globals['_SERVER_STATUS']._serialized_end=1001
  _globals['_NETWORKINTERFACE']._serialized_start=1071
  _globals['_NETWORKINTERFACE']._serialized_end=1334
  _globals['_PRIVATESUBNETNETWORKINTERFACE']._serialized_start=1336
  _globals['_PRIVATESUBNETNETWORKINTERFACE']._serialized_end=1394
  _globals['_PUBLICSUBNETNETWORKINTERFACE']._serialized_start=1396
  _globals['_PUBLICSUBNETNETWORKINTERFACE']._serialized_end=1452
  _globals['_OSSETTINGS']._serialized_start=1454
  _globals['_OSSETTINGS']._serialized_end=1567
# @@protoc_insertion_point(module_scope)
