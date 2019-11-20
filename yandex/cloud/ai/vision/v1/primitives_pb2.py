# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/ai/vision/v1/primitives.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/ai/vision/v1/primitives.proto',
  package='yandex.cloud.ai.vision.v1',
  syntax='proto3',
  serialized_options=_b('\n\035yandex.cloud.api.ai.vision.v1ZDgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/vision/v1;vision'),
  serialized_pb=_b('\n*yandex/cloud/ai/vision/v1/primitives.proto\x12\x19yandex.cloud.ai.vision.v1\">\n\x07Polygon\x12\x33\n\x08vertices\x18\x01 \x03(\x0b\x32!.yandex.cloud.ai.vision.v1.Vertex\"\x1e\n\x06Vertex\x12\t\n\x01x\x18\x01 \x01(\x03\x12\t\n\x01y\x18\x02 \x01(\x03\x42\x65\n\x1dyandex.cloud.api.ai.vision.v1ZDgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/vision/v1;visionb\x06proto3')
)




_POLYGON = _descriptor.Descriptor(
  name='Polygon',
  full_name='yandex.cloud.ai.vision.v1.Polygon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vertices', full_name='yandex.cloud.ai.vision.v1.Polygon.vertices', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=73,
  serialized_end=135,
)


_VERTEX = _descriptor.Descriptor(
  name='Vertex',
  full_name='yandex.cloud.ai.vision.v1.Vertex',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='yandex.cloud.ai.vision.v1.Vertex.x', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='yandex.cloud.ai.vision.v1.Vertex.y', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=137,
  serialized_end=167,
)

_POLYGON.fields_by_name['vertices'].message_type = _VERTEX
DESCRIPTOR.message_types_by_name['Polygon'] = _POLYGON
DESCRIPTOR.message_types_by_name['Vertex'] = _VERTEX
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Polygon = _reflection.GeneratedProtocolMessageType('Polygon', (_message.Message,), dict(
  DESCRIPTOR = _POLYGON,
  __module__ = 'yandex.cloud.ai.vision.v1.primitives_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.ai.vision.v1.Polygon)
  ))
_sym_db.RegisterMessage(Polygon)

Vertex = _reflection.GeneratedProtocolMessageType('Vertex', (_message.Message,), dict(
  DESCRIPTOR = _VERTEX,
  __module__ = 'yandex.cloud.ai.vision.v1.primitives_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.ai.vision.v1.Vertex)
  ))
_sym_db.RegisterMessage(Vertex)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
