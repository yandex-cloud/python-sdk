# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/apploadbalancer/v1/backend_group.proto
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
    'yandex/cloud/apploadbalancer/v1/backend_group.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from yandex.cloud.apploadbalancer.v1 import payload_pb2 as yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_payload__pb2
from yandex.cloud.apploadbalancer.v1 import tls_pb2 as yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_tls__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3yandex/cloud/apploadbalancer/v1/backend_group.proto\x12\x1fyandex.cloud.apploadbalancer.v1\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a-yandex/cloud/apploadbalancer/v1/payload.proto\x1a)yandex/cloud/apploadbalancer/v1/tls.proto\x1a\x1dyandex/cloud/validation.proto\"\xd8\x03\n\x0c\x42\x61\x63kendGroup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x11\n\tfolder_id\x18\x04 \x01(\t\x12I\n\x06labels\x18\x05 \x03(\x0b\x32\x39.yandex.cloud.apploadbalancer.v1.BackendGroup.LabelsEntry\x12\x41\n\x04http\x18\x06 \x01(\x0b\x32\x31.yandex.cloud.apploadbalancer.v1.HttpBackendGroupH\x00\x12\x41\n\x04grpc\x18\x07 \x01(\x0b\x32\x31.yandex.cloud.apploadbalancer.v1.GrpcBackendGroupH\x00\x12\x45\n\x06stream\x18\n \x01(\x0b\x32\x33.yandex.cloud.apploadbalancer.v1.StreamBackendGroupH\x00\x12.\n\ncreated_at\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\t\n\x07\x62\x61\x63kendJ\x04\x08\x08\x10\t\"\xbc\x01\n\x12StreamBackendGroup\x12@\n\x08\x62\x61\x63kends\x18\x01 \x03(\x0b\x32..yandex.cloud.apploadbalancer.v1.StreamBackend\x12P\n\nconnection\x18\x02 \x01(\x0b\x32:.yandex.cloud.apploadbalancer.v1.ConnectionSessionAffinityH\x00\x42\x12\n\x10session_affinity\"\xcc\x02\n\x10HttpBackendGroup\x12>\n\x08\x62\x61\x63kends\x18\x01 \x03(\x0b\x32,.yandex.cloud.apploadbalancer.v1.HttpBackend\x12P\n\nconnection\x18\x02 \x01(\x0b\x32:.yandex.cloud.apploadbalancer.v1.ConnectionSessionAffinityH\x00\x12H\n\x06header\x18\x03 \x01(\x0b\x32\x36.yandex.cloud.apploadbalancer.v1.HeaderSessionAffinityH\x00\x12H\n\x06\x63ookie\x18\x04 \x01(\x0b\x32\x36.yandex.cloud.apploadbalancer.v1.CookieSessionAffinityH\x00\x42\x12\n\x10session_affinity\"\xcc\x02\n\x10GrpcBackendGroup\x12>\n\x08\x62\x61\x63kends\x18\x01 \x03(\x0b\x32,.yandex.cloud.apploadbalancer.v1.GrpcBackend\x12P\n\nconnection\x18\x02 \x01(\x0b\x32:.yandex.cloud.apploadbalancer.v1.ConnectionSessionAffinityH\x00\x12H\n\x06header\x18\x03 \x01(\x0b\x32\x36.yandex.cloud.apploadbalancer.v1.HeaderSessionAffinityH\x00\x12H\n\x06\x63ookie\x18\x04 \x01(\x0b\x32\x36.yandex.cloud.apploadbalancer.v1.CookieSessionAffinityH\x00\x42\x12\n\x10session_affinity\"7\n\x15HeaderSessionAffinity\x12\x1e\n\x0bheader_name\x18\x01 \x01(\tB\t\x8a\xc8\x31\x05\x31-256\"X\n\x15\x43ookieSessionAffinity\x12\x17\n\x04name\x18\x01 \x01(\tB\t\x8a\xc8\x31\x05\x31-256\x12&\n\x03ttl\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\".\n\x19\x43onnectionSessionAffinity\x12\x11\n\tsource_ip\x18\x01 \x01(\x08\"\xc7\x01\n\x13LoadBalancingConfig\x12\"\n\x0fpanic_threshold\x18\x01 \x01(\x03\x42\t\xfa\xc7\x31\x05\x30-100\x12\x31\n\x1elocality_aware_routing_percent\x18\x02 \x01(\x03\x42\t\xfa\xc7\x31\x05\x30-100\x12\x17\n\x0fstrict_locality\x18\x03 \x01(\x08\x12@\n\x04mode\x18\x04 \x01(\x0e\x32\x32.yandex.cloud.apploadbalancer.v1.LoadBalancingMode\"\x97\x04\n\rStreamBackend\x12.\n\x04name\x18\x01 \x01(\tB \xf2\xc7\x31\x1c[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x33\n\x0e\x62\x61\x63kend_weight\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12S\n\x15load_balancing_config\x18\x03 \x01(\x0b\x32\x34.yandex.cloud.apploadbalancer.v1.LoadBalancingConfig\x12\x19\n\x04port\x18\x04 \x01(\x03\x42\x0b\xfa\xc7\x31\x07\x30-65535\x12M\n\rtarget_groups\x18\x05 \x01(\x0b\x32\x34.yandex.cloud.apploadbalancer.v1.TargetGroupsBackendH\x00\x12\x42\n\x0chealthchecks\x18\x06 \x03(\x0b\x32,.yandex.cloud.apploadbalancer.v1.HealthCheck\x12\x38\n\x03tls\x18\x07 \x01(\x0b\x32+.yandex.cloud.apploadbalancer.v1.BackendTls\x12\x1d\n\x15\x65nable_proxy_protocol\x18\x08 \x01(\x08\x12/\n\'keep_connections_on_host_health_failure\x18\t \x01(\x08\x42\x14\n\x0c\x62\x61\x63kend_type\x12\x04\xc0\xc1\x31\x01\"\xad\x04\n\x0bHttpBackend\x12\x32\n\x04name\x18\x01 \x01(\tB$\xe8\xc7\x31\x01\xf2\xc7\x31\x1c[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x33\n\x0e\x62\x61\x63kend_weight\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12S\n\x15load_balancing_config\x18\x03 \x01(\x0b\x32\x34.yandex.cloud.apploadbalancer.v1.LoadBalancingConfig\x12\x19\n\x04port\x18\x04 \x01(\x03\x42\x0b\xfa\xc7\x31\x07\x30-65535\x12M\n\rtarget_groups\x18\x05 \x01(\x0b\x32\x34.yandex.cloud.apploadbalancer.v1.TargetGroupsBackendH\x00\x12O\n\x0estorage_bucket\x18\t \x01(\x0b\x32\x35.yandex.cloud.apploadbalancer.v1.StorageBucketBackendH\x00\x12\x42\n\x0chealthchecks\x18\x06 \x03(\x0b\x32,.yandex.cloud.apploadbalancer.v1.HealthCheck\x12\x38\n\x03tls\x18\x07 \x01(\x0b\x32+.yandex.cloud.apploadbalancer.v1.BackendTls\x12\x11\n\tuse_http2\x18\x08 \x01(\x08\x42\x14\n\x0c\x62\x61\x63kend_type\x12\x04\xc0\xc1\x31\x01\"\xcf\x03\n\x0bGrpcBackend\x12\x32\n\x04name\x18\x01 \x01(\tB$\xe8\xc7\x31\x01\xf2\xc7\x31\x1c[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x33\n\x0e\x62\x61\x63kend_weight\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12S\n\x15load_balancing_config\x18\x03 \x01(\x0b\x32\x34.yandex.cloud.apploadbalancer.v1.LoadBalancingConfig\x12\x19\n\x04port\x18\x04 \x01(\x03\x42\x0b\xfa\xc7\x31\x07\x30-65535\x12M\n\rtarget_groups\x18\x05 \x01(\x0b\x32\x34.yandex.cloud.apploadbalancer.v1.TargetGroupsBackendH\x00\x12\x42\n\x0chealthchecks\x18\x07 \x03(\x0b\x32,.yandex.cloud.apploadbalancer.v1.HealthCheck\x12\x38\n\x03tls\x18\x08 \x01(\x0b\x32+.yandex.cloud.apploadbalancer.v1.BackendTlsB\x14\n\x0c\x62\x61\x63kend_type\x12\x04\xc0\xc1\x31\x01J\x04\x08\x06\x10\x07\"7\n\x13TargetGroupsBackend\x12 \n\x10target_group_ids\x18\x01 \x03(\tB\x06\x82\xc8\x31\x02>0\"\x1c\n\x1aPlaintextTransportSettings\"|\n\x17SecureTransportSettings\x12\x0b\n\x03sni\x18\x01 \x01(\t\x12N\n\x12validation_context\x18\x03 \x01(\x0b\x32\x32.yandex.cloud.apploadbalancer.v1.ValidationContextJ\x04\x08\x02\x10\x03\"o\n\nBackendTls\x12\x0b\n\x03sni\x18\x01 \x01(\t\x12N\n\x12validation_context\x18\x03 \x01(\x0b\x32\x32.yandex.cloud.apploadbalancer.v1.ValidationContextJ\x04\x08\x02\x10\x03\",\n\x14StorageBucketBackend\x12\x14\n\x06\x62ucket\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"\xcc\x07\n\x0bHealthCheck\x12\x30\n\x07timeout\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x04\xe8\xc7\x31\x01\x12\x31\n\x08interval\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\x04\xe8\xc7\x31\x01\x12\x1f\n\x17interval_jitter_percent\x18\x03 \x01(\x01\x12\x19\n\x11healthy_threshold\x18\x04 \x01(\x03\x12\x1b\n\x13unhealthy_threshold\x18\x05 \x01(\x03\x12%\n\x10healthcheck_port\x18\x06 \x01(\x03\x42\x0b\xfa\xc7\x31\x07\x30-65535\x12P\n\x06stream\x18\x07 \x01(\x0b\x32>.yandex.cloud.apploadbalancer.v1.HealthCheck.StreamHealthCheckH\x00\x12L\n\x04http\x18\x08 \x01(\x0b\x32<.yandex.cloud.apploadbalancer.v1.HealthCheck.HttpHealthCheckH\x00\x12L\n\x04grpc\x18\t \x01(\x0b\x32<.yandex.cloud.apploadbalancer.v1.HealthCheck.GrpcHealthCheckH\x00\x12P\n\tplaintext\x18\n \x01(\x0b\x32;.yandex.cloud.apploadbalancer.v1.PlaintextTransportSettingsH\x01\x12G\n\x03tls\x18\x0b \x01(\x0b\x32\x38.yandex.cloud.apploadbalancer.v1.SecureTransportSettingsH\x01\x1a\x86\x01\n\x11StreamHealthCheck\x12\x36\n\x04send\x18\x01 \x01(\x0b\x32(.yandex.cloud.apploadbalancer.v1.Payload\x12\x39\n\x07receive\x18\x02 \x01(\x0b\x32(.yandex.cloud.apploadbalancer.v1.Payload\x1ar\n\x0fHttpHealthCheck\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x12\n\x04path\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x11\n\tuse_http2\x18\x03 \x01(\x08\x12*\n\x11\x65xpected_statuses\x18\x04 \x03(\x03\x42\x0f\xfa\xc7\x31\x07\x31\x30\x30-599\x90\xc8\x31\x01\x1a\'\n\x0fGrpcHealthCheck\x12\x14\n\x0cservice_name\x18\x01 \x01(\tB\x13\n\x0bhealthcheck\x12\x04\xc0\xc1\x31\x01\x42\x14\n\x12transport_settings*T\n\x11LoadBalancingMode\x12\x0f\n\x0bROUND_ROBIN\x10\x00\x12\n\n\x06RANDOM\x10\x01\x12\x11\n\rLEAST_REQUEST\x10\x02\x12\x0f\n\x0bMAGLEV_HASH\x10\x03\x42z\n#yandex.cloud.api.apploadbalancer.v1ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/apploadbalancer/v1;apploadbalancerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.apploadbalancer.v1.backend_group_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n#yandex.cloud.api.apploadbalancer.v1ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/apploadbalancer/v1;apploadbalancer'
  _globals['_BACKENDGROUP_LABELSENTRY']._loaded_options = None
  _globals['_BACKENDGROUP_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_HEADERSESSIONAFFINITY'].fields_by_name['header_name']._loaded_options = None
  _globals['_HEADERSESSIONAFFINITY'].fields_by_name['header_name']._serialized_options = b'\212\3101\0051-256'
  _globals['_COOKIESESSIONAFFINITY'].fields_by_name['name']._loaded_options = None
  _globals['_COOKIESESSIONAFFINITY'].fields_by_name['name']._serialized_options = b'\212\3101\0051-256'
  _globals['_LOADBALANCINGCONFIG'].fields_by_name['panic_threshold']._loaded_options = None
  _globals['_LOADBALANCINGCONFIG'].fields_by_name['panic_threshold']._serialized_options = b'\372\3071\0050-100'
  _globals['_LOADBALANCINGCONFIG'].fields_by_name['locality_aware_routing_percent']._loaded_options = None
  _globals['_LOADBALANCINGCONFIG'].fields_by_name['locality_aware_routing_percent']._serialized_options = b'\372\3071\0050-100'
  _globals['_STREAMBACKEND'].oneofs_by_name['backend_type']._loaded_options = None
  _globals['_STREAMBACKEND'].oneofs_by_name['backend_type']._serialized_options = b'\300\3011\001'
  _globals['_STREAMBACKEND'].fields_by_name['name']._loaded_options = None
  _globals['_STREAMBACKEND'].fields_by_name['name']._serialized_options = b'\362\3071\034[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _globals['_STREAMBACKEND'].fields_by_name['port']._loaded_options = None
  _globals['_STREAMBACKEND'].fields_by_name['port']._serialized_options = b'\372\3071\0070-65535'
  _globals['_HTTPBACKEND'].oneofs_by_name['backend_type']._loaded_options = None
  _globals['_HTTPBACKEND'].oneofs_by_name['backend_type']._serialized_options = b'\300\3011\001'
  _globals['_HTTPBACKEND'].fields_by_name['name']._loaded_options = None
  _globals['_HTTPBACKEND'].fields_by_name['name']._serialized_options = b'\350\3071\001\362\3071\034[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _globals['_HTTPBACKEND'].fields_by_name['port']._loaded_options = None
  _globals['_HTTPBACKEND'].fields_by_name['port']._serialized_options = b'\372\3071\0070-65535'
  _globals['_GRPCBACKEND'].oneofs_by_name['backend_type']._loaded_options = None
  _globals['_GRPCBACKEND'].oneofs_by_name['backend_type']._serialized_options = b'\300\3011\001'
  _globals['_GRPCBACKEND'].fields_by_name['name']._loaded_options = None
  _globals['_GRPCBACKEND'].fields_by_name['name']._serialized_options = b'\350\3071\001\362\3071\034[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _globals['_GRPCBACKEND'].fields_by_name['port']._loaded_options = None
  _globals['_GRPCBACKEND'].fields_by_name['port']._serialized_options = b'\372\3071\0070-65535'
  _globals['_TARGETGROUPSBACKEND'].fields_by_name['target_group_ids']._loaded_options = None
  _globals['_TARGETGROUPSBACKEND'].fields_by_name['target_group_ids']._serialized_options = b'\202\3101\002>0'
  _globals['_STORAGEBUCKETBACKEND'].fields_by_name['bucket']._loaded_options = None
  _globals['_STORAGEBUCKETBACKEND'].fields_by_name['bucket']._serialized_options = b'\350\3071\001'
  _globals['_HEALTHCHECK_HTTPHEALTHCHECK'].fields_by_name['path']._loaded_options = None
  _globals['_HEALTHCHECK_HTTPHEALTHCHECK'].fields_by_name['path']._serialized_options = b'\350\3071\001'
  _globals['_HEALTHCHECK_HTTPHEALTHCHECK'].fields_by_name['expected_statuses']._loaded_options = None
  _globals['_HEALTHCHECK_HTTPHEALTHCHECK'].fields_by_name['expected_statuses']._serialized_options = b'\372\3071\007100-599\220\3101\001'
  _globals['_HEALTHCHECK'].oneofs_by_name['healthcheck']._loaded_options = None
  _globals['_HEALTHCHECK'].oneofs_by_name['healthcheck']._serialized_options = b'\300\3011\001'
  _globals['_HEALTHCHECK'].fields_by_name['timeout']._loaded_options = None
  _globals['_HEALTHCHECK'].fields_by_name['timeout']._serialized_options = b'\350\3071\001'
  _globals['_HEALTHCHECK'].fields_by_name['interval']._loaded_options = None
  _globals['_HEALTHCHECK'].fields_by_name['interval']._serialized_options = b'\350\3071\001'
  _globals['_HEALTHCHECK'].fields_by_name['healthcheck_port']._loaded_options = None
  _globals['_HEALTHCHECK'].fields_by_name['healthcheck_port']._serialized_options = b'\372\3071\0070-65535'
  _globals['_LOADBALANCINGMODE']._serialized_start=4950
  _globals['_LOADBALANCINGMODE']._serialized_end=5034
  _globals['_BACKENDGROUP']._serialized_start=307
  _globals['_BACKENDGROUP']._serialized_end=779
  _globals['_BACKENDGROUP_LABELSENTRY']._serialized_start=717
  _globals['_BACKENDGROUP_LABELSENTRY']._serialized_end=762
  _globals['_STREAMBACKENDGROUP']._serialized_start=782
  _globals['_STREAMBACKENDGROUP']._serialized_end=970
  _globals['_HTTPBACKENDGROUP']._serialized_start=973
  _globals['_HTTPBACKENDGROUP']._serialized_end=1305
  _globals['_GRPCBACKENDGROUP']._serialized_start=1308
  _globals['_GRPCBACKENDGROUP']._serialized_end=1640
  _globals['_HEADERSESSIONAFFINITY']._serialized_start=1642
  _globals['_HEADERSESSIONAFFINITY']._serialized_end=1697
  _globals['_COOKIESESSIONAFFINITY']._serialized_start=1699
  _globals['_COOKIESESSIONAFFINITY']._serialized_end=1787
  _globals['_CONNECTIONSESSIONAFFINITY']._serialized_start=1789
  _globals['_CONNECTIONSESSIONAFFINITY']._serialized_end=1835
  _globals['_LOADBALANCINGCONFIG']._serialized_start=1838
  _globals['_LOADBALANCINGCONFIG']._serialized_end=2037
  _globals['_STREAMBACKEND']._serialized_start=2040
  _globals['_STREAMBACKEND']._serialized_end=2575
  _globals['_HTTPBACKEND']._serialized_start=2578
  _globals['_HTTPBACKEND']._serialized_end=3135
  _globals['_GRPCBACKEND']._serialized_start=3138
  _globals['_GRPCBACKEND']._serialized_end=3601
  _globals['_TARGETGROUPSBACKEND']._serialized_start=3603
  _globals['_TARGETGROUPSBACKEND']._serialized_end=3658
  _globals['_PLAINTEXTTRANSPORTSETTINGS']._serialized_start=3660
  _globals['_PLAINTEXTTRANSPORTSETTINGS']._serialized_end=3688
  _globals['_SECURETRANSPORTSETTINGS']._serialized_start=3690
  _globals['_SECURETRANSPORTSETTINGS']._serialized_end=3814
  _globals['_BACKENDTLS']._serialized_start=3816
  _globals['_BACKENDTLS']._serialized_end=3927
  _globals['_STORAGEBUCKETBACKEND']._serialized_start=3929
  _globals['_STORAGEBUCKETBACKEND']._serialized_end=3973
  _globals['_HEALTHCHECK']._serialized_start=3976
  _globals['_HEALTHCHECK']._serialized_end=4948
  _globals['_HEALTHCHECK_STREAMHEALTHCHECK']._serialized_start=4614
  _globals['_HEALTHCHECK_STREAMHEALTHCHECK']._serialized_end=4748
  _globals['_HEALTHCHECK_HTTPHEALTHCHECK']._serialized_start=4750
  _globals['_HEALTHCHECK_HTTPHEALTHCHECK']._serialized_end=4864
  _globals['_HEALTHCHECK_GRPCHEALTHCHECK']._serialized_start=4866
  _globals['_HEALTHCHECK_GRPCHEALTHCHECK']._serialized_end=4905
# @@protoc_insertion_point(module_scope)
