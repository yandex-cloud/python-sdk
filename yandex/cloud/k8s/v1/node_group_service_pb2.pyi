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
import yandex.cloud.k8s.v1.node_group_pb2
import yandex.cloud.k8s.v1.node_pb2
import yandex.cloud.k8s.v1.version_pb2
import yandex.cloud.operation.operation_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetNodeGroupRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NODE_GROUP_ID_FIELD_NUMBER: builtins.int
    node_group_id: builtins.str
    """ID of the node group to return.
    To get the node group ID use a [NodeGroupService.List] request.
    """
    def __init__(
        self,
        *,
        node_group_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["node_group_id", b"node_group_id"]) -> None: ...

global___GetNodeGroupRequest = GetNodeGroupRequest

@typing.final
class ListNodeGroupsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to list node groups in.
    To get the folder ID use a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListNodeGroupsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set `page_token` to the
    [ListNodeGroupsResponse.next_page_token] returned by a previous list request.
    """
    filter: builtins.str
    """A filter expression that filters resources listed in the response.
    The expression must specify:
    1. The field name. Currently you can use filtering only on [NodeGroup.name] field.
    2. An `=` operator.
    3. The value in double quotes (`"`). Must be 3-63 characters long and match the regular expression `[a-z][-a-z0-9]{1,61}[a-z0-9]`.
    """
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["filter", b"filter", "folder_id", b"folder_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListNodeGroupsRequest = ListNodeGroupsRequest

@typing.final
class ListNodeGroupsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NODE_GROUPS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListNodeGroupsRequest.page_size], use
    the `next_page_token` as the value
    for the [ListNodeGroupsRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    `next_page_token` to continue paging through the results.
    """
    @property
    def node_groups(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.k8s.v1.node_group_pb2.NodeGroup]:
        """List of node groups."""

    def __init__(
        self,
        *,
        node_groups: collections.abc.Iterable[yandex.cloud.k8s.v1.node_group_pb2.NodeGroup] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "node_groups", b"node_groups"]) -> None: ...

global___ListNodeGroupsResponse = ListNodeGroupsResponse

