# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/cic/v1/peering.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!yandex/cloud/cic/v1/peering.proto\x12\x13yandex.cloud.cic.v1\"\x8b\x01\n\x07Peering\x12\x16\n\x0epeering_subnet\x18\x01 \x01(\t\x12\x0f\n\x07peer_ip\x18\x02 \x01(\t\x12\x10\n\x08\x63loud_ip\x18\x03 \x01(\t\x12\x14\n\x0cpeer_bgp_asn\x18\x04 \x01(\x03\x12\x15\n\rcloud_bgp_asn\x18\x05 \x01(\x03\x12\x18\n\x10peer_bgp_md5_key\x18\x06 \x01(\tBV\n\x17yandex.cloud.api.cic.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/cic/v1;cicb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.cic.v1.peering_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027yandex.cloud.api.cic.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/cic/v1;cic'
  _globals['_PEERING']._serialized_start=59
  _globals['_PEERING']._serialized_end=198
# @@protoc_insertion_point(module_scope)