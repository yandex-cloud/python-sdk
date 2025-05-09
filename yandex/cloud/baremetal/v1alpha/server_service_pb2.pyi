"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import yandex.cloud.baremetal.v1alpha.server_pb2
import yandex.cloud.baremetal.v1alpha.storage_pb2
import yandex.cloud.operation.operation_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetServerRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVER_ID_FIELD_NUMBER: builtins.int
    server_id: builtins.str
    """ID of the Server resource to return.

    To get the server ID, use a [ServerService.List] request.
    """
    def __init__(
        self,
        *,
        server_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["server_id", b"server_id"]) -> None: ...

global___GetServerRequest = GetServerRequest

@typing.final
class ListServerRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    ORDER_BY_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to list servers in.

    To get the folder ID, use a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is greater than `page_size`,
    the service returns a [ListServerResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value is 20.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set `page_token` to the
    [ListServerResponse.next_page_token] returned by a previous list request.
    """
    order_by: builtins.str
    """By which column the listing should be ordered and in which direction,
    format is "createdAt desc". "id asc" if omitted.
    Supported fields: ["id", "name", "createdAt"].
    Both snake_case and camelCase are supported for fields.
    """
    filter: builtins.str
    """A filter expression that filters resources listed in the response.
    The expression consists of one or more conditions united by `AND` operator: `<condition1> [AND <condition2> [<...> AND <conditionN>]]`.

    Each condition has the form `<field> <operator> <value>`, where:
    1. `<field>` is the field name. Currently you can use filtering only on the limited number of fields.
    2. `<operator>` is a logical operator, one of `=` (equal), `:` (substring).
    3. `<value>` represents a value.
    String values should be written in double (`"`) or single (`'`) quotes. C-style escape sequences are supported (`\\"` turns to `"`, `\\'` to `'`, `\\\\` to backslash).
    Example: "key1='value' AND key2='value'"
    Supported operators: ["AND"].
    Supported fields: ["id", "name", "zoneId", "hardwarePoolId"].
    Both snake_case and camelCase are supported for fields.
    """
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        order_by: builtins.str = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["filter", b"filter", "folder_id", b"folder_id", "order_by", b"order_by", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListServerRequest = ListServerRequest

@typing.final
class ListServerResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVERS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token for getting the next page of the list. If the number of results is greater than
    [ListServerRequest.page_size], use `next_page_token` as the value
    for the [ListServerRequest.page_token] parameter in the next list request.

    Each subsequent page will have its own `next_page_token` to continue paging through the results.
    """
    @property
    def servers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.baremetal.v1alpha.server_pb2.Server]:
        """List of Server resources."""

    def __init__(
        self,
        *,
        servers: collections.abc.Iterable[yandex.cloud.baremetal.v1alpha.server_pb2.Server] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "servers", b"servers"]) -> None: ...

global___ListServerResponse = ListServerResponse

