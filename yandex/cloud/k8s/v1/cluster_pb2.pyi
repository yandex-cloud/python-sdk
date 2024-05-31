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
import yandex.cloud.k8s.v1.maintenance_pb2
import yandex.cloud.k8s.v1.version_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _ReleaseChannel:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ReleaseChannelEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ReleaseChannel.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    RELEASE_CHANNEL_UNSPECIFIED: _ReleaseChannel.ValueType  # 0
    RAPID: _ReleaseChannel.ValueType  # 1
    """Minor updates with new functions and improvements are often added.
    You can't disable automatic updates in this channel, but you can specify a time period for automatic updates.
    """
    REGULAR: _ReleaseChannel.ValueType  # 2
    """New functions and improvements are added in chunks shortly after they appear on `RAPID`."""
    STABLE: _ReleaseChannel.ValueType  # 3
    """Only updates related to bug fixes or security improvements are added."""

class ReleaseChannel(_ReleaseChannel, metaclass=_ReleaseChannelEnumTypeWrapper): ...

RELEASE_CHANNEL_UNSPECIFIED: ReleaseChannel.ValueType  # 0
RAPID: ReleaseChannel.ValueType  # 1
"""Minor updates with new functions and improvements are often added.
You can't disable automatic updates in this channel, but you can specify a time period for automatic updates.
"""
REGULAR: ReleaseChannel.ValueType  # 2
"""New functions and improvements are added in chunks shortly after they appear on `RAPID`."""
STABLE: ReleaseChannel.ValueType  # 3
"""Only updates related to bug fixes or security improvements are added."""
global___ReleaseChannel = ReleaseChannel

