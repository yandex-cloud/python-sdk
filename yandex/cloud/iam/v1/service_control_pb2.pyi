"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys
import typing
import yandex.cloud.iam.v1.resource_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Service(google.protobuf.message.Message):
    """A Service."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Service._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: Service._Status.ValueType  # 0
        ENABLED: Service._Status.ValueType  # 1
        """The service is enabled."""
        PAUSED: Service._Status.ValueType  # 2
        """The service is paused."""
        DISABLED: Service._Status.ValueType  # 3
        """The service is disabled."""
        ENABLING: Service._Status.ValueType  # 4
        """The service is being enabled."""
        RESUMING: Service._Status.ValueType  # 5
        """The service is being resumed."""
        PAUSING: Service._Status.ValueType  # 6
        """The service is being paused."""
        DISABLING: Service._Status.ValueType  # 7
        """The service is being disabled."""
        ERROR: Service._Status.ValueType  # 8
        """The service is in error state."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...
    STATUS_UNSPECIFIED: Service.Status.ValueType  # 0
    ENABLED: Service.Status.ValueType  # 1
    """The service is enabled."""
    PAUSED: Service.Status.ValueType  # 2
    """The service is paused."""
    DISABLED: Service.Status.ValueType  # 3
    """The service is disabled."""
    ENABLING: Service.Status.ValueType  # 4
    """The service is being enabled."""
    RESUMING: Service.Status.ValueType  # 5
    """The service is being resumed."""
    PAUSING: Service.Status.ValueType  # 6
    """The service is being paused."""
    DISABLING: Service.Status.ValueType  # 7
    """The service is being disabled."""
    ERROR: Service.Status.ValueType  # 8
    """The service is in error state."""

    SERVICE_ID_FIELD_NUMBER: builtins.int
    RESOURCE_FIELD_NUMBER: builtins.int
    UPDATED_AT_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    service_id: builtins.str
    """ID of the service."""
    status: global___Service.Status.ValueType
    """Current status of the service."""
    @property
    def resource(self) -> yandex.cloud.iam.v1.resource_pb2.Resource:
        """Resource that the service belongs to."""

    @property
    def updated_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time of the last status update of the service."""

    def __init__(
        self,
        *,
        service_id: builtins.str = ...,
        resource: yandex.cloud.iam.v1.resource_pb2.Resource | None = ...,
        updated_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        status: global___Service.Status.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["resource", b"resource", "updated_at", b"updated_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["resource", b"resource", "service_id", b"service_id", "status", b"status", "updated_at", b"updated_at"]) -> None: ...

global___Service = Service

@typing.final
class ServiceAgent(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVICE_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    SERVICE_ID_FIELD_NUMBER: builtins.int
    MICROSERVICE_ID_FIELD_NUMBER: builtins.int
    service_account_id: builtins.str
    """ID of the agent service account."""
    service_id: builtins.str
    """ID of the service."""
    microservice_id: builtins.str
    """ID of the microservice."""
    def __init__(
        self,
        *,
        service_account_id: builtins.str = ...,
        service_id: builtins.str = ...,
        microservice_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["microservice_id", b"microservice_id", "service_account_id", b"service_account_id", "service_id", b"service_id"]) -> None: ...

global___ServiceAgent = ServiceAgent
