# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/iot/broker/v1/broker.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'yandex/cloud/iot/broker/v1/broker.proto\x12\x1ayandex.cloud.iot.broker.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\xee\x02\n\x06\x42roker\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12>\n\x06labels\x18\x06 \x03(\x0b\x32..yandex.cloud.iot.broker.v1.Broker.LabelsEntry\x12\x39\n\x06status\x18\x07 \x01(\x0e\x32).yandex.cloud.iot.broker.v1.Broker.Status\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"H\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12\x0c\n\x08\x44\x45LETING\x10\x03\"\x85\x01\n\x11\x42rokerCertificate\x12\x11\n\tbroker_id\x18\x01 \x01(\t\x12\x13\n\x0b\x66ingerprint\x18\x02 \x01(\t\x12\x18\n\x10\x63\x65rtificate_data\x18\x03 \x01(\t\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"_\n\x0e\x42rokerPassword\x12\x11\n\tbroker_id\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampBg\n\x1eyandex.cloud.api.iot.broker.v1ZEgithub.com/yandex-cloud/go-genproto/yandex/cloud/iot/broker/v1;brokerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.iot.broker.v1.broker_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\036yandex.cloud.api.iot.broker.v1ZEgithub.com/yandex-cloud/go-genproto/yandex/cloud/iot/broker/v1;broker'
  _BROKER_LABELSENTRY._options = None
  _BROKER_LABELSENTRY._serialized_options = b'8\001'
  _globals['_BROKER']._serialized_start=105
  _globals['_BROKER']._serialized_end=471
  _globals['_BROKER_LABELSENTRY']._serialized_start=352
  _globals['_BROKER_LABELSENTRY']._serialized_end=397
  _globals['_BROKER_STATUS']._serialized_start=399
  _globals['_BROKER_STATUS']._serialized_end=471
  _globals['_BROKERCERTIFICATE']._serialized_start=474
  _globals['_BROKERCERTIFICATE']._serialized_end=607
  _globals['_BROKERPASSWORD']._serialized_start=609
  _globals['_BROKERPASSWORD']._serialized_end=704
# @@protoc_insertion_point(module_scope)
