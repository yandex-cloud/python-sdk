# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/ai/foundation_models/v1/embedding/embedding_service.proto
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
    'yandex/cloud/ai/foundation_models/v1/embedding/embedding_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nFyandex/cloud/ai/foundation_models/v1/embedding/embedding_service.proto\x12$yandex.cloud.ai.foundation_models.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/wrappers.proto\"a\n\x14TextEmbeddingRequest\x12\x11\n\tmodel_uri\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12(\n\x03\x64im\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\"U\n\x15TextEmbeddingResponse\x12\x11\n\tembedding\x18\x01 \x03(\x01\x12\x12\n\nnum_tokens\x18\x02 \x01(\x03\x12\x15\n\rmodel_version\x18\x03 \x01(\t2\xcd\x01\n\x11\x45mbeddingsService\x12\xb7\x01\n\rTextEmbedding\x12:.yandex.cloud.ai.foundation_models.v1.TextEmbeddingRequest\x1a;.yandex.cloud.ai.foundation_models.v1.TextEmbeddingResponse\"-\x82\xd3\xe4\x93\x02\'\"\"/foundationModels/v1/textEmbedding:\x01*B\x90\x01\n(yandex.cloud.api.ai.foundation_models.v1Zdgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/foundation_models/v1/embedding;foundation_modelsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.ai.foundation_models.v1.embedding.embedding_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n(yandex.cloud.api.ai.foundation_models.v1Zdgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/foundation_models/v1/embedding;foundation_models'
  _globals['_EMBEDDINGSSERVICE'].methods_by_name['TextEmbedding']._loaded_options = None
  _globals['_EMBEDDINGSSERVICE'].methods_by_name['TextEmbedding']._serialized_options = b'\202\323\344\223\002\'\"\"/foundationModels/v1/textEmbedding:\001*'
  _globals['_TEXTEMBEDDINGREQUEST']._serialized_start=174
  _globals['_TEXTEMBEDDINGREQUEST']._serialized_end=271
  _globals['_TEXTEMBEDDINGRESPONSE']._serialized_start=273
  _globals['_TEXTEMBEDDINGRESPONSE']._serialized_end=358
  _globals['_EMBEDDINGSSERVICE']._serialized_start=361
  _globals['_EMBEDDINGSSERVICE']._serialized_end=566
# @@protoc_insertion_point(module_scope)
