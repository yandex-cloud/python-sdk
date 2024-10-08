"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import google.protobuf.wrappers_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Secret(google.protobuf.message.Message):
    """A secret that may contain several versions of the payload."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Secret._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: Secret._Status.ValueType  # 0
        CREATING: Secret._Status.ValueType  # 1
        """The secret is being created."""
        ACTIVE: Secret._Status.ValueType  # 2
        """The secret is active and the secret payload can be accessed.

        Can be set to INACTIVE using the [SecretService.Deactivate] method.
        """
        INACTIVE: Secret._Status.ValueType  # 3
        """The secret is inactive and unusable.

        Can be set to ACTIVE using the [SecretService.Deactivate] method.
        """

    class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...
    STATUS_UNSPECIFIED: Secret.Status.ValueType  # 0
    CREATING: Secret.Status.ValueType  # 1
    """The secret is being created."""
    ACTIVE: Secret.Status.ValueType  # 2
    """The secret is active and the secret payload can be accessed.

    Can be set to INACTIVE using the [SecretService.Deactivate] method.
    """
    INACTIVE: Secret.Status.ValueType  # 3
    """The secret is inactive and unusable.

    Can be set to ACTIVE using the [SecretService.Deactivate] method.
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
    KMS_KEY_ID_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    CURRENT_VERSION_FIELD_NUMBER: builtins.int
    DELETION_PROTECTION_FIELD_NUMBER: builtins.int
    PASSWORD_PAYLOAD_SPECIFICATION_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the secret."""
    folder_id: builtins.str
    """ID of the folder that the secret belongs to."""
    name: builtins.str
    """Name of the secret."""
    description: builtins.str
    """Description of the secret."""
    kms_key_id: builtins.str
    """Optional ID of the KMS key will be used to encrypt and decrypt the secret."""
    status: global___Secret.Status.ValueType
    """Status of the secret."""
    deletion_protection: builtins.bool
    """Flag that inhibits deletion of the secret."""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Custom labels for the secret as `key:value` pairs. Maximum 64 per key."""

    @property
    def current_version(self) -> global___Version:
        """Current (i.e. the `latest`) version of the secret."""

    @property
    def password_payload_specification(self) -> global___PasswordPayloadSpecification: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        folder_id: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        kms_key_id: builtins.str = ...,
        status: global___Secret.Status.ValueType = ...,
        current_version: global___Version | None = ...,
        deletion_protection: builtins.bool = ...,
        password_payload_specification: global___PasswordPayloadSpecification | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at", "current_version", b"current_version", "password_payload_specification", b"password_payload_specification", "payload_specification", b"payload_specification"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["created_at", b"created_at", "current_version", b"current_version", "deletion_protection", b"deletion_protection", "description", b"description", "folder_id", b"folder_id", "id", b"id", "kms_key_id", b"kms_key_id", "labels", b"labels", "name", b"name", "password_payload_specification", b"password_payload_specification", "payload_specification", b"payload_specification", "status", b"status"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["payload_specification", b"payload_specification"]) -> typing.Literal["password_payload_specification"] | None: ...

global___Secret = Secret

