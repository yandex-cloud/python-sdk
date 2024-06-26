"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _SymmetricAlgorithm:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _SymmetricAlgorithmEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_SymmetricAlgorithm.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    SYMMETRIC_ALGORITHM_UNSPECIFIED: _SymmetricAlgorithm.ValueType  # 0
    AES_128: _SymmetricAlgorithm.ValueType  # 1
    """AES algorithm with 128-bit keys."""
    AES_192: _SymmetricAlgorithm.ValueType  # 2
    """AES algorithm with 192-bit keys."""
    AES_256: _SymmetricAlgorithm.ValueType  # 3
    """AES algorithm with 256-bit keys."""
    AES_256_HSM: _SymmetricAlgorithm.ValueType  # 4
    """AES algorithm with 256-bit keys hosted by HSM"""

class SymmetricAlgorithm(_SymmetricAlgorithm, metaclass=_SymmetricAlgorithmEnumTypeWrapper):
    """Supported symmetric encryption algorithms."""

SYMMETRIC_ALGORITHM_UNSPECIFIED: SymmetricAlgorithm.ValueType  # 0
AES_128: SymmetricAlgorithm.ValueType  # 1
"""AES algorithm with 128-bit keys."""
AES_192: SymmetricAlgorithm.ValueType  # 2
"""AES algorithm with 192-bit keys."""
AES_256: SymmetricAlgorithm.ValueType  # 3
"""AES algorithm with 256-bit keys."""
AES_256_HSM: SymmetricAlgorithm.ValueType  # 4
"""AES algorithm with 256-bit keys hosted by HSM"""
global___SymmetricAlgorithm = SymmetricAlgorithm

@typing.final
class SymmetricKey(google.protobuf.message.Message):
    """A symmetric KMS key that may contain several versions of the cryptographic material."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[SymmetricKey._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: SymmetricKey._Status.ValueType  # 0
        CREATING: SymmetricKey._Status.ValueType  # 1
        """The key is being created."""
        ACTIVE: SymmetricKey._Status.ValueType  # 2
        """The key is active and can be used for encryption and decryption.
        Can be set to INACTIVE using the [SymmetricKeyService.Update] method.
        """
        INACTIVE: SymmetricKey._Status.ValueType  # 3
        """The key is inactive and unusable.
        Can be set to ACTIVE using the [SymmetricKeyService.Update] method.
        """

    class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...
    STATUS_UNSPECIFIED: SymmetricKey.Status.ValueType  # 0
    CREATING: SymmetricKey.Status.ValueType  # 1
    """The key is being created."""
    ACTIVE: SymmetricKey.Status.ValueType  # 2
    """The key is active and can be used for encryption and decryption.
    Can be set to INACTIVE using the [SymmetricKeyService.Update] method.
    """
    INACTIVE: SymmetricKey.Status.ValueType  # 3
    """The key is inactive and unusable.
    Can be set to ACTIVE using the [SymmetricKeyService.Update] method.
    """

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
    FOLDER_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    PRIMARY_VERSION_FIELD_NUMBER: builtins.int
    DEFAULT_ALGORITHM_FIELD_NUMBER: builtins.int
    ROTATED_AT_FIELD_NUMBER: builtins.int
    ROTATION_PERIOD_FIELD_NUMBER: builtins.int
    DELETION_PROTECTION_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the key."""
    folder_id: builtins.str
    """ID of the folder that the key belongs to."""
    name: builtins.str
    """Name of the key."""
    description: builtins.str
    """Description of the key."""
    status: global___SymmetricKey.Status.ValueType
    """Current status of the key."""
    default_algorithm: global___SymmetricAlgorithm.ValueType
    """Default encryption algorithm to be used with new versions of the key."""
    deletion_protection: builtins.bool
    """Flag that inhibits deletion of the key"""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time when the key was created."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Custom labels for the key as `key:value` pairs. Maximum 64 per key."""

    @property
    def primary_version(self) -> global___SymmetricKeyVersion:
        """Primary version of the key, used as the default for all encrypt/decrypt operations,
        when no version ID is specified.
        """

    @property
    def rotated_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time of the last key rotation (time when the last version was created).
        Empty if the key does not have versions yet.
        """

    @property
    def rotation_period(self) -> google.protobuf.duration_pb2.Duration:
        """Time period between automatic key rotations."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        folder_id: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        status: global___SymmetricKey.Status.ValueType = ...,
        primary_version: global___SymmetricKeyVersion | None = ...,
        default_algorithm: global___SymmetricAlgorithm.ValueType = ...,
        rotated_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        rotation_period: google.protobuf.duration_pb2.Duration | None = ...,
        deletion_protection: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at", "primary_version", b"primary_version", "rotated_at", b"rotated_at", "rotation_period", b"rotation_period"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["created_at", b"created_at", "default_algorithm", b"default_algorithm", "deletion_protection", b"deletion_protection", "description", b"description", "folder_id", b"folder_id", "id", b"id", "labels", b"labels", "name", b"name", "primary_version", b"primary_version", "rotated_at", b"rotated_at", "rotation_period", b"rotation_period", "status", b"status"]) -> None: ...

