# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/containerregistry/v1/scan_policy_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.containerregistry.v1 import scan_policy_pb2 as yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/containerregistry/v1/scan_policy_service.proto',
  package='yandex.cloud.containerregistry.v1',
  syntax='proto3',
  serialized_options=b'\n%yandex.cloud.api.containerregistry.v1ZWgithub.com/yandex-cloud/go-genproto/yandex/cloud/containerregistry/v1;containerregistry',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n;yandex/cloud/containerregistry/v1/scan_policy_service.proto\x12!yandex.cloud.containerregistry.v1\x1a yandex/cloud/api/operation.proto\x1a\x33yandex/cloud/containerregistry/v1/scan_policy.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/api/annotations.proto\"<\n\x14GetScanPolicyRequest\x12$\n\x0escan_policy_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"C\n\x1eGetScanPolicyByRegistryRequest\x12!\n\x0bregistry_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\xca\x01\n\x17\x43reateScanPolicyRequest\x12!\n\x0bregistry_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x04name\x18\x02 \x01(\tB!\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12;\n\x05rules\x18\x04 \x01(\x0b\x32,.yandex.cloud.containerregistry.v1.ScanRules\"\xfe\x01\n\x17UpdateScanPolicyRequest\x12$\n\x0escan_policy_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12/\n\x04name\x18\x03 \x01(\tB!\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12;\n\x05rules\x18\x05 \x01(\x0b\x32,.yandex.cloud.containerregistry.v1.ScanRules\"?\n\x17\x44\x65leteScanPolicyRequest\x12$\n\x0escan_policy_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"2\n\x18\x43reateScanPolicyMetadata\x12\x16\n\x0escan_policy_id\x18\x01 \x01(\t\"2\n\x18UpdateScanPolicyMetadata\x12\x16\n\x0escan_policy_id\x18\x01 \x01(\t\"2\n\x18\x44\x65leteScanPolicyMetadata\x12\x16\n\x0escan_policy_id\x18\x01 \x01(\t2\x81\x08\n\x11ScanPolicyService\x12\xab\x01\n\x03Get\x12\x37.yandex.cloud.containerregistry.v1.GetScanPolicyRequest\x1a-.yandex.cloud.containerregistry.v1.ScanPolicy\"<\x82\xd3\xe4\x93\x02\x36\x12\x34/container-registry/v1/scanPolicies/{scan_policy_id}\x12\xc7\x01\n\rGetByRegistry\x12\x41.yandex.cloud.containerregistry.v1.GetScanPolicyByRegistryRequest\x1a-.yandex.cloud.containerregistry.v1.ScanPolicy\"D\x82\xd3\xe4\x93\x02>\x12</container-registry/v1/scanPolicies/{registry_id}:byRegistry\x12\xc1\x01\n\x06\x43reate\x12:.yandex.cloud.containerregistry.v1.CreateScanPolicyRequest\x1a!.yandex.cloud.operation.Operation\"X\x82\xd3\xe4\x93\x02(\"#/container-registry/v1/scanPolicies:\x01*\xb2\xd2*&\n\x18\x43reateScanPolicyMetadata\x12\nScanPolicy\x12\xd2\x01\n\x06Update\x12:.yandex.cloud.containerregistry.v1.UpdateScanPolicyRequest\x1a!.yandex.cloud.operation.Operation\"i\x82\xd3\xe4\x93\x02\x39\x32\x34/container-registry/v1/scanPolicies/{scan_policy_id}:\x01*\xb2\xd2*&\n\x18UpdateScanPolicyMetadata\x12\nScanPolicy\x12\xda\x01\n\x06\x44\x65lete\x12:.yandex.cloud.containerregistry.v1.DeleteScanPolicyRequest\x1a!.yandex.cloud.operation.Operation\"q\x82\xd3\xe4\x93\x02\x36*4/container-registry/v1/scanPolicies/{scan_policy_id}\xb2\xd2*1\n\x18\x44\x65leteScanPolicyMetadata\x12\x15google.protobuf.EmptyB\x80\x01\n%yandex.cloud.api.containerregistry.v1ZWgithub.com/yandex-cloud/go-genproto/yandex/cloud/containerregistry/v1;containerregistryb\x06proto3'
  ,
  dependencies=[yandex_dot_cloud_dot_api_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__pb2.DESCRIPTOR,yandex_dot_cloud_dot_operation_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_GETSCANPOLICYREQUEST = _descriptor.Descriptor(
  name='GetScanPolicyRequest',
  full_name='yandex.cloud.containerregistry.v1.GetScanPolicyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='scan_policy_id', full_name='yandex.cloud.containerregistry.v1.GetScanPolicyRequest.scan_policy_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=320,
  serialized_end=380,
)


_GETSCANPOLICYBYREGISTRYREQUEST = _descriptor.Descriptor(
  name='GetScanPolicyByRegistryRequest',
  full_name='yandex.cloud.containerregistry.v1.GetScanPolicyByRegistryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='registry_id', full_name='yandex.cloud.containerregistry.v1.GetScanPolicyByRegistryRequest.registry_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=382,
  serialized_end=449,
)


_CREATESCANPOLICYREQUEST = _descriptor.Descriptor(
  name='CreateScanPolicyRequest',
  full_name='yandex.cloud.containerregistry.v1.CreateScanPolicyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='registry_id', full_name='yandex.cloud.containerregistry.v1.CreateScanPolicyRequest.registry_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.containerregistry.v1.CreateScanPolicyRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.containerregistry.v1.CreateScanPolicyRequest.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\005<=256', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rules', full_name='yandex.cloud.containerregistry.v1.CreateScanPolicyRequest.rules', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=452,
  serialized_end=654,
)


_UPDATESCANPOLICYREQUEST = _descriptor.Descriptor(
  name='UpdateScanPolicyRequest',
  full_name='yandex.cloud.containerregistry.v1.UpdateScanPolicyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='scan_policy_id', full_name='yandex.cloud.containerregistry.v1.UpdateScanPolicyRequest.scan_policy_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='yandex.cloud.containerregistry.v1.UpdateScanPolicyRequest.update_mask', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.containerregistry.v1.UpdateScanPolicyRequest.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.containerregistry.v1.UpdateScanPolicyRequest.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\005<=256', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rules', full_name='yandex.cloud.containerregistry.v1.UpdateScanPolicyRequest.rules', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=657,
  serialized_end=911,
)


_DELETESCANPOLICYREQUEST = _descriptor.Descriptor(
  name='DeleteScanPolicyRequest',
  full_name='yandex.cloud.containerregistry.v1.DeleteScanPolicyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='scan_policy_id', full_name='yandex.cloud.containerregistry.v1.DeleteScanPolicyRequest.scan_policy_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=913,
  serialized_end=976,
)


_CREATESCANPOLICYMETADATA = _descriptor.Descriptor(
  name='CreateScanPolicyMetadata',
  full_name='yandex.cloud.containerregistry.v1.CreateScanPolicyMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='scan_policy_id', full_name='yandex.cloud.containerregistry.v1.CreateScanPolicyMetadata.scan_policy_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=978,
  serialized_end=1028,
)


_UPDATESCANPOLICYMETADATA = _descriptor.Descriptor(
  name='UpdateScanPolicyMetadata',
  full_name='yandex.cloud.containerregistry.v1.UpdateScanPolicyMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='scan_policy_id', full_name='yandex.cloud.containerregistry.v1.UpdateScanPolicyMetadata.scan_policy_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1030,
  serialized_end=1080,
)


_DELETESCANPOLICYMETADATA = _descriptor.Descriptor(
  name='DeleteScanPolicyMetadata',
  full_name='yandex.cloud.containerregistry.v1.DeleteScanPolicyMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='scan_policy_id', full_name='yandex.cloud.containerregistry.v1.DeleteScanPolicyMetadata.scan_policy_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1082,
  serialized_end=1132,
)

_CREATESCANPOLICYREQUEST.fields_by_name['rules'].message_type = yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__pb2._SCANRULES
_UPDATESCANPOLICYREQUEST.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_UPDATESCANPOLICYREQUEST.fields_by_name['rules'].message_type = yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__pb2._SCANRULES
DESCRIPTOR.message_types_by_name['GetScanPolicyRequest'] = _GETSCANPOLICYREQUEST
DESCRIPTOR.message_types_by_name['GetScanPolicyByRegistryRequest'] = _GETSCANPOLICYBYREGISTRYREQUEST
DESCRIPTOR.message_types_by_name['CreateScanPolicyRequest'] = _CREATESCANPOLICYREQUEST
DESCRIPTOR.message_types_by_name['UpdateScanPolicyRequest'] = _UPDATESCANPOLICYREQUEST
DESCRIPTOR.message_types_by_name['DeleteScanPolicyRequest'] = _DELETESCANPOLICYREQUEST
DESCRIPTOR.message_types_by_name['CreateScanPolicyMetadata'] = _CREATESCANPOLICYMETADATA
DESCRIPTOR.message_types_by_name['UpdateScanPolicyMetadata'] = _UPDATESCANPOLICYMETADATA
DESCRIPTOR.message_types_by_name['DeleteScanPolicyMetadata'] = _DELETESCANPOLICYMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetScanPolicyRequest = _reflection.GeneratedProtocolMessageType('GetScanPolicyRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSCANPOLICYREQUEST,
  '__module__' : 'yandex.cloud.containerregistry.v1.scan_policy_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.containerregistry.v1.GetScanPolicyRequest)
  })
_sym_db.RegisterMessage(GetScanPolicyRequest)

GetScanPolicyByRegistryRequest = _reflection.GeneratedProtocolMessageType('GetScanPolicyByRegistryRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSCANPOLICYBYREGISTRYREQUEST,
  '__module__' : 'yandex.cloud.containerregistry.v1.scan_policy_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.containerregistry.v1.GetScanPolicyByRegistryRequest)
  })
_sym_db.RegisterMessage(GetScanPolicyByRegistryRequest)

CreateScanPolicyRequest = _reflection.GeneratedProtocolMessageType('CreateScanPolicyRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATESCANPOLICYREQUEST,
  '__module__' : 'yandex.cloud.containerregistry.v1.scan_policy_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.containerregistry.v1.CreateScanPolicyRequest)
  })
_sym_db.RegisterMessage(CreateScanPolicyRequest)

UpdateScanPolicyRequest = _reflection.GeneratedProtocolMessageType('UpdateScanPolicyRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESCANPOLICYREQUEST,
  '__module__' : 'yandex.cloud.containerregistry.v1.scan_policy_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.containerregistry.v1.UpdateScanPolicyRequest)
  })
