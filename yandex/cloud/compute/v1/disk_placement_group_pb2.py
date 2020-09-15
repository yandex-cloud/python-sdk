# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/compute/v1/disk_placement_group.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/compute/v1/disk_placement_group.proto',
  package='yandex.cloud.compute.v1',
  syntax='proto3',
  serialized_options=b'\n\033yandex.cloud.api.compute.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;compute',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n2yandex/cloud/compute/v1/disk_placement_group.proto\x12\x17yandex.cloud.compute.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\x8d\x04\n\x12\x44iskPlacementGroup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12G\n\x06labels\x18\x06 \x03(\x0b\x32\x37.yandex.cloud.compute.v1.DiskPlacementGroup.LabelsEntry\x12\x0f\n\x07zone_id\x18\x07 \x01(\t\x12\x42\n\x06status\x18\x0b \x01(\x0e\x32\x32.yandex.cloud.compute.v1.DiskPlacementGroup.Status\x12Y\n\x19spread_placement_strategy\x18\x08 \x01(\x0b\x32\x34.yandex.cloud.compute.v1.DiskSpreadPlacementStrategyH\x00\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"G\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\t\n\x05READY\x10\x02\x12\x0c\n\x08\x44\x45LETING\x10\x04\x42\x14\n\x12placement_strategy\"\x1d\n\x1b\x44iskSpreadPlacementStrategyBb\n\x1byandex.cloud.api.compute.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;computeb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])



_DISKPLACEMENTGROUP_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='yandex.cloud.compute.v1.DiskPlacementGroup.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CREATING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='READY', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DELETING', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=545,
  serialized_end=616,
)
_sym_db.RegisterEnumDescriptor(_DISKPLACEMENTGROUP_STATUS)


_DISKPLACEMENTGROUP_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='yandex.cloud.compute.v1.DiskPlacementGroup.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.compute.v1.DiskPlacementGroup.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.compute.v1.DiskPlacementGroup.LabelsEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=498,
  serialized_end=543,
)

_DISKPLACEMENTGROUP = _descriptor.Descriptor(
  name='DiskPlacementGroup',
  full_name='yandex.cloud.compute.v1.DiskPlacementGroup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.compute.v1.DiskPlacementGroup.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.compute.v1.DiskPlacementGroup.folder_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.compute.v1.DiskPlacementGroup.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.compute.v1.DiskPlacementGroup.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.compute.v1.DiskPlacementGroup.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='yandex.cloud.compute.v1.DiskPlacementGroup.labels', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='zone_id', full_name='yandex.cloud.compute.v1.DiskPlacementGroup.zone_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='yandex.cloud.compute.v1.DiskPlacementGroup.status', index=7,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='spread_placement_strategy', full_name='yandex.cloud.compute.v1.DiskPlacementGroup.spread_placement_strategy', index=8,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DISKPLACEMENTGROUP_LABELSENTRY, ],
  enum_types=[
    _DISKPLACEMENTGROUP_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='placement_strategy', full_name='yandex.cloud.compute.v1.DiskPlacementGroup.placement_strategy',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=113,
  serialized_end=638,
)


_DISKSPREADPLACEMENTSTRATEGY = _descriptor.Descriptor(
  name='DiskSpreadPlacementStrategy',
  full_name='yandex.cloud.compute.v1.DiskSpreadPlacementStrategy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=640,
  serialized_end=669,
)

_DISKPLACEMENTGROUP_LABELSENTRY.containing_type = _DISKPLACEMENTGROUP
_DISKPLACEMENTGROUP.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DISKPLACEMENTGROUP.fields_by_name['labels'].message_type = _DISKPLACEMENTGROUP_LABELSENTRY
_DISKPLACEMENTGROUP.fields_by_name['status'].enum_type = _DISKPLACEMENTGROUP_STATUS
_DISKPLACEMENTGROUP.fields_by_name['spread_placement_strategy'].message_type = _DISKSPREADPLACEMENTSTRATEGY
_DISKPLACEMENTGROUP_STATUS.containing_type = _DISKPLACEMENTGROUP
_DISKPLACEMENTGROUP.oneofs_by_name['placement_strategy'].fields.append(
  _DISKPLACEMENTGROUP.fields_by_name['spread_placement_strategy'])
_DISKPLACEMENTGROUP.fields_by_name['spread_placement_strategy'].containing_oneof = _DISKPLACEMENTGROUP.oneofs_by_name['placement_strategy']
DESCRIPTOR.message_types_by_name['DiskPlacementGroup'] = _DISKPLACEMENTGROUP
DESCRIPTOR.message_types_by_name['DiskSpreadPlacementStrategy'] = _DISKSPREADPLACEMENTSTRATEGY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DiskPlacementGroup = _reflection.GeneratedProtocolMessageType('DiskPlacementGroup', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _DISKPLACEMENTGROUP_LABELSENTRY,
    '__module__' : 'yandex.cloud.compute.v1.disk_placement_group_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.DiskPlacementGroup.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _DISKPLACEMENTGROUP,
  '__module__' : 'yandex.cloud.compute.v1.disk_placement_group_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.DiskPlacementGroup)
  })
_sym_db.RegisterMessage(DiskPlacementGroup)
_sym_db.RegisterMessage(DiskPlacementGroup.LabelsEntry)

DiskSpreadPlacementStrategy = _reflection.GeneratedProtocolMessageType('DiskSpreadPlacementStrategy', (_message.Message,), {
  'DESCRIPTOR' : _DISKSPREADPLACEMENTSTRATEGY,
  '__module__' : 'yandex.cloud.compute.v1.disk_placement_group_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.DiskSpreadPlacementStrategy)
  })
_sym_db.RegisterMessage(DiskSpreadPlacementStrategy)


DESCRIPTOR._options = None
_DISKPLACEMENTGROUP_LABELSENTRY._options = None
# @@protoc_insertion_point(module_scope)
