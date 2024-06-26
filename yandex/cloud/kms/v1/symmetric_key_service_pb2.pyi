"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import yandex.cloud.kms.v1.symmetric_key_pb2
import yandex.cloud.operation.operation_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class CreateSymmetricKeyRequest(google.protobuf.message.Message):
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
    DEFAULT_ALGORITHM_FIELD_NUMBER: builtins.int
    ROTATION_PERIOD_FIELD_NUMBER: builtins.int
    DELETION_PROTECTION_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to create a symmetric KMS key in."""
    name: builtins.str
    """Name of the key."""
    description: builtins.str
    """Description of the key."""
    default_algorithm: yandex.cloud.kms.v1.symmetric_key_pb2.SymmetricAlgorithm.ValueType
    """Encryption algorithm to be used with a new key version, generated with the next rotation."""
    deletion_protection: builtins.bool
    """Flag that inhibits deletion of the symmetric KMS key"""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Custom labels for the symmetric KMS key as `key:value` pairs. Maximum 64 per key.
        For example, `"project": "mvp"` or `"source": "dictionary"`.
        """

    @property
    def rotation_period(self) -> google.protobuf.duration_pb2.Duration:
        """Interval between automatic rotations. To disable automatic rotation, don't include
        this field in the creation request.
        """

    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        default_algorithm: yandex.cloud.kms.v1.symmetric_key_pb2.SymmetricAlgorithm.ValueType = ...,
        rotation_period: google.protobuf.duration_pb2.Duration | None = ...,
        deletion_protection: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["rotation_period", b"rotation_period"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["default_algorithm", b"default_algorithm", "deletion_protection", b"deletion_protection", "description", b"description", "folder_id", b"folder_id", "labels", b"labels", "name", b"name", "rotation_period", b"rotation_period"]) -> None: ...

global___CreateSymmetricKeyRequest = CreateSymmetricKeyRequest

@typing.final
class CreateSymmetricKeyMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_ID_FIELD_NUMBER: builtins.int
    PRIMARY_VERSION_ID_FIELD_NUMBER: builtins.int
    key_id: builtins.str
    """ID of the key being created."""
    primary_version_id: builtins.str
    """ID of the primary version of the key being created."""
    def __init__(
        self,
        *,
        key_id: builtins.str = ...,
        primary_version_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["key_id", b"key_id", "primary_version_id", b"primary_version_id"]) -> None: ...

global___CreateSymmetricKeyMetadata = CreateSymmetricKeyMetadata

@typing.final
class GetSymmetricKeyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_ID_FIELD_NUMBER: builtins.int
    key_id: builtins.str
    """ID of the symmetric KMS key to return.
    To get the ID of a symmetric KMS key use a [SymmetricKeyService.List] request.
    """
    def __init__(
        self,
        *,
        key_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["key_id", b"key_id"]) -> None: ...

global___GetSymmetricKeyRequest = GetSymmetricKeyRequest

