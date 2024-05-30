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

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Template(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _State:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Template._State.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATE_UNSPECIFIED: Template._State.ValueType  # 0
        PENDING: Template._State.ValueType  # 1
        """Subscription template created but not active yet."""
        ACTIVE: Template._State.ValueType  # 2
        """Subscription template is active."""
        DEPRECATED: Template._State.ValueType  # 3
        """Subscription template deprecated."""
        DELETED: Template._State.ValueType  # 4
        """Subscription template deleted."""

    class State(_State, metaclass=_StateEnumTypeWrapper): ...
    STATE_UNSPECIFIED: Template.State.ValueType  # 0
    PENDING: Template.State.ValueType  # 1
    """Subscription template created but not active yet."""
    ACTIVE: Template.State.ValueType  # 2
    """Subscription template is active."""
    DEPRECATED: Template.State.ValueType  # 3
    """Subscription template deprecated."""
    DELETED: Template.State.ValueType  # 4
    """Subscription template deleted."""

    ID_FIELD_NUMBER: builtins.int
    VERSION_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    PUBLISHER_ID_FIELD_NUMBER: builtins.int
    PRODUCT_ID_FIELD_NUMBER: builtins.int
    TARIFF_ID_FIELD_NUMBER: builtins.int
    LICENSE_SKU_ID_FIELD_NUMBER: builtins.int
    PERIOD_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    UPDATED_AT_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the subscription template."""
    version_id: builtins.str
    """Version of the subscription template."""
    name: builtins.str
    """Name of the subscription template."""
    publisher_id: builtins.str
    """ID of publisher."""
    product_id: builtins.str
    """ID of product."""
    tariff_id: builtins.str
    """ID of tariff."""
    license_sku_id: builtins.str
    """ID of subscription SKU."""
    period: builtins.str
    """Subscription period."""
    state: global___Template.State.ValueType
    """Subscription template state."""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp."""

    @property
    def updated_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Update timestamp."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        version_id: builtins.str = ...,
        name: builtins.str = ...,
        publisher_id: builtins.str = ...,
        product_id: builtins.str = ...,
        tariff_id: builtins.str = ...,
        license_sku_id: builtins.str = ...,
        period: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        updated_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        state: global___Template.State.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at", "updated_at", b"updated_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["created_at", b"created_at", "id", b"id", "license_sku_id", b"license_sku_id", "name", b"name", "period", b"period", "product_id", b"product_id", "publisher_id", b"publisher_id", "state", b"state", "tariff_id", b"tariff_id", "updated_at", b"updated_at", "version_id", b"version_id"]) -> None: ...

global___Template = Template
