# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/containerregistry/v1/scanner_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.containerregistry.v1 import scanner_pb2 as yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scanner__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/containerregistry/v1/scanner_service.proto',
  package='yandex.cloud.containerregistry.v1',
  syntax='proto3',
  serialized_options=b'\n%yandex.cloud.api.containerregistry.v1ZWgithub.com/yandex-cloud/go-genproto/yandex/cloud/containerregistry/v1;containerregistry',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n7yandex/cloud/containerregistry/v1/scanner_service.proto\x12!yandex.cloud.containerregistry.v1\x1a yandex/cloud/api/operation.proto\x1a/yandex/cloud/containerregistry/v1/scanner.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\x1a\x1cgoogle/api/annotations.proto\"-\n\x0bScanRequest\x12\x1e\n\x08image_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"&\n\x0cScanMetadata\x12\x16\n\x0escan_result_id\x18\x01 \x01(\t\"<\n\x14GetScanResultRequest\x12$\n\x0escan_result_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"6\n\x18GetLastScanResultRequest\x12\x1a\n\x08image_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\"\xdc\x01\n\x16ListScanResultsRequest\x12\x1c\n\x08image_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50H\x00\x12!\n\rrepository_id\x18\x02 \x01(\tB\x08\x8a\xc8\x31\x04<=50H\x00\x12\x1d\n\tpage_size\x18\x03 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x05 \x01(\tB\n\x8a\xc8\x31\x06<=1000\x12\x1b\n\x08order_by\x18\x06 \x01(\tB\t\x8a\xc8\x31\x05<=100B\n\n\x02id\x12\x04\xc0\xc1\x31\x01\"w\n\x17ListScanResultsResponse\x12\x43\n\x0cscan_results\x18\x01 \x03(\x0b\x32-.yandex.cloud.containerregistry.v1.ScanResult\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xb9\x01\n\x1aListVulnerabilitiesRequest\x12$\n\x0escan_result_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\x12\x1b\n\x08order_by\x18\x05 \x01(\tB\t\x8a\xc8\x31\x05<=100\"\x81\x01\n\x1bListVulnerabilitiesResponse\x12I\n\x0fvulnerabilities\x18\x01 \x03(\x0b\x32\x30.yandex.cloud.containerregistry.v1.Vulnerability\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\x9b\x07\n\x0eScannerService\x12\xa0\x01\n\x04Scan\x12..yandex.cloud.containerregistry.v1.ScanRequest\x1a!.yandex.cloud.operation.Operation\"E\x82\xd3\xe4\x93\x02!\"\x1c/container-registry/v1/scans:\x01*\xb2\xd2*\x1a\n\x0cScanMetadata\x12\nScanResult\x12\xa4\x01\n\x03Get\x12\x37.yandex.cloud.containerregistry.v1.GetScanResultRequest\x1a-.yandex.cloud.containerregistry.v1.ScanResult\"5\x82\xd3\xe4\x93\x02/\x12-/container-registry/v1/scans/{scan_result_id}\x12\xb6\x01\n\x07GetLast\x12;.yandex.cloud.containerregistry.v1.GetLastScanResultRequest\x1a-.yandex.cloud.containerregistry.v1.ScanResult\"?\x82\xd3\xe4\x93\x02\x39\x12\x37/container-registry/v1/images/{image_id}:lastScanResult\x12\xa3\x01\n\x04List\x12\x39.yandex.cloud.containerregistry.v1.ListScanResultsRequest\x1a:.yandex.cloud.containerregistry.v1.ListScanResultsResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/container-registry/v1/scans\x12\xdf\x01\n\x13ListVulnerabilities\x12=.yandex.cloud.containerregistry.v1.ListVulnerabilitiesRequest\x1a>.yandex.cloud.containerregistry.v1.ListVulnerabilitiesResponse\"I\x82\xd3\xe4\x93\x02\x43\x12\x41/container-registry/v1/scans/{scan_result_id}:listVulnerabilitiesB\x80\x01\n%yandex.cloud.api.containerregistry.v1ZWgithub.com/yandex-cloud/go-genproto/yandex/cloud/containerregistry/v1;containerregistryb\x06proto3'
  ,
  dependencies=[yandex_dot_cloud_dot_api_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scanner__pb2.DESCRIPTOR,yandex_dot_cloud_dot_operation_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_SCANREQUEST = _descriptor.Descriptor(
  name='ScanRequest',
  full_name='yandex.cloud.containerregistry.v1.ScanRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='image_id', full_name='yandex.cloud.containerregistry.v1.ScanRequest.image_id', index=0,
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
  serialized_start=278,
  serialized_end=323,
)


_SCANMETADATA = _descriptor.Descriptor(
  name='ScanMetadata',
  full_name='yandex.cloud.containerregistry.v1.ScanMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='scan_result_id', full_name='yandex.cloud.containerregistry.v1.ScanMetadata.scan_result_id', index=0,
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
  serialized_start=325,
  serialized_end=363,
)


_GETSCANRESULTREQUEST = _descriptor.Descriptor(
  name='GetScanResultRequest',
  full_name='yandex.cloud.containerregistry.v1.GetScanResultRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='scan_result_id', full_name='yandex.cloud.containerregistry.v1.GetScanResultRequest.scan_result_id', index=0,
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
  serialized_start=365,
  serialized_end=425,
)


_GETLASTSCANRESULTREQUEST = _descriptor.Descriptor(
  name='GetLastScanResultRequest',
  full_name='yandex.cloud.containerregistry.v1.GetLastScanResultRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='image_id', full_name='yandex.cloud.containerregistry.v1.GetLastScanResultRequest.image_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=427,
  serialized_end=481,
)


_LISTSCANRESULTSREQUEST = _descriptor.Descriptor(
  name='ListScanResultsRequest',
  full_name='yandex.cloud.containerregistry.v1.ListScanResultsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='image_id', full_name='yandex.cloud.containerregistry.v1.ListScanResultsRequest.image_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='repository_id', full_name='yandex.cloud.containerregistry.v1.ListScanResultsRequest.repository_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='yandex.cloud.containerregistry.v1.ListScanResultsRequest.page_size', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\0060-1000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='yandex.cloud.containerregistry.v1.ListScanResultsRequest.page_token', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\005<=100', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filter', full_name='yandex.cloud.containerregistry.v1.ListScanResultsRequest.filter', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\006<=1000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order_by', full_name='yandex.cloud.containerregistry.v1.ListScanResultsRequest.order_by', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\005<=100', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
    _descriptor.OneofDescriptor(
      name='id', full_name='yandex.cloud.containerregistry.v1.ListScanResultsRequest.id',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[], serialized_options=b'\300\3011\001'),
  ],
  serialized_start=484,
  serialized_end=704,
)


_LISTSCANRESULTSRESPONSE = _descriptor.Descriptor(
  name='ListScanResultsResponse',
  full_name='yandex.cloud.containerregistry.v1.ListScanResultsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='scan_results', full_name='yandex.cloud.containerregistry.v1.ListScanResultsResponse.scan_results', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='yandex.cloud.containerregistry.v1.ListScanResultsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=706,
  serialized_end=825,
)


_LISTVULNERABILITIESREQUEST = _descriptor.Descriptor(
  name='ListVulnerabilitiesRequest',
  full_name='yandex.cloud.containerregistry.v1.ListVulnerabilitiesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='scan_result_id', full_name='yandex.cloud.containerregistry.v1.ListVulnerabilitiesRequest.scan_result_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='yandex.cloud.containerregistry.v1.ListVulnerabilitiesRequest.page_size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\0060-1000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='yandex.cloud.containerregistry.v1.ListVulnerabilitiesRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\005<=100', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filter', full_name='yandex.cloud.containerregistry.v1.ListVulnerabilitiesRequest.filter', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\006<=1000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order_by', full_name='yandex.cloud.containerregistry.v1.ListVulnerabilitiesRequest.order_by', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\005<=100', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=828,
  serialized_end=1013,
)


_LISTVULNERABILITIESRESPONSE = _descriptor.Descriptor(
  name='ListVulnerabilitiesResponse',
  full_name='yandex.cloud.containerregistry.v1.ListVulnerabilitiesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='vulnerabilities', full_name='yandex.cloud.containerregistry.v1.ListVulnerabilitiesResponse.vulnerabilities', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='yandex.cloud.containerregistry.v1.ListVulnerabilitiesResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=1016,
  serialized_end=1145,
)

_LISTSCANRESULTSREQUEST.oneofs_by_name['id'].fields.append(
  _LISTSCANRESULTSREQUEST.fields_by_name['image_id'])
_LISTSCANRESULTSREQUEST.fields_by_name['image_id'].containing_oneof = _LISTSCANRESULTSREQUEST.oneofs_by_name['id']
_LISTSCANRESULTSREQUEST.oneofs_by_name['id'].fields.append(
  _LISTSCANRESULTSREQUEST.fields_by_name['repository_id'])
_LISTSCANRESULTSREQUEST.fields_by_name['repository_id'].containing_oneof = _LISTSCANRESULTSREQUEST.oneofs_by_name['id']
_LISTSCANRESULTSRESPONSE.fields_by_name['scan_results'].message_type = yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scanner__pb2._SCANRESULT
_LISTVULNERABILITIESRESPONSE.fields_by_name['vulnerabilities'].message_type = yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scanner__pb2._VULNERABILITY
DESCRIPTOR.message_types_by_name['ScanRequest'] = _SCANREQUEST
DESCRIPTOR.message_types_by_name['ScanMetadata'] = _SCANMETADATA
DESCRIPTOR.message_types_by_name['GetScanResultRequest'] = _GETSCANRESULTREQUEST
DESCRIPTOR.message_types_by_name['GetLastScanResultRequest'] = _GETLASTSCANRESULTREQUEST
DESCRIPTOR.message_types_by_name['ListScanResultsRequest'] = _LISTSCANRESULTSREQUEST
DESCRIPTOR.message_types_by_name['ListScanResultsResponse'] = _LISTSCANRESULTSRESPONSE
DESCRIPTOR.message_types_by_name['ListVulnerabilitiesRequest'] = _LISTVULNERABILITIESREQUEST
DESCRIPTOR.message_types_by_name['ListVulnerabilitiesResponse'] = _LISTVULNERABILITIESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ScanRequest = _reflection.GeneratedProtocolMessageType('ScanRequest', (_message.Message,), {
  'DESCRIPTOR' : _SCANREQUEST,
  '__module__' : 'yandex.cloud.containerregistry.v1.scanner_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.containerregistry.v1.ScanRequest)
  })
_sym_db.RegisterMessage(ScanRequest)

ScanMetadata = _reflection.GeneratedProtocolMessageType('ScanMetadata', (_message.Message,), {
  'DESCRIPTOR' : _SCANMETADATA,
  '__module__' : 'yandex.cloud.containerregistry.v1.scanner_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.containerregistry.v1.ScanMetadata)
  })
_sym_db.RegisterMessage(ScanMetadata)

GetScanResultRequest = _reflection.GeneratedProtocolMessageType('GetScanResultRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSCANRESULTREQUEST,
  '__module__' : 'yandex.cloud.containerregistry.v1.scanner_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.containerregistry.v1.GetScanResultRequest)
  })
