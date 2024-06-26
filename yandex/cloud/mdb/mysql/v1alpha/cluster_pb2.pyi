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
import google.type.timeofday_pb2
import sys
import typing
import yandex.cloud.mdb.mysql.v1alpha.config.mysql5_7_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Cluster(google.protobuf.message.Message):
    """A MySQL cluster. For more information, see
    the [documentation](/docs/managed-mysql/concepts).
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Environment:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _EnvironmentEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Cluster._Environment.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        ENVIRONMENT_UNSPECIFIED: Cluster._Environment.ValueType  # 0
        PRODUCTION: Cluster._Environment.ValueType  # 1
        """Stable environment with a conservative update policy:
        only hotfixes are applied during regular maintenance.
        """
        PRESTABLE: Cluster._Environment.ValueType  # 2
        """Environment with more aggressive update policy: new versions
        are rolled out irrespective of backward compatibility.
        """

    class Environment(_Environment, metaclass=_EnvironmentEnumTypeWrapper): ...
    ENVIRONMENT_UNSPECIFIED: Cluster.Environment.ValueType  # 0
    PRODUCTION: Cluster.Environment.ValueType  # 1
    """Stable environment with a conservative update policy:
    only hotfixes are applied during regular maintenance.
    """
    PRESTABLE: Cluster.Environment.ValueType  # 2
    """Environment with more aggressive update policy: new versions
    are rolled out irrespective of backward compatibility.
    """

    class _Health:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _HealthEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Cluster._Health.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        HEALTH_UNKNOWN: Cluster._Health.ValueType  # 0
        """State of the cluster is unknown ([Host.health] for every host in the cluster is UNKNOWN)."""
        ALIVE: Cluster._Health.ValueType  # 1
        """Cluster is alive and well ([Host.health] for every host in the cluster is ALIVE)."""
        DEAD: Cluster._Health.ValueType  # 2
        """Cluster is inoperable ([Host.health] for every host in the cluster is DEAD)."""
        DEGRADED: Cluster._Health.ValueType  # 3
        """Cluster is working below capacity ([Host.health] for at least one host in the cluster is not ALIVE)."""

    class Health(_Health, metaclass=_HealthEnumTypeWrapper): ...
    HEALTH_UNKNOWN: Cluster.Health.ValueType  # 0
    """State of the cluster is unknown ([Host.health] for every host in the cluster is UNKNOWN)."""
    ALIVE: Cluster.Health.ValueType  # 1
    """Cluster is alive and well ([Host.health] for every host in the cluster is ALIVE)."""
    DEAD: Cluster.Health.ValueType  # 2
    """Cluster is inoperable ([Host.health] for every host in the cluster is DEAD)."""
    DEGRADED: Cluster.Health.ValueType  # 3
    """Cluster is working below capacity ([Host.health] for at least one host in the cluster is not ALIVE)."""

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Cluster._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNKNOWN: Cluster._Status.ValueType  # 0
        """Cluster state is unknown."""
        CREATING: Cluster._Status.ValueType  # 1
        """Cluster is being created."""
        RUNNING: Cluster._Status.ValueType  # 2
        """Cluster is running normally."""
        ERROR: Cluster._Status.ValueType  # 3
        """Cluster encountered a problem and cannot operate."""
        UPDATING: Cluster._Status.ValueType  # 4
        """Cluster is being updated."""
        STOPPING: Cluster._Status.ValueType  # 5
        """Cluster is stopping."""
        STOPPED: Cluster._Status.ValueType  # 6
        """Cluster stopped."""
        STARTING: Cluster._Status.ValueType  # 7
        """Cluster is starting."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...
    STATUS_UNKNOWN: Cluster.Status.ValueType  # 0
    """Cluster state is unknown."""
    CREATING: Cluster.Status.ValueType  # 1
    """Cluster is being created."""
    RUNNING: Cluster.Status.ValueType  # 2
    """Cluster is running normally."""
    ERROR: Cluster.Status.ValueType  # 3
    """Cluster encountered a problem and cannot operate."""
    UPDATING: Cluster.Status.ValueType  # 4
    """Cluster is being updated."""
    STOPPING: Cluster.Status.ValueType  # 5
    """Cluster is stopping."""
    STOPPED: Cluster.Status.ValueType  # 6
    """Cluster stopped."""
    STARTING: Cluster.Status.ValueType  # 7
    """Cluster is starting."""

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
    ENVIRONMENT_FIELD_NUMBER: builtins.int
    MONITORING_FIELD_NUMBER: builtins.int
    CONFIG_FIELD_NUMBER: builtins.int
    NETWORK_ID_FIELD_NUMBER: builtins.int
    HEALTH_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the MySQL cluster.
    This ID is assigned by Managed Service for MySQL at creation time.
    """
    folder_id: builtins.str
    """ID of the folder that the MySQL cluster belongs to."""
    name: builtins.str
    """Name of the MySQL cluster.
    The name must be unique within the folder, comply with RFC 1035
    and be 1-63 characters long.
    """
    description: builtins.str
    """Description of the MySQL cluster. 0-256 characters long."""
    environment: global___Cluster.Environment.ValueType
    """Deployment environment of the MySQL cluster."""
    network_id: builtins.str
    """ID of the network that the cluster belongs to."""
    health: global___Cluster.Health.ValueType
    """Aggregated cluster health."""
    status: global___Cluster.Status.ValueType
    """Current state of the cluster."""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Custom labels for the MySQL cluster as `key:value` pairs.
        Maximum 64 per resource.
        """

    @property
    def monitoring(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Monitoring]:
        """Description of monitoring systems relevant to the MySQL cluster."""

    @property
    def config(self) -> global___ClusterConfig:
        """Configuration of the MySQL cluster."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        folder_id: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        environment: global___Cluster.Environment.ValueType = ...,
        monitoring: collections.abc.Iterable[global___Monitoring] | None = ...,
        config: global___ClusterConfig | None = ...,
        network_id: builtins.str = ...,
        health: global___Cluster.Health.ValueType = ...,
        status: global___Cluster.Status.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["config", b"config", "created_at", b"created_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["config", b"config", "created_at", b"created_at", "description", b"description", "environment", b"environment", "folder_id", b"folder_id", "health", b"health", "id", b"id", "labels", b"labels", "monitoring", b"monitoring", "name", b"name", "network_id", b"network_id", "status", b"status"]) -> None: ...

global___Cluster = Cluster

@typing.final
class Monitoring(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LINK_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the monitoring system."""
    description: builtins.str
    """Description of the monitoring system."""
    link: builtins.str
    """Link to the monitoring system charts for the MySQL cluster."""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        description: builtins.str = ...,
        link: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "link", b"link", "name", b"name"]) -> None: ...

