# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/speechsense/v1/analysis/predefined_classifiers.proto
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
    'yandex/cloud/speechsense/v1/analysis/predefined_classifiers.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAyandex/cloud/speechsense/v1/analysis/predefined_classifiers.proto\x12$yandex.cloud.speechsense.v1.analysis\"\xfa\x01\n\x1bRecognitionClassifierResult\x12\x15\n\rstart_time_ms\x18\x01 \x01(\x03\x12\x13\n\x0b\x65nd_time_ms\x18\x02 \x01(\x03\x12\x12\n\nclassifier\x18\x03 \x01(\t\x12I\n\nhighlights\x18\x04 \x03(\x0b\x32\x35.yandex.cloud.speechsense.v1.analysis.PhraseHighlight\x12P\n\x06labels\x18\x05 \x03(\x0b\x32@.yandex.cloud.speechsense.v1.analysis.RecognitionClassifierLabel\">\n\x0fPhraseHighlight\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x03\x12\r\n\x05\x63ount\x18\x03 \x01(\x03\"?\n\x1aRecognitionClassifierLabel\x12\r\n\x05label\x18\x01 \x01(\t\x12\x12\n\nconfidence\x18\x02 \x01(\x01\x42\x9c\x01\n(yandex.cloud.api.speechsense.v1.analysisB\x1aRecognitionClassifierProtoZTgithub.com/yandex-cloud/go-genproto/yandex/cloud/speechsense/v1/analysis;speechsenseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.speechsense.v1.analysis.predefined_classifiers_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n(yandex.cloud.api.speechsense.v1.analysisB\032RecognitionClassifierProtoZTgithub.com/yandex-cloud/go-genproto/yandex/cloud/speechsense/v1/analysis;speechsense'
  _globals['_RECOGNITIONCLASSIFIERRESULT']._serialized_start=108
  _globals['_RECOGNITIONCLASSIFIERRESULT']._serialized_end=358
  _globals['_PHRASEHIGHLIGHT']._serialized_start=360
  _globals['_PHRASEHIGHLIGHT']._serialized_end=422
  _globals['_RECOGNITIONCLASSIFIERLABEL']._serialized_start=424
  _globals['_RECOGNITIONCLASSIFIERLABEL']._serialized_end=487
# @@protoc_insertion_point(module_scope)
