# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/monitoring/v3/parametrization.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.monitoring.v3 import unit_format_pb2 as yandex_dot_cloud_dot_monitoring_dot_v3_dot_unit__format__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0yandex/cloud/monitoring/v3/parametrization.proto\x12\x1ayandex.cloud.monitoring.v3\x1a,yandex/cloud/monitoring/v3/unit_format.proto\"\x8f\x01\n\x14LabelValuesParameter\x12\x13\n\tfolder_id\x18\x02 \x01(\tH\x00\x12\x11\n\tselectors\x18\x13 \x01(\t\x12\x11\n\tlabel_key\x18\x14 \x01(\t\x12\x17\n\x0fmultiselectable\x18\x15 \x01(\x08\x12\x16\n\x0e\x64\x65\x66\x61ult_values\x18\x16 \x03(\tB\x0b\n\tcontainer\"R\n\x0f\x43ustomParameter\x12\x0e\n\x06values\x18\x01 \x03(\t\x12\x17\n\x0fmultiselectable\x18\x02 \x01(\x08\x12\x16\n\x0e\x64\x65\x66\x61ult_values\x18\x03 \x03(\t\"&\n\rTextParameter\x12\x15\n\rdefault_value\x18\x01 \x01(\t\"e\n\x0f\x44oubleParameter\x12\x15\n\rdefault_value\x18\x01 \x01(\x01\x12;\n\x0bunit_format\x18\x02 \x01(\x0e\x32&.yandex.cloud.monitoring.v3.UnitFormat\"f\n\x10IntegerParameter\x12\x15\n\rdefault_value\x18\x01 \x01(\x03\x12;\n\x0bunit_format\x18\x02 \x01(\x0e\x32&.yandex.cloud.monitoring.v3.UnitFormat\"-\n\x13TextValuesParameter\x12\x16\n\x0e\x64\x65\x66\x61ult_values\x18\x01 \x03(\t\"\xf5\x03\n\tParameter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12H\n\x0clabel_values\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.monitoring.v3.LabelValuesParameterH\x00\x12=\n\x06\x63ustom\x18\x04 \x01(\x0b\x32+.yandex.cloud.monitoring.v3.CustomParameterH\x00\x12\x39\n\x04text\x18\x05 \x01(\x0b\x32).yandex.cloud.monitoring.v3.TextParameterH\x00\x12I\n\x11integer_parameter\x18\x07 \x01(\x0b\x32,.yandex.cloud.monitoring.v3.IntegerParameterH\x00\x12G\n\x10\x64ouble_parameter\x18\x08 \x01(\x0b\x32+.yandex.cloud.monitoring.v3.DoubleParameterH\x00\x12\x46\n\x0btext_values\x18\t \x01(\x0b\x32/.yandex.cloud.monitoring.v3.TextValuesParameterH\x00\x12\x0e\n\x06hidden\x18\x06 \x01(\x08\x12\x13\n\x0b\x64\x65scription\x18\n \x01(\tB\x06\n\x04\x64\x61ta\"_\n\x0fParametrization\x12\x39\n\nparameters\x18\x01 \x03(\x0b\x32%.yandex.cloud.monitoring.v3.Parameter\x12\x11\n\tselectors\x18\x02 \x01(\tBk\n\x1eyandex.cloud.api.monitoring.v3ZIgithub.com/yandex-cloud/go-genproto/yandex/cloud/monitoring/v3;monitoringb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.monitoring.v3.parametrization_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\036yandex.cloud.api.monitoring.v3ZIgithub.com/yandex-cloud/go-genproto/yandex/cloud/monitoring/v3;monitoring'
  _globals['_LABELVALUESPARAMETER']._serialized_start=127
  _globals['_LABELVALUESPARAMETER']._serialized_end=270
  _globals['_CUSTOMPARAMETER']._serialized_start=272
  _globals['_CUSTOMPARAMETER']._serialized_end=354
  _globals['_TEXTPARAMETER']._serialized_start=356
  _globals['_TEXTPARAMETER']._serialized_end=394
  _globals['_DOUBLEPARAMETER']._serialized_start=396
  _globals['_DOUBLEPARAMETER']._serialized_end=497
  _globals['_INTEGERPARAMETER']._serialized_start=499
  _globals['_INTEGERPARAMETER']._serialized_end=601
  _globals['_TEXTVALUESPARAMETER']._serialized_start=603
  _globals['_TEXTVALUESPARAMETER']._serialized_end=648
  _globals['_PARAMETER']._serialized_start=651
  _globals['_PARAMETER']._serialized_end=1152
  _globals['_PARAMETRIZATION']._serialized_start=1154
  _globals['_PARAMETRIZATION']._serialized_end=1249
# @@protoc_insertion_point(module_scope)
