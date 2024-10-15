# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/apploadbalancer/v1/virtual_host_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.apploadbalancer.v1 import rate_limit_pb2 as yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_rate__limit__pb2
from yandex.cloud.apploadbalancer.v1 import virtual_host_pb2 as yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_virtual__host__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:yandex/cloud/apploadbalancer/v1/virtual_host_service.proto\x12\x1fyandex.cloud.apploadbalancer.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/api/operation.proto\x1a\x30yandex/cloud/apploadbalancer/v1/rate_limit.proto\x1a\x32yandex/cloud/apploadbalancer/v1/virtual_host.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"|\n\x15GetVirtualHostRequest\x12\x1c\n\x0ehttp_router_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x45\n\x11virtual_host_name\x18\x02 \x01(\tB*\xe8\xc7\x31\x01\xf2\xc7\x31\"([a-z]([-a-z0-9]{0,61}[a-z0-9])?)?\"u\n\x17ListVirtualHostsRequest\x12\x1c\n\x0ehttp_router_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"x\n\x18ListVirtualHostsResponse\x12\x43\n\rvirtual_hosts\x18\x01 \x03(\x0b\x32,.yandex.cloud.apploadbalancer.v1.VirtualHost\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xf0\x03\n\x18\x43reateVirtualHostRequest\x12\x1c\n\x0ehttp_router_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x34\n\x04name\x18\x02 \x01(\tB&\xf2\xc7\x31\"([a-z]([-a-z0-9]{0,61}[a-z0-9])?)?\x12\x11\n\tauthority\x18\x03 \x03(\t\x12\x36\n\x06routes\x18\x05 \x03(\x0b\x32&.yandex.cloud.apploadbalancer.v1.Route\x12S\n\x16modify_request_headers\x18\x06 \x03(\x0b\x32\x33.yandex.cloud.apploadbalancer.v1.HeaderModification\x12T\n\x17modify_response_headers\x18\x07 \x03(\x0b\x32\x33.yandex.cloud.apploadbalancer.v1.HeaderModification\x12\x44\n\rroute_options\x18\x08 \x01(\x0b\x32-.yandex.cloud.apploadbalancer.v1.RouteOptions\x12>\n\nrate_limit\x18\t \x01(\x0b\x32*.yandex.cloud.apploadbalancer.v1.RateLimitJ\x04\x08\x04\x10\x05\"T\n\x19\x43reateVirtualHostMetadata\x12\x1c\n\x0ehttp_router_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x19\n\x11virtual_host_name\x18\x02 \x01(\t\"\x8c\x04\n\x18UpdateVirtualHostRequest\x12\x1c\n\x0ehttp_router_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x1f\n\x11virtual_host_name\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x11\n\tauthority\x18\x04 \x03(\t\x12\x36\n\x06routes\x18\x06 \x03(\x0b\x32&.yandex.cloud.apploadbalancer.v1.Route\x12S\n\x16modify_request_headers\x18\x07 \x03(\x0b\x32\x33.yandex.cloud.apploadbalancer.v1.HeaderModification\x12T\n\x17modify_response_headers\x18\x08 \x03(\x0b\x32\x33.yandex.cloud.apploadbalancer.v1.HeaderModification\x12\x44\n\rroute_options\x18\t \x01(\x0b\x32-.yandex.cloud.apploadbalancer.v1.RouteOptions\x12>\n\nrate_limit\x18\n \x01(\x0b\x32*.yandex.cloud.apploadbalancer.v1.RateLimitJ\x04\x08\x05\x10\x06\"N\n\x19UpdateVirtualHostMetadata\x12\x16\n\x0ehttp_router_id\x18\x01 \x01(\t\x12\x19\n\x11virtual_host_name\x18\x02 \x01(\t\"\x7f\n\x18\x44\x65leteVirtualHostRequest\x12\x1c\n\x0ehttp_router_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x45\n\x11virtual_host_name\x18\x02 \x01(\tB*\xe8\xc7\x31\x01\xf2\xc7\x31\"([a-z]([-a-z0-9]{0,61}[a-z0-9])?)?\"N\n\x19\x44\x65leteVirtualHostMetadata\x12\x16\n\x0ehttp_router_id\x18\x01 \x01(\t\x12\x19\n\x11virtual_host_name\x18\x02 \x01(\t\"m\n\x12RemoveRouteRequest\x12\x1c\n\x0ehttp_router_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x1f\n\x11virtual_host_name\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x18\n\nroute_name\x18\x03 \x01(\tB\x04\xe8\xc7\x31\x01\"\\\n\x13RemoveRouteMetadata\x12\x16\n\x0ehttp_router_id\x18\x01 \x01(\t\x12\x19\n\x11virtual_host_name\x18\x02 \x01(\t\x12\x12\n\nroute_name\x18\x03 \x01(\t\"\xeb\x02\n\x12UpdateRouteRequest\x12\x1c\n\x0ehttp_router_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x1f\n\x11virtual_host_name\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x18\n\nroute_name\x18\x03 \x01(\tB\x04\xe8\xc7\x31\x01\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12:\n\x04http\x18\x05 \x01(\x0b\x32*.yandex.cloud.apploadbalancer.v1.HttpRouteH\x00\x12:\n\x04grpc\x18\x06 \x01(\x0b\x32*.yandex.cloud.apploadbalancer.v1.GrpcRouteH\x00\x12\x44\n\rroute_options\x18\x07 \x01(\x0b\x32-.yandex.cloud.apploadbalancer.v1.RouteOptionsB\r\n\x05route\x12\x04\xc0\xc1\x31\x01\"\\\n\x13UpdateRouteMetadata\x12\x16\n\x0ehttp_router_id\x18\x01 \x01(\t\x12\x19\n\x11virtual_host_name\x18\x02 \x01(\t\x12\x12\n\nroute_name\x18\x03 \x01(\t2\xe2\x0c\n\x12VirtualHostService\x12\xc6\x01\n\x03Get\x12\x36.yandex.cloud.apploadbalancer.v1.GetVirtualHostRequest\x1a,.yandex.cloud.apploadbalancer.v1.VirtualHost\"Y\x82\xd3\xe4\x93\x02S\x12Q/apploadbalancer/v1/httpRouters/{http_router_id}/virtualHosts/{virtual_host_name}\x12\xc2\x01\n\x04List\x12\x38.yandex.cloud.apploadbalancer.v1.ListVirtualHostsRequest\x1a\x39.yandex.cloud.apploadbalancer.v1.ListVirtualHostsResponse\"E\x82\xd3\xe4\x93\x02?\x12=/apploadbalancer/v1/httpRouters/{http_router_id}/virtualHosts\x12\xdc\x01\n\x06\x43reate\x12\x39.yandex.cloud.apploadbalancer.v1.CreateVirtualHostRequest\x1a!.yandex.cloud.operation.Operation\"t\xb2\xd2*(\n\x19\x43reateVirtualHostMetadata\x12\x0bVirtualHost\x82\xd3\xe4\x93\x02\x42\"=/apploadbalancer/v1/httpRouters/{http_router_id}/virtualHosts:\x01*\x12\xf1\x01\n\x06Update\x12\x39.yandex.cloud.apploadbalancer.v1.UpdateVirtualHostRequest\x1a!.yandex.cloud.operation.Operation\"\x88\x01\xb2\xd2*(\n\x19UpdateVirtualHostMetadata\x12\x0bVirtualHost\x82\xd3\xe4\x93\x02V2Q/apploadbalancer/v1/httpRouters/{http_router_id}/virtualHosts/{virtual_host_name}:\x01*\x12\xf8\x01\n\x06\x44\x65lete\x12\x39.yandex.cloud.apploadbalancer.v1.DeleteVirtualHostRequest\x1a!.yandex.cloud.operation.Operation\"\x8f\x01\xb2\xd2*2\n\x19\x44\x65leteVirtualHostMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02S*Q/apploadbalancer/v1/httpRouters/{http_router_id}/virtualHosts/{virtual_host_name}\x12\xf6\x01\n\x0bRemoveRoute\x12\x33.yandex.cloud.apploadbalancer.v1.RemoveRouteRequest\x1a!.yandex.cloud.operation.Operation\"\x8e\x01\xb2\xd2*\"\n\x13RemoveRouteMetadata\x12\x0bVirtualHost\x82\xd3\xe4\x93\x02\x62\"]/apploadbalancer/v1/httpRouters/{http_router_id}/virtualHosts/{virtual_host_name}:removeRoute:\x01*\x12\xf6\x01\n\x0bUpdateRoute\x12\x33.yandex.cloud.apploadbalancer.v1.UpdateRouteRequest\x1a!.yandex.cloud.operation.Operation\"\x8e\x01\xb2\xd2*\"\n\x13UpdateRouteMetadata\x12\x0bVirtualHost\x82\xd3\xe4\x93\x02\x62\"]/apploadbalancer/v1/httpRouters/{http_router_id}/virtualHosts/{virtual_host_name}:updateRoute:\x01*Bz\n#yandex.cloud.api.apploadbalancer.v1ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/apploadbalancer/v1;apploadbalancerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.apploadbalancer.v1.virtual_host_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#yandex.cloud.api.apploadbalancer.v1ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/apploadbalancer/v1;apploadbalancer'
  _GETVIRTUALHOSTREQUEST.fields_by_name['http_router_id']._options = None
  _GETVIRTUALHOSTREQUEST.fields_by_name['http_router_id']._serialized_options = b'\350\3071\001'
  _GETVIRTUALHOSTREQUEST.fields_by_name['virtual_host_name']._options = None
  _GETVIRTUALHOSTREQUEST.fields_by_name['virtual_host_name']._serialized_options = b'\350\3071\001\362\3071\"([a-z]([-a-z0-9]{0,61}[a-z0-9])?)?'
  _LISTVIRTUALHOSTSREQUEST.fields_by_name['http_router_id']._options = None
  _LISTVIRTUALHOSTSREQUEST.fields_by_name['http_router_id']._serialized_options = b'\350\3071\001'
  _LISTVIRTUALHOSTSREQUEST.fields_by_name['page_size']._options = None
  _LISTVIRTUALHOSTSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTVIRTUALHOSTSREQUEST.fields_by_name['page_token']._options = None
  _LISTVIRTUALHOSTSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _CREATEVIRTUALHOSTREQUEST.fields_by_name['http_router_id']._options = None
  _CREATEVIRTUALHOSTREQUEST.fields_by_name['http_router_id']._serialized_options = b'\350\3071\001'
  _CREATEVIRTUALHOSTREQUEST.fields_by_name['name']._options = None
  _CREATEVIRTUALHOSTREQUEST.fields_by_name['name']._serialized_options = b'\362\3071\"([a-z]([-a-z0-9]{0,61}[a-z0-9])?)?'
  _CREATEVIRTUALHOSTMETADATA.fields_by_name['http_router_id']._options = None
  _CREATEVIRTUALHOSTMETADATA.fields_by_name['http_router_id']._serialized_options = b'\350\3071\001'
  _UPDATEVIRTUALHOSTREQUEST.fields_by_name['http_router_id']._options = None
  _UPDATEVIRTUALHOSTREQUEST.fields_by_name['http_router_id']._serialized_options = b'\350\3071\001'
  _UPDATEVIRTUALHOSTREQUEST.fields_by_name['virtual_host_name']._options = None
  _UPDATEVIRTUALHOSTREQUEST.fields_by_name['virtual_host_name']._serialized_options = b'\350\3071\001'
  _DELETEVIRTUALHOSTREQUEST.fields_by_name['http_router_id']._options = None
  _DELETEVIRTUALHOSTREQUEST.fields_by_name['http_router_id']._serialized_options = b'\350\3071\001'
  _DELETEVIRTUALHOSTREQUEST.fields_by_name['virtual_host_name']._options = None
  _DELETEVIRTUALHOSTREQUEST.fields_by_name['virtual_host_name']._serialized_options = b'\350\3071\001\362\3071\"([a-z]([-a-z0-9]{0,61}[a-z0-9])?)?'
  _REMOVEROUTEREQUEST.fields_by_name['http_router_id']._options = None
  _REMOVEROUTEREQUEST.fields_by_name['http_router_id']._serialized_options = b'\350\3071\001'
  _REMOVEROUTEREQUEST.fields_by_name['virtual_host_name']._options = None
  _REMOVEROUTEREQUEST.fields_by_name['virtual_host_name']._serialized_options = b'\350\3071\001'
  _REMOVEROUTEREQUEST.fields_by_name['route_name']._options = None
  _REMOVEROUTEREQUEST.fields_by_name['route_name']._serialized_options = b'\350\3071\001'
  _UPDATEROUTEREQUEST.oneofs_by_name['route']._options = None
  _UPDATEROUTEREQUEST.oneofs_by_name['route']._serialized_options = b'\300\3011\001'
  _UPDATEROUTEREQUEST.fields_by_name['http_router_id']._options = None
  _UPDATEROUTEREQUEST.fields_by_name['http_router_id']._serialized_options = b'\350\3071\001'
  _UPDATEROUTEREQUEST.fields_by_name['virtual_host_name']._options = None
  _UPDATEROUTEREQUEST.fields_by_name['virtual_host_name']._serialized_options = b'\350\3071\001'
  _UPDATEROUTEREQUEST.fields_by_name['route_name']._options = None
  _UPDATEROUTEREQUEST.fields_by_name['route_name']._serialized_options = b'\350\3071\001'
  _VIRTUALHOSTSERVICE.methods_by_name['Get']._options = None
  _VIRTUALHOSTSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002S\022Q/apploadbalancer/v1/httpRouters/{http_router_id}/virtualHosts/{virtual_host_name}'
  _VIRTUALHOSTSERVICE.methods_by_name['List']._options = None
  _VIRTUALHOSTSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002?\022=/apploadbalancer/v1/httpRouters/{http_router_id}/virtualHosts'
  _VIRTUALHOSTSERVICE.methods_by_name['Create']._options = None
  _VIRTUALHOSTSERVICE.methods_by_name['Create']._serialized_options = b'\262\322*(\n\031CreateVirtualHostMetadata\022\013VirtualHost\202\323\344\223\002B\"=/apploadbalancer/v1/httpRouters/{http_router_id}/virtualHosts:\001*'
  _VIRTUALHOSTSERVICE.methods_by_name['Update']._options = None
  _VIRTUALHOSTSERVICE.methods_by_name['Update']._serialized_options = b'\262\322*(\n\031UpdateVirtualHostMetadata\022\013VirtualHost\202\323\344\223\002V2Q/apploadbalancer/v1/httpRouters/{http_router_id}/virtualHosts/{virtual_host_name}:\001*'
  _VIRTUALHOSTSERVICE.methods_by_name['Delete']._options = None
  _VIRTUALHOSTSERVICE.methods_by_name['Delete']._serialized_options = b'\262\322*2\n\031DeleteVirtualHostMetadata\022\025google.protobuf.Empty\202\323\344\223\002S*Q/apploadbalancer/v1/httpRouters/{http_router_id}/virtualHosts/{virtual_host_name}'
  _VIRTUALHOSTSERVICE.methods_by_name['RemoveRoute']._options = None
  _VIRTUALHOSTSERVICE.methods_by_name['RemoveRoute']._serialized_options = b'\262\322*\"\n\023RemoveRouteMetadata\022\013VirtualHost\202\323\344\223\002b\"]/apploadbalancer/v1/httpRouters/{http_router_id}/virtualHosts/{virtual_host_name}:removeRoute:\001*'
  _VIRTUALHOSTSERVICE.methods_by_name['UpdateRoute']._options = None
  _VIRTUALHOSTSERVICE.methods_by_name['UpdateRoute']._serialized_options = b'\262\322*\"\n\023UpdateRouteMetadata\022\013VirtualHost\202\323\344\223\002b\"]/apploadbalancer/v1/httpRouters/{http_router_id}/virtualHosts/{virtual_host_name}:updateRoute:\001*'
  _globals['_GETVIRTUALHOSTREQUEST']._serialized_start=366
  _globals['_GETVIRTUALHOSTREQUEST']._serialized_end=490
  _globals['_LISTVIRTUALHOSTSREQUEST']._serialized_start=492
  _globals['_LISTVIRTUALHOSTSREQUEST']._serialized_end=609
  _globals['_LISTVIRTUALHOSTSRESPONSE']._serialized_start=611
  _globals['_LISTVIRTUALHOSTSRESPONSE']._serialized_end=731
  _globals['_CREATEVIRTUALHOSTREQUEST']._serialized_start=734
  _globals['_CREATEVIRTUALHOSTREQUEST']._serialized_end=1230
  _globals['_CREATEVIRTUALHOSTMETADATA']._serialized_start=1232
  _globals['_CREATEVIRTUALHOSTMETADATA']._serialized_end=1316
  _globals['_UPDATEVIRTUALHOSTREQUEST']._serialized_start=1319
  _globals['_UPDATEVIRTUALHOSTREQUEST']._serialized_end=1843
  _globals['_UPDATEVIRTUALHOSTMETADATA']._serialized_start=1845
  _globals['_UPDATEVIRTUALHOSTMETADATA']._serialized_end=1923
  _globals['_DELETEVIRTUALHOSTREQUEST']._serialized_start=1925
  _globals['_DELETEVIRTUALHOSTREQUEST']._serialized_end=2052
  _globals['_DELETEVIRTUALHOSTMETADATA']._serialized_start=2054
  _globals['_DELETEVIRTUALHOSTMETADATA']._serialized_end=2132
  _globals['_REMOVEROUTEREQUEST']._serialized_start=2134
  _globals['_REMOVEROUTEREQUEST']._serialized_end=2243
  _globals['_REMOVEROUTEMETADATA']._serialized_start=2245
  _globals['_REMOVEROUTEMETADATA']._serialized_end=2337
  _globals['_UPDATEROUTEREQUEST']._serialized_start=2340
  _globals['_UPDATEROUTEREQUEST']._serialized_end=2703
  _globals['_UPDATEROUTEMETADATA']._serialized_start=2705
  _globals['_UPDATEROUTEMETADATA']._serialized_end=2797
  _globals['_VIRTUALHOSTSERVICE']._serialized_start=2800
  _globals['_VIRTUALHOSTSERVICE']._serialized_end=4434
# @@protoc_insertion_point(module_scope)
