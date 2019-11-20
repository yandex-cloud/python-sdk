# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/compute/v1/disk_type_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.compute.v1 import disk_type_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_disk__type__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/compute/v1/disk_type_service.proto',
  package='yandex.cloud.compute.v1',
  syntax='proto3',
  serialized_options=_b('\n\033yandex.cloud.api.compute.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;compute'),
  serialized_pb=_b('\n/yandex/cloud/compute/v1/disk_type_service.proto\x12\x17yandex.cloud.compute.v1\x1a\x1cgoogle/api/annotations.proto\x1a\'yandex/cloud/compute/v1/disk_type.proto\x1a\x1dyandex/cloud/validation.proto\"0\n\x12GetDiskTypeRequest\x12\x1a\n\x0c\x64isk_type_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"T\n\x14ListDiskTypesRequest\x12\x1d\n\tpage_size\x18\x01 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x02 \x01(\tB\t\x8a\xc8\x31\x05<=100\"g\n\x15ListDiskTypesResponse\x12\x35\n\ndisk_types\x18\x01 \x03(\x0b\x32!.yandex.cloud.compute.v1.DiskType\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\x9e\x02\n\x0f\x44iskTypeService\x12\x83\x01\n\x03Get\x12+.yandex.cloud.compute.v1.GetDiskTypeRequest\x1a!.yandex.cloud.compute.v1.DiskType\",\x82\xd3\xe4\x93\x02&\x12$/compute/v1/diskTypes/{disk_type_id}\x12\x84\x01\n\x04List\x12-.yandex.cloud.compute.v1.ListDiskTypesRequest\x1a..yandex.cloud.compute.v1.ListDiskTypesResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/compute/v1/diskTypesBb\n\x1byandex.cloud.api.compute.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;computeb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,yandex_dot_cloud_dot_compute_dot_v1_dot_disk__type__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_GETDISKTYPEREQUEST = _descriptor.Descriptor(
  name='GetDiskTypeRequest',
  full_name='yandex.cloud.compute.v1.GetDiskTypeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='disk_type_id', full_name='yandex.cloud.compute.v1.GetDiskTypeRequest.disk_type_id', index=0,
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
  serialized_start=178,
  serialized_end=226,
)


_LISTDISKTYPESREQUEST = _descriptor.Descriptor(
  name='ListDiskTypesRequest',
  full_name='yandex.cloud.compute.v1.ListDiskTypesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page_size', full_name='yandex.cloud.compute.v1.ListDiskTypesRequest.page_size', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\372\3071\006<=1000'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='yandex.cloud.compute.v1.ListDiskTypesRequest.page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3101\005<=100'), file=DESCRIPTOR),
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
  serialized_start=228,
  serialized_end=312,
)


_LISTDISKTYPESRESPONSE = _descriptor.Descriptor(
  name='ListDiskTypesResponse',
  full_name='yandex.cloud.compute.v1.ListDiskTypesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='disk_types', full_name='yandex.cloud.compute.v1.ListDiskTypesResponse.disk_types', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='yandex.cloud.compute.v1.ListDiskTypesResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=314,
  serialized_end=417,
)

_LISTDISKTYPESRESPONSE.fields_by_name['disk_types'].message_type = yandex_dot_cloud_dot_compute_dot_v1_dot_disk__type__pb2._DISKTYPE
DESCRIPTOR.message_types_by_name['GetDiskTypeRequest'] = _GETDISKTYPEREQUEST
DESCRIPTOR.message_types_by_name['ListDiskTypesRequest'] = _LISTDISKTYPESREQUEST
DESCRIPTOR.message_types_by_name['ListDiskTypesResponse'] = _LISTDISKTYPESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetDiskTypeRequest = _reflection.GeneratedProtocolMessageType('GetDiskTypeRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETDISKTYPEREQUEST,
  __module__ = 'yandex.cloud.compute.v1.disk_type_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.GetDiskTypeRequest)
  ))
_sym_db.RegisterMessage(GetDiskTypeRequest)

ListDiskTypesRequest = _reflection.GeneratedProtocolMessageType('ListDiskTypesRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTDISKTYPESREQUEST,
  __module__ = 'yandex.cloud.compute.v1.disk_type_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.ListDiskTypesRequest)
  ))
_sym_db.RegisterMessage(ListDiskTypesRequest)

ListDiskTypesResponse = _reflection.GeneratedProtocolMessageType('ListDiskTypesResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTDISKTYPESRESPONSE,
  __module__ = 'yandex.cloud.compute.v1.disk_type_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.ListDiskTypesResponse)
  ))
_sym_db.RegisterMessage(ListDiskTypesResponse)


DESCRIPTOR._options = None
_GETDISKTYPEREQUEST.fields_by_name['disk_type_id']._options = None
_LISTDISKTYPESREQUEST.fields_by_name['page_size']._options = None
_LISTDISKTYPESREQUEST.fields_by_name['page_token']._options = None

_DISKTYPESERVICE = _descriptor.ServiceDescriptor(
  name='DiskTypeService',
  full_name='yandex.cloud.compute.v1.DiskTypeService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=420,
  serialized_end=706,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='yandex.cloud.compute.v1.DiskTypeService.Get',
    index=0,
    containing_service=None,
    input_type=_GETDISKTYPEREQUEST,
    output_type=yandex_dot_cloud_dot_compute_dot_v1_dot_disk__type__pb2._DISKTYPE,
    serialized_options=_b('\202\323\344\223\002&\022$/compute/v1/diskTypes/{disk_type_id}'),
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='yandex.cloud.compute.v1.DiskTypeService.List',
    index=1,
    containing_service=None,
    input_type=_LISTDISKTYPESREQUEST,
    output_type=_LISTDISKTYPESRESPONSE,
    serialized_options=_b('\202\323\344\223\002\027\022\025/compute/v1/diskTypes'),
  ),
])
_sym_db.RegisterServiceDescriptor(_DISKTYPESERVICE)

DESCRIPTOR.services_by_name['DiskTypeService'] = _DISKTYPESERVICE

# @@protoc_insertion_point(module_scope)
