"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.wrappers_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class PXFConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONNECTION_TIMEOUT_FIELD_NUMBER: builtins.int
    UPLOAD_TIMEOUT_FIELD_NUMBER: builtins.int
    MAX_THREADS_FIELD_NUMBER: builtins.int
    POOL_ALLOW_CORE_THREAD_TIMEOUT_FIELD_NUMBER: builtins.int
    POOL_CORE_SIZE_FIELD_NUMBER: builtins.int
    POOL_QUEUE_CAPACITY_FIELD_NUMBER: builtins.int
    POOL_MAX_SIZE_FIELD_NUMBER: builtins.int
    XMX_FIELD_NUMBER: builtins.int
    XMS_FIELD_NUMBER: builtins.int
    @property
    def connection_timeout(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """Connection"""

    @property
    def upload_timeout(self) -> google.protobuf.wrappers_pb2.Int64Value: ...
    @property
    def max_threads(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """Thread pool"""

    @property
    def pool_allow_core_thread_timeout(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def pool_core_size(self) -> google.protobuf.wrappers_pb2.Int64Value: ...
    @property
    def pool_queue_capacity(self) -> google.protobuf.wrappers_pb2.Int64Value: ...
    @property
    def pool_max_size(self) -> google.protobuf.wrappers_pb2.Int64Value: ...
    @property
    def xmx(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """JVM"""

    @property
    def xms(self) -> google.protobuf.wrappers_pb2.Int64Value: ...
    def __init__(
        self,
        *,
        connection_timeout: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        upload_timeout: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        max_threads: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        pool_allow_core_thread_timeout: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        pool_core_size: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        pool_queue_capacity: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        pool_max_size: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        xmx: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        xms: google.protobuf.wrappers_pb2.Int64Value | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["connection_timeout", b"connection_timeout", "max_threads", b"max_threads", "pool_allow_core_thread_timeout", b"pool_allow_core_thread_timeout", "pool_core_size", b"pool_core_size", "pool_max_size", b"pool_max_size", "pool_queue_capacity", b"pool_queue_capacity", "upload_timeout", b"upload_timeout", "xms", b"xms", "xmx", b"xmx"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["connection_timeout", b"connection_timeout", "max_threads", b"max_threads", "pool_allow_core_thread_timeout", b"pool_allow_core_thread_timeout", "pool_core_size", b"pool_core_size", "pool_max_size", b"pool_max_size", "pool_queue_capacity", b"pool_queue_capacity", "upload_timeout", b"upload_timeout", "xms", b"xms", "xmx", b"xmx"]) -> None: ...

global___PXFConfig = PXFConfig

@typing.final
class PXFConfigSet(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EFFECTIVE_CONFIG_FIELD_NUMBER: builtins.int
    USER_CONFIG_FIELD_NUMBER: builtins.int
    DEFAULT_CONFIG_FIELD_NUMBER: builtins.int
    @property
    def effective_config(self) -> global___PXFConfig: ...
    @property
    def user_config(self) -> global___PXFConfig:
        """User-defined settings"""

    @property
    def default_config(self) -> global___PXFConfig:
        """Default configuration"""

    def __init__(
        self,
        *,
        effective_config: global___PXFConfig | None = ...,
        user_config: global___PXFConfig | None = ...,
        default_config: global___PXFConfig | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["default_config", b"default_config", "effective_config", b"effective_config", "user_config", b"user_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["default_config", b"default_config", "effective_config", b"effective_config", "user_config", b"user_config"]) -> None: ...

global___PXFConfigSet = PXFConfigSet

@typing.final
class PXFDatasourceS3(google.protobuf.message.Message):
    """Datasources API"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCESS_KEY_FIELD_NUMBER: builtins.int
    SECRET_KEY_FIELD_NUMBER: builtins.int
    FAST_UPLOAD_FIELD_NUMBER: builtins.int
    ENDPOINT_FIELD_NUMBER: builtins.int
    access_key: builtins.str
    secret_key: builtins.str
    endpoint: builtins.str
    @property
    def fast_upload(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    def __init__(
        self,
        *,
        access_key: builtins.str = ...,
        secret_key: builtins.str = ...,
        fast_upload: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        endpoint: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["fast_upload", b"fast_upload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["access_key", b"access_key", "endpoint", b"endpoint", "fast_upload", b"fast_upload", "secret_key", b"secret_key"]) -> None: ...

global___PXFDatasourceS3 = PXFDatasourceS3

@typing.final
class PXFDatasourceJDBC(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DRIVER_FIELD_NUMBER: builtins.int
    URL_FIELD_NUMBER: builtins.int
    USER_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    STATEMENT_BATCH_SIZE_FIELD_NUMBER: builtins.int
    STATEMENT_FETCH_SIZE_FIELD_NUMBER: builtins.int
    STATEMENT_QUERY_TIMEOUT_FIELD_NUMBER: builtins.int
    POOL_ENABLED_FIELD_NUMBER: builtins.int
    POOL_MAXIMUM_SIZE_FIELD_NUMBER: builtins.int
    POOL_CONNECTION_TIMEOUT_FIELD_NUMBER: builtins.int
    POOL_IDLE_TIMEOUT_FIELD_NUMBER: builtins.int
    POOL_MINIMUM_IDLE_FIELD_NUMBER: builtins.int
    driver: builtins.str
    """Matches jdbc.driver"""
    url: builtins.str
    """Matches jdbc.url"""
    user: builtins.str
    """Matches jdbc.user"""
    password: builtins.str
    """Matches jdbc.password"""
    @property
    def statement_batch_size(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """Matches jdbc.statement.batchsize"""

    @property
    def statement_fetch_size(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """Matches jdbc.statement.fetchsize"""

    @property
    def statement_query_timeout(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """Matches jdbc.statement.querytimeout"""

    @property
    def pool_enabled(self) -> google.protobuf.wrappers_pb2.BoolValue:
        """Matches jdbc.pool.enabled"""

    @property
    def pool_maximum_size(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """Matches jdbc.pool.property.maximumpoolsize"""

    @property
    def pool_connection_timeout(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """Matches jdbc.pool.property.connectiontimeout"""

    @property
    def pool_idle_timeout(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """Matches jdbc.pool.property.idletimeout"""

    @property
    def pool_minimum_idle(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """Matches jdbc.pool.property.minimumidle"""

    def __init__(
        self,
        *,
        driver: builtins.str = ...,
        url: builtins.str = ...,
        user: builtins.str = ...,
        password: builtins.str = ...,
        statement_batch_size: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        statement_fetch_size: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        statement_query_timeout: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        pool_enabled: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        pool_maximum_size: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        pool_connection_timeout: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        pool_idle_timeout: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        pool_minimum_idle: google.protobuf.wrappers_pb2.Int64Value | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["pool_connection_timeout", b"pool_connection_timeout", "pool_enabled", b"pool_enabled", "pool_idle_timeout", b"pool_idle_timeout", "pool_maximum_size", b"pool_maximum_size", "pool_minimum_idle", b"pool_minimum_idle", "statement_batch_size", b"statement_batch_size", "statement_fetch_size", b"statement_fetch_size", "statement_query_timeout", b"statement_query_timeout"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["driver", b"driver", "password", b"password", "pool_connection_timeout", b"pool_connection_timeout", "pool_enabled", b"pool_enabled", "pool_idle_timeout", b"pool_idle_timeout", "pool_maximum_size", b"pool_maximum_size", "pool_minimum_idle", b"pool_minimum_idle", "statement_batch_size", b"statement_batch_size", "statement_fetch_size", b"statement_fetch_size", "statement_query_timeout", b"statement_query_timeout", "url", b"url", "user", b"user"]) -> None: ...

global___PXFDatasourceJDBC = PXFDatasourceJDBC

@typing.final
class PXFDatasourceCore(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEFAULT_FS_FIELD_NUMBER: builtins.int
    SECURITY_AUTH_TO_LOCAL_FIELD_NUMBER: builtins.int
    default_fs: builtins.str
    security_auth_to_local: builtins.str
    def __init__(
        self,
        *,
        default_fs: builtins.str = ...,
        security_auth_to_local: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["default_fs", b"default_fs", "security_auth_to_local", b"security_auth_to_local"]) -> None: ...

global___PXFDatasourceCore = PXFDatasourceCore

@typing.final
class PXFDatasourceKerberos(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ENABLE_FIELD_NUMBER: builtins.int
    PRIMARY_FIELD_NUMBER: builtins.int
    REALM_FIELD_NUMBER: builtins.int
    KDC_SERVERS_FIELD_NUMBER: builtins.int
    ADMIN_SERVER_FIELD_NUMBER: builtins.int
    DEFAULT_DOMAIN_FIELD_NUMBER: builtins.int
    KEYTAB_BASE64_FIELD_NUMBER: builtins.int
    primary: builtins.str
    realm: builtins.str
    admin_server: builtins.str
    default_domain: builtins.str
    keytab_base64: builtins.str
    @property
    def enable(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def kdc_servers(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        enable: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        primary: builtins.str = ...,
        realm: builtins.str = ...,
        kdc_servers: collections.abc.Iterable[builtins.str] | None = ...,
        admin_server: builtins.str = ...,
        default_domain: builtins.str = ...,
        keytab_base64: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["enable", b"enable"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["admin_server", b"admin_server", "default_domain", b"default_domain", "enable", b"enable", "kdc_servers", b"kdc_servers", "keytab_base64", b"keytab_base64", "primary", b"primary", "realm", b"realm"]) -> None: ...

global___PXFDatasourceKerberos = PXFDatasourceKerberos

@typing.final
class PXFDatasourceHDFSDfsNamenode(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RPC_ADDRESS_FIELD_NUMBER: builtins.int
    SERVICE_RPC_ADDRESS_FIELD_NUMBER: builtins.int
    HTTP_ADDRESS_FIELD_NUMBER: builtins.int
    HTTPS_ADDRESS_FIELD_NUMBER: builtins.int
    rpc_address: builtins.str
    service_rpc_address: builtins.str
    http_address: builtins.str
    https_address: builtins.str
    def __init__(
        self,
        *,
        rpc_address: builtins.str = ...,
        service_rpc_address: builtins.str = ...,
        http_address: builtins.str = ...,
        https_address: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["http_address", b"http_address", "https_address", b"https_address", "rpc_address", b"rpc_address", "service_rpc_address", b"service_rpc_address"]) -> None: ...

global___PXFDatasourceHDFSDfsNamenode = PXFDatasourceHDFSDfsNamenode

@typing.final
class PXFDatasourceHDFSDfs(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class NamenodesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___PXFDatasourceHDFSDfsNamenode: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: global___PXFDatasourceHDFSDfsNamenode | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    HA_AUTOMATIC_FAILOVER_ENABLED_FIELD_NUMBER: builtins.int
    BLOCK_ACCESS_TOKEN_ENABLED_FIELD_NUMBER: builtins.int
    USE_DATANODE_HOSTNAME_FIELD_NUMBER: builtins.int
    NAMENODES_FIELD_NUMBER: builtins.int
    NAMESERVICES_FIELD_NUMBER: builtins.int
    nameservices: builtins.str
    """Corresponds well-known HDFS client setting "dfs.nameservices" for this datasource"""
    @property
    def ha_automatic_failover_enabled(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def block_access_token_enabled(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def use_datanode_hostname(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def namenodes(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___PXFDatasourceHDFSDfsNamenode]: ...
    def __init__(
        self,
        *,
        ha_automatic_failover_enabled: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        block_access_token_enabled: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        use_datanode_hostname: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        namenodes: collections.abc.Mapping[builtins.str, global___PXFDatasourceHDFSDfsNamenode] | None = ...,
        nameservices: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["block_access_token_enabled", b"block_access_token_enabled", "ha_automatic_failover_enabled", b"ha_automatic_failover_enabled", "use_datanode_hostname", b"use_datanode_hostname"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["block_access_token_enabled", b"block_access_token_enabled", "ha_automatic_failover_enabled", b"ha_automatic_failover_enabled", "namenodes", b"namenodes", "nameservices", b"nameservices", "use_datanode_hostname", b"use_datanode_hostname"]) -> None: ...

global___PXFDatasourceHDFSDfs = PXFDatasourceHDFSDfs

@typing.final
class PXFDatasourceHDFSYarnHaRm(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCEMANAGER_ADDRESS_FIELD_NUMBER: builtins.int
    RESOURCEMANAGER_SCHEDULER_ADDRESS_FIELD_NUMBER: builtins.int
    RESOURCEMANAGER_RESOURCE_TRACKER_ADDRESS_FIELD_NUMBER: builtins.int
    RESOURCEMANAGER_ADMIN_ADDRESS_FIELD_NUMBER: builtins.int
    RESOURCEMANAGER_WEBAPP_ADDRESS_FIELD_NUMBER: builtins.int
    RESOURCEMANAGER_WEBAPP_HTTPS_ADDRESS_FIELD_NUMBER: builtins.int
    resourcemanager_address: builtins.str
    resourcemanager_scheduler_address: builtins.str
    resourcemanager_resource_tracker_address: builtins.str
    resourcemanager_admin_address: builtins.str
    resourcemanager_webapp_address: builtins.str
    resourcemanager_webapp_https_address: builtins.str
    def __init__(
        self,
        *,
        resourcemanager_address: builtins.str = ...,
        resourcemanager_scheduler_address: builtins.str = ...,
        resourcemanager_resource_tracker_address: builtins.str = ...,
        resourcemanager_admin_address: builtins.str = ...,
        resourcemanager_webapp_address: builtins.str = ...,
        resourcemanager_webapp_https_address: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["resourcemanager_address", b"resourcemanager_address", "resourcemanager_admin_address", b"resourcemanager_admin_address", "resourcemanager_resource_tracker_address", b"resourcemanager_resource_tracker_address", "resourcemanager_scheduler_address", b"resourcemanager_scheduler_address", "resourcemanager_webapp_address", b"resourcemanager_webapp_address", "resourcemanager_webapp_https_address", b"resourcemanager_webapp_https_address"]) -> None: ...

global___PXFDatasourceHDFSYarnHaRm = PXFDatasourceHDFSYarnHaRm

@typing.final
class PXFDatasourceHDFSYarn(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class HaRmEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___PXFDatasourceHDFSYarnHaRm: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: global___PXFDatasourceHDFSYarnHaRm | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    RESOURCEMANAGER_HA_ENABLED_FIELD_NUMBER: builtins.int
    RESOURCEMANAGER_HA_AUTO_FAILOVER_ENABLED_FIELD_NUMBER: builtins.int
    RESOURCEMANAGER_HA_AUTO_FAILOVER_EMBEDDED_FIELD_NUMBER: builtins.int
    RESOURCEMANAGER_CLUSTER_ID_FIELD_NUMBER: builtins.int
    HA_RM_FIELD_NUMBER: builtins.int
    resourcemanager_cluster_id: builtins.str
    @property
    def resourcemanager_ha_enabled(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def resourcemanager_ha_auto_failover_enabled(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def resourcemanager_ha_auto_failover_embedded(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def ha_rm(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___PXFDatasourceHDFSYarnHaRm]: ...
    def __init__(
        self,
        *,
        resourcemanager_ha_enabled: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        resourcemanager_ha_auto_failover_enabled: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        resourcemanager_ha_auto_failover_embedded: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        resourcemanager_cluster_id: builtins.str = ...,
        ha_rm: collections.abc.Mapping[builtins.str, global___PXFDatasourceHDFSYarnHaRm] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["resourcemanager_ha_auto_failover_embedded", b"resourcemanager_ha_auto_failover_embedded", "resourcemanager_ha_auto_failover_enabled", b"resourcemanager_ha_auto_failover_enabled", "resourcemanager_ha_enabled", b"resourcemanager_ha_enabled"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["ha_rm", b"ha_rm", "resourcemanager_cluster_id", b"resourcemanager_cluster_id", "resourcemanager_ha_auto_failover_embedded", b"resourcemanager_ha_auto_failover_embedded", "resourcemanager_ha_auto_failover_enabled", b"resourcemanager_ha_auto_failover_enabled", "resourcemanager_ha_enabled", b"resourcemanager_ha_enabled"]) -> None: ...

global___PXFDatasourceHDFSYarn = PXFDatasourceHDFSYarn

@typing.final
class PXFDatasourceHDFS(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CORE_FIELD_NUMBER: builtins.int
    KERBEROS_FIELD_NUMBER: builtins.int
    USER_IMPERSONATION_FIELD_NUMBER: builtins.int
    USERNAME_FIELD_NUMBER: builtins.int
    SASL_CONNECTION_RETRIES_FIELD_NUMBER: builtins.int
    ZK_HOSTS_FIELD_NUMBER: builtins.int
    DFS_FIELD_NUMBER: builtins.int
    YARN_FIELD_NUMBER: builtins.int
    username: builtins.str
    @property
    def core(self) -> global___PXFDatasourceCore: ...
    @property
    def kerberos(self) -> global___PXFDatasourceKerberos: ...
    @property
    def user_impersonation(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def sasl_connection_retries(self) -> google.protobuf.wrappers_pb2.Int64Value: ...
    @property
    def zk_hosts(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def dfs(self) -> global___PXFDatasourceHDFSDfs: ...
    @property
    def yarn(self) -> global___PXFDatasourceHDFSYarn: ...
    def __init__(
        self,
        *,
        core: global___PXFDatasourceCore | None = ...,
        kerberos: global___PXFDatasourceKerberos | None = ...,
        user_impersonation: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        username: builtins.str = ...,
        sasl_connection_retries: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        zk_hosts: collections.abc.Iterable[builtins.str] | None = ...,
        dfs: global___PXFDatasourceHDFSDfs | None = ...,
        yarn: global___PXFDatasourceHDFSYarn | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["core", b"core", "dfs", b"dfs", "kerberos", b"kerberos", "sasl_connection_retries", b"sasl_connection_retries", "user_impersonation", b"user_impersonation", "yarn", b"yarn"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["core", b"core", "dfs", b"dfs", "kerberos", b"kerberos", "sasl_connection_retries", b"sasl_connection_retries", "user_impersonation", b"user_impersonation", "username", b"username", "yarn", b"yarn", "zk_hosts", b"zk_hosts"]) -> None: ...

global___PXFDatasourceHDFS = PXFDatasourceHDFS

@typing.final
class PXFDatasourceHive(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CORE_FIELD_NUMBER: builtins.int
    KERBEROS_FIELD_NUMBER: builtins.int
    USER_IMPERSONATION_FIELD_NUMBER: builtins.int
    USERNAME_FIELD_NUMBER: builtins.int
    SASL_CONNECTION_RETRIES_FIELD_NUMBER: builtins.int
    ZK_HOSTS_FIELD_NUMBER: builtins.int
    PPD_FIELD_NUMBER: builtins.int
    METASTORE_URIS_FIELD_NUMBER: builtins.int
    METASTORE_KERBEROS_PRINCIPAL_FIELD_NUMBER: builtins.int
    AUTH_KERBEROS_PRINCIPAL_FIELD_NUMBER: builtins.int
    username: builtins.str
    metastore_kerberos_principal: builtins.str
    auth_kerberos_principal: builtins.str
    @property
    def core(self) -> global___PXFDatasourceCore: ...
    @property
    def kerberos(self) -> global___PXFDatasourceKerberos: ...
    @property
    def user_impersonation(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def sasl_connection_retries(self) -> google.protobuf.wrappers_pb2.Int64Value: ...
    @property
    def zk_hosts(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def ppd(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def metastore_uris(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        core: global___PXFDatasourceCore | None = ...,
        kerberos: global___PXFDatasourceKerberos | None = ...,
        user_impersonation: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        username: builtins.str = ...,
        sasl_connection_retries: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        zk_hosts: collections.abc.Iterable[builtins.str] | None = ...,
        ppd: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        metastore_uris: collections.abc.Iterable[builtins.str] | None = ...,
        metastore_kerberos_principal: builtins.str = ...,
        auth_kerberos_principal: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["core", b"core", "kerberos", b"kerberos", "ppd", b"ppd", "sasl_connection_retries", b"sasl_connection_retries", "user_impersonation", b"user_impersonation"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["auth_kerberos_principal", b"auth_kerberos_principal", "core", b"core", "kerberos", b"kerberos", "metastore_kerberos_principal", b"metastore_kerberos_principal", "metastore_uris", b"metastore_uris", "ppd", b"ppd", "sasl_connection_retries", b"sasl_connection_retries", "user_impersonation", b"user_impersonation", "username", b"username", "zk_hosts", b"zk_hosts"]) -> None: ...

global___PXFDatasourceHive = PXFDatasourceHive

@typing.final
class PXFDatasource(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    S3_FIELD_NUMBER: builtins.int
    JDBC_FIELD_NUMBER: builtins.int
    HDFS_FIELD_NUMBER: builtins.int
    HIVE_FIELD_NUMBER: builtins.int
    name: builtins.str
    @property
    def s3(self) -> global___PXFDatasourceS3: ...
    @property
    def jdbc(self) -> global___PXFDatasourceJDBC: ...
    @property
    def hdfs(self) -> global___PXFDatasourceHDFS: ...
    @property
    def hive(self) -> global___PXFDatasourceHive: ...
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        s3: global___PXFDatasourceS3 | None = ...,
        jdbc: global___PXFDatasourceJDBC | None = ...,
        hdfs: global___PXFDatasourceHDFS | None = ...,
        hive: global___PXFDatasourceHive | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["hdfs", b"hdfs", "hive", b"hive", "jdbc", b"jdbc", "s3", b"s3", "settings", b"settings"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["hdfs", b"hdfs", "hive", b"hive", "jdbc", b"jdbc", "name", b"name", "s3", b"s3", "settings", b"settings"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["settings", b"settings"]) -> typing.Literal["s3", "jdbc", "hdfs", "hive"] | None: ...

global___PXFDatasource = PXFDatasource