@typing.final
class ListNodeGroupNodesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NODE_GROUP_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    node_group_id: builtins.str
    """ID of the node group to list.
    To get the node group ID use a [NodeGroupService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListNodeGroupsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set `page_token` to the
    [ListNodeGroupNodesResponse.next_page_token] returned by a previous list request.
    """
    def __init__(
        self,
        *,
        node_group_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["node_group_id", b"node_group_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListNodeGroupNodesRequest = ListNodeGroupNodesRequest

@typing.final
class ListNodeGroupNodesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NODES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListNodeGroupNodesRequest.page_size], use
    the `next_page_token` as the value
    for the [ListNodeGroupNodesRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    `next_page_token` to continue paging through the results.
    """
    @property
    def nodes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.k8s.v1.node_pb2.Node]:
        """List of nodes."""

    def __init__(
        self,
        *,
        nodes: collections.abc.Iterable[yandex.cloud.k8s.v1.node_pb2.Node] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "nodes", b"nodes"]) -> None: ...

global___ListNodeGroupNodesResponse = ListNodeGroupNodesResponse

@typing.final
class DeleteNodeGroupRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NODE_GROUP_ID_FIELD_NUMBER: builtins.int
    node_group_id: builtins.str
    """ID of the node group to delete.
    To get node group ID use a [NodeGroupService.List] request.
    """
    def __init__(
        self,
        *,
        node_group_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["node_group_id", b"node_group_id"]) -> None: ...

global___DeleteNodeGroupRequest = DeleteNodeGroupRequest

@typing.final
class DeleteNodeGroupMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NODE_GROUP_ID_FIELD_NUMBER: builtins.int
    node_group_id: builtins.str
    """ID of the node group that is being deleted."""
    def __init__(
        self,
        *,
        node_group_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["node_group_id", b"node_group_id"]) -> None: ...

global___DeleteNodeGroupMetadata = DeleteNodeGroupMetadata

@typing.final
class UpdateNodeGroupRequest(google.protobuf.message.Message):
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

    @typing.final
    class NodeLabelsEntry(google.protobuf.message.Message):
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

    NODE_GROUP_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    NODE_TEMPLATE_FIELD_NUMBER: builtins.int
    SCALE_POLICY_FIELD_NUMBER: builtins.int
    ALLOCATION_POLICY_FIELD_NUMBER: builtins.int
    DEPLOY_POLICY_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    MAINTENANCE_POLICY_FIELD_NUMBER: builtins.int
    ALLOWED_UNSAFE_SYSCTLS_FIELD_NUMBER: builtins.int
    NODE_TAINTS_FIELD_NUMBER: builtins.int
    NODE_LABELS_FIELD_NUMBER: builtins.int
    node_group_id: builtins.str
    """ID of the node group to update.
    To get the node group ID use a [NodeGroupService.List] request.
    """
    name: builtins.str
    """Name of the node group.
    The name must be unique within the folder.
    """
    description: builtins.str
    """Description of the node group."""
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which fields of the node group are going to be updated."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `key:value` pairs.

        Existing set of `labels` is completely replaced by the provided set.
        """

    @property
    def node_template(self) -> yandex.cloud.k8s.v1.node_pb2.NodeTemplate:
        """Node template for the node group.
        Change may trigger nodes rolling reboot or recreate.
        """

    @property
    def scale_policy(self) -> yandex.cloud.k8s.v1.node_group_pb2.ScalePolicy:
        """Scale policy of the node group."""

    @property
    def allocation_policy(self) -> yandex.cloud.k8s.v1.node_group_pb2.NodeGroupAllocationPolicy:
        """Allocation policy of the node group by the zones and regions."""

    @property
    def deploy_policy(self) -> yandex.cloud.k8s.v1.node_group_pb2.DeployPolicy:
        """Deploy policy according to which the updates are rolled out. If not specified,
        the default is used.
        """

    @property
    def version(self) -> yandex.cloud.k8s.v1.version_pb2.UpdateVersionSpec:
        """Version of Kubernetes components that runs on the nodes."""

    @property
    def maintenance_policy(self) -> yandex.cloud.k8s.v1.node_group_pb2.NodeGroupMaintenancePolicy:
        """Maintenance policy of the node group."""

    @property
    def allowed_unsafe_sysctls(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Support for unsafe sysctl parameters. For more details see [documentation](https://kubernetes.io/docs/tasks/administer-cluster/sysctl-cluster/)."""

    @property
    def node_taints(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.k8s.v1.node_pb2.Taint]:
        """Taints that are applied to the nodes of the node group at creation time."""

    @property
    def node_labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Labels that are assigned to the nodes of the node group at creation time."""

    def __init__(
        self,
        *,
        node_group_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        node_template: yandex.cloud.k8s.v1.node_pb2.NodeTemplate | None = ...,
        scale_policy: yandex.cloud.k8s.v1.node_group_pb2.ScalePolicy | None = ...,
        allocation_policy: yandex.cloud.k8s.v1.node_group_pb2.NodeGroupAllocationPolicy | None = ...,
        deploy_policy: yandex.cloud.k8s.v1.node_group_pb2.DeployPolicy | None = ...,
        version: yandex.cloud.k8s.v1.version_pb2.UpdateVersionSpec | None = ...,
        maintenance_policy: yandex.cloud.k8s.v1.node_group_pb2.NodeGroupMaintenancePolicy | None = ...,
        allowed_unsafe_sysctls: collections.abc.Iterable[builtins.str] | None = ...,
        node_taints: collections.abc.Iterable[yandex.cloud.k8s.v1.node_pb2.Taint] | None = ...,
        node_labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["allocation_policy", b"allocation_policy", "deploy_policy", b"deploy_policy", "maintenance_policy", b"maintenance_policy", "node_template", b"node_template", "scale_policy", b"scale_policy", "update_mask", b"update_mask", "version", b"version"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["allocation_policy", b"allocation_policy", "allowed_unsafe_sysctls", b"allowed_unsafe_sysctls", "deploy_policy", b"deploy_policy", "description", b"description", "labels", b"labels", "maintenance_policy", b"maintenance_policy", "name", b"name", "node_group_id", b"node_group_id", "node_labels", b"node_labels", "node_taints", b"node_taints", "node_template", b"node_template", "scale_policy", b"scale_policy", "update_mask", b"update_mask", "version", b"version"]) -> None: ...

global___UpdateNodeGroupRequest = UpdateNodeGroupRequest

@typing.final
class UpdateNodeGroupMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NODE_GROUP_ID_FIELD_NUMBER: builtins.int
    node_group_id: builtins.str
    """ID of the Node group that is being updated."""
    def __init__(
        self,
        *,
        node_group_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["node_group_id", b"node_group_id"]) -> None: ...

global___UpdateNodeGroupMetadata = UpdateNodeGroupMetadata

@typing.final
class CreateNodeGroupRequest(google.protobuf.message.Message):
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

    @typing.final
    class NodeLabelsEntry(google.protobuf.message.Message):
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
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    NODE_TEMPLATE_FIELD_NUMBER: builtins.int
    SCALE_POLICY_FIELD_NUMBER: builtins.int
    ALLOCATION_POLICY_FIELD_NUMBER: builtins.int
    DEPLOY_POLICY_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    MAINTENANCE_POLICY_FIELD_NUMBER: builtins.int
    ALLOWED_UNSAFE_SYSCTLS_FIELD_NUMBER: builtins.int
    NODE_TAINTS_FIELD_NUMBER: builtins.int
    NODE_LABELS_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Kubernetes cluster to create a node group in.
    To get the Kubernetes cluster ID, use a [ClusterService.List] request.
    """
    name: builtins.str
    """Name of the node group.
    The name must be unique within the folder.
    """
    description: builtins.str
    """Description of the node group."""
    version: builtins.str
    """Version of Kubernetes components that runs on the nodes."""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `key:value` pairs."""

    @property
    def node_template(self) -> yandex.cloud.k8s.v1.node_pb2.NodeTemplate:
        """Node template for creating the node group."""

    @property
    def scale_policy(self) -> yandex.cloud.k8s.v1.node_group_pb2.ScalePolicy:
        """Scale policy of the node group."""

    @property
    def allocation_policy(self) -> yandex.cloud.k8s.v1.node_group_pb2.NodeGroupAllocationPolicy:
        """Allocation policy of the node group by the zones and regions."""

    @property
    def deploy_policy(self) -> yandex.cloud.k8s.v1.node_group_pb2.DeployPolicy:
        """Deploy policy according to which the updates are rolled out. If not specified,
        the default is used.
        """

    @property
    def maintenance_policy(self) -> yandex.cloud.k8s.v1.node_group_pb2.NodeGroupMaintenancePolicy:
        """Maintenance policy of the node group."""

    @property
    def allowed_unsafe_sysctls(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Support for unsafe sysctl parameters. For more details see [documentation](https://kubernetes.io/docs/tasks/administer-cluster/sysctl-cluster/)."""

    @property
    def node_taints(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.k8s.v1.node_pb2.Taint]:
        """Taints that are applied to the nodes of the node group at creation time."""

    @property
    def node_labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Labels that are assigned to the nodes of the node group at creation time."""

    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        node_template: yandex.cloud.k8s.v1.node_pb2.NodeTemplate | None = ...,
        scale_policy: yandex.cloud.k8s.v1.node_group_pb2.ScalePolicy | None = ...,
        allocation_policy: yandex.cloud.k8s.v1.node_group_pb2.NodeGroupAllocationPolicy | None = ...,
        deploy_policy: yandex.cloud.k8s.v1.node_group_pb2.DeployPolicy | None = ...,
        version: builtins.str = ...,
        maintenance_policy: yandex.cloud.k8s.v1.node_group_pb2.NodeGroupMaintenancePolicy | None = ...,
        allowed_unsafe_sysctls: collections.abc.Iterable[builtins.str] | None = ...,
        node_taints: collections.abc.Iterable[yandex.cloud.k8s.v1.node_pb2.Taint] | None = ...,
        node_labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["allocation_policy", b"allocation_policy", "deploy_policy", b"deploy_policy", "maintenance_policy", b"maintenance_policy", "node_template", b"node_template", "scale_policy", b"scale_policy"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["allocation_policy", b"allocation_policy", "allowed_unsafe_sysctls", b"allowed_unsafe_sysctls", "cluster_id", b"cluster_id", "deploy_policy", b"deploy_policy", "description", b"description", "labels", b"labels", "maintenance_policy", b"maintenance_policy", "name", b"name", "node_labels", b"node_labels", "node_taints", b"node_taints", "node_template", b"node_template", "scale_policy", b"scale_policy", "version", b"version"]) -> None: ...

global___CreateNodeGroupRequest = CreateNodeGroupRequest

@typing.final
class CreateNodeGroupMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NODE_GROUP_ID_FIELD_NUMBER: builtins.int
    node_group_id: builtins.str
    """ID of the node group that is being created."""
    def __init__(
        self,
        *,
        node_group_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["node_group_id", b"node_group_id"]) -> None: ...

global___CreateNodeGroupMetadata = CreateNodeGroupMetadata

@typing.final
class AutoUpgradeNodeGroupMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NODE_GROUP_ID_FIELD_NUMBER: builtins.int
    node_group_id: builtins.str
    """ID of the node group that is being auto upgraded."""
    def __init__(
        self,
        *,
        node_group_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["node_group_id", b"node_group_id"]) -> None: ...

global___AutoUpgradeNodeGroupMetadata = AutoUpgradeNodeGroupMetadata

@typing.final
class ListNodeGroupOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NODE_GROUP_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    node_group_id: builtins.str
    """ID of the node group to list operations for."""
    page_size: builtins.int
    """The maximum number of results per page that should be returned. If the number of available
    results is larger than [page_size], the service returns a [ListNodeGroupOperationsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set `page_token` to the
    [ListNodeGroupOperationsResponse.next_page_token] returned by a previous list request.
    """
    filter: builtins.str
    """A filter expression that filters resources listed in the response.
    Currently you can use filtering only on [NodeGroup.name] field.
    """
    def __init__(
        self,
        *,
        node_group_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["filter", b"filter", "node_group_id", b"node_group_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListNodeGroupOperationsRequest = ListNodeGroupOperationsRequest

@typing.final
class ListNodeGroupOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListNodeGroupOperationsRequest.page_size], use the `next_page_token` as the value
    for the [ListNodeGroupOperationsRequest.page_token] query parameter in the next list request.
    Each subsequent list request will have its own `next_page_token` to continue paging through the results.
    """
    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.operation.operation_pb2.Operation]:
        """List of operations for the specified node group."""

    def __init__(
        self,
        *,
        operations: collections.abc.Iterable[yandex.cloud.operation.operation_pb2.Operation] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "operations", b"operations"]) -> None: ...

global___ListNodeGroupOperationsResponse = ListNodeGroupOperationsResponse
