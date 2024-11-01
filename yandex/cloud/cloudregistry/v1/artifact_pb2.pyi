"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
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

@typing.final
class Artifact(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Kind:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _KindEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Artifact._Kind.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        KIND_UNSPECIFIED: Artifact._Kind.ValueType  # 0
        FOLDER: Artifact._Kind.ValueType  # 1
        """Artifact kind is folder."""
        PACKAGE: Artifact._Kind.ValueType  # 2
        """Artifact kind is package."""
        ARTIFACT: Artifact._Kind.ValueType  # 3
        """Artifact kind is artifact."""

    class Kind(_Kind, metaclass=_KindEnumTypeWrapper): ...
    KIND_UNSPECIFIED: Artifact.Kind.ValueType  # 0
    FOLDER: Artifact.Kind.ValueType  # 1
    """Artifact kind is folder."""
    PACKAGE: Artifact.Kind.ValueType  # 2
    """Artifact kind is package."""
    ARTIFACT: Artifact.Kind.ValueType  # 3
    """Artifact kind is artifact."""

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Artifact._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: Artifact._Status.ValueType  # 0
        CREATING: Artifact._Status.ValueType  # 1
        """Artifact status is being created."""
        ACTIVE: Artifact._Status.ValueType  # 2
        """Artifact status is ready to use."""
        DELETING: Artifact._Status.ValueType  # 3
        """Artifact status is being deleted."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...
    STATUS_UNSPECIFIED: Artifact.Status.ValueType  # 0
    CREATING: Artifact.Status.ValueType  # 1
    """Artifact status is being created."""
    ACTIVE: Artifact.Status.ValueType  # 2
    """Artifact status is ready to use."""
    DELETING: Artifact.Status.ValueType  # 3
    """Artifact status is being deleted."""

    ID_FIELD_NUMBER: builtins.int
    PATH_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    KIND_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    MODIFIED_AT_FIELD_NUMBER: builtins.int
    id: builtins.str
    """Output only. ID of the artifact."""
    path: builtins.str
    """Path where the artifact is located."""
    name: builtins.str
    """Name of the artifact."""
    kind: global___Artifact.Kind.ValueType
    """Kind of the artifact."""
    status: global___Artifact.Status.ValueType
    """Output only. Status of the artifact."""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format."""

    @property
    def modified_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. Modification timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        path: builtins.str = ...,
        name: builtins.str = ...,
        kind: global___Artifact.Kind.ValueType = ...,
        status: global___Artifact.Status.ValueType = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        modified_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at", "modified_at", b"modified_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["created_at", b"created_at", "id", b"id", "kind", b"kind", "modified_at", b"modified_at", "name", b"name", "path", b"path", "status", b"status"]) -> None: ...

global___Artifact = Artifact