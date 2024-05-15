# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/certificatemanager/v1/certificate.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4yandex/cloud/certificatemanager/v1/certificate.proto\x12\"yandex.cloud.certificatemanager.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\xfa\x06\n\x0b\x43\x65rtificate\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12K\n\x06labels\x18\x06 \x03(\x0b\x32;.yandex.cloud.certificatemanager.v1.Certificate.LabelsEntry\x12\x41\n\x04type\x18\x07 \x01(\x0e\x32\x33.yandex.cloud.certificatemanager.v1.CertificateType\x12\x0f\n\x07\x64omains\x18\x08 \x03(\t\x12\x46\n\x06status\x18\t \x01(\x0e\x32\x36.yandex.cloud.certificatemanager.v1.Certificate.Status\x12\x0e\n\x06issuer\x18\n \x01(\t\x12\x0f\n\x07subject\x18\x0b \x01(\t\x12\x0e\n\x06serial\x18\x0c \x01(\t\x12.\n\nupdated_at\x18\r \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\tissued_at\x18\x0e \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\tnot_after\x18\x0f \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nnot_before\x18\x10 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x41\n\nchallenges\x18\x11 \x03(\x0b\x32-.yandex.cloud.certificatemanager.v1.Challenge\x12\x1b\n\x13\x64\x65letion_protection\x18\x12 \x01(\x08\x12\x18\n\x10incomplete_chain\x18\x13 \x01(\x08\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"x\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0e\n\nVALIDATING\x10\x01\x12\x0b\n\x07INVALID\x10\x02\x12\n\n\x06ISSUED\x10\x03\x12\x0b\n\x07REVOKED\x10\x04\x12\x0c\n\x08RENEWING\x10\x05\x12\x12\n\x0eRENEWAL_FAILED\x10\x06\"\x8c\x05\n\tChallenge\x12\x0e\n\x06\x64omain\x18\x01 \x01(\t\x12?\n\x04type\x18\x02 \x01(\x0e\x32\x31.yandex.cloud.certificatemanager.v1.ChallengeType\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x44\n\x06status\x18\x05 \x01(\x0e\x32\x34.yandex.cloud.certificatemanager.v1.Challenge.Status\x12\x0f\n\x07message\x18\x06 \x01(\t\x12\r\n\x05\x65rror\x18\x07 \x01(\t\x12P\n\rdns_challenge\x18\x08 \x01(\x0b\x32\x37.yandex.cloud.certificatemanager.v1.Challenge.DnsRecordH\x00\x12P\n\x0ehttp_challenge\x18\t \x01(\x0b\x32\x36.yandex.cloud.certificatemanager.v1.Challenge.HttpFileH\x00\x1a\x36\n\tDnsRecord\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\x1a(\n\x08HttpFile\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\"U\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0e\n\nPROCESSING\x10\x02\x12\t\n\x05VALID\x10\x03\x12\x0b\n\x07INVALID\x10\x04\x42\x0b\n\tchallenge\"]\n\x07Version\x12\n\n\x02id\x18\x01 \x01(\t\x12\x16\n\x0e\x63\x65rtificate_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp*N\n\x0f\x43\x65rtificateType\x12 \n\x1c\x43\x45RTIFICATE_TYPE_UNSPECIFIED\x10\x00\x12\x0c\n\x08IMPORTED\x10\x01\x12\x0b\n\x07MANAGED\x10\x02*B\n\rChallengeType\x12\x1e\n\x1a\x43HALLENGE_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03\x44NS\x10\x01\x12\x08\n\x04HTTP\x10\x02\x42\x83\x01\n&yandex.cloud.api.certificatemanager.v1ZYgithub.com/yandex-cloud/go-genproto/yandex/cloud/certificatemanager/v1;certificatemanagerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.certificatemanager.v1.certificate_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n&yandex.cloud.api.certificatemanager.v1ZYgithub.com/yandex-cloud/go-genproto/yandex/cloud/certificatemanager/v1;certificatemanager'
  _globals['_CERTIFICATE_LABELSENTRY']._loaded_options = None
  _globals['_CERTIFICATE_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_CERTIFICATETYPE']._serialized_start=1768
  _globals['_CERTIFICATETYPE']._serialized_end=1846
  _globals['_CHALLENGETYPE']._serialized_start=1848
  _globals['_CHALLENGETYPE']._serialized_end=1914
  _globals['_CERTIFICATE']._serialized_start=126
  _globals['_CERTIFICATE']._serialized_end=1016
  _globals['_CERTIFICATE_LABELSENTRY']._serialized_start=849
  _globals['_CERTIFICATE_LABELSENTRY']._serialized_end=894
  _globals['_CERTIFICATE_STATUS']._serialized_start=896
  _globals['_CERTIFICATE_STATUS']._serialized_end=1016
  _globals['_CHALLENGE']._serialized_start=1019
  _globals['_CHALLENGE']._serialized_end=1671
  _globals['_CHALLENGE_DNSRECORD']._serialized_start=1475
  _globals['_CHALLENGE_DNSRECORD']._serialized_end=1529
  _globals['_CHALLENGE_HTTPFILE']._serialized_start=1531
  _globals['_CHALLENGE_HTTPFILE']._serialized_end=1571
  _globals['_CHALLENGE_STATUS']._serialized_start=1573
  _globals['_CHALLENGE_STATUS']._serialized_end=1658
  _globals['_VERSION']._serialized_start=1673
  _globals['_VERSION']._serialized_end=1766
# @@protoc_insertion_point(module_scope)
