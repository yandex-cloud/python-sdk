# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/cloudapps/workload/v1/cloud_application.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:yandex/cloud/cloudapps/workload/v1/cloud_application.proto\x12\"yandex.cloud.cloudapps.workload.v1\x1a\x1dyandex/cloud/validation.proto\"\x84\x05\n\x10\x43loudApplication\x12\x18\n\x02id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12Q\n\x06status\x18\x02 \x01(\x0e\x32;.yandex.cloud.cloudapps.workload.v1.CloudApplication.StatusB\x04\xe8\xc7\x31\x01\x12S\n\x07\x62illing\x18\x03 \x01(\x0b\x32<.yandex.cloud.cloudapps.workload.v1.CloudApplication.BillingB\x04\xe8\xc7\x31\x01\x1a\xe1\x02\n\x07\x42illing\x12\\\n\x04type\x18\x01 \x01(\x0e\x32H.yandex.cloud.cloudapps.workload.v1.CloudApplication.Billing.BillingTypeB\x04\xe8\xc7\x31\x01\x12`\n\rsubscriptions\x18\x02 \x03(\x0b\x32I.yandex.cloud.cloudapps.workload.v1.CloudApplication.Billing.Subscription\x1a\x44\n\x0cSubscription\x12\x19\n\x0binstance_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x19\n\x0btemplate_id\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\"P\n\x0b\x42illingType\x12\x1c\n\x18\x42ILLING_TYPE_UNSPECIFIED\x10\x00\x12\x11\n\rPAY_AS_YOU_GO\x10\x01\x12\x10\n\x0cSUBSCRIPTION\x10\x02\"J\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0e\n\nPROCESSING\x10\x01\x12\x0c\n\x08\x44\x45PLOYED\x10\x02\x12\n\n\x06\x46\x41ILED\x10\x03\x42y\n&yandex.cloud.api.cloudapps.workload.v1ZOgithub.com/yandex-cloud/go-genproto/yandex/cloud/cloudapps/workload/v1;workloadb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.cloudapps.workload.v1.cloud_application_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n&yandex.cloud.api.cloudapps.workload.v1ZOgithub.com/yandex-cloud/go-genproto/yandex/cloud/cloudapps/workload/v1;workload'
  _CLOUDAPPLICATION_BILLING_SUBSCRIPTION.fields_by_name['instance_id']._options = None
  _CLOUDAPPLICATION_BILLING_SUBSCRIPTION.fields_by_name['instance_id']._serialized_options = b'\350\3071\001'
  _CLOUDAPPLICATION_BILLING_SUBSCRIPTION.fields_by_name['template_id']._options = None
  _CLOUDAPPLICATION_BILLING_SUBSCRIPTION.fields_by_name['template_id']._serialized_options = b'\350\3071\001'
  _CLOUDAPPLICATION_BILLING.fields_by_name['type']._options = None
  _CLOUDAPPLICATION_BILLING.fields_by_name['type']._serialized_options = b'\350\3071\001'
  _CLOUDAPPLICATION.fields_by_name['id']._options = None
  _CLOUDAPPLICATION.fields_by_name['id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _CLOUDAPPLICATION.fields_by_name['status']._options = None
  _CLOUDAPPLICATION.fields_by_name['status']._serialized_options = b'\350\3071\001'
  _CLOUDAPPLICATION.fields_by_name['billing']._options = None
  _CLOUDAPPLICATION.fields_by_name['billing']._serialized_options = b'\350\3071\001'
  _globals['_CLOUDAPPLICATION']._serialized_start=130
  _globals['_CLOUDAPPLICATION']._serialized_end=774
  _globals['_CLOUDAPPLICATION_BILLING']._serialized_start=345
  _globals['_CLOUDAPPLICATION_BILLING']._serialized_end=698
  _globals['_CLOUDAPPLICATION_BILLING_SUBSCRIPTION']._serialized_start=548
  _globals['_CLOUDAPPLICATION_BILLING_SUBSCRIPTION']._serialized_end=616
  _globals['_CLOUDAPPLICATION_BILLING_BILLINGTYPE']._serialized_start=618
  _globals['_CLOUDAPPLICATION_BILLING_BILLINGTYPE']._serialized_end=698
  _globals['_CLOUDAPPLICATION_STATUS']._serialized_start=700
  _globals['_CLOUDAPPLICATION_STATUS']._serialized_end=774
# @@protoc_insertion_point(module_scope)
