# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/marketplace/licensemanager/v1/instance_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.marketplace.licensemanager.v1 import instance_pb2 as yandex_dot_cloud_dot_marketplace_dot_licensemanager_dot_v1_dot_instance__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAyandex/cloud/marketplace/licensemanager/v1/instance_service.proto\x12*yandex.cloud.marketplace.licensemanager.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x39yandex/cloud/marketplace/licensemanager/v1/instance.proto\x1a\x1dyandex/cloud/validation.proto\"/\n\x12GetInstanceRequest\x12\x19\n\x0binstance_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"\xa6\x01\n\x14ListInstancesRequest\x12\x17\n\tfolder_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\x12\x1b\n\x08order_by\x18\x05 \x01(\tB\t\x8a\xc8\x31\x05<=100\"y\n\x15ListInstancesResponse\x12G\n\tinstances\x18\x01 \x03(\x0b\x32\x34.yandex.cloud.marketplace.licensemanager.v1.Instance\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\x91\x03\n\x0fInstanceService\x12\xbc\x01\n\x03Get\x12>.yandex.cloud.marketplace.licensemanager.v1.GetInstanceRequest\x1a\x34.yandex.cloud.marketplace.licensemanager.v1.Instance\"?\x82\xd3\xe4\x93\x02\x39\x12\x37/marketplace/license-manager/v1/instances/{instance_id}\x12\xbe\x01\n\x04List\x12@.yandex.cloud.marketplace.licensemanager.v1.ListInstancesRequest\x1a\x41.yandex.cloud.marketplace.licensemanager.v1.ListInstancesResponse\"1\x82\xd3\xe4\x93\x02+\x12)/marketplace/license-manager/v1/instancesB\x8f\x01\n.yandex.cloud.api.marketplace.licensemanager.v1Z]github.com/yandex-cloud/go-genproto/yandex/cloud/marketplace/licensemanager/v1;licensemanagerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.marketplace.licensemanager.v1.instance_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n.yandex.cloud.api.marketplace.licensemanager.v1Z]github.com/yandex-cloud/go-genproto/yandex/cloud/marketplace/licensemanager/v1;licensemanager'
  _GETINSTANCEREQUEST.fields_by_name['instance_id']._options = None
  _GETINSTANCEREQUEST.fields_by_name['instance_id']._serialized_options = b'\350\3071\001'
  _LISTINSTANCESREQUEST.fields_by_name['folder_id']._options = None
  _LISTINSTANCESREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001'
  _LISTINSTANCESREQUEST.fields_by_name['page_size']._options = None
  _LISTINSTANCESREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _LISTINSTANCESREQUEST.fields_by_name['page_token']._options = None
  _LISTINSTANCESREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _LISTINSTANCESREQUEST.fields_by_name['filter']._options = None
  _LISTINSTANCESREQUEST.fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _LISTINSTANCESREQUEST.fields_by_name['order_by']._options = None
  _LISTINSTANCESREQUEST.fields_by_name['order_by']._serialized_options = b'\212\3101\005<=100'
  _INSTANCESERVICE.methods_by_name['Get']._options = None
  _INSTANCESERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\0029\0227/marketplace/license-manager/v1/instances/{instance_id}'
  _INSTANCESERVICE.methods_by_name['List']._options = None
  _INSTANCESERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002+\022)/marketplace/license-manager/v1/instances'
  _globals['_GETINSTANCEREQUEST']._serialized_start=233
  _globals['_GETINSTANCEREQUEST']._serialized_end=280
  _globals['_LISTINSTANCESREQUEST']._serialized_start=283
  _globals['_LISTINSTANCESREQUEST']._serialized_end=449
  _globals['_LISTINSTANCESRESPONSE']._serialized_start=451
  _globals['_LISTINSTANCESRESPONSE']._serialized_end=572
  _globals['_INSTANCESERVICE']._serialized_start=575
  _globals['_INSTANCESERVICE']._serialized_end=976
# @@protoc_insertion_point(module_scope)
