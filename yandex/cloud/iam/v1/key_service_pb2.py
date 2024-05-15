# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/iam/v1/key_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.iam.v1 import key_pb2 as yandex_dot_cloud_dot_iam_dot_v1_dot_key__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%yandex/cloud/iam/v1/key_service.proto\x12\x13yandex.cloud.iam.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x1dyandex/cloud/iam/v1/key.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"]\n\rGetKeyRequest\x12\x1c\n\x06key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12.\n\x06\x66ormat\x18\x02 \x01(\x0e\x32\x1e.yandex.cloud.iam.v1.KeyFormat\"\xa6\x01\n\x0fListKeysRequest\x12.\n\x06\x66ormat\x18\x01 \x01(\x0e\x32\x1e.yandex.cloud.iam.v1.KeyFormat\x12$\n\x12service_account_id\x18\x02 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x03 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1e\n\npage_token\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=2000\"S\n\x10ListKeysResponse\x12&\n\x04keys\x18\x01 \x03(\x0b\x32\x18.yandex.cloud.iam.v1.Key\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xc3\x01\n\x10\x43reateKeyRequest\x12$\n\x12service_account_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x1e\n\x0b\x64\x65scription\x18\x02 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12.\n\x06\x66ormat\x18\x03 \x01(\x0e\x32\x1e.yandex.cloud.iam.v1.KeyFormat\x12\x39\n\rkey_algorithm\x18\x04 \x01(\x0e\x32\".yandex.cloud.iam.v1.Key.Algorithm\"O\n\x11\x43reateKeyResponse\x12%\n\x03key\x18\x01 \x01(\x0b\x32\x18.yandex.cloud.iam.v1.Key\x12\x13\n\x0bprivate_key\x18\x02 \x01(\t\"\x81\x01\n\x10UpdateKeyRequest\x12\x1c\n\x06key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\"#\n\x11UpdateKeyMetadata\x12\x0e\n\x06key_id\x18\x01 \x01(\t\"0\n\x10\x44\x65leteKeyRequest\x12\x1c\n\x06key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"#\n\x11\x44\x65leteKeyMetadata\x12\x0e\n\x06key_id\x18\x01 \x01(\t\"w\n\x18ListKeyOperationsRequest\x12\x1c\n\x06key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1e\n\npage_token\x18\x03 \x01(\tB\n\x8a\xc8\x31\x06<=2000\"k\n\x19ListKeyOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t*\x19\n\tKeyFormat\x12\x0c\n\x08PEM_FILE\x10\x00\x32\x9e\x06\n\nKeyService\x12\x62\n\x03Get\x12\".yandex.cloud.iam.v1.GetKeyRequest\x1a\x18.yandex.cloud.iam.v1.Key\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/iam/v1/keys/{key_id}\x12i\n\x04List\x12$.yandex.cloud.iam.v1.ListKeysRequest\x1a%.yandex.cloud.iam.v1.ListKeysResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/iam/v1/keys\x12p\n\x06\x43reate\x12%.yandex.cloud.iam.v1.CreateKeyRequest\x1a&.yandex.cloud.iam.v1.CreateKeyResponse\"\x17\x82\xd3\xe4\x93\x02\x11\"\x0c/iam/v1/keys:\x01*\x12\x90\x01\n\x06Update\x12%.yandex.cloud.iam.v1.UpdateKeyRequest\x1a!.yandex.cloud.operation.Operation\"<\xb2\xd2*\x18\n\x11UpdateKeyMetadata\x12\x03Key\x82\xd3\xe4\x93\x02\x1a\x32\x15/iam/v1/keys/{key_id}:\x01*\x12\x9f\x01\n\x06\x44\x65lete\x12%.yandex.cloud.iam.v1.DeleteKeyRequest\x1a!.yandex.cloud.operation.Operation\"K\xb2\xd2**\n\x11\x44\x65leteKeyMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x17*\x15/iam/v1/keys/{key_id}\x12\x99\x01\n\x0eListOperations\x12-.yandex.cloud.iam.v1.ListKeyOperationsRequest\x1a..yandex.cloud.iam.v1.ListKeyOperationsResponse\"(\x82\xd3\xe4\x93\x02\"\x12 /iam/v1/keys/{key_id}/operationsBV\n\x17yandex.cloud.api.iam.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/iam/v1;iamb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.iam.v1.key_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027yandex.cloud.api.iam.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/iam/v1;iam'
  _GETKEYREQUEST.fields_by_name['key_id']._options = None
  _GETKEYREQUEST.fields_by_name['key_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTKEYSREQUEST.fields_by_name['service_account_id']._options = None
  _LISTKEYSREQUEST.fields_by_name['service_account_id']._serialized_options = b'\212\3101\004<=50'
  _LISTKEYSREQUEST.fields_by_name['page_size']._options = None
  _LISTKEYSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTKEYSREQUEST.fields_by_name['page_token']._options = None
  _LISTKEYSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\006<=2000'
  _CREATEKEYREQUEST.fields_by_name['service_account_id']._options = None
  _CREATEKEYREQUEST.fields_by_name['service_account_id']._serialized_options = b'\212\3101\004<=50'
  _CREATEKEYREQUEST.fields_by_name['description']._options = None
  _CREATEKEYREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _UPDATEKEYREQUEST.fields_by_name['key_id']._options = None
  _UPDATEKEYREQUEST.fields_by_name['key_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _UPDATEKEYREQUEST.fields_by_name['description']._options = None
  _UPDATEKEYREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _DELETEKEYREQUEST.fields_by_name['key_id']._options = None
  _DELETEKEYREQUEST.fields_by_name['key_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTKEYOPERATIONSREQUEST.fields_by_name['key_id']._options = None
  _LISTKEYOPERATIONSREQUEST.fields_by_name['key_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTKEYOPERATIONSREQUEST.fields_by_name['page_size']._options = None
  _LISTKEYOPERATIONSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _LISTKEYOPERATIONSREQUEST.fields_by_name['page_token']._options = None
  _LISTKEYOPERATIONSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\006<=2000'
  _KEYSERVICE.methods_by_name['Get']._options = None
  _KEYSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\027\022\025/iam/v1/keys/{key_id}'
  _KEYSERVICE.methods_by_name['List']._options = None
  _KEYSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\016\022\014/iam/v1/keys'
  _KEYSERVICE.methods_by_name['Create']._options = None
  _KEYSERVICE.methods_by_name['Create']._serialized_options = b'\202\323\344\223\002\021\"\014/iam/v1/keys:\001*'
  _KEYSERVICE.methods_by_name['Update']._options = None
  _KEYSERVICE.methods_by_name['Update']._serialized_options = b'\262\322*\030\n\021UpdateKeyMetadata\022\003Key\202\323\344\223\002\0322\025/iam/v1/keys/{key_id}:\001*'
  _KEYSERVICE.methods_by_name['Delete']._options = None
  _KEYSERVICE.methods_by_name['Delete']._serialized_options = b'\262\322**\n\021DeleteKeyMetadata\022\025google.protobuf.Empty\202\323\344\223\002\027*\025/iam/v1/keys/{key_id}'
  _KEYSERVICE.methods_by_name['ListOperations']._options = None
  _KEYSERVICE.methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\002\"\022 /iam/v1/keys/{key_id}/operations'
  _globals['_KEYFORMAT']._serialized_start=1376
  _globals['_KEYFORMAT']._serialized_end=1401
  _globals['_GETKEYREQUEST']._serialized_start=262
  _globals['_GETKEYREQUEST']._serialized_end=355
  _globals['_LISTKEYSREQUEST']._serialized_start=358
  _globals['_LISTKEYSREQUEST']._serialized_end=524
  _globals['_LISTKEYSRESPONSE']._serialized_start=526
  _globals['_LISTKEYSRESPONSE']._serialized_end=609
  _globals['_CREATEKEYREQUEST']._serialized_start=612
  _globals['_CREATEKEYREQUEST']._serialized_end=807
  _globals['_CREATEKEYRESPONSE']._serialized_start=809
  _globals['_CREATEKEYRESPONSE']._serialized_end=888
  _globals['_UPDATEKEYREQUEST']._serialized_start=891
  _globals['_UPDATEKEYREQUEST']._serialized_end=1020
  _globals['_UPDATEKEYMETADATA']._serialized_start=1022
  _globals['_UPDATEKEYMETADATA']._serialized_end=1057
  _globals['_DELETEKEYREQUEST']._serialized_start=1059
  _globals['_DELETEKEYREQUEST']._serialized_end=1107
  _globals['_DELETEKEYMETADATA']._serialized_start=1109
  _globals['_DELETEKEYMETADATA']._serialized_end=1144
  _globals['_LISTKEYOPERATIONSREQUEST']._serialized_start=1146
  _globals['_LISTKEYOPERATIONSREQUEST']._serialized_end=1265
  _globals['_LISTKEYOPERATIONSRESPONSE']._serialized_start=1267
  _globals['_LISTKEYOPERATIONSRESPONSE']._serialized_end=1374
  _globals['_KEYSERVICE']._serialized_start=1404
  _globals['_KEYSERVICE']._serialized_end=2202
# @@protoc_insertion_point(module_scope)
