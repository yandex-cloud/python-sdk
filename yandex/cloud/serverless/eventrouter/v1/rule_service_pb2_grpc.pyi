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
import yandex.cloud.operation.operation_pb2
import yandex.cloud.serverless.eventrouter.v1.rule_pb2
import yandex.cloud.serverless.eventrouter.v1.rule_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class RuleServiceStub:
    """A set of methods for managing rules for serverless eventrouter."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.eventrouter.v1.rule_service_pb2.GetRuleRequest,
        yandex.cloud.serverless.eventrouter.v1.rule_pb2.Rule,
    ]
    """Returns the specified rules.
    To get the list of all available buses, make a [List] request.
    """

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.eventrouter.v1.rule_service_pb2.ListRulesRequest,
        yandex.cloud.serverless.eventrouter.v1.rule_service_pb2.ListRulesResponse,
    ]
    """Retrieves the list of rules in the specified folder."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.eventrouter.v1.rule_service_pb2.CreateRuleRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a rule in the specified folder."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.eventrouter.v1.rule_service_pb2.UpdateRuleRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified rule."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.eventrouter.v1.rule_service_pb2.DeleteRuleRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified rule."""

    Enable: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.eventrouter.v1.rule_service_pb2.EnableRuleRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Enables the specified rule."""

    Disable: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.eventrouter.v1.rule_service_pb2.DisableRuleRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Disables the specified rule."""

    ListAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        yandex.cloud.access.access_pb2.ListAccessBindingsResponse,
    ]
    """Lists existing access bindings for the specified rule."""

    SetAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Sets access bindings for the rule."""

    UpdateAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates access bindings for the specified rule."""

    ListOperations: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.eventrouter.v1.rule_service_pb2.ListRuleOperationsRequest,
        yandex.cloud.serverless.eventrouter.v1.rule_service_pb2.ListRuleOperationsResponse,
    ]
    """Lists operations for the specified rule."""

class RuleServiceAsyncStub:
    """A set of methods for managing rules for serverless eventrouter."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.eventrouter.v1.rule_service_pb2.GetRuleRequest,
        yandex.cloud.serverless.eventrouter.v1.rule_pb2.Rule,
    ]
    """Returns the specified rules.
    To get the list of all available buses, make a [List] request.
    """

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.eventrouter.v1.rule_service_pb2.ListRulesRequest,
        yandex.cloud.serverless.eventrouter.v1.rule_service_pb2.ListRulesResponse,
    ]
    """Retrieves the list of rules in the specified folder."""

    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.eventrouter.v1.rule_service_pb2.CreateRuleRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a rule in the specified folder."""

    Update: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.eventrouter.v1.rule_service_pb2.UpdateRuleRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified rule."""

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.eventrouter.v1.rule_service_pb2.DeleteRuleRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified rule."""

    Enable: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.eventrouter.v1.rule_service_pb2.EnableRuleRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Enables the specified rule."""

    Disable: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.eventrouter.v1.rule_service_pb2.DisableRuleRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Disables the specified rule."""

    ListAccessBindings: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        yandex.cloud.access.access_pb2.ListAccessBindingsResponse,
    ]
    """Lists existing access bindings for the specified rule."""

    SetAccessBindings: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Sets access bindings for the rule."""

    UpdateAccessBindings: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates access bindings for the specified rule."""

    ListOperations: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.serverless.eventrouter.v1.rule_service_pb2.ListRuleOperationsRequest,
        yandex.cloud.serverless.eventrouter.v1.rule_service_pb2.ListRuleOperationsResponse,
    ]
    """Lists operations for the specified rule."""

class RuleServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing rules for serverless eventrouter."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.serverless.eventrouter.v1.rule_service_pb2.GetRuleRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.serverless.eventrouter.v1.rule_pb2.Rule, collections.abc.Awaitable[yandex.cloud.serverless.eventrouter.v1.rule_pb2.Rule]]:
        """Returns the specified rules.
        To get the list of all available buses, make a [List] request.
        """

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.serverless.eventrouter.v1.rule_service_pb2.ListRulesRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.serverless.eventrouter.v1.rule_service_pb2.ListRulesResponse, collections.abc.Awaitable[yandex.cloud.serverless.eventrouter.v1.rule_service_pb2.ListRulesResponse]]:
        """Retrieves the list of rules in the specified folder."""

    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.serverless.eventrouter.v1.rule_service_pb2.CreateRuleRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates a rule in the specified folder."""

    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.serverless.eventrouter.v1.rule_service_pb2.UpdateRuleRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates the specified rule."""

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.serverless.eventrouter.v1.rule_service_pb2.DeleteRuleRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deletes the specified rule."""

    @abc.abstractmethod
    def Enable(
        self,
        request: yandex.cloud.serverless.eventrouter.v1.rule_service_pb2.EnableRuleRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Enables the specified rule."""

    @abc.abstractmethod
    def Disable(
        self,
        request: yandex.cloud.serverless.eventrouter.v1.rule_service_pb2.DisableRuleRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Disables the specified rule."""

    @abc.abstractmethod
    def ListAccessBindings(
        self,
        request: yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.access.access_pb2.ListAccessBindingsResponse, collections.abc.Awaitable[yandex.cloud.access.access_pb2.ListAccessBindingsResponse]]:
        """Lists existing access bindings for the specified rule."""

    @abc.abstractmethod
    def SetAccessBindings(
        self,
        request: yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Sets access bindings for the rule."""

    @abc.abstractmethod
    def UpdateAccessBindings(
        self,
        request: yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates access bindings for the specified rule."""

    @abc.abstractmethod
    def ListOperations(
        self,
        request: yandex.cloud.serverless.eventrouter.v1.rule_service_pb2.ListRuleOperationsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.serverless.eventrouter.v1.rule_service_pb2.ListRuleOperationsResponse, collections.abc.Awaitable[yandex.cloud.serverless.eventrouter.v1.rule_service_pb2.ListRuleOperationsResponse]]:
        """Lists operations for the specified rule."""

def add_RuleServiceServicer_to_server(servicer: RuleServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
