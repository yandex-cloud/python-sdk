# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/ai/vision/v2/image_classifier.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.ai.vision.v2 import image_pb2 as yandex_dot_cloud_dot_ai_dot_vision_dot_v2_dot_image__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0yandex/cloud/ai/vision/v2/image_classifier.proto\x12\x19yandex.cloud.ai.vision.v2\x1a%yandex/cloud/ai/vision/v2/image.proto\"*\n\x05Label\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"V\n\x0f\x43lassAnnotation\x12/\n\x05label\x18\x01 \x01(\x0b\x32 .yandex.cloud.ai.vision.v2.Label\x12\x12\n\nconfidence\x18\x02 \x01(\x01\"\x8c\x02\n\x17\x43lassifierSpecification\x12\x30\n\x06labels\x18\x01 \x03(\x0b\x32 .yandex.cloud.ai.vision.v2.Label\x12\x62\n\x13\x63lassification_type\x18\x02 \x01(\x0e\x32\x45.yandex.cloud.ai.vision.v2.ClassifierSpecification.ClassificationType\"[\n\x12\x43lassificationType\x12#\n\x1f\x43LASSIFICATION_TYPE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bMULTI_LABEL\x10\x01\x12\x0f\n\x0bMULTI_CLASS\x10\x02\"\xbf\x01\n\x12\x41nnotationResponse\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12T\n\x18\x63lassifier_specification\x18\x02 \x01(\x0b\x32\x32.yandex.cloud.ai.vision.v2.ClassifierSpecification\x12?\n\x0b\x61nnotations\x18\x03 \x03(\x0b\x32*.yandex.cloud.ai.vision.v2.ClassAnnotation\"D\n\x11\x41nnotationRequest\x12/\n\x05image\x18\x01 \x01(\x0b\x32 .yandex.cloud.ai.vision.v2.ImageBe\n\x1dyandex.cloud.api.ai.vision.v2ZDgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/vision/v2;visionb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.ai.vision.v2.image_classifier_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035yandex.cloud.api.ai.vision.v2ZDgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/vision/v2;vision'
  _globals['_LABEL']._serialized_start=118
  _globals['_LABEL']._serialized_end=160
  _globals['_CLASSANNOTATION']._serialized_start=162
  _globals['_CLASSANNOTATION']._serialized_end=248
  _globals['_CLASSIFIERSPECIFICATION']._serialized_start=251
  _globals['_CLASSIFIERSPECIFICATION']._serialized_end=519
  _globals['_CLASSIFIERSPECIFICATION_CLASSIFICATIONTYPE']._serialized_start=428
  _globals['_CLASSIFIERSPECIFICATION_CLASSIFICATIONTYPE']._serialized_end=519
  _globals['_ANNOTATIONRESPONSE']._serialized_start=522
  _globals['_ANNOTATIONRESPONSE']._serialized_end=713
  _globals['_ANNOTATIONREQUEST']._serialized_start=715
  _globals['_ANNOTATIONREQUEST']._serialized_end=783
# @@protoc_insertion_point(module_scope)
