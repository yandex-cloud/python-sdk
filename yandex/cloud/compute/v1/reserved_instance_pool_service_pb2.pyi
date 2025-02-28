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
import yandex.cloud.compute.v1.instance_pb2
import yandex.cloud.compute.v1.instance_service_pb2
import yandex.cloud.compute.v1.reserved_instance_pool_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetReservedInstancePoolRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESERVED_INSTANCE_POOL_ID_FIELD_NUMBER: builtins.int
    reserved_instance_pool_id: builtins.str
    """ID of the reserved instance pool resource to return.
    To get the reserved instance pool ID, use a [ReservedInstancePoolService.List] request.
    """
    def __init__(
        self,
        *,
        reserved_instance_pool_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["reserved_instance_pool_id", b"reserved_instance_pool_id"]) -> None: ...

global___GetReservedInstancePoolRequest = GetReservedInstancePoolRequest

@typing.final
class ListReservedInstancePoolsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    ORDER_BY_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the Folder to list reserved instance pools in.
    To get the folder ID, use a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListReservedInstancePoolsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    """
    page_token: builtins.str
    """Page token. To get the next page of results,
    set [page_token] to the [ListReservedInstancePoolsResponse.next_page_token]
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

global___ListReservedInstancePoolsRequest = ListReservedInstancePoolsRequest

