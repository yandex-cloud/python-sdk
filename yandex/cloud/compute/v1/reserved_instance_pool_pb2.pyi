"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import yandex.cloud.compute.v1.instance_pb2
import yandex.cloud.compute.v1.instance_service_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class ProductIDs(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PRODUCT_IDS_FIELD_NUMBER: builtins.int
    @property
    def product_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """License IDs that indicate which licenses are attached to resource.
        License IDs are used to calculate additional charges for the use of the virtual machine.
        """

    def __init__(
        self,
        *,
        product_ids: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["product_ids", b"product_ids"]) -> None: ...

global___ProductIDs = ProductIDs

@typing.final
class BootDiskSpec(google.protobuf.message.Message):
    """Specification used to determine required product_ids
    You can specify product ids explicitly or use disk_id|image_id|snapshot_id to infer products ids from them.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DISK_ID_FIELD_NUMBER: builtins.int
    IMAGE_ID_FIELD_NUMBER: builtins.int
    SNAPSHOT_ID_FIELD_NUMBER: builtins.int
    PRODUCT_IDS_FIELD_NUMBER: builtins.int
    disk_id: builtins.str
    """Disk ID."""
    image_id: builtins.str
    """Image ID."""
    snapshot_id: builtins.str
    """Snapshot ID."""
    @property
    def product_ids(self) -> global___ProductIDs:
        """Product IDs."""

    def __init__(
        self,
        *,
        disk_id: builtins.str = ...,
        image_id: builtins.str = ...,
        snapshot_id: builtins.str = ...,
        product_ids: global___ProductIDs | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["boot_source", b"boot_source", "disk_id", b"disk_id", "image_id", b"image_id", "product_ids", b"product_ids", "snapshot_id", b"snapshot_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["boot_source", b"boot_source", "disk_id", b"disk_id", "image_id", b"image_id", "product_ids", b"product_ids", "snapshot_id", b"snapshot_id"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["boot_source", b"boot_source"]) -> typing.Literal["disk_id", "image_id", "snapshot_id", "product_ids"] | None: ...

global___BootDiskSpec = BootDiskSpec

@typing.final
class ReservedInstancePool(google.protobuf.message.Message):
    """A Reserved Instance Pool resource."""

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

    ID_FIELD_NUMBER: builtins.int
    ZONE_ID_FIELD_NUMBER: builtins.int
    CLOUD_ID_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    PLATFORM_ID_FIELD_NUMBER: builtins.int
    RESOURCES_SPEC_FIELD_NUMBER: builtins.int
    GPU_SETTINGS_FIELD_NUMBER: builtins.int
    PRODUCT_IDS_FIELD_NUMBER: builtins.int
    NETWORK_SETTINGS_FIELD_NUMBER: builtins.int
    SIZE_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the pool."""
    zone_id: builtins.str
    """ID of the availability zone where the pool resides."""
    cloud_id: builtins.str
    """ID of the cloud that the pool belongs to."""
    folder_id: builtins.str
    """ID of the folder that the pool belongs to."""
    name: builtins.str
    """Name of the pool. 1-63 characters long."""
    description: builtins.str
    """Description of the pool. 0-256 characters long."""
    platform_id: builtins.str
    """ID of the hardware platform configuration for pool instances."""
    size: builtins.int
    """Desired size of the pool (number of slots for instances in this pool)."""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `key:value` pairs. Maximum of 64 per resource."""

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def resources_spec(self) -> yandex.cloud.compute.v1.instance_service_pb2.ResourcesSpec:
        """Computing resources of pool instances, such as the amount of memory and number of cores."""

    @property
    def gpu_settings(self) -> yandex.cloud.compute.v1.instance_pb2.GpuSettings:
        """GPU settings."""

    @property
    def product_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """License IDs that indicate which licenses are attached to resource.
        License IDs are used to calculate additional charges for the use of the virtual machine.
        """

    @property
    def network_settings(self) -> yandex.cloud.compute.v1.instance_pb2.NetworkSettings:
        """Network Settings."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        zone_id: builtins.str = ...,
        cloud_id: builtins.str = ...,
        folder_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        platform_id: builtins.str = ...,
        resources_spec: yandex.cloud.compute.v1.instance_service_pb2.ResourcesSpec | None = ...,
        gpu_settings: yandex.cloud.compute.v1.instance_pb2.GpuSettings | None = ...,
        product_ids: collections.abc.Iterable[builtins.str] | None = ...,
        network_settings: yandex.cloud.compute.v1.instance_pb2.NetworkSettings | None = ...,
        size: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at", "gpu_settings", b"gpu_settings", "network_settings", b"network_settings", "resources_spec", b"resources_spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cloud_id", b"cloud_id", "created_at", b"created_at", "description", b"description", "folder_id", b"folder_id", "gpu_settings", b"gpu_settings", "id", b"id", "labels", b"labels", "name", b"name", "network_settings", b"network_settings", "platform_id", b"platform_id", "product_ids", b"product_ids", "resources_spec", b"resources_spec", "size", b"size", "zone_id", b"zone_id"]) -> None: ...

global___ReservedInstancePool = ReservedInstancePool
