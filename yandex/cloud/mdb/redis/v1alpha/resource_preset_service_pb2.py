# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/redis/v1alpha/resource_preset_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.mdb.redis.v1alpha import resource_preset_pb2 as yandex_dot_cloud_dot_mdb_dot_redis_dot_v1alpha_dot_resource__preset__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/mdb/redis/v1alpha/resource_preset_service.proto',
  package='yandex.cloud.mdb.redis.v1alpha',
  syntax='proto3',
  serialized_options=_b('ZHgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/redis/v1alpha;redis'),
  serialized_pb=_b('\n<yandex/cloud/mdb/redis/v1alpha/resource_preset_service.proto\x12\x1eyandex.cloud.mdb.redis.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x34yandex/cloud/mdb/redis/v1alpha/resource_preset.proto\x1a\x1dyandex/cloud/validation.proto\"<\n\x18GetResourcePresetRequest\x12 \n\x12resource_preset_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"C\n\x1aListResourcePresetsRequest\x12\x11\n\tpage_size\x18\x02 \x01(\x03\x12\x12\n\npage_token\x18\x03 \x01(\t\"\x80\x01\n\x1bListResourcePresetsResponse\x12H\n\x10resource_presets\x18\x01 \x03(\x0b\x32..yandex.cloud.mdb.redis.v1alpha.ResourcePreset\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\x80\x03\n\x15ResourcePresetService\x12\xb4\x01\n\x03Get\x12\x38.yandex.cloud.mdb.redis.v1alpha.GetResourcePresetRequest\x1a..yandex.cloud.mdb.redis.v1alpha.ResourcePreset\"C\x82\xd3\xe4\x93\x02=\x12;/managed-redis/v1alpha/resourcePresets/{resource_preset_id}\x12\xaf\x01\n\x04List\x12:.yandex.cloud.mdb.redis.v1alpha.ListResourcePresetsRequest\x1a;.yandex.cloud.mdb.redis.v1alpha.ListResourcePresetsResponse\".\x82\xd3\xe4\x93\x02(\x12&/managed-redis/v1alpha/resourcePresetsBJZHgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/redis/v1alpha;redisb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,yandex_dot_cloud_dot_mdb_dot_redis_dot_v1alpha_dot_resource__preset__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_GETRESOURCEPRESETREQUEST = _descriptor.Descriptor(
  name='GetResourcePresetRequest',
  full_name='yandex.cloud.mdb.redis.v1alpha.GetResourcePresetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_preset_id', full_name='yandex.cloud.mdb.redis.v1alpha.GetResourcePresetRequest.resource_preset_id', index=0,
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
  serialized_start=211,
  serialized_end=271,
)


_LISTRESOURCEPRESETSREQUEST = _descriptor.Descriptor(
  name='ListResourcePresetsRequest',
  full_name='yandex.cloud.mdb.redis.v1alpha.ListResourcePresetsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page_size', full_name='yandex.cloud.mdb.redis.v1alpha.ListResourcePresetsRequest.page_size', index=0,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='yandex.cloud.mdb.redis.v1alpha.ListResourcePresetsRequest.page_token', index=1,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=273,
  serialized_end=340,
)


_LISTRESOURCEPRESETSRESPONSE = _descriptor.Descriptor(
  name='ListResourcePresetsResponse',
  full_name='yandex.cloud.mdb.redis.v1alpha.ListResourcePresetsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_presets', full_name='yandex.cloud.mdb.redis.v1alpha.ListResourcePresetsResponse.resource_presets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='yandex.cloud.mdb.redis.v1alpha.ListResourcePresetsResponse.next_page_token', index=1,
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
  serialized_start=343,
  serialized_end=471,
)

_LISTRESOURCEPRESETSRESPONSE.fields_by_name['resource_presets'].message_type = yandex_dot_cloud_dot_mdb_dot_redis_dot_v1alpha_dot_resource__preset__pb2._RESOURCEPRESET
DESCRIPTOR.message_types_by_name['GetResourcePresetRequest'] = _GETRESOURCEPRESETREQUEST
DESCRIPTOR.message_types_by_name['ListResourcePresetsRequest'] = _LISTRESOURCEPRESETSREQUEST
DESCRIPTOR.message_types_by_name['ListResourcePresetsResponse'] = _LISTRESOURCEPRESETSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetResourcePresetRequest = _reflection.GeneratedProtocolMessageType('GetResourcePresetRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETRESOURCEPRESETREQUEST,
  __module__ = 'yandex.cloud.mdb.redis.v1alpha.resource_preset_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.redis.v1alpha.GetResourcePresetRequest)
  ))
_sym_db.RegisterMessage(GetResourcePresetRequest)

ListResourcePresetsRequest = _reflection.GeneratedProtocolMessageType('ListResourcePresetsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTRESOURCEPRESETSREQUEST,
  __module__ = 'yandex.cloud.mdb.redis.v1alpha.resource_preset_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.redis.v1alpha.ListResourcePresetsRequest)
  ))
_sym_db.RegisterMessage(ListResourcePresetsRequest)

ListResourcePresetsResponse = _reflection.GeneratedProtocolMessageType('ListResourcePresetsResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTRESOURCEPRESETSRESPONSE,
  __module__ = 'yandex.cloud.mdb.redis.v1alpha.resource_preset_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.redis.v1alpha.ListResourcePresetsResponse)
  ))
_sym_db.RegisterMessage(ListResourcePresetsResponse)


DESCRIPTOR._options = None
_GETRESOURCEPRESETREQUEST.fields_by_name['resource_preset_id']._options = None

_RESOURCEPRESETSERVICE = _descriptor.ServiceDescriptor(
  name='ResourcePresetService',
  full_name='yandex.cloud.mdb.redis.v1alpha.ResourcePresetService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=474,
  serialized_end=858,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='yandex.cloud.mdb.redis.v1alpha.ResourcePresetService.Get',
    index=0,
    containing_service=None,
    input_type=_GETRESOURCEPRESETREQUEST,
    output_type=yandex_dot_cloud_dot_mdb_dot_redis_dot_v1alpha_dot_resource__preset__pb2._RESOURCEPRESET,
    serialized_options=_b('\202\323\344\223\002=\022;/managed-redis/v1alpha/resourcePresets/{resource_preset_id}'),
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='yandex.cloud.mdb.redis.v1alpha.ResourcePresetService.List',
    index=1,
    containing_service=None,
    input_type=_LISTRESOURCEPRESETSREQUEST,
    output_type=_LISTRESOURCEPRESETSRESPONSE,
    serialized_options=_b('\202\323\344\223\002(\022&/managed-redis/v1alpha/resourcePresets'),
  ),
])
_sym_db.RegisterServiceDescriptor(_RESOURCEPRESETSERVICE)

DESCRIPTOR.services_by_name['ResourcePresetService'] = _RESOURCEPRESETSERVICE

# @@protoc_insertion_point(module_scope)
