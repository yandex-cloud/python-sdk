# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/speechsense/v1/talk_service.proto
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
    'yandex/cloud/speechsense/v1/talk_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.speechsense.v1 import audio_pb2 as yandex_dot_cloud_dot_speechsense_dot_v1_dot_audio__pb2
from yandex.cloud.speechsense.v1 import text_pb2 as yandex_dot_cloud_dot_speechsense_dot_v1_dot_text__pb2
from yandex.cloud.speechsense.v1 import search_pb2 as yandex_dot_cloud_dot_speechsense_dot_v1_dot_search__pb2
from yandex.cloud.speechsense.v1 import talk_pb2 as yandex_dot_cloud_dot_speechsense_dot_v1_dot_talk__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.yandex/cloud/speechsense/v1/talk_service.proto\x12\x1byandex.cloud.speechsense.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\'yandex/cloud/speechsense/v1/audio.proto\x1a&yandex/cloud/speechsense/v1/text.proto\x1a(yandex/cloud/speechsense/v1/search.proto\x1a&yandex/cloud/speechsense/v1/talk.proto\"\xa0\x01\n\x11StreamTalkRequest\x12=\n\x08metadata\x18\x01 \x01(\x0b\x32).yandex.cloud.speechsense.v1.TalkMetadataH\x00\x12\x43\n\x05\x61udio\x18\x02 \x01(\x0b\x32\x32.yandex.cloud.speechsense.v1.AudioStreamingRequestH\x00\x42\x07\n\x05\x45vent\"\x9b\x01\n\x11UploadTalkRequest\x12\x0f\n\x07talk_id\x18\x03 \x01(\t\x12;\n\x08metadata\x18\x01 \x01(\x0b\x32).yandex.cloud.speechsense.v1.TalkMetadata\x12\x38\n\x05\x61udio\x18\x02 \x01(\x0b\x32).yandex.cloud.speechsense.v1.AudioRequest\"%\n\x12UploadTalkResponse\x12\x0f\n\x07talk_id\x18\x01 \x01(\t\"\xa1\x01\n\x11UploadTextRequest\x12\x0f\n\x07talk_id\x18\x03 \x01(\t\x12;\n\x08metadata\x18\x01 \x01(\x0b\x32).yandex.cloud.speechsense.v1.TalkMetadata\x12>\n\x0ctext_content\x18\x02 \x01(\x0b\x32(.yandex.cloud.speechsense.v1.TextContent\"%\n\x12UploadTextResponse\x12\x0f\n\x07talk_id\x18\x01 \x01(\t\"\xd5\x01\n\x0cTalkMetadata\x12\x15\n\rconnection_id\x18\x01 \x01(\t\x12\x45\n\x06\x66ields\x18\x02 \x03(\x0b\x32\x35.yandex.cloud.speechsense.v1.TalkMetadata.FieldsEntry\x12\x38\n\x05users\x18\x03 \x03(\x0b\x32).yandex.cloud.speechsense.v1.UserMetadata\x1a-\n\x0b\x46ieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xc5\x01\n\x0cUserMetadata\x12\n\n\x02id\x18\x01 \x01(\t\x12\x33\n\x04role\x18\x02 \x01(\x0e\x32%.yandex.cloud.speechsense.v1.UserRole\x12\x45\n\x06\x66ields\x18\x03 \x03(\x0b\x32\x35.yandex.cloud.speechsense.v1.UserMetadata.FieldsEntry\x1a-\n\x0b\x46ieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xb3\x02\n\x11SearchTalkRequest\x12\x17\n\x0forganization_id\x18\x01 \x01(\t\x12\x10\n\x08space_id\x18\x02 \x01(\t\x12\x15\n\rconnection_id\x18\x03 \x01(\t\x12\x12\n\nproject_id\x18\x04 \x01(\t\x12\x34\n\x07\x66ilters\x18\x05 \x03(\x0b\x32#.yandex.cloud.speechsense.v1.Filter\x12\x31\n\x05query\x18\x06 \x01(\x0b\x32\".yandex.cloud.speechsense.v1.Query\x12\x11\n\tpage_size\x18\x07 \x01(\x03\x12\x12\n\npage_token\x18\x08 \x01(\t\x12\x38\n\tsort_data\x18\t \x01(\x0b\x32%.yandex.cloud.speechsense.v1.SortData\"T\n\x12SearchTalkResponse\x12\x10\n\x08talk_ids\x18\x01 \x03(\t\x12\x13\n\x0btalks_count\x18\x02 \x01(\x03\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t\"\xaa\x01\n\x0eGetTalkRequest\x12\x17\n\x0forganization_id\x18\x01 \x01(\t\x12\x10\n\x08space_id\x18\x02 \x01(\t\x12\x15\n\rconnection_id\x18\x03 \x01(\t\x12\x12\n\nproject_id\x18\x04 \x01(\t\x12\x10\n\x08talk_ids\x18\x05 \x03(\t\x12\x30\n\x0cresults_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"B\n\x0fGetTalkResponse\x12/\n\x04talk\x18\x01 \x03(\x0b\x32!.yandex.cloud.speechsense.v1.Talk*f\n\x08UserRole\x12\x19\n\x15USER_ROLE_UNSPECIFIED\x10\x00\x12\x16\n\x12USER_ROLE_OPERATOR\x10\x01\x12\x14\n\x10USER_ROLE_CLIENT\x10\x02\x12\x11\n\rUSER_ROLE_BOT\x10\x03\x32\xfe\x04\n\x0bTalkService\x12s\n\x0eUploadAsStream\x12..yandex.cloud.speechsense.v1.StreamTalkRequest\x1a/.yandex.cloud.speechsense.v1.UploadTalkResponse(\x01\x12k\n\x06Upload\x12..yandex.cloud.speechsense.v1.UploadTalkRequest\x1a/.yandex.cloud.speechsense.v1.UploadTalkResponse\"\x00\x12o\n\nUploadText\x12..yandex.cloud.speechsense.v1.UploadTextRequest\x1a/.yandex.cloud.speechsense.v1.UploadTextResponse\"\x00\x12\x92\x01\n\x06Search\x12..yandex.cloud.speechsense.v1.SearchTalkRequest\x1a/.yandex.cloud.speechsense.v1.SearchTalkResponse\"\'\x82\xd3\xe4\x93\x02!\"\x1c/speechsense/v1/talks/search:\x01*\x12\x86\x01\n\x03Get\x12+.yandex.cloud.speechsense.v1.GetTalkRequest\x1a,.yandex.cloud.speechsense.v1.GetTalkResponse\"$\x82\xd3\xe4\x93\x02\x1e\"\x19/speechsense/v1/talks/get:\x01*B\x80\x01\n\x1fyandex.cloud.api.speechsense.v1B\x10TalkServiceProtoZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/speechsense/v1;speechsenseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.speechsense.v1.talk_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037yandex.cloud.api.speechsense.v1B\020TalkServiceProtoZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/speechsense/v1;speechsense'
  _globals['_TALKMETADATA_FIELDSENTRY']._loaded_options = None
  _globals['_TALKMETADATA_FIELDSENTRY']._serialized_options = b'8\001'
  _globals['_USERMETADATA_FIELDSENTRY']._loaded_options = None
  _globals['_USERMETADATA_FIELDSENTRY']._serialized_options = b'8\001'
  _globals['_TALKSERVICE'].methods_by_name['Search']._loaded_options = None
  _globals['_TALKSERVICE'].methods_by_name['Search']._serialized_options = b'\202\323\344\223\002!\"\034/speechsense/v1/talks/search:\001*'
  _globals['_TALKSERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_TALKSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\036\"\031/speechsense/v1/talks/get:\001*'
  _globals['_USERROLE']._serialized_start=1922
  _globals['_USERROLE']._serialized_end=2024
  _globals['_STREAMTALKREQUEST']._serialized_start=307
  _globals['_STREAMTALKREQUEST']._serialized_end=467
  _globals['_UPLOADTALKREQUEST']._serialized_start=470
  _globals['_UPLOADTALKREQUEST']._serialized_end=625
  _globals['_UPLOADTALKRESPONSE']._serialized_start=627
  _globals['_UPLOADTALKRESPONSE']._serialized_end=664
  _globals['_UPLOADTEXTREQUEST']._serialized_start=667
  _globals['_UPLOADTEXTREQUEST']._serialized_end=828
  _globals['_UPLOADTEXTRESPONSE']._serialized_start=830
  _globals['_UPLOADTEXTRESPONSE']._serialized_end=867
  _globals['_TALKMETADATA']._serialized_start=870
  _globals['_TALKMETADATA']._serialized_end=1083
  _globals['_TALKMETADATA_FIELDSENTRY']._serialized_start=1038
  _globals['_TALKMETADATA_FIELDSENTRY']._serialized_end=1083
  _globals['_USERMETADATA']._serialized_start=1086
  _globals['_USERMETADATA']._serialized_end=1283
  _globals['_USERMETADATA_FIELDSENTRY']._serialized_start=1038
  _globals['_USERMETADATA_FIELDSENTRY']._serialized_end=1083
  _globals['_SEARCHTALKREQUEST']._serialized_start=1286
  _globals['_SEARCHTALKREQUEST']._serialized_end=1593
  _globals['_SEARCHTALKRESPONSE']._serialized_start=1595
  _globals['_SEARCHTALKRESPONSE']._serialized_end=1679
  _globals['_GETTALKREQUEST']._serialized_start=1682
  _globals['_GETTALKREQUEST']._serialized_end=1852
  _globals['_GETTALKRESPONSE']._serialized_start=1854
  _globals['_GETTALKRESPONSE']._serialized_end=1920
  _globals['_TALKSERVICE']._serialized_start=2027
  _globals['_TALKSERVICE']._serialized_end=2665
# @@protoc_insertion_point(module_scope)
