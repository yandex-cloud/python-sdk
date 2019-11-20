# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/endpoint/api_endpoint_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.endpoint import api_endpoint_pb2 as yandex_dot_cloud_dot_endpoint_dot_api__endpoint__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/endpoint/api_endpoint_service.proto',
  package='yandex.cloud.endpoint',
  syntax='proto3',
  serialized_options=_b('\n\031yandex.cloud.api.endpointZBgithub.com/yandex-cloud/go-genproto/yandex/cloud/endpoint;endpoint'),
  serialized_pb=_b('\n0yandex/cloud/endpoint/api_endpoint_service.proto\x12\x15yandex.cloud.endpoint\x1a\x1cgoogle/api/annotations.proto\x1a(yandex/cloud/endpoint/api_endpoint.proto\"0\n\x15GetApiEndpointRequest\x12\x17\n\x0f\x61pi_endpoint_id\x18\x01 \x01(\t\"@\n\x17ListApiEndpointsRequest\x12\x11\n\tpage_size\x18\x01 \x01(\x03\x12\x12\n\npage_token\x18\x02 \x01(\t\"j\n\x18ListApiEndpointsResponse\x12\x35\n\tendpoints\x18\x01 \x03(\x0b\x32\".yandex.cloud.endpoint.ApiEndpoint\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\x90\x02\n\x12\x41piEndpointService\x12}\n\x03Get\x12,.yandex.cloud.endpoint.GetApiEndpointRequest\x1a\".yandex.cloud.endpoint.ApiEndpoint\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/endpoints/{api_endpoint_id}\x12{\n\x04List\x12..yandex.cloud.endpoint.ListApiEndpointsRequest\x1a/.yandex.cloud.endpoint.ListApiEndpointsResponse\"\x12\x82\xd3\xe4\x93\x02\x0c\x12\n/endpointsB_\n\x19yandex.cloud.api.endpointZBgithub.com/yandex-cloud/go-genproto/yandex/cloud/endpoint;endpointb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,yandex_dot_cloud_dot_endpoint_dot_api__endpoint__pb2.DESCRIPTOR,])




_GETAPIENDPOINTREQUEST = _descriptor.Descriptor(
  name='GetApiEndpointRequest',
  full_name='yandex.cloud.endpoint.GetApiEndpointRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='api_endpoint_id', full_name='yandex.cloud.endpoint.GetApiEndpointRequest.api_endpoint_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=147,
  serialized_end=195,
)


_LISTAPIENDPOINTSREQUEST = _descriptor.Descriptor(
  name='ListApiEndpointsRequest',
  full_name='yandex.cloud.endpoint.ListApiEndpointsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page_size', full_name='yandex.cloud.endpoint.ListApiEndpointsRequest.page_size', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='yandex.cloud.endpoint.ListApiEndpointsRequest.page_token', index=1,
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
  serialized_start=197,
  serialized_end=261,
)


_LISTAPIENDPOINTSRESPONSE = _descriptor.Descriptor(
  name='ListApiEndpointsResponse',
  full_name='yandex.cloud.endpoint.ListApiEndpointsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='endpoints', full_name='yandex.cloud.endpoint.ListApiEndpointsResponse.endpoints', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='yandex.cloud.endpoint.ListApiEndpointsResponse.next_page_token', index=1,
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
  serialized_start=263,
  serialized_end=369,
)

_LISTAPIENDPOINTSRESPONSE.fields_by_name['endpoints'].message_type = yandex_dot_cloud_dot_endpoint_dot_api__endpoint__pb2._APIENDPOINT
DESCRIPTOR.message_types_by_name['GetApiEndpointRequest'] = _GETAPIENDPOINTREQUEST
DESCRIPTOR.message_types_by_name['ListApiEndpointsRequest'] = _LISTAPIENDPOINTSREQUEST
DESCRIPTOR.message_types_by_name['ListApiEndpointsResponse'] = _LISTAPIENDPOINTSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetApiEndpointRequest = _reflection.GeneratedProtocolMessageType('GetApiEndpointRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETAPIENDPOINTREQUEST,
  __module__ = 'yandex.cloud.endpoint.api_endpoint_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.endpoint.GetApiEndpointRequest)
  ))
_sym_db.RegisterMessage(GetApiEndpointRequest)

ListApiEndpointsRequest = _reflection.GeneratedProtocolMessageType('ListApiEndpointsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTAPIENDPOINTSREQUEST,
  __module__ = 'yandex.cloud.endpoint.api_endpoint_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.endpoint.ListApiEndpointsRequest)
  ))
_sym_db.RegisterMessage(ListApiEndpointsRequest)

ListApiEndpointsResponse = _reflection.GeneratedProtocolMessageType('ListApiEndpointsResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTAPIENDPOINTSRESPONSE,
  __module__ = 'yandex.cloud.endpoint.api_endpoint_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.endpoint.ListApiEndpointsResponse)
  ))
_sym_db.RegisterMessage(ListApiEndpointsResponse)


DESCRIPTOR._options = None

_APIENDPOINTSERVICE = _descriptor.ServiceDescriptor(
  name='ApiEndpointService',
  full_name='yandex.cloud.endpoint.ApiEndpointService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=372,
  serialized_end=644,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='yandex.cloud.endpoint.ApiEndpointService.Get',
    index=0,
    containing_service=None,
    input_type=_GETAPIENDPOINTREQUEST,
    output_type=yandex_dot_cloud_dot_endpoint_dot_api__endpoint__pb2._APIENDPOINT,
    serialized_options=_b('\202\323\344\223\002\036\022\034/endpoints/{api_endpoint_id}'),
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='yandex.cloud.endpoint.ApiEndpointService.List',
    index=1,
    containing_service=None,
    input_type=_LISTAPIENDPOINTSREQUEST,
    output_type=_LISTAPIENDPOINTSRESPONSE,
    serialized_options=_b('\202\323\344\223\002\014\022\n/endpoints'),
  ),
])
_sym_db.RegisterServiceDescriptor(_APIENDPOINTSERVICE)

DESCRIPTOR.services_by_name['ApiEndpointService'] = _APIENDPOINTSERVICE

# @@protoc_insertion_point(module_scope)
