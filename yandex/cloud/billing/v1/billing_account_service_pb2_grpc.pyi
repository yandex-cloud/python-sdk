"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.access.access_pb2
import yandex.cloud.billing.v1.billing_account_pb2
import yandex.cloud.billing.v1.billing_account_service_pb2
import yandex.cloud.operation.operation_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class BillingAccountServiceStub:
    """A set of methods for managing BillingAccount resources."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.billing.v1.billing_account_service_pb2.GetBillingAccountRequest,
        yandex.cloud.billing.v1.billing_account_pb2.BillingAccount,
    ]
    """Returns the specified billing account."""

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.billing.v1.billing_account_service_pb2.ListBillingAccountsRequest,
        yandex.cloud.billing.v1.billing_account_service_pb2.ListBillingAccountsResponse,
    ]
    """Retrieves the list of billing accounts available for current user."""

    ListBillableObjectBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.billing.v1.billing_account_service_pb2.ListBillableObjectBindingsRequest,
        yandex.cloud.billing.v1.billing_account_service_pb2.ListBillableObjectBindingsResponse,
    ]
    """Retrieves the list of billable object bindings associated with the specified billing account."""

    BindBillableObject: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.billing.v1.billing_account_service_pb2.BindBillableObjectRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Binds billable object to the specified billing account."""

    ListAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        yandex.cloud.access.access_pb2.ListAccessBindingsResponse,
    ]
    """Lists access bindings for the specified billing account."""

    UpdateAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates access bindings for the specified billing account."""

class BillingAccountServiceAsyncStub:
    """A set of methods for managing BillingAccount resources."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.billing.v1.billing_account_service_pb2.GetBillingAccountRequest,
        yandex.cloud.billing.v1.billing_account_pb2.BillingAccount,
    ]
    """Returns the specified billing account."""

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.billing.v1.billing_account_service_pb2.ListBillingAccountsRequest,
        yandex.cloud.billing.v1.billing_account_service_pb2.ListBillingAccountsResponse,
    ]
    """Retrieves the list of billing accounts available for current user."""

    ListBillableObjectBindings: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.billing.v1.billing_account_service_pb2.ListBillableObjectBindingsRequest,
        yandex.cloud.billing.v1.billing_account_service_pb2.ListBillableObjectBindingsResponse,
    ]
    """Retrieves the list of billable object bindings associated with the specified billing account."""

    BindBillableObject: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.billing.v1.billing_account_service_pb2.BindBillableObjectRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Binds billable object to the specified billing account."""

    ListAccessBindings: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        yandex.cloud.access.access_pb2.ListAccessBindingsResponse,
    ]
    """Lists access bindings for the specified billing account."""

    UpdateAccessBindings: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates access bindings for the specified billing account."""

class BillingAccountServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing BillingAccount resources."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.billing.v1.billing_account_service_pb2.GetBillingAccountRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.billing.v1.billing_account_pb2.BillingAccount, collections.abc.Awaitable[yandex.cloud.billing.v1.billing_account_pb2.BillingAccount]]:
        """Returns the specified billing account."""

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.billing.v1.billing_account_service_pb2.ListBillingAccountsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.billing.v1.billing_account_service_pb2.ListBillingAccountsResponse, collections.abc.Awaitable[yandex.cloud.billing.v1.billing_account_service_pb2.ListBillingAccountsResponse]]:
        """Retrieves the list of billing accounts available for current user."""

    @abc.abstractmethod
    def ListBillableObjectBindings(
        self,
        request: yandex.cloud.billing.v1.billing_account_service_pb2.ListBillableObjectBindingsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.billing.v1.billing_account_service_pb2.ListBillableObjectBindingsResponse, collections.abc.Awaitable[yandex.cloud.billing.v1.billing_account_service_pb2.ListBillableObjectBindingsResponse]]:
        """Retrieves the list of billable object bindings associated with the specified billing account."""

    @abc.abstractmethod
    def BindBillableObject(
        self,
        request: yandex.cloud.billing.v1.billing_account_service_pb2.BindBillableObjectRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Binds billable object to the specified billing account."""

    @abc.abstractmethod
    def ListAccessBindings(
        self,
        request: yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.access.access_pb2.ListAccessBindingsResponse, collections.abc.Awaitable[yandex.cloud.access.access_pb2.ListAccessBindingsResponse]]:
        """Lists access bindings for the specified billing account."""

    @abc.abstractmethod
    def UpdateAccessBindings(
        self,
        request: yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates access bindings for the specified billing account."""

def add_BillingAccountServiceServicer_to_server(servicer: BillingAccountServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
