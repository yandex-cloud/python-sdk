# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/billing/v1/budget_service.proto
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
    'yandex/cloud/billing/v1/budget_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.billing.v1 import budget_pb2 as yandex_dot_cloud_dot_billing_dot_v1_dot_budget__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,yandex/cloud/billing/v1/budget_service.proto\x12\x17yandex.cloud.billing.v1\x1a\x1cgoogle/api/annotations.proto\x1a$yandex/cloud/billing/v1/budget.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\",\n\x10GetBudgetRequest\x12\x18\n\x02id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"|\n\x12ListBudgetsRequest\x12(\n\x12\x62illing_account_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"`\n\x13ListBudgetsResponse\x12\x30\n\x07\x62udgets\x18\x01 \x03(\x0b\x32\x1f.yandex.cloud.billing.v1.Budget\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xc3\x02\n\x13\x43reateBudgetRequest\x12(\n\x12\x62illing_account_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x12\n\x04name\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x43\n\x10\x63ost_budget_spec\x18\x03 \x01(\x0b\x32\'.yandex.cloud.billing.v1.CostBudgetSpecH\x00\x12I\n\x13\x65xpense_budget_spec\x18\x04 \x01(\x0b\x32*.yandex.cloud.billing.v1.ExpenseBudgetSpecH\x00\x12I\n\x13\x62\x61lance_budget_spec\x18\x05 \x01(\x0b\x32*.yandex.cloud.billing.v1.BalanceBudgetSpecH\x00\x42\x13\n\x0b\x62udget_spec\x12\x04\xc0\xc1\x31\x01\")\n\x14\x43reateBudgetMetadata\x12\x11\n\tbudget_id\x18\x01 \x01(\t2\xa2\x03\n\rBudgetService\x12s\n\x03Get\x12).yandex.cloud.billing.v1.GetBudgetRequest\x1a\x1f.yandex.cloud.billing.v1.Budget\" \x82\xd3\xe4\x93\x02\x1a\x12\x18/billing/v1/budgets/{id}\x12~\n\x04List\x12+.yandex.cloud.billing.v1.ListBudgetsRequest\x1a,.yandex.cloud.billing.v1.ListBudgetsResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\x12\x13/billing/v1/budgets\x12\x9b\x01\n\x06\x43reate\x12,.yandex.cloud.billing.v1.CreateBudgetRequest\x1a!.yandex.cloud.operation.Operation\"@\xb2\xd2*\x1e\n\x14\x43reateBudgetMetadata\x12\x06\x42udget\x82\xd3\xe4\x93\x02\x18\"\x13/billing/v1/budgets:\x01*Bb\n\x1byandex.cloud.api.billing.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/billing/v1;billingb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.billing.v1.budget_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033yandex.cloud.api.billing.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/billing/v1;billing'
  _globals['_GETBUDGETREQUEST'].fields_by_name['id']._loaded_options = None
  _globals['_GETBUDGETREQUEST'].fields_by_name['id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTBUDGETSREQUEST'].fields_by_name['billing_account_id']._loaded_options = None
  _globals['_LISTBUDGETSREQUEST'].fields_by_name['billing_account_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTBUDGETSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTBUDGETSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTBUDGETSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTBUDGETSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_CREATEBUDGETREQUEST'].oneofs_by_name['budget_spec']._loaded_options = None
  _globals['_CREATEBUDGETREQUEST'].oneofs_by_name['budget_spec']._serialized_options = b'\300\3011\001'
  _globals['_CREATEBUDGETREQUEST'].fields_by_name['billing_account_id']._loaded_options = None
  _globals['_CREATEBUDGETREQUEST'].fields_by_name['billing_account_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_CREATEBUDGETREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_CREATEBUDGETREQUEST'].fields_by_name['name']._serialized_options = b'\350\3071\001'
  _globals['_BUDGETSERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_BUDGETSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\032\022\030/billing/v1/budgets/{id}'
  _globals['_BUDGETSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_BUDGETSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002\025\022\023/billing/v1/budgets'
  _globals['_BUDGETSERVICE'].methods_by_name['Create']._loaded_options = None
  _globals['_BUDGETSERVICE'].methods_by_name['Create']._serialized_options = b'\262\322*\036\n\024CreateBudgetMetadata\022\006Budget\202\323\344\223\002\030\"\023/billing/v1/budgets:\001*'
  _globals['_GETBUDGETREQUEST']._serialized_start=246
  _globals['_GETBUDGETREQUEST']._serialized_end=290
  _globals['_LISTBUDGETSREQUEST']._serialized_start=292
  _globals['_LISTBUDGETSREQUEST']._serialized_end=416
  _globals['_LISTBUDGETSRESPONSE']._serialized_start=418
  _globals['_LISTBUDGETSRESPONSE']._serialized_end=514
  _globals['_CREATEBUDGETREQUEST']._serialized_start=517
  _globals['_CREATEBUDGETREQUEST']._serialized_end=840
  _globals['_CREATEBUDGETMETADATA']._serialized_start=842
  _globals['_CREATEBUDGETMETADATA']._serialized_end=883
  _globals['_BUDGETSERVICE']._serialized_start=886
  _globals['_BUDGETSERVICE']._serialized_end=1304
# @@protoc_insertion_point(module_scope)
