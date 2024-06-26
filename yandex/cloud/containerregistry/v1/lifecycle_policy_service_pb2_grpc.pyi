"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.containerregistry.v1.lifecycle_policy_pb2
import yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2
import yandex.cloud.operation.operation_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class LifecyclePolicyServiceStub:
    """A set of methods for managing Lifecycle policy resources."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.GetLifecyclePolicyRequest,
        yandex.cloud.containerregistry.v1.lifecycle_policy_pb2.LifecyclePolicy,
    ]
    """Returns the specified lifecycle policy.

    To get the list of all available lifecycle policies, make a [List] request.
    """

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.ListLifecyclePoliciesRequest,
        yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.ListLifecyclePoliciesResponse,
    ]
    """Retrieves the list of lifecycle policies in the specified repository."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.CreateLifecyclePolicyRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a lifecycle policy in the specified repository."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.UpdateLifecyclePolicyRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified lifecycle policy."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.DeleteLifecyclePolicyRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified lifecycle policy."""

    DryRun: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.DryRunLifecyclePolicyRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a request of a dry run of the lifecycle policy."""

    GetDryRunResult: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.GetDryRunLifecyclePolicyResultRequest,
        yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.DryRunLifecyclePolicyResult,
    ]
    """Returns the dry run result of the specified lifecycle policy."""

    ListDryRunResults: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.ListDryRunLifecyclePolicyResultsRequest,
        yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.ListDryRunLifecyclePolicyResultsResponse,
    ]
    """Retrieves the list of the dry run results."""

    ListDryRunResultAffectedImages: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.ListDryRunLifecyclePolicyResultAffectedImagesRequest,
        yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.ListDryRunLifecyclePolicyResultAffectedImagesResponse,
    ]
    """Retrieves the list of the affected images."""

class LifecyclePolicyServiceAsyncStub:
    """A set of methods for managing Lifecycle policy resources."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.GetLifecyclePolicyRequest,
        yandex.cloud.containerregistry.v1.lifecycle_policy_pb2.LifecyclePolicy,
    ]
    """Returns the specified lifecycle policy.

    To get the list of all available lifecycle policies, make a [List] request.
    """

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.ListLifecyclePoliciesRequest,
        yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.ListLifecyclePoliciesResponse,
    ]
    """Retrieves the list of lifecycle policies in the specified repository."""

    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.CreateLifecyclePolicyRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a lifecycle policy in the specified repository."""

    Update: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.UpdateLifecyclePolicyRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified lifecycle policy."""

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.DeleteLifecyclePolicyRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified lifecycle policy."""

    DryRun: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.DryRunLifecyclePolicyRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a request of a dry run of the lifecycle policy."""

    GetDryRunResult: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.GetDryRunLifecyclePolicyResultRequest,
        yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.DryRunLifecyclePolicyResult,
    ]
    """Returns the dry run result of the specified lifecycle policy."""

    ListDryRunResults: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.ListDryRunLifecyclePolicyResultsRequest,
        yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.ListDryRunLifecyclePolicyResultsResponse,
    ]
    """Retrieves the list of the dry run results."""

    ListDryRunResultAffectedImages: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.ListDryRunLifecyclePolicyResultAffectedImagesRequest,
        yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.ListDryRunLifecyclePolicyResultAffectedImagesResponse,
    ]
    """Retrieves the list of the affected images."""

class LifecyclePolicyServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing Lifecycle policy resources."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.GetLifecyclePolicyRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.containerregistry.v1.lifecycle_policy_pb2.LifecyclePolicy, collections.abc.Awaitable[yandex.cloud.containerregistry.v1.lifecycle_policy_pb2.LifecyclePolicy]]:
        """Returns the specified lifecycle policy.

        To get the list of all available lifecycle policies, make a [List] request.
        """

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.ListLifecyclePoliciesRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.ListLifecyclePoliciesResponse, collections.abc.Awaitable[yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.ListLifecyclePoliciesResponse]]:
        """Retrieves the list of lifecycle policies in the specified repository."""

    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.CreateLifecyclePolicyRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates a lifecycle policy in the specified repository."""

    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.UpdateLifecyclePolicyRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates the specified lifecycle policy."""

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.DeleteLifecyclePolicyRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deletes the specified lifecycle policy."""

    @abc.abstractmethod
    def DryRun(
        self,
        request: yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.DryRunLifecyclePolicyRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates a request of a dry run of the lifecycle policy."""

    @abc.abstractmethod
    def GetDryRunResult(
        self,
        request: yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.GetDryRunLifecyclePolicyResultRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.DryRunLifecyclePolicyResult, collections.abc.Awaitable[yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.DryRunLifecyclePolicyResult]]:
        """Returns the dry run result of the specified lifecycle policy."""

    @abc.abstractmethod
    def ListDryRunResults(
        self,
        request: yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.ListDryRunLifecyclePolicyResultsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.ListDryRunLifecyclePolicyResultsResponse, collections.abc.Awaitable[yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.ListDryRunLifecyclePolicyResultsResponse]]:
        """Retrieves the list of the dry run results."""

    @abc.abstractmethod
    def ListDryRunResultAffectedImages(
        self,
        request: yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.ListDryRunLifecyclePolicyResultAffectedImagesRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.ListDryRunLifecyclePolicyResultAffectedImagesResponse, collections.abc.Awaitable[yandex.cloud.containerregistry.v1.lifecycle_policy_service_pb2.ListDryRunLifecyclePolicyResultAffectedImagesResponse]]:
        """Retrieves the list of the affected images."""

def add_LifecyclePolicyServiceServicer_to_server(servicer: LifecyclePolicyServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
