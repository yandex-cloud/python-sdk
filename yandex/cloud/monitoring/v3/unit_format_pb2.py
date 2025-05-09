# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/monitoring/v3/unit_format.proto
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
    'yandex/cloud/monitoring/v3/unit_format.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,yandex/cloud/monitoring/v3/unit_format.proto\x12\x1ayandex.cloud.monitoring.v3*\xfa\x11\n\nUnitFormat\x12\x1b\n\x17UNIT_FORMAT_UNSPECIFIED\x10\x00\x12\r\n\tUNIT_NONE\x10\x01\x12\x0e\n\nUNIT_COUNT\x10\x02\x12\x10\n\x0cUNIT_PERCENT\x10\x03\x12\x15\n\x11UNIT_PERCENT_UNIT\x10\x04\x12\x14\n\x10UNIT_NANOSECONDS\x10\x05\x12\x15\n\x11UNIT_MICROSECONDS\x10\x06\x12\x15\n\x11UNIT_MILLISECONDS\x10\x07\x12\x10\n\x0cUNIT_SECONDS\x10\x08\x12\x10\n\x0cUNIT_MINUTES\x10\t\x12\x0e\n\nUNIT_HOURS\x10\n\x12\r\n\tUNIT_DAYS\x10\x0b\x12\x10\n\x0cUNIT_BITS_SI\x10\x0c\x12\x11\n\rUNIT_BYTES_SI\x10\r\x12\x12\n\x0eUNIT_KILOBYTES\x10\x0e\x12\x12\n\x0eUNIT_MEGABYTES\x10\x0f\x12\x12\n\x0eUNIT_GIGABYTES\x10\x10\x12\x12\n\x0eUNIT_TERABYTES\x10\x11\x12\x12\n\x0eUNIT_PETABYTES\x10\x12\x12\x11\n\rUNIT_EXABYTES\x10\x13\x12\x11\n\rUNIT_BITS_IEC\x10\x14\x12\x12\n\x0eUNIT_BYTES_IEC\x10\x15\x12\x12\n\x0eUNIT_KIBIBYTES\x10\x16\x12\x12\n\x0eUNIT_MEBIBYTES\x10\x17\x12\x12\n\x0eUNIT_GIBIBYTES\x10\x18\x12\x12\n\x0eUNIT_TEBIBYTES\x10\x19\x12\x12\n\x0eUNIT_PEBIBYTES\x10\x1a\x12\x12\n\x0eUNIT_EXBIBYTES\x10\x1b\x12\x1c\n\x18UNIT_REQUESTS_PER_SECOND\x10\x1c\x12\x1e\n\x1aUNIT_OPERATIONS_PER_SECOND\x10\x1d\x12\x1a\n\x16UNIT_WRITES_PER_SECOND\x10\x1e\x12\x19\n\x15UNIT_READS_PER_SECOND\x10\x1f\x12\x1b\n\x17UNIT_PACKETS_PER_SECOND\x10 \x12!\n\x1dUNIT_IO_OPERATIONS_PER_SECOND\x10!\x12\x1a\n\x16UNIT_COUNTS_PER_SECOND\x10\"\x12\x1b\n\x17UNIT_BITS_SI_PER_SECOND\x10#\x12\x1c\n\x18UNIT_BYTES_SI_PER_SECOND\x10$\x12\x1c\n\x18UNIT_KILOBITS_PER_SECOND\x10%\x12\x1d\n\x19UNIT_KILOBYTES_PER_SECOND\x10&\x12\x1c\n\x18UNIT_MEGABITS_PER_SECOND\x10\'\x12\x1d\n\x19UNIT_MEGABYTES_PER_SECOND\x10(\x12\x1c\n\x18UNIT_GIGABITS_PER_SECOND\x10)\x12\x1d\n\x19UNIT_GIGABYTES_PER_SECOND\x10*\x12\x1c\n\x18UNIT_TERABITS_PER_SECOND\x10+\x12\x1d\n\x19UNIT_TERABYTES_PER_SECOND\x10,\x12\x1c\n\x18UNIT_PETABITS_PER_SECOND\x10-\x12\x1d\n\x19UNIT_PETABYTES_PER_SECOND\x10.\x12\x1c\n\x18UNIT_BITS_IEC_PER_SECOND\x10/\x12\x1d\n\x19UNIT_BYTES_IEC_PER_SECOND\x10\x30\x12\x1c\n\x18UNIT_KIBIBITS_PER_SECOND\x10\x31\x12\x1d\n\x19UNIT_KIBIBYTES_PER_SECOND\x10\x32\x12\x1c\n\x18UNIT_MEBIBITS_PER_SECOND\x10\x33\x12\x1d\n\x19UNIT_MEBIBYTES_PER_SECOND\x10\x34\x12\x1c\n\x18UNIT_GIBIBITS_PER_SECOND\x10\x35\x12\x1d\n\x19UNIT_GIBIBYTES_PER_SECOND\x10\x36\x12\x1c\n\x18UNIT_TEBIBITS_PER_SECOND\x10\x37\x12\x1d\n\x19UNIT_TEBIBYTES_PER_SECOND\x10\x38\x12\x1c\n\x18UNIT_PEBIBITS_PER_SECOND\x10\x39\x12\x1d\n\x19UNIT_PEBIBYTES_PER_SECOND\x10:\x12\x15\n\x11UNIT_DATETIME_UTC\x10;\x12\x17\n\x13UNIT_DATETIME_LOCAL\x10<\x12\x0e\n\nUNIT_HERTZ\x10=\x12\x12\n\x0eUNIT_KILOHERTZ\x10>\x12\x12\n\x0eUNIT_MEGAHERTZ\x10?\x12\x12\n\x0eUNIT_GIGAHERTZ\x10@\x12\x0f\n\x0bUNIT_DOLLAR\x10\x41\x12\r\n\tUNIT_EURO\x10\x42\x12\x0f\n\x0bUNIT_ROUBLE\x10\x43\x12\x10\n\x0cUNIT_CELSIUS\x10\x44\x12\x13\n\x0fUNIT_FAHRENHEIT\x10\x45\x12\x0f\n\x0bUNIT_KELVIN\x10\x46\x12\x18\n\x14UNIT_FLOP_PER_SECOND\x10G\x12\x1c\n\x18UNIT_KILOFLOP_PER_SECOND\x10H\x12\x1c\n\x18UNIT_MEGAFLOP_PER_SECOND\x10I\x12\x1c\n\x18UNIT_GIGAFLOP_PER_SECOND\x10J\x12\x1c\n\x18UNIT_PETAFLOP_PER_SECOND\x10K\x12\x1b\n\x17UNIT_EXAFLOP_PER_SECOND\x10L\x12\x1a\n\x16UNIT_METERS_PER_SECOND\x10M\x12\x1c\n\x18UNIT_KILOMETERS_PER_HOUR\x10N\x12\x17\n\x13UNIT_MILES_PER_HOUR\x10O\x12\x13\n\x0fUNIT_MILLIMETER\x10P\x12\x13\n\x0fUNIT_CENTIMETER\x10Q\x12\x0e\n\nUNIT_METER\x10R\x12\x12\n\x0eUNIT_KILOMETER\x10S\x12\r\n\tUNIT_MILE\x10T\x12\x0c\n\x08UNIT_PPM\x10U\x12\x1a\n\x16UNIT_EVENTS_PER_SECOND\x10V\x12\x10\n\x0cUNIT_PACKETS\x10W\x12\x0c\n\x08UNIT_DBM\x10X\x12\x14\n\x10UNIT_VIRTUAL_CPU\x10Y\x12\x1c\n\x18UNIT_MESSAGES_PER_SECOND\x10Z\x12\x15\n\x11UNIT_NANOCORE_CPU\x10[\x12\x16\n\x12UNIT_MICROCORE_CPU\x10\\\x12\x16\n\x12UNIT_MILLICORE_CPU\x10]\x12\x11\n\rUNIT_CORE_CPU\x10^Bk\n\x1eyandex.cloud.api.monitoring.v3ZIgithub.com/yandex-cloud/go-genproto/yandex/cloud/monitoring/v3;monitoringb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.monitoring.v3.unit_format_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036yandex.cloud.api.monitoring.v3ZIgithub.com/yandex-cloud/go-genproto/yandex/cloud/monitoring/v3;monitoring'
  _globals['_UNITFORMAT']._serialized_start=77
  _globals['_UNITFORMAT']._serialized_end=2375
# @@protoc_insertion_point(module_scope)