_sym_db.RegisterMessage(UpdateScanPolicyRequest)

DeleteScanPolicyRequest = _reflection.GeneratedProtocolMessageType('DeleteScanPolicyRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETESCANPOLICYREQUEST,
  '__module__' : 'yandex.cloud.containerregistry.v1.scan_policy_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.containerregistry.v1.DeleteScanPolicyRequest)
  })
_sym_db.RegisterMessage(DeleteScanPolicyRequest)

CreateScanPolicyMetadata = _reflection.GeneratedProtocolMessageType('CreateScanPolicyMetadata', (_message.Message,), {
  'DESCRIPTOR' : _CREATESCANPOLICYMETADATA,
  '__module__' : 'yandex.cloud.containerregistry.v1.scan_policy_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.containerregistry.v1.CreateScanPolicyMetadata)
  })
_sym_db.RegisterMessage(CreateScanPolicyMetadata)

UpdateScanPolicyMetadata = _reflection.GeneratedProtocolMessageType('UpdateScanPolicyMetadata', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESCANPOLICYMETADATA,
  '__module__' : 'yandex.cloud.containerregistry.v1.scan_policy_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.containerregistry.v1.UpdateScanPolicyMetadata)
  })
_sym_db.RegisterMessage(UpdateScanPolicyMetadata)

