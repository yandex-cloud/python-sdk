# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/iam/v1/yandex_passport_user_account_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.iam.v1 import user_account_pb2 as yandex_dot_cloud_dot_iam_dot_v1_dot_user__account__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/iam/v1/yandex_passport_user_account_service.proto',
  package='yandex.cloud.iam.v1',
  syntax='proto3',
  serialized_options=_b('\n\027yandex.cloud.api.iam.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/iam/v1;iam'),
  serialized_pb=_b('\n>yandex/cloud/iam/v1/yandex_passport_user_account_service.proto\x12\x13yandex.cloud.iam.v1\x1a\x1cgoogle/api/annotations.proto\x1a&yandex/cloud/iam/v1/user_account.proto\x1a\x1dyandex/cloud/validation.proto\"3\n\x1cGetUserAccountByLoginRequest\x12\x13\n\x05login\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x32\xba\x01\n YandexPassportUserAccountService\x12\x95\x01\n\nGetByLogin\x12\x31.yandex.cloud.iam.v1.GetUserAccountByLoginRequest\x1a .yandex.cloud.iam.v1.UserAccount\"2\x82\xd3\xe4\x93\x02,\x12*/iam/v1/yandexPassportUserAccounts:byLoginBV\n\x17yandex.cloud.api.iam.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/iam/v1;iamb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,yandex_dot_cloud_dot_iam_dot_v1_dot_user__account__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_GETUSERACCOUNTBYLOGINREQUEST = _descriptor.Descriptor(
  name='GetUserAccountByLoginRequest',
  full_name='yandex.cloud.iam.v1.GetUserAccountByLoginRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='login', full_name='yandex.cloud.iam.v1.GetUserAccountByLoginRequest.login', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=188,
  serialized_end=239,
)

DESCRIPTOR.message_types_by_name['GetUserAccountByLoginRequest'] = _GETUSERACCOUNTBYLOGINREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetUserAccountByLoginRequest = _reflection.GeneratedProtocolMessageType('GetUserAccountByLoginRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETUSERACCOUNTBYLOGINREQUEST,
  __module__ = 'yandex.cloud.iam.v1.yandex_passport_user_account_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iam.v1.GetUserAccountByLoginRequest)
  ))
_sym_db.RegisterMessage(GetUserAccountByLoginRequest)


DESCRIPTOR._options = None
_GETUSERACCOUNTBYLOGINREQUEST.fields_by_name['login']._options = None

_YANDEXPASSPORTUSERACCOUNTSERVICE = _descriptor.ServiceDescriptor(
  name='YandexPassportUserAccountService',
  full_name='yandex.cloud.iam.v1.YandexPassportUserAccountService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=242,
  serialized_end=428,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetByLogin',
    full_name='yandex.cloud.iam.v1.YandexPassportUserAccountService.GetByLogin',
    index=0,
    containing_service=None,
    input_type=_GETUSERACCOUNTBYLOGINREQUEST,
    output_type=yandex_dot_cloud_dot_iam_dot_v1_dot_user__account__pb2._USERACCOUNT,
    serialized_options=_b('\202\323\344\223\002,\022*/iam/v1/yandexPassportUserAccounts:byLogin'),
  ),
])
_sym_db.RegisterServiceDescriptor(_YANDEXPASSPORTUSERACCOUNTSERVICE)

DESCRIPTOR.services_by_name['YandexPassportUserAccountService'] = _YANDEXPASSPORTUSERACCOUNTSERVICE

# @@protoc_insertion_point(module_scope)