@typing.final
class Cluster(google.protobuf.message.Message):
    """A Kubernetes cluster."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Cluster._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: Cluster._Status.ValueType  # 0
        PROVISIONING: Cluster._Status.ValueType  # 1
        """Kubernetes cluster is waiting for resources to be allocated."""
        RUNNING: Cluster._Status.ValueType  # 2
        """Kubernetes cluster is running."""
        RECONCILING: Cluster._Status.ValueType  # 3
        """Kubernetes cluster is being reconciled."""
        STOPPING: Cluster._Status.ValueType  # 4
        """Kubernetes cluster is being stopped."""
        STOPPED: Cluster._Status.ValueType  # 5
        """Kubernetes cluster stopped."""
        DELETING: Cluster._Status.ValueType  # 6
        """Kubernetes cluster is being deleted."""
        STARTING: Cluster._Status.ValueType  # 7
        """Kubernetes cluster is being started."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...
    STATUS_UNSPECIFIED: Cluster.Status.ValueType  # 0
    PROVISIONING: Cluster.Status.ValueType  # 1
    """Kubernetes cluster is waiting for resources to be allocated."""
    RUNNING: Cluster.Status.ValueType  # 2
    """Kubernetes cluster is running."""
    RECONCILING: Cluster.Status.ValueType  # 3
    """Kubernetes cluster is being reconciled."""
    STOPPING: Cluster.Status.ValueType  # 4
    """Kubernetes cluster is being stopped."""
    STOPPED: Cluster.Status.ValueType  # 5
    """Kubernetes cluster stopped."""
    DELETING: Cluster.Status.ValueType  # 6
    """Kubernetes cluster is being deleted."""
    STARTING: Cluster.Status.ValueType  # 7
    """Kubernetes cluster is being started."""

    class _Health:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _HealthEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Cluster._Health.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        HEALTH_UNSPECIFIED: Cluster._Health.ValueType  # 0
        HEALTHY: Cluster._Health.ValueType  # 1
        """Kubernetes cluster is alive and well."""
        UNHEALTHY: Cluster._Health.ValueType  # 2
        """Kubernetes cluster is inoperable."""

    class Health(_Health, metaclass=_HealthEnumTypeWrapper): ...
    HEALTH_UNSPECIFIED: Cluster.Health.ValueType  # 0
    HEALTHY: Cluster.Health.ValueType  # 1
    """Kubernetes cluster is alive and well."""
    UNHEALTHY: Cluster.Health.ValueType  # 2
    """Kubernetes cluster is inoperable."""

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
    HEALTH_FIELD_NUMBER: builtins.int
    NETWORK_ID_FIELD_NUMBER: builtins.int
    MASTER_FIELD_NUMBER: builtins.int
    IP_ALLOCATION_POLICY_FIELD_NUMBER: builtins.int
    GATEWAY_IPV4_ADDRESS_FIELD_NUMBER: builtins.int
    SERVICE_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    NODE_SERVICE_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    RELEASE_CHANNEL_FIELD_NUMBER: builtins.int
    NETWORK_POLICY_FIELD_NUMBER: builtins.int
    KMS_PROVIDER_FIELD_NUMBER: builtins.int
    LOG_GROUP_ID_FIELD_NUMBER: builtins.int
    CILIUM_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the Kubernetes cluster."""
    folder_id: builtins.str
    """ID of the folder that the Kubernetes cluster belongs to."""
    name: builtins.str
    """Name of the Kubernetes cluster."""
    description: builtins.str
    """Description of the Kubernetes cluster. 0-256 characters long."""
    status: global___Cluster.Status.ValueType
    """Status of the Kubernetes cluster."""
    health: global___Cluster.Health.ValueType
    """Health of the Kubernetes cluster."""
    network_id: builtins.str
    """ID of the network the Kubernetes cluster belongs to."""
    gateway_ipv4_address: builtins.str
    """Gateway IPv4 address."""
    service_account_id: builtins.str
    """Service account to be used for provisioning Compute Cloud and VPC resources for Kubernetes cluster."""
    node_service_account_id: builtins.str
    """Service account to be used by the worker nodes of the Kubernetes cluster to access Container Registry or to push node logs and metrics."""
    release_channel: global___ReleaseChannel.ValueType
    """When creating a Kubernetes cluster, you should specify one of three release channels. The release channel contains several Kubernetes versions.
    Channels differ in the set of available versions, the management of auto-updates, and the updates received.
    You can't change the channel once the Kubernetes cluster is created, you can only recreate the Kubernetes cluster and specify a new release channel.
    For more details see [documentation](/docs/managed-kubernetes/concepts/release-channels-and-updates).
    """
    log_group_id: builtins.str
    """Log group where cluster stores cluster system logs, like audit, events, or controlplane logs."""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `key:value` pairs. Maximum of 64 per resource."""

    @property
    def master(self) -> global___Master:
        """Properties of the master for the Kubernetes cluster."""

    @property
    def ip_allocation_policy(self) -> global___IPAllocationPolicy:
        """Allocation policy for IP addresses of services and pods inside the Kubernetes cluster in different availability zones."""

    @property
    def network_policy(self) -> global___NetworkPolicy: ...
    @property
    def kms_provider(self) -> global___KMSProvider:
        """KMS provider configuration."""

    @property
    def cilium(self) -> global___Cilium: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        folder_id: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        status: global___Cluster.Status.ValueType = ...,
        health: global___Cluster.Health.ValueType = ...,
        network_id: builtins.str = ...,
        master: global___Master | None = ...,
        ip_allocation_policy: global___IPAllocationPolicy | None = ...,
        gateway_ipv4_address: builtins.str = ...,
        service_account_id: builtins.str = ...,
        node_service_account_id: builtins.str = ...,
        release_channel: global___ReleaseChannel.ValueType = ...,
        network_policy: global___NetworkPolicy | None = ...,
        kms_provider: global___KMSProvider | None = ...,
        log_group_id: builtins.str = ...,
        cilium: global___Cilium | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["cilium", b"cilium", "created_at", b"created_at", "gateway_ipv4_address", b"gateway_ipv4_address", "internet_gateway", b"internet_gateway", "ip_allocation_policy", b"ip_allocation_policy", "kms_provider", b"kms_provider", "master", b"master", "network_implementation", b"network_implementation", "network_policy", b"network_policy"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cilium", b"cilium", "created_at", b"created_at", "description", b"description", "folder_id", b"folder_id", "gateway_ipv4_address", b"gateway_ipv4_address", "health", b"health", "id", b"id", "internet_gateway", b"internet_gateway", "ip_allocation_policy", b"ip_allocation_policy", "kms_provider", b"kms_provider", "labels", b"labels", "log_group_id", b"log_group_id", "master", b"master", "name", b"name", "network_id", b"network_id", "network_implementation", b"network_implementation", "network_policy", b"network_policy", "node_service_account_id", b"node_service_account_id", "release_channel", b"release_channel", "service_account_id", b"service_account_id", "status", b"status"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["internet_gateway", b"internet_gateway"]) -> typing.Literal["gateway_ipv4_address"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["network_implementation", b"network_implementation"]) -> typing.Literal["cilium"] | None: ...

global___Cluster = Cluster

@typing.final
class Master(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ZONAL_MASTER_FIELD_NUMBER: builtins.int
    REGIONAL_MASTER_FIELD_NUMBER: builtins.int
    LOCATIONS_FIELD_NUMBER: builtins.int
    ETCD_CLUSTER_SIZE_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    ENDPOINTS_FIELD_NUMBER: builtins.int
    MASTER_AUTH_FIELD_NUMBER: builtins.int
    VERSION_INFO_FIELD_NUMBER: builtins.int
    MAINTENANCE_POLICY_FIELD_NUMBER: builtins.int
    SECURITY_GROUP_IDS_FIELD_NUMBER: builtins.int
    MASTER_LOGGING_FIELD_NUMBER: builtins.int
    etcd_cluster_size: builtins.int
    """Number of etcd nodes in cluster."""
    version: builtins.str
    """Version of Kubernetes components that runs on the master."""
    @property
    def zonal_master(self) -> global___ZonalMaster:
        """Parameters of the availability zone for the master."""

    @property
    def regional_master(self) -> global___RegionalMaster:
        """Parameters of the region for the master."""

    @property
    def locations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Location]:
        """Locations specification for Kubernetes control-plane (master) instances."""

    @property
    def endpoints(self) -> global___MasterEndpoints:
        """Endpoints of the master. Endpoints constitute of scheme and port (i.e. `https://ip-address:port`)
        and can be used by the clients to communicate with the Kubernetes API of the Kubernetes cluster.
        """

    @property
    def master_auth(self) -> global___MasterAuth:
        """Master authentication parameters are used to establish trust between the master and a client."""

    @property
    def version_info(self) -> yandex.cloud.k8s.v1.version_pb2.VersionInfo:
        """Detailed information about the Kubernetes version that is running on the master."""

    @property
    def maintenance_policy(self) -> global___MasterMaintenancePolicy:
        """Maintenance policy of the master."""

    @property
    def security_group_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Master security groups."""

    @property
    def master_logging(self) -> global___MasterLogging:
        """Cloud Logging for master components."""

    def __init__(
        self,
        *,
        zonal_master: global___ZonalMaster | None = ...,
        regional_master: global___RegionalMaster | None = ...,
        locations: collections.abc.Iterable[global___Location] | None = ...,
        etcd_cluster_size: builtins.int = ...,
        version: builtins.str = ...,
        endpoints: global___MasterEndpoints | None = ...,
        master_auth: global___MasterAuth | None = ...,
        version_info: yandex.cloud.k8s.v1.version_pb2.VersionInfo | None = ...,
        maintenance_policy: global___MasterMaintenancePolicy | None = ...,
        security_group_ids: collections.abc.Iterable[builtins.str] | None = ...,
        master_logging: global___MasterLogging | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["endpoints", b"endpoints", "maintenance_policy", b"maintenance_policy", "master_auth", b"master_auth", "master_logging", b"master_logging", "master_type", b"master_type", "regional_master", b"regional_master", "version_info", b"version_info", "zonal_master", b"zonal_master"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["endpoints", b"endpoints", "etcd_cluster_size", b"etcd_cluster_size", "locations", b"locations", "maintenance_policy", b"maintenance_policy", "master_auth", b"master_auth", "master_logging", b"master_logging", "master_type", b"master_type", "regional_master", b"regional_master", "security_group_ids", b"security_group_ids", "version", b"version", "version_info", b"version_info", "zonal_master", b"zonal_master"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["master_type", b"master_type"]) -> typing.Literal["zonal_master", "regional_master"] | None: ...

global___Master = Master

@typing.final
class MasterAuth(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_CA_CERTIFICATE_FIELD_NUMBER: builtins.int
    cluster_ca_certificate: builtins.str
    """PEM-encoded public certificate that is the root of trust for the Kubernetes cluster."""
    def __init__(
        self,
        *,
        cluster_ca_certificate: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_ca_certificate", b"cluster_ca_certificate"]) -> None: ...

global___MasterAuth = MasterAuth

@typing.final
class ZonalMaster(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ZONE_ID_FIELD_NUMBER: builtins.int
    INTERNAL_V4_ADDRESS_FIELD_NUMBER: builtins.int
    EXTERNAL_V4_ADDRESS_FIELD_NUMBER: builtins.int
    zone_id: builtins.str
    """ID of the availability zone where the master resides."""
    internal_v4_address: builtins.str
    """IPv4 internal network address that is assigned to the master."""
    external_v4_address: builtins.str
    """IPv4 external network address that is assigned to the master."""
    def __init__(
        self,
        *,
        zone_id: builtins.str = ...,
        internal_v4_address: builtins.str = ...,
        external_v4_address: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["external_v4_address", b"external_v4_address", "internal_v4_address", b"internal_v4_address", "zone_id", b"zone_id"]) -> None: ...

global___ZonalMaster = ZonalMaster

@typing.final
class RegionalMaster(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REGION_ID_FIELD_NUMBER: builtins.int
    INTERNAL_V4_ADDRESS_FIELD_NUMBER: builtins.int
    EXTERNAL_V4_ADDRESS_FIELD_NUMBER: builtins.int
    EXTERNAL_V6_ADDRESS_FIELD_NUMBER: builtins.int
    region_id: builtins.str
    """ID of the region where the master resides."""
    internal_v4_address: builtins.str
    """IPv4 internal network address that is assigned to the master."""
    external_v4_address: builtins.str
    """IPv4 external network address that is assigned to the master."""
    external_v6_address: builtins.str
    """IPv6 external network address that is assigned to the master."""
    def __init__(
        self,
        *,
        region_id: builtins.str = ...,
        internal_v4_address: builtins.str = ...,
        external_v4_address: builtins.str = ...,
        external_v6_address: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["external_v4_address", b"external_v4_address", "external_v6_address", b"external_v6_address", "internal_v4_address", b"internal_v4_address", "region_id", b"region_id"]) -> None: ...

global___RegionalMaster = RegionalMaster

@typing.final
class Location(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ZONE_ID_FIELD_NUMBER: builtins.int
    SUBNET_ID_FIELD_NUMBER: builtins.int
    zone_id: builtins.str
    """ID of the availability zone where the master resides."""
    subnet_id: builtins.str
    """ID of the VPC network's subnet where the master resides."""
    def __init__(
        self,
        *,
        zone_id: builtins.str = ...,
        subnet_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["subnet_id", b"subnet_id", "zone_id", b"zone_id"]) -> None: ...

global___Location = Location

@typing.final
class MasterEndpoints(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INTERNAL_V4_ENDPOINT_FIELD_NUMBER: builtins.int
    EXTERNAL_V4_ENDPOINT_FIELD_NUMBER: builtins.int
    EXTERNAL_V6_ENDPOINT_FIELD_NUMBER: builtins.int
    internal_v4_endpoint: builtins.str
    """Internal endpoint that can be used to connect to the master from cloud networks."""
    external_v4_endpoint: builtins.str
    """External endpoint that can be used to access Kubernetes cluster API from the internet (outside of the cloud)."""
    external_v6_endpoint: builtins.str
    """External IPv6 endpoint that can be used to access Kubernetes cluster API from the internet (outside of the cloud)."""
    def __init__(
        self,
        *,
        internal_v4_endpoint: builtins.str = ...,
        external_v4_endpoint: builtins.str = ...,
        external_v6_endpoint: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["external_v4_endpoint", b"external_v4_endpoint", "external_v6_endpoint", b"external_v6_endpoint", "internal_v4_endpoint", b"internal_v4_endpoint"]) -> None: ...

global___MasterEndpoints = MasterEndpoints

@typing.final
class IPAllocationPolicy(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_IPV4_CIDR_BLOCK_FIELD_NUMBER: builtins.int
    NODE_IPV4_CIDR_MASK_SIZE_FIELD_NUMBER: builtins.int
    SERVICE_IPV4_CIDR_BLOCK_FIELD_NUMBER: builtins.int
    CLUSTER_IPV6_CIDR_BLOCK_FIELD_NUMBER: builtins.int
    SERVICE_IPV6_CIDR_BLOCK_FIELD_NUMBER: builtins.int
    cluster_ipv4_cidr_block: builtins.str
    """CIDR block. IP range for allocating pod addresses.

    It should not overlap with any subnet in the network the Kubernetes cluster located in. Static routes will be
    set up for this CIDR blocks in node subnets.
    """
    node_ipv4_cidr_mask_size: builtins.int
    """Size of the masks that are assigned for each node in the cluster.

    If not specified, 24 is used.
    """
    service_ipv4_cidr_block: builtins.str
    """CIDR block. IP range Kubernetes service Kubernetes cluster IP addresses will be allocated from.

    It should not overlap with any subnet in the network the Kubernetes cluster located in.
    """
    cluster_ipv6_cidr_block: builtins.str
    """IPv6 range for allocating pod IP addresses."""
    service_ipv6_cidr_block: builtins.str
    """IPv6 range for allocating Kubernetes service IP addresses"""
    def __init__(
        self,
        *,
        cluster_ipv4_cidr_block: builtins.str = ...,
        node_ipv4_cidr_mask_size: builtins.int = ...,
        service_ipv4_cidr_block: builtins.str = ...,
        cluster_ipv6_cidr_block: builtins.str = ...,
        service_ipv6_cidr_block: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_ipv4_cidr_block", b"cluster_ipv4_cidr_block", "cluster_ipv6_cidr_block", b"cluster_ipv6_cidr_block", "node_ipv4_cidr_mask_size", b"node_ipv4_cidr_mask_size", "service_ipv4_cidr_block", b"service_ipv4_cidr_block", "service_ipv6_cidr_block", b"service_ipv6_cidr_block"]) -> None: ...

global___IPAllocationPolicy = IPAllocationPolicy

@typing.final
class MasterMaintenancePolicy(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AUTO_UPGRADE_FIELD_NUMBER: builtins.int
    MAINTENANCE_WINDOW_FIELD_NUMBER: builtins.int
    auto_upgrade: builtins.bool
    """If set to true, automatic updates are installed in the specified period of time with no interaction from the user.
    If set to false, automatic upgrades are disabled.
    """
    @property
    def maintenance_window(self) -> yandex.cloud.k8s.v1.maintenance_pb2.MaintenanceWindow:
        """Maintenance window settings. Update will start at the specified time and last no more than the specified duration.
        The time is set in UTC.
        """

    def __init__(
        self,
        *,
        auto_upgrade: builtins.bool = ...,
        maintenance_window: yandex.cloud.k8s.v1.maintenance_pb2.MaintenanceWindow | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["maintenance_window", b"maintenance_window"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["auto_upgrade", b"auto_upgrade", "maintenance_window", b"maintenance_window"]) -> None: ...

global___MasterMaintenancePolicy = MasterMaintenancePolicy

@typing.final
class MasterLogging(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ENABLED_FIELD_NUMBER: builtins.int
    LOG_GROUP_ID_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    AUDIT_ENABLED_FIELD_NUMBER: builtins.int
    CLUSTER_AUTOSCALER_ENABLED_FIELD_NUMBER: builtins.int
    KUBE_APISERVER_ENABLED_FIELD_NUMBER: builtins.int
    EVENTS_ENABLED_FIELD_NUMBER: builtins.int
    enabled: builtins.bool
    """Identifies whether Cloud Logging is enabled for master components."""
    log_group_id: builtins.str
    """ID of the log group where logs of master components should be stored."""
    folder_id: builtins.str
    """ID of the folder where logs should be stored (in default group)."""
    audit_enabled: builtins.bool
    """Identifies whether Cloud Logging is enabled for audit logs."""
    cluster_autoscaler_enabled: builtins.bool
    """Identifies whether Cloud Logging is enabled for cluster-autoscaler."""
    kube_apiserver_enabled: builtins.bool
    """Identifies whether Cloud Logging is enabled for kube-apiserver."""
    events_enabled: builtins.bool
    """Identifies whether Cloud Logging is enabled for events."""
    def __init__(
        self,
        *,
        enabled: builtins.bool = ...,
        log_group_id: builtins.str = ...,
        folder_id: builtins.str = ...,
        audit_enabled: builtins.bool = ...,
        cluster_autoscaler_enabled: builtins.bool = ...,
        kube_apiserver_enabled: builtins.bool = ...,
        events_enabled: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["destination", b"destination", "folder_id", b"folder_id", "log_group_id", b"log_group_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["audit_enabled", b"audit_enabled", "cluster_autoscaler_enabled", b"cluster_autoscaler_enabled", "destination", b"destination", "enabled", b"enabled", "events_enabled", b"events_enabled", "folder_id", b"folder_id", "kube_apiserver_enabled", b"kube_apiserver_enabled", "log_group_id", b"log_group_id"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["destination", b"destination"]) -> typing.Literal["log_group_id", "folder_id"] | None: ...

global___MasterLogging = MasterLogging

@typing.final
class NetworkPolicy(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Provider:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _ProviderEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[NetworkPolicy._Provider.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        PROVIDER_UNSPECIFIED: NetworkPolicy._Provider.ValueType  # 0
        CALICO: NetworkPolicy._Provider.ValueType  # 1

    class Provider(_Provider, metaclass=_ProviderEnumTypeWrapper): ...
    PROVIDER_UNSPECIFIED: NetworkPolicy.Provider.ValueType  # 0
    CALICO: NetworkPolicy.Provider.ValueType  # 1

    PROVIDER_FIELD_NUMBER: builtins.int
    provider: global___NetworkPolicy.Provider.ValueType
    def __init__(
        self,
        *,
        provider: global___NetworkPolicy.Provider.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["provider", b"provider"]) -> None: ...

global___NetworkPolicy = NetworkPolicy

@typing.final
class KMSProvider(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_ID_FIELD_NUMBER: builtins.int
    key_id: builtins.str
    """KMS key ID for secrets encryption.
    To obtain a KMS key ID use a [yandex.cloud.kms.v1.SymmetricKeyService.List] request.
    """
    def __init__(
        self,
        *,
        key_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["key_id", b"key_id"]) -> None: ...

global___KMSProvider = KMSProvider

@typing.final
class Cilium(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _RoutingMode:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _RoutingModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Cilium._RoutingMode.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        ROUTING_MODE_UNSPECIFIED: Cilium._RoutingMode.ValueType  # 0
        TUNNEL: Cilium._RoutingMode.ValueType  # 1

    class RoutingMode(_RoutingMode, metaclass=_RoutingModeEnumTypeWrapper): ...
    ROUTING_MODE_UNSPECIFIED: Cilium.RoutingMode.ValueType  # 0
    TUNNEL: Cilium.RoutingMode.ValueType  # 1

    ROUTING_MODE_FIELD_NUMBER: builtins.int
    routing_mode: global___Cilium.RoutingMode.ValueType
    def __init__(
        self,
        *,
        routing_mode: global___Cilium.RoutingMode.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["routing_mode", b"routing_mode"]) -> None: ...

global___Cilium = Cilium