_sym_db.RegisterMessage(GetScanResultRequest)

GetLastScanResultRequest = _reflection.GeneratedProtocolMessageType('GetLastScanResultRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETLASTSCANRESULTREQUEST,
  '__module__' : 'yandex.cloud.containerregistry.v1.scanner_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.containerregistry.v1.GetLastScanResultRequest)
  })
_sym_db.RegisterMessage(GetLastScanResultRequest)

ListScanResultsRequest = _reflection.GeneratedProtocolMessageType('ListScanResultsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTSCANRESULTSREQUEST,
  '__module__' : 'yandex.cloud.containerregistry.v1.scanner_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.containerregistry.v1.ListScanResultsRequest)
  })
_sym_db.RegisterMessage(ListScanResultsRequest)

ListScanResultsResponse = _reflection.GeneratedProtocolMessageType('ListScanResultsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTSCANRESULTSRESPONSE,
  '__module__' : 'yandex.cloud.containerregistry.v1.scanner_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.containerregistry.v1.ListScanResultsResponse)
  })
_sym_db.RegisterMessage(ListScanResultsResponse)

ListVulnerabilitiesRequest = _reflection.GeneratedProtocolMessageType('ListVulnerabilitiesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTVULNERABILITIESREQUEST,
  '__module__' : 'yandex.cloud.containerregistry.v1.scanner_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.containerregistry.v1.ListVulnerabilitiesRequest)
  })
