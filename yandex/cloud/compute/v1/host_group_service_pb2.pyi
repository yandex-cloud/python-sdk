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
import google.protobuf.timestamp_pb2
import typing
import yandex.cloud.compute.v1.host_group_pb2
import yandex.cloud.compute.v1.instance_pb2
import yandex.cloud.compute.v1.maintenance_pb2
import yandex.cloud.operation.operation_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetHostGroupRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOST_GROUP_ID_FIELD_NUMBER: builtins.int
    host_group_id: builtins.str
    """ID of the host group to return.
    To get the host group ID, use [HostGroupService.List] request.
    """
    def __init__(
        self,
        *,
        host_group_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["host_group_id", b"host_group_id"]) -> None: ...

global___GetHostGroupRequest = GetHostGroupRequest

@typing.final
class ListHostGroupsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    ORDER_BY_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to list host groups in.
    To get the folder ID, use [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListHostGroupsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    """
    page_token: builtins.str
    """Page token. To get the next page of results,
    set [page_token] to the [ListHostGroupsResponse.next_page_token]
    returned by a previous list request.
    """
    filter: builtins.str
    """A filter expression that filters resources listed in the response.
    The expression consists of one or more conditions united by `AND` operator: `<condition1> [AND <condition2> [<...> AND <conditionN>]]`.

    Each condition has the form `<field> <operator> <value>`, where:
    1. `<field>` is the field name. Currently you can use filtering only on the limited number of fields.
    2. `<operator>` is a logical operator, one of `=`, `!=`, `IN`, `NOT IN`.
    3. `<value>` represents a value.
    String values should be written in double (`"`) or single (`'`) quotes. C-style escape sequences are supported (`\\"` turns to `"`, `\\'` to `'`, `\\\\` to backslash).
    """
    order_by: builtins.str
    """By which column the listing should be ordered and in which direction,
    format is "createdAt desc". "id asc" if omitted.
    The default sorting order is ascending
    """
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: builtins.str = ...,
        order_by: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["filter", b"filter", "folder_id", b"folder_id", "order_by", b"order_by", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListHostGroupsRequest = ListHostGroupsRequest

@typing.final
class ListHostGroupsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOST_GROUPS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListHostGroupsRequest.page_size], use
    [next_page_token] as the value
    for the [ListHostGroupsRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    [next_page_token] to continue paging through the results.
    """
    @property
    def host_groups(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.compute.v1.host_group_pb2.HostGroup]:
        """Lists host groups for the specified folder."""

    def __init__(
        self,
        *,
        host_groups: collections.abc.Iterable[yandex.cloud.compute.v1.host_group_pb2.HostGroup] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["host_groups", b"host_groups", "next_page_token", b"next_page_token"]) -> None: ...

global___ListHostGroupsResponse = ListHostGroupsResponse

@typing.final
class CreateHostGroupRequest(google.protobuf.message.Message):
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
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    ZONE_ID_FIELD_NUMBER: builtins.int
    TYPE_ID_FIELD_NUMBER: builtins.int
    MAINTENANCE_POLICY_FIELD_NUMBER: builtins.int
    SCALE_POLICY_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to create a host group in.
    To get the folder ID, use a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    name: builtins.str
    """Name of the group."""
    description: builtins.str
    """Description of the group."""
    zone_id: builtins.str
    """Availability zone where all dedicated hosts will be allocated."""
    type_id: builtins.str
    """ID of host type. Resources provided by each host of the group."""
    maintenance_policy: yandex.cloud.compute.v1.maintenance_pb2.MaintenancePolicy.ValueType
    """Behaviour on maintenance events."""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `key:value` pairs."""

    @property
    def scale_policy(self) -> yandex.cloud.compute.v1.host_group_pb2.ScalePolicy:
        """Scale policy. Only fixed number of hosts are supported at this moment."""

    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        zone_id: builtins.str = ...,
        type_id: builtins.str = ...,
        maintenance_policy: yandex.cloud.compute.v1.maintenance_pb2.MaintenancePolicy.ValueType = ...,
        scale_policy: yandex.cloud.compute.v1.host_group_pb2.ScalePolicy | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["scale_policy", b"scale_policy"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "folder_id", b"folder_id", "labels", b"labels", "maintenance_policy", b"maintenance_policy", "name", b"name", "scale_policy", b"scale_policy", "type_id", b"type_id", "zone_id", b"zone_id"]) -> None: ...

global___CreateHostGroupRequest = CreateHostGroupRequest

@typing.final
class CreateHostGroupMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOST_GROUP_ID_FIELD_NUMBER: builtins.int
    host_group_id: builtins.str
    """ID of the host group that is being created."""
    def __init__(
        self,
        *,
        host_group_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["host_group_id", b"host_group_id"]) -> None: ...

global___CreateHostGroupMetadata = CreateHostGroupMetadata

@typing.final
class UpdateHostGroupRequest(google.protobuf.message.Message):
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

    HOST_GROUP_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    MAINTENANCE_POLICY_FIELD_NUMBER: builtins.int
    SCALE_POLICY_FIELD_NUMBER: builtins.int
    host_group_id: builtins.str
    """ID of the host group to update.
    To get the host group ID, use an [HostGroupService.List] request.
    """
    name: builtins.str
    """Name of the group."""
    description: builtins.str
    """Description of the group."""
    maintenance_policy: yandex.cloud.compute.v1.maintenance_pb2.MaintenancePolicy.ValueType
    """Behaviour on maintenance events"""
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which fields of the HostGroup resource are going to be updated."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `key:value` pairs.

        The existing set of `labels` is completely replaced by the provided set.
        """

    @property
    def scale_policy(self) -> yandex.cloud.compute.v1.host_group_pb2.ScalePolicy:
        """Scale policy. Only fixed number of hosts are supported at this moment."""

    def __init__(
        self,
        *,
        host_group_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        maintenance_policy: yandex.cloud.compute.v1.maintenance_pb2.MaintenancePolicy.ValueType = ...,
        scale_policy: yandex.cloud.compute.v1.host_group_pb2.ScalePolicy | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["scale_policy", b"scale_policy", "update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "host_group_id", b"host_group_id", "labels", b"labels", "maintenance_policy", b"maintenance_policy", "name", b"name", "scale_policy", b"scale_policy", "update_mask", b"update_mask"]) -> None: ...

global___UpdateHostGroupRequest = UpdateHostGroupRequest

@typing.final
class UpdateHostGroupMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOST_GROUP_ID_FIELD_NUMBER: builtins.int
    host_group_id: builtins.str
    """ID of the host group that is being updated."""
    def __init__(
        self,
        *,
        host_group_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["host_group_id", b"host_group_id"]) -> None: ...

global___UpdateHostGroupMetadata = UpdateHostGroupMetadata

@typing.final
class DeleteHostGroupRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOST_GROUP_ID_FIELD_NUMBER: builtins.int
    host_group_id: builtins.str
    """ID of the host group to delete.
    To get the host group ID, use [HostGroupService.List] request.
    """
    def __init__(
        self,
        *,
        host_group_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["host_group_id", b"host_group_id"]) -> None: ...

global___DeleteHostGroupRequest = DeleteHostGroupRequest

@typing.final
class DeleteHostGroupMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOST_GROUP_ID_FIELD_NUMBER: builtins.int
    host_group_id: builtins.str
    """ID of the host group that is being deleted."""
    def __init__(
        self,
        *,
        host_group_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["host_group_id", b"host_group_id"]) -> None: ...

global___DeleteHostGroupMetadata = DeleteHostGroupMetadata

@typing.final
class ListHostGroupInstancesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOST_GROUP_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    host_group_id: builtins.str
    """ID of the host group to list instances for.
    To get the host group ID, use [HostGroupService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListHostGroupInstancesResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    """
    page_token: builtins.str
    """Page token. To get the next page of results,
    set [page_token] to the [ListHostGroupInstancesResponse.next_page_token]
    returned by a previous list request.
    """
    filter: builtins.str
    """Filter support is not currently implemented. Any filters are ignored."""
    def __init__(
        self,
        *,
        host_group_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["filter", b"filter", "host_group_id", b"host_group_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListHostGroupInstancesRequest = ListHostGroupInstancesRequest

@typing.final
class ListHostGroupInstancesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INSTANCES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is more than [ListHostGroupInstancesRequest.page_size], use
    [next_page_token] as the value
    for the [ListHostGroupInstancesRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    [next_page_token] to continue paging through the results.
    """
    @property
    def instances(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.compute.v1.instance_pb2.Instance]:
        """Lists instances for the specified host group."""

    def __init__(
        self,
        *,
        instances: collections.abc.Iterable[yandex.cloud.compute.v1.instance_pb2.Instance] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["instances", b"instances", "next_page_token", b"next_page_token"]) -> None: ...

global___ListHostGroupInstancesResponse = ListHostGroupInstancesResponse

@typing.final
class ListHostGroupHostsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOST_GROUP_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    host_group_id: builtins.str
    """ID of the host group to list hosts for.
    To get the host group ID, use [HostGroupService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListHostGroupHostsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    """
    page_token: builtins.str
    """Page token. To get the next page of results,
    set [page_token] to the [ListHostGroupHostsResponse.next_page_token]
    returned by a previous list request.
    """
    def __init__(
        self,
        *,
        host_group_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["host_group_id", b"host_group_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListHostGroupHostsRequest = ListHostGroupHostsRequest

@typing.final
class ListHostGroupHostsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOSTS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is more than [ListHostGroupHostsRequest.page_size], use
    [next_page_token] as the value
    for the [ListHostGroupHostsRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    [next_page_token] to continue paging through the results.
    """
    @property
    def hosts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.compute.v1.host_group_pb2.Host]:
        """Lists hosts for the specified host group."""

    def __init__(
        self,
        *,
        hosts: collections.abc.Iterable[yandex.cloud.compute.v1.host_group_pb2.Host] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["hosts", b"hosts", "next_page_token", b"next_page_token"]) -> None: ...

global___ListHostGroupHostsResponse = ListHostGroupHostsResponse

@typing.final
class UpdateHostGroupHostRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOST_GROUP_ID_FIELD_NUMBER: builtins.int
    HOST_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    DEADLINE_AT_FIELD_NUMBER: builtins.int
    host_group_id: builtins.str
    """ID of the host group to update."""
    host_id: builtins.str
    """ID of the host to update."""
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which fields of the Host are going to be updated."""

    @property
    def deadline_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The date and time when this host will be automatically freed of instances.
        Timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.
        """

    def __init__(
        self,
        *,
        host_group_id: builtins.str = ...,
        host_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        deadline_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["deadline_at", b"deadline_at", "update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["deadline_at", b"deadline_at", "host_group_id", b"host_group_id", "host_id", b"host_id", "update_mask", b"update_mask"]) -> None: ...

global___UpdateHostGroupHostRequest = UpdateHostGroupHostRequest

@typing.final
class UpdateHostGroupHostMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOST_GROUP_ID_FIELD_NUMBER: builtins.int
    HOST_ID_FIELD_NUMBER: builtins.int
    host_group_id: builtins.str
    """ID of the host group that is being updated."""
    host_id: builtins.str
    """ID of the host that is being updated."""
    def __init__(
        self,
        *,
        host_group_id: builtins.str = ...,
        host_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["host_group_id", b"host_group_id", "host_id", b"host_id"]) -> None: ...

global___UpdateHostGroupHostMetadata = UpdateHostGroupHostMetadata

@typing.final
class ListHostGroupOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOST_GROUP_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    host_group_id: builtins.str
    """ID of the host group to list operations for.
    To get the host group ID, use [HostGroupService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size], the service returns a [ListHostGroupOperationsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token] to the
    [ListHostGroupOperationsResponse.next_page_token] returned by a previous list request.
    """
    def __init__(
        self,
        *,
        host_group_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["host_group_id", b"host_group_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListHostGroupOperationsRequest = ListHostGroupOperationsRequest

@typing.final
class ListHostGroupOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListHostGroupOperationsRequest.page_size], use the [next_page_token] as the value
    for the [ListHostGroupOperationsRequest.page_token] query parameter in the next list request.
    Each subsequent list request will have its own [next_page_token] to continue paging through the results.
    """
    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.operation.operation_pb2.Operation]:
        """List of operations for the specified host group."""

    def __init__(
        self,
        *,
        operations: collections.abc.Iterable[yandex.cloud.operation.operation_pb2.Operation] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "operations", b"operations"]) -> None: ...

global___ListHostGroupOperationsResponse = ListHostGroupOperationsResponse
