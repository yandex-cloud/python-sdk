"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import yandex.cloud.baremetal.v1alpha.storage_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class DefaultStorage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONFIGURATION_ID_FIELD_NUMBER: builtins.int
    STORAGES_FIELD_NUMBER: builtins.int
    configuration_id: builtins.str
    """ID of the configuration.

    To get the configuration ID, use a [ConfigurationService.List] request.
    """
    @property
    def storages(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.baremetal.v1alpha.storage_pb2.Storage]:
        """List of default storages."""

    def __init__(
        self,
        *,
        configuration_id: builtins.str = ...,
        storages: collections.abc.Iterable[yandex.cloud.baremetal.v1alpha.storage_pb2.Storage] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["configuration_id", b"configuration_id", "storages", b"storages"]) -> None: ...

global___DefaultStorage = DefaultStorage

@typing.final
class GetDefaultStorageRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONFIGURATION_ID_FIELD_NUMBER: builtins.int
    configuration_id: builtins.str
    """ID of the configuration."""
    def __init__(
        self,
        *,
        configuration_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["configuration_id", b"configuration_id"]) -> None: ...

global___GetDefaultStorageRequest = GetDefaultStorageRequest

@typing.final
class BatchGetDefaultStoragesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONFIGURATION_IDS_FIELD_NUMBER: builtins.int
    @property
    def configuration_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of configuration IDs."""

    def __init__(
        self,
        *,
        configuration_ids: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["configuration_ids", b"configuration_ids"]) -> None: ...

global___BatchGetDefaultStoragesRequest = BatchGetDefaultStoragesRequest

@typing.final
class BatchGetDefaultStoragesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEFAULT_STORAGES_FIELD_NUMBER: builtins.int
    @property
    def default_storages(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DefaultStorage]:
        """List of default storages."""

    def __init__(
        self,
        *,
        default_storages: collections.abc.Iterable[global___DefaultStorage] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["default_storages", b"default_storages"]) -> None: ...

global___BatchGetDefaultStoragesResponse = BatchGetDefaultStoragesResponse
