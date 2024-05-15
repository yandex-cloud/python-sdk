# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/video/v1/stream_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.video.v1 import stream_pb2 as yandex_dot_cloud_dot_video_dot_v1_dot_stream__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*yandex/cloud/video/v1/stream_service.proto\x12\x15yandex.cloud.video.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\"yandex/cloud/video/v1/stream.proto\"%\n\x10GetStreamRequest\x12\x11\n\tstream_id\x18\x01 \x01(\t\"q\n\x12ListStreamsRequest\x12\x12\n\nchannel_id\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x64 \x01(\x03\x12\x12\n\npage_token\x18\x65 \x01(\t\x12\x10\n\x08order_by\x18\x66 \x01(\t\x12\x0e\n\x06\x66ilter\x18g \x01(\t\"^\n\x13ListStreamsResponse\x12.\n\x07streams\x18\x01 \x03(\x0b\x32\x1d.yandex.cloud.video.v1.Stream\x12\x17\n\x0fnext_page_token\x18\x64 \x01(\t\"\xf4\x02\n\x13\x43reateStreamRequest\x12\x12\n\nchannel_id\x18\x01 \x01(\t\x12\x0f\n\x07line_id\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x14\n\x0cthumbnail_id\x18\x05 \x01(\t\x12G\n\x06labels\x18\xc8\x01 \x03(\x0b\x32\x36.yandex.cloud.video.v1.CreateStreamRequest.LabelsEntry\x12;\n\ton_demand\x18\xe8\x07 \x01(\x0b\x32%.yandex.cloud.video.v1.OnDemandParamsH\x00\x12:\n\x08schedule\x18\xe9\x07 \x01(\x0b\x32%.yandex.cloud.video.v1.ScheduleParamsH\x00\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\r\n\x0bstream_type\"\x10\n\x0eOnDemandParams\"q\n\x0eScheduleParams\x12.\n\nstart_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x66inish_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\")\n\x14\x43reateStreamMetadata\x12\x11\n\tstream_id\x18\x01 \x01(\t\"\xa3\x03\n\x13UpdateStreamRequest\x12\x11\n\tstream_id\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x0f\n\x07line_id\x18\x03 \x01(\t\x12\r\n\x05title\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x14\n\x0cthumbnail_id\x18\x06 \x01(\t\x12G\n\x06labels\x18\xc8\x01 \x03(\x0b\x32\x36.yandex.cloud.video.v1.UpdateStreamRequest.LabelsEntry\x12;\n\ton_demand\x18\xe8\x07 \x01(\x0b\x32%.yandex.cloud.video.v1.OnDemandParamsH\x00\x12:\n\x08schedule\x18\xe9\x07 \x01(\x0b\x32%.yandex.cloud.video.v1.ScheduleParamsH\x00\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\r\n\x0bstream_type\")\n\x14UpdateStreamMetadata\x12\x11\n\tstream_id\x18\x01 \x01(\t\"(\n\x13\x44\x65leteStreamRequest\x12\x11\n\tstream_id\x18\x01 \x01(\t\")\n\x14\x44\x65leteStreamMetadata\x12\x11\n\tstream_id\x18\x01 \x01(\t\"\xaf\x01\n\x1aPerformStreamActionRequest\x12\x11\n\tstream_id\x18\x01 \x01(\t\x12\x38\n\x07publish\x18\xe8\x07 \x01(\x0b\x32$.yandex.cloud.video.v1.PublishActionH\x00\x12\x32\n\x04stop\x18\xea\x07 \x01(\x0b\x32!.yandex.cloud.video.v1.StopActionH\x00\x42\x08\n\x06\x61\x63tionJ\x06\x08\xe9\x07\x10\xea\x07\"\x0f\n\rPublishAction\"\x0c\n\nStopAction\"0\n\x1bPerformStreamActionMetadata\x12\x11\n\tstream_id\x18\x01 \x01(\t2\xdb\x05\n\rStreamService\x12O\n\x03Get\x12\'.yandex.cloud.video.v1.GetStreamRequest\x1a\x1d.yandex.cloud.video.v1.Stream\"\x00\x12_\n\x04List\x12).yandex.cloud.video.v1.ListStreamsRequest\x1a*.yandex.cloud.video.v1.ListStreamsResponse\"\x00\x12{\n\x06\x43reate\x12*.yandex.cloud.video.v1.CreateStreamRequest\x1a!.yandex.cloud.operation.Operation\"\"\xb2\xd2*\x1e\n\x14\x43reateStreamMetadata\x12\x06Stream\x12{\n\x06Update\x12*.yandex.cloud.video.v1.UpdateStreamRequest\x1a!.yandex.cloud.operation.Operation\"\"\xb2\xd2*\x1e\n\x14UpdateStreamMetadata\x12\x06Stream\x12\x8a\x01\n\x06\x44\x65lete\x12*.yandex.cloud.video.v1.DeleteStreamRequest\x1a!.yandex.cloud.operation.Operation\"1\xb2\xd2*-\n\x14\x44\x65leteStreamMetadata\x12\x15google.protobuf.Empty\x12\x90\x01\n\rPerformAction\x12\x31.yandex.cloud.video.v1.PerformStreamActionRequest\x1a!.yandex.cloud.operation.Operation\")\xb2\xd2*%\n\x1bPerformStreamActionMetadata\x12\x06StreamB\\\n\x19yandex.cloud.api.video.v1Z?github.com/yandex-cloud/go-genproto/yandex/cloud/video/v1;videob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.video.v1.stream_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031yandex.cloud.api.video.v1Z?github.com/yandex-cloud/go-genproto/yandex/cloud/video/v1;video'
  _CREATESTREAMREQUEST_LABELSENTRY._options = None
  _CREATESTREAMREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _UPDATESTREAMREQUEST_LABELSENTRY._options = None
  _UPDATESTREAMREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _STREAMSERVICE.methods_by_name['Create']._options = None
  _STREAMSERVICE.methods_by_name['Create']._serialized_options = b'\262\322*\036\n\024CreateStreamMetadata\022\006Stream'
  _STREAMSERVICE.methods_by_name['Update']._options = None
  _STREAMSERVICE.methods_by_name['Update']._serialized_options = b'\262\322*\036\n\024UpdateStreamMetadata\022\006Stream'
  _STREAMSERVICE.methods_by_name['Delete']._options = None
  _STREAMSERVICE.methods_by_name['Delete']._serialized_options = b'\262\322*-\n\024DeleteStreamMetadata\022\025google.protobuf.Empty'
  _STREAMSERVICE.methods_by_name['PerformAction']._options = None
  _STREAMSERVICE.methods_by_name['PerformAction']._serialized_options = b'\262\322*%\n\033PerformStreamActionMetadata\022\006Stream'
  _globals['_GETSTREAMREQUEST']._serialized_start=246
  _globals['_GETSTREAMREQUEST']._serialized_end=283
  _globals['_LISTSTREAMSREQUEST']._serialized_start=285
  _globals['_LISTSTREAMSREQUEST']._serialized_end=398
  _globals['_LISTSTREAMSRESPONSE']._serialized_start=400
  _globals['_LISTSTREAMSRESPONSE']._serialized_end=494
  _globals['_CREATESTREAMREQUEST']._serialized_start=497
  _globals['_CREATESTREAMREQUEST']._serialized_end=869
  _globals['_CREATESTREAMREQUEST_LABELSENTRY']._serialized_start=809
  _globals['_CREATESTREAMREQUEST_LABELSENTRY']._serialized_end=854
  _globals['_ONDEMANDPARAMS']._serialized_start=871
  _globals['_ONDEMANDPARAMS']._serialized_end=887
  _globals['_SCHEDULEPARAMS']._serialized_start=889
  _globals['_SCHEDULEPARAMS']._serialized_end=1002
  _globals['_CREATESTREAMMETADATA']._serialized_start=1004
  _globals['_CREATESTREAMMETADATA']._serialized_end=1045
  _globals['_UPDATESTREAMREQUEST']._serialized_start=1048
  _globals['_UPDATESTREAMREQUEST']._serialized_end=1467
  _globals['_UPDATESTREAMREQUEST_LABELSENTRY']._serialized_start=809
  _globals['_UPDATESTREAMREQUEST_LABELSENTRY']._serialized_end=854
  _globals['_UPDATESTREAMMETADATA']._serialized_start=1469
  _globals['_UPDATESTREAMMETADATA']._serialized_end=1510
  _globals['_DELETESTREAMREQUEST']._serialized_start=1512
  _globals['_DELETESTREAMREQUEST']._serialized_end=1552
  _globals['_DELETESTREAMMETADATA']._serialized_start=1554
  _globals['_DELETESTREAMMETADATA']._serialized_end=1595
  _globals['_PERFORMSTREAMACTIONREQUEST']._serialized_start=1598
  _globals['_PERFORMSTREAMACTIONREQUEST']._serialized_end=1773
  _globals['_PUBLISHACTION']._serialized_start=1775
  _globals['_PUBLISHACTION']._serialized_end=1790
  _globals['_STOPACTION']._serialized_start=1792
  _globals['_STOPACTION']._serialized_end=1804
  _globals['_PERFORMSTREAMACTIONMETADATA']._serialized_start=1806
  _globals['_PERFORMSTREAMACTIONMETADATA']._serialized_end=1854
  _globals['_STREAMSERVICE']._serialized_start=1857
  _globals['_STREAMSERVICE']._serialized_end=2588
# @@protoc_insertion_point(module_scope)
