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
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class CloudApplication(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[CloudApplication._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: CloudApplication._Status.ValueType  # 0
        PROCESSING: CloudApplication._Status.ValueType  # 1
        """Application under deploying / updating /deleting"""
        DEPLOYED: CloudApplication._Status.ValueType  # 2
        """Application successfully deployed to YC"""
        FAILED: CloudApplication._Status.ValueType  # 3
        """Application failed to deploy"""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...
    STATUS_UNSPECIFIED: CloudApplication.Status.ValueType  # 0
    PROCESSING: CloudApplication.Status.ValueType  # 1
    """Application under deploying / updating /deleting"""
    DEPLOYED: CloudApplication.Status.ValueType  # 2
    """Application successfully deployed to YC"""
    FAILED: CloudApplication.Status.ValueType  # 3
    """Application failed to deploy"""

    @typing.final
    class Billing(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        class _BillingType:
            ValueType = typing.NewType("ValueType", builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _BillingTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[CloudApplication.Billing._BillingType.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            BILLING_TYPE_UNSPECIFIED: CloudApplication.Billing._BillingType.ValueType  # 0
            PAY_AS_YOU_GO: CloudApplication.Billing._BillingType.ValueType  # 1
            """User pays for application usage time"""
            SUBSCRIPTION: CloudApplication.Billing._BillingType.ValueType  # 2
            """User bought a subscription"""

        class BillingType(_BillingType, metaclass=_BillingTypeEnumTypeWrapper): ...
        BILLING_TYPE_UNSPECIFIED: CloudApplication.Billing.BillingType.ValueType  # 0
        PAY_AS_YOU_GO: CloudApplication.Billing.BillingType.ValueType  # 1
        """User pays for application usage time"""
        SUBSCRIPTION: CloudApplication.Billing.BillingType.ValueType  # 2
        """User bought a subscription"""

        @typing.final
        class Subscription(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            INSTANCE_ID_FIELD_NUMBER: builtins.int
            TEMPLATE_ID_FIELD_NUMBER: builtins.int
            instance_id: builtins.str
            """Identifier of subscription instance"""
            template_id: builtins.str
            """Subscription template identifier"""
            def __init__(
                self,
                *,
                instance_id: builtins.str = ...,
                template_id: builtins.str = ...,
            ) -> None: ...
            def ClearField(self, field_name: typing.Literal["instance_id", b"instance_id", "template_id", b"template_id"]) -> None: ...

        TYPE_FIELD_NUMBER: builtins.int
        SUBSCRIPTIONS_FIELD_NUMBER: builtins.int
        type: global___CloudApplication.Billing.BillingType.ValueType
        """Type of application billing"""
        @property
        def subscriptions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CloudApplication.Billing.Subscription]:
            """Subscriptions bounded to cloud application"""

        def __init__(
            self,
            *,
            type: global___CloudApplication.Billing.BillingType.ValueType = ...,
            subscriptions: collections.abc.Iterable[global___CloudApplication.Billing.Subscription] | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["subscriptions", b"subscriptions", "type", b"type"]) -> None: ...

    ID_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    BILLING_FIELD_NUMBER: builtins.int
    id: builtins.str
    """Application Identifier"""
    status: global___CloudApplication.Status.ValueType
    """Application Status"""
    @property
    def billing(self) -> global___CloudApplication.Billing:
        """Application billing info"""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        status: global___CloudApplication.Status.ValueType = ...,
        billing: global___CloudApplication.Billing | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["billing", b"billing"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["billing", b"billing", "id", b"id", "status", b"status"]) -> None: ...

global___CloudApplication = CloudApplication