_sym_db.RegisterMessage(ListVulnerabilitiesRequest)

ListVulnerabilitiesResponse = _reflection.GeneratedProtocolMessageType('ListVulnerabilitiesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTVULNERABILITIESRESPONSE,
  '__module__' : 'yandex.cloud.containerregistry.v1.scanner_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.containerregistry.v1.ListVulnerabilitiesResponse)
  })
_sym_db.RegisterMessage(ListVulnerabilitiesResponse)


DESCRIPTOR._options = None
_SCANREQUEST.fields_by_name['image_id']._options = None
_GETSCANRESULTREQUEST.fields_by_name['scan_result_id']._options = None
_GETLASTSCANRESULTREQUEST.fields_by_name['image_id']._options = None
_LISTSCANRESULTSREQUEST.oneofs_by_name['id']._options = None
_LISTSCANRESULTSREQUEST.fields_by_name['image_id']._options = None
_LISTSCANRESULTSREQUEST.fields_by_name['repository_id']._options = None
_LISTSCANRESULTSREQUEST.fields_by_name['page_size']._options = None
_LISTSCANRESULTSREQUEST.fields_by_name['page_token']._options = None
_LISTSCANRESULTSREQUEST.fields_by_name['filter']._options = None
_LISTSCANRESULTSREQUEST.fields_by_name['order_by']._options = None
_LISTVULNERABILITIESREQUEST.fields_by_name['scan_result_id']._options = None
_LISTVULNERABILITIESREQUEST.fields_by_name['page_size']._options = None
_LISTVULNERABILITIESREQUEST.fields_by_name['page_token']._options = None
_LISTVULNERABILITIESREQUEST.fields_by_name['filter']._options = None
_LISTVULNERABILITIESREQUEST.fields_by_name['order_by']._options = None

