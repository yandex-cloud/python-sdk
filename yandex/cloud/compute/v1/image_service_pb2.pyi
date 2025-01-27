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
import yandex.cloud.compute.v1.image_pb2
import yandex.cloud.operation.operation_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetImageRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IMAGE_ID_FIELD_NUMBER: builtins.int
    image_id: builtins.str
    """ID of the Image resource to return.
    To get the image ID, use a [ImageService.List] request.
    """
    def __init__(
        self,
        *,
        image_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["image_id", b"image_id"]) -> None: ...

global___GetImageRequest = GetImageRequest

@typing.final
class GetImageLatestByFamilyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    FAMILY_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to get the image from.
    To get the folder ID, use a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    family: builtins.str
    """Name of the image family to search for."""
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        family: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["family", b"family", "folder_id", b"folder_id"]) -> None: ...

global___GetImageLatestByFamilyRequest = GetImageLatestByFamilyRequest

@typing.final
class ListImagesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    ORDER_BY_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to list images in.
    To get the folder ID, use a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListImagesResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token] to the
    [ListImagesResponse.next_page_token] returned by a previous list request.
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

global___ListImagesRequest = ListImagesRequest

@typing.final
class ListImagesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IMAGES_FIELD_NUMBER: builtins.int
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
    def images(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.compute.v1.image_pb2.Image]:
        """List of images."""

    def __init__(
        self,
        *,
        images: collections.abc.Iterable[yandex.cloud.compute.v1.image_pb2.Image] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["images", b"images", "next_page_token", b"next_page_token"]) -> None: ...

global___ListImagesResponse = ListImagesResponse

@typing.final
class CreateImageRequest(google.protobuf.message.Message):
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
    FAMILY_FIELD_NUMBER: builtins.int
    MIN_DISK_SIZE_FIELD_NUMBER: builtins.int
    PRODUCT_IDS_FIELD_NUMBER: builtins.int
    IMAGE_ID_FIELD_NUMBER: builtins.int
    DISK_ID_FIELD_NUMBER: builtins.int
    SNAPSHOT_ID_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    OS_FIELD_NUMBER: builtins.int
    POOLED_FIELD_NUMBER: builtins.int
    HARDWARE_GENERATION_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to create an image in.
    To get the folder ID, use a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    name: builtins.str
    """Name of the image."""
    description: builtins.str
    """Description of the image."""
    family: builtins.str
    """The name of the image family to which this image belongs. For more information, see [Image family](/docs/compute/concepts/image#family).

    To get an information about the most recent image from a family, use a [ImageService.GetLatestByFamily] request.
    """
    min_disk_size: builtins.int
    """Minimum size of the disk that will be created from this image.
    Specified in bytes. Should be more than the volume of source data.
    optional, should be > source data
    """
    image_id: builtins.str
    """ID of the source image to create the new image from."""
    disk_id: builtins.str
    """ID of the disk to create the image from."""
    snapshot_id: builtins.str
    """ID of the snapshot to create the image from."""
    uri: builtins.str
    """URI of the source image to create the new image from.
    Currently only supports links to images that are stored in Object Storage.
    Must be a valid [pre-signed URL](/docs/storage/concepts/pre-signed-urls).
    Currently only supports Qcow2, VMDK, and RAW image formats.
    """
    pooled: builtins.bool
    """When true, an image pool will be created for fast creation disks from the image."""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `key:value` pairs."""

    @property
    def product_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """License IDs that indicate which licenses are attached to this resource.
        License IDs are used to calculate additional charges for the use of the virtual machine.

        The correct license ID is generated by the platform. IDs are inherited by new resources created from this resource.

        If you know the license IDs, specify them when you create the image.
        For example, if you create a disk image using a third-party utility and load it into Object Storage, the license IDs will be lost.
        You can specify them in this request.
        """

    @property
    def os(self) -> yandex.cloud.compute.v1.image_pb2.Os:
        """Operating system that is contained in the image.

        If not specified and you used the `image_id` or `disk_id` field to set the source, then the value can be inherited from the source resource.
        """

    @property
    def hardware_generation(self) -> yandex.cloud.compute.v1.hardware_generation_pb2.HardwareGeneration:
        """Specify the overrides to hardware_generation of a source disk, image or snapshot,
        or to the default values if the source does not define it.
        """

    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        family: builtins.str = ...,
        min_disk_size: builtins.int = ...,
        product_ids: collections.abc.Iterable[builtins.str] | None = ...,
        image_id: builtins.str = ...,
        disk_id: builtins.str = ...,
        snapshot_id: builtins.str = ...,
        uri: builtins.str = ...,
        os: yandex.cloud.compute.v1.image_pb2.Os | None = ...,
        pooled: builtins.bool = ...,
        hardware_generation: yandex.cloud.compute.v1.hardware_generation_pb2.HardwareGeneration | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["disk_id", b"disk_id", "hardware_generation", b"hardware_generation", "image_id", b"image_id", "os", b"os", "snapshot_id", b"snapshot_id", "source", b"source", "uri", b"uri"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "disk_id", b"disk_id", "family", b"family", "folder_id", b"folder_id", "hardware_generation", b"hardware_generation", "image_id", b"image_id", "labels", b"labels", "min_disk_size", b"min_disk_size", "name", b"name", "os", b"os", "pooled", b"pooled", "product_ids", b"product_ids", "snapshot_id", b"snapshot_id", "source", b"source", "uri", b"uri"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["source", b"source"]) -> typing.Literal["image_id", "disk_id", "snapshot_id", "uri"] | None: ...

global___CreateImageRequest = CreateImageRequest

@typing.final
class CreateImageMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IMAGE_ID_FIELD_NUMBER: builtins.int
    image_id: builtins.str
    """ID of the image that is being created."""
    def __init__(
        self,
        *,
        image_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["image_id", b"image_id"]) -> None: ...

global___CreateImageMetadata = CreateImageMetadata

@typing.final
class UpdateImageRequest(google.protobuf.message.Message):
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

    IMAGE_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    MIN_DISK_SIZE_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    image_id: builtins.str
    """ID of the Image resource to update.
    To get the image ID, use a [ImageService.List] request.
    """
    name: builtins.str
    """Name of the image."""
    description: builtins.str
    """Description of the image."""
    min_disk_size: builtins.int
    """Minimum size of the disk that can be created from this image.
    Specified in bytes. Should be more than the volume of source data and more than the virtual disk size.
    """
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which fields of the Image resource are going to be updated."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `key:value` pairs.

        Existing set of `labels` is completely replaced by the provided set.
        """

    def __init__(
        self,
        *,
        image_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        min_disk_size: builtins.int = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "image_id", b"image_id", "labels", b"labels", "min_disk_size", b"min_disk_size", "name", b"name", "update_mask", b"update_mask"]) -> None: ...

