# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/compute/v1/disk_type.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/compute/v1/disk_type.proto',
  package='yandex.cloud.compute.v1',
  syntax='proto3',
  serialized_options=_b('\n\033yandex.cloud.api.compute.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;compute'),
  serialized_pb=_b('\n\'yandex/cloud/compute/v1/disk_type.proto\x12\x17yandex.cloud.compute.v1\"=\n\x08\x44iskType\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x10\n\x08zone_ids\x18\x03 \x03(\tBb\n\x1byandex.cloud.api.compute.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;computeb\x06proto3')
)




_DISKTYPE = _descriptor.Descriptor(
  name='DiskType',
  full_name='yandex.cloud.compute.v1.DiskType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.compute.v1.DiskType.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.compute.v1.DiskType.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zone_ids', full_name='yandex.cloud.compute.v1.DiskType.zone_ids', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=68,
  serialized_end=129,
)

DESCRIPTOR.message_types_by_name['DiskType'] = _DISKTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DiskType = _reflection.GeneratedProtocolMessageType('DiskType', (_message.Message,), dict(
  DESCRIPTOR = _DISKTYPE,
  __module__ = 'yandex.cloud.compute.v1.disk_type_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.DiskType)
  ))
_sym_db.RegisterMessage(DiskType)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
