# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/speechsense/v1/analysis/transcription.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'yandex/cloud/speechsense/v1/analysis/transcription.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud.speechsense.v1.analysis import utterance_statistics_pb2 as yandex_dot_cloud_dot_speechsense_dot_v1_dot_analysis_dot_utterance__statistics__pb2
from yandex.cloud.speechsense.v1.analysis import predefined_classifiers_pb2 as yandex_dot_cloud_dot_speechsense_dot_v1_dot_analysis_dot_predefined__classifiers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8yandex/cloud/speechsense/v1/analysis/transcription.proto\x12$yandex.cloud.speechsense.v1.analysis\x1a\x1fgoogle/protobuf/timestamp.proto\x1a?yandex/cloud/speechsense/v1/analysis/utterance_statistics.proto\x1a\x41yandex/cloud/speechsense/v1/analysis/predefined_classifiers.proto\"\xa4\x01\n\rTranscription\x12=\n\x07phrases\x18\x01 \x03(\x0b\x32,.yandex.cloud.speechsense.v1.analysis.Phrase\x12T\n\x13\x61lgorithms_metadata\x18\x02 \x03(\x0b\x32\x37.yandex.cloud.speechsense.v1.analysis.AlgorithmMetadata\"\xb2\x02\n\x06Phrase\x12\x16\n\x0e\x63hannel_number\x18\x01 \x01(\x03\x12\x15\n\rstart_time_ms\x18\x02 \x01(\x03\x12\x13\n\x0b\x65nd_time_ms\x18\x03 \x01(\x03\x12@\n\x06phrase\x18\x04 \x01(\x0b\x32\x30.yandex.cloud.speechsense.v1.analysis.PhraseText\x12J\n\nstatistics\x18\x05 \x01(\x0b\x32\x36.yandex.cloud.speechsense.v1.analysis.PhraseStatistics\x12V\n\x0b\x63lassifiers\x18\x06 \x03(\x0b\x32\x41.yandex.cloud.speechsense.v1.analysis.RecognitionClassifierResult\"\x80\x01\n\nPhraseText\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x10\n\x08language\x18\x02 \x01(\t\x12\x17\n\x0fnormalized_text\x18\x03 \x01(\t\x12\x39\n\x05words\x18\x04 \x03(\x0b\x32*.yandex.cloud.speechsense.v1.analysis.Word\"@\n\x04Word\x12\x0c\n\x04word\x18\x01 \x01(\t\x12\x15\n\rstart_time_ms\x18\x02 \x01(\x03\x12\x13\n\x0b\x65nd_time_ms\x18\x03 \x01(\x03\"\xdf\x01\n\x11\x41lgorithmMetadata\x12\x35\n\x11\x63reated_task_date\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x37\n\x13\x63ompleted_task_date\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12:\n\x05\x65rror\x18\x03 \x01(\x0b\x32+.yandex.cloud.speechsense.v1.analysis.Error\x12\x10\n\x08trace_id\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\"&\n\x05\x45rror\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"a\n\x10PhraseStatistics\x12M\n\nstatistics\x18\x01 \x01(\x0b\x32\x39.yandex.cloud.speechsense.v1.analysis.UtteranceStatisticsB\x94\x01\n(yandex.cloud.api.speechsense.v1.analysisB\x12TranscriptionProtoZTgithub.com/yandex-cloud/go-genproto/yandex/cloud/speechsense/v1/analysis;speechsenseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.speechsense.v1.analysis.transcription_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n(yandex.cloud.api.speechsense.v1.analysisB\022TranscriptionProtoZTgithub.com/yandex-cloud/go-genproto/yandex/cloud/speechsense/v1/analysis;speechsense'
  _globals['_TRANSCRIPTION']._serialized_start=264
  _globals['_TRANSCRIPTION']._serialized_end=428
  _globals['_PHRASE']._serialized_start=431
  _globals['_PHRASE']._serialized_end=737
  _globals['_PHRASETEXT']._serialized_start=740
  _globals['_PHRASETEXT']._serialized_end=868
  _globals['_WORD']._serialized_start=870
  _globals['_WORD']._serialized_end=934
  _globals['_ALGORITHMMETADATA']._serialized_start=937
  _globals['_ALGORITHMMETADATA']._serialized_end=1160
  _globals['_ERROR']._serialized_start=1162
  _globals['_ERROR']._serialized_end=1200
  _globals['_PHRASESTATISTICS']._serialized_start=1202
  _globals['_PHRASESTATISTICS']._serialized_end=1299
# @@protoc_insertion_point(module_scope)