@typing.final
class CreateServerRequest(google.protobuf.message.Message):
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

    FOLDER_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    HARDWARE_POOL_ID_FIELD_NUMBER: builtins.int
    CONFIGURATION_ID_FIELD_NUMBER: builtins.int
    RENTAL_PERIOD_ID_FIELD_NUMBER: builtins.int
    NETWORK_INTERFACES_FIELD_NUMBER: builtins.int
    OS_SETTINGS_SPEC_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to create server in.

    To get the folder ID, use a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    name: builtins.str
    """Name of the server.
    The name must be unique within the folder.
    """
    description: builtins.str
    """Description of the server."""
    hardware_pool_id: builtins.str
    """ID of the hardware pool that the server belongs to.

    To get the hardware pool ID, use a [HardwarePoolService.List] request.
    """
    configuration_id: builtins.str
    """ID of the configuration to use for the server.

    To get the configuration ID, use a [ConfigurationService.List] request.
    """
    rental_period_id: builtins.str
    """A period of time for which the server is rented."""
    @property
    def network_interfaces(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___NetworkInterfaceSpec]:
        """Network configuration for the server. Specifies how the network interface is configured
        to interact with other servers on the internal network and on the internet.
        Currently up to 2 network interfaces are supported: required private network interface and
        optional public network interface.
        """

    @property
    def os_settings_spec(self) -> global___OsSettingsSpec:
        """Operating system specific settings for provisioning the server. Optional, if omitted, the
        server will be created without an operating system.
        """

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `key:value` pairs."""

    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        hardware_pool_id: builtins.str = ...,
        configuration_id: builtins.str = ...,
        rental_period_id: builtins.str = ...,
        network_interfaces: collections.abc.Iterable[global___NetworkInterfaceSpec] | None = ...,
        os_settings_spec: global___OsSettingsSpec | None = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["os_settings_spec", b"os_settings_spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["configuration_id", b"configuration_id", "description", b"description", "folder_id", b"folder_id", "hardware_pool_id", b"hardware_pool_id", "labels", b"labels", "name", b"name", "network_interfaces", b"network_interfaces", "os_settings_spec", b"os_settings_spec", "rental_period_id", b"rental_period_id"]) -> None: ...

global___CreateServerRequest = CreateServerRequest

@typing.final
class CreateServerMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVER_ID_FIELD_NUMBER: builtins.int
    server_id: builtins.str
    """ID of the server that is being created."""
    def __init__(
        self,
        *,
        server_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["server_id", b"server_id"]) -> None: ...

global___CreateServerMetadata = CreateServerMetadata

@typing.final
class UpdateServerRequest(google.protobuf.message.Message):
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

    SERVER_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    NETWORK_INTERFACES_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    server_id: builtins.str
    """ID of the server to update.

    To get the server ID, use a [ServerService.List] request.
    """
    name: builtins.str
    """Name of the server.
    The name must be unique within the folder.
    """
    description: builtins.str
    """Description of the server."""
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which fields of the Server resource are going to be updated."""

    @property
    def network_interfaces(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___NetworkInterfaceSpec]:
        """Network configuration for the server. Specifies how the network interface is configured
        to interact with other servers on the internal network and on the internet.
        Currently up to 2 network interfaces are supported: required private network interface and
        optional public network interface.
        """

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `key:value` pairs."""

    def __init__(
        self,
        *,
        server_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        network_interfaces: collections.abc.Iterable[global___NetworkInterfaceSpec] | None = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "labels", b"labels", "name", b"name", "network_interfaces", b"network_interfaces", "server_id", b"server_id", "update_mask", b"update_mask"]) -> None: ...

global___UpdateServerRequest = UpdateServerRequest

@typing.final
class NetworkInterfaceSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    PRIVATE_SUBNET_FIELD_NUMBER: builtins.int
    PUBLIC_SUBNET_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the network interface. Should not be specified when creating a server."""
    @property
    def private_subnet(self) -> yandex.cloud.baremetal.v1alpha.server_pb2.PrivateSubnetNetworkInterface:
        """Private subnet."""

    @property
    def public_subnet(self) -> yandex.cloud.baremetal.v1alpha.server_pb2.PublicSubnetNetworkInterface:
        """Public subnet."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        private_subnet: yandex.cloud.baremetal.v1alpha.server_pb2.PrivateSubnetNetworkInterface | None = ...,
        public_subnet: yandex.cloud.baremetal.v1alpha.server_pb2.PublicSubnetNetworkInterface | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["private_subnet", b"private_subnet", "public_subnet", b"public_subnet", "subnet", b"subnet"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["id", b"id", "private_subnet", b"private_subnet", "public_subnet", b"public_subnet", "subnet", b"subnet"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["subnet", b"subnet"]) -> typing.Literal["private_subnet", "public_subnet"] | None: ...

global___NetworkInterfaceSpec = NetworkInterfaceSpec

@typing.final
class UpdateServerMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVER_ID_FIELD_NUMBER: builtins.int
    server_id: builtins.str
    """ID of the Server resource that is being updated."""
    def __init__(
        self,
        *,
        server_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["server_id", b"server_id"]) -> None: ...

global___UpdateServerMetadata = UpdateServerMetadata

@typing.final
class DeleteServerRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVER_ID_FIELD_NUMBER: builtins.int
    server_id: builtins.str
    """ID of the server to delete.

    To get the server ID, use a [ServerService.List] request.
    """
    def __init__(
        self,
        *,
        server_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["server_id", b"server_id"]) -> None: ...

global___DeleteServerRequest = DeleteServerRequest

@typing.final
class DeleteServerMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVER_ID_FIELD_NUMBER: builtins.int
    server_id: builtins.str
    """ID of the Server resource that is being deleted."""
    def __init__(
        self,
        *,
        server_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["server_id", b"server_id"]) -> None: ...

global___DeleteServerMetadata = DeleteServerMetadata

@typing.final
class PowerOffServerRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVER_ID_FIELD_NUMBER: builtins.int
    server_id: builtins.str
    """ID of the server to power off.

    To get the server ID, use a [ServerService.List] request.
    """
    def __init__(
        self,
        *,
        server_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["server_id", b"server_id"]) -> None: ...

global___PowerOffServerRequest = PowerOffServerRequest

@typing.final
class PowerOffServerMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVER_ID_FIELD_NUMBER: builtins.int
    server_id: builtins.str
    """ID of the Server resource that is being powered off."""
    def __init__(
        self,
        *,
        server_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["server_id", b"server_id"]) -> None: ...

global___PowerOffServerMetadata = PowerOffServerMetadata

@typing.final
class PowerOnServerRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVER_ID_FIELD_NUMBER: builtins.int
    server_id: builtins.str
    """ID of the server to power on.

    To get the server ID, use a [ServerService.List] request.
    """
    def __init__(
        self,
        *,
        server_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["server_id", b"server_id"]) -> None: ...

global___PowerOnServerRequest = PowerOnServerRequest

@typing.final
class PowerOnServerMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVER_ID_FIELD_NUMBER: builtins.int
    server_id: builtins.str
    """ID of the Server resource that is being powered on."""
    def __init__(
        self,
        *,
        server_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["server_id", b"server_id"]) -> None: ...

global___PowerOnServerMetadata = PowerOnServerMetadata

@typing.final
class RebootServerRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVER_ID_FIELD_NUMBER: builtins.int
    server_id: builtins.str
    """ID of the server to reboot.

    To get the server ID, use a [ServerService.List] request.
    """
    def __init__(
        self,
        *,
        server_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["server_id", b"server_id"]) -> None: ...

global___RebootServerRequest = RebootServerRequest

@typing.final
class RebootServerMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVER_ID_FIELD_NUMBER: builtins.int
    server_id: builtins.str
    """ID of the Server resource that is being rebooted."""
    def __init__(
        self,
        *,
        server_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["server_id", b"server_id"]) -> None: ...

global___RebootServerMetadata = RebootServerMetadata

@typing.final
class ReinstallServerRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVER_ID_FIELD_NUMBER: builtins.int
    OS_SETTINGS_SPEC_FIELD_NUMBER: builtins.int
    server_id: builtins.str
    """ID of the server to reinstall.

    To get the server ID, use a [ServerService.List] request.
    """
    @property
    def os_settings_spec(self) -> global___OsSettingsSpec:
        """Operating system specific settings for provisioning the server."""

    def __init__(
        self,
        *,
        server_id: builtins.str = ...,
        os_settings_spec: global___OsSettingsSpec | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["os_settings_spec", b"os_settings_spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["os_settings_spec", b"os_settings_spec", "server_id", b"server_id"]) -> None: ...

global___ReinstallServerRequest = ReinstallServerRequest

@typing.final
class ReinstallServerMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVER_ID_FIELD_NUMBER: builtins.int
    server_id: builtins.str
    """ID of the Server resource that is being reinstalled."""
    def __init__(
        self,
        *,
        server_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["server_id", b"server_id"]) -> None: ...

global___ReinstallServerMetadata = ReinstallServerMetadata

@typing.final
class ListServerOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    server_id: builtins.str
    """ID of the Server resource to list operations for."""
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is greater than `page_size`,
    the service returns a [ListServerOperationsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value is 20.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set `page_token` to the
    [ListServerOperationsResponse.next_page_token] returned by a previous list request.
    """
    def __init__(
        self,
        *,
        server_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["page_size", b"page_size", "page_token", b"page_token", "server_id", b"server_id"]) -> None: ...

