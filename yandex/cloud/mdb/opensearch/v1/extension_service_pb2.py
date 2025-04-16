# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/mdb/opensearch/v1/extension_service.proto
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
    'yandex/cloud/mdb/opensearch/v1/extension_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.mdb.opensearch.v1 import extension_pb2 as yandex_dot_cloud_dot_mdb_dot_opensearch_dot_v1_dot_extension__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6yandex/cloud/mdb/opensearch/v1/extension_service.proto\x12\x1eyandex.cloud.mdb.opensearch.v1\x1a\x1cgoogle/api/annotations.proto\x1a yandex/cloud/api/operation.proto\x1a\x1dyandex/cloud/validation.proto\x1a.yandex/cloud/mdb/opensearch/v1/extension.proto\x1a&yandex/cloud/operation/operation.proto\"S\n\x13GetExtensionRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1a\n\x0c\x65xtension_id\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\"w\n\x15ListExtensionsRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"p\n\x16ListExtensionsResponse\x12=\n\nextensions\x18\x01 \x03(\x0b\x32).yandex.cloud.mdb.opensearch.v1.Extension\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"V\n\x16\x44\x65leteExtensionRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1a\n\x0c\x65xtension_id\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\"W\n\x17\x44\x65leteExtensionMetadata\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1a\n\x0c\x65xtension_id\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\"f\n\x16UpdateExtensionRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1a\n\x0c\x65xtension_id\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x0e\n\x06\x61\x63tive\x18\x03 \x01(\x08\"W\n\x17UpdateExtensionMetadata\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1a\n\x0c\x65xtension_id\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\"\x8d\x01\n\x16\x43reateExtensionRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12K\n\x0e\x65xtension_spec\x18\x05 \x01(\x0b\x32-.yandex.cloud.mdb.opensearch.v1.ExtensionSpecB\x04\xe8\xc7\x31\x01J\x04\x08\x02\x10\x05\"W\n\x17\x43reateExtensionMetadata\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1a\n\x0c\x65xtension_id\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\x32\xa1\x08\n\x10\x45xtensionService\x12\xb5\x01\n\x03Get\x12\x33.yandex.cloud.mdb.opensearch.v1.GetExtensionRequest\x1a).yandex.cloud.mdb.opensearch.v1.Extension\"N\x82\xd3\xe4\x93\x02H\x12\x46/managed-opensearch/v1/clusters/{cluster_id}/extensions/{extension_id}\x12\xb6\x01\n\x04List\x12\x35.yandex.cloud.mdb.opensearch.v1.ListExtensionsRequest\x1a\x36.yandex.cloud.mdb.opensearch.v1.ListExtensionsResponse\"?\x82\xd3\xe4\x93\x02\x39\x12\x37/managed-opensearch/v1/clusters/{cluster_id}/extensions\x12\xcf\x01\n\x06\x43reate\x12\x36.yandex.cloud.mdb.opensearch.v1.CreateExtensionRequest\x1a!.yandex.cloud.operation.Operation\"j\xb2\xd2*$\n\x17\x43reateExtensionMetadata\x12\tExtension\x82\xd3\xe4\x93\x02<\"7/managed-opensearch/v1/clusters/{cluster_id}/extensions:\x01*\x12\xde\x01\n\x06Update\x12\x36.yandex.cloud.mdb.opensearch.v1.UpdateExtensionRequest\x1a!.yandex.cloud.operation.Operation\"y\xb2\xd2*$\n\x17UpdateExtensionMetadata\x12\tExtension\x82\xd3\xe4\x93\x02K2F/managed-opensearch/v1/clusters/{cluster_id}/extensions/{extension_id}:\x01*\x12\xe8\x01\n\x06\x44\x65lete\x12\x36.yandex.cloud.mdb.opensearch.v1.DeleteExtensionRequest\x1a!.yandex.cloud.operation.Operation\"\x82\x01\xb2\xd2*0\n\x17\x44\x65leteExtensionMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02H*F/managed-opensearch/v1/clusters/{cluster_id}/extensions/{extension_id}Bs\n\"yandex.cloud.api.mdb.opensearch.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/opensearch/v1;opensearchb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.opensearch.v1.extension_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"yandex.cloud.api.mdb.opensearch.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/opensearch/v1;opensearch'
  _globals['_GETEXTENSIONREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_GETEXTENSIONREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_GETEXTENSIONREQUEST'].fields_by_name['extension_id']._loaded_options = None
  _globals['_GETEXTENSIONREQUEST'].fields_by_name['extension_id']._serialized_options = b'\350\3071\001'
  _globals['_LISTEXTENSIONSREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_LISTEXTENSIONSREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTEXTENSIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTEXTENSIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _globals['_LISTEXTENSIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTEXTENSIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_DELETEEXTENSIONREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_DELETEEXTENSIONREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_DELETEEXTENSIONREQUEST'].fields_by_name['extension_id']._loaded_options = None
  _globals['_DELETEEXTENSIONREQUEST'].fields_by_name['extension_id']._serialized_options = b'\350\3071\001'
  _globals['_DELETEEXTENSIONMETADATA'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_DELETEEXTENSIONMETADATA'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_DELETEEXTENSIONMETADATA'].fields_by_name['extension_id']._loaded_options = None
  _globals['_DELETEEXTENSIONMETADATA'].fields_by_name['extension_id']._serialized_options = b'\350\3071\001'
  _globals['_UPDATEEXTENSIONREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_UPDATEEXTENSIONREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_UPDATEEXTENSIONREQUEST'].fields_by_name['extension_id']._loaded_options = None
  _globals['_UPDATEEXTENSIONREQUEST'].fields_by_name['extension_id']._serialized_options = b'\350\3071\001'
  _globals['_UPDATEEXTENSIONMETADATA'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_UPDATEEXTENSIONMETADATA'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_UPDATEEXTENSIONMETADATA'].fields_by_name['extension_id']._loaded_options = None
  _globals['_UPDATEEXTENSIONMETADATA'].fields_by_name['extension_id']._serialized_options = b'\350\3071\001'
  _globals['_CREATEEXTENSIONREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_CREATEEXTENSIONREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_CREATEEXTENSIONREQUEST'].fields_by_name['extension_spec']._loaded_options = None
  _globals['_CREATEEXTENSIONREQUEST'].fields_by_name['extension_spec']._serialized_options = b'\350\3071\001'
  _globals['_CREATEEXTENSIONMETADATA'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_CREATEEXTENSIONMETADATA'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_CREATEEXTENSIONMETADATA'].fields_by_name['extension_id']._loaded_options = None
  _globals['_CREATEEXTENSIONMETADATA'].fields_by_name['extension_id']._serialized_options = b'\350\3071\001'
  _globals['_EXTENSIONSERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_EXTENSIONSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002H\022F/managed-opensearch/v1/clusters/{cluster_id}/extensions/{extension_id}'
  _globals['_EXTENSIONSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_EXTENSIONSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\0029\0227/managed-opensearch/v1/clusters/{cluster_id}/extensions'
  _globals['_EXTENSIONSERVICE'].methods_by_name['Create']._loaded_options = None
  _globals['_EXTENSIONSERVICE'].methods_by_name['Create']._serialized_options = b'\262\322*$\n\027CreateExtensionMetadata\022\tExtension\202\323\344\223\002<\"7/managed-opensearch/v1/clusters/{cluster_id}/extensions:\001*'
  _globals['_EXTENSIONSERVICE'].methods_by_name['Update']._loaded_options = None
  _globals['_EXTENSIONSERVICE'].methods_by_name['Update']._serialized_options = b'\262\322*$\n\027UpdateExtensionMetadata\022\tExtension\202\323\344\223\002K2F/managed-opensearch/v1/clusters/{cluster_id}/extensions/{extension_id}:\001*'
  _globals['_EXTENSIONSERVICE'].methods_by_name['Delete']._loaded_options = None
  _globals['_EXTENSIONSERVICE'].methods_by_name['Delete']._serialized_options = b'\262\322*0\n\027DeleteExtensionMetadata\022\025google.protobuf.Empty\202\323\344\223\002H*F/managed-opensearch/v1/clusters/{cluster_id}/extensions/{extension_id}'
  _globals['_GETEXTENSIONREQUEST']._serialized_start=273
  _globals['_GETEXTENSIONREQUEST']._serialized_end=356
  _globals['_LISTEXTENSIONSREQUEST']._serialized_start=358
  _globals['_LISTEXTENSIONSREQUEST']._serialized_end=477
  _globals['_LISTEXTENSIONSRESPONSE']._serialized_start=479
  _globals['_LISTEXTENSIONSRESPONSE']._serialized_end=591
  _globals['_DELETEEXTENSIONREQUEST']._serialized_start=593
  _globals['_DELETEEXTENSIONREQUEST']._serialized_end=679
  _globals['_DELETEEXTENSIONMETADATA']._serialized_start=681
  _globals['_DELETEEXTENSIONMETADATA']._serialized_end=768
  _globals['_UPDATEEXTENSIONREQUEST']._serialized_start=770
  _globals['_UPDATEEXTENSIONREQUEST']._serialized_end=872
  _globals['_UPDATEEXTENSIONMETADATA']._serialized_start=874
  _globals['_UPDATEEXTENSIONMETADATA']._serialized_end=961
  _globals['_CREATEEXTENSIONREQUEST']._serialized_start=964
  _globals['_CREATEEXTENSIONREQUEST']._serialized_end=1105
  _globals['_CREATEEXTENSIONMETADATA']._serialized_start=1107
  _globals['_CREATEEXTENSIONMETADATA']._serialized_end=1194
  _globals['_EXTENSIONSERVICE']._serialized_start=1197
  _globals['_EXTENSIONSERVICE']._serialized_end=2254
# @@protoc_insertion_point(module_scope)