@typing.final
class Version(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Version._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: Version._Status.ValueType  # 0
        ACTIVE: Version._Status.ValueType  # 1
        """The version is active and the secret payload can be accessed."""
        SCHEDULED_FOR_DESTRUCTION: Version._Status.ValueType  # 2
        """The version is scheduled for destruction, the time when it will be destroyed
        is specified in the [Version.destroy_at] field.
        """
        DESTROYED: Version._Status.ValueType  # 3
        """The version is destroyed and cannot be recovered."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...
    STATUS_UNSPECIFIED: Version.Status.ValueType  # 0
    ACTIVE: Version.Status.ValueType  # 1
    """The version is active and the secret payload can be accessed."""
    SCHEDULED_FOR_DESTRUCTION: Version.Status.ValueType  # 2
    """The version is scheduled for destruction, the time when it will be destroyed
    is specified in the [Version.destroy_at] field.
    """
    DESTROYED: Version.Status.ValueType  # 3
    """The version is destroyed and cannot be recovered."""

    ID_FIELD_NUMBER: builtins.int
    SECRET_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    DESTROY_AT_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    PAYLOAD_ENTRY_KEYS_FIELD_NUMBER: builtins.int
    PASSWORD_PAYLOAD_SPECIFICATION_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the version."""
    secret_id: builtins.str
    """ID of the secret that the version belongs to."""
    description: builtins.str
    """Description of the version."""
    status: global___Version.Status.ValueType
    """Status of the secret."""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time when the version was created."""

    @property
    def destroy_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time when the version is going to be destroyed. Empty unless the status
        is `SCHEDULED_FOR_DESTRUCTION`.
        """

    @property
    def payload_entry_keys(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Keys of the entries contained in the version payload."""

    @property
    def password_payload_specification(self) -> global___PasswordPayloadSpecification: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        secret_id: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        destroy_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        description: builtins.str = ...,
        status: global___Version.Status.ValueType = ...,
        payload_entry_keys: collections.abc.Iterable[builtins.str] | None = ...,
        password_payload_specification: global___PasswordPayloadSpecification | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at", "destroy_at", b"destroy_at", "password_payload_specification", b"password_payload_specification", "payload_specification", b"payload_specification"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["created_at", b"created_at", "description", b"description", "destroy_at", b"destroy_at", "id", b"id", "password_payload_specification", b"password_payload_specification", "payload_entry_keys", b"payload_entry_keys", "payload_specification", b"payload_specification", "secret_id", b"secret_id", "status", b"status"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["payload_specification", b"payload_specification"]) -> typing.Literal["password_payload_specification"] | None: ...

global___Version = Version

@typing.final
class PasswordPayloadSpecification(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PASSWORD_KEY_FIELD_NUMBER: builtins.int
    LENGTH_FIELD_NUMBER: builtins.int
    INCLUDE_UPPERCASE_FIELD_NUMBER: builtins.int
    INCLUDE_LOWERCASE_FIELD_NUMBER: builtins.int
    INCLUDE_DIGITS_FIELD_NUMBER: builtins.int
    INCLUDE_PUNCTUATION_FIELD_NUMBER: builtins.int
    INCLUDED_PUNCTUATION_FIELD_NUMBER: builtins.int
    EXCLUDED_PUNCTUATION_FIELD_NUMBER: builtins.int
    password_key: builtins.str
    """key of the entry to store generated password value"""
    length: builtins.int
    """password length; by default, a reasonable length will be decided"""
    included_punctuation: builtins.str
    """If include_punctuation is true, one of these two fields (not both) may be used optionally to customize the punctuation:
    a string of specific punctuation characters to use (at most, all the 32)
    """
    excluded_punctuation: builtins.str
    """a string of punctuation characters to exclude from the default (at most 31, it's not allowed to exclude all the 32)"""
    @property
    def include_uppercase(self) -> google.protobuf.wrappers_pb2.BoolValue:
        """whether at least one A..Z character is included in the password, true by default"""

    @property
    def include_lowercase(self) -> google.protobuf.wrappers_pb2.BoolValue:
        """whether at least one a..z character is included in the password, true by default"""

    @property
    def include_digits(self) -> google.protobuf.wrappers_pb2.BoolValue:
        """whether at least one 0..9 character is included in the password, true by default"""

    @property
    def include_punctuation(self) -> google.protobuf.wrappers_pb2.BoolValue:
        """whether at least one punctuation character is included in the password, true by default
        punctuation characters by default (there are 32): !"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~
        to customize the punctuation characters, see included_punctuation and excluded_punctuation below
        """

    def __init__(
        self,
        *,
        password_key: builtins.str = ...,
        length: builtins.int = ...,
        include_uppercase: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        include_lowercase: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        include_digits: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        include_punctuation: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        included_punctuation: builtins.str = ...,
        excluded_punctuation: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["include_digits", b"include_digits", "include_lowercase", b"include_lowercase", "include_punctuation", b"include_punctuation", "include_uppercase", b"include_uppercase"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["excluded_punctuation", b"excluded_punctuation", "include_digits", b"include_digits", "include_lowercase", b"include_lowercase", "include_punctuation", b"include_punctuation", "include_uppercase", b"include_uppercase", "included_punctuation", b"included_punctuation", "length", b"length", "password_key", b"password_key"]) -> None: ...

global___PasswordPayloadSpecification = PasswordPayloadSpecification