global___Monitoring = Monitoring

@typing.final
class ClusterConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VERSION_FIELD_NUMBER: builtins.int
    MYSQL_CONFIG_5_7_FIELD_NUMBER: builtins.int
    RESOURCES_FIELD_NUMBER: builtins.int
    BACKUP_WINDOW_START_FIELD_NUMBER: builtins.int
    version: builtins.str
    """Version of MySQL server software."""
    @property
    def mysql_config_5_7(self) -> yandex.cloud.mdb.mysql.v1alpha.config.mysql5_7_pb2.MysqlConfigSet5_7:
        """Configuration of a MySQL 5.7 server."""

    @property
    def resources(self) -> global___Resources:
        """Resources allocated to MySQL hosts."""

    @property
    def backup_window_start(self) -> google.type.timeofday_pb2.TimeOfDay:
        """Time to start the daily backup, in the UTC timezone."""

    def __init__(
        self,
        *,
        version: builtins.str = ...,
        mysql_config_5_7: yandex.cloud.mdb.mysql.v1alpha.config.mysql5_7_pb2.MysqlConfigSet5_7 | None = ...,
        resources: global___Resources | None = ...,
        backup_window_start: google.type.timeofday_pb2.TimeOfDay | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["backup_window_start", b"backup_window_start", "mysql_config", b"mysql_config", "mysql_config_5_7", b"mysql_config_5_7", "resources", b"resources"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["backup_window_start", b"backup_window_start", "mysql_config", b"mysql_config", "mysql_config_5_7", b"mysql_config_5_7", "resources", b"resources", "version", b"version"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["mysql_config", b"mysql_config"]) -> typing.Literal["mysql_config_5_7"] | None: ...

global___ClusterConfig = ClusterConfig

@typing.final
class Host(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Role:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _RoleEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Host._Role.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        ROLE_UNKNOWN: Host._Role.ValueType  # 0
        """Role of the host in the cluster is unknown."""
        MASTER: Host._Role.ValueType  # 1
        """Host is the master MySQL server in the cluster."""
        REPLICA: Host._Role.ValueType  # 2
        """Host is a replica MySQL server in the cluster."""

    class Role(_Role, metaclass=_RoleEnumTypeWrapper): ...
    ROLE_UNKNOWN: Host.Role.ValueType  # 0
    """Role of the host in the cluster is unknown."""
    MASTER: Host.Role.ValueType  # 1
    """Host is the master MySQL server in the cluster."""
    REPLICA: Host.Role.ValueType  # 2
    """Host is a replica MySQL server in the cluster."""

    class _Health:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _HealthEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Host._Health.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        HEALTH_UNKNOWN: Host._Health.ValueType  # 0
        """Health of the host is unknown."""
        ALIVE: Host._Health.ValueType  # 1
        """The host is performing all its functions normally."""
        DEAD: Host._Health.ValueType  # 2
        """The host is inoperable, and cannot perform any of its essential functions."""
        DEGRADED: Host._Health.ValueType  # 3
        """The host is degraded, and can perform only some of its essential functions."""

    class Health(_Health, metaclass=_HealthEnumTypeWrapper): ...
    HEALTH_UNKNOWN: Host.Health.ValueType  # 0
    """Health of the host is unknown."""
    ALIVE: Host.Health.ValueType  # 1
    """The host is performing all its functions normally."""
    DEAD: Host.Health.ValueType  # 2
    """The host is inoperable, and cannot perform any of its essential functions."""
    DEGRADED: Host.Health.ValueType  # 3
    """The host is degraded, and can perform only some of its essential functions."""

    NAME_FIELD_NUMBER: builtins.int
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    ZONE_ID_FIELD_NUMBER: builtins.int
    RESOURCES_FIELD_NUMBER: builtins.int
    ROLE_FIELD_NUMBER: builtins.int
    HEALTH_FIELD_NUMBER: builtins.int
    SERVICES_FIELD_NUMBER: builtins.int
    SUBNET_ID_FIELD_NUMBER: builtins.int
    ASSIGN_PUBLIC_IP_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the MySQL host. The host name is assigned by Managed Service for MySQL
    at creation time, and cannot be changed. 1-63 characters long.

    The name is unique across all database hosts that exist on the platform,
    as it defines the FQDN of the host.
    """
    cluster_id: builtins.str
    """ID of the MySQL host. The ID is assigned by Managed Service for MySQL
    at creation time.
    """
    zone_id: builtins.str
    """ID of the availability zone where the MySQL host resides."""
    role: global___Host.Role.ValueType
    """Role of the host in the cluster."""
    health: global___Host.Health.ValueType
    """Status code of the aggregated health of the host."""
    subnet_id: builtins.str
    """ID of the subnet that the host belongs to."""
    assign_public_ip: builtins.bool
    """Flag showing public IP assignment status to this host."""
    @property
    def resources(self) -> global___Resources:
        """Resources allocated to the host."""

    @property
    def services(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Service]:
        """Services provided by the host."""

    def __init__(
        self,
        *,
        name: builtins.str = ...,
        cluster_id: builtins.str = ...,
        zone_id: builtins.str = ...,
        resources: global___Resources | None = ...,
        role: global___Host.Role.ValueType = ...,
        health: global___Host.Health.ValueType = ...,
        services: collections.abc.Iterable[global___Service] | None = ...,
        subnet_id: builtins.str = ...,
        assign_public_ip: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["resources", b"resources"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["assign_public_ip", b"assign_public_ip", "cluster_id", b"cluster_id", "health", b"health", "name", b"name", "resources", b"resources", "role", b"role", "services", b"services", "subnet_id", b"subnet_id", "zone_id", b"zone_id"]) -> None: ...

global___Host = Host

@typing.final
class Service(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Type:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Service._Type.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        TYPE_UNSPECIFIED: Service._Type.ValueType  # 0
        MYSQL_ERROR: Service._Type.ValueType  # 1
        """Host provides the MySQL error log."""
        MYSQL_GENERAL: Service._Type.ValueType  # 2
        """Host provides the MySQL general query log."""
        MYSQL_SLOW_QUERY: Service._Type.ValueType  # 3
        """Host provides the MySQL slow query log."""

    class Type(_Type, metaclass=_TypeEnumTypeWrapper): ...
    TYPE_UNSPECIFIED: Service.Type.ValueType  # 0
    MYSQL_ERROR: Service.Type.ValueType  # 1
    """Host provides the MySQL error log."""
    MYSQL_GENERAL: Service.Type.ValueType  # 2
    """Host provides the MySQL general query log."""
    MYSQL_SLOW_QUERY: Service.Type.ValueType  # 3
    """Host provides the MySQL slow query log."""

    class _Health:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _HealthEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Service._Health.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        HEALTH_UNKNOWN: Service._Health.ValueType  # 0
        """Health of the server is unknown."""
        ALIVE: Service._Health.ValueType  # 1
        """The server is working normally."""
        DEAD: Service._Health.ValueType  # 2
        """The server is dead or unresponsive."""

    class Health(_Health, metaclass=_HealthEnumTypeWrapper): ...
    HEALTH_UNKNOWN: Service.Health.ValueType  # 0
    """Health of the server is unknown."""
    ALIVE: Service.Health.ValueType  # 1
    """The server is working normally."""
    DEAD: Service.Health.ValueType  # 2
    """The server is dead or unresponsive."""

    TYPE_FIELD_NUMBER: builtins.int
    HEALTH_FIELD_NUMBER: builtins.int
    type: global___Service.Type.ValueType
    """Type of the service provided by the host."""
    health: global___Service.Health.ValueType
    """Status code of server availability."""
    def __init__(
        self,
        *,
        type: global___Service.Type.ValueType = ...,
        health: global___Service.Health.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["health", b"health", "type", b"type"]) -> None: ...

global___Service = Service

@typing.final
class Resources(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_PRESET_ID_FIELD_NUMBER: builtins.int
    DISK_SIZE_FIELD_NUMBER: builtins.int
    DISK_TYPE_ID_FIELD_NUMBER: builtins.int
    resource_preset_id: builtins.str
    """ID of the preset for computational resources available to a host (CPU, memory etc.).
    All available presets are listed in the [documentation](/docs/managed-mysql/concepts/instance-types).
    """
    disk_size: builtins.int
    """Volume of the storage available to a host."""
    disk_type_id: builtins.str
    """Type of the storage environment for the host.
    Possible values:
    * network-ssd - network SSD drive,
    * local-ssd - local SSD storage.
    """
    def __init__(
        self,
        *,
        resource_preset_id: builtins.str = ...,
        disk_size: builtins.int = ...,
        disk_type_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["disk_size", b"disk_size", "disk_type_id", b"disk_type_id", "resource_preset_id", b"resource_preset_id"]) -> None: ...

global___Resources = Resources
