# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/iam/v1/refresh_token_service.proto
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
    'yandex/cloud/iam/v1/refresh_token_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.iam.v1 import refresh_token_pb2 as yandex_dot_cloud_dot_iam_dot_v1_dot_refresh__token__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/yandex/cloud/iam/v1/refresh_token_service.proto\x12\x13yandex.cloud.iam.v1\x1a\x1cgoogle/api/annotations.proto\x1a yandex/cloud/api/operation.proto\x1a\'yandex/cloud/iam/v1/refresh_token.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"K\n\x1aRevokeRefreshTokenMetadata\x12\x12\n\nsubject_id\x18\x01 \x01(\t\x12\x19\n\x11refresh_token_ids\x18\x02 \x03(\t\"\x9f\x01\n\x18ListRefreshTokensRequest\x12\x1c\n\nsubject_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x04 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1e\n\npage_token\x18\x05 \x01(\tB\n\x8a\xc8\x31\x06<=2000\x12\x1a\n\x06\x66ilter\x18\x06 \x01(\tB\n\x8a\xc8\x31\x06<=1000J\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04\"o\n\x19ListRefreshTokensResponse\x12\x39\n\x0erefresh_tokens\x18\x01 \x03(\x0b\x32!.yandex.cloud.iam.v1.RefreshToken\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xb2\x01\n\x19RevokeRefreshTokenRequest\x12$\n\x10refresh_token_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50H\x00\x12#\n\rrefresh_token\x18\x02 \x01(\tB\n\x8a\xc8\x31\x06<=1000H\x00\x12:\n\rrevoke_filter\x18\x03 \x01(\x0b\x32!.yandex.cloud.iam.v1.RevokeFilterH\x00\x42\x0e\n\x06\x66ilter\x12\x04\xc0\xc1\x31\x01\"y\n\x0cRevokeFilter\x12\x1b\n\tclient_id\x18\x02 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x1c\n\nsubject_id\x18\x03 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12(\n\x14\x63lient_instance_info\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000J\x04\x08\x01\x10\x02\"7\n\x1aRevokeRefreshTokenResponse\x12\x19\n\x11refresh_token_ids\x18\x01 \x03(\t2\xdf\x02\n\x13RefreshTokenService\x12\x84\x01\n\x04List\x12-.yandex.cloud.iam.v1.ListRefreshTokensRequest\x1a..yandex.cloud.iam.v1.ListRefreshTokensResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/iam/v1/refreshTokens\x12\xc0\x01\n\x06Revoke\x12..yandex.cloud.iam.v1.RevokeRefreshTokenRequest\x1a!.yandex.cloud.operation.Operation\"c\xb2\xd2*8\n\x1aRevokeRefreshTokenMetadata\x12\x1aRevokeRefreshTokenResponse\x82\xd3\xe4\x93\x02!\"\x1c/iam/v1/refreshTokens:revoke:\x01*BV\n\x17yandex.cloud.api.iam.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/iam/v1;iamb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.iam.v1.refresh_token_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027yandex.cloud.api.iam.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/iam/v1;iam'
  _globals['_LISTREFRESHTOKENSREQUEST'].fields_by_name['subject_id']._loaded_options = None
  _globals['_LISTREFRESHTOKENSREQUEST'].fields_by_name['subject_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_LISTREFRESHTOKENSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTREFRESHTOKENSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _globals['_LISTREFRESHTOKENSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTREFRESHTOKENSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\006<=2000'
  _globals['_LISTREFRESHTOKENSREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTREFRESHTOKENSREQUEST'].fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _globals['_REVOKEREFRESHTOKENREQUEST'].oneofs_by_name['filter']._loaded_options = None
  _globals['_REVOKEREFRESHTOKENREQUEST'].oneofs_by_name['filter']._serialized_options = b'\300\3011\001'
  _globals['_REVOKEREFRESHTOKENREQUEST'].fields_by_name['refresh_token_id']._loaded_options = None
  _globals['_REVOKEREFRESHTOKENREQUEST'].fields_by_name['refresh_token_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_REVOKEREFRESHTOKENREQUEST'].fields_by_name['refresh_token']._loaded_options = None
  _globals['_REVOKEREFRESHTOKENREQUEST'].fields_by_name['refresh_token']._serialized_options = b'\212\3101\006<=1000'
  _globals['_REVOKEFILTER'].fields_by_name['client_id']._loaded_options = None
  _globals['_REVOKEFILTER'].fields_by_name['client_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_REVOKEFILTER'].fields_by_name['subject_id']._loaded_options = None
  _globals['_REVOKEFILTER'].fields_by_name['subject_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_REVOKEFILTER'].fields_by_name['client_instance_info']._loaded_options = None
  _globals['_REVOKEFILTER'].fields_by_name['client_instance_info']._serialized_options = b'\212\3101\006<=1000'
  _globals['_REFRESHTOKENSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_REFRESHTOKENSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002\027\022\025/iam/v1/refreshTokens'
  _globals['_REFRESHTOKENSERVICE'].methods_by_name['Revoke']._loaded_options = None
  _globals['_REFRESHTOKENSERVICE'].methods_by_name['Revoke']._serialized_options = b'\262\322*8\n\032RevokeRefreshTokenMetadata\022\032RevokeRefreshTokenResponse\202\323\344\223\002!\"\034/iam/v1/refreshTokens:revoke:\001*'
  _globals['_REVOKEREFRESHTOKENMETADATA']._serialized_start=248
  _globals['_REVOKEREFRESHTOKENMETADATA']._serialized_end=323
  _globals['_LISTREFRESHTOKENSREQUEST']._serialized_start=326
  _globals['_LISTREFRESHTOKENSREQUEST']._serialized_end=485
  _globals['_LISTREFRESHTOKENSRESPONSE']._serialized_start=487
  _globals['_LISTREFRESHTOKENSRESPONSE']._serialized_end=598
  _globals['_REVOKEREFRESHTOKENREQUEST']._serialized_start=601
  _globals['_REVOKEREFRESHTOKENREQUEST']._serialized_end=779
  _globals['_REVOKEFILTER']._serialized_start=781
  _globals['_REVOKEFILTER']._serialized_end=902
  _globals['_REVOKEREFRESHTOKENRESPONSE']._serialized_start=904
  _globals['_REVOKEREFRESHTOKENRESPONSE']._serialized_end=959
  _globals['_REFRESHTOKENSERVICE']._serialized_start=962
  _globals['_REFRESHTOKENSERVICE']._serialized_end=1313
# @@protoc_insertion_point(module_scope)
