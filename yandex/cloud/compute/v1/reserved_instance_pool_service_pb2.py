# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/compute/v1/reserved_instance_pool_service.proto
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
    'yandex/cloud/compute/v1/reserved_instance_pool_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.compute.v1 import instance_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_instance__pb2
from yandex.cloud.compute.v1 import instance_service_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2
from yandex.cloud.compute.v1 import reserved_instance_pool_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_reserved__instance__pool__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<yandex/cloud/compute/v1/reserved_instance_pool_service.proto\x12\x17yandex.cloud.compute.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/compute/v1/instance.proto\x1a.yandex/cloud/compute/v1/instance_service.proto\x1a\x34yandex/cloud/compute/v1/reserved_instance_pool.proto\x1a\x1dyandex/cloud/validation.proto\x1a&yandex/cloud/operation/operation.proto\"Q\n\x1eGetReservedInstancePoolRequest\x12/\n\x19reserved_instance_pool_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\xba\x01\n ListReservedInstancePoolsRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\x12\x1b\n\x08order_by\x18\x05 \x01(\tB\t\x8a\xc8\x31\x05<=100\"\x8c\x01\n!ListReservedInstancePoolsResponse\x12N\n\x17reserved_instance_pools\x18\x01 \x03(\x0b\x32-.yandex.cloud.compute.v1.ReservedInstancePool\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xc2\x05\n!CreateReservedInstancePoolRequest\x12\x33\n\x04name\x18\x01 \x01(\tB%\xf2\xc7\x31!|[a-z]([-_a-z0-9]{0,61}[a-z0-9])?\x12\x1e\n\x0b\x64\x65scription\x18\x02 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x9b\x01\n\x06labels\x18\x03 \x03(\x0b\x32\x46.yandex.cloud.compute.v1.CreateReservedInstancePoolRequest.LabelsEntryBC\xf2\xc7\x31\x0f[-_./\\@0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x1c\x12\x14[a-z][-_./\\@0-9a-z]*\x1a\x04\x31-63\x12\x1d\n\x07zone_id\x18\x04 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1f\n\tfolder_id\x18\x05 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x19\n\x0bplatform_id\x18\x06 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x44\n\x0eresources_spec\x18\x07 \x01(\x0b\x32&.yandex.cloud.compute.v1.ResourcesSpecB\x04\xe8\xc7\x31\x01\x12:\n\x0cgpu_settings\x18\x08 \x01(\x0b\x32$.yandex.cloud.compute.v1.GpuSettings\x12=\n\x0e\x62oot_disk_spec\x18\t \x01(\x0b\x32%.yandex.cloud.compute.v1.BootDiskSpec\x12\x42\n\x10network_settings\x18\n \x01(\x0b\x32(.yandex.cloud.compute.v1.NetworkSettings\x12\x1b\n\x04size\x18\x0b \x01(\x03\x42\r\xfa\xc7\x31\t0-1048576\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"G\n\"CreateReservedInstancePoolMetadata\x12!\n\x19reserved_instance_pool_id\x18\x01 \x01(\t\"\xc4\x03\n!UpdateReservedInstancePoolRequest\x12/\n\x19reserved_instance_pool_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x33\n\x04name\x18\x03 \x01(\tB%\xf2\xc7\x31!|[a-z]([-_a-z0-9]{0,61}[a-z0-9])?\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x9b\x01\n\x06labels\x18\x05 \x03(\x0b\x32\x46.yandex.cloud.compute.v1.UpdateReservedInstancePoolRequest.LabelsEntryBC\xf2\xc7\x31\x0f[-_./\\@0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x1c\x12\x14[a-z][-_./\\@0-9a-z]*\x1a\x04\x31-63\x12\x1b\n\x04size\x18\x06 \x01(\x03\x42\r\xfa\xc7\x31\t0-1048576\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"G\n\"UpdateReservedInstancePoolMetadata\x12!\n\x19reserved_instance_pool_id\x18\x01 \x01(\t\"T\n!DeleteReservedInstancePoolRequest\x12/\n\x19reserved_instance_pool_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"G\n\"DeleteReservedInstancePoolMetadata\x12!\n\x19reserved_instance_pool_id\x18\x01 \x01(\t\"$\n\"DeleteReservedInstancePoolResponse2\xc6\x08\n\x1bReservedInstancePoolService\x12\xb4\x01\n\x03Get\x12\x37.yandex.cloud.compute.v1.GetReservedInstancePoolRequest\x1a-.yandex.cloud.compute.v1.ReservedInstancePool\"E\x82\xd3\xe4\x93\x02?\x12=/compute/v1/reservedInstancePools/{reserved_instance_pool_id}\x12\xa8\x01\n\x04List\x12\x39.yandex.cloud.compute.v1.ListReservedInstancePoolsRequest\x1a:.yandex.cloud.compute.v1.ListReservedInstancePoolsResponse\")\x82\xd3\xe4\x93\x02#\x12!/compute/v1/reservedInstancePools\x12\xd3\x01\n\x06\x43reate\x12:.yandex.cloud.compute.v1.CreateReservedInstancePoolRequest\x1a!.yandex.cloud.operation.Operation\"j\xb2\xd2*:\n\"CreateReservedInstancePoolMetadata\x12\x14ReservedInstancePool\x82\xd3\xe4\x93\x02&\"!/compute/v1/reservedInstancePools:\x01*\x12\xf0\x01\n\x06Update\x12:.yandex.cloud.compute.v1.UpdateReservedInstancePoolRequest\x1a!.yandex.cloud.operation.Operation\"\x86\x01\xb2\xd2*:\n\"UpdateReservedInstancePoolMetadata\x12\x14ReservedInstancePool\x82\xd3\xe4\x93\x02\x42\x32=/compute/v1/reservedInstancePools/{reserved_instance_pool_id}:\x01*\x12\xfb\x01\n\x06\x44\x65lete\x12:.yandex.cloud.compute.v1.DeleteReservedInstancePoolRequest\x1a!.yandex.cloud.operation.Operation\"\x91\x01\xb2\xd2*H\n\"DeleteReservedInstancePoolMetadata\x12\"DeleteReservedInstancePoolResponse\x82\xd3\xe4\x93\x02?*=/compute/v1/reservedInstancePools/{reserved_instance_pool_id}Bb\n\x1byandex.cloud.api.compute.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;computeb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.compute.v1.reserved_instance_pool_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033yandex.cloud.api.compute.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;compute'
  _globals['_GETRESERVEDINSTANCEPOOLREQUEST'].fields_by_name['reserved_instance_pool_id']._loaded_options = None
  _globals['_GETRESERVEDINSTANCEPOOLREQUEST'].fields_by_name['reserved_instance_pool_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTRESERVEDINSTANCEPOOLSREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_LISTRESERVEDINSTANCEPOOLSREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTRESERVEDINSTANCEPOOLSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTRESERVEDINSTANCEPOOLSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTRESERVEDINSTANCEPOOLSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTRESERVEDINSTANCEPOOLSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTRESERVEDINSTANCEPOOLSREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTRESERVEDINSTANCEPOOLSREQUEST'].fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _globals['_LISTRESERVEDINSTANCEPOOLSREQUEST'].fields_by_name['order_by']._loaded_options = None
  _globals['_LISTRESERVEDINSTANCEPOOLSREQUEST'].fields_by_name['order_by']._serialized_options = b'\212\3101\005<=100'
  _globals['_CREATERESERVEDINSTANCEPOOLREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_CREATERESERVEDINSTANCEPOOLREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_CREATERESERVEDINSTANCEPOOLREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_CREATERESERVEDINSTANCEPOOLREQUEST'].fields_by_name['name']._serialized_options = b'\362\3071!|[a-z]([-_a-z0-9]{0,61}[a-z0-9])?'
  _globals['_CREATERESERVEDINSTANCEPOOLREQUEST'].fields_by_name['description']._loaded_options = None
  _globals['_CREATERESERVEDINSTANCEPOOLREQUEST'].fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _globals['_CREATERESERVEDINSTANCEPOOLREQUEST'].fields_by_name['labels']._loaded_options = None
  _globals['_CREATERESERVEDINSTANCEPOOLREQUEST'].fields_by_name['labels']._serialized_options = b'\362\3071\017[-_./\\@0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\034\022\024[a-z][-_./\\@0-9a-z]*\032\0041-63'
  _globals['_CREATERESERVEDINSTANCEPOOLREQUEST'].fields_by_name['zone_id']._loaded_options = None
  _globals['_CREATERESERVEDINSTANCEPOOLREQUEST'].fields_by_name['zone_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_CREATERESERVEDINSTANCEPOOLREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_CREATERESERVEDINSTANCEPOOLREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_CREATERESERVEDINSTANCEPOOLREQUEST'].fields_by_name['platform_id']._loaded_options = None
  _globals['_CREATERESERVEDINSTANCEPOOLREQUEST'].fields_by_name['platform_id']._serialized_options = b'\350\3071\001'
  _globals['_CREATERESERVEDINSTANCEPOOLREQUEST'].fields_by_name['resources_spec']._loaded_options = None
  _globals['_CREATERESERVEDINSTANCEPOOLREQUEST'].fields_by_name['resources_spec']._serialized_options = b'\350\3071\001'
  _globals['_CREATERESERVEDINSTANCEPOOLREQUEST'].fields_by_name['size']._loaded_options = None
  _globals['_CREATERESERVEDINSTANCEPOOLREQUEST'].fields_by_name['size']._serialized_options = b'\372\3071\t0-1048576'
  _globals['_UPDATERESERVEDINSTANCEPOOLREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_UPDATERESERVEDINSTANCEPOOLREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_UPDATERESERVEDINSTANCEPOOLREQUEST'].fields_by_name['reserved_instance_pool_id']._loaded_options = None
  _globals['_UPDATERESERVEDINSTANCEPOOLREQUEST'].fields_by_name['reserved_instance_pool_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_UPDATERESERVEDINSTANCEPOOLREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_UPDATERESERVEDINSTANCEPOOLREQUEST'].fields_by_name['name']._serialized_options = b'\362\3071!|[a-z]([-_a-z0-9]{0,61}[a-z0-9])?'
  _globals['_UPDATERESERVEDINSTANCEPOOLREQUEST'].fields_by_name['description']._loaded_options = None
  _globals['_UPDATERESERVEDINSTANCEPOOLREQUEST'].fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _globals['_UPDATERESERVEDINSTANCEPOOLREQUEST'].fields_by_name['labels']._loaded_options = None
  _globals['_UPDATERESERVEDINSTANCEPOOLREQUEST'].fields_by_name['labels']._serialized_options = b'\362\3071\017[-_./\\@0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\034\022\024[a-z][-_./\\@0-9a-z]*\032\0041-63'
  _globals['_UPDATERESERVEDINSTANCEPOOLREQUEST'].fields_by_name['size']._loaded_options = None
  _globals['_UPDATERESERVEDINSTANCEPOOLREQUEST'].fields_by_name['size']._serialized_options = b'\372\3071\t0-1048576'
  _globals['_DELETERESERVEDINSTANCEPOOLREQUEST'].fields_by_name['reserved_instance_pool_id']._loaded_options = None
  _globals['_DELETERESERVEDINSTANCEPOOLREQUEST'].fields_by_name['reserved_instance_pool_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_RESERVEDINSTANCEPOOLSERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_RESERVEDINSTANCEPOOLSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002?\022=/compute/v1/reservedInstancePools/{reserved_instance_pool_id}'
  _globals['_RESERVEDINSTANCEPOOLSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_RESERVEDINSTANCEPOOLSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002#\022!/compute/v1/reservedInstancePools'
  _globals['_RESERVEDINSTANCEPOOLSERVICE'].methods_by_name['Create']._loaded_options = None
  _globals['_RESERVEDINSTANCEPOOLSERVICE'].methods_by_name['Create']._serialized_options = b'\262\322*:\n\"CreateReservedInstancePoolMetadata\022\024ReservedInstancePool\202\323\344\223\002&\"!/compute/v1/reservedInstancePools:\001*'
  _globals['_RESERVEDINSTANCEPOOLSERVICE'].methods_by_name['Update']._loaded_options = None
  _globals['_RESERVEDINSTANCEPOOLSERVICE'].methods_by_name['Update']._serialized_options = b'\262\322*:\n\"UpdateReservedInstancePoolMetadata\022\024ReservedInstancePool\202\323\344\223\002B2=/compute/v1/reservedInstancePools/{reserved_instance_pool_id}:\001*'
  _globals['_RESERVEDINSTANCEPOOLSERVICE'].methods_by_name['Delete']._loaded_options = None
  _globals['_RESERVEDINSTANCEPOOLSERVICE'].methods_by_name['Delete']._serialized_options = b'\262\322*H\n\"DeleteReservedInstancePoolMetadata\022\"DeleteReservedInstancePoolResponse\202\323\344\223\002?*=/compute/v1/reservedInstancePools/{reserved_instance_pool_id}'
  _globals['_GETRESERVEDINSTANCEPOOLREQUEST']._serialized_start=400
  _globals['_GETRESERVEDINSTANCEPOOLREQUEST']._serialized_end=481
  _globals['_LISTRESERVEDINSTANCEPOOLSREQUEST']._serialized_start=484
  _globals['_LISTRESERVEDINSTANCEPOOLSREQUEST']._serialized_end=670
  _globals['_LISTRESERVEDINSTANCEPOOLSRESPONSE']._serialized_start=673
  _globals['_LISTRESERVEDINSTANCEPOOLSRESPONSE']._serialized_end=813
  _globals['_CREATERESERVEDINSTANCEPOOLREQUEST']._serialized_start=816
  _globals['_CREATERESERVEDINSTANCEPOOLREQUEST']._serialized_end=1522
  _globals['_CREATERESERVEDINSTANCEPOOLREQUEST_LABELSENTRY']._serialized_start=1477
  _globals['_CREATERESERVEDINSTANCEPOOLREQUEST_LABELSENTRY']._serialized_end=1522
  _globals['_CREATERESERVEDINSTANCEPOOLMETADATA']._serialized_start=1524
  _globals['_CREATERESERVEDINSTANCEPOOLMETADATA']._serialized_end=1595
  _globals['_UPDATERESERVEDINSTANCEPOOLREQUEST']._serialized_start=1598
  _globals['_UPDATERESERVEDINSTANCEPOOLREQUEST']._serialized_end=2050
  _globals['_UPDATERESERVEDINSTANCEPOOLREQUEST_LABELSENTRY']._serialized_start=1477
  _globals['_UPDATERESERVEDINSTANCEPOOLREQUEST_LABELSENTRY']._serialized_end=1522
  _globals['_UPDATERESERVEDINSTANCEPOOLMETADATA']._serialized_start=2052
  _globals['_UPDATERESERVEDINSTANCEPOOLMETADATA']._serialized_end=2123
  _globals['_DELETERESERVEDINSTANCEPOOLREQUEST']._serialized_start=2125
  _globals['_DELETERESERVEDINSTANCEPOOLREQUEST']._serialized_end=2209
  _globals['_DELETERESERVEDINSTANCEPOOLMETADATA']._serialized_start=2211
  _globals['_DELETERESERVEDINSTANCEPOOLMETADATA']._serialized_end=2282
  _globals['_DELETERESERVEDINSTANCEPOOLRESPONSE']._serialized_start=2284
  _globals['_DELETERESERVEDINSTANCEPOOLRESPONSE']._serialized_end=2320
  _globals['_RESERVEDINSTANCEPOOLSERVICE']._serialized_start=2323
  _globals['_RESERVEDINSTANCEPOOLSERVICE']._serialized_end=3417
# @@protoc_insertion_point(module_scope)
