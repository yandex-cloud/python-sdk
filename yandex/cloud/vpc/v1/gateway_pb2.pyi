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
class Gateway(google.protobuf.message.Message):
    """A Gateway resource. For more information, see [Gateway](/docs/vpc/concepts/gateways)."""

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
    SHARED_EGRESS_GATEWAY_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the gateway. Generated at creation time."""
    folder_id: builtins.str
    """ID of the folder that the gateway belongs to."""
    name: builtins.str
    """Name of the gateway.
    The name is unique within the folder.
    """
    description: builtins.str
    """Description of the gateway."""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `key:value` pairs."""

    @property
    def shared_egress_gateway(self) -> global___SharedEgressGateway: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        folder_id: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        shared_egress_gateway: global___SharedEgressGateway | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at", "gateway", b"gateway", "shared_egress_gateway", b"shared_egress_gateway"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["created_at", b"created_at", "description", b"description", "folder_id", b"folder_id", "gateway", b"gateway", "id", b"id", "labels", b"labels", "name", b"name", "shared_egress_gateway", b"shared_egress_gateway"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["gateway", b"gateway"]) -> typing.Literal["shared_egress_gateway"] | None: ...

global___Gateway = Gateway

@typing.final
class SharedEgressGateway(google.protobuf.message.Message):
    """Shared Egress Gateway configuration"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___SharedEgressGateway = SharedEgressGateway
