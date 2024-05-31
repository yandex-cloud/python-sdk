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
import yandex.cloud.iot.devices.v1.device_pb2
import yandex.cloud.operation.operation_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetDeviceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEVICE_ID_FIELD_NUMBER: builtins.int
    DEVICE_VIEW_FIELD_NUMBER: builtins.int
    device_id: builtins.str
    """ID of the device to return.

    To get a device ID make a [DeviceService.List] request.
    """
    device_view: yandex.cloud.iot.devices.v1.device_pb2.DeviceView.ValueType
    """Specifies which parts of the device resource should be returned
    in the response.
    """
    def __init__(
        self,
        *,
        device_id: builtins.str = ...,
        device_view: yandex.cloud.iot.devices.v1.device_pb2.DeviceView.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["device_id", b"device_id", "device_view", b"device_view"]) -> None: ...

global___GetDeviceRequest = GetDeviceRequest

@typing.final
class GetByNameDeviceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REGISTRY_ID_FIELD_NUMBER: builtins.int
    DEVICE_NAME_FIELD_NUMBER: builtins.int
    DEVICE_VIEW_FIELD_NUMBER: builtins.int
    registry_id: builtins.str
    """ID of the registry to get device.

    To get a registry ID make a [yandex.cloud.iot.devices.v1.RegistryService.List] request.
    """
    device_name: builtins.str
    """Name of the device to return.

    To get a device name make a [DeviceService.List] request.
    """
    device_view: yandex.cloud.iot.devices.v1.device_pb2.DeviceView.ValueType
    """Specifies which parts of the device resource should be returned
    in the response.
    """
    def __init__(
        self,
        *,
        registry_id: builtins.str = ...,
        device_name: builtins.str = ...,
        device_view: yandex.cloud.iot.devices.v1.device_pb2.DeviceView.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["device_name", b"device_name", "device_view", b"device_view", "registry_id", b"registry_id"]) -> None: ...

global___GetByNameDeviceRequest = GetByNameDeviceRequest

