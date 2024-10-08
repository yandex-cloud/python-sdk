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
import yandex.cloud.compute.v1.hardware_generation_pb2
import yandex.cloud.compute.v1.snapshot_pb2
import yandex.cloud.operation.operation_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetSnapshotRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SNAPSHOT_ID_FIELD_NUMBER: builtins.int
    snapshot_id: builtins.str
    """ID of the Snapshot resource to return.
    To get the snapshot ID, use a [SnapshotService.List] request.
    """
    def __init__(
        self,
        *,
        snapshot_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["snapshot_id", b"snapshot_id"]) -> None: ...

global___GetSnapshotRequest = GetSnapshotRequest

@typing.final
class ListSnapshotsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    ORDER_BY_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to list snapshots in.
    To get the folder ID, use a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListSnapshotsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token] to the
    [ListSnapshotsResponse.next_page_token] returned by a previous list request.
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

global___ListSnapshotsRequest = ListSnapshotsRequest

@typing.final
class ListSnapshotsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SNAPSHOTS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListSnapshotsRequest.page_size], use
    the [next_page_token] as the value
    for the [ListSnapshotsRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    [next_page_token] to continue paging through the results.
    """
    @property
    def snapshots(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.compute.v1.snapshot_pb2.Snapshot]:
        """List of snapshots."""

    def __init__(
        self,
        *,
        snapshots: collections.abc.Iterable[yandex.cloud.compute.v1.snapshot_pb2.Snapshot] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "snapshots", b"snapshots"]) -> None: ...

global___ListSnapshotsResponse = ListSnapshotsResponse

@typing.final
class CreateSnapshotRequest(google.protobuf.message.Message):
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
    DISK_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    HARDWARE_GENERATION_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to create a snapshot in.
    To get the folder ID use a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    disk_id: builtins.str
    """ID of the disk to create the snapshot from.
    To get the disk ID use a [yandex.cloud.compute.v1.DiskService.List] request.
    """
    name: builtins.str
    """Name of the snapshot."""
    description: builtins.str
    """Description of the snapshot."""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `key:value` pairs."""

    @property
    def hardware_generation(self) -> yandex.cloud.compute.v1.hardware_generation_pb2.HardwareGeneration:
        """Specify the overrides to hardware_generation of a source disk, image or snapshot,
        or to the default values if the source does not define it.
        """

    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        disk_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        hardware_generation: yandex.cloud.compute.v1.hardware_generation_pb2.HardwareGeneration | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["hardware_generation", b"hardware_generation"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "disk_id", b"disk_id", "folder_id", b"folder_id", "hardware_generation", b"hardware_generation", "labels", b"labels", "name", b"name"]) -> None: ...

global___CreateSnapshotRequest = CreateSnapshotRequest

@typing.final
class CreateSnapshotMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SNAPSHOT_ID_FIELD_NUMBER: builtins.int
    DISK_ID_FIELD_NUMBER: builtins.int
    snapshot_id: builtins.str
    """ID of the snapshot that is being created."""
    disk_id: builtins.str
    """ID of the source disk used to create this snapshot."""
    def __init__(
        self,
        *,
        snapshot_id: builtins.str = ...,
        disk_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["disk_id", b"disk_id", "snapshot_id", b"snapshot_id"]) -> None: ...

global___CreateSnapshotMetadata = CreateSnapshotMetadata

@typing.final
class UpdateSnapshotRequest(google.protobuf.message.Message):
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

    SNAPSHOT_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    snapshot_id: builtins.str
    """ID of the Snapshot resource to update.
    To get the snapshot ID use a [SnapshotService.List] request.
    """
    name: builtins.str
    """Name of the snapshot."""
    description: builtins.str
    """Description of the snapshot."""
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which fields of the Snapshot resource are going to be updated."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `key:value` pairs.

        Existing set of `labels` is completely replaced by the provided set.
        """

    def __init__(
        self,
        *,
        snapshot_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "labels", b"labels", "name", b"name", "snapshot_id", b"snapshot_id", "update_mask", b"update_mask"]) -> None: ...

global___UpdateSnapshotRequest = UpdateSnapshotRequest

@typing.final
class UpdateSnapshotMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SNAPSHOT_ID_FIELD_NUMBER: builtins.int
    snapshot_id: builtins.str
    """ID of the Snapshot resource that is being updated."""
    def __init__(
        self,
        *,
        snapshot_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["snapshot_id", b"snapshot_id"]) -> None: ...

global___UpdateSnapshotMetadata = UpdateSnapshotMetadata

@typing.final
class DeleteSnapshotRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SNAPSHOT_ID_FIELD_NUMBER: builtins.int
    snapshot_id: builtins.str
    """ID of the snapshot to delete.
    To get the snapshot ID, use a [SnapshotService.List] request.
    """
    def __init__(
        self,
        *,
        snapshot_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["snapshot_id", b"snapshot_id"]) -> None: ...

global___DeleteSnapshotRequest = DeleteSnapshotRequest

@typing.final
class DeleteSnapshotMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SNAPSHOT_ID_FIELD_NUMBER: builtins.int
    snapshot_id: builtins.str
    """ID of the snapshot that is being deleted."""
    def __init__(
        self,
        *,
        snapshot_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["snapshot_id", b"snapshot_id"]) -> None: ...

global___DeleteSnapshotMetadata = DeleteSnapshotMetadata

@typing.final
class ListSnapshotOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SNAPSHOT_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    snapshot_id: builtins.str
    """ID of the Snapshot resource to list operations for."""
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size], the service returns a [ListSnapshotOperationsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token] to the
    [ListSnapshotOperationsResponse.next_page_token] returned by a previous list request.
    """
    def __init__(
        self,
        *,
        snapshot_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["page_size", b"page_size", "page_token", b"page_token", "snapshot_id", b"snapshot_id"]) -> None: ...

global___ListSnapshotOperationsRequest = ListSnapshotOperationsRequest

@typing.final
class ListSnapshotOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListSnapshotOperationsRequest.page_size], use the [next_page_token] as the value
    for the [ListSnapshotOperationsRequest.page_token] query parameter in the next list request.
    Each subsequent list request will have its own [next_page_token] to continue paging through the results.
    """
    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.operation.operation_pb2.Operation]:
        """List of operations for the specified snapshot."""

    def __init__(
        self,
        *,
        operations: collections.abc.Iterable[yandex.cloud.operation.operation_pb2.Operation] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "operations", b"operations"]) -> None: ...

global___ListSnapshotOperationsResponse = ListSnapshotOperationsResponse