global___ListServerOperationsRequest = ListServerOperationsRequest

@typing.final
class ListServerOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token for getting the next page of the list. If the number of results is greater than
    [ListServerOperationsRequest.page_size], use `next_page_token` as the value
    for the [ListServerOperationsRequest.page_token] parameter in the next list request.

    Each subsequent page will have its own `next_page_token` to continue paging through the results.
    """
    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.operation.operation_pb2.Operation]:
        """List of operations for the specified Server resource."""

    def __init__(
        self,
        *,
        operations: collections.abc.Iterable[yandex.cloud.operation.operation_pb2.Operation] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "operations", b"operations"]) -> None: ...

global___ListServerOperationsResponse = ListServerOperationsResponse

@typing.final
class BatchCreateServersRequest(google.protobuf.message.Message):
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

    FOLDER_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    HARDWARE_POOL_ID_FIELD_NUMBER: builtins.int
    CONFIGURATION_ID_FIELD_NUMBER: builtins.int
    RENTAL_PERIOD_ID_FIELD_NUMBER: builtins.int
    NETWORK_INTERFACES_FIELD_NUMBER: builtins.int
    OS_SETTINGS_SPEC_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    COUNT_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to list images in.

    To get the folder ID, use a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    name: builtins.str
    """Name of the server.
    The name must be unique within the folder.
    """
    description: builtins.str
    """Description of the server."""
    hardware_pool_id: builtins.str
    """ID of the hardware pool that the server belongs to.

    To get the hardware pool ID, use a [HardwarePoolService.List] request.
    """
    configuration_id: builtins.str
    """ID of the configuration to use for the server.

    To get the configuration ID, use a [ConfigurationService.List] request.
    """
    rental_period_id: builtins.str
    """A period of time for which the server is rented."""
    count: builtins.int
    """Number of servers to create."""
    @property
    def network_interfaces(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___NetworkInterfaceSpec]:
        """Network configuration for the server. Specifies how the network interface is configured
        to interact with other servers on the internal network and on the internet.
        Currently up to 2 network interfaces are supported: required private network interface and
        optional public network interface.
        """

    @property
    def os_settings_spec(self) -> global___OsSettingsSpec:
        """Operating system specific settings for provisioning the server. Optional, if omitted, the
        server will be created without an operating system.
        """

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `key:value` pairs."""

    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        hardware_pool_id: builtins.str = ...,
        configuration_id: builtins.str = ...,
        rental_period_id: builtins.str = ...,
        network_interfaces: collections.abc.Iterable[global___NetworkInterfaceSpec] | None = ...,
        os_settings_spec: global___OsSettingsSpec | None = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        count: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["os_settings_spec", b"os_settings_spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["configuration_id", b"configuration_id", "count", b"count", "description", b"description", "folder_id", b"folder_id", "hardware_pool_id", b"hardware_pool_id", "labels", b"labels", "name", b"name", "network_interfaces", b"network_interfaces", "os_settings_spec", b"os_settings_spec", "rental_period_id", b"rental_period_id"]) -> None: ...

global___BatchCreateServersRequest = BatchCreateServersRequest

@typing.final
class BatchCreateServersResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVERS_FIELD_NUMBER: builtins.int
    @property
    def servers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.baremetal.v1alpha.server_pb2.Server]:
        """List of Server resources that were created."""

    def __init__(
        self,
        *,
        servers: collections.abc.Iterable[yandex.cloud.baremetal.v1alpha.server_pb2.Server] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["servers", b"servers"]) -> None: ...

