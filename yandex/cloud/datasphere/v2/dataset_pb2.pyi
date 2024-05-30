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

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Dataset(google.protobuf.message.Message):
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
    PROJECT_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    CREATED_BY_ID_FIELD_NUMBER: builtins.int
    CODE_FIELD_NUMBER: builtins.int
    SIZE_GB_FIELD_NUMBER: builtins.int
    ZONE_IDS_FIELD_NUMBER: builtins.int
    MOUNT_PATH_FIELD_NUMBER: builtins.int
    DATA_CAPSULE_ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the dataset."""
    project_id: builtins.str
    """ID of the project."""
    name: builtins.str
    """Name of the dataset."""
    description: builtins.str
    """Description of the dataset."""
    created_by_id: builtins.str
    """ID of the user who created the dataset."""
    code: builtins.str
    """Code used to create dataset."""
    size_gb: builtins.int
    """Size of the dataset, Gb."""
    mount_path: builtins.str
    """Dataset mount path."""
    data_capsule_id: builtins.str
    """ID of the data capsule object, storing information about dataset storage."""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time the dataset was created."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Labels of the dataset."""

    @property
    def zone_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Zone IDs where dataset is available."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        project_id: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        created_by_id: builtins.str = ...,
        code: builtins.str = ...,
        size_gb: builtins.int = ...,
        zone_ids: collections.abc.Iterable[builtins.str] | None = ...,
        mount_path: builtins.str = ...,
        data_capsule_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["code", b"code", "created_at", b"created_at", "created_by_id", b"created_by_id", "data_capsule_id", b"data_capsule_id", "description", b"description", "id", b"id", "labels", b"labels", "mount_path", b"mount_path", "name", b"name", "project_id", b"project_id", "size_gb", b"size_gb", "zone_ids", b"zone_ids"]) -> None: ...

global___Dataset = Dataset

@typing.final
class DatasetStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class StatusActive(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        def __init__(
            self,
        ) -> None: ...

    @typing.final
    class StatusInactive(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        def __init__(
            self,
        ) -> None: ...

    @typing.final
    class StatusError(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        ERROR_FIELD_NUMBER: builtins.int
        error: builtins.str
        """Text of the error."""
        def __init__(
            self,
            *,
            error: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["error", b"error"]) -> None: ...

    STATUS_ACTIVE_FIELD_NUMBER: builtins.int
    STATUS_INACTIVE_FIELD_NUMBER: builtins.int
    STATUS_ERROR_FIELD_NUMBER: builtins.int
    @property
    def status_active(self) -> global___DatasetStatus.StatusActive:
        """Dataset is activated."""

    @property
    def status_inactive(self) -> global___DatasetStatus.StatusInactive:
        """Dataset is inactive."""

    @property
    def status_error(self) -> global___DatasetStatus.StatusError:
        """Error while activating dataset."""

    def __init__(
        self,
        *,
        status_active: global___DatasetStatus.StatusActive | None = ...,
        status_inactive: global___DatasetStatus.StatusInactive | None = ...,
        status_error: global___DatasetStatus.StatusError | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["status", b"status", "status_active", b"status_active", "status_error", b"status_error", "status_inactive", b"status_inactive"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["status", b"status", "status_active", b"status_active", "status_error", b"status_error", "status_inactive", b"status_inactive"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["status", b"status"]) -> typing.Literal["status_active", "status_inactive", "status_error"] | None: ...

global___DatasetStatus = DatasetStatus