global___SymmetricKey = SymmetricKey

@typing.final
class SymmetricKeyVersion(google.protobuf.message.Message):
    """Symmetric KMS key version: metadata about actual cryptographic data."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[SymmetricKeyVersion._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: SymmetricKeyVersion._Status.ValueType  # 0
        ACTIVE: SymmetricKeyVersion._Status.ValueType  # 1
        """The version is active and can be used for encryption and decryption."""
        SCHEDULED_FOR_DESTRUCTION: SymmetricKeyVersion._Status.ValueType  # 2
        """The version is scheduled for destruction, the time when it will be destroyed
        is specified in the [SymmetricKeyVersion.destroy_at] field.
        """
        DESTROYED: SymmetricKeyVersion._Status.ValueType  # 3
        """The version is destroyed and cannot be recovered."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper):
        """Possible version status."""

    STATUS_UNSPECIFIED: SymmetricKeyVersion.Status.ValueType  # 0
    ACTIVE: SymmetricKeyVersion.Status.ValueType  # 1
    """The version is active and can be used for encryption and decryption."""
    SCHEDULED_FOR_DESTRUCTION: SymmetricKeyVersion.Status.ValueType  # 2
    """The version is scheduled for destruction, the time when it will be destroyed
    is specified in the [SymmetricKeyVersion.destroy_at] field.
    """
    DESTROYED: SymmetricKeyVersion.Status.ValueType  # 3
    """The version is destroyed and cannot be recovered."""

    ID_FIELD_NUMBER: builtins.int
    KEY_ID_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    ALGORITHM_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    PRIMARY_FIELD_NUMBER: builtins.int
    DESTROY_AT_FIELD_NUMBER: builtins.int
    HOSTED_BY_HSM_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the key version."""
    key_id: builtins.str
    """ID of the symmetric KMS key that the version belongs to."""
    status: global___SymmetricKeyVersion.Status.ValueType
    """Status of the key version."""
    algorithm: global___SymmetricAlgorithm.ValueType
    """Encryption algorithm that should be used when using the key version to encrypt plaintext."""
    primary: builtins.bool
    """Indication of a primary version, that is to be used by default for all cryptographic
    operations that don't have a key version explicitly specified.
    """
    hosted_by_hsm: builtins.bool
    """Indication of the version that is hosted by HSM."""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time when the key version was created."""

    @property
    def destroy_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time when the key version is going to be destroyed. Empty unless the status
        is `SCHEDULED_FOR_DESTRUCTION`.
        """

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        key_id: builtins.str = ...,
        status: global___SymmetricKeyVersion.Status.ValueType = ...,
        algorithm: global___SymmetricAlgorithm.ValueType = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        primary: builtins.bool = ...,
        destroy_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        hosted_by_hsm: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at", "destroy_at", b"destroy_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["algorithm", b"algorithm", "created_at", b"created_at", "destroy_at", b"destroy_at", "hosted_by_hsm", b"hosted_by_hsm", "id", b"id", "key_id", b"key_id", "primary", b"primary", "status", b"status"]) -> None: ...

global___SymmetricKeyVersion = SymmetricKeyVersion
