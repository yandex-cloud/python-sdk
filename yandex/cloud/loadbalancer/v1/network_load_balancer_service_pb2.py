# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/loadbalancer/v1/network_load_balancer_service.proto
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
    'yandex/cloud/loadbalancer/v1/network_load_balancer_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.loadbalancer.v1 import network_load_balancer_pb2 as yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_network__load__balancer__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@yandex/cloud/loadbalancer/v1/network_load_balancer_service.proto\x12\x1cyandex.cloud.loadbalancer.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/api/operation.proto\x1a\x1dyandex/cloud/validation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x38yandex/cloud/loadbalancer/v1/network_load_balancer.proto\"K\n\x1dGetNetworkLoadBalancerRequest\x12*\n\x18network_load_balancer_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\"\x9c\x01\n\x1fListNetworkLoadBalancersRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"\x8e\x01\n ListNetworkLoadBalancersResponse\x12Q\n\x16network_load_balancers\x18\x01 \x03(\x0b\x32\x31.yandex.cloud.loadbalancer.v1.NetworkLoadBalancer\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xad\x05\n CreateNetworkLoadBalancerRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x04name\x18\x02 \x01(\tB!\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x97\x01\n\x06labels\x18\x04 \x03(\x0b\x32J.yandex.cloud.loadbalancer.v1.CreateNetworkLoadBalancerRequest.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04\x31-63\x12\x1b\n\tregion_id\x18\x05 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12J\n\x04type\x18\x06 \x01(\x0e\x32\x36.yandex.cloud.loadbalancer.v1.NetworkLoadBalancer.TypeB\x04\xe8\xc7\x31\x01\x12N\n\x0elistener_specs\x18\x07 \x03(\x0b\x32*.yandex.cloud.loadbalancer.v1.ListenerSpecB\n\x82\xc8\x31\x06<=1000\x12]\n\x16\x61ttached_target_groups\x18\x08 \x03(\x0b\x32\x31.yandex.cloud.loadbalancer.v1.AttachedTargetGroupB\n\x82\xc8\x31\x06<=1000\x12\x1b\n\x13\x64\x65letion_protection\x18\t \x01(\x08\x12\x19\n\x11\x61llow_zonal_shift\x18\n \x01(\x08\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"E\n!CreateNetworkLoadBalancerMetadata\x12 \n\x18network_load_balancer_id\x18\x01 \x01(\t\"\x84\x05\n UpdateNetworkLoadBalancerRequest\x12.\n\x18network_load_balancer_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12/\n\x04name\x18\x03 \x01(\tB!\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x97\x01\n\x06labels\x18\x05 \x03(\x0b\x32J.yandex.cloud.loadbalancer.v1.UpdateNetworkLoadBalancerRequest.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04\x31-63\x12N\n\x0elistener_specs\x18\x06 \x03(\x0b\x32*.yandex.cloud.loadbalancer.v1.ListenerSpecB\n\x82\xc8\x31\x06<=1000\x12]\n\x16\x61ttached_target_groups\x18\x07 \x03(\x0b\x32\x31.yandex.cloud.loadbalancer.v1.AttachedTargetGroupB\n\x82\xc8\x31\x06<=1000\x12\x1b\n\x13\x64\x65letion_protection\x18\x08 \x01(\x08\x12\x19\n\x11\x61llow_zonal_shift\x18\t \x01(\x08\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"E\n!UpdateNetworkLoadBalancerMetadata\x12 \n\x18network_load_balancer_id\x18\x01 \x01(\t\"R\n DeleteNetworkLoadBalancerRequest\x12.\n\x18network_load_balancer_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"E\n!DeleteNetworkLoadBalancerMetadata\x12 \n\x18network_load_balancer_id\x18\x01 \x01(\t\"Q\n\x1fStartNetworkLoadBalancerRequest\x12.\n\x18network_load_balancer_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"D\n StartNetworkLoadBalancerMetadata\x12 \n\x18network_load_balancer_id\x18\x01 \x01(\t\"P\n\x1eStopNetworkLoadBalancerRequest\x12.\n\x18network_load_balancer_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"C\n\x1fStopNetworkLoadBalancerMetadata\x12 \n\x18network_load_balancer_id\x18\x01 \x01(\t\"\xb5\x01\n+AttachNetworkLoadBalancerTargetGroupRequest\x12.\n\x18network_load_balancer_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12V\n\x15\x61ttached_target_group\x18\x02 \x01(\x0b\x32\x31.yandex.cloud.loadbalancer.v1.AttachedTargetGroupB\x04\xe8\xc7\x31\x01\"i\n,AttachNetworkLoadBalancerTargetGroupMetadata\x12 \n\x18network_load_balancer_id\x18\x01 \x01(\t\x12\x17\n\x0ftarget_group_id\x18\x02 \x01(\t\"\x84\x01\n+DetachNetworkLoadBalancerTargetGroupRequest\x12.\n\x18network_load_balancer_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12%\n\x0ftarget_group_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"i\n,DetachNetworkLoadBalancerTargetGroupMetadata\x12 \n\x18network_load_balancer_id\x18\x01 \x01(\t\x12\x17\n\x0ftarget_group_id\x18\x02 \x01(\t\"\xa0\x01\n%AddNetworkLoadBalancerListenerRequest\x12.\n\x18network_load_balancer_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12G\n\rlistener_spec\x18\x02 \x01(\x0b\x32*.yandex.cloud.loadbalancer.v1.ListenerSpecB\x04\xe8\xc7\x31\x01\"J\n&AddNetworkLoadBalancerListenerMetadata\x12 \n\x18network_load_balancer_id\x18\x01 \x01(\t\"\x98\x01\n(RemoveNetworkLoadBalancerListenerRequest\x12.\n\x18network_load_balancer_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12<\n\rlistener_name\x18\x02 \x01(\tB%\xe8\xc7\x31\x01\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\"M\n)RemoveNetworkLoadBalancerListenerMetadata\x12 \n\x18network_load_balancer_id\x18\x01 \x01(\t\"\x98\x01\n(ListNetworkLoadBalancerOperationsRequest\x12.\n\x18network_load_balancer_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"{\n)ListNetworkLoadBalancerOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"g\n\x16GetTargetStatesRequest\x12*\n\x18network_load_balancer_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12!\n\x0ftarget_group_id\x18\x02 \x01(\tB\x08\x8a\xc8\x31\x04<=50\"[\n\x17GetTargetStatesResponse\x12@\n\rtarget_states\x18\x01 \x03(\x0b\x32).yandex.cloud.loadbalancer.v1.TargetState\"c\n\x13\x45xternalAddressSpec\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12;\n\nip_version\x18\x02 \x01(\x0e\x32\'.yandex.cloud.loadbalancer.v1.IpVersion\"v\n\x13InternalAddressSpec\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x11\n\tsubnet_id\x18\x02 \x01(\t\x12;\n\nip_version\x18\x03 \x01(\x0e\x32\'.yandex.cloud.loadbalancer.v1.IpVersion\"\xef\x02\n\x0cListenerSpec\x12\x33\n\x04name\x18\x01 \x01(\tB%\xe8\xc7\x31\x01\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x19\n\x04port\x18\x02 \x01(\x03\x42\x0b\xfa\xc7\x31\x07\x31-65535\x12G\n\x08protocol\x18\x03 \x01(\x0e\x32/.yandex.cloud.loadbalancer.v1.Listener.ProtocolB\x04\xe8\xc7\x31\x01\x12R\n\x15\x65xternal_address_spec\x18\x04 \x01(\x0b\x32\x31.yandex.cloud.loadbalancer.v1.ExternalAddressSpecH\x00\x12R\n\x15internal_address_spec\x18\x06 \x01(\x0b\x32\x31.yandex.cloud.loadbalancer.v1.InternalAddressSpecH\x00\x12\x13\n\x0btarget_port\x18\x05 \x01(\x03\x42\t\n\x07\x61\x64\x64ress2\xb9\x19\n\x1aNetworkLoadBalancerService\x12\xc0\x01\n\x03Get\x12;.yandex.cloud.loadbalancer.v1.GetNetworkLoadBalancerRequest\x1a\x31.yandex.cloud.loadbalancer.v1.NetworkLoadBalancer\"I\x82\xd3\xe4\x93\x02\x43\x12\x41/load-balancer/v1/networkLoadBalancers/{network_load_balancer_id}\x12\xb5\x01\n\x04List\x12=.yandex.cloud.loadbalancer.v1.ListNetworkLoadBalancersRequest\x1a>.yandex.cloud.loadbalancer.v1.ListNetworkLoadBalancersResponse\".\x82\xd3\xe4\x93\x02(\x12&/load-balancer/v1/networkLoadBalancers\x12\xda\x01\n\x06\x43reate\x12>.yandex.cloud.loadbalancer.v1.CreateNetworkLoadBalancerRequest\x1a!.yandex.cloud.operation.Operation\"m\xb2\xd2*8\n!CreateNetworkLoadBalancerMetadata\x12\x13NetworkLoadBalancer\x82\xd3\xe4\x93\x02+\"&/load-balancer/v1/networkLoadBalancers:\x01*\x12\xf6\x01\n\x06Update\x12>.yandex.cloud.loadbalancer.v1.UpdateNetworkLoadBalancerRequest\x1a!.yandex.cloud.operation.Operation\"\x88\x01\xb2\xd2*8\n!UpdateNetworkLoadBalancerMetadata\x12\x13NetworkLoadBalancer\x82\xd3\xe4\x93\x02\x46\x32\x41/load-balancer/v1/networkLoadBalancers/{network_load_balancer_id}:\x01*\x12\xf5\x01\n\x06\x44\x65lete\x12>.yandex.cloud.loadbalancer.v1.DeleteNetworkLoadBalancerRequest\x1a!.yandex.cloud.operation.Operation\"\x87\x01\xb2\xd2*:\n!DeleteNetworkLoadBalancerMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x43*A/load-balancer/v1/networkLoadBalancers/{network_load_balancer_id}\x12\xf8\x01\n\x05Start\x12=.yandex.cloud.loadbalancer.v1.StartNetworkLoadBalancerRequest\x1a!.yandex.cloud.operation.Operation\"\x8c\x01\xb2\xd2*9\n StartNetworkLoadBalancerMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02I\"G/load-balancer/v1/networkLoadBalancers/{network_load_balancer_id}:start\x12\xf4\x01\n\x04Stop\x12<.yandex.cloud.loadbalancer.v1.StopNetworkLoadBalancerRequest\x1a!.yandex.cloud.operation.Operation\"\x8a\x01\xb2\xd2*8\n\x1fStopNetworkLoadBalancerMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02H\"F/load-balancer/v1/networkLoadBalancers/{network_load_balancer_id}:stop\x12\xa9\x02\n\x11\x41ttachTargetGroup\x12I.yandex.cloud.loadbalancer.v1.AttachNetworkLoadBalancerTargetGroupRequest\x1a!.yandex.cloud.operation.Operation\"\xa5\x01\xb2\xd2*C\n,AttachNetworkLoadBalancerTargetGroupMetadata\x12\x13NetworkLoadBalancer\x82\xd3\xe4\x93\x02X\"S/load-balancer/v1/networkLoadBalancers/{network_load_balancer_id}:attachTargetGroup:\x01*\x12\xa9\x02\n\x11\x44\x65tachTargetGroup\x12I.yandex.cloud.loadbalancer.v1.DetachNetworkLoadBalancerTargetGroupRequest\x1a!.yandex.cloud.operation.Operation\"\xa5\x01\xb2\xd2*C\n,DetachNetworkLoadBalancerTargetGroupMetadata\x12\x13NetworkLoadBalancer\x82\xd3\xe4\x93\x02X\"S/load-balancer/v1/networkLoadBalancers/{network_load_balancer_id}:detachTargetGroup:\x01*\x12\xd9\x01\n\x0fGetTargetStates\x12\x34.yandex.cloud.loadbalancer.v1.GetTargetStatesRequest\x1a\x35.yandex.cloud.loadbalancer.v1.GetTargetStatesResponse\"Y\x82\xd3\xe4\x93\x02S\x12Q/load-balancer/v1/networkLoadBalancers/{network_load_balancer_id}:getTargetStates\x12\x91\x02\n\x0b\x41\x64\x64Listener\x12\x43.yandex.cloud.loadbalancer.v1.AddNetworkLoadBalancerListenerRequest\x1a!.yandex.cloud.operation.Operation\"\x99\x01\xb2\xd2*=\n&AddNetworkLoadBalancerListenerMetadata\x12\x13NetworkLoadBalancer\x82\xd3\xe4\x93\x02R\"M/load-balancer/v1/networkLoadBalancers/{network_load_balancer_id}:addListener:\x01*\x12\x9d\x02\n\x0eRemoveListener\x12\x46.yandex.cloud.loadbalancer.v1.RemoveNetworkLoadBalancerListenerRequest\x1a!.yandex.cloud.operation.Operation\"\x9f\x01\xb2\xd2*@\n)RemoveNetworkLoadBalancerListenerMetadata\x12\x13NetworkLoadBalancer\x82\xd3\xe4\x93\x02U\"P/load-balancer/v1/networkLoadBalancers/{network_load_balancer_id}:removeListener:\x01*\x12\xf7\x01\n\x0eListOperations\x12\x46.yandex.cloud.loadbalancer.v1.ListNetworkLoadBalancerOperationsRequest\x1aG.yandex.cloud.loadbalancer.v1.ListNetworkLoadBalancerOperationsResponse\"T\x82\xd3\xe4\x93\x02N\x12L/load-balancer/v1/networkLoadBalancers/{network_load_balancer_id}/operationsBq\n yandex.cloud.api.loadbalancer.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/loadbalancer/v1;loadbalancerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.loadbalancer.v1.network_load_balancer_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n yandex.cloud.api.loadbalancer.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/loadbalancer/v1;loadbalancer'
  _globals['_GETNETWORKLOADBALANCERREQUEST'].fields_by_name['network_load_balancer_id']._loaded_options = None
  _globals['_GETNETWORKLOADBALANCERREQUEST'].fields_by_name['network_load_balancer_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_LISTNETWORKLOADBALANCERSREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_LISTNETWORKLOADBALANCERSREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTNETWORKLOADBALANCERSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTNETWORKLOADBALANCERSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTNETWORKLOADBALANCERSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTNETWORKLOADBALANCERSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTNETWORKLOADBALANCERSREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTNETWORKLOADBALANCERSREQUEST'].fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _globals['_CREATENETWORKLOADBALANCERREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_CREATENETWORKLOADBALANCERREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_CREATENETWORKLOADBALANCERREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_CREATENETWORKLOADBALANCERREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_CREATENETWORKLOADBALANCERREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_CREATENETWORKLOADBALANCERREQUEST'].fields_by_name['name']._serialized_options = b'\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _globals['_CREATENETWORKLOADBALANCERREQUEST'].fields_by_name['description']._loaded_options = None
  _globals['_CREATENETWORKLOADBALANCERREQUEST'].fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _globals['_CREATENETWORKLOADBALANCERREQUEST'].fields_by_name['labels']._loaded_options = None
  _globals['_CREATENETWORKLOADBALANCERREQUEST'].fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\0041-63'
  _globals['_CREATENETWORKLOADBALANCERREQUEST'].fields_by_name['region_id']._loaded_options = None
  _globals['_CREATENETWORKLOADBALANCERREQUEST'].fields_by_name['region_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_CREATENETWORKLOADBALANCERREQUEST'].fields_by_name['type']._loaded_options = None
  _globals['_CREATENETWORKLOADBALANCERREQUEST'].fields_by_name['type']._serialized_options = b'\350\3071\001'
  _globals['_CREATENETWORKLOADBALANCERREQUEST'].fields_by_name['listener_specs']._loaded_options = None
  _globals['_CREATENETWORKLOADBALANCERREQUEST'].fields_by_name['listener_specs']._serialized_options = b'\202\3101\006<=1000'
  _globals['_CREATENETWORKLOADBALANCERREQUEST'].fields_by_name['attached_target_groups']._loaded_options = None
  _globals['_CREATENETWORKLOADBALANCERREQUEST'].fields_by_name['attached_target_groups']._serialized_options = b'\202\3101\006<=1000'
  _globals['_UPDATENETWORKLOADBALANCERREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_UPDATENETWORKLOADBALANCERREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_UPDATENETWORKLOADBALANCERREQUEST'].fields_by_name['network_load_balancer_id']._loaded_options = None
  _globals['_UPDATENETWORKLOADBALANCERREQUEST'].fields_by_name['network_load_balancer_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_UPDATENETWORKLOADBALANCERREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_UPDATENETWORKLOADBALANCERREQUEST'].fields_by_name['name']._serialized_options = b'\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _globals['_UPDATENETWORKLOADBALANCERREQUEST'].fields_by_name['description']._loaded_options = None
  _globals['_UPDATENETWORKLOADBALANCERREQUEST'].fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _globals['_UPDATENETWORKLOADBALANCERREQUEST'].fields_by_name['labels']._loaded_options = None
  _globals['_UPDATENETWORKLOADBALANCERREQUEST'].fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\0041-63'
  _globals['_UPDATENETWORKLOADBALANCERREQUEST'].fields_by_name['listener_specs']._loaded_options = None
  _globals['_UPDATENETWORKLOADBALANCERREQUEST'].fields_by_name['listener_specs']._serialized_options = b'\202\3101\006<=1000'
  _globals['_UPDATENETWORKLOADBALANCERREQUEST'].fields_by_name['attached_target_groups']._loaded_options = None
  _globals['_UPDATENETWORKLOADBALANCERREQUEST'].fields_by_name['attached_target_groups']._serialized_options = b'\202\3101\006<=1000'
  _globals['_DELETENETWORKLOADBALANCERREQUEST'].fields_by_name['network_load_balancer_id']._loaded_options = None
  _globals['_DELETENETWORKLOADBALANCERREQUEST'].fields_by_name['network_load_balancer_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_STARTNETWORKLOADBALANCERREQUEST'].fields_by_name['network_load_balancer_id']._loaded_options = None
  _globals['_STARTNETWORKLOADBALANCERREQUEST'].fields_by_name['network_load_balancer_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_STOPNETWORKLOADBALANCERREQUEST'].fields_by_name['network_load_balancer_id']._loaded_options = None
  _globals['_STOPNETWORKLOADBALANCERREQUEST'].fields_by_name['network_load_balancer_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_ATTACHNETWORKLOADBALANCERTARGETGROUPREQUEST'].fields_by_name['network_load_balancer_id']._loaded_options = None
  _globals['_ATTACHNETWORKLOADBALANCERTARGETGROUPREQUEST'].fields_by_name['network_load_balancer_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_ATTACHNETWORKLOADBALANCERTARGETGROUPREQUEST'].fields_by_name['attached_target_group']._loaded_options = None
  _globals['_ATTACHNETWORKLOADBALANCERTARGETGROUPREQUEST'].fields_by_name['attached_target_group']._serialized_options = b'\350\3071\001'
  _globals['_DETACHNETWORKLOADBALANCERTARGETGROUPREQUEST'].fields_by_name['network_load_balancer_id']._loaded_options = None
  _globals['_DETACHNETWORKLOADBALANCERTARGETGROUPREQUEST'].fields_by_name['network_load_balancer_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_DETACHNETWORKLOADBALANCERTARGETGROUPREQUEST'].fields_by_name['target_group_id']._loaded_options = None
  _globals['_DETACHNETWORKLOADBALANCERTARGETGROUPREQUEST'].fields_by_name['target_group_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_ADDNETWORKLOADBALANCERLISTENERREQUEST'].fields_by_name['network_load_balancer_id']._loaded_options = None
  _globals['_ADDNETWORKLOADBALANCERLISTENERREQUEST'].fields_by_name['network_load_balancer_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_ADDNETWORKLOADBALANCERLISTENERREQUEST'].fields_by_name['listener_spec']._loaded_options = None
  _globals['_ADDNETWORKLOADBALANCERLISTENERREQUEST'].fields_by_name['listener_spec']._serialized_options = b'\350\3071\001'
  _globals['_REMOVENETWORKLOADBALANCERLISTENERREQUEST'].fields_by_name['network_load_balancer_id']._loaded_options = None
  _globals['_REMOVENETWORKLOADBALANCERLISTENERREQUEST'].fields_by_name['network_load_balancer_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_REMOVENETWORKLOADBALANCERLISTENERREQUEST'].fields_by_name['listener_name']._loaded_options = None
  _globals['_REMOVENETWORKLOADBALANCERLISTENERREQUEST'].fields_by_name['listener_name']._serialized_options = b'\350\3071\001\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _globals['_LISTNETWORKLOADBALANCEROPERATIONSREQUEST'].fields_by_name['network_load_balancer_id']._loaded_options = None
  _globals['_LISTNETWORKLOADBALANCEROPERATIONSREQUEST'].fields_by_name['network_load_balancer_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTNETWORKLOADBALANCEROPERATIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTNETWORKLOADBALANCEROPERATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTNETWORKLOADBALANCEROPERATIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTNETWORKLOADBALANCEROPERATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_GETTARGETSTATESREQUEST'].fields_by_name['network_load_balancer_id']._loaded_options = None
  _globals['_GETTARGETSTATESREQUEST'].fields_by_name['network_load_balancer_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_GETTARGETSTATESREQUEST'].fields_by_name['target_group_id']._loaded_options = None
  _globals['_GETTARGETSTATESREQUEST'].fields_by_name['target_group_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_LISTENERSPEC'].fields_by_name['name']._loaded_options = None
  _globals['_LISTENERSPEC'].fields_by_name['name']._serialized_options = b'\350\3071\001\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _globals['_LISTENERSPEC'].fields_by_name['port']._loaded_options = None
  _globals['_LISTENERSPEC'].fields_by_name['port']._serialized_options = b'\372\3071\0071-65535'
  _globals['_LISTENERSPEC'].fields_by_name['protocol']._loaded_options = None
  _globals['_LISTENERSPEC'].fields_by_name['protocol']._serialized_options = b'\350\3071\001'
  _globals['_NETWORKLOADBALANCERSERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_NETWORKLOADBALANCERSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002C\022A/load-balancer/v1/networkLoadBalancers/{network_load_balancer_id}'
  _globals['_NETWORKLOADBALANCERSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_NETWORKLOADBALANCERSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002(\022&/load-balancer/v1/networkLoadBalancers'
  _globals['_NETWORKLOADBALANCERSERVICE'].methods_by_name['Create']._loaded_options = None
  _globals['_NETWORKLOADBALANCERSERVICE'].methods_by_name['Create']._serialized_options = b'\262\322*8\n!CreateNetworkLoadBalancerMetadata\022\023NetworkLoadBalancer\202\323\344\223\002+\"&/load-balancer/v1/networkLoadBalancers:\001*'
  _globals['_NETWORKLOADBALANCERSERVICE'].methods_by_name['Update']._loaded_options = None
  _globals['_NETWORKLOADBALANCERSERVICE'].methods_by_name['Update']._serialized_options = b'\262\322*8\n!UpdateNetworkLoadBalancerMetadata\022\023NetworkLoadBalancer\202\323\344\223\002F2A/load-balancer/v1/networkLoadBalancers/{network_load_balancer_id}:\001*'
  _globals['_NETWORKLOADBALANCERSERVICE'].methods_by_name['Delete']._loaded_options = None
  _globals['_NETWORKLOADBALANCERSERVICE'].methods_by_name['Delete']._serialized_options = b'\262\322*:\n!DeleteNetworkLoadBalancerMetadata\022\025google.protobuf.Empty\202\323\344\223\002C*A/load-balancer/v1/networkLoadBalancers/{network_load_balancer_id}'
  _globals['_NETWORKLOADBALANCERSERVICE'].methods_by_name['Start']._loaded_options = None
  _globals['_NETWORKLOADBALANCERSERVICE'].methods_by_name['Start']._serialized_options = b'\262\322*9\n StartNetworkLoadBalancerMetadata\022\025google.protobuf.Empty\202\323\344\223\002I\"G/load-balancer/v1/networkLoadBalancers/{network_load_balancer_id}:start'
  _globals['_NETWORKLOADBALANCERSERVICE'].methods_by_name['Stop']._loaded_options = None
  _globals['_NETWORKLOADBALANCERSERVICE'].methods_by_name['Stop']._serialized_options = b'\262\322*8\n\037StopNetworkLoadBalancerMetadata\022\025google.protobuf.Empty\202\323\344\223\002H\"F/load-balancer/v1/networkLoadBalancers/{network_load_balancer_id}:stop'
  _globals['_NETWORKLOADBALANCERSERVICE'].methods_by_name['AttachTargetGroup']._loaded_options = None
  _globals['_NETWORKLOADBALANCERSERVICE'].methods_by_name['AttachTargetGroup']._serialized_options = b'\262\322*C\n,AttachNetworkLoadBalancerTargetGroupMetadata\022\023NetworkLoadBalancer\202\323\344\223\002X\"S/load-balancer/v1/networkLoadBalancers/{network_load_balancer_id}:attachTargetGroup:\001*'
  _globals['_NETWORKLOADBALANCERSERVICE'].methods_by_name['DetachTargetGroup']._loaded_options = None
  _globals['_NETWORKLOADBALANCERSERVICE'].methods_by_name['DetachTargetGroup']._serialized_options = b'\262\322*C\n,DetachNetworkLoadBalancerTargetGroupMetadata\022\023NetworkLoadBalancer\202\323\344\223\002X\"S/load-balancer/v1/networkLoadBalancers/{network_load_balancer_id}:detachTargetGroup:\001*'
  _globals['_NETWORKLOADBALANCERSERVICE'].methods_by_name['GetTargetStates']._loaded_options = None
  _globals['_NETWORKLOADBALANCERSERVICE'].methods_by_name['GetTargetStates']._serialized_options = b'\202\323\344\223\002S\022Q/load-balancer/v1/networkLoadBalancers/{network_load_balancer_id}:getTargetStates'
  _globals['_NETWORKLOADBALANCERSERVICE'].methods_by_name['AddListener']._loaded_options = None
  _globals['_NETWORKLOADBALANCERSERVICE'].methods_by_name['AddListener']._serialized_options = b'\262\322*=\n&AddNetworkLoadBalancerListenerMetadata\022\023NetworkLoadBalancer\202\323\344\223\002R\"M/load-balancer/v1/networkLoadBalancers/{network_load_balancer_id}:addListener:\001*'
  _globals['_NETWORKLOADBALANCERSERVICE'].methods_by_name['RemoveListener']._loaded_options = None
  _globals['_NETWORKLOADBALANCERSERVICE'].methods_by_name['RemoveListener']._serialized_options = b'\262\322*@\n)RemoveNetworkLoadBalancerListenerMetadata\022\023NetworkLoadBalancer\202\323\344\223\002U\"P/load-balancer/v1/networkLoadBalancers/{network_load_balancer_id}:removeListener:\001*'
  _globals['_NETWORKLOADBALANCERSERVICE'].methods_by_name['ListOperations']._loaded_options = None
  _globals['_NETWORKLOADBALANCERSERVICE'].methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\002N\022L/load-balancer/v1/networkLoadBalancers/{network_load_balancer_id}/operations'
  _globals['_GETNETWORKLOADBALANCERREQUEST']._serialized_start=325
  _globals['_GETNETWORKLOADBALANCERREQUEST']._serialized_end=400
  _globals['_LISTNETWORKLOADBALANCERSREQUEST']._serialized_start=403
  _globals['_LISTNETWORKLOADBALANCERSREQUEST']._serialized_end=559
  _globals['_LISTNETWORKLOADBALANCERSRESPONSE']._serialized_start=562
  _globals['_LISTNETWORKLOADBALANCERSRESPONSE']._serialized_end=704
  _globals['_CREATENETWORKLOADBALANCERREQUEST']._serialized_start=707
  _globals['_CREATENETWORKLOADBALANCERREQUEST']._serialized_end=1392
  _globals['_CREATENETWORKLOADBALANCERREQUEST_LABELSENTRY']._serialized_start=1347
  _globals['_CREATENETWORKLOADBALANCERREQUEST_LABELSENTRY']._serialized_end=1392
  _globals['_CREATENETWORKLOADBALANCERMETADATA']._serialized_start=1394
  _globals['_CREATENETWORKLOADBALANCERMETADATA']._serialized_end=1463
  _globals['_UPDATENETWORKLOADBALANCERREQUEST']._serialized_start=1466
  _globals['_UPDATENETWORKLOADBALANCERREQUEST']._serialized_end=2110
  _globals['_UPDATENETWORKLOADBALANCERREQUEST_LABELSENTRY']._serialized_start=1347
  _globals['_UPDATENETWORKLOADBALANCERREQUEST_LABELSENTRY']._serialized_end=1392
  _globals['_UPDATENETWORKLOADBALANCERMETADATA']._serialized_start=2112
  _globals['_UPDATENETWORKLOADBALANCERMETADATA']._serialized_end=2181
  _globals['_DELETENETWORKLOADBALANCERREQUEST']._serialized_start=2183
  _globals['_DELETENETWORKLOADBALANCERREQUEST']._serialized_end=2265
  _globals['_DELETENETWORKLOADBALANCERMETADATA']._serialized_start=2267
  _globals['_DELETENETWORKLOADBALANCERMETADATA']._serialized_end=2336
  _globals['_STARTNETWORKLOADBALANCERREQUEST']._serialized_start=2338
  _globals['_STARTNETWORKLOADBALANCERREQUEST']._serialized_end=2419
  _globals['_STARTNETWORKLOADBALANCERMETADATA']._serialized_start=2421
  _globals['_STARTNETWORKLOADBALANCERMETADATA']._serialized_end=2489
  _globals['_STOPNETWORKLOADBALANCERREQUEST']._serialized_start=2491
  _globals['_STOPNETWORKLOADBALANCERREQUEST']._serialized_end=2571
  _globals['_STOPNETWORKLOADBALANCERMETADATA']._serialized_start=2573
  _globals['_STOPNETWORKLOADBALANCERMETADATA']._serialized_end=2640
  _globals['_ATTACHNETWORKLOADBALANCERTARGETGROUPREQUEST']._serialized_start=2643
  _globals['_ATTACHNETWORKLOADBALANCERTARGETGROUPREQUEST']._serialized_end=2824
  _globals['_ATTACHNETWORKLOADBALANCERTARGETGROUPMETADATA']._serialized_start=2826
  _globals['_ATTACHNETWORKLOADBALANCERTARGETGROUPMETADATA']._serialized_end=2931
  _globals['_DETACHNETWORKLOADBALANCERTARGETGROUPREQUEST']._serialized_start=2934
  _globals['_DETACHNETWORKLOADBALANCERTARGETGROUPREQUEST']._serialized_end=3066
  _globals['_DETACHNETWORKLOADBALANCERTARGETGROUPMETADATA']._serialized_start=3068
  _globals['_DETACHNETWORKLOADBALANCERTARGETGROUPMETADATA']._serialized_end=3173
  _globals['_ADDNETWORKLOADBALANCERLISTENERREQUEST']._serialized_start=3176
  _globals['_ADDNETWORKLOADBALANCERLISTENERREQUEST']._serialized_end=3336
  _globals['_ADDNETWORKLOADBALANCERLISTENERMETADATA']._serialized_start=3338
  _globals['_ADDNETWORKLOADBALANCERLISTENERMETADATA']._serialized_end=3412
  _globals['_REMOVENETWORKLOADBALANCERLISTENERREQUEST']._serialized_start=3415
  _globals['_REMOVENETWORKLOADBALANCERLISTENERREQUEST']._serialized_end=3567
  _globals['_REMOVENETWORKLOADBALANCERLISTENERMETADATA']._serialized_start=3569
  _globals['_REMOVENETWORKLOADBALANCERLISTENERMETADATA']._serialized_end=3646
  _globals['_LISTNETWORKLOADBALANCEROPERATIONSREQUEST']._serialized_start=3649
  _globals['_LISTNETWORKLOADBALANCEROPERATIONSREQUEST']._serialized_end=3801
  _globals['_LISTNETWORKLOADBALANCEROPERATIONSRESPONSE']._serialized_start=3803
  _globals['_LISTNETWORKLOADBALANCEROPERATIONSRESPONSE']._serialized_end=3926
  _globals['_GETTARGETSTATESREQUEST']._serialized_start=3928
  _globals['_GETTARGETSTATESREQUEST']._serialized_end=4031
  _globals['_GETTARGETSTATESRESPONSE']._serialized_start=4033
  _globals['_GETTARGETSTATESRESPONSE']._serialized_end=4124
  _globals['_EXTERNALADDRESSSPEC']._serialized_start=4126
  _globals['_EXTERNALADDRESSSPEC']._serialized_end=4225
  _globals['_INTERNALADDRESSSPEC']._serialized_start=4227
  _globals['_INTERNALADDRESSSPEC']._serialized_end=4345
  _globals['_LISTENERSPEC']._serialized_start=4348
  _globals['_LISTENERSPEC']._serialized_end=4715
  _globals['_NETWORKLOADBALANCERSERVICE']._serialized_start=4718
  _globals['_NETWORKLOADBALANCERSERVICE']._serialized_end=7975
# @@protoc_insertion_point(module_scope)
