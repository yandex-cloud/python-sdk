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
import yandex.cloud.iot.broker.v1.broker_pb2
import yandex.cloud.operation.operation_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetBrokerRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BROKER_ID_FIELD_NUMBER: builtins.int
    broker_id: builtins.str
    """ID of the broker to return.

    To get a broker ID make a [BrokerService.List] request.
    """
    def __init__(
        self,
        *,
        broker_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["broker_id", b"broker_id"]) -> None: ...

global___GetBrokerRequest = GetBrokerRequest

@typing.final
class ListBrokersRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to list brokers in.

    To get a folder ID make a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page that should be returned. If the number of available
    results is larger than `page_size`, the service returns a [ListBrokersResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set `page_token` to the
    [ListBrokersResponse.next_page_token] returned by a previous list request.
    """
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["folder_id", b"folder_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListBrokersRequest = ListBrokersRequest

@typing.final
class ListBrokersResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BROKERS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token for getting the next page of the list. If the number of results is greater than
    the specified [ListBrokersRequest.page_size], use `next_page_token` as the value
    for the [ListBrokersRequest.page_token] parameter in the next list request.

    Each subsequent page will have its own `next_page_token` to continue paging through the results.
    """
    @property
    def brokers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.iot.broker.v1.broker_pb2.Broker]:
        """List of brokers."""

    def __init__(
        self,
        *,
        brokers: collections.abc.Iterable[yandex.cloud.iot.broker.v1.broker_pb2.Broker] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["brokers", b"brokers", "next_page_token", b"next_page_token"]) -> None: ...

global___ListBrokersResponse = ListBrokersResponse

@typing.final
class CreateBrokerRequest(google.protobuf.message.Message):
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
    class Certificate(google.protobuf.message.Message):
        """Specification of a broker certificate."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        CERTIFICATE_DATA_FIELD_NUMBER: builtins.int
        certificate_data: builtins.str
        """Public part of the broker certificate."""
        def __init__(
            self,
            *,
            certificate_data: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["certificate_data", b"certificate_data"]) -> None: ...

    FOLDER_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    CERTIFICATES_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    LOG_OPTIONS_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to create a broker in.

    To get a folder ID, make a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    name: builtins.str
    """Name of the broker. The name must be unique within the folder."""
    description: builtins.str
    """Description of the broker."""
    password: builtins.str
    """Broker passwords.

    The password must contain at least three character categories among the following: upper case latin, lower case latin, numbers and special symbols.
    """
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `key:value` pairs."""

    @property
    def certificates(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CreateBrokerRequest.Certificate]:
        """Broker certificates."""

    @property
    def log_options(self) -> yandex.cloud.iot.broker.v1.broker_pb2.LogOptions:
        """Options for logging broker events"""

    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        certificates: collections.abc.Iterable[global___CreateBrokerRequest.Certificate] | None = ...,
        password: builtins.str = ...,
        log_options: yandex.cloud.iot.broker.v1.broker_pb2.LogOptions | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["log_options", b"log_options"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["certificates", b"certificates", "description", b"description", "folder_id", b"folder_id", "labels", b"labels", "log_options", b"log_options", "name", b"name", "password", b"password"]) -> None: ...

global___CreateBrokerRequest = CreateBrokerRequest

@typing.final
class CreateBrokerMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BROKER_ID_FIELD_NUMBER: builtins.int
    broker_id: builtins.str
    """ID of the broker that is being created."""
    def __init__(
        self,
        *,
        broker_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["broker_id", b"broker_id"]) -> None: ...

global___CreateBrokerMetadata = CreateBrokerMetadata

