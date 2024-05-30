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
class RouteTable(google.protobuf.message.Message):
    """A RouteTable resource. For more information, see [Static Routes](/docs/vpc/concepts/static-routes)."""

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
    FOLDER_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    NETWORK_ID_FIELD_NUMBER: builtins.int
    STATIC_ROUTES_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the route table."""
    folder_id: builtins.str
    """ID of the folder that the route table belongs to."""
    name: builtins.str
    """Name of the route table. The name is unique within the project. 3-63 characters long."""
    description: builtins.str
    """Optional description of the route table. 0-256 characters long."""
    network_id: builtins.str
    """ID of the network the route table belongs to."""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `` key:value `` pairs. Maximum of 64 per resource."""

    @property
    def static_routes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StaticRoute]:
        """List of static routes."""

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
        static_routes: collections.abc.Iterable[global___StaticRoute] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["created_at", b"created_at", "description", b"description", "folder_id", b"folder_id", "id", b"id", "labels", b"labels", "name", b"name", "network_id", b"network_id", "static_routes", b"static_routes"]) -> None: ...

global___RouteTable = RouteTable

@typing.final
class StaticRoute(google.protobuf.message.Message):
    """A StaticRoute resource. For more information, see [Static Routes](/docs/vpc/concepts/static-routes)."""

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

    DESTINATION_PREFIX_FIELD_NUMBER: builtins.int
    NEXT_HOP_ADDRESS_FIELD_NUMBER: builtins.int
    GATEWAY_ID_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    destination_prefix: builtins.str
    """Destination subnet in CIDR notation"""
    next_hop_address: builtins.str
    """Next hop IP address"""
    gateway_id: builtins.str
    """Next hop gateway id"""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `` key:value `` pairs. Maximum of 64 per resource."""

    def __init__(
        self,
        *,
        destination_prefix: builtins.str = ...,
        next_hop_address: builtins.str = ...,
        gateway_id: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["destination", b"destination", "destination_prefix", b"destination_prefix", "gateway_id", b"gateway_id", "next_hop", b"next_hop", "next_hop_address", b"next_hop_address"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["destination", b"destination", "destination_prefix", b"destination_prefix", "gateway_id", b"gateway_id", "labels", b"labels", "next_hop", b"next_hop", "next_hop_address", b"next_hop_address"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["destination", b"destination"]) -> typing.Literal["destination_prefix"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["next_hop", b"next_hop"]) -> typing.Literal["next_hop_address", "gateway_id"] | None: ...

global___StaticRoute = StaticRoute
