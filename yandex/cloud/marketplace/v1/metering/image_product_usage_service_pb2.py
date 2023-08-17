# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/marketplace/v1/metering/image_product_usage_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.marketplace.v1.metering import usage_record_pb2 as yandex_dot_cloud_dot_marketplace_dot_v1_dot_metering_dot_usage__record__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nFyandex/cloud/marketplace/v1/metering/image_product_usage_service.proto\x12$yandex.cloud.marketplace.v1.metering\x1a\x1cgoogle/api/annotations.proto\x1a\x1dyandex/cloud/validation.proto\x1a\x37yandex/cloud/marketplace/v1/metering/usage_record.proto\"\xac\x01\n\x1dWriteImageProductUsageRequest\x12\x15\n\rvalidate_only\x18\x01 \x01(\x08\x12 \n\nproduct_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12R\n\rusage_records\x18\x03 \x03(\x0b\x32\x31.yandex.cloud.marketplace.v1.metering.UsageRecordB\x08\x82\xc8\x31\x04\x31-25\"\xba\x01\n\x1eWriteImageProductUsageResponse\x12K\n\x08\x61\x63\x63\x65pted\x18\x01 \x03(\x0b\x32\x39.yandex.cloud.marketplace.v1.metering.AcceptedUsageRecord\x12K\n\x08rejected\x18\x02 \x03(\x0b\x32\x39.yandex.cloud.marketplace.v1.metering.RejectedUsageRecord2\xec\x01\n\x18ImageProductUsageService\x12\xcf\x01\n\x05Write\x12\x43.yandex.cloud.marketplace.v1.metering.WriteImageProductUsageRequest\x1a\x44.yandex.cloud.marketplace.v1.metering.WriteImageProductUsageResponse\";\x82\xd3\xe4\x93\x02\x35\"0/marketplace/v1/metering/imageProductUsage/write:\x01*B}\n(yandex.cloud.api.marketplace.v1.meteringZQgithub.com/yandex-cloud/go-genproto/yandex/cloud/marketplace/v1/metering;meteringb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.marketplace.v1.metering.image_product_usage_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n(yandex.cloud.api.marketplace.v1.meteringZQgithub.com/yandex-cloud/go-genproto/yandex/cloud/marketplace/v1/metering;metering'
  _WRITEIMAGEPRODUCTUSAGEREQUEST.fields_by_name['product_id']._options = None
  _WRITEIMAGEPRODUCTUSAGEREQUEST.fields_by_name['product_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _WRITEIMAGEPRODUCTUSAGEREQUEST.fields_by_name['usage_records']._options = None
  _WRITEIMAGEPRODUCTUSAGEREQUEST.fields_by_name['usage_records']._serialized_options = b'\202\3101\0041-25'
  _IMAGEPRODUCTUSAGESERVICE.methods_by_name['Write']._options = None
  _IMAGEPRODUCTUSAGESERVICE.methods_by_name['Write']._serialized_options = b'\202\323\344\223\0025\"0/marketplace/v1/metering/imageProductUsage/write:\001*'
  _globals['_WRITEIMAGEPRODUCTUSAGEREQUEST']._serialized_start=231
  _globals['_WRITEIMAGEPRODUCTUSAGEREQUEST']._serialized_end=403
  _globals['_WRITEIMAGEPRODUCTUSAGERESPONSE']._serialized_start=406
  _globals['_WRITEIMAGEPRODUCTUSAGERESPONSE']._serialized_end=592
  _globals['_IMAGEPRODUCTUSAGESERVICE']._serialized_start=595
  _globals['_IMAGEPRODUCTUSAGESERVICE']._serialized_end=831
# @@protoc_insertion_point(module_scope)