DeleteScanPolicyMetadata = _reflection.GeneratedProtocolMessageType('DeleteScanPolicyMetadata', (_message.Message,), {
  'DESCRIPTOR' : _DELETESCANPOLICYMETADATA,
  '__module__' : 'yandex.cloud.containerregistry.v1.scan_policy_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.containerregistry.v1.DeleteScanPolicyMetadata)
  })
_sym_db.RegisterMessage(DeleteScanPolicyMetadata)


DESCRIPTOR._options = None
_GETSCANPOLICYREQUEST.fields_by_name['scan_policy_id']._options = None
_GETSCANPOLICYBYREGISTRYREQUEST.fields_by_name['registry_id']._options = None
_CREATESCANPOLICYREQUEST.fields_by_name['registry_id']._options = None
_CREATESCANPOLICYREQUEST.fields_by_name['name']._options = None
_CREATESCANPOLICYREQUEST.fields_by_name['description']._options = None
_UPDATESCANPOLICYREQUEST.fields_by_name['scan_policy_id']._options = None
_UPDATESCANPOLICYREQUEST.fields_by_name['name']._options = None
_UPDATESCANPOLICYREQUEST.fields_by_name['description']._options = None
_DELETESCANPOLICYREQUEST.fields_by_name['scan_policy_id']._options = None

