"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import yandex.cloud.mdb.clickhouse.v1.ml_model_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetMlModelRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    ML_MODEL_NAME_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the cluster that the model belongs to."""
    ml_model_name: builtins.str
    """Name of the model to return.

    To get a model name make a [MlModelService.List] request.
    """
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        ml_model_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "ml_model_name", b"ml_model_name"]) -> None: ...

global___GetMlModelRequest = GetMlModelRequest

@typing.final
class ListMlModelsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the cluster that models belongs to."""
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than `page_size`, the service returns a [ListMlModelsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set `page_token` to the
    [ListMlModelsResponse.next_page_token] returned by the previous list request.
    """
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListMlModelsRequest = ListMlModelsRequest

@typing.final
class ListMlModelsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ML_MODELS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token for getting the next page of the list. If the number of results is greater than
    the specified [ListMlModelsRequest.page_size], use `next_page_token` as the value
    for the [ListMlModelsRequest.page_token] parameter in the next list request.

    Each subsequent page will have its own `next_page_token` to continue paging through the results.
    """
    @property
    def ml_models(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.mdb.clickhouse.v1.ml_model_pb2.MlModel]:
        """List of models in the specified cluster."""

    def __init__(
        self,
        *,
        ml_models: collections.abc.Iterable[yandex.cloud.mdb.clickhouse.v1.ml_model_pb2.MlModel] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["ml_models", b"ml_models", "next_page_token", b"next_page_token"]) -> None: ...

global___ListMlModelsResponse = ListMlModelsResponse

@typing.final
class CreateMlModelRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    ML_MODEL_NAME_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the cluster to create a model in.

    To get a cluster ID make a [ClusterService.List] request.
    """
    ml_model_name: builtins.str
    """Model name. The model name is one of the arguments of the modelEvaluate() function, which is used to call the model in ClickHouse."""
    type: yandex.cloud.mdb.clickhouse.v1.ml_model_pb2.MlModelType.ValueType
    """Type of the model."""
    uri: builtins.str
    """Model file URL. You can only use models stored in Object Storage."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        ml_model_name: builtins.str = ...,
        type: yandex.cloud.mdb.clickhouse.v1.ml_model_pb2.MlModelType.ValueType = ...,
        uri: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "ml_model_name", b"ml_model_name", "type", b"type", "uri", b"uri"]) -> None: ...

global___CreateMlModelRequest = CreateMlModelRequest

@typing.final
class CreateMlModelMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    ML_MODEL_NAME_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the cluster that a model is being added to."""
    ml_model_name: builtins.str
    """Name of the the model that is being created."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        ml_model_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "ml_model_name", b"ml_model_name"]) -> None: ...

global___CreateMlModelMetadata = CreateMlModelMetadata

@typing.final
class UpdateMlModelRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    ML_MODEL_NAME_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the cluster to update the model in.

    To get a cluster ID make a [ClusterService.List] request.
    """
    ml_model_name: builtins.str
    """Name of the the model to update."""
    uri: builtins.str
    """The new model file URL. You can only use models stored in Object Storage."""
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask: ...
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        ml_model_name: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        uri: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "ml_model_name", b"ml_model_name", "update_mask", b"update_mask", "uri", b"uri"]) -> None: ...

global___UpdateMlModelRequest = UpdateMlModelRequest

@typing.final
class UpdateMlModelMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    ML_MODEL_NAME_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the cluster that contains the model being updated."""
    ml_model_name: builtins.str
    """Name of the the model that is being updated."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        ml_model_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "ml_model_name", b"ml_model_name"]) -> None: ...

global___UpdateMlModelMetadata = UpdateMlModelMetadata

@typing.final
class DeleteMlModelRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    ML_MODEL_NAME_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the cluster to delete the model in.

    To get a cluster ID make a [ClusterService.List] request.
    """
    ml_model_name: builtins.str
    """Name of the the model to delete."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        ml_model_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "ml_model_name", b"ml_model_name"]) -> None: ...

global___DeleteMlModelRequest = DeleteMlModelRequest

@typing.final
class DeleteMlModelMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    ML_MODEL_NAME_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the cluster that contains the model being deleted."""
    ml_model_name: builtins.str
    """Name of the the model that is being deleted."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        ml_model_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "ml_model_name", b"ml_model_name"]) -> None: ...

global___DeleteMlModelMetadata = DeleteMlModelMetadata
