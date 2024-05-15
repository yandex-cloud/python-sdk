# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/iam/v1/service_control_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.iam.v1 import resource_pb2 as yandex_dot_cloud_dot_iam_dot_v1_dot_resource__pb2
from yandex.cloud.iam.v1 import service_control_pb2 as yandex_dot_cloud_dot_iam_dot_v1_dot_service__control__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1yandex/cloud/iam/v1/service_control_service.proto\x12\x13yandex.cloud.iam.v1\x1a\x1cgoogle/api/annotations.proto\x1a yandex/cloud/api/operation.proto\x1a\"yandex/cloud/iam/v1/resource.proto\x1a)yandex/cloud/iam/v1/service_control.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"l\n\x11GetServiceRequest\x12 \n\nservice_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x35\n\x08resource\x18\x02 \x01(\x0b\x32\x1d.yandex.cloud.iam.v1.ResourceB\x04\xe8\xc7\x31\x01\"\x8b\x01\n\x13ListServicesRequest\x12\x35\n\x08resource\x18\x01 \x01(\x0b\x32\x1d.yandex.cloud.iam.v1.ResourceB\x04\xe8\xc7\x31\x01\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1e\n\npage_token\x18\x03 \x01(\tB\n\x8a\xc8\x31\x06<=2000\"_\n\x14ListServicesResponse\x12.\n\x08services\x18\x01 \x03(\x0b\x32\x1c.yandex.cloud.iam.v1.Service\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"o\n\x14\x45nableServiceRequest\x12 \n\nservice_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x35\n\x08resource\x18\x02 \x01(\x0b\x32\x1d.yandex.cloud.iam.v1.ResourceB\x04\xe8\xc7\x31\x01\"\\\n\x15\x45nableServiceMetadata\x12\x12\n\nservice_id\x18\x01 \x01(\t\x12/\n\x08resource\x18\x02 \x01(\x0b\x32\x1d.yandex.cloud.iam.v1.Resource\"o\n\x14ResumeServiceRequest\x12 \n\nservice_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x35\n\x08resource\x18\x02 \x01(\x0b\x32\x1d.yandex.cloud.iam.v1.ResourceB\x04\xe8\xc7\x31\x01\"\\\n\x15ResumeServiceMetadata\x12\x12\n\nservice_id\x18\x01 \x01(\t\x12/\n\x08resource\x18\x02 \x01(\x0b\x32\x1d.yandex.cloud.iam.v1.Resource\"}\n\x13PauseServiceRequest\x12 \n\nservice_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x35\n\x08resource\x18\x02 \x01(\x0b\x32\x1d.yandex.cloud.iam.v1.ResourceB\x04\xe8\xc7\x31\x01\x12\r\n\x05\x66orce\x18\x03 \x01(\x08\"[\n\x14PauseServiceMetadata\x12\x12\n\nservice_id\x18\x01 \x01(\t\x12/\n\x08resource\x18\x02 \x01(\x0b\x32\x1d.yandex.cloud.iam.v1.Resource\"p\n\x15\x44isableServiceRequest\x12 \n\nservice_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x35\n\x08resource\x18\x02 \x01(\x0b\x32\x1d.yandex.cloud.iam.v1.ResourceB\x04\xe8\xc7\x31\x01\"]\n\x16\x44isableServiceMetadata\x12\x12\n\nservice_id\x18\x01 \x01(\t\x12/\n\x08resource\x18\x02 \x01(\x0b\x32\x1d.yandex.cloud.iam.v1.Resource2\xb6\x07\n\x15ServiceControlService\x12r\n\x03Get\x12&.yandex.cloud.iam.v1.GetServiceRequest\x1a\x1c.yandex.cloud.iam.v1.Service\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/iam/v1/services/{service_id}\x12u\n\x04List\x12(.yandex.cloud.iam.v1.ListServicesRequest\x1a).yandex.cloud.iam.v1.ListServicesResponse\"\x18\x82\xd3\xe4\x93\x02\x12\x12\x10/iam/v1/services\x12\xaa\x01\n\x06\x45nable\x12).yandex.cloud.iam.v1.EnableServiceRequest\x1a!.yandex.cloud.operation.Operation\"R\xb2\xd2* \n\x15\x45nableServiceMetadata\x12\x07Service\x82\xd3\xe4\x93\x02(\"#/iam/v1/service/{service_id}:enable:\x01*\x12\xaa\x01\n\x06Resume\x12).yandex.cloud.iam.v1.ResumeServiceRequest\x1a!.yandex.cloud.operation.Operation\"R\xb2\xd2* \n\x15ResumeServiceMetadata\x12\x07Service\x82\xd3\xe4\x93\x02(\"#/iam/v1/service/{service_id}:resume:\x01*\x12\xa6\x01\n\x05Pause\x12(.yandex.cloud.iam.v1.PauseServiceRequest\x1a!.yandex.cloud.operation.Operation\"P\xb2\xd2*\x1f\n\x14PauseServiceMetadata\x12\x07Service\x82\xd3\xe4\x93\x02\'\"\"/iam/v1/service/{service_id}:pause:\x01*\x12\xae\x01\n\x07\x44isable\x12*.yandex.cloud.iam.v1.DisableServiceRequest\x1a!.yandex.cloud.operation.Operation\"T\xb2\xd2*!\n\x16\x44isableServiceMetadata\x12\x07Service\x82\xd3\xe4\x93\x02)\"$/iam/v1/service/{service_id}:disable:\x01*BV\n\x17yandex.cloud.api.iam.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/iam/v1;iamb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.iam.v1.service_control_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027yandex.cloud.api.iam.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/iam/v1;iam'
  _globals['_GETSERVICEREQUEST'].fields_by_name['service_id']._loaded_options = None
  _globals['_GETSERVICEREQUEST'].fields_by_name['service_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_GETSERVICEREQUEST'].fields_by_name['resource']._loaded_options = None
  _globals['_GETSERVICEREQUEST'].fields_by_name['resource']._serialized_options = b'\350\3071\001'
  _globals['_LISTSERVICESREQUEST'].fields_by_name['resource']._loaded_options = None
  _globals['_LISTSERVICESREQUEST'].fields_by_name['resource']._serialized_options = b'\350\3071\001'
  _globals['_LISTSERVICESREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTSERVICESREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _globals['_LISTSERVICESREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTSERVICESREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\006<=2000'
  _globals['_ENABLESERVICEREQUEST'].fields_by_name['service_id']._loaded_options = None
  _globals['_ENABLESERVICEREQUEST'].fields_by_name['service_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_ENABLESERVICEREQUEST'].fields_by_name['resource']._loaded_options = None
  _globals['_ENABLESERVICEREQUEST'].fields_by_name['resource']._serialized_options = b'\350\3071\001'
  _globals['_RESUMESERVICEREQUEST'].fields_by_name['service_id']._loaded_options = None
  _globals['_RESUMESERVICEREQUEST'].fields_by_name['service_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_RESUMESERVICEREQUEST'].fields_by_name['resource']._loaded_options = None
  _globals['_RESUMESERVICEREQUEST'].fields_by_name['resource']._serialized_options = b'\350\3071\001'
  _globals['_PAUSESERVICEREQUEST'].fields_by_name['service_id']._loaded_options = None
  _globals['_PAUSESERVICEREQUEST'].fields_by_name['service_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_PAUSESERVICEREQUEST'].fields_by_name['resource']._loaded_options = None
  _globals['_PAUSESERVICEREQUEST'].fields_by_name['resource']._serialized_options = b'\350\3071\001'
  _globals['_DISABLESERVICEREQUEST'].fields_by_name['service_id']._loaded_options = None
  _globals['_DISABLESERVICEREQUEST'].fields_by_name['service_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_DISABLESERVICEREQUEST'].fields_by_name['resource']._loaded_options = None
  _globals['_DISABLESERVICEREQUEST'].fields_by_name['resource']._serialized_options = b'\350\3071\001'
  _globals['_SERVICECONTROLSERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_SERVICECONTROLSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\037\022\035/iam/v1/services/{service_id}'
  _globals['_SERVICECONTROLSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_SERVICECONTROLSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002\022\022\020/iam/v1/services'
  _globals['_SERVICECONTROLSERVICE'].methods_by_name['Enable']._loaded_options = None
  _globals['_SERVICECONTROLSERVICE'].methods_by_name['Enable']._serialized_options = b'\262\322* \n\025EnableServiceMetadata\022\007Service\202\323\344\223\002(\"#/iam/v1/service/{service_id}:enable:\001*'
  _globals['_SERVICECONTROLSERVICE'].methods_by_name['Resume']._loaded_options = None
  _globals['_SERVICECONTROLSERVICE'].methods_by_name['Resume']._serialized_options = b'\262\322* \n\025ResumeServiceMetadata\022\007Service\202\323\344\223\002(\"#/iam/v1/service/{service_id}:resume:\001*'
  _globals['_SERVICECONTROLSERVICE'].methods_by_name['Pause']._loaded_options = None
  _globals['_SERVICECONTROLSERVICE'].methods_by_name['Pause']._serialized_options = b'\262\322*\037\n\024PauseServiceMetadata\022\007Service\202\323\344\223\002\'\"\"/iam/v1/service/{service_id}:pause:\001*'
  _globals['_SERVICECONTROLSERVICE'].methods_by_name['Disable']._loaded_options = None
  _globals['_SERVICECONTROLSERVICE'].methods_by_name['Disable']._serialized_options = b'\262\322*!\n\026DisableServiceMetadata\022\007Service\202\323\344\223\002)\"$/iam/v1/service/{service_id}:disable:\001*'
  _globals['_GETSERVICEREQUEST']._serialized_start=288
  _globals['_GETSERVICEREQUEST']._serialized_end=396
  _globals['_LISTSERVICESREQUEST']._serialized_start=399
  _globals['_LISTSERVICESREQUEST']._serialized_end=538
  _globals['_LISTSERVICESRESPONSE']._serialized_start=540
  _globals['_LISTSERVICESRESPONSE']._serialized_end=635
  _globals['_ENABLESERVICEREQUEST']._serialized_start=637
  _globals['_ENABLESERVICEREQUEST']._serialized_end=748
  _globals['_ENABLESERVICEMETADATA']._serialized_start=750
  _globals['_ENABLESERVICEMETADATA']._serialized_end=842
  _globals['_RESUMESERVICEREQUEST']._serialized_start=844
  _globals['_RESUMESERVICEREQUEST']._serialized_end=955
  _globals['_RESUMESERVICEMETADATA']._serialized_start=957
  _globals['_RESUMESERVICEMETADATA']._serialized_end=1049
  _globals['_PAUSESERVICEREQUEST']._serialized_start=1051
  _globals['_PAUSESERVICEREQUEST']._serialized_end=1176
  _globals['_PAUSESERVICEMETADATA']._serialized_start=1178
  _globals['_PAUSESERVICEMETADATA']._serialized_end=1269
  _globals['_DISABLESERVICEREQUEST']._serialized_start=1271
  _globals['_DISABLESERVICEREQUEST']._serialized_end=1383
  _globals['_DISABLESERVICEMETADATA']._serialized_start=1385
  _globals['_DISABLESERVICEMETADATA']._serialized_end=1478
  _globals['_SERVICECONTROLSERVICE']._serialized_start=1481
  _globals['_SERVICECONTROLSERVICE']._serialized_end=2431
# @@protoc_insertion_point(module_scope)
