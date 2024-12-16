# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/ai/translate/v2/translation_service.proto
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
    'yandex/cloud/ai/translate/v2/translation_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.ai.translate.v2 import translation_pb2 as yandex_dot_cloud_dot_ai_dot_translate_dot_v2_dot_translation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6yandex/cloud/ai/translate/v2/translation_service.proto\x12\x1cyandex.cloud.ai.translate.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x1dyandex/cloud/validation.proto\x1a.yandex/cloud/ai/translate/v2/translation.proto\"\x95\x03\n\x10TranslateRequest\x12%\n\x14source_language_code\x18\x01 \x01(\tB\x07\x8a\xc8\x31\x03<=3\x12)\n\x14target_language_code\x18\x02 \x01(\tB\x0b\xe8\xc7\x31\x01\x8a\xc8\x31\x03<=3\x12\x45\n\x06\x66ormat\x18\x03 \x01(\x0e\x32\x35.yandex.cloud.ai.translate.v2.TranslateRequest.Format\x12\x15\n\x05texts\x18\x04 \x03(\tB\x06\x82\xc8\x31\x02>0\x12\x1b\n\tfolder_id\x18\x05 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x17\n\x05model\x18\x06 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12N\n\x0fglossary_config\x18\x07 \x01(\x0b\x32\x35.yandex.cloud.ai.translate.v2.TranslateGlossaryConfig\x12\x0f\n\x07speller\x18\x08 \x01(\x08\":\n\x06\x46ormat\x12\x16\n\x12\x46ORMAT_UNSPECIFIED\x10\x00\x12\x0e\n\nPLAIN_TEXT\x10\x01\x12\x08\n\x04HTML\x10\x02\"w\n\x17TranslateGlossaryConfig\x12\x43\n\rglossary_data\x18\x01 \x01(\x0b\x32*.yandex.cloud.ai.translate.v2.GlossaryDataH\x00\x42\x17\n\x0fglossary_source\x12\x04\xc0\xc1\x31\x01\"\\\n\x0cGlossaryData\x12L\n\x0eglossary_pairs\x18\x01 \x03(\x0b\x32*.yandex.cloud.ai.translate.v2.GlossaryPairB\x08\x82\xc8\x31\x04\x31-50\"W\n\x0cGlossaryPair\x12\x19\n\x0bsource_text\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x1d\n\x0ftranslated_text\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\x12\r\n\x05\x65xact\x18\x03 \x01(\x08\"W\n\x11TranslateResponse\x12\x42\n\x0ctranslations\x18\x01 \x03(\x0b\x32,.yandex.cloud.ai.translate.v2.TranslatedText\"\x80\x01\n\x15\x44\x65tectLanguageRequest\x12\x1c\n\x04text\x18\x01 \x01(\tB\x0e\xe8\xc7\x31\x01\x8a\xc8\x31\x06<=1000\x12,\n\x13language_code_hints\x18\x02 \x03(\tB\x0f\x82\xc8\x31\x04<=10\x8a\xc8\x31\x03<=3\x12\x1b\n\tfolder_id\x18\x03 \x01(\tB\x08\x8a\xc8\x31\x04<=50\"/\n\x16\x44\x65tectLanguageResponse\x12\x15\n\rlanguage_code\x18\x01 \x01(\t\"3\n\x14ListLanguagesRequest\x12\x1b\n\tfolder_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\"R\n\x15ListLanguagesResponse\x12\x39\n\tlanguages\x18\x01 \x03(\x0b\x32&.yandex.cloud.ai.translate.v2.Language2\xe5\x03\n\x12TranslationService\x12\x90\x01\n\tTranslate\x12..yandex.cloud.ai.translate.v2.TranslateRequest\x1a/.yandex.cloud.ai.translate.v2.TranslateResponse\"\"\x82\xd3\xe4\x93\x02\x1c\"\x17/translate/v2/translate:\x01*\x12\x9c\x01\n\x0e\x44\x65tectLanguage\x12\x33.yandex.cloud.ai.translate.v2.DetectLanguageRequest\x1a\x34.yandex.cloud.ai.translate.v2.DetectLanguageResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\"\x14/translate/v2/detect:\x01*\x12\x9c\x01\n\rListLanguages\x12\x32.yandex.cloud.ai.translate.v2.ListLanguagesRequest\x1a\x33.yandex.cloud.ai.translate.v2.ListLanguagesResponse\"\"\x82\xd3\xe4\x93\x02\x1c\"\x17/translate/v2/languages:\x01*Bn\n yandex.cloud.api.ai.translate.v2ZJgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/translate/v2;translateb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.ai.translate.v2.translation_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n yandex.cloud.api.ai.translate.v2ZJgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/translate/v2;translate'
  _globals['_TRANSLATEREQUEST'].fields_by_name['source_language_code']._loaded_options = None
  _globals['_TRANSLATEREQUEST'].fields_by_name['source_language_code']._serialized_options = b'\212\3101\003<=3'
  _globals['_TRANSLATEREQUEST'].fields_by_name['target_language_code']._loaded_options = None
  _globals['_TRANSLATEREQUEST'].fields_by_name['target_language_code']._serialized_options = b'\350\3071\001\212\3101\003<=3'
  _globals['_TRANSLATEREQUEST'].fields_by_name['texts']._loaded_options = None
  _globals['_TRANSLATEREQUEST'].fields_by_name['texts']._serialized_options = b'\202\3101\002>0'
  _globals['_TRANSLATEREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_TRANSLATEREQUEST'].fields_by_name['folder_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_TRANSLATEREQUEST'].fields_by_name['model']._loaded_options = None
  _globals['_TRANSLATEREQUEST'].fields_by_name['model']._serialized_options = b'\212\3101\004<=50'
  _globals['_TRANSLATEGLOSSARYCONFIG'].oneofs_by_name['glossary_source']._loaded_options = None
  _globals['_TRANSLATEGLOSSARYCONFIG'].oneofs_by_name['glossary_source']._serialized_options = b'\300\3011\001'
  _globals['_GLOSSARYDATA'].fields_by_name['glossary_pairs']._loaded_options = None
  _globals['_GLOSSARYDATA'].fields_by_name['glossary_pairs']._serialized_options = b'\202\3101\0041-50'
  _globals['_GLOSSARYPAIR'].fields_by_name['source_text']._loaded_options = None
  _globals['_GLOSSARYPAIR'].fields_by_name['source_text']._serialized_options = b'\350\3071\001'
  _globals['_GLOSSARYPAIR'].fields_by_name['translated_text']._loaded_options = None
  _globals['_GLOSSARYPAIR'].fields_by_name['translated_text']._serialized_options = b'\350\3071\001'
  _globals['_DETECTLANGUAGEREQUEST'].fields_by_name['text']._loaded_options = None
  _globals['_DETECTLANGUAGEREQUEST'].fields_by_name['text']._serialized_options = b'\350\3071\001\212\3101\006<=1000'
  _globals['_DETECTLANGUAGEREQUEST'].fields_by_name['language_code_hints']._loaded_options = None
  _globals['_DETECTLANGUAGEREQUEST'].fields_by_name['language_code_hints']._serialized_options = b'\202\3101\004<=10\212\3101\003<=3'
  _globals['_DETECTLANGUAGEREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_DETECTLANGUAGEREQUEST'].fields_by_name['folder_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_LISTLANGUAGESREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_LISTLANGUAGESREQUEST'].fields_by_name['folder_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_TRANSLATIONSERVICE'].methods_by_name['Translate']._loaded_options = None
  _globals['_TRANSLATIONSERVICE'].methods_by_name['Translate']._serialized_options = b'\202\323\344\223\002\034\"\027/translate/v2/translate:\001*'
  _globals['_TRANSLATIONSERVICE'].methods_by_name['DetectLanguage']._loaded_options = None
  _globals['_TRANSLATIONSERVICE'].methods_by_name['DetectLanguage']._serialized_options = b'\202\323\344\223\002\031\"\024/translate/v2/detect:\001*'
  _globals['_TRANSLATIONSERVICE'].methods_by_name['ListLanguages']._loaded_options = None
  _globals['_TRANSLATIONSERVICE'].methods_by_name['ListLanguages']._serialized_options = b'\202\323\344\223\002\034\"\027/translate/v2/languages:\001*'
  _globals['_TRANSLATEREQUEST']._serialized_start=198
  _globals['_TRANSLATEREQUEST']._serialized_end=603
  _globals['_TRANSLATEREQUEST_FORMAT']._serialized_start=545
  _globals['_TRANSLATEREQUEST_FORMAT']._serialized_end=603
  _globals['_TRANSLATEGLOSSARYCONFIG']._serialized_start=605
  _globals['_TRANSLATEGLOSSARYCONFIG']._serialized_end=724
  _globals['_GLOSSARYDATA']._serialized_start=726
  _globals['_GLOSSARYDATA']._serialized_end=818
  _globals['_GLOSSARYPAIR']._serialized_start=820
  _globals['_GLOSSARYPAIR']._serialized_end=907
  _globals['_TRANSLATERESPONSE']._serialized_start=909
  _globals['_TRANSLATERESPONSE']._serialized_end=996
  _globals['_DETECTLANGUAGEREQUEST']._serialized_start=999
  _globals['_DETECTLANGUAGEREQUEST']._serialized_end=1127
  _globals['_DETECTLANGUAGERESPONSE']._serialized_start=1129
  _globals['_DETECTLANGUAGERESPONSE']._serialized_end=1176
  _globals['_LISTLANGUAGESREQUEST']._serialized_start=1178
  _globals['_LISTLANGUAGESREQUEST']._serialized_end=1229
  _globals['_LISTLANGUAGESRESPONSE']._serialized_start=1231
  _globals['_LISTLANGUAGESRESPONSE']._serialized_end=1313
  _globals['_TRANSLATIONSERVICE']._serialized_start=1316
  _globals['_TRANSLATIONSERVICE']._serialized_end=1801
# @@protoc_insertion_point(module_scope)