@typing.final
class UpdateBrokerRequest(google.protobuf.message.Message):
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

    BROKER_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    LOG_OPTIONS_FIELD_NUMBER: builtins.int
    broker_id: builtins.str
    """ID of the broker to update.

    To get a broker ID make a [BrokerService.List] request.
    """
    name: builtins.str
    """Name of the broker. The name must be unique within the folder."""
    description: builtins.str
    """Description of the broker."""
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which fields of the broker are going to be updated."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `key:value` pairs.

        Existing set of `labels` is completely replaced by the provided set.
        """

    @property
    def log_options(self) -> yandex.cloud.iot.broker.v1.broker_pb2.LogOptions:
        """Options for logging broker events"""

    def __init__(
        self,
        *,
        broker_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        log_options: yandex.cloud.iot.broker.v1.broker_pb2.LogOptions | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["log_options", b"log_options", "update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["broker_id", b"broker_id", "description", b"description", "labels", b"labels", "log_options", b"log_options", "name", b"name", "update_mask", b"update_mask"]) -> None: ...

global___UpdateBrokerRequest = UpdateBrokerRequest

@typing.final
class UpdateBrokerMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BROKER_ID_FIELD_NUMBER: builtins.int
    broker_id: builtins.str
    """ID of the broker that is being updated."""
    def __init__(
        self,
        *,
        broker_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["broker_id", b"broker_id"]) -> None: ...

global___UpdateBrokerMetadata = UpdateBrokerMetadata

@typing.final
class DeleteBrokerRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BROKER_ID_FIELD_NUMBER: builtins.int
    broker_id: builtins.str
    """ID of the broker to delete.

    To get a broker ID make a [BrokerService.List] request.
    """
    def __init__(
        self,
        *,
        broker_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["broker_id", b"broker_id"]) -> None: ...

global___DeleteBrokerRequest = DeleteBrokerRequest

@typing.final
class DeleteBrokerMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BROKER_ID_FIELD_NUMBER: builtins.int
    broker_id: builtins.str
    """ID of the broker that is being deleted."""
    def __init__(
        self,
        *,
        broker_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["broker_id", b"broker_id"]) -> None: ...

global___DeleteBrokerMetadata = DeleteBrokerMetadata

@typing.final
class ListBrokerCertificatesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BROKER_ID_FIELD_NUMBER: builtins.int
    broker_id: builtins.str
    """ID of the broker to list certificates for."""
    def __init__(
        self,
        *,
        broker_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["broker_id", b"broker_id"]) -> None: ...

global___ListBrokerCertificatesRequest = ListBrokerCertificatesRequest

@typing.final
class ListBrokerCertificatesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CERTIFICATES_FIELD_NUMBER: builtins.int
    @property
    def certificates(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.iot.broker.v1.broker_pb2.BrokerCertificate]:
        """List of certificates for the specified broker."""

    def __init__(
        self,
        *,
        certificates: collections.abc.Iterable[yandex.cloud.iot.broker.v1.broker_pb2.BrokerCertificate] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["certificates", b"certificates"]) -> None: ...

global___ListBrokerCertificatesResponse = ListBrokerCertificatesResponse

@typing.final
class AddBrokerCertificateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BROKER_ID_FIELD_NUMBER: builtins.int
    CERTIFICATE_DATA_FIELD_NUMBER: builtins.int
    broker_id: builtins.str
    """ID of the broker for which the certificate is being added.

    To get a broker ID make a [BrokerService.List] request.
    """
    certificate_data: builtins.str
    """Public part of the certificate that is being added."""
    def __init__(
        self,
        *,
        broker_id: builtins.str = ...,
        certificate_data: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["broker_id", b"broker_id", "certificate_data", b"certificate_data"]) -> None: ...

global___AddBrokerCertificateRequest = AddBrokerCertificateRequest

@typing.final
class AddBrokerCertificateMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BROKER_ID_FIELD_NUMBER: builtins.int
    FINGERPRINT_FIELD_NUMBER: builtins.int
    broker_id: builtins.str
    """ID of the broker certificate that is being added."""
    fingerprint: builtins.str
    """Fingerprint of the certificate that is being added."""
    def __init__(
        self,
        *,
        broker_id: builtins.str = ...,
        fingerprint: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["broker_id", b"broker_id", "fingerprint", b"fingerprint"]) -> None: ...

global___AddBrokerCertificateMetadata = AddBrokerCertificateMetadata

@typing.final
class DeleteBrokerCertificateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BROKER_ID_FIELD_NUMBER: builtins.int
    FINGERPRINT_FIELD_NUMBER: builtins.int
    broker_id: builtins.str
    """ID of the broker to delete a certificate for.

    To get a broker ID make a [BrokerService.List] request.
    """
    fingerprint: builtins.str
    """Fingerprint of the certificate that is being deleted."""
    def __init__(
        self,
        *,
        broker_id: builtins.str = ...,
        fingerprint: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["broker_id", b"broker_id", "fingerprint", b"fingerprint"]) -> None: ...

global___DeleteBrokerCertificateRequest = DeleteBrokerCertificateRequest

@typing.final
class DeleteBrokerCertificateMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BROKER_ID_FIELD_NUMBER: builtins.int
    FINGERPRINT_FIELD_NUMBER: builtins.int
    broker_id: builtins.str
    """ID of a broker for which the certificate is being delete."""
    fingerprint: builtins.str
    """Fingerprint of the certificate to deleted."""
    def __init__(
        self,
        *,
        broker_id: builtins.str = ...,
        fingerprint: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["broker_id", b"broker_id", "fingerprint", b"fingerprint"]) -> None: ...

global___DeleteBrokerCertificateMetadata = DeleteBrokerCertificateMetadata

@typing.final
class ListBrokerPasswordsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BROKER_ID_FIELD_NUMBER: builtins.int
    broker_id: builtins.str
    """ID of the broker to list passwords in.

    To get a broker ID make a [BrokerService.List] request.
    """
    def __init__(
        self,
        *,
        broker_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["broker_id", b"broker_id"]) -> None: ...

global___ListBrokerPasswordsRequest = ListBrokerPasswordsRequest

@typing.final
class ListBrokerPasswordsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PASSWORDS_FIELD_NUMBER: builtins.int
    @property
    def passwords(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.iot.broker.v1.broker_pb2.BrokerPassword]:
        """List of passwords for the specified broker."""

    def __init__(
        self,
        *,
        passwords: collections.abc.Iterable[yandex.cloud.iot.broker.v1.broker_pb2.BrokerPassword] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["passwords", b"passwords"]) -> None: ...

global___ListBrokerPasswordsResponse = ListBrokerPasswordsResponse

@typing.final
class AddBrokerPasswordRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BROKER_ID_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    broker_id: builtins.str
    """ID of the broker to add a password for.

    To get a broker ID make a [BrokerService.List] request.
    """
    password: builtins.str
    """Passwords for the broker.

    The password must contain at least three character categories among the following: upper case latin, lower case latin, numbers and special symbols.
    """
    def __init__(
        self,
        *,
        broker_id: builtins.str = ...,
        password: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["broker_id", b"broker_id", "password", b"password"]) -> None: ...

global___AddBrokerPasswordRequest = AddBrokerPasswordRequest

@typing.final
class AddBrokerPasswordMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BROKER_ID_FIELD_NUMBER: builtins.int
    PASSWORD_ID_FIELD_NUMBER: builtins.int
    broker_id: builtins.str
    """ID of the broker for which the password is being added."""
    password_id: builtins.str
    """ID of a password that is being added."""
    def __init__(
        self,
        *,
        broker_id: builtins.str = ...,
        password_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["broker_id", b"broker_id", "password_id", b"password_id"]) -> None: ...

global___AddBrokerPasswordMetadata = AddBrokerPasswordMetadata

@typing.final
class DeleteBrokerPasswordRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BROKER_ID_FIELD_NUMBER: builtins.int
    PASSWORD_ID_FIELD_NUMBER: builtins.int
    broker_id: builtins.str
    """ID of the broker to delete a password for.

    To get a broker ID make a [BrokerService.List] request.
    """
    password_id: builtins.str
    """ID of the password to delete.

    To get a password ID make a [BrokerService.ListPasswords] request.
    """
    def __init__(
        self,
        *,
        broker_id: builtins.str = ...,
        password_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["broker_id", b"broker_id", "password_id", b"password_id"]) -> None: ...

global___DeleteBrokerPasswordRequest = DeleteBrokerPasswordRequest

@typing.final
class DeleteBrokerPasswordMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BROKER_ID_FIELD_NUMBER: builtins.int
    PASSWORD_ID_FIELD_NUMBER: builtins.int
    broker_id: builtins.str
    """ID of a broker for which the password is being delete."""
    password_id: builtins.str
    """ID of the password to delete.

    To get a password ID make a [BrokerService.ListPasswords] request.
    """
    def __init__(
        self,
        *,
        broker_id: builtins.str = ...,
        password_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["broker_id", b"broker_id", "password_id", b"password_id"]) -> None: ...

global___DeleteBrokerPasswordMetadata = DeleteBrokerPasswordMetadata

@typing.final
class ListBrokerOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BROKER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    broker_id: builtins.str
    """ID of the broker to list operations for."""
    page_size: builtins.int
    """The maximum number of results per page that should be returned. If the number of available
    results is larger than `page_size`, the service returns a [ListBrokerOperationsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set `page_token` to the
    [ListBrokerOperationsResponse.next_page_token] returned by a previous list request.
    """
    filter: builtins.str
    """A filter expression that filters resources listed in the response.
    Currently you can use filtering only on [Broker.name] field.
    """
    def __init__(
        self,
        *,
        broker_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["broker_id", b"broker_id", "filter", b"filter", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListBrokerOperationsRequest = ListBrokerOperationsRequest

@typing.final
class ListBrokerOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token for getting the next page of the list. If the number of results is greater than
    the specified [ListBrokerOperationsRequest.page_size], use `next_page_token` as the value
    for the [ListBrokerOperationsRequest.page_token] parameter in the next list request.

    Each subsequent page will have its own `next_page_token` to continue paging through the results.
    """
    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.operation.operation_pb2.Operation]:
        """List of operations for the specified broker."""

    def __init__(
        self,
        *,
        operations: collections.abc.Iterable[yandex.cloud.operation.operation_pb2.Operation] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "operations", b"operations"]) -> None: ...

global___ListBrokerOperationsResponse = ListBrokerOperationsResponse
