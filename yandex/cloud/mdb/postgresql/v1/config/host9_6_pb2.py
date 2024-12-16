# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/mdb/postgresql/v1/config/host9_6.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'yandex/cloud/mdb/postgresql/v1/config/host9_6.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3yandex/cloud/mdb/postgresql/v1/config/host9_6.proto\x12%yandex.cloud.mdb.postgresql.v1.config\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dyandex/cloud/validation.proto\"\xf6)\n\x17PostgresqlHostConfig9_6\x12=\n\x18recovery_min_apply_delay\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x33\n\x0eshared_buffers\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x31\n\x0ctemp_buffers\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12-\n\x08work_mem\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12<\n\x17replacement_sort_tuples\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x34\n\x0ftemp_file_limit\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x44\n\x13\x62\x61\x63kend_flush_after\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\n\xfa\xc7\x31\x06\x30-2048\x12I\n\x16old_snapshot_threshold\x18\x08 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0c\xfa\xc7\x31\x08-1-86400\x12@\n\x1bmax_standby_streaming_delay\x18\t \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12p\n\x14\x63onstraint_exclusion\x18\n \x01(\x0e\x32R.yandex.cloud.mdb.postgresql.v1.config.PostgresqlHostConfig9_6.ConstraintExclusion\x12;\n\x15\x63ursor_tuple_fraction\x18\x0b \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12J\n\x13\x66rom_collapse_limit\x18\x0c \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x10\xfa\xc7\x31\x0c\x31-2147483647\x12J\n\x13join_collapse_limit\x18\r \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x10\xfa\xc7\x31\x0c\x31-2147483647\x12m\n\x13\x66orce_parallel_mode\x18\x0e \x01(\x0e\x32P.yandex.cloud.mdb.postgresql.v1.config.PostgresqlHostConfig9_6.ForceParallelMode\x12\x64\n\x13\x63lient_min_messages\x18\x0f \x01(\x0e\x32G.yandex.cloud.mdb.postgresql.v1.config.PostgresqlHostConfig9_6.LogLevel\x12\x61\n\x10log_min_messages\x18\x10 \x01(\x0e\x32G.yandex.cloud.mdb.postgresql.v1.config.PostgresqlHostConfig9_6.LogLevel\x12h\n\x17log_min_error_statement\x18\x11 \x01(\x0e\x32G.yandex.cloud.mdb.postgresql.v1.config.PostgresqlHostConfig9_6.LogLevel\x12?\n\x1alog_min_duration_statement\x18\x12 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x33\n\x0flog_checkpoints\x18\x13 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x33\n\x0flog_connections\x18\x14 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x36\n\x12log_disconnections\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x30\n\x0clog_duration\x18\x16 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12m\n\x13log_error_verbosity\x18\x17 \x01(\x0e\x32P.yandex.cloud.mdb.postgresql.v1.config.PostgresqlHostConfig9_6.LogErrorVerbosity\x12\x32\n\x0elog_lock_waits\x18\x18 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x62\n\rlog_statement\x18\x19 \x01(\x0e\x32K.yandex.cloud.mdb.postgresql.v1.config.PostgresqlHostConfig9_6.LogStatement\x12\x33\n\x0elog_temp_files\x18\x1a \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x13\n\x0bsearch_path\x18\x1b \x01(\t\x12\x30\n\x0crow_security\x18\x1c \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12z\n\x1d\x64\x65\x66\x61ult_transaction_isolation\x18\x1d \x01(\x0e\x32S.yandex.cloud.mdb.postgresql.v1.config.PostgresqlHostConfig9_6.TransactionIsolation\x12\x36\n\x11statement_timeout\x18\x1e \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x31\n\x0clock_timeout\x18\x1f \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12Z\n#idle_in_transaction_session_timeout\x18  \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x10\xfa\xc7\x31\x0c\x30-2147483647\x12`\n\x0c\x62ytea_output\x18! \x01(\x0e\x32J.yandex.cloud.mdb.postgresql.v1.config.PostgresqlHostConfig9_6.ByteaOutput\x12[\n\txmlbinary\x18\" \x01(\x0e\x32H.yandex.cloud.mdb.postgresql.v1.config.PostgresqlHostConfig9_6.XmlBinary\x12[\n\txmloption\x18# \x01(\x0e\x32H.yandex.cloud.mdb.postgresql.v1.config.PostgresqlHostConfig9_6.XmlOption\x12;\n\x16gin_pending_list_limit\x18$ \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x35\n\x10\x64\x65\x61\x64lock_timeout\x18% \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12>\n\x19max_locks_per_transaction\x18& \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x43\n\x1emax_pred_locks_per_transaction\x18\' \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12/\n\x0b\x61rray_nulls\x18( \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x66\n\x0f\x62\x61\x63kslash_quote\x18) \x01(\x0e\x32M.yandex.cloud.mdb.postgresql.v1.config.PostgresqlHostConfig9_6.BackslashQuote\x12\x35\n\x11\x64\x65\x66\x61ult_with_oids\x18* \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x39\n\x15\x65scape_string_warning\x18+ \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x38\n\x14lo_compat_privileges\x18, \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12?\n\x1boperator_precedence_warning\x18- \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x39\n\x15quote_all_identifiers\x18. \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12?\n\x1bstandard_conforming_strings\x18/ \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x38\n\x14synchronize_seqscans\x18\x30 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x39\n\x15transform_null_equals\x18\x31 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x31\n\rexit_on_error\x18\x32 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x33\n\rseq_page_cost\x18\x33 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x36\n\x10random_page_cost\x18\x34 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x33\n\x0fsql_inheritance\x18\x35 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12I\n\x18\x65\x66\x66\x65\x63tive_io_concurrency\x18\x36 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\n\xfa\xc7\x31\x06\x30-1000\x12M\n\x14\x65\x66\x66\x65\x63tive_cache_size\x18\x37 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x12\xfa\xc7\x31\x0e\x30-549755813888\"\x9a\x01\n\x13\x43onstraintExclusion\x12$\n CONSTRAINT_EXCLUSION_UNSPECIFIED\x10\x00\x12\x1b\n\x17\x43ONSTRAINT_EXCLUSION_ON\x10\x01\x12\x1c\n\x18\x43ONSTRAINT_EXCLUSION_OFF\x10\x02\x12\"\n\x1e\x43ONSTRAINT_EXCLUSION_PARTITION\x10\x03\"\x92\x01\n\x11\x46orceParallelMode\x12#\n\x1f\x46ORCE_PARALLEL_MODE_UNSPECIFIED\x10\x00\x12\x1a\n\x16\x46ORCE_PARALLEL_MODE_ON\x10\x01\x12\x1b\n\x17\x46ORCE_PARALLEL_MODE_OFF\x10\x02\x12\x1f\n\x1b\x46ORCE_PARALLEL_MODE_REGRESS\x10\x03\"\x92\x02\n\x08LogLevel\x12\x19\n\x15LOG_LEVEL_UNSPECIFIED\x10\x00\x12\x14\n\x10LOG_LEVEL_DEBUG5\x10\x01\x12\x14\n\x10LOG_LEVEL_DEBUG4\x10\x02\x12\x14\n\x10LOG_LEVEL_DEBUG3\x10\x03\x12\x14\n\x10LOG_LEVEL_DEBUG2\x10\x04\x12\x14\n\x10LOG_LEVEL_DEBUG1\x10\x05\x12\x11\n\rLOG_LEVEL_LOG\x10\x06\x12\x14\n\x10LOG_LEVEL_NOTICE\x10\x07\x12\x15\n\x11LOG_LEVEL_WARNING\x10\x08\x12\x13\n\x0fLOG_LEVEL_ERROR\x10\t\x12\x13\n\x0fLOG_LEVEL_FATAL\x10\n\x12\x13\n\x0fLOG_LEVEL_PANIC\x10\x0b\"\x99\x01\n\x11LogErrorVerbosity\x12#\n\x1fLOG_ERROR_VERBOSITY_UNSPECIFIED\x10\x00\x12\x1d\n\x19LOG_ERROR_VERBOSITY_TERSE\x10\x01\x12\x1f\n\x1bLOG_ERROR_VERBOSITY_DEFAULT\x10\x02\x12\x1f\n\x1bLOG_ERROR_VERBOSITY_VERBOSE\x10\x03\"\x8a\x01\n\x0cLogStatement\x12\x1d\n\x19LOG_STATEMENT_UNSPECIFIED\x10\x00\x12\x16\n\x12LOG_STATEMENT_NONE\x10\x01\x12\x15\n\x11LOG_STATEMENT_DDL\x10\x02\x12\x15\n\x11LOG_STATEMENT_MOD\x10\x03\x12\x15\n\x11LOG_STATEMENT_ALL\x10\x04\"\xe6\x01\n\x14TransactionIsolation\x12%\n!TRANSACTION_ISOLATION_UNSPECIFIED\x10\x00\x12*\n&TRANSACTION_ISOLATION_READ_UNCOMMITTED\x10\x01\x12(\n$TRANSACTION_ISOLATION_READ_COMMITTED\x10\x02\x12)\n%TRANSACTION_ISOLATION_REPEATABLE_READ\x10\x03\x12&\n\"TRANSACTION_ISOLATION_SERIALIZABLE\x10\x04\"[\n\x0b\x42yteaOutput\x12\x1c\n\x18\x42YTEA_OUTPUT_UNSPECIFIED\x10\x00\x12\x14\n\x10\x42YTEA_OUTPUT_HEX\x10\x01\x12\x18\n\x14\x42YTEA_OUTPUT_ESCAPED\x10\x02\"R\n\tXmlBinary\x12\x1a\n\x16XML_BINARY_UNSPECIFIED\x10\x00\x12\x15\n\x11XML_BINARY_BASE64\x10\x01\x12\x12\n\x0eXML_BINARY_HEX\x10\x02\"X\n\tXmlOption\x12\x1a\n\x16XML_OPTION_UNSPECIFIED\x10\x00\x12\x17\n\x13XML_OPTION_DOCUMENT\x10\x01\x12\x16\n\x12XML_OPTION_CONTENT\x10\x02\"\x9a\x01\n\x0e\x42\x61\x63kslashQuote\x12\x1f\n\x1b\x42\x41\x43KSLASH_QUOTE_UNSPECIFIED\x10\x00\x12\x13\n\x0f\x42\x41\x43KSLASH_QUOTE\x10\x01\x12\x16\n\x12\x42\x41\x43KSLASH_QUOTE_ON\x10\x02\x12\x17\n\x13\x42\x41\x43KSLASH_QUOTE_OFF\x10\x03\x12!\n\x1d\x42\x41\x43KSLASH_QUOTE_SAFE_ENCODING\x10\x04\x42\x81\x01\n)yandex.cloud.api.mdb.postgresql.v1.configZTgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/postgresql/v1/config;postgresqlb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.postgresql.v1.config.host9_6_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n)yandex.cloud.api.mdb.postgresql.v1.configZTgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/postgresql/v1/config;postgresql'
  _globals['_POSTGRESQLHOSTCONFIG9_6'].fields_by_name['backend_flush_after']._loaded_options = None
  _globals['_POSTGRESQLHOSTCONFIG9_6'].fields_by_name['backend_flush_after']._serialized_options = b'\372\3071\0060-2048'
  _globals['_POSTGRESQLHOSTCONFIG9_6'].fields_by_name['old_snapshot_threshold']._loaded_options = None
  _globals['_POSTGRESQLHOSTCONFIG9_6'].fields_by_name['old_snapshot_threshold']._serialized_options = b'\372\3071\010-1-86400'
  _globals['_POSTGRESQLHOSTCONFIG9_6'].fields_by_name['from_collapse_limit']._loaded_options = None
  _globals['_POSTGRESQLHOSTCONFIG9_6'].fields_by_name['from_collapse_limit']._serialized_options = b'\372\3071\0141-2147483647'
  _globals['_POSTGRESQLHOSTCONFIG9_6'].fields_by_name['join_collapse_limit']._loaded_options = None
  _globals['_POSTGRESQLHOSTCONFIG9_6'].fields_by_name['join_collapse_limit']._serialized_options = b'\372\3071\0141-2147483647'
  _globals['_POSTGRESQLHOSTCONFIG9_6'].fields_by_name['idle_in_transaction_session_timeout']._loaded_options = None
  _globals['_POSTGRESQLHOSTCONFIG9_6'].fields_by_name['idle_in_transaction_session_timeout']._serialized_options = b'\372\3071\0140-2147483647'
  _globals['_POSTGRESQLHOSTCONFIG9_6'].fields_by_name['effective_io_concurrency']._loaded_options = None
  _globals['_POSTGRESQLHOSTCONFIG9_6'].fields_by_name['effective_io_concurrency']._serialized_options = b'\372\3071\0060-1000'
  _globals['_POSTGRESQLHOSTCONFIG9_6'].fields_by_name['effective_cache_size']._loaded_options = None
  _globals['_POSTGRESQLHOSTCONFIG9_6'].fields_by_name['effective_cache_size']._serialized_options = b'\372\3071\0160-549755813888'
  _globals['_POSTGRESQLHOSTCONFIG9_6']._serialized_start=158
  _globals['_POSTGRESQLHOSTCONFIG9_6']._serialized_end=5524
  _globals['_POSTGRESQLHOSTCONFIG9_6_CONSTRAINTEXCLUSION']._serialized_start=3990
  _globals['_POSTGRESQLHOSTCONFIG9_6_CONSTRAINTEXCLUSION']._serialized_end=4144
  _globals['_POSTGRESQLHOSTCONFIG9_6_FORCEPARALLELMODE']._serialized_start=4147
  _globals['_POSTGRESQLHOSTCONFIG9_6_FORCEPARALLELMODE']._serialized_end=4293
  _globals['_POSTGRESQLHOSTCONFIG9_6_LOGLEVEL']._serialized_start=4296
  _globals['_POSTGRESQLHOSTCONFIG9_6_LOGLEVEL']._serialized_end=4570
  _globals['_POSTGRESQLHOSTCONFIG9_6_LOGERRORVERBOSITY']._serialized_start=4573
  _globals['_POSTGRESQLHOSTCONFIG9_6_LOGERRORVERBOSITY']._serialized_end=4726
  _globals['_POSTGRESQLHOSTCONFIG9_6_LOGSTATEMENT']._serialized_start=4729
  _globals['_POSTGRESQLHOSTCONFIG9_6_LOGSTATEMENT']._serialized_end=4867
  _globals['_POSTGRESQLHOSTCONFIG9_6_TRANSACTIONISOLATION']._serialized_start=4870
  _globals['_POSTGRESQLHOSTCONFIG9_6_TRANSACTIONISOLATION']._serialized_end=5100
  _globals['_POSTGRESQLHOSTCONFIG9_6_BYTEAOUTPUT']._serialized_start=5102
  _globals['_POSTGRESQLHOSTCONFIG9_6_BYTEAOUTPUT']._serialized_end=5193
  _globals['_POSTGRESQLHOSTCONFIG9_6_XMLBINARY']._serialized_start=5195
  _globals['_POSTGRESQLHOSTCONFIG9_6_XMLBINARY']._serialized_end=5277
  _globals['_POSTGRESQLHOSTCONFIG9_6_XMLOPTION']._serialized_start=5279
  _globals['_POSTGRESQLHOSTCONFIG9_6_XMLOPTION']._serialized_end=5367
  _globals['_POSTGRESQLHOSTCONFIG9_6_BACKSLASHQUOTE']._serialized_start=5370
  _globals['_POSTGRESQLHOSTCONFIG9_6_BACKSLASHQUOTE']._serialized_end=5524
# @@protoc_insertion_point(module_scope)
