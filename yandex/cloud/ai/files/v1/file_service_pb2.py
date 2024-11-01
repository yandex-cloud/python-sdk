# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/ai/files/v1/file_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.ai.common import common_pb2 as yandex_dot_cloud_dot_ai_dot_common_dot_common__pb2
from yandex.cloud.ai.files.v1 import file_pb2 as yandex_dot_cloud_dot_ai_dot_files_dot_v1_dot_file__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+yandex/cloud/ai/files/v1/file_service.proto\x12\x18yandex.cloud.ai.files.v1\x1a#yandex/cloud/ai/common/common.proto\x1a#yandex/cloud/ai/files/v1/file.proto\x1a\x1dyandex/cloud/validation.proto\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\"\xb6\x02\n\x11\x43reateFileRequest\x12\x17\n\tfolder_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x11\n\tmime_type\x18\x04 \x01(\t\x12\x15\n\x07\x63ontent\x18\x05 \x01(\x0c\x42\x04\xe8\xc7\x31\x01\x12G\n\x06labels\x18\x06 \x03(\x0b\x32\x37.yandex.cloud.ai.files.v1.CreateFileRequest.LabelsEntry\x12\x43\n\x11\x65xpiration_config\x18\x07 \x01(\x0b\x32(.yandex.cloud.ai.common.ExpirationConfig\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\'\n\x0eGetFileRequest\x12\x15\n\x07\x66ile_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"*\n\x11GetFileUrlRequest\x12\x15\n\x07\x66ile_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"!\n\x12GetFileUrlResponse\x12\x0b\n\x03url\x18\x01 \x01(\t\"\xc1\x02\n\x11UpdateFileRequest\x12\x15\n\x07\x66ile_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x35\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x04\xe8\xc7\x31\x01\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x43\n\x11\x65xpiration_config\x18\x05 \x01(\x0b\x32(.yandex.cloud.ai.common.ExpirationConfig\x12G\n\x06labels\x18\x06 \x03(\x0b\x32\x37.yandex.cloud.ai.files.v1.UpdateFileRequest.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"*\n\x11\x44\x65leteFileRequest\x12\x15\n\x07\x66ile_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"\x14\n\x12\x44\x65leteFileResponse\"R\n\x10ListFilesRequest\x12\x17\n\tfolder_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x11\n\tpage_size\x18\x02 \x01(\x03\x12\x12\n\npage_token\x18\x03 \x01(\t\"[\n\x11ListFilesResponse\x12-\n\x05\x66iles\x18\x01 \x03(\x0b\x32\x1e.yandex.cloud.ai.files.v1.File\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xfb\x05\n\x0b\x46ileService\x12q\n\x06\x43reate\x12+.yandex.cloud.ai.files.v1.CreateFileRequest\x1a\x1e.yandex.cloud.ai.files.v1.File\"\x1a\x82\xd3\xe4\x93\x02\x14\"\x0f/files/v1/files:\x01*\x12r\n\x03Get\x12(.yandex.cloud.ai.files.v1.GetFileRequest\x1a\x1e.yandex.cloud.ai.files.v1.File\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/files/v1/files/{file_id}\x12\x83\x01\n\x06GetUrl\x12+.yandex.cloud.ai.files.v1.GetFileUrlRequest\x1a,.yandex.cloud.ai.files.v1.GetFileUrlResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/files/v1/files:getUrl\x12|\n\x06Update\x12+.yandex.cloud.ai.files.v1.UpdateFileRequest\x1a\x1e.yandex.cloud.ai.files.v1.File\"%\x82\xd3\xe4\x93\x02\x1f\x32\x1a/files/v1/update/{file_id}:\x01*\x12\x86\x01\n\x06\x44\x65lete\x12+.yandex.cloud.ai.files.v1.DeleteFileRequest\x1a,.yandex.cloud.ai.files.v1.DeleteFileResponse\"!\x82\xd3\xe4\x93\x02\x1b*\x19/files/v1/files/{file_id}\x12x\n\x04List\x12*.yandex.cloud.ai.files.v1.ListFilesRequest\x1a+.yandex.cloud.ai.files.v1.ListFilesResponse\"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0f/files/v1/filesBb\n\x1cyandex.cloud.api.ai.files.v1ZBgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/files/v1;filesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.ai.files.v1.file_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034yandex.cloud.api.ai.files.v1ZBgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/files/v1;files'
  _CREATEFILEREQUEST_LABELSENTRY._options = None
  _CREATEFILEREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _CREATEFILEREQUEST.fields_by_name['folder_id']._options = None
  _CREATEFILEREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001'
  _CREATEFILEREQUEST.fields_by_name['content']._options = None
  _CREATEFILEREQUEST.fields_by_name['content']._serialized_options = b'\350\3071\001'
  _GETFILEREQUEST.fields_by_name['file_id']._options = None
  _GETFILEREQUEST.fields_by_name['file_id']._serialized_options = b'\350\3071\001'
  _GETFILEURLREQUEST.fields_by_name['file_id']._options = None
  _GETFILEURLREQUEST.fields_by_name['file_id']._serialized_options = b'\350\3071\001'
  _UPDATEFILEREQUEST_LABELSENTRY._options = None
  _UPDATEFILEREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _UPDATEFILEREQUEST.fields_by_name['file_id']._options = None
  _UPDATEFILEREQUEST.fields_by_name['file_id']._serialized_options = b'\350\3071\001'
  _UPDATEFILEREQUEST.fields_by_name['update_mask']._options = None
  _UPDATEFILEREQUEST.fields_by_name['update_mask']._serialized_options = b'\350\3071\001'
  _DELETEFILEREQUEST.fields_by_name['file_id']._options = None
  _DELETEFILEREQUEST.fields_by_name['file_id']._serialized_options = b'\350\3071\001'
  _LISTFILESREQUEST.fields_by_name['folder_id']._options = None
  _LISTFILESREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001'
  _FILESERVICE.methods_by_name['Create']._options = None
  _FILESERVICE.methods_by_name['Create']._serialized_options = b'\202\323\344\223\002\024\"\017/files/v1/files:\001*'
  _FILESERVICE.methods_by_name['Get']._options = None
  _FILESERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\033\022\031/files/v1/files/{file_id}'
  _FILESERVICE.methods_by_name['GetUrl']._options = None
  _FILESERVICE.methods_by_name['GetUrl']._serialized_options = b'\202\323\344\223\002\030\022\026/files/v1/files:getUrl'
  _FILESERVICE.methods_by_name['Update']._options = None
  _FILESERVICE.methods_by_name['Update']._serialized_options = b'\202\323\344\223\002\0372\032/files/v1/update/{file_id}:\001*'
  _FILESERVICE.methods_by_name['Delete']._options = None
  _FILESERVICE.methods_by_name['Delete']._serialized_options = b'\202\323\344\223\002\033*\031/files/v1/files/{file_id}'
  _FILESERVICE.methods_by_name['List']._options = None
  _FILESERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\021\022\017/files/v1/files'
  _globals['_CREATEFILEREQUEST']._serialized_start=243
  _globals['_CREATEFILEREQUEST']._serialized_end=553
  _globals['_CREATEFILEREQUEST_LABELSENTRY']._serialized_start=508
  _globals['_CREATEFILEREQUEST_LABELSENTRY']._serialized_end=553
  _globals['_GETFILEREQUEST']._serialized_start=555
  _globals['_GETFILEREQUEST']._serialized_end=594
  _globals['_GETFILEURLREQUEST']._serialized_start=596
  _globals['_GETFILEURLREQUEST']._serialized_end=638
  _globals['_GETFILEURLRESPONSE']._serialized_start=640
  _globals['_GETFILEURLRESPONSE']._serialized_end=673
  _globals['_UPDATEFILEREQUEST']._serialized_start=676
  _globals['_UPDATEFILEREQUEST']._serialized_end=997
  _globals['_UPDATEFILEREQUEST_LABELSENTRY']._serialized_start=508
  _globals['_UPDATEFILEREQUEST_LABELSENTRY']._serialized_end=553
  _globals['_DELETEFILEREQUEST']._serialized_start=999
  _globals['_DELETEFILEREQUEST']._serialized_end=1041
  _globals['_DELETEFILERESPONSE']._serialized_start=1043
  _globals['_DELETEFILERESPONSE']._serialized_end=1063
  _globals['_LISTFILESREQUEST']._serialized_start=1065
  _globals['_LISTFILESREQUEST']._serialized_end=1147
  _globals['_LISTFILESRESPONSE']._serialized_start=1149
  _globals['_LISTFILESRESPONSE']._serialized_end=1240
  _globals['_FILESERVICE']._serialized_start=1243
  _globals['_FILESERVICE']._serialized_end=2006
# @@protoc_insertion_point(module_scope)