@typing.final
class ListReservedInstancePoolsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESERVED_INSTANCE_POOLS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListReservedInstancePoolsRequest.page_size], use
    the [next_page_token] as the value
    for the [ListReservedInstancePoolsRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    [next_page_token] to continue paging through the results.
    """
    @property
    def reserved_instance_pools(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.compute.v1.reserved_instance_pool_pb2.ReservedInstancePool]:
        """List of reserved instance pool resources."""

    def __init__(
        self,
        *,
        reserved_instance_pools: collections.abc.Iterable[yandex.cloud.compute.v1.reserved_instance_pool_pb2.ReservedInstancePool] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "reserved_instance_pools", b"reserved_instance_pools"]) -> None: ...

global___ListReservedInstancePoolsResponse = ListReservedInstancePoolsResponse

@typing.final
class CreateReservedInstancePoolRequest(google.protobuf.message.Message):
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

    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    ZONE_ID_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    PLATFORM_ID_FIELD_NUMBER: builtins.int
    RESOURCES_SPEC_FIELD_NUMBER: builtins.int
    GPU_SETTINGS_FIELD_NUMBER: builtins.int
    BOOT_DISK_SPEC_FIELD_NUMBER: builtins.int
    NETWORK_SETTINGS_FIELD_NUMBER: builtins.int
    SIZE_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the reserved instance pool."""
    description: builtins.str
    """Description of the reserved instance pool."""
    zone_id: builtins.str
    """ID of the availability zone where the reserved instance pool resides.
    To get a list of available zones, use the [yandex.cloud.compute.v1.ZoneService.List] request
    """
    folder_id: builtins.str
    """ID of the folder to create the reserved instance pool in.
    To get the folder ID, use a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    platform_id: builtins.str
    """ID of the hardware platform configuration for the reserved instance pool.
    This field affects the available values in [resources_spec] field.

    For more information, see [Platforms](/docs/compute/concepts/vm-platforms).
    """
    size: builtins.int
    """Desired size of the pool (number of slots for instances in this pool)."""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `key:value` pairs."""

    @property
    def resources_spec(self) -> yandex.cloud.compute.v1.instance_service_pb2.ResourcesSpec:
        """Computing resources of the reserved instance pool instances, such as the amount of memory and number of cores.
        To get a list of available values, see [Levels of core performance](/docs/compute/concepts/performance-levels).
        """

    @property
    def gpu_settings(self) -> yandex.cloud.compute.v1.instance_pb2.GpuSettings:
        """GPU settings."""

    @property
    def boot_disk_spec(self) -> yandex.cloud.compute.v1.reserved_instance_pool_pb2.BootDiskSpec:
        """Spec is used to determine which License IDs should be allowed for instances created in the pool."""

    @property
    def network_settings(self) -> yandex.cloud.compute.v1.instance_pb2.NetworkSettings:
        """Network settings."""

    def __init__(
        self,
        *,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        zone_id: builtins.str = ...,
        folder_id: builtins.str = ...,
        platform_id: builtins.str = ...,
        resources_spec: yandex.cloud.compute.v1.instance_service_pb2.ResourcesSpec | None = ...,
        gpu_settings: yandex.cloud.compute.v1.instance_pb2.GpuSettings | None = ...,
        boot_disk_spec: yandex.cloud.compute.v1.reserved_instance_pool_pb2.BootDiskSpec | None = ...,
        network_settings: yandex.cloud.compute.v1.instance_pb2.NetworkSettings | None = ...,
        size: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["boot_disk_spec", b"boot_disk_spec", "gpu_settings", b"gpu_settings", "network_settings", b"network_settings", "resources_spec", b"resources_spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["boot_disk_spec", b"boot_disk_spec", "description", b"description", "folder_id", b"folder_id", "gpu_settings", b"gpu_settings", "labels", b"labels", "name", b"name", "network_settings", b"network_settings", "platform_id", b"platform_id", "resources_spec", b"resources_spec", "size", b"size", "zone_id", b"zone_id"]) -> None: ...

global___CreateReservedInstancePoolRequest = CreateReservedInstancePoolRequest

@typing.final
class CreateReservedInstancePoolMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESERVED_INSTANCE_POOL_ID_FIELD_NUMBER: builtins.int
    reserved_instance_pool_id: builtins.str
    """ID of the reserved instance pool that is being created."""
    def __init__(
        self,
        *,
        reserved_instance_pool_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["reserved_instance_pool_id", b"reserved_instance_pool_id"]) -> None: ...

global___CreateReservedInstancePoolMetadata = CreateReservedInstancePoolMetadata

@typing.final
class UpdateReservedInstancePoolRequest(google.protobuf.message.Message):
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

    RESERVED_INSTANCE_POOL_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    SIZE_FIELD_NUMBER: builtins.int
    reserved_instance_pool_id: builtins.str
    """ID of the reserved instance pool to update.
    To get the reserved instance pool ID, use a [ReservedInstancePoolService.List] request.
    """
    name: builtins.str
    """New name for the reserved instance pool."""
    description: builtins.str
    """Description of the reserved instance pool."""
    size: builtins.int
    """Desired size of the pool."""
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which fields of the reserved instance pool should be updated."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `key:value` pairs.

        Existing set of `labels` is completely replaced by the provided set.
        """

    def __init__(
        self,
        *,
        reserved_instance_pool_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        size: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "labels", b"labels", "name", b"name", "reserved_instance_pool_id", b"reserved_instance_pool_id", "size", b"size", "update_mask", b"update_mask"]) -> None: ...

global___UpdateReservedInstancePoolRequest = UpdateReservedInstancePoolRequest

@typing.final
class UpdateReservedInstancePoolMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESERVED_INSTANCE_POOL_ID_FIELD_NUMBER: builtins.int
    reserved_instance_pool_id: builtins.str
    """ID of the reserved instance pool that is being updated."""
    def __init__(
        self,
        *,
        reserved_instance_pool_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["reserved_instance_pool_id", b"reserved_instance_pool_id"]) -> None: ...

global___UpdateReservedInstancePoolMetadata = UpdateReservedInstancePoolMetadata

@typing.final
class DeleteReservedInstancePoolRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESERVED_INSTANCE_POOL_ID_FIELD_NUMBER: builtins.int
    reserved_instance_pool_id: builtins.str
    """ID of the reserved instance pool to delete.
    To get the reserved instance pool ID, use a [ReservedInstancePoolService.List] request.
    """
    def __init__(
        self,
        *,
        reserved_instance_pool_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["reserved_instance_pool_id", b"reserved_instance_pool_id"]) -> None: ...

global___DeleteReservedInstancePoolRequest = DeleteReservedInstancePoolRequest

@typing.final
class DeleteReservedInstancePoolMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESERVED_INSTANCE_POOL_ID_FIELD_NUMBER: builtins.int
    reserved_instance_pool_id: builtins.str
    """ID of the reserved instance pool that is being deleted."""
    def __init__(
        self,
        *,
        reserved_instance_pool_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["reserved_instance_pool_id", b"reserved_instance_pool_id"]) -> None: ...

global___DeleteReservedInstancePoolMetadata = DeleteReservedInstancePoolMetadata

@typing.final
class DeleteReservedInstancePoolResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___DeleteReservedInstancePoolResponse = DeleteReservedInstancePoolResponse
