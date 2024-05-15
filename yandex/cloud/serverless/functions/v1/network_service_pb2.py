# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/serverless/functions/v1/network_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:yandex/cloud/serverless/functions/v1/network_service.proto\x12$yandex.cloud.serverless.functions.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dyandex/cloud/validation.proto\"\xb0\x02\n\x0bUsedNetwork\x12\x12\n\nnetwork_id\x18\x01 \x01(\t\x12\x10\n\x08\x63loud_id\x18\x02 \x01(\t\x12\x11\n\tfolder_id\x18\x03 \x01(\t\x12H\n\x06status\x18\x04 \x01(\x0e\x32\x38.yandex.cloud.serverless.functions.v1.UsedNetwork.Status\x12\x39\n\x15will_be_cleaned_up_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x19\n\x11\x63onnections_count\x18\x06 \x01(\x03\"H\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12\x0c\n\x08OBSOLETE\x10\x03\"1\n\x15GetUsedNetworkRequest\x12\x18\n\nnetwork_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"\x8f\x01\n\x17ListUsedNetworksRequest\x12\x1d\n\tpage_size\x18\x01 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x02 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x12\n\x08\x63loud_id\x18\x03 \x01(\tH\x00\x12\x13\n\tfolder_id\x18\x04 \x01(\tH\x00\x42\r\n\x05scope\x12\x04\xc0\xc1\x31\x01\"x\n\x18ListUsedNetworksResponse\x12\x43\n\x08networks\x18\x01 \x03(\x0b\x32\x31.yandex.cloud.serverless.functions.v1.UsedNetwork\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xb3\x01\n\x1dListConnectedResourcesRequest\x12\x1d\n\tpage_size\x18\x01 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x02 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x14\n\nnetwork_id\x18\x03 \x01(\tH\x00\x12\x12\n\x08\x63loud_id\x18\x04 \x01(\tH\x00\x12\x13\n\tfolder_id\x18\x05 \x01(\tH\x00\x42\x15\n\rnetwork_scope\x12\x04\xc0\xc1\x31\x01\"\xe3\x02\n\x1eListConnectedResourcesResponse\x12i\n\tresources\x18\x01 \x03(\x0b\x32V.yandex.cloud.serverless.functions.v1.ListConnectedResourcesResponse.ConnectedResource\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x1a\xbc\x01\n\x11\x43onnectedResource\x12\x12\n\nnetwork_id\x18\x01 \x01(\t\x12\x15\n\rresource_type\x18\x02 \x01(\t\x12\x13\n\x0bresource_id\x18\x03 \x01(\t\x12\x18\n\x10subresource_type\x18\x04 \x01(\t\x12\x16\n\x0esubresource_id\x18\x05 \x01(\t\x12\x19\n\x11resource_cloud_id\x18\x06 \x01(\t\x12\x1a\n\x12resource_folder_id\x18\x07 \x01(\t\"<\n TriggerUsedNetworkCleanupRequest\x12\x18\n\nnetwork_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"]\n!TriggerUsedNetworkCleanupResponse\x12\x38\n\x14network_cleanup_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp2\xad\x06\n\x0eNetworkService\x12\xab\x01\n\x07GetUsed\x12;.yandex.cloud.serverless.functions.v1.GetUsedNetworkRequest\x1a\x31.yandex.cloud.serverless.functions.v1.UsedNetwork\"0\x82\xd3\xe4\x93\x02*\x12(/functions/v1/networks/used/{network_id}\x12\xae\x01\n\x08ListUsed\x12=.yandex.cloud.serverless.functions.v1.ListUsedNetworksRequest\x1a>.yandex.cloud.serverless.functions.v1.ListUsedNetworksResponse\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/functions/v1/networks/used\x12\xcf\x01\n\x16ListConnectedResources\x12\x43.yandex.cloud.serverless.functions.v1.ListConnectedResourcesRequest\x1a\x44.yandex.cloud.serverless.functions.v1.ListConnectedResourcesResponse\"*\x82\xd3\xe4\x93\x02$\x12\"/functions/v1/networks/connections\x12\xe9\x01\n\x12TriggerUsedCleanup\x12\x46.yandex.cloud.serverless.functions.v1.TriggerUsedNetworkCleanupRequest\x1aG.yandex.cloud.serverless.functions.v1.TriggerUsedNetworkCleanupResponse\"B\x82\xd3\xe4\x93\x02<\"7/functions/v1/networks/used/{network_id}:triggerCleanup:\x01*B~\n(yandex.cloud.api.serverless.functions.v1ZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/functions/v1;functionsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.serverless.functions.v1.network_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n(yandex.cloud.api.serverless.functions.v1ZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/functions/v1;functions'
  _GETUSEDNETWORKREQUEST.fields_by_name['network_id']._options = None
  _GETUSEDNETWORKREQUEST.fields_by_name['network_id']._serialized_options = b'\350\3071\001'
  _LISTUSEDNETWORKSREQUEST.oneofs_by_name['scope']._options = None
  _LISTUSEDNETWORKSREQUEST.oneofs_by_name['scope']._serialized_options = b'\300\3011\001'
  _LISTUSEDNETWORKSREQUEST.fields_by_name['page_size']._options = None
  _LISTUSEDNETWORKSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTUSEDNETWORKSREQUEST.fields_by_name['page_token']._options = None
  _LISTUSEDNETWORKSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _LISTCONNECTEDRESOURCESREQUEST.oneofs_by_name['network_scope']._options = None
  _LISTCONNECTEDRESOURCESREQUEST.oneofs_by_name['network_scope']._serialized_options = b'\300\3011\001'
  _LISTCONNECTEDRESOURCESREQUEST.fields_by_name['page_size']._options = None
  _LISTCONNECTEDRESOURCESREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTCONNECTEDRESOURCESREQUEST.fields_by_name['page_token']._options = None
  _LISTCONNECTEDRESOURCESREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _TRIGGERUSEDNETWORKCLEANUPREQUEST.fields_by_name['network_id']._options = None
  _TRIGGERUSEDNETWORKCLEANUPREQUEST.fields_by_name['network_id']._serialized_options = b'\350\3071\001'
  _NETWORKSERVICE.methods_by_name['GetUsed']._options = None
  _NETWORKSERVICE.methods_by_name['GetUsed']._serialized_options = b'\202\323\344\223\002*\022(/functions/v1/networks/used/{network_id}'
  _NETWORKSERVICE.methods_by_name['ListUsed']._options = None
  _NETWORKSERVICE.methods_by_name['ListUsed']._serialized_options = b'\202\323\344\223\002\035\022\033/functions/v1/networks/used'
  _NETWORKSERVICE.methods_by_name['ListConnectedResources']._options = None
  _NETWORKSERVICE.methods_by_name['ListConnectedResources']._serialized_options = b'\202\323\344\223\002$\022\"/functions/v1/networks/connections'
  _NETWORKSERVICE.methods_by_name['TriggerUsedCleanup']._options = None
  _NETWORKSERVICE.methods_by_name['TriggerUsedCleanup']._serialized_options = b'\202\323\344\223\002<\"7/functions/v1/networks/used/{network_id}:triggerCleanup:\001*'
  _globals['_USEDNETWORK']._serialized_start=195
  _globals['_USEDNETWORK']._serialized_end=499
  _globals['_USEDNETWORK_STATUS']._serialized_start=427
  _globals['_USEDNETWORK_STATUS']._serialized_end=499
  _globals['_GETUSEDNETWORKREQUEST']._serialized_start=501
  _globals['_GETUSEDNETWORKREQUEST']._serialized_end=550
  _globals['_LISTUSEDNETWORKSREQUEST']._serialized_start=553
  _globals['_LISTUSEDNETWORKSREQUEST']._serialized_end=696
  _globals['_LISTUSEDNETWORKSRESPONSE']._serialized_start=698
  _globals['_LISTUSEDNETWORKSRESPONSE']._serialized_end=818
  _globals['_LISTCONNECTEDRESOURCESREQUEST']._serialized_start=821
  _globals['_LISTCONNECTEDRESOURCESREQUEST']._serialized_end=1000
  _globals['_LISTCONNECTEDRESOURCESRESPONSE']._serialized_start=1003
  _globals['_LISTCONNECTEDRESOURCESRESPONSE']._serialized_end=1358
  _globals['_LISTCONNECTEDRESOURCESRESPONSE_CONNECTEDRESOURCE']._serialized_start=1170
  _globals['_LISTCONNECTEDRESOURCESRESPONSE_CONNECTEDRESOURCE']._serialized_end=1358
  _globals['_TRIGGERUSEDNETWORKCLEANUPREQUEST']._serialized_start=1360
  _globals['_TRIGGERUSEDNETWORKCLEANUPREQUEST']._serialized_end=1420
  _globals['_TRIGGERUSEDNETWORKCLEANUPRESPONSE']._serialized_start=1422
  _globals['_TRIGGERUSEDNETWORKCLEANUPRESPONSE']._serialized_end=1515
  _globals['_NETWORKSERVICE']._serialized_start=1518
  _globals['_NETWORKSERVICE']._serialized_end=2331
# @@protoc_insertion_point(module_scope)
