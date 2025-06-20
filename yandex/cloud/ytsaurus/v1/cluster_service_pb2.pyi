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
import yandex.cloud.ytsaurus.v1.cluster_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetClusterRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the cluster to return."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id"]) -> None: ...

global___GetClusterRequest = GetClusterRequest

@typing.final
class ListClustersRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to list clusters in."""
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than `page_size`, the service returns a [ListClustersResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set `page_token` to the
    [ListClustersResponse.next_page_token] returned by a previous list request.
    """
    @property
    def filter(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """A filter expression that filters clusters listed in the response."""

    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["filter", b"filter", "folder_id", b"folder_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListClustersRequest = ListClustersRequest

@typing.final
class ListClustersResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTERS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListClustersRequest.page_size], use the [next_page_token] as the value
    for the [ListClustersRequest.page_token] query parameter in the next list request.
    Each subsequent list request will have its own [next_page_token] to continue paging through the results.
    """
    @property
    def clusters(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.ytsaurus.v1.cluster_pb2.Cluster]:
        """List of clusters in the specified folder."""

    def __init__(
        self,
        *,
        clusters: collections.abc.Iterable[yandex.cloud.ytsaurus.v1.cluster_pb2.Cluster] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["clusters", b"clusters", "next_page_token", b"next_page_token"]) -> None: ...

global___ListClustersResponse = ListClustersResponse

@typing.final
class CreateClusterRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class LabelsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    FOLDER_ID_FIELD_NUMBER: builtins.int
    ZONE_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    SUBNET_ID_FIELD_NUMBER: builtins.int
    SECURITY_GROUP_IDS_FIELD_NUMBER: builtins.int
    SPEC_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to create the cluster in."""
    zone_id: builtins.str
    """ID of the availability zone where the cluster resides."""
    name: builtins.str
    """Name of the cluster."""
    description: builtins.str
    """Description of the cluster."""
    subnet_id: builtins.str
    """ID of the subnet to create the cluster in."""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Cluster labels as `key:value` pairs."""

    @property
    def security_group_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """IDs of the security groups to attach to the cluster."""

    @property
    def spec(self) -> yandex.cloud.ytsaurus.v1.cluster_pb2.ClusterSpec:
        """Cluster specification."""

    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        zone_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        subnet_id: builtins.str = ...,
        security_group_ids: collections.abc.Iterable[builtins.str] | None = ...,
        spec: yandex.cloud.ytsaurus.v1.cluster_pb2.ClusterSpec | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["spec", b"spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "folder_id", b"folder_id", "labels", b"labels", "name", b"name", "security_group_ids", b"security_group_ids", "spec", b"spec", "subnet_id", b"subnet_id", "zone_id", b"zone_id"]) -> None: ...

global___CreateClusterRequest = CreateClusterRequest

@typing.final
class CreateClusterMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the cluster being created."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id"]) -> None: ...

global___CreateClusterMetadata = CreateClusterMetadata

@typing.final
class UpdateClusterRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class LabelsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    SUBNET_ID_FIELD_NUMBER: builtins.int
    SECURITY_GROUP_IDS_FIELD_NUMBER: builtins.int
    SPEC_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the cluster to update."""
    name: builtins.str
    """New name for the cluster.
    The name must be unique within the folder.
    """
    description: builtins.str
    """New description for the cluster."""
    subnet_id: builtins.str
    """New subnet for the cluster."""
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which attributes of the cluster should be updated."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Cluster labels as `key:value` pairs.

        Existing set of labels is completely replaced by the provided set, so if you just want
        to add or remove a label:
        1. Get the current set of labels with a [ClusterService.Get] request.
        2. Add or remove a label in this set.
        3. Send the new set in this field.
        """

    @property
    def security_group_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """New security groups for the cluster."""

    @property
    def spec(self) -> yandex.cloud.ytsaurus.v1.cluster_pb2.ClusterSpec:
        """New cluster specification."""

    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        subnet_id: builtins.str = ...,
        security_group_ids: collections.abc.Iterable[builtins.str] | None = ...,
        spec: yandex.cloud.ytsaurus.v1.cluster_pb2.ClusterSpec | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["spec", b"spec", "update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "description", b"description", "labels", b"labels", "name", b"name", "security_group_ids", b"security_group_ids", "spec", b"spec", "subnet_id", b"subnet_id", "update_mask", b"update_mask"]) -> None: ...

global___UpdateClusterRequest = UpdateClusterRequest

@typing.final
class UpdateClusterMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the cluster that is being updated."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id"]) -> None: ...

global___UpdateClusterMetadata = UpdateClusterMetadata

@typing.final
class DeleteClusterRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the cluster to delete."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id"]) -> None: ...

global___DeleteClusterRequest = DeleteClusterRequest

@typing.final
class DeleteClusterMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the cluster that is being deleted."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id"]) -> None: ...

global___DeleteClusterMetadata = DeleteClusterMetadata

@typing.final
class StartClusterRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the cluster to start."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id"]) -> None: ...

global___StartClusterRequest = StartClusterRequest

@typing.final
class StartClusterMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the cluster that is being started."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id"]) -> None: ...

global___StartClusterMetadata = StartClusterMetadata

@typing.final
class StopClusterRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the cluster to stop."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id"]) -> None: ...

global___StopClusterRequest = StopClusterRequest

@typing.final
class StopClusterMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the cluster that is being stopped."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id"]) -> None: ...

global___StopClusterMetadata = StopClusterMetadata
