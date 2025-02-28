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
import google.protobuf.wrappers_pb2
import typing
import yandex.cloud.cic.v1.common.transceiver_type_pb2
import yandex.cloud.cic.v1.trunk_connection_pb2
import yandex.cloud.operation.operation_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetTrunkConnectionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TRUNK_CONNECTION_ID_FIELD_NUMBER: builtins.int
    trunk_connection_id: builtins.str
    """ID of the TrunkConnection resource to return.
    To get the trunkConnection ID use a [TrunkConnectionService.List] request.
    """
    def __init__(
        self,
        *,
        trunk_connection_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["trunk_connection_id", b"trunk_connection_id"]) -> None: ...

global___GetTrunkConnectionRequest = GetTrunkConnectionRequest

@typing.final
class ListTrunkConnectionsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to list TrunkConnection resources.
    To get the folder ID use a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListTrunkConnectionsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests. Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token] to the
    [ListTrunkConnectionsResponse.next_page_token] returned by a previous list request.
    """
    filter: builtins.str
    """A filter expression that filters resources listed in the response.
    The expression must specify:
    1. The field name. Currently you can use filtering only on [Subnet.name] field.
    2. An `=` operator.
    3. The value in double quotes (`"`). Must be 3-63 characters long and match the regular expression `[a-z][-a-z0-9]{1,61}[a-z0-9]`.
    """
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["filter", b"filter", "folder_id", b"folder_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListTrunkConnectionsRequest = ListTrunkConnectionsRequest

@typing.final
class ListTrunkConnectionsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TRUNK_CONNECTIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListTrunkConnectionsRequest.page_size], use
    the [next_page_token] as the value
    for the [ListTrunkConnectionsRequest.page_token] query parameter
    in the next list request. Subsequent list requests will have their own
    [next_page_token] to continue paging through the results.
    """
    @property
    def trunk_connections(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.cic.v1.trunk_connection_pb2.TrunkConnection]:
        """List of TrunkConnection resources."""

    def __init__(
        self,
        *,
        trunk_connections: collections.abc.Iterable[yandex.cloud.cic.v1.trunk_connection_pb2.TrunkConnection] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "trunk_connections", b"trunk_connections"]) -> None: ...

global___ListTrunkConnectionsResponse = ListTrunkConnectionsResponse