@typing.final
class ListSymmetricKeysRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to list symmetric KMS keys in."""
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size], the service returns a [ListSymmetricKeysResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token] to the
    [ListSymmetricKeysResponse.next_page_token] returned by a previous list request.
    """
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["folder_id", b"folder_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListSymmetricKeysRequest = ListSymmetricKeysRequest

@typing.final
class ListSymmetricKeysResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEYS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number
    of results is greater than the specified [ListSymmetricKeysRequest.page_size], use
    the [next_page_token] as the value for the [ListSymmetricKeysRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    [next_page_token] to continue paging through the results.
    """
    @property
    def keys(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.kms.v1.symmetric_key_pb2.SymmetricKey]:
        """List of symmetric KMS keys in the specified folder."""

    def __init__(
        self,
        *,
        keys: collections.abc.Iterable[yandex.cloud.kms.v1.symmetric_key_pb2.SymmetricKey] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["keys", b"keys", "next_page_token", b"next_page_token"]) -> None: ...

global___ListSymmetricKeysResponse = ListSymmetricKeysResponse

@typing.final
class ListSymmetricKeyVersionsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    key_id: builtins.str
    """ID of the symmetric KMS key to list versions for."""
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size], the service returns a [ListSymmetricKeyVersionsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token] to the
    [ListSymmetricKeyVersionsResponse.next_page_token] returned by a previous list request.
    """
    def __init__(
        self,
        *,
        key_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["key_id", b"key_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListSymmetricKeyVersionsRequest = ListSymmetricKeyVersionsRequest

@typing.final
class ListSymmetricKeyVersionsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_VERSIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number
    of results is greater than the specified [ListSymmetricKeyVersionsRequest.page_size], use
    the [next_page_token] as the value for the [ListSymmetricKeyVersionsRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    [next_page_token] to continue paging through the results.
    """
    @property
    def key_versions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.kms.v1.symmetric_key_pb2.SymmetricKeyVersion]:
        """List of versions for the specified symmetric KMS key."""

    def __init__(
        self,
        *,
        key_versions: collections.abc.Iterable[yandex.cloud.kms.v1.symmetric_key_pb2.SymmetricKeyVersion] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["key_versions", b"key_versions", "next_page_token", b"next_page_token"]) -> None: ...

global___ListSymmetricKeyVersionsResponse = ListSymmetricKeyVersionsResponse

@typing.final
class UpdateSymmetricKeyRequest(google.protobuf.message.Message):
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

    KEY_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    DEFAULT_ALGORITHM_FIELD_NUMBER: builtins.int
    ROTATION_PERIOD_FIELD_NUMBER: builtins.int
    DELETION_PROTECTION_FIELD_NUMBER: builtins.int
    key_id: builtins.str
    """ID of the symmetric KMS key to update.
    To get the ID of a symmetric KMS key use a [SymmetricKeyService.List] request.
    """
    name: builtins.str
    """New name for the symmetric KMS key."""
    description: builtins.str
    """New description for the symmetric KMS key."""
    status: yandex.cloud.kms.v1.symmetric_key_pb2.SymmetricKey.Status.ValueType
    """New status for the symmetric KMS key.
    Using the [SymmetricKeyService.Update] method you can only set ACTIVE or INACTIVE status.
    """
    default_algorithm: yandex.cloud.kms.v1.symmetric_key_pb2.SymmetricAlgorithm.ValueType
    """Default encryption algorithm to be used with new versions of the symmetric KMS key."""
    deletion_protection: builtins.bool
    """Flag that inhibits deletion of the symmetric KMS key"""
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which attributes of the symmetric KMS key are going to be updated."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Custom labels for the symmetric KMS key as `key:value` pairs. Maximum 64 per key."""

    @property
    def rotation_period(self) -> google.protobuf.duration_pb2.Duration:
        """Time period between automatic symmetric KMS key rotations.
        period between two automatic rotations
        """

    def __init__(
        self,
        *,
        key_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        status: yandex.cloud.kms.v1.symmetric_key_pb2.SymmetricKey.Status.ValueType = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        default_algorithm: yandex.cloud.kms.v1.symmetric_key_pb2.SymmetricAlgorithm.ValueType = ...,
        rotation_period: google.protobuf.duration_pb2.Duration | None = ...,
        deletion_protection: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["rotation_period", b"rotation_period", "update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["default_algorithm", b"default_algorithm", "deletion_protection", b"deletion_protection", "description", b"description", "key_id", b"key_id", "labels", b"labels", "name", b"name", "rotation_period", b"rotation_period", "status", b"status", "update_mask", b"update_mask"]) -> None: ...

global___UpdateSymmetricKeyRequest = UpdateSymmetricKeyRequest

@typing.final
class UpdateSymmetricKeyMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_ID_FIELD_NUMBER: builtins.int
    key_id: builtins.str
    """ID of the key being updated."""
    def __init__(
        self,
        *,
        key_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["key_id", b"key_id"]) -> None: ...

global___UpdateSymmetricKeyMetadata = UpdateSymmetricKeyMetadata

@typing.final
class DeleteSymmetricKeyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_ID_FIELD_NUMBER: builtins.int
    key_id: builtins.str
    """ID of the key to be deleted."""
    def __init__(
        self,
        *,
        key_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["key_id", b"key_id"]) -> None: ...

global___DeleteSymmetricKeyRequest = DeleteSymmetricKeyRequest

@typing.final
class DeleteSymmetricKeyMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_ID_FIELD_NUMBER: builtins.int
    key_id: builtins.str
    """ID of the key being deleted."""
    def __init__(
        self,
        *,
        key_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["key_id", b"key_id"]) -> None: ...

global___DeleteSymmetricKeyMetadata = DeleteSymmetricKeyMetadata

@typing.final
class SetPrimarySymmetricKeyVersionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_ID_FIELD_NUMBER: builtins.int
    VERSION_ID_FIELD_NUMBER: builtins.int
    key_id: builtins.str
    """ID of the key to set a primary version for."""
    version_id: builtins.str
    """ID of the version that should become primary for the specified key."""
    def __init__(
        self,
        *,
        key_id: builtins.str = ...,
        version_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["key_id", b"key_id", "version_id", b"version_id"]) -> None: ...

global___SetPrimarySymmetricKeyVersionRequest = SetPrimarySymmetricKeyVersionRequest

@typing.final
class SetPrimarySymmetricKeyVersionMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_ID_FIELD_NUMBER: builtins.int
    VERSION_ID_FIELD_NUMBER: builtins.int
    key_id: builtins.str
    """ID of the key that the primary version if being changed for."""
    version_id: builtins.str
    """ID of the version that is being made primary for the key."""
    def __init__(
        self,
        *,
        key_id: builtins.str = ...,
        version_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["key_id", b"key_id", "version_id", b"version_id"]) -> None: ...

global___SetPrimarySymmetricKeyVersionMetadata = SetPrimarySymmetricKeyVersionMetadata

@typing.final
class RotateSymmetricKeyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_ID_FIELD_NUMBER: builtins.int
    key_id: builtins.str
    """ID of the key to be rotated."""
    def __init__(
        self,
        *,
        key_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["key_id", b"key_id"]) -> None: ...

global___RotateSymmetricKeyRequest = RotateSymmetricKeyRequest

@typing.final
class RotateSymmetricKeyMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_ID_FIELD_NUMBER: builtins.int
    NEW_PRIMARY_VERSION_ID_FIELD_NUMBER: builtins.int
    key_id: builtins.str
    """ID of the key being rotated."""
    new_primary_version_id: builtins.str
    """ID of the version generated as a result of key rotation."""
    def __init__(
        self,
        *,
        key_id: builtins.str = ...,
        new_primary_version_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["key_id", b"key_id", "new_primary_version_id", b"new_primary_version_id"]) -> None: ...

global___RotateSymmetricKeyMetadata = RotateSymmetricKeyMetadata

@typing.final
class ScheduleSymmetricKeyVersionDestructionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_ID_FIELD_NUMBER: builtins.int
    VERSION_ID_FIELD_NUMBER: builtins.int
    PENDING_PERIOD_FIELD_NUMBER: builtins.int
    key_id: builtins.str
    """ID of the key whose version should be scheduled for destruction."""
    version_id: builtins.str
    """ID of the version to be destroyed."""
    @property
    def pending_period(self) -> google.protobuf.duration_pb2.Duration:
        """Time interval between the version destruction request and actual destruction.
        Default value: 7 days.
        """

    def __init__(
        self,
        *,
        key_id: builtins.str = ...,
        version_id: builtins.str = ...,
        pending_period: google.protobuf.duration_pb2.Duration | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["pending_period", b"pending_period"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["key_id", b"key_id", "pending_period", b"pending_period", "version_id", b"version_id"]) -> None: ...

global___ScheduleSymmetricKeyVersionDestructionRequest = ScheduleSymmetricKeyVersionDestructionRequest

@typing.final
class ScheduleSymmetricKeyVersionDestructionMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_ID_FIELD_NUMBER: builtins.int
    VERSION_ID_FIELD_NUMBER: builtins.int
    DESTROY_AT_FIELD_NUMBER: builtins.int
    key_id: builtins.str
    """ID of the key whose version is being scheduled for destruction."""
    version_id: builtins.str
    """ID of the version that is being scheduled for destruction."""
    @property
    def destroy_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time when the version is scheduled to be destroyed."""

    def __init__(
        self,
        *,
        key_id: builtins.str = ...,
        version_id: builtins.str = ...,
        destroy_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["destroy_at", b"destroy_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["destroy_at", b"destroy_at", "key_id", b"key_id", "version_id", b"version_id"]) -> None: ...

global___ScheduleSymmetricKeyVersionDestructionMetadata = ScheduleSymmetricKeyVersionDestructionMetadata

@typing.final
class CancelSymmetricKeyVersionDestructionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_ID_FIELD_NUMBER: builtins.int
    VERSION_ID_FIELD_NUMBER: builtins.int
    key_id: builtins.str
    """ID of the key to cancel a version's destruction for."""
    version_id: builtins.str
    """ID of the version whose scheduled destruction should be cancelled."""
    def __init__(
        self,
        *,
        key_id: builtins.str = ...,
        version_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["key_id", b"key_id", "version_id", b"version_id"]) -> None: ...

global___CancelSymmetricKeyVersionDestructionRequest = CancelSymmetricKeyVersionDestructionRequest

@typing.final
class CancelSymmetricKeyVersionDestructionMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_ID_FIELD_NUMBER: builtins.int
    VERSION_ID_FIELD_NUMBER: builtins.int
    key_id: builtins.str
    """ID of the key whose version's destruction is being cancelled."""
    version_id: builtins.str
    """ID of the version whose scheduled destruction is being cancelled."""
    def __init__(
        self,
        *,
        key_id: builtins.str = ...,
        version_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["key_id", b"key_id", "version_id", b"version_id"]) -> None: ...

global___CancelSymmetricKeyVersionDestructionMetadata = CancelSymmetricKeyVersionDestructionMetadata

@typing.final
class ListSymmetricKeyOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    key_id: builtins.str
    """ID of the symmetric KMS key to get operations for.

    To get the key ID, use a [SymmetricKeyService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page that should be returned. If the number of available
    results is larger than [page_size], the service returns a [ListSymmetricKeyOperationsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token] to the
    [ListSymmetricKeyOperationsResponse.next_page_token] returned by a previous list request.
    """
    def __init__(
        self,
        *,
        key_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["key_id", b"key_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListSymmetricKeyOperationsRequest = ListSymmetricKeyOperationsRequest

@typing.final
class ListSymmetricKeyOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListSymmetricKeyOperationsRequest.page_size], use the [next_page_token] as the value
    for the [ListSymmetricKeyOperationsRequest.page_token] query parameter in the next list request.
    Each subsequent list request will have its own [next_page_token] to continue paging through the results.
    """
    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.operation.operation_pb2.Operation]:
        """List of operations for the specified key."""

    def __init__(
        self,
        *,
        operations: collections.abc.Iterable[yandex.cloud.operation.operation_pb2.Operation] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "operations", b"operations"]) -> None: ...

global___ListSymmetricKeyOperationsResponse = ListSymmetricKeyOperationsResponse
