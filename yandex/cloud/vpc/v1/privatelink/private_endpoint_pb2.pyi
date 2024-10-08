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
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class PrivateEndpoint(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[PrivateEndpoint._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: PrivateEndpoint._Status.ValueType  # 0
        PENDING: PrivateEndpoint._Status.ValueType  # 1
        """Private endpoint is still creating / updating."""
        AVAILABLE: PrivateEndpoint._Status.ValueType  # 2
        """Private endpoint is available."""
        DELETING: PrivateEndpoint._Status.ValueType  # 3
        """Private endpoint is deleting."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper):
        """Status of the private endpoint."""

    STATUS_UNSPECIFIED: PrivateEndpoint.Status.ValueType  # 0
    PENDING: PrivateEndpoint.Status.ValueType  # 1
    """Private endpoint is still creating / updating."""
    AVAILABLE: PrivateEndpoint.Status.ValueType  # 2
    """Private endpoint is available."""
    DELETING: PrivateEndpoint.Status.ValueType  # 3
    """Private endpoint is deleting."""

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

    @typing.final
    class ObjectStorage(google.protobuf.message.Message):
        """Yandex Cloud Object Storage."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        def __init__(
            self,
        ) -> None: ...

    @typing.final
    class DnsOptions(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        PRIVATE_DNS_RECORDS_ENABLED_FIELD_NUMBER: builtins.int
        private_dns_records_enabled: builtins.bool
        """If enabled - vpc will create private dns records for specified service."""
        def __init__(
            self,
            *,
            private_dns_records_enabled: builtins.bool = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["private_dns_records_enabled", b"private_dns_records_enabled"]) -> None: ...

    @typing.final
    class EndpointAddress(google.protobuf.message.Message):
        """Private endpoint ip address details."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        SUBNET_ID_FIELD_NUMBER: builtins.int
        ADDRESS_FIELD_NUMBER: builtins.int
        ADDRESS_ID_FIELD_NUMBER: builtins.int
        subnet_id: builtins.str
        """ID of the subnet that the private endpoint address belongs to."""
        address: builtins.str
        """IP address of the private endpoint."""
        address_id: builtins.str
        """ID of the private endpoint address."""
        def __init__(
            self,
            *,
            subnet_id: builtins.str = ...,
            address: builtins.str = ...,
            address_id: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["address", b"address", "address_id", b"address_id", "subnet_id", b"subnet_id"]) -> None: ...

    ID_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    NETWORK_ID_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    ADDRESS_FIELD_NUMBER: builtins.int
    DNS_OPTIONS_FIELD_NUMBER: builtins.int
    OBJECT_STORAGE_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the private endpoint. Generated at creation time."""
    folder_id: builtins.str
    """ID of the folder that the private endpoint belongs to."""
    name: builtins.str
    """Name of the private endpoint.
    The name is unique within the folder.
    Value must match the regular expression
    ``\\|[a-zA-Z]([-_a-zA-Z0-9]{0,61}[a-zA-Z0-9])?``.
    """
    description: builtins.str
    """Description of the private endpoint. 0-256 characters long."""
    network_id: builtins.str
    """ID of the network that the private endpoint belongs to."""
    status: global___PrivateEndpoint.Status.ValueType
    """Status of the private endpoint."""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Private endpoint labels as `key:value` pairs.
        No more than 64 per resource.
        The maximum string length in characters for each value is 63.
        Each value must match the regular expression `[-_0-9a-z]*`.
        The string length in characters for each key must be 1-63.
        Each key must match the regular expression `[a-z][-_0-9a-z]*`.
        """

    @property
    def address(self) -> global___PrivateEndpoint.EndpointAddress:
        """Private endpoint ip address details."""

    @property
    def dns_options(self) -> global___PrivateEndpoint.DnsOptions:
        """Private endpoint dns options."""

    @property
    def object_storage(self) -> global___PrivateEndpoint.ObjectStorage:
        """Yandex Cloud Object Storage."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        folder_id: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        network_id: builtins.str = ...,
        status: global___PrivateEndpoint.Status.ValueType = ...,
        address: global___PrivateEndpoint.EndpointAddress | None = ...,
        dns_options: global___PrivateEndpoint.DnsOptions | None = ...,
        object_storage: global___PrivateEndpoint.ObjectStorage | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["address", b"address", "created_at", b"created_at", "dns_options", b"dns_options", "object_storage", b"object_storage", "service", b"service"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["address", b"address", "created_at", b"created_at", "description", b"description", "dns_options", b"dns_options", "folder_id", b"folder_id", "id", b"id", "labels", b"labels", "name", b"name", "network_id", b"network_id", "object_storage", b"object_storage", "service", b"service", "status", b"status"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["service", b"service"]) -> typing.Literal["object_storage"] | None: ...

global___PrivateEndpoint = PrivateEndpoint
