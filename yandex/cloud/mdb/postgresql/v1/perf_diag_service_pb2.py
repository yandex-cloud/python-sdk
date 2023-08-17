# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/postgresql/v1/perf_diag_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.mdb.postgresql.v1 import perf_diag_pb2 as yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_perf__diag__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6yandex/cloud/mdb/postgresql/v1/perf_diag_service.proto\x12\x1eyandex.cloud.mdb.postgresql.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dyandex/cloud/validation.proto\x1a.yandex/cloud/mdb/postgresql/v1/perf_diag.proto\"\xd7\x01\n\x18ListRawStatementsRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12-\n\tfrom_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x07to_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1e\n\tpage_size\x18\x04 \x01(\x03\x42\x0b\xfa\xc7\x31\x07<=10000\x12\x1d\n\npage_token\x18\x05 \x01(\tB\t\x8a\xc8\x31\x05<=100\"\xda\x01\n\x1bListRawSessionStatesRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12-\n\tfrom_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x07to_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1e\n\tpage_size\x18\x04 \x01(\x03\x42\x0b\xfa\xc7\x31\x07<=10000\x12\x1d\n\npage_token\x18\x05 \x01(\tB\t\x8a\xc8\x31\x05<=100\"}\n\x1cListRawSessionStatesResponse\x12\x44\n\x0esession_states\x18\x01 \x03(\x0b\x32,.yandex.cloud.mdb.postgresql.v1.SessionState\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"x\n\x19ListRawStatementsResponse\x12\x42\n\nstatements\x18\x01 \x03(\x0b\x32..yandex.cloud.mdb.postgresql.v1.QueryStatement\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xbe\x02\n\x1dPerformanceDiagnosticsService\x12\x91\x01\n\x14ListRawSessionStates\x12;.yandex.cloud.mdb.postgresql.v1.ListRawSessionStatesRequest\x1a<.yandex.cloud.mdb.postgresql.v1.ListRawSessionStatesResponse\x12\x88\x01\n\x11ListRawStatements\x12\x38.yandex.cloud.mdb.postgresql.v1.ListRawStatementsRequest\x1a\x39.yandex.cloud.mdb.postgresql.v1.ListRawStatementsResponseBs\n\"yandex.cloud.api.mdb.postgresql.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/postgresql/v1;postgresqlb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.postgresql.v1.perf_diag_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"yandex.cloud.api.mdb.postgresql.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/postgresql/v1;postgresql'
  _LISTRAWSTATEMENTSREQUEST.fields_by_name['cluster_id']._options = None
  _LISTRAWSTATEMENTSREQUEST.fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTRAWSTATEMENTSREQUEST.fields_by_name['page_size']._options = None
  _LISTRAWSTATEMENTSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\007<=10000'
  _LISTRAWSTATEMENTSREQUEST.fields_by_name['page_token']._options = None
  _LISTRAWSTATEMENTSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _LISTRAWSESSIONSTATESREQUEST.fields_by_name['cluster_id']._options = None
  _LISTRAWSESSIONSTATESREQUEST.fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTRAWSESSIONSTATESREQUEST.fields_by_name['page_size']._options = None
  _LISTRAWSESSIONSTATESREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\007<=10000'
  _LISTRAWSESSIONSTATESREQUEST.fields_by_name['page_token']._options = None
  _LISTRAWSESSIONSTATESREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTRAWSTATEMENTSREQUEST']._serialized_start=203
  _globals['_LISTRAWSTATEMENTSREQUEST']._serialized_end=418
  _globals['_LISTRAWSESSIONSTATESREQUEST']._serialized_start=421
  _globals['_LISTRAWSESSIONSTATESREQUEST']._serialized_end=639
  _globals['_LISTRAWSESSIONSTATESRESPONSE']._serialized_start=641
  _globals['_LISTRAWSESSIONSTATESRESPONSE']._serialized_end=766
  _globals['_LISTRAWSTATEMENTSRESPONSE']._serialized_start=768
  _globals['_LISTRAWSTATEMENTSRESPONSE']._serialized_end=888
  _globals['_PERFORMANCEDIAGNOSTICSSERVICE']._serialized_start=891
  _globals['_PERFORMANCEDIAGNOSTICSSERVICE']._serialized_end=1209
# @@protoc_insertion_point(module_scope)
