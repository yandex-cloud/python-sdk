# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/serverless/mdbproxy/v1/proxy_service.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'yandex/cloud/serverless/mdbproxy/v1/proxy_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2
from yandex.cloud.serverless.mdbproxy.v1 import proxy_pb2 as yandex_dot_cloud_dot_serverless_dot_mdbproxy_dot_v1_dot_proxy__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7yandex/cloud/serverless/mdbproxy/v1/proxy_service.proto\x12#yandex.cloud.serverless.mdbproxy.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/api/operation.proto\x1a yandex/cloud/access/access.proto\x1a/yandex/cloud/serverless/mdbproxy/v1/proxy.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"1\n\x0fGetProxyRequest\x12\x1e\n\x08proxy_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\x8d\x01\n\x10ListProxyRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"t\n\x11ListProxyResponse\x12;\n\x07proxies\x18\x01 \x03(\x0b\x32*.yandex.cloud.serverless.mdbproxy.v1.Proxy\x12\"\n\x0fnext_page_token\x18\x02 \x01(\tB\t\x8a\xc8\x31\x05<=100\"\x8b\x03\n\x12\x43reateProxyRequest\x12\x17\n\tfolder_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12/\n\x04name\x18\x02 \x01(\tB!\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x98\x01\n\x06labels\x18\x04 \x03(\x0b\x32\x43.yandex.cloud.serverless.mdbproxy.v1.CreateProxyRequest.LabelsEntryBC\xf2\xc7\x31\x0f[-_./\\@0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x1c\x12\x14[a-z][-_./\\@0-9a-z]*\x1a\x04\x31-63\x12\x41\n\x06target\x18\x05 \x01(\x0b\x32+.yandex.cloud.serverless.mdbproxy.v1.TargetB\x04\xe8\xc7\x31\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"1\n\x13\x43reateProxyMetadata\x12\x1a\n\x08proxy_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\"\xb5\x03\n\x12UpdateProxyRequest\x12\x16\n\x08proxy_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12/\n\x04name\x18\x03 \x01(\tB!\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x98\x01\n\x06labels\x18\x05 \x03(\x0b\x32\x43.yandex.cloud.serverless.mdbproxy.v1.UpdateProxyRequest.LabelsEntryBC\xf2\xc7\x31\x0f[-_./\\@0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x1c\x12\x14[a-z][-_./\\@0-9a-z]*\x1a\x04\x31-63\x12;\n\x06target\x18\x06 \x01(\x0b\x32+.yandex.cloud.serverless.mdbproxy.v1.Target\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"5\n\x13UpdateProxyMetadata\x12\x1e\n\x08proxy_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"4\n\x12\x44\x65leteProxyRequest\x12\x1e\n\x08proxy_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"5\n\x13\x44\x65leteProxyMetadata\x12\x1e\n\x08proxy_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\x8e\x01\n\x1aListProxyOperationsRequest\x12\x16\n\x08proxy_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"m\n\x1bListProxyOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xac\r\n\x0cProxyService\x12\x90\x01\n\x03Get\x12\x34.yandex.cloud.serverless.mdbproxy.v1.GetProxyRequest\x1a*.yandex.cloud.serverless.mdbproxy.v1.Proxy\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/mdbproxy/v1/proxies/{proxy_id}\x12\x93\x01\n\x04List\x12\x35.yandex.cloud.serverless.mdbproxy.v1.ListProxyRequest\x1a\x36.yandex.cloud.serverless.mdbproxy.v1.ListProxyResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/mdbproxy/v1/proxies\x12\xa5\x01\n\x06\x43reate\x12\x37.yandex.cloud.serverless.mdbproxy.v1.CreateProxyRequest\x1a!.yandex.cloud.operation.Operation\"?\xb2\xd2*\x1c\n\x13\x43reateProxyMetadata\x12\x05Proxy\x82\xd3\xe4\x93\x02\x19\"\x14/mdbproxy/v1/proxies:\x01*\x12\xb0\x01\n\x06Update\x12\x37.yandex.cloud.serverless.mdbproxy.v1.UpdateProxyRequest\x1a!.yandex.cloud.operation.Operation\"J\xb2\xd2*\x1c\n\x13UpdateProxyMetadata\x12\x05Proxy\x82\xd3\xe4\x93\x02$2\x1f/mdbproxy/v1/proxies/{proxy_id}:\x01*\x12\xbd\x01\n\x06\x44\x65lete\x12\x37.yandex.cloud.serverless.mdbproxy.v1.DeleteProxyRequest\x1a!.yandex.cloud.operation.Operation\"W\xb2\xd2*,\n\x13\x44\x65leteProxyMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02!*\x1f/mdbproxy/v1/proxies/{proxy_id}\x12\xc7\x01\n\x0eListOperations\x12?.yandex.cloud.serverless.mdbproxy.v1.ListProxyOperationsRequest\x1a@.yandex.cloud.serverless.mdbproxy.v1.ListProxyOperationsResponse\"2\x82\xd3\xe4\x93\x02,\x12*/mdbproxy/v1/proxies/{proxy_id}/operations\x12\xb4\x01\n\x12ListAccessBindings\x12..yandex.cloud.access.ListAccessBindingsRequest\x1a/.yandex.cloud.access.ListAccessBindingsResponse\"=\x82\xd3\xe4\x93\x02\x37\x12\x35/mdbproxy/v1/proxies/{resource_id}:listAccessBindings\x12\xe3\x01\n\x11SetAccessBindings\x12-.yandex.cloud.access.SetAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"|\xb2\xd2*9\n access.SetAccessBindingsMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x39\"4/mdbproxy/v1/proxies/{resource_id}:setAccessBindings:\x01*\x12\xf0\x01\n\x14UpdateAccessBindings\x12\x30.yandex.cloud.access.UpdateAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x82\x01\xb2\xd2*<\n#access.UpdateAccessBindingsMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02<27/mdbproxy/v1/proxies/{resource_id}:updateAccessBindings:\x01*Bx\n\'yandex.cloud.api.serverless.mdbproxy.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/mdbproxy/v1;proxyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.serverless.mdbproxy.v1.proxy_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\'yandex.cloud.api.serverless.mdbproxy.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/mdbproxy/v1;proxy'
  _globals['_GETPROXYREQUEST'].fields_by_name['proxy_id']._loaded_options = None
  _globals['_GETPROXYREQUEST'].fields_by_name['proxy_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTPROXYREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_LISTPROXYREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTPROXYREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTPROXYREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _globals['_LISTPROXYREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTPROXYREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTPROXYREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTPROXYREQUEST'].fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _globals['_LISTPROXYRESPONSE'].fields_by_name['next_page_token']._loaded_options = None
  _globals['_LISTPROXYRESPONSE'].fields_by_name['next_page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_CREATEPROXYREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_CREATEPROXYREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_CREATEPROXYREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_CREATEPROXYREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001'
  _globals['_CREATEPROXYREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_CREATEPROXYREQUEST'].fields_by_name['name']._serialized_options = b'\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _globals['_CREATEPROXYREQUEST'].fields_by_name['description']._loaded_options = None
  _globals['_CREATEPROXYREQUEST'].fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _globals['_CREATEPROXYREQUEST'].fields_by_name['labels']._loaded_options = None
  _globals['_CREATEPROXYREQUEST'].fields_by_name['labels']._serialized_options = b'\362\3071\017[-_./\\@0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\034\022\024[a-z][-_./\\@0-9a-z]*\032\0041-63'
  _globals['_CREATEPROXYREQUEST'].fields_by_name['target']._loaded_options = None
  _globals['_CREATEPROXYREQUEST'].fields_by_name['target']._serialized_options = b'\350\3071\001'
  _globals['_CREATEPROXYMETADATA'].fields_by_name['proxy_id']._loaded_options = None
  _globals['_CREATEPROXYMETADATA'].fields_by_name['proxy_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_UPDATEPROXYREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_UPDATEPROXYREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_UPDATEPROXYREQUEST'].fields_by_name['proxy_id']._loaded_options = None
  _globals['_UPDATEPROXYREQUEST'].fields_by_name['proxy_id']._serialized_options = b'\350\3071\001'
  _globals['_UPDATEPROXYREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_UPDATEPROXYREQUEST'].fields_by_name['name']._serialized_options = b'\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _globals['_UPDATEPROXYREQUEST'].fields_by_name['description']._loaded_options = None
  _globals['_UPDATEPROXYREQUEST'].fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _globals['_UPDATEPROXYREQUEST'].fields_by_name['labels']._loaded_options = None
  _globals['_UPDATEPROXYREQUEST'].fields_by_name['labels']._serialized_options = b'\362\3071\017[-_./\\@0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\034\022\024[a-z][-_./\\@0-9a-z]*\032\0041-63'
  _globals['_UPDATEPROXYMETADATA'].fields_by_name['proxy_id']._loaded_options = None
  _globals['_UPDATEPROXYMETADATA'].fields_by_name['proxy_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_DELETEPROXYREQUEST'].fields_by_name['proxy_id']._loaded_options = None
  _globals['_DELETEPROXYREQUEST'].fields_by_name['proxy_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_DELETEPROXYMETADATA'].fields_by_name['proxy_id']._loaded_options = None
  _globals['_DELETEPROXYMETADATA'].fields_by_name['proxy_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTPROXYOPERATIONSREQUEST'].fields_by_name['proxy_id']._loaded_options = None
  _globals['_LISTPROXYOPERATIONSREQUEST'].fields_by_name['proxy_id']._serialized_options = b'\350\3071\001'
  _globals['_LISTPROXYOPERATIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTPROXYOPERATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _globals['_LISTPROXYOPERATIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTPROXYOPERATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTPROXYOPERATIONSREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTPROXYOPERATIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _globals['_PROXYSERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_PROXYSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002!\022\037/mdbproxy/v1/proxies/{proxy_id}'
  _globals['_PROXYSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_PROXYSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002\026\022\024/mdbproxy/v1/proxies'
  _globals['_PROXYSERVICE'].methods_by_name['Create']._loaded_options = None
  _globals['_PROXYSERVICE'].methods_by_name['Create']._serialized_options = b'\262\322*\034\n\023CreateProxyMetadata\022\005Proxy\202\323\344\223\002\031\"\024/mdbproxy/v1/proxies:\001*'
  _globals['_PROXYSERVICE'].methods_by_name['Update']._loaded_options = None
  _globals['_PROXYSERVICE'].methods_by_name['Update']._serialized_options = b'\262\322*\034\n\023UpdateProxyMetadata\022\005Proxy\202\323\344\223\002$2\037/mdbproxy/v1/proxies/{proxy_id}:\001*'
  _globals['_PROXYSERVICE'].methods_by_name['Delete']._loaded_options = None
  _globals['_PROXYSERVICE'].methods_by_name['Delete']._serialized_options = b'\262\322*,\n\023DeleteProxyMetadata\022\025google.protobuf.Empty\202\323\344\223\002!*\037/mdbproxy/v1/proxies/{proxy_id}'
  _globals['_PROXYSERVICE'].methods_by_name['ListOperations']._loaded_options = None
  _globals['_PROXYSERVICE'].methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\002,\022*/mdbproxy/v1/proxies/{proxy_id}/operations'
  _globals['_PROXYSERVICE'].methods_by_name['ListAccessBindings']._loaded_options = None
  _globals['_PROXYSERVICE'].methods_by_name['ListAccessBindings']._serialized_options = b'\202\323\344\223\0027\0225/mdbproxy/v1/proxies/{resource_id}:listAccessBindings'
  _globals['_PROXYSERVICE'].methods_by_name['SetAccessBindings']._loaded_options = None
  _globals['_PROXYSERVICE'].methods_by_name['SetAccessBindings']._serialized_options = b'\262\322*9\n access.SetAccessBindingsMetadata\022\025google.protobuf.Empty\202\323\344\223\0029\"4/mdbproxy/v1/proxies/{resource_id}:setAccessBindings:\001*'
  _globals['_PROXYSERVICE'].methods_by_name['UpdateAccessBindings']._loaded_options = None
  _globals['_PROXYSERVICE'].methods_by_name['UpdateAccessBindings']._serialized_options = b'\262\322*<\n#access.UpdateAccessBindingsMetadata\022\025google.protobuf.Empty\202\323\344\223\002<27/mdbproxy/v1/proxies/{resource_id}:updateAccessBindings:\001*'
  _globals['_GETPROXYREQUEST']._serialized_start=348
  _globals['_GETPROXYREQUEST']._serialized_end=397
  _globals['_LISTPROXYREQUEST']._serialized_start=400
  _globals['_LISTPROXYREQUEST']._serialized_end=541
  _globals['_LISTPROXYRESPONSE']._serialized_start=543
  _globals['_LISTPROXYRESPONSE']._serialized_end=659
  _globals['_CREATEPROXYREQUEST']._serialized_start=662
  _globals['_CREATEPROXYREQUEST']._serialized_end=1057
  _globals['_CREATEPROXYREQUEST_LABELSENTRY']._serialized_start=1012
  _globals['_CREATEPROXYREQUEST_LABELSENTRY']._serialized_end=1057
  _globals['_CREATEPROXYMETADATA']._serialized_start=1059
  _globals['_CREATEPROXYMETADATA']._serialized_end=1108
  _globals['_UPDATEPROXYREQUEST']._serialized_start=1111
  _globals['_UPDATEPROXYREQUEST']._serialized_end=1548
  _globals['_UPDATEPROXYREQUEST_LABELSENTRY']._serialized_start=1012
  _globals['_UPDATEPROXYREQUEST_LABELSENTRY']._serialized_end=1057
  _globals['_UPDATEPROXYMETADATA']._serialized_start=1550
  _globals['_UPDATEPROXYMETADATA']._serialized_end=1603
  _globals['_DELETEPROXYREQUEST']._serialized_start=1605
  _globals['_DELETEPROXYREQUEST']._serialized_end=1657
  _globals['_DELETEPROXYMETADATA']._serialized_start=1659
  _globals['_DELETEPROXYMETADATA']._serialized_end=1712
  _globals['_LISTPROXYOPERATIONSREQUEST']._serialized_start=1715
  _globals['_LISTPROXYOPERATIONSREQUEST']._serialized_end=1857
  _globals['_LISTPROXYOPERATIONSRESPONSE']._serialized_start=1859
  _globals['_LISTPROXYOPERATIONSRESPONSE']._serialized_end=1968
  _globals['_PROXYSERVICE']._serialized_start=1971
  _globals['_PROXYSERVICE']._serialized_end=3679
# @@protoc_insertion_point(module_scope)
