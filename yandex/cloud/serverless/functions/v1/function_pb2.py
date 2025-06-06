# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/serverless/functions/v1/function.proto
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
    'yandex/cloud/serverless/functions/v1/function.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud.logging.v1 import log_entry_pb2 as yandex_dot_cloud_dot_logging_dot_v1_dot_log__entry__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3yandex/cloud/serverless/functions/v1/function.proto\x12$yandex.cloud.serverless.functions.v1\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\'yandex/cloud/logging/v1/log_entry.proto\x1a\x1dyandex/cloud/validation.proto\"\xd1\x03\n\x08\x46unction\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x16\n\x04name\x18\x04 \x01(\tB\x08\x8a\xc8\x31\x04\x33-63\x12\x1e\n\x0b\x64\x65scription\x18\x05 \x01(\tB\t\x8a\xc8\x31\x05\x30-256\x12T\n\x06labels\x18\x06 \x03(\x0b\x32:.yandex.cloud.serverless.functions.v1.Function.LabelsEntryB\x08\x82\xc8\x31\x04<=64\x12\x17\n\x0fhttp_invoke_url\x18\x08 \x01(\t\x12\x45\n\x06status\x18\t \x01(\x0e\x32\x35.yandex.cloud.serverless.functions.v1.Function.Status\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"S\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12\x0c\n\x08\x44\x45LETING\x10\x03\x12\t\n\x05\x45RROR\x10\x04J\x04\x08\x07\x10\x08\"\xf1\n\n\x07Version\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x66unction_id\x18\x02 \x01(\t\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05\x30-256\x12.\n\ncreated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07runtime\x18\x06 \x01(\t\x12\x12\n\nentrypoint\x18\x07 \x01(\t\x12\x42\n\tresources\x18\x08 \x01(\x0b\x32/.yandex.cloud.serverless.functions.v1.Resources\x12\x34\n\x11\x65xecution_timeout\x18\t \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x1a\n\x12service_account_id\x18\n \x01(\t\x12\x12\n\nimage_size\x18\x0c \x01(\x03\x12\x44\n\x06status\x18\r \x01(\x0e\x32\x34.yandex.cloud.serverless.functions.v1.Version.Status\x12\x0c\n\x04tags\x18\x0e \x03(\t\x12S\n\x0b\x65nvironment\x18\x10 \x03(\x0b\x32>.yandex.cloud.serverless.functions.v1.Version.EnvironmentEntry\x12H\n\x0c\x63onnectivity\x18\x11 \x01(\x0b\x32\x32.yandex.cloud.serverless.functions.v1.Connectivity\x12g\n\x16named_service_accounts\x18\x12 \x03(\x0b\x32G.yandex.cloud.serverless.functions.v1.Version.NamedServiceAccountsEntry\x12=\n\x07secrets\x18\x13 \x03(\x0b\x32,.yandex.cloud.serverless.functions.v1.Secret\x12\x45\n\x0blog_options\x18\x14 \x01(\x0b\x32\x30.yandex.cloud.serverless.functions.v1.LogOptions\x12J\n\x0estorage_mounts\x18\x15 \x03(\x0b\x32\x32.yandex.cloud.serverless.functions.v1.StorageMount\x12\\\n\x17\x61sync_invocation_config\x18\x16 \x01(\x0b\x32;.yandex.cloud.serverless.functions.v1.AsyncInvocationConfig\x12\x12\n\ntmpfs_size\x18\x17 \x01(\x03\x12\x1d\n\x0b\x63oncurrency\x18\x18 \x01(\x03\x42\x08\xfa\xc7\x31\x04\x30-16\x12;\n\x06mounts\x18\x19 \x03(\x0b\x32+.yandex.cloud.serverless.functions.v1.Mount\x12O\n\x10metadata_options\x18\x1a \x01(\x0b\x32\x35.yandex.cloud.serverless.functions.v1.MetadataOptions\x1a\x32\n\x10\x45nvironmentEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a;\n\x19NamedServiceAccountsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"V\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12\x0c\n\x08OBSOLETE\x10\x03\x12\x0c\n\x08\x44\x45LETING\x10\x04J\x04\x08\x04\x10\x05J\x04\x08\x0b\x10\x0cJ\x04\x08\x0f\x10\x10\"5\n\tResources\x12(\n\x06memory\x18\x01 \x01(\x03\x42\x18\xfa\xc7\x31\x14\x31\x33\x34\x32\x31\x37\x37\x32\x38-8589934592\"O\n\x07Package\x12\x19\n\x0b\x62ucket_name\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x19\n\x0bobject_name\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x0e\n\x06sha256\x18\x03 \x01(\t\"A\n\x0c\x43onnectivity\x12\x12\n\nnetwork_id\x18\x01 \x01(\t\x12\x1d\n\tsubnet_id\x18\x02 \x03(\tB\n\x8a\xc8\x31\x02>0\x90\xc8\x31\x01\"\xf8\x01\n\rScalingPolicy\x12\x13\n\x0b\x66unction_id\x18\x01 \x01(\t\x12\x0b\n\x03tag\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bmodified_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12#\n\x1bprovisioned_instances_count\x18\x06 \x01(\x03\x12\x1c\n\x14zone_instances_limit\x18\x07 \x01(\x03\x12\x1b\n\x13zone_requests_limit\x18\x08 \x01(\x03J\x04\x08\x05\x10\x06\"b\n\x06Secret\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nversion_id\x18\x02 \x01(\t\x12\x0b\n\x03key\x18\x03 \x01(\t\x12\x1e\n\x14\x65nvironment_variable\x18\x04 \x01(\tH\x00\x42\x0b\n\treference\"\xe0\x01\n\nLogOptions\x12\x10\n\x08\x64isabled\x18\x01 \x01(\x08\x12;\n\x0clog_group_id\x18\x02 \x01(\tB#\xf2\xc7\x31\x1f([a-zA-Z][-a-zA-Z0-9_.]{0,63})?H\x00\x12\x38\n\tfolder_id\x18\x03 \x01(\tB#\xf2\xc7\x31\x1f([a-zA-Z][-a-zA-Z0-9_.]{0,63})?H\x00\x12:\n\tmin_level\x18\x04 \x01(\x0e\x32\'.yandex.cloud.logging.v1.LogLevel.LevelB\r\n\x0b\x64\x65stination\"\xa3\x01\n\x0cStorageMount\x12\x31\n\tbucket_id\x18\x01 \x01(\tB\x1e\xe8\xc7\x31\x01\xf2\xc7\x31\x0e[-.0-9a-zA-Z]*\x8a\xc8\x31\x04\x33-63\x12\x0e\n\x06prefix\x18\x02 \x01(\t\x12\x39\n\x10mount_point_name\x18\x03 \x01(\tB\x1f\xe8\xc7\x31\x01\xf2\xc7\x31\x0e[-_0-9a-zA-Z]*\x8a\xc8\x31\x05\x31-100\x12\x11\n\tread_only\x18\x04 \x01(\x08:\x02\x18\x01\"\x83\x04\n\x05Mount\x12-\n\x04name\x18\x01 \x01(\tB\x1f\xe8\xc7\x31\x01\xf2\xc7\x31\x0e[-_0-9a-zA-Z]*\x8a\xc8\x31\x05\x31-100\x12>\n\x04mode\x18\x03 \x01(\x0e\x32\x30.yandex.cloud.serverless.functions.v1.Mount.Mode\x12S\n\x0eobject_storage\x18\n \x01(\x0b\x32\x39.yandex.cloud.serverless.functions.v1.Mount.ObjectStorageH\x00\x12S\n\x13\x65phemeral_disk_spec\x18\x0b \x01(\x0b\x32\x34.yandex.cloud.serverless.functions.v1.Mount.DiskSpecH\x00\x1aR\n\rObjectStorage\x12\x31\n\tbucket_id\x18\x01 \x01(\tB\x1e\xe8\xc7\x31\x01\xf2\xc7\x31\x0e[-.0-9a-zA-Z]*\x8a\xc8\x31\x04\x33-63\x12\x0e\n\x06prefix\x18\x02 \x01(\t\x1a\x34\n\x08\x44iskSpec\x12\x14\n\x04size\x18\x01 \x01(\x03\x42\x06\xfa\xc7\x31\x02>0\x12\x12\n\nblock_size\x18\x02 \x01(\x03\";\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\r\n\tREAD_ONLY\x10\x01\x12\x0e\n\nREAD_WRITE\x10\x02\x42\x0e\n\x06target\x12\x04\xc0\xc1\x31\x01J\x04\x08\x02\x10\x03J\x04\x08\x04\x10\n\"\xde\x03\n\x15\x41syncInvocationConfig\x12 \n\rretries_count\x18\x01 \x01(\x03\x42\t\xfa\xc7\x31\x05\x30-100\x12h\n\x0esuccess_target\x18\x02 \x01(\x0b\x32J.yandex.cloud.serverless.functions.v1.AsyncInvocationConfig.ResponseTargetB\x04\xe8\xc7\x31\x01\x12h\n\x0e\x66\x61ilure_target\x18\x03 \x01(\x0b\x32J.yandex.cloud.serverless.functions.v1.AsyncInvocationConfig.ResponseTargetB\x04\xe8\xc7\x31\x01\x12\x1a\n\x12service_account_id\x18\x04 \x01(\t\x1a\xb2\x01\n\x0eResponseTarget\x12I\n\x0c\x65mpty_target\x18\x01 \x01(\x0b\x32\x31.yandex.cloud.serverless.functions.v1.EmptyTargetH\x00\x12\x45\n\nymq_target\x18\x02 \x01(\x0b\x32/.yandex.cloud.serverless.functions.v1.YMQTargetH\x00\x42\x0e\n\x06target\x12\x04\xc0\xc1\x31\x01\"N\n\tYMQTarget\x12\x17\n\tqueue_arn\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12(\n\x12service_account_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\r\n\x0b\x45mptyTarget\"\xb6\x01\n\x0fMetadataOptions\x12O\n\x11gce_http_endpoint\x18\x01 \x01(\x0e\x32\x34.yandex.cloud.serverless.functions.v1.MetadataOption\x12R\n\x14\x61ws_v1_http_endpoint\x18\x02 \x01(\x0e\x32\x34.yandex.cloud.serverless.functions.v1.MetadataOption*L\n\x0eMetadataOption\x12\x1f\n\x1bMETADATA_OPTION_UNSPECIFIED\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02\x42~\n(yandex.cloud.api.serverless.functions.v1ZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/functions/v1;functionsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.serverless.functions.v1.function_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n(yandex.cloud.api.serverless.functions.v1ZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/functions/v1;functions'
  _globals['_FUNCTION_LABELSENTRY']._loaded_options = None
  _globals['_FUNCTION_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_FUNCTION'].fields_by_name['name']._loaded_options = None
  _globals['_FUNCTION'].fields_by_name['name']._serialized_options = b'\212\3101\0043-63'
  _globals['_FUNCTION'].fields_by_name['description']._loaded_options = None
  _globals['_FUNCTION'].fields_by_name['description']._serialized_options = b'\212\3101\0050-256'
  _globals['_FUNCTION'].fields_by_name['labels']._loaded_options = None
  _globals['_FUNCTION'].fields_by_name['labels']._serialized_options = b'\202\3101\004<=64'
  _globals['_VERSION_ENVIRONMENTENTRY']._loaded_options = None
  _globals['_VERSION_ENVIRONMENTENTRY']._serialized_options = b'8\001'
  _globals['_VERSION_NAMEDSERVICEACCOUNTSENTRY']._loaded_options = None
  _globals['_VERSION_NAMEDSERVICEACCOUNTSENTRY']._serialized_options = b'8\001'
  _globals['_VERSION'].fields_by_name['description']._loaded_options = None
  _globals['_VERSION'].fields_by_name['description']._serialized_options = b'\212\3101\0050-256'
  _globals['_VERSION'].fields_by_name['concurrency']._loaded_options = None
  _globals['_VERSION'].fields_by_name['concurrency']._serialized_options = b'\372\3071\0040-16'
  _globals['_RESOURCES'].fields_by_name['memory']._loaded_options = None
  _globals['_RESOURCES'].fields_by_name['memory']._serialized_options = b'\372\3071\024134217728-8589934592'
  _globals['_PACKAGE'].fields_by_name['bucket_name']._loaded_options = None
  _globals['_PACKAGE'].fields_by_name['bucket_name']._serialized_options = b'\350\3071\001'
  _globals['_PACKAGE'].fields_by_name['object_name']._loaded_options = None
  _globals['_PACKAGE'].fields_by_name['object_name']._serialized_options = b'\350\3071\001'
  _globals['_CONNECTIVITY'].fields_by_name['subnet_id']._loaded_options = None
  _globals['_CONNECTIVITY'].fields_by_name['subnet_id']._serialized_options = b'\212\3101\002>0\220\3101\001'
  _globals['_LOGOPTIONS'].fields_by_name['log_group_id']._loaded_options = None
  _globals['_LOGOPTIONS'].fields_by_name['log_group_id']._serialized_options = b'\362\3071\037([a-zA-Z][-a-zA-Z0-9_.]{0,63})?'
  _globals['_LOGOPTIONS'].fields_by_name['folder_id']._loaded_options = None
  _globals['_LOGOPTIONS'].fields_by_name['folder_id']._serialized_options = b'\362\3071\037([a-zA-Z][-a-zA-Z0-9_.]{0,63})?'
  _globals['_STORAGEMOUNT'].fields_by_name['bucket_id']._loaded_options = None
  _globals['_STORAGEMOUNT'].fields_by_name['bucket_id']._serialized_options = b'\350\3071\001\362\3071\016[-.0-9a-zA-Z]*\212\3101\0043-63'
  _globals['_STORAGEMOUNT'].fields_by_name['mount_point_name']._loaded_options = None
  _globals['_STORAGEMOUNT'].fields_by_name['mount_point_name']._serialized_options = b'\350\3071\001\362\3071\016[-_0-9a-zA-Z]*\212\3101\0051-100'
  _globals['_STORAGEMOUNT']._loaded_options = None
  _globals['_STORAGEMOUNT']._serialized_options = b'\030\001'
  _globals['_MOUNT_OBJECTSTORAGE'].fields_by_name['bucket_id']._loaded_options = None
  _globals['_MOUNT_OBJECTSTORAGE'].fields_by_name['bucket_id']._serialized_options = b'\350\3071\001\362\3071\016[-.0-9a-zA-Z]*\212\3101\0043-63'
  _globals['_MOUNT_DISKSPEC'].fields_by_name['size']._loaded_options = None
  _globals['_MOUNT_DISKSPEC'].fields_by_name['size']._serialized_options = b'\372\3071\002>0'
  _globals['_MOUNT'].oneofs_by_name['target']._loaded_options = None
  _globals['_MOUNT'].oneofs_by_name['target']._serialized_options = b'\300\3011\001'
  _globals['_MOUNT'].fields_by_name['name']._loaded_options = None
  _globals['_MOUNT'].fields_by_name['name']._serialized_options = b'\350\3071\001\362\3071\016[-_0-9a-zA-Z]*\212\3101\0051-100'
  _globals['_ASYNCINVOCATIONCONFIG_RESPONSETARGET'].oneofs_by_name['target']._loaded_options = None
  _globals['_ASYNCINVOCATIONCONFIG_RESPONSETARGET'].oneofs_by_name['target']._serialized_options = b'\300\3011\001'
  _globals['_ASYNCINVOCATIONCONFIG'].fields_by_name['retries_count']._loaded_options = None
  _globals['_ASYNCINVOCATIONCONFIG'].fields_by_name['retries_count']._serialized_options = b'\372\3071\0050-100'
  _globals['_ASYNCINVOCATIONCONFIG'].fields_by_name['success_target']._loaded_options = None
  _globals['_ASYNCINVOCATIONCONFIG'].fields_by_name['success_target']._serialized_options = b'\350\3071\001'
  _globals['_ASYNCINVOCATIONCONFIG'].fields_by_name['failure_target']._loaded_options = None
  _globals['_ASYNCINVOCATIONCONFIG'].fields_by_name['failure_target']._serialized_options = b'\350\3071\001'
  _globals['_YMQTARGET'].fields_by_name['queue_arn']._loaded_options = None
  _globals['_YMQTARGET'].fields_by_name['queue_arn']._serialized_options = b'\350\3071\001'
  _globals['_YMQTARGET'].fields_by_name['service_account_id']._loaded_options = None
  _globals['_YMQTARGET'].fields_by_name['service_account_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_METADATAOPTION']._serialized_start=4320
  _globals['_METADATAOPTION']._serialized_end=4396
  _globals['_FUNCTION']._serialized_start=231
  _globals['_FUNCTION']._serialized_end=696
  _globals['_FUNCTION_LABELSENTRY']._serialized_start=560
  _globals['_FUNCTION_LABELSENTRY']._serialized_end=605
  _globals['_FUNCTION_STATUS']._serialized_start=607
  _globals['_FUNCTION_STATUS']._serialized_end=690
  _globals['_VERSION']._serialized_start=699
  _globals['_VERSION']._serialized_end=2092
  _globals['_VERSION_ENVIRONMENTENTRY']._serialized_start=1875
  _globals['_VERSION_ENVIRONMENTENTRY']._serialized_end=1925
  _globals['_VERSION_NAMEDSERVICEACCOUNTSENTRY']._serialized_start=1927
  _globals['_VERSION_NAMEDSERVICEACCOUNTSENTRY']._serialized_end=1986
  _globals['_VERSION_STATUS']._serialized_start=1988
  _globals['_VERSION_STATUS']._serialized_end=2074
  _globals['_RESOURCES']._serialized_start=2094
  _globals['_RESOURCES']._serialized_end=2147
  _globals['_PACKAGE']._serialized_start=2149
  _globals['_PACKAGE']._serialized_end=2228
  _globals['_CONNECTIVITY']._serialized_start=2230
  _globals['_CONNECTIVITY']._serialized_end=2295
  _globals['_SCALINGPOLICY']._serialized_start=2298
  _globals['_SCALINGPOLICY']._serialized_end=2546
  _globals['_SECRET']._serialized_start=2548
  _globals['_SECRET']._serialized_end=2646
  _globals['_LOGOPTIONS']._serialized_start=2649
  _globals['_LOGOPTIONS']._serialized_end=2873
  _globals['_STORAGEMOUNT']._serialized_start=2876
  _globals['_STORAGEMOUNT']._serialized_end=3039
  _globals['_MOUNT']._serialized_start=3042
  _globals['_MOUNT']._serialized_end=3557
  _globals['_MOUNT_OBJECTSTORAGE']._serialized_start=3332
  _globals['_MOUNT_OBJECTSTORAGE']._serialized_end=3414
  _globals['_MOUNT_DISKSPEC']._serialized_start=3416
  _globals['_MOUNT_DISKSPEC']._serialized_end=3468
  _globals['_MOUNT_MODE']._serialized_start=3470
  _globals['_MOUNT_MODE']._serialized_end=3529
  _globals['_ASYNCINVOCATIONCONFIG']._serialized_start=3560
  _globals['_ASYNCINVOCATIONCONFIG']._serialized_end=4038
  _globals['_ASYNCINVOCATIONCONFIG_RESPONSETARGET']._serialized_start=3860
  _globals['_ASYNCINVOCATIONCONFIG_RESPONSETARGET']._serialized_end=4038
  _globals['_YMQTARGET']._serialized_start=4040
  _globals['_YMQTARGET']._serialized_end=4118
  _globals['_EMPTYTARGET']._serialized_start=4120
  _globals['_EMPTYTARGET']._serialized_end=4133
  _globals['_METADATAOPTIONS']._serialized_start=4136
  _globals['_METADATAOPTIONS']._serialized_end=4318
# @@protoc_insertion_point(module_scope)