@typing.final
class CreateTrunkConnectionRequest(google.protobuf.message.Message):
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

    @typing.final
    class SinglePortDirectJoint(google.protobuf.message.Message):
        """Config of trunkConnection that is deployed on single port."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TRANSCEIVER_TYPE_FIELD_NUMBER: builtins.int
        transceiver_type: yandex.cloud.cic.v1.common.transceiver_type_pb2.TransceiverType.ValueType
        """Type of transceiver that the trunkConnection is deployed on."""
        def __init__(
            self,
            *,
            transceiver_type: yandex.cloud.cic.v1.common.transceiver_type_pb2.TransceiverType.ValueType = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["transceiver_type", b"transceiver_type"]) -> None: ...

    @typing.final
    class LagDirectJoint(google.protobuf.message.Message):
        """Config of trunkConnection that is deployed on lag."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TRANSCEIVER_TYPE_FIELD_NUMBER: builtins.int
        transceiver_type: yandex.cloud.cic.v1.common.transceiver_type_pb2.TransceiverType.ValueType
        """Type of transceiver that the trunkConnection is deployed on."""
        def __init__(
            self,
            *,
            transceiver_type: yandex.cloud.cic.v1.common.transceiver_type_pb2.TransceiverType.ValueType = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["transceiver_type", b"transceiver_type"]) -> None: ...

    @typing.final
    class PartnerJoint(google.protobuf.message.Message):
        """Config of trunkConnection that is deployed on partner joint."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        PARTNER_ID_FIELD_NUMBER: builtins.int
        @property
        def partner_id(self) -> google.protobuf.wrappers_pb2.StringValue:
            """ID of partner that the trunkConnection is deployed on.
            Optional.
            If is not set scheduler selects it by himself.
            """

        def __init__(
            self,
            *,
            partner_id: google.protobuf.wrappers_pb2.StringValue | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["partner_id", b"partner_id"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["partner_id", b"partner_id"]) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    REGION_ID_FIELD_NUMBER: builtins.int
    SINGLE_PORT_DIRECT_JOINT_FIELD_NUMBER: builtins.int
    LAG_DIRECT_JOINT_FIELD_NUMBER: builtins.int
    PARTNER_JOINT_INFO_FIELD_NUMBER: builtins.int
    POINT_OF_PRESENCE_ID_FIELD_NUMBER: builtins.int
    CAPACITY_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    DELETION_PROTECTION_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the trunkConnection.
    The name must be unique within the folder.
    Value must match the regular expression ``\\|[a-zA-Z]([-_a-zA-Z0-9]{0,61}[a-zA-Z0-9])?``.
    """
    description: builtins.str
    """Optional description of the trunkConnection. 0-256 characters long."""
    folder_id: builtins.str
    """ID of the folder that the trunkConnection belongs to."""
    region_id: builtins.str
    """ID of the region that the trunkConnection belongs to."""
    capacity: yandex.cloud.cic.v1.trunk_connection_pb2.TrunkConnection.Capacity.ValueType
    """Capacity of the trunkConnection"""
    deletion_protection: builtins.bool
    """Deletion protection flag.
    Optional.
    If set prohibits deletion of the trunkConnection.
    """
    @property
    def single_port_direct_joint(self) -> global___CreateTrunkConnectionRequest.SinglePortDirectJoint: ...
    @property
    def lag_direct_joint(self) -> global___CreateTrunkConnectionRequest.LagDirectJoint: ...
    @property
    def partner_joint_info(self) -> global___CreateTrunkConnectionRequest.PartnerJoint: ...
    @property
    def point_of_presence_id(self) -> google.protobuf.wrappers_pb2.StringValue:
        """ID of pointOfPresence that the trunkConnection is deployed on.
        Optional.
        If is not set scheduler selects it by himself.
        """

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels, `key:value` pairs.
        No more than 64 per resource.
        The maximum string length in characters for each value is 63.
        Each value must match the regular expression `[-_0-9a-z]*`.
        The string length in characters for each key must be 1-63.
        Each key must match the regular expression `[a-z][-_0-9a-z]*`.
        """

    def __init__(
        self,
        *,
        name: builtins.str = ...,
        description: builtins.str = ...,
        folder_id: builtins.str = ...,
        region_id: builtins.str = ...,
        single_port_direct_joint: global___CreateTrunkConnectionRequest.SinglePortDirectJoint | None = ...,
        lag_direct_joint: global___CreateTrunkConnectionRequest.LagDirectJoint | None = ...,
        partner_joint_info: global___CreateTrunkConnectionRequest.PartnerJoint | None = ...,
        point_of_presence_id: google.protobuf.wrappers_pb2.StringValue | None = ...,
        capacity: yandex.cloud.cic.v1.trunk_connection_pb2.TrunkConnection.Capacity.ValueType = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        deletion_protection: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["joint", b"joint", "lag_direct_joint", b"lag_direct_joint", "partner_joint_info", b"partner_joint_info", "point_of_presence_id", b"point_of_presence_id", "single_port_direct_joint", b"single_port_direct_joint"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["capacity", b"capacity", "deletion_protection", b"deletion_protection", "description", b"description", "folder_id", b"folder_id", "joint", b"joint", "labels", b"labels", "lag_direct_joint", b"lag_direct_joint", "name", b"name", "partner_joint_info", b"partner_joint_info", "point_of_presence_id", b"point_of_presence_id", "region_id", b"region_id", "single_port_direct_joint", b"single_port_direct_joint"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["joint", b"joint"]) -> typing.Literal["single_port_direct_joint", "lag_direct_joint", "partner_joint_info"] | None: ...

global___CreateTrunkConnectionRequest = CreateTrunkConnectionRequest

@typing.final
class CreateTrunkConnectionMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TRUNK_CONNECTION_ID_FIELD_NUMBER: builtins.int
    trunk_connection_id: builtins.str
    """ID of the TrunkConnection resource."""
    def __init__(
        self,
        *,
        trunk_connection_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["trunk_connection_id", b"trunk_connection_id"]) -> None: ...

global___CreateTrunkConnectionMetadata = CreateTrunkConnectionMetadata

@typing.final
class UpdateTrunkConnectionRequest(google.protobuf.message.Message):
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

    TRUNK_CONNECTION_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    REGION_ID_FIELD_NUMBER: builtins.int
    POINT_OF_PRESENCE_ID_FIELD_NUMBER: builtins.int
    CAPACITY_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    DELETION_PROTECTION_FIELD_NUMBER: builtins.int
    trunk_connection_id: builtins.str
    """ID of the TrunkConnection resource to return."""
    name: builtins.str
    """Name of the trunkConnection.
    The name must be unique within the folder.
    Value must match the regular expression ``\\|[a-zA-Z]([-_a-zA-Z0-9]{0,61}[a-zA-Z0-9])?``.
    """
    description: builtins.str
    """Optional description of the trunkConnection. 0-256 characters long."""
    region_id: builtins.str
    """ID of the region that the trunkConnection belongs to."""
    capacity: yandex.cloud.cic.v1.trunk_connection_pb2.TrunkConnection.Capacity.ValueType
    """Capacity of the trunkConnection"""
    deletion_protection: builtins.bool
    """Deletion protection flag.
    Optional.
    If set prohibits deletion of the trunkConnection.
    """
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which fields of the TrunkConnection resource are going to be updated."""

    @property
    def point_of_presence_id(self) -> google.protobuf.wrappers_pb2.StringValue:
        """ID of pointOfPresence that the trunkConnection is deployed on.
        Optional.
        If is not set scheduler selects it by himself.
        """

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels, `key:value` pairs.
        No more than 64 per resource.
        The maximum string length in characters for each value is 63.
        Each value must match the regular expression `[-_0-9a-z]*`.
        The string length in characters for each key must be 1-63.
        Each key must match the regular expression `[a-z][-_0-9a-z]*`.
        """

    def __init__(
        self,
        *,
        trunk_connection_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        region_id: builtins.str = ...,
        point_of_presence_id: google.protobuf.wrappers_pb2.StringValue | None = ...,
        capacity: yandex.cloud.cic.v1.trunk_connection_pb2.TrunkConnection.Capacity.ValueType = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        deletion_protection: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["point_of_presence_id", b"point_of_presence_id", "update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["capacity", b"capacity", "deletion_protection", b"deletion_protection", "description", b"description", "labels", b"labels", "name", b"name", "point_of_presence_id", b"point_of_presence_id", "region_id", b"region_id", "trunk_connection_id", b"trunk_connection_id", "update_mask", b"update_mask"]) -> None: ...

global___UpdateTrunkConnectionRequest = UpdateTrunkConnectionRequest

@typing.final
class UpdateTrunkConnectionMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TRUNK_CONNECTION_ID_FIELD_NUMBER: builtins.int
    trunk_connection_id: builtins.str
    """ID of the TrunkConnection resource."""
    def __init__(
        self,
        *,
        trunk_connection_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["trunk_connection_id", b"trunk_connection_id"]) -> None: ...

global___UpdateTrunkConnectionMetadata = UpdateTrunkConnectionMetadata

@typing.final
class DeleteTrunkConnectionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TRUNK_CONNECTION_ID_FIELD_NUMBER: builtins.int
    trunk_connection_id: builtins.str
    """ID of the TrunkConnection resource."""
    def __init__(
        self,
        *,
        trunk_connection_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["trunk_connection_id", b"trunk_connection_id"]) -> None: ...

global___DeleteTrunkConnectionRequest = DeleteTrunkConnectionRequest

@typing.final
class DeleteTrunkConnectionMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TRUNK_CONNECTION_ID_FIELD_NUMBER: builtins.int
    trunk_connection_id: builtins.str
    """ID of the TrunkConnection resource."""
    def __init__(
        self,
        *,
        trunk_connection_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["trunk_connection_id", b"trunk_connection_id"]) -> None: ...

global___DeleteTrunkConnectionMetadata = DeleteTrunkConnectionMetadata

@typing.final
class ListTrunkConnectionOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TRUNK_CONNECTION_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    trunk_connection_id: builtins.str
    """ID of the TrunkConnection resource."""
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListTrunkConnectionOperationsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests. Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token] to the
    [ListTrunkConnectionOperationsResponse.next_page_token] returned by a previous list request.
    """
    def __init__(
        self,
        *,
        trunk_connection_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["page_size", b"page_size", "page_token", b"page_token", "trunk_connection_id", b"trunk_connection_id"]) -> None: ...

global___ListTrunkConnectionOperationsRequest = ListTrunkConnectionOperationsRequest

@typing.final
class ListTrunkConnectionOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListTrunkConnectionOperationsRequest.page_size], use
    the [next_page_token] as the value
    for the [ListTrunkConnectionOperationsRequest.page_token] query parameter
    in the next list request. Subsequent list requests will have their own
    [next_page_token] to continue paging through the results.
    """
    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.operation.operation_pb2.Operation]:
        """List of TrunkConnection operations."""

    def __init__(
        self,
        *,
        operations: collections.abc.Iterable[yandex.cloud.operation.operation_pb2.Operation] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "operations", b"operations"]) -> None: ...

global___ListTrunkConnectionOperationsResponse = ListTrunkConnectionOperationsResponse
