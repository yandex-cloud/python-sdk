"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing
import yandex.cloud.mdb.greenplum.v1.config_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Host(google.protobuf.message.Message):
    """A Greenplum® cluster host resource."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Type:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Host._Type.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        TYPE_UNSPECIFIED: Host._Type.ValueType  # 0
        """Host type is not specified. Default value."""
        MASTER: Host._Type.ValueType  # 1
        """A Greenplum® master host."""
        REPLICA: Host._Type.ValueType  # 2
        """A Greenplum® master replica host."""
        SEGMENT: Host._Type.ValueType  # 3
        """A Greenplum® segment host."""

    class Type(_Type, metaclass=_TypeEnumTypeWrapper): ...
    TYPE_UNSPECIFIED: Host.Type.ValueType  # 0
    """Host type is not specified. Default value."""
    MASTER: Host.Type.ValueType  # 1
    """A Greenplum® master host."""
    REPLICA: Host.Type.ValueType  # 2
    """A Greenplum® master replica host."""
    SEGMENT: Host.Type.ValueType  # 3
    """A Greenplum® segment host."""

    class _Health:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _HealthEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Host._Health.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN: Host._Health.ValueType  # 0
        """Health of the host is unknown. Default value."""
        ALIVE: Host._Health.ValueType  # 1
        """The host is performing all its functions normally."""
        DEAD: Host._Health.ValueType  # 2
        """The host is inoperable and cannot perform any of its essential functions."""
        DEGRADED: Host._Health.ValueType  # 3
        """The host is working below capacity or not fully functional."""
        UNBALANCED: Host._Health.ValueType  # 4
        """One or more segments are not in the preferred role."""

    class Health(_Health, metaclass=_HealthEnumTypeWrapper): ...
    UNKNOWN: Host.Health.ValueType  # 0
    """Health of the host is unknown. Default value."""
    ALIVE: Host.Health.ValueType  # 1
    """The host is performing all its functions normally."""
    DEAD: Host.Health.ValueType  # 2
    """The host is inoperable and cannot perform any of its essential functions."""
    DEGRADED: Host.Health.ValueType  # 3
    """The host is working below capacity or not fully functional."""
    UNBALANCED: Host.Health.ValueType  # 4
    """One or more segments are not in the preferred role."""

    NAME_FIELD_NUMBER: builtins.int
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    ZONE_ID_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    RESOURCES_FIELD_NUMBER: builtins.int
    HEALTH_FIELD_NUMBER: builtins.int
    SUBNET_ID_FIELD_NUMBER: builtins.int
    ASSIGN_PUBLIC_IP_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the Greenplum® host.

    The host name is assigned by the platform at creation time and cannot be changed.

    The name is unique across all MDB hosts that exist on the platform, as it defines the FQDN of the host.
    """
    cluster_id: builtins.str
    """ID of the Greenplum® cluster. The ID is assigned by the platform at creation time."""
    zone_id: builtins.str
    """ID of the availability zone the Greenplum® host belongs to."""
    type: global___Host.Type.ValueType
    """Type of the host. If the field has default value, it is not returned in the response."""
    health: global___Host.Health.ValueType
    """Aggregated health of the host. If the field has default value, it is not returned in the response."""
    subnet_id: builtins.str
    """ID of the subnet that the host belongs to."""
    assign_public_ip: builtins.bool
    """Determines whether a public IP is assigned to the host."""
    @property
    def resources(self) -> yandex.cloud.mdb.greenplum.v1.config_pb2.Resources:
        """Resources allocated to the Greenplum® host."""

    def __init__(
        self,
        *,
        name: builtins.str = ...,
        cluster_id: builtins.str = ...,
        zone_id: builtins.str = ...,
        type: global___Host.Type.ValueType = ...,
        resources: yandex.cloud.mdb.greenplum.v1.config_pb2.Resources | None = ...,
        health: global___Host.Health.ValueType = ...,
        subnet_id: builtins.str = ...,
        assign_public_ip: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["resources", b"resources"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["assign_public_ip", b"assign_public_ip", "cluster_id", b"cluster_id", "health", b"health", "name", b"name", "resources", b"resources", "subnet_id", b"subnet_id", "type", b"type", "zone_id", b"zone_id"]) -> None: ...

global___Host = Host