@typing.final
class ListDevicesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REGISTRY_ID_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    DEVICE_VIEW_FIELD_NUMBER: builtins.int
    registry_id: builtins.str
    """ID of the registry to list devices in.

    To get a registry ID make a [yandex.cloud.iot.devices.v1.RegistryService.List] request.
    """
    folder_id: builtins.str
    """ID of the folder to list devices in.

    To get a folder ID make a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than `page_size`, the service returns a [ListDevicesResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set `page_token` to the
    [ListDevicesResponse.next_page_token] returned by a previous list request.
    """
    device_view: yandex.cloud.iot.devices.v1.device_pb2.DeviceView.ValueType
    """Specifies which parts of the device resource should be returned
    in the response.
    """
    def __init__(
        self,
        *,
        registry_id: builtins.str = ...,
        folder_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        device_view: yandex.cloud.iot.devices.v1.device_pb2.DeviceView.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["folder_id", b"folder_id", "id", b"id", "registry_id", b"registry_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["device_view", b"device_view", "folder_id", b"folder_id", "id", b"id", "page_size", b"page_size", "page_token", b"page_token", "registry_id", b"registry_id"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["id", b"id"]) -> typing.Literal["registry_id", "folder_id"] | None: ...

global___ListDevicesRequest = ListDevicesRequest

@typing.final
class ListDevicesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEVICES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token for getting the next page of the list. If the number of results is greater than
    the specified [ListDevicesRequest.page_size], use `next_page_token` as the value
    for the [ListDevicesRequest.page_token] parameter in the next list request.

    Each subsequent page will have its own `next_page_token` to continue paging through the results.
    """
    @property
    def devices(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.iot.devices.v1.device_pb2.Device]:
        """List of devices."""

    def __init__(
        self,
        *,
        devices: collections.abc.Iterable[yandex.cloud.iot.devices.v1.device_pb2.Device] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["devices", b"devices", "next_page_token", b"next_page_token"]) -> None: ...

global___ListDevicesResponse = ListDevicesResponse

@typing.final
class CreateDeviceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class TopicAliasesEntry(google.protobuf.message.Message):
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
    class Certificate(google.protobuf.message.Message):
        """Specification of a device certificate."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        CERTIFICATE_DATA_FIELD_NUMBER: builtins.int
        certificate_data: builtins.str
        """Public part of the device certificate."""
        def __init__(
            self,
            *,
            certificate_data: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["certificate_data", b"certificate_data"]) -> None: ...

    REGISTRY_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    CERTIFICATES_FIELD_NUMBER: builtins.int
    TOPIC_ALIASES_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    registry_id: builtins.str
    """ID of the registry to create a device in.

    To get a registry ID, make a [yandex.cloud.iot.devices.v1.RegistryService.List] request.
    """
    name: builtins.str
    """Name of the device. The name must be unique within the registry."""
    description: builtins.str
    """Description of the device."""
    password: builtins.str
    """Device password.

    The password must contain at least three character categories among the following: upper case latin, lower case latin, numbers and special symbols.
    """
    @property
    def certificates(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CreateDeviceRequest.Certificate]:
        """Device certificate."""

    @property
    def topic_aliases(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Alias of a device topic.

        Alias is an alternate name of a device topic assigned by the user. Map alias to canonical topic name prefix, e.g. `my/custom/alias` match to `$device/{id}/events`.
        """

    def __init__(
        self,
        *,
        registry_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        certificates: collections.abc.Iterable[global___CreateDeviceRequest.Certificate] | None = ...,
        topic_aliases: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        password: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["certificates", b"certificates", "description", b"description", "name", b"name", "password", b"password", "registry_id", b"registry_id", "topic_aliases", b"topic_aliases"]) -> None: ...

global___CreateDeviceRequest = CreateDeviceRequest

@typing.final
class CreateDeviceMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEVICE_ID_FIELD_NUMBER: builtins.int
    device_id: builtins.str
    """ID of the device that is being created."""
    def __init__(
        self,
        *,
        device_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["device_id", b"device_id"]) -> None: ...

global___CreateDeviceMetadata = CreateDeviceMetadata

@typing.final
class UpdateDeviceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class TopicAliasesEntry(google.protobuf.message.Message):
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

    DEVICE_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    TOPIC_ALIASES_FIELD_NUMBER: builtins.int
    device_id: builtins.str
    """ID of the device to update.

    To get a device ID make a [DeviceService.List] request.
    """
    name: builtins.str
    """Name of the device. The name must be unique within the registry."""
    description: builtins.str
    """Description of the device."""
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which fields of the device are going to be updated."""

    @property
    def topic_aliases(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Alias of a device topic.

        Alias is an alternate name of a device topic assigned by the user. Map alias to canonical topic name prefix, e.g. `my/custom/alias` match to `$device/{id}/events`.
        """

    def __init__(
        self,
        *,
        device_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        topic_aliases: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "device_id", b"device_id", "name", b"name", "topic_aliases", b"topic_aliases", "update_mask", b"update_mask"]) -> None: ...

global___UpdateDeviceRequest = UpdateDeviceRequest

@typing.final
class UpdateDeviceMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEVICE_ID_FIELD_NUMBER: builtins.int
    device_id: builtins.str
    """ID of the device that is being updated."""
    def __init__(
        self,
        *,
        device_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["device_id", b"device_id"]) -> None: ...

global___UpdateDeviceMetadata = UpdateDeviceMetadata

@typing.final
class DeleteDeviceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEVICE_ID_FIELD_NUMBER: builtins.int
    device_id: builtins.str
    """ID of the device to delete.

    To get a device ID make a [DeviceService.List] request.
    """
    def __init__(
        self,
        *,
        device_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["device_id", b"device_id"]) -> None: ...

global___DeleteDeviceRequest = DeleteDeviceRequest

@typing.final
class DeleteDeviceMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEVICE_ID_FIELD_NUMBER: builtins.int
    device_id: builtins.str
    """ID of the device that is being deleted."""
    def __init__(
        self,
        *,
        device_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["device_id", b"device_id"]) -> None: ...

global___DeleteDeviceMetadata = DeleteDeviceMetadata

@typing.final
class ListDeviceCertificatesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEVICE_ID_FIELD_NUMBER: builtins.int
    device_id: builtins.str
    """ID of the device to list certificates for."""
    def __init__(
        self,
        *,
        device_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["device_id", b"device_id"]) -> None: ...

global___ListDeviceCertificatesRequest = ListDeviceCertificatesRequest

@typing.final
class ListDeviceCertificatesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CERTIFICATES_FIELD_NUMBER: builtins.int
    @property
    def certificates(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.iot.devices.v1.device_pb2.DeviceCertificate]:
        """List of certificates for the specified device."""

    def __init__(
        self,
        *,
        certificates: collections.abc.Iterable[yandex.cloud.iot.devices.v1.device_pb2.DeviceCertificate] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["certificates", b"certificates"]) -> None: ...

global___ListDeviceCertificatesResponse = ListDeviceCertificatesResponse

@typing.final
class AddDeviceCertificateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEVICE_ID_FIELD_NUMBER: builtins.int
    CERTIFICATE_DATA_FIELD_NUMBER: builtins.int
    device_id: builtins.str
    """ID of the device for which the certificate is being added.

    To get a device ID make a [DeviceService.List] request.
    """
    certificate_data: builtins.str
    """Public part of the certificate."""
    def __init__(
        self,
        *,
        device_id: builtins.str = ...,
        certificate_data: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["certificate_data", b"certificate_data", "device_id", b"device_id"]) -> None: ...

global___AddDeviceCertificateRequest = AddDeviceCertificateRequest

@typing.final
class AddDeviceCertificateMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEVICE_ID_FIELD_NUMBER: builtins.int
    FINGERPRINT_FIELD_NUMBER: builtins.int
    device_id: builtins.str
    """ID of the device certificate that is being added."""
    fingerprint: builtins.str
    """Fingerprint of the certificate that is being added."""
    def __init__(
        self,
        *,
        device_id: builtins.str = ...,
        fingerprint: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["device_id", b"device_id", "fingerprint", b"fingerprint"]) -> None: ...

global___AddDeviceCertificateMetadata = AddDeviceCertificateMetadata

@typing.final
class DeleteDeviceCertificateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEVICE_ID_FIELD_NUMBER: builtins.int
    FINGERPRINT_FIELD_NUMBER: builtins.int
    device_id: builtins.str
    """ID of the device to delete a certificate for.

    To get a device ID make a [DeviceService.List] request.
    """
    fingerprint: builtins.str
    """Fingerprint of the certificate to delete."""
    def __init__(
        self,
        *,
        device_id: builtins.str = ...,
        fingerprint: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["device_id", b"device_id", "fingerprint", b"fingerprint"]) -> None: ...

global___DeleteDeviceCertificateRequest = DeleteDeviceCertificateRequest

@typing.final
class DeleteDeviceCertificateMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEVICE_ID_FIELD_NUMBER: builtins.int
    FINGERPRINT_FIELD_NUMBER: builtins.int
    device_id: builtins.str
    """ID of the device certificate that is being deleted."""
    fingerprint: builtins.str
    """Fingerprint of the certificate that is being deleted."""
    def __init__(
        self,
        *,
        device_id: builtins.str = ...,
        fingerprint: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["device_id", b"device_id", "fingerprint", b"fingerprint"]) -> None: ...

global___DeleteDeviceCertificateMetadata = DeleteDeviceCertificateMetadata

@typing.final
class ListDevicePasswordsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEVICE_ID_FIELD_NUMBER: builtins.int
    device_id: builtins.str
    """ID of the registry to list passwords in.

    To get a registry ID make a [RegistryService.List] request.
    """
    def __init__(
        self,
        *,
        device_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["device_id", b"device_id"]) -> None: ...

global___ListDevicePasswordsRequest = ListDevicePasswordsRequest

@typing.final
class ListDevicePasswordsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PASSWORDS_FIELD_NUMBER: builtins.int
    @property
    def passwords(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.iot.devices.v1.device_pb2.DevicePassword]:
        """List of passwords for the specified device."""

    def __init__(
        self,
        *,
        passwords: collections.abc.Iterable[yandex.cloud.iot.devices.v1.device_pb2.DevicePassword] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["passwords", b"passwords"]) -> None: ...

global___ListDevicePasswordsResponse = ListDevicePasswordsResponse

@typing.final
class AddDevicePasswordRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEVICE_ID_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    device_id: builtins.str
    """ID of the device to add a password for.

    To get a device ID make a [DeviceService.List] request.
    """
    password: builtins.str
    """Passwords for the device.

    The password must contain at least three character categories among the following: upper case latin, lower case latin, numbers and special symbols.
    """
    def __init__(
        self,
        *,
        device_id: builtins.str = ...,
        password: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["device_id", b"device_id", "password", b"password"]) -> None: ...

global___AddDevicePasswordRequest = AddDevicePasswordRequest

@typing.final
class AddDevicePasswordMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEVICE_ID_FIELD_NUMBER: builtins.int
    PASSWORD_ID_FIELD_NUMBER: builtins.int
    device_id: builtins.str
    """ID of the device for which the password is being added."""
    password_id: builtins.str
    """ID of the password that is being added."""
    def __init__(
        self,
        *,
        device_id: builtins.str = ...,
        password_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["device_id", b"device_id", "password_id", b"password_id"]) -> None: ...

global___AddDevicePasswordMetadata = AddDevicePasswordMetadata

@typing.final
class DeleteDevicePasswordRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEVICE_ID_FIELD_NUMBER: builtins.int
    PASSWORD_ID_FIELD_NUMBER: builtins.int
    device_id: builtins.str
    """ID of the device to delete a password for.

    To get a device ID make a [DeviceService.List] request.
    """
    password_id: builtins.str
    """ID of the password to delete.

    To get a password ID make a [DeviceService.ListPasswords] request.
    """
    def __init__(
        self,
        *,
        device_id: builtins.str = ...,
        password_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["device_id", b"device_id", "password_id", b"password_id"]) -> None: ...

global___DeleteDevicePasswordRequest = DeleteDevicePasswordRequest

@typing.final
class DeleteDevicePasswordMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEVICE_ID_FIELD_NUMBER: builtins.int
    PASSWORD_ID_FIELD_NUMBER: builtins.int
    device_id: builtins.str
    """ID of the device for which the password is being deleted."""
    password_id: builtins.str
    """ID of the password that is being deleted."""
    def __init__(
        self,
        *,
        device_id: builtins.str = ...,
        password_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["device_id", b"device_id", "password_id", b"password_id"]) -> None: ...

global___DeleteDevicePasswordMetadata = DeleteDevicePasswordMetadata

@typing.final
class ListDeviceOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEVICE_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    device_id: builtins.str
    """ID of the device to list operations for.

    To get a device ID make a [DeviceService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page that should be returned. If the number of available
    results is larger than `page_size`, the service returns a [ListDeviceOperationsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set `page_token` to the
    [ListDeviceOperationsResponse.next_page_token] returned by a previous list request.
    """
    filter: builtins.str
    """A filter expression that filters resources listed in the response.
    Currently you can use filtering only on [Device.name] field.
    """
    def __init__(
        self,
        *,
        device_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["device_id", b"device_id", "filter", b"filter", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListDeviceOperationsRequest = ListDeviceOperationsRequest

@typing.final
class ListDeviceOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token for getting the next page of the list. If the number of results is greater than
    the specified [ListDeviceOperationsRequest.page_size], use `next_page_token` as the value
    for the [ListDeviceOperationsRequest.page_token] parameter in the next list request.

    Each subsequent page will have its own `next_page_token` to continue paging through the results.
    """
    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.operation.operation_pb2.Operation]:
        """List of operations for the specified device certificate."""

    def __init__(
        self,
        *,
        operations: collections.abc.Iterable[yandex.cloud.operation.operation_pb2.Operation] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "operations", b"operations"]) -> None: ...

global___ListDeviceOperationsResponse = ListDeviceOperationsResponse