_SCANPOLICYSERVICE = _descriptor.ServiceDescriptor(
  name='ScanPolicyService',
  full_name='yandex.cloud.containerregistry.v1.ScanPolicyService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1135,
  serialized_end=2160,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='yandex.cloud.containerregistry.v1.ScanPolicyService.Get',
    index=0,
    containing_service=None,
    input_type=_GETSCANPOLICYREQUEST,
    output_type=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__pb2._SCANPOLICY,
    serialized_options=b'\202\323\344\223\0026\0224/container-registry/v1/scanPolicies/{scan_policy_id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetByRegistry',
    full_name='yandex.cloud.containerregistry.v1.ScanPolicyService.GetByRegistry',
    index=1,
    containing_service=None,
    input_type=_GETSCANPOLICYBYREGISTRYREQUEST,
    output_type=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scan__policy__pb2._SCANPOLICY,
    serialized_options=b'\202\323\344\223\002>\022</container-registry/v1/scanPolicies/{registry_id}:byRegistry',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='yandex.cloud.containerregistry.v1.ScanPolicyService.Create',
    index=2,
    containing_service=None,
    input_type=_CREATESCANPOLICYREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002(\"#/container-registry/v1/scanPolicies:\001*\262\322*&\n\030CreateScanPolicyMetadata\022\nScanPolicy',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='yandex.cloud.containerregistry.v1.ScanPolicyService.Update',
    index=3,
    containing_service=None,
    input_type=_UPDATESCANPOLICYREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002924/container-registry/v1/scanPolicies/{scan_policy_id}:\001*\262\322*&\n\030UpdateScanPolicyMetadata\022\nScanPolicy',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='yandex.cloud.containerregistry.v1.ScanPolicyService.Delete',
    index=4,
    containing_service=None,
    input_type=_DELETESCANPOLICYREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\0026*4/container-registry/v1/scanPolicies/{scan_policy_id}\262\322*1\n\030DeleteScanPolicyMetadata\022\025google.protobuf.Empty',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SCANPOLICYSERVICE)

DESCRIPTOR.services_by_name['ScanPolicyService'] = _SCANPOLICYSERVICE

# @@protoc_insertion_point(module_scope)