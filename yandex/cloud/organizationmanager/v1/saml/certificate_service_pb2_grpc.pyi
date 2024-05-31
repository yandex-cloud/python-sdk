"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.operation.operation_pb2
import yandex.cloud.organizationmanager.v1.saml.certificate_pb2
import yandex.cloud.organizationmanager.v1.saml.certificate_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class CertificateServiceStub:
    """A set of methods for managing certificates."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.organizationmanager.v1.saml.certificate_service_pb2.GetCertificateRequest,
        yandex.cloud.organizationmanager.v1.saml.certificate_pb2.Certificate,
    ]
    """Returns the specified certificate.

    To get the list of available certificates, make a [List] request.
    """

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.organizationmanager.v1.saml.certificate_service_pb2.ListCertificatesRequest,
        yandex.cloud.organizationmanager.v1.saml.certificate_service_pb2.ListCertificatesResponse,
    ]
    """Retrieves the list of certificates in the specified federation."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.organizationmanager.v1.saml.certificate_service_pb2.CreateCertificateRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a certificate in the specified federation."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.organizationmanager.v1.saml.certificate_service_pb2.UpdateCertificateRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified certificate."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.organizationmanager.v1.saml.certificate_service_pb2.DeleteCertificateRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified certificate."""

    ListOperations: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.organizationmanager.v1.saml.certificate_service_pb2.ListCertificateOperationsRequest,
        yandex.cloud.organizationmanager.v1.saml.certificate_service_pb2.ListCertificateOperationsResponse,
    ]
    """Lists operations for the specified certificate."""

class CertificateServiceAsyncStub:
    """A set of methods for managing certificates."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.organizationmanager.v1.saml.certificate_service_pb2.GetCertificateRequest,
        yandex.cloud.organizationmanager.v1.saml.certificate_pb2.Certificate,
    ]
    """Returns the specified certificate.

    To get the list of available certificates, make a [List] request.
    """

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.organizationmanager.v1.saml.certificate_service_pb2.ListCertificatesRequest,
        yandex.cloud.organizationmanager.v1.saml.certificate_service_pb2.ListCertificatesResponse,
    ]
    """Retrieves the list of certificates in the specified federation."""

    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.organizationmanager.v1.saml.certificate_service_pb2.CreateCertificateRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a certificate in the specified federation."""

    Update: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.organizationmanager.v1.saml.certificate_service_pb2.UpdateCertificateRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified certificate."""

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.organizationmanager.v1.saml.certificate_service_pb2.DeleteCertificateRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified certificate."""

    ListOperations: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.organizationmanager.v1.saml.certificate_service_pb2.ListCertificateOperationsRequest,
        yandex.cloud.organizationmanager.v1.saml.certificate_service_pb2.ListCertificateOperationsResponse,
    ]
    """Lists operations for the specified certificate."""

class CertificateServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing certificates."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.organizationmanager.v1.saml.certificate_service_pb2.GetCertificateRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.organizationmanager.v1.saml.certificate_pb2.Certificate, collections.abc.Awaitable[yandex.cloud.organizationmanager.v1.saml.certificate_pb2.Certificate]]:
        """Returns the specified certificate.

        To get the list of available certificates, make a [List] request.
        """

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.organizationmanager.v1.saml.certificate_service_pb2.ListCertificatesRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.organizationmanager.v1.saml.certificate_service_pb2.ListCertificatesResponse, collections.abc.Awaitable[yandex.cloud.organizationmanager.v1.saml.certificate_service_pb2.ListCertificatesResponse]]:
        """Retrieves the list of certificates in the specified federation."""

    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.organizationmanager.v1.saml.certificate_service_pb2.CreateCertificateRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates a certificate in the specified federation."""

    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.organizationmanager.v1.saml.certificate_service_pb2.UpdateCertificateRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates the specified certificate."""

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.organizationmanager.v1.saml.certificate_service_pb2.DeleteCertificateRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deletes the specified certificate."""

    @abc.abstractmethod
    def ListOperations(
        self,
        request: yandex.cloud.organizationmanager.v1.saml.certificate_service_pb2.ListCertificateOperationsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.organizationmanager.v1.saml.certificate_service_pb2.ListCertificateOperationsResponse, collections.abc.Awaitable[yandex.cloud.organizationmanager.v1.saml.certificate_service_pb2.ListCertificateOperationsResponse]]:
        """Lists operations for the specified certificate."""

def add_CertificateServiceServicer_to_server(servicer: CertificateServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