global___BatchCreateServersResponse = BatchCreateServersResponse

@typing.final
class BatchCreateServersMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVER_IDS_FIELD_NUMBER: builtins.int
    @property
    def server_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """IDs of the servers that were created."""

    def __init__(
        self,
        *,
        server_ids: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["server_ids", b"server_ids"]) -> None: ...

global___BatchCreateServersMetadata = BatchCreateServersMetadata

@typing.final
class QuarantineServerMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVER_ID_FIELD_NUMBER: builtins.int
    server_id: builtins.str
    """ID of the server that is being quarantined."""
    def __init__(
        self,
        *,
        server_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["server_id", b"server_id"]) -> None: ...

global___QuarantineServerMetadata = QuarantineServerMetadata

@typing.final
class StartProlongationRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVER_ID_FIELD_NUMBER: builtins.int
    server_id: builtins.str
    """ID of the server that is being prolonged."""
    def __init__(
        self,
        *,
        server_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["server_id", b"server_id"]) -> None: ...

global___StartProlongationRequest = StartProlongationRequest

@typing.final
class StopProlongationRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVER_ID_FIELD_NUMBER: builtins.int
    server_id: builtins.str
    """ID of the server to stop prolongation for.

    To get the server ID, use a [ServerService.List] request.
    """
    def __init__(
        self,
        *,
        server_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["server_id", b"server_id"]) -> None: ...

