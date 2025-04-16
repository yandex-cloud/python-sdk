# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/cdn/v1/shielding_service.proto
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
    'yandex/cloud/cdn/v1/shielding_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.cdn.v1 import shielding_pb2 as yandex_dot_cloud_dot_cdn_dot_v1_dot_shielding__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+yandex/cloud/cdn/v1/shielding_service.proto\x12\x13yandex.cloud.cdn.v1\x1a yandex/cloud/api/operation.proto\x1a#yandex/cloud/cdn/v1/shielding.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"?\n\x1aGetShieldingDetailsRequest\x12!\n\x0bresource_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"Z\n\x18\x41\x63tivateShieldingRequest\x12!\n\x0bresource_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1b\n\x0blocation_id\x18\x02 \x01(\x03\x42\x06\xfa\xc7\x31\x02>0\">\n\x19\x41\x63tivateShieldingMetadata\x12!\n\x0bresource_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"?\n\x1a\x44\x65\x61\x63tivateShieldingRequest\x12!\n\x0bresource_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"@\n\x1b\x44\x65\x61\x63tivateShieldingMetadata\x12!\n\x0bresource_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"X\n\x16UpdateShieldingRequest\x12!\n\x0bresource_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1b\n\x0blocation_id\x18\x02 \x01(\x03\x42\x06\xfa\xc7\x31\x02>0\"<\n\x17UpdateShieldingMetadata\x12!\n\x0bresource_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"~\n\x1dListShieldingLocationsRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"}\n\x1eListShieldingLocationsResponse\x12\x42\n\x13shielding_locations\x18\x01 \x03(\x0b\x32%.yandex.cloud.cdn.v1.ShieldingDetails\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xb0\x05\n\x10ShieldingService\x12\x8f\x01\n\x08\x41\x63tivate\x12-.yandex.cloud.cdn.v1.ActivateShieldingRequest\x1a!.yandex.cloud.operation.Operation\"1\xb2\xd2*-\n\x19\x41\x63tivateShieldingMetadata\x12\x10ShieldingDetails\x12\x9a\x01\n\nDeactivate\x12/.yandex.cloud.cdn.v1.DeactivateShieldingRequest\x1a!.yandex.cloud.operation.Operation\"8\xb2\xd2*4\n\x1b\x44\x65\x61\x63tivateShieldingMetadata\x12\x15google.protobuf.Empty\x12]\n\x03Get\x12/.yandex.cloud.cdn.v1.GetShieldingDetailsRequest\x1a%.yandex.cloud.cdn.v1.ShieldingDetails\x12\x89\x01\n\x06Update\x12+.yandex.cloud.cdn.v1.UpdateShieldingRequest\x1a!.yandex.cloud.operation.Operation\"/\xb2\xd2*+\n\x17UpdateShieldingMetadata\x12\x10ShieldingDetails\x12\x81\x01\n\x16ListAvailableLocations\x12\x32.yandex.cloud.cdn.v1.ListShieldingLocationsRequest\x1a\x33.yandex.cloud.cdn.v1.ListShieldingLocationsResponseBV\n\x17yandex.cloud.api.cdn.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/cdn/v1;cdnb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.cdn.v1.shielding_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027yandex.cloud.api.cdn.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/cdn/v1;cdn'
  _globals['_GETSHIELDINGDETAILSREQUEST'].fields_by_name['resource_id']._loaded_options = None
  _globals['_GETSHIELDINGDETAILSREQUEST'].fields_by_name['resource_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_ACTIVATESHIELDINGREQUEST'].fields_by_name['resource_id']._loaded_options = None
  _globals['_ACTIVATESHIELDINGREQUEST'].fields_by_name['resource_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_ACTIVATESHIELDINGREQUEST'].fields_by_name['location_id']._loaded_options = None
  _globals['_ACTIVATESHIELDINGREQUEST'].fields_by_name['location_id']._serialized_options = b'\372\3071\002>0'
  _globals['_ACTIVATESHIELDINGMETADATA'].fields_by_name['resource_id']._loaded_options = None
  _globals['_ACTIVATESHIELDINGMETADATA'].fields_by_name['resource_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_DEACTIVATESHIELDINGREQUEST'].fields_by_name['resource_id']._loaded_options = None
  _globals['_DEACTIVATESHIELDINGREQUEST'].fields_by_name['resource_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_DEACTIVATESHIELDINGMETADATA'].fields_by_name['resource_id']._loaded_options = None
  _globals['_DEACTIVATESHIELDINGMETADATA'].fields_by_name['resource_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_UPDATESHIELDINGREQUEST'].fields_by_name['resource_id']._loaded_options = None
  _globals['_UPDATESHIELDINGREQUEST'].fields_by_name['resource_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_UPDATESHIELDINGREQUEST'].fields_by_name['location_id']._loaded_options = None
  _globals['_UPDATESHIELDINGREQUEST'].fields_by_name['location_id']._serialized_options = b'\372\3071\002>0'
  _globals['_UPDATESHIELDINGMETADATA'].fields_by_name['resource_id']._loaded_options = None
  _globals['_UPDATESHIELDINGMETADATA'].fields_by_name['resource_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTSHIELDINGLOCATIONSREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_LISTSHIELDINGLOCATIONSREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTSHIELDINGLOCATIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTSHIELDINGLOCATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTSHIELDINGLOCATIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTSHIELDINGLOCATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_SHIELDINGSERVICE'].methods_by_name['Activate']._loaded_options = None
  _globals['_SHIELDINGSERVICE'].methods_by_name['Activate']._serialized_options = b'\262\322*-\n\031ActivateShieldingMetadata\022\020ShieldingDetails'
  _globals['_SHIELDINGSERVICE'].methods_by_name['Deactivate']._loaded_options = None
  _globals['_SHIELDINGSERVICE'].methods_by_name['Deactivate']._serialized_options = b'\262\322*4\n\033DeactivateShieldingMetadata\022\025google.protobuf.Empty'
  _globals['_SHIELDINGSERVICE'].methods_by_name['Update']._loaded_options = None
  _globals['_SHIELDINGSERVICE'].methods_by_name['Update']._serialized_options = b'\262\322*+\n\027UpdateShieldingMetadata\022\020ShieldingDetails'
  _globals['_GETSHIELDINGDETAILSREQUEST']._serialized_start=210
  _globals['_GETSHIELDINGDETAILSREQUEST']._serialized_end=273
  _globals['_ACTIVATESHIELDINGREQUEST']._serialized_start=275
  _globals['_ACTIVATESHIELDINGREQUEST']._serialized_end=365
  _globals['_ACTIVATESHIELDINGMETADATA']._serialized_start=367
  _globals['_ACTIVATESHIELDINGMETADATA']._serialized_end=429
  _globals['_DEACTIVATESHIELDINGREQUEST']._serialized_start=431
  _globals['_DEACTIVATESHIELDINGREQUEST']._serialized_end=494
  _globals['_DEACTIVATESHIELDINGMETADATA']._serialized_start=496
  _globals['_DEACTIVATESHIELDINGMETADATA']._serialized_end=560
  _globals['_UPDATESHIELDINGREQUEST']._serialized_start=562
  _globals['_UPDATESHIELDINGREQUEST']._serialized_end=650
  _globals['_UPDATESHIELDINGMETADATA']._serialized_start=652
  _globals['_UPDATESHIELDINGMETADATA']._serialized_end=712
  _globals['_LISTSHIELDINGLOCATIONSREQUEST']._serialized_start=714
  _globals['_LISTSHIELDINGLOCATIONSREQUEST']._serialized_end=840
  _globals['_LISTSHIELDINGLOCATIONSRESPONSE']._serialized_start=842
  _globals['_LISTSHIELDINGLOCATIONSRESPONSE']._serialized_end=967
  _globals['_SHIELDINGSERVICE']._serialized_start=970
  _globals['_SHIELDINGSERVICE']._serialized_end=1658
# @@protoc_insertion_point(module_scope)