_SCANNERSERVICE = _descriptor.ServiceDescriptor(
  name='ScannerService',
  full_name='yandex.cloud.containerregistry.v1.ScannerService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1148,
  serialized_end=2071,
  methods=[
  _descriptor.MethodDescriptor(
    name='Scan',
    full_name='yandex.cloud.containerregistry.v1.ScannerService.Scan',
    index=0,
    containing_service=None,
    input_type=_SCANREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002!\"\034/container-registry/v1/scans:\001*\262\322*\032\n\014ScanMetadata\022\nScanResult',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='yandex.cloud.containerregistry.v1.ScannerService.Get',
    index=1,
    containing_service=None,
    input_type=_GETSCANRESULTREQUEST,
    output_type=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scanner__pb2._SCANRESULT,
    serialized_options=b'\202\323\344\223\002/\022-/container-registry/v1/scans/{scan_result_id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetLast',
    full_name='yandex.cloud.containerregistry.v1.ScannerService.GetLast',
    index=2,
    containing_service=None,
    input_type=_GETLASTSCANRESULTREQUEST,
    output_type=yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scanner__pb2._SCANRESULT,
    serialized_options=b'\202\323\344\223\0029\0227/container-registry/v1/images/{image_id}:lastScanResult',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='yandex.cloud.containerregistry.v1.ScannerService.List',
    index=3,
    containing_service=None,
    input_type=_LISTSCANRESULTSREQUEST,
    output_type=_LISTSCANRESULTSRESPONSE,
    serialized_options=b'\202\323\344\223\002\036\022\034/container-registry/v1/scans',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListVulnerabilities',
    full_name='yandex.cloud.containerregistry.v1.ScannerService.ListVulnerabilities',
    index=4,
    containing_service=None,
    input_type=_LISTVULNERABILITIESREQUEST,
    output_type=_LISTVULNERABILITIESRESPONSE,
    serialized_options=b'\202\323\344\223\002C\022A/container-registry/v1/scans/{scan_result_id}:listVulnerabilities',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SCANNERSERVICE)

DESCRIPTOR.services_by_name['ScannerService'] = _SCANNERSERVICE

# @@protoc_insertion_point(module_scope)
