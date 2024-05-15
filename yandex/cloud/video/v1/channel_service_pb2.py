# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/video/v1/channel_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.video.v1 import channel_pb2 as yandex_dot_cloud_dot_video_dot_v1_dot_channel__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+yandex/cloud/video/v1/channel_service.proto\x12\x15yandex.cloud.video.v1\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a#yandex/cloud/video/v1/channel.proto\"\'\n\x11GetChannelRequest\x12\x12\n\nchannel_id\x18\x01 \x01(\t\"w\n\x13ListChannelsRequest\x12\x17\n\x0forganization_id\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x64 \x01(\x03\x12\x12\n\npage_token\x18\x65 \x01(\t\x12\x10\n\x08order_by\x18\x66 \x01(\t\x12\x0e\n\x06\x66ilter\x18g \x01(\t\"a\n\x14ListChannelsResponse\x12\x30\n\x08\x63hannels\x18\x01 \x03(\x0b\x32\x1e.yandex.cloud.video.v1.Channel\x12\x17\n\x0fnext_page_token\x18\x64 \x01(\t\"\xcc\x01\n\x14\x43reateChannelRequest\x12\x17\n\x0forganization_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12H\n\x06labels\x18\xc8\x01 \x03(\x0b\x32\x37.yandex.cloud.video.v1.CreateChannelRequest.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"+\n\x15\x43reateChannelMetadata\x12\x12\n\nchannel_id\x18\x01 \x01(\t\"\xf7\x01\n\x14UpdateChannelRequest\x12\x12\n\nchannel_id\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\r\n\x05title\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12H\n\x06labels\x18\xc8\x01 \x03(\x0b\x32\x37.yandex.cloud.video.v1.UpdateChannelRequest.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"+\n\x15UpdateChannelMetadata\x12\x12\n\nchannel_id\x18\x01 \x01(\t\"*\n\x14\x44\x65leteChannelRequest\x12\x12\n\nchannel_id\x18\x01 \x01(\t\"+\n\x15\x44\x65leteChannelMetadata\x12\x12\n\nchannel_id\x18\x01 \x01(\t2\xd5\x04\n\x0e\x43hannelService\x12Q\n\x03Get\x12(.yandex.cloud.video.v1.GetChannelRequest\x1a\x1e.yandex.cloud.video.v1.Channel\"\x00\x12\x61\n\x04List\x12*.yandex.cloud.video.v1.ListChannelsRequest\x1a+.yandex.cloud.video.v1.ListChannelsResponse\"\x00\x12~\n\x06\x43reate\x12+.yandex.cloud.video.v1.CreateChannelRequest\x1a!.yandex.cloud.operation.Operation\"$\xb2\xd2* \n\x15\x43reateChannelMetadata\x12\x07\x43hannel\x12~\n\x06Update\x12+.yandex.cloud.video.v1.UpdateChannelRequest\x1a!.yandex.cloud.operation.Operation\"$\xb2\xd2* \n\x15UpdateChannelMetadata\x12\x07\x43hannel\x12\x8c\x01\n\x06\x44\x65lete\x12+.yandex.cloud.video.v1.DeleteChannelRequest\x1a!.yandex.cloud.operation.Operation\"2\xb2\xd2*.\n\x15\x44\x65leteChannelMetadata\x12\x15google.protobuf.EmptyB\\\n\x19yandex.cloud.api.video.v1Z?github.com/yandex-cloud/go-genproto/yandex/cloud/video/v1;videob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.video.v1.channel_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031yandex.cloud.api.video.v1Z?github.com/yandex-cloud/go-genproto/yandex/cloud/video/v1;video'
  _globals['_CREATECHANNELREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_CREATECHANNELREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_UPDATECHANNELREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_UPDATECHANNELREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_CHANNELSERVICE'].methods_by_name['Create']._loaded_options = None
  _globals['_CHANNELSERVICE'].methods_by_name['Create']._serialized_options = b'\262\322* \n\025CreateChannelMetadata\022\007Channel'
  _globals['_CHANNELSERVICE'].methods_by_name['Update']._loaded_options = None
  _globals['_CHANNELSERVICE'].methods_by_name['Update']._serialized_options = b'\262\322* \n\025UpdateChannelMetadata\022\007Channel'
  _globals['_CHANNELSERVICE'].methods_by_name['Delete']._loaded_options = None
  _globals['_CHANNELSERVICE'].methods_by_name['Delete']._serialized_options = b'\262\322*.\n\025DeleteChannelMetadata\022\025google.protobuf.Empty'
  _globals['_GETCHANNELREQUEST']._serialized_start=215
  _globals['_GETCHANNELREQUEST']._serialized_end=254
  _globals['_LISTCHANNELSREQUEST']._serialized_start=256
  _globals['_LISTCHANNELSREQUEST']._serialized_end=375
  _globals['_LISTCHANNELSRESPONSE']._serialized_start=377
  _globals['_LISTCHANNELSRESPONSE']._serialized_end=474
  _globals['_CREATECHANNELREQUEST']._serialized_start=477
  _globals['_CREATECHANNELREQUEST']._serialized_end=681
  _globals['_CREATECHANNELREQUEST_LABELSENTRY']._serialized_start=636
  _globals['_CREATECHANNELREQUEST_LABELSENTRY']._serialized_end=681
  _globals['_CREATECHANNELMETADATA']._serialized_start=683
  _globals['_CREATECHANNELMETADATA']._serialized_end=726
  _globals['_UPDATECHANNELREQUEST']._serialized_start=729
  _globals['_UPDATECHANNELREQUEST']._serialized_end=976
  _globals['_UPDATECHANNELREQUEST_LABELSENTRY']._serialized_start=636
  _globals['_UPDATECHANNELREQUEST_LABELSENTRY']._serialized_end=681
  _globals['_UPDATECHANNELMETADATA']._serialized_start=978
  _globals['_UPDATECHANNELMETADATA']._serialized_end=1021
  _globals['_DELETECHANNELREQUEST']._serialized_start=1023
  _globals['_DELETECHANNELREQUEST']._serialized_end=1065
  _globals['_DELETECHANNELMETADATA']._serialized_start=1067
  _globals['_DELETECHANNELMETADATA']._serialized_end=1110
  _globals['_CHANNELSERVICE']._serialized_start=1113
  _globals['_CHANNELSERVICE']._serialized_end=1710
# @@protoc_insertion_point(module_scope)
