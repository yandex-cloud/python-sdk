# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/billing/v1/customer.proto
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
    'yandex/cloud/billing/v1/customer.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&yandex/cloud/billing/v1/customer.proto\x12\x17yandex.cloud.billing.v1\"2\n\x08\x43ustomer\x12\n\n\x02id\x18\x01 \x01(\t\x12\x1a\n\x12\x62illing_account_id\x18\x02 \x01(\t\"\x9b\x01\n\x0e\x43ustomerPerson\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08longname\x18\x02 \x01(\t\x12\r\n\x05phone\x18\x03 \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t\x12\x11\n\tpost_code\x18\x05 \x01(\t\x12\x14\n\x0cpost_address\x18\x06 \x01(\t\x12\x15\n\rlegal_address\x18\x07 \x01(\t\x12\x0b\n\x03tin\x18\x08 \x01(\tBb\n\x1byandex.cloud.api.billing.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/billing/v1;billingb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.billing.v1.customer_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033yandex.cloud.api.billing.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/billing/v1;billing'
  _globals['_CUSTOMER']._serialized_start=67
  _globals['_CUSTOMER']._serialized_end=117
  _globals['_CUSTOMERPERSON']._serialized_start=120
  _globals['_CUSTOMERPERSON']._serialized_end=275
# @@protoc_insertion_point(module_scope)
