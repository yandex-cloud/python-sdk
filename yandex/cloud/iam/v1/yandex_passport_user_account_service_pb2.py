# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/iam/v1/yandex_passport_user_account_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.iam.v1 import user_account_pb2 as yandex_dot_cloud_dot_iam_dot_v1_dot_user__account__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>yandex/cloud/iam/v1/yandex_passport_user_account_service.proto\x12\x13yandex.cloud.iam.v1\x1a\x1cgoogle/api/annotations.proto\x1a&yandex/cloud/iam/v1/user_account.proto\x1a\x1dyandex/cloud/validation.proto\"3\n\x1cGetUserAccountByLoginRequest\x12\x13\n\x05login\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x32\xba\x01\n YandexPassportUserAccountService\x12\x95\x01\n\nGetByLogin\x12\x31.yandex.cloud.iam.v1.GetUserAccountByLoginRequest\x1a .yandex.cloud.iam.v1.UserAccount\"2\x82\xd3\xe4\x93\x02,\x12*/iam/v1/yandexPassportUserAccounts:byLoginBV\n\x17yandex.cloud.api.iam.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/iam/v1;iamb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.iam.v1.yandex_passport_user_account_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027yandex.cloud.api.iam.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/iam/v1;iam'
  _GETUSERACCOUNTBYLOGINREQUEST.fields_by_name['login']._options = None
  _GETUSERACCOUNTBYLOGINREQUEST.fields_by_name['login']._serialized_options = b'\350\3071\001'
  _YANDEXPASSPORTUSERACCOUNTSERVICE.methods_by_name['GetByLogin']._options = None
  _YANDEXPASSPORTUSERACCOUNTSERVICE.methods_by_name['GetByLogin']._serialized_options = b'\202\323\344\223\002,\022*/iam/v1/yandexPassportUserAccounts:byLogin'
  _globals['_GETUSERACCOUNTBYLOGINREQUEST']._serialized_start=188
  _globals['_GETUSERACCOUNTBYLOGINREQUEST']._serialized_end=239
  _globals['_YANDEXPASSPORTUSERACCOUNTSERVICE']._serialized_start=242
  _globals['_YANDEXPASSPORTUSERACCOUNTSERVICE']._serialized_end=428
# @@protoc_insertion_point(module_scope)
