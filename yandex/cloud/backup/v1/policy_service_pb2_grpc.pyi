"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.backup.v1.policy_pb2
import yandex.cloud.backup.v1.policy_service_pb2
import yandex.cloud.operation.operation_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class PolicyServiceStub:
    """A set of methods for managing [policies](/docs/backup/concepts/policy)."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.backup.v1.policy_service_pb2.ListPoliciesRequest,
        yandex.cloud.backup.v1.policy_service_pb2.ListPoliciesResponse,
    ]
    """List [policies](/docs/backup/concepts/policy) of specified folder."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.backup.v1.policy_service_pb2.CreatePolicyRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Create a new policy.

    For detailed information, please see [Creating a backup policy](/docs/backup/operations/policy-vm/create).
    """

    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.backup.v1.policy_service_pb2.GetPolicyRequest,
        yandex.cloud.backup.v1.policy_pb2.Policy,
    ]
    """Get specific policy."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.backup.v1.policy_service_pb2.UpdatePolicyRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Update specific policy."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.backup.v1.policy_service_pb2.DeletePolicyRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Delete specific policy."""

    Apply: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.backup.v1.policy_service_pb2.ApplyPolicyRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Apply policy to [Compute Cloud instance](/docs/backup/concepts/vm-connection#os)."""

    ListApplications: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.backup.v1.policy_service_pb2.ListApplicationsRequest,
        yandex.cloud.backup.v1.policy_service_pb2.ListApplicationsResponse,
    ]
    """List applied policies using filters."""

    Execute: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.backup.v1.policy_service_pb2.ExecuteRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Run policy on specific Compute Cloud instance. That will create backup
    according selected policy. In order to perform this action, policy should be
    applied to the Compute Cloud instance.
    """

    Revoke: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.backup.v1.policy_service_pb2.RevokeRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Revoke policy from Compute Cloud instance."""

class PolicyServiceAsyncStub:
    """A set of methods for managing [policies](/docs/backup/concepts/policy)."""

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.backup.v1.policy_service_pb2.ListPoliciesRequest,
        yandex.cloud.backup.v1.policy_service_pb2.ListPoliciesResponse,
    ]
    """List [policies](/docs/backup/concepts/policy) of specified folder."""

    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.backup.v1.policy_service_pb2.CreatePolicyRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Create a new policy.

    For detailed information, please see [Creating a backup policy](/docs/backup/operations/policy-vm/create).
    """

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.backup.v1.policy_service_pb2.GetPolicyRequest,
        yandex.cloud.backup.v1.policy_pb2.Policy,
    ]
    """Get specific policy."""

    Update: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.backup.v1.policy_service_pb2.UpdatePolicyRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Update specific policy."""

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.backup.v1.policy_service_pb2.DeletePolicyRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Delete specific policy."""

    Apply: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.backup.v1.policy_service_pb2.ApplyPolicyRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Apply policy to [Compute Cloud instance](/docs/backup/concepts/vm-connection#os)."""

    ListApplications: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.backup.v1.policy_service_pb2.ListApplicationsRequest,
        yandex.cloud.backup.v1.policy_service_pb2.ListApplicationsResponse,
    ]
    """List applied policies using filters."""

    Execute: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.backup.v1.policy_service_pb2.ExecuteRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Run policy on specific Compute Cloud instance. That will create backup
    according selected policy. In order to perform this action, policy should be
    applied to the Compute Cloud instance.
    """

    Revoke: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.backup.v1.policy_service_pb2.RevokeRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Revoke policy from Compute Cloud instance."""

class PolicyServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing [policies](/docs/backup/concepts/policy)."""

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.backup.v1.policy_service_pb2.ListPoliciesRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.backup.v1.policy_service_pb2.ListPoliciesResponse, collections.abc.Awaitable[yandex.cloud.backup.v1.policy_service_pb2.ListPoliciesResponse]]:
        """List [policies](/docs/backup/concepts/policy) of specified folder."""

    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.backup.v1.policy_service_pb2.CreatePolicyRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Create a new policy.

        For detailed information, please see [Creating a backup policy](/docs/backup/operations/policy-vm/create).
        """

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.backup.v1.policy_service_pb2.GetPolicyRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.backup.v1.policy_pb2.Policy, collections.abc.Awaitable[yandex.cloud.backup.v1.policy_pb2.Policy]]:
        """Get specific policy."""

    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.backup.v1.policy_service_pb2.UpdatePolicyRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Update specific policy."""

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.backup.v1.policy_service_pb2.DeletePolicyRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Delete specific policy."""

    @abc.abstractmethod
    def Apply(
        self,
        request: yandex.cloud.backup.v1.policy_service_pb2.ApplyPolicyRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Apply policy to [Compute Cloud instance](/docs/backup/concepts/vm-connection#os)."""

    @abc.abstractmethod
    def ListApplications(
        self,
        request: yandex.cloud.backup.v1.policy_service_pb2.ListApplicationsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.backup.v1.policy_service_pb2.ListApplicationsResponse, collections.abc.Awaitable[yandex.cloud.backup.v1.policy_service_pb2.ListApplicationsResponse]]:
        """List applied policies using filters."""

    @abc.abstractmethod
    def Execute(
        self,
        request: yandex.cloud.backup.v1.policy_service_pb2.ExecuteRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Run policy on specific Compute Cloud instance. That will create backup
        according selected policy. In order to perform this action, policy should be
        applied to the Compute Cloud instance.
        """

    @abc.abstractmethod
    def Revoke(
        self,
        request: yandex.cloud.backup.v1.policy_service_pb2.RevokeRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Revoke policy from Compute Cloud instance."""

def add_PolicyServiceServicer_to_server(servicer: PolicyServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