global___StopProlongationRequest = StopProlongationRequest

@typing.final
class ServerSetProlongationMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVER_ID_FIELD_NUMBER: builtins.int
    server_id: builtins.str
    """ID of the server for which the prolongation is being set."""
    def __init__(
        self,
        *,
        server_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["server_id", b"server_id"]) -> None: ...

global___ServerSetProlongationMetadata = ServerSetProlongationMetadata

@typing.final
class OsSettingsSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IMAGE_ID_FIELD_NUMBER: builtins.int
    STORAGES_FIELD_NUMBER: builtins.int
    SSH_PUBLIC_KEY_FIELD_NUMBER: builtins.int
    USER_SSH_ID_FIELD_NUMBER: builtins.int
    PASSWORD_PLAIN_TEXT_FIELD_NUMBER: builtins.int
    PASSWORD_LOCKBOX_SECRET_FIELD_NUMBER: builtins.int
    image_id: builtins.str
    """ID of the image that the server was created from."""
    ssh_public_key: builtins.str
    """Public SSH key for the server."""
    user_ssh_id: builtins.str
    """ID of the user SSH key to use for the server.

    To get the user SSH key ID, use a [yandex.cloud.organizationmanager.v1.UserSshKeyService.List] request.
    """
    password_plain_text: builtins.str
    """Raw password."""
    @property
    def storages(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.baremetal.v1alpha.storage_pb2.Storage]:
        """List of storages to be created on the server. If not specified, the default value based on the
        selected configuration will be used as the field value.
        """

    @property
    def password_lockbox_secret(self) -> global___LockboxSecret:
        """Reference to the Lockbox secret used to obtain the password."""

    def __init__(
        self,
        *,
        image_id: builtins.str = ...,
        storages: collections.abc.Iterable[yandex.cloud.baremetal.v1alpha.storage_pb2.Storage] | None = ...,
        ssh_public_key: builtins.str = ...,
        user_ssh_id: builtins.str = ...,
        password_plain_text: builtins.str = ...,
        password_lockbox_secret: global___LockboxSecret | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["password", b"password", "password_lockbox_secret", b"password_lockbox_secret", "password_plain_text", b"password_plain_text", "ssh_key", b"ssh_key", "ssh_public_key", b"ssh_public_key", "user_ssh_id", b"user_ssh_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["image_id", b"image_id", "password", b"password", "password_lockbox_secret", b"password_lockbox_secret", "password_plain_text", b"password_plain_text", "ssh_key", b"ssh_key", "ssh_public_key", b"ssh_public_key", "storages", b"storages", "user_ssh_id", b"user_ssh_id"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["password", b"password"]) -> typing.Literal["password_plain_text", "password_lockbox_secret"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["ssh_key", b"ssh_key"]) -> typing.Literal["ssh_public_key", "user_ssh_id"] | None: ...

global___OsSettingsSpec = OsSettingsSpec

@typing.final
class LockboxSecret(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SECRET_ID_FIELD_NUMBER: builtins.int
    VERSION_ID_FIELD_NUMBER: builtins.int
    KEY_FIELD_NUMBER: builtins.int
    secret_id: builtins.str
    """The unique identifier for the lockbox secret that contains the user password."""
    version_id: builtins.str
    """The unique identifier for the lockbox version.
    If omitted, the current version of the secret will be used.
    """
    key: builtins.str
    """The key used to access a specific secret entry."""
    def __init__(
        self,
        *,
        secret_id: builtins.str = ...,
        version_id: builtins.str = ...,
        key: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["key", b"key", "secret_id", b"secret_id", "version_id", b"version_id"]) -> None: ...

global___LockboxSecret = LockboxSecret
