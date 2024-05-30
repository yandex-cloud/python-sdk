"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import yandex.cloud.datatransfer.v1.endpoint.common_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Parser(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JSON_PARSER_FIELD_NUMBER: builtins.int
    AUDIT_TRAILS_V1_PARSER_FIELD_NUMBER: builtins.int
    CLOUD_LOGGING_PARSER_FIELD_NUMBER: builtins.int
    TSKV_PARSER_FIELD_NUMBER: builtins.int
    @property
    def json_parser(self) -> global___GenericParserCommon: ...
    @property
    def audit_trails_v1_parser(self) -> global___AuditTrailsV1Parser: ...
    @property
    def cloud_logging_parser(self) -> global___CloudLoggingParser: ...
    @property
    def tskv_parser(self) -> global___GenericParserCommon: ...
    def __init__(
        self,
        *,
        json_parser: global___GenericParserCommon | None = ...,
        audit_trails_v1_parser: global___AuditTrailsV1Parser | None = ...,
        cloud_logging_parser: global___CloudLoggingParser | None = ...,
        tskv_parser: global___GenericParserCommon | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["audit_trails_v1_parser", b"audit_trails_v1_parser", "cloud_logging_parser", b"cloud_logging_parser", "json_parser", b"json_parser", "parser", b"parser", "tskv_parser", b"tskv_parser"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["audit_trails_v1_parser", b"audit_trails_v1_parser", "cloud_logging_parser", b"cloud_logging_parser", "json_parser", b"json_parser", "parser", b"parser", "tskv_parser", b"tskv_parser"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["parser", b"parser"]) -> typing.Literal["json_parser", "audit_trails_v1_parser", "cloud_logging_parser", "tskv_parser"] | None: ...

global___Parser = Parser

@typing.final
class GenericParserCommon(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_SCHEMA_FIELD_NUMBER: builtins.int
    NULL_KEYS_ALLOWED_FIELD_NUMBER: builtins.int
    ADD_REST_COLUMN_FIELD_NUMBER: builtins.int
    UNESCAPE_STRING_VALUES_FIELD_NUMBER: builtins.int
    null_keys_allowed: builtins.bool
    """Allow null keys, if no - null keys will be putted to unparsed data"""
    add_rest_column: builtins.bool
    """Will add _rest column for all unknown fields"""
    unescape_string_values: builtins.bool
    """Unescape string values"""
    @property
    def data_schema(self) -> yandex.cloud.datatransfer.v1.endpoint.common_pb2.DataSchema: ...
    def __init__(
        self,
        *,
        data_schema: yandex.cloud.datatransfer.v1.endpoint.common_pb2.DataSchema | None = ...,
        null_keys_allowed: builtins.bool = ...,
        add_rest_column: builtins.bool = ...,
        unescape_string_values: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["data_schema", b"data_schema"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["add_rest_column", b"add_rest_column", "data_schema", b"data_schema", "null_keys_allowed", b"null_keys_allowed", "unescape_string_values", b"unescape_string_values"]) -> None: ...

global___GenericParserCommon = GenericParserCommon

@typing.final
class AuditTrailsV1Parser(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___AuditTrailsV1Parser = AuditTrailsV1Parser

@typing.final
class CloudLoggingParser(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___CloudLoggingParser = CloudLoggingParser