global___UpdateImageRequest = UpdateImageRequest

@typing.final
class UpdateImageMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IMAGE_ID_FIELD_NUMBER: builtins.int
    image_id: builtins.str
    """ID of the Image resource that is being updated."""
    def __init__(
        self,
        *,
        image_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["image_id", b"image_id"]) -> None: ...

global___UpdateImageMetadata = UpdateImageMetadata

@typing.final
class DeleteImageRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IMAGE_ID_FIELD_NUMBER: builtins.int
    image_id: builtins.str
    """ID of the image to delete.
    To get the image ID, use a [ImageService.List] request.
    """
    def __init__(
        self,
        *,
        image_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["image_id", b"image_id"]) -> None: ...

global___DeleteImageRequest = DeleteImageRequest

@typing.final
class DeleteImageMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IMAGE_ID_FIELD_NUMBER: builtins.int
    image_id: builtins.str
    """ID of the image that is being deleted."""
    def __init__(
        self,
        *,
        image_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["image_id", b"image_id"]) -> None: ...

global___DeleteImageMetadata = DeleteImageMetadata

@typing.final
class ListImageOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IMAGE_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    image_id: builtins.str
    """ID of the Image resource to list operations for."""
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size], the service returns a [ListImageOperationsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token] to the
    [ListImageOperationsResponse.next_page_token] returned by a previous list request.
    """
    def __init__(
        self,
        *,
        image_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["image_id", b"image_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListImageOperationsRequest = ListImageOperationsRequest

@typing.final
class ListImageOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListImageOperationsRequest.page_size], use the [next_page_token] as the value
    for the [ListImageOperationsRequest.page_token] query parameter in the next list request.
    Each subsequent list request will have its own [next_page_token] to continue paging through the results.
    """
    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.operation.operation_pb2.Operation]:
        """List of operations for the specified image."""

    def __init__(
        self,
        *,
        operations: collections.abc.Iterable[yandex.cloud.operation.operation_pb2.Operation] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "operations", b"operations"]) -> None: ...

global___ListImageOperationsResponse = ListImageOperationsResponse
