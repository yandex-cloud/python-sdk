# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.serverless.eventrouter.v1 import rule_pb2 as yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_rule__pb2
from yandex.cloud.serverless.eventrouter.v1 import rule_service_pb2 as yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_rule__service__pb2

GRPC_GENERATED_VERSION = '1.70.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in yandex/cloud/serverless/eventrouter/v1/rule_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class RuleServiceStub(object):
    """A set of methods for managing rules for serverless eventrouter.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.serverless.eventrouter.v1.RuleService/Get',
                request_serializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_rule__service__pb2.GetRuleRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_rule__pb2.Rule.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/yandex.cloud.serverless.eventrouter.v1.RuleService/List',
                request_serializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_rule__service__pb2.ListRulesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_rule__service__pb2.ListRulesResponse.FromString,
                _registered_method=True)
        self.Create = channel.unary_unary(
                '/yandex.cloud.serverless.eventrouter.v1.RuleService/Create',
                request_serializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_rule__service__pb2.CreateRuleRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Update = channel.unary_unary(
                '/yandex.cloud.serverless.eventrouter.v1.RuleService/Update',
                request_serializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_rule__service__pb2.UpdateRuleRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/yandex.cloud.serverless.eventrouter.v1.RuleService/Delete',
                request_serializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_rule__service__pb2.DeleteRuleRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Enable = channel.unary_unary(
                '/yandex.cloud.serverless.eventrouter.v1.RuleService/Enable',
                request_serializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_rule__service__pb2.EnableRuleRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Disable = channel.unary_unary(
                '/yandex.cloud.serverless.eventrouter.v1.RuleService/Disable',
                request_serializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_rule__service__pb2.DisableRuleRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.ListAccessBindings = channel.unary_unary(
                '/yandex.cloud.serverless.eventrouter.v1.RuleService/ListAccessBindings',
                request_serializer=yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsResponse.FromString,
                _registered_method=True)
        self.SetAccessBindings = channel.unary_unary(
                '/yandex.cloud.serverless.eventrouter.v1.RuleService/SetAccessBindings',
                request_serializer=yandex_dot_cloud_dot_access_dot_access__pb2.SetAccessBindingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.UpdateAccessBindings = channel.unary_unary(
                '/yandex.cloud.serverless.eventrouter.v1.RuleService/UpdateAccessBindings',
                request_serializer=yandex_dot_cloud_dot_access_dot_access__pb2.UpdateAccessBindingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.ListOperations = channel.unary_unary(
                '/yandex.cloud.serverless.eventrouter.v1.RuleService/ListOperations',
                request_serializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_rule__service__pb2.ListRuleOperationsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_rule__service__pb2.ListRuleOperationsResponse.FromString,
                _registered_method=True)


class RuleServiceServicer(object):
    """A set of methods for managing rules for serverless eventrouter.
    """

    def Get(self, request, context):
        """Returns the specified rules.
        To get the list of all available buses, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of rules in the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates a rule in the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates the specified rule.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified rule.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Enable(self, request, context):
        """Enables the specified rule.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Disable(self, request, context):
        """Disables the specified rule.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAccessBindings(self, request, context):
        """Lists existing access bindings for the specified rule.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAccessBindings(self, request, context):
        """Sets access bindings for the rule.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateAccessBindings(self, request, context):
        """Updates access bindings for the specified rule.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOperations(self, request, context):
        """Lists operations for the specified rule.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RuleServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_rule__service__pb2.GetRuleRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_rule__pb2.Rule.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_rule__service__pb2.ListRulesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_rule__service__pb2.ListRulesResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_rule__service__pb2.CreateRuleRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_rule__service__pb2.UpdateRuleRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_rule__service__pb2.DeleteRuleRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Enable': grpc.unary_unary_rpc_method_handler(
                    servicer.Enable,
                    request_deserializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_rule__service__pb2.EnableRuleRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Disable': grpc.unary_unary_rpc_method_handler(
                    servicer.Disable,
                    request_deserializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_rule__service__pb2.DisableRuleRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListAccessBindings': grpc.unary_unary_rpc_method_handler(
                    servicer.ListAccessBindings,
                    request_deserializer=yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsResponse.SerializeToString,
            ),
            'SetAccessBindings': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAccessBindings,
                    request_deserializer=yandex_dot_cloud_dot_access_dot_access__pb2.SetAccessBindingsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'UpdateAccessBindings': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateAccessBindings,
                    request_deserializer=yandex_dot_cloud_dot_access_dot_access__pb2.UpdateAccessBindingsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListOperations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOperations,
                    request_deserializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_rule__service__pb2.ListRuleOperationsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_rule__service__pb2.ListRuleOperationsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.serverless.eventrouter.v1.RuleService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.serverless.eventrouter.v1.RuleService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class RuleService(object):
    """A set of methods for managing rules for serverless eventrouter.
    """

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.serverless.eventrouter.v1.RuleService/Get',
            yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_rule__service__pb2.GetRuleRequest.SerializeToString,
            yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_rule__pb2.Rule.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.serverless.eventrouter.v1.RuleService/List',
            yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_rule__service__pb2.ListRulesRequest.SerializeToString,
            yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_rule__service__pb2.ListRulesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.serverless.eventrouter.v1.RuleService/Create',
            yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_rule__service__pb2.CreateRuleRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.serverless.eventrouter.v1.RuleService/Update',
            yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_rule__service__pb2.UpdateRuleRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.serverless.eventrouter.v1.RuleService/Delete',
            yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_rule__service__pb2.DeleteRuleRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Enable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.serverless.eventrouter.v1.RuleService/Enable',
            yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_rule__service__pb2.EnableRuleRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Disable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.serverless.eventrouter.v1.RuleService/Disable',
            yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_rule__service__pb2.DisableRuleRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListAccessBindings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.serverless.eventrouter.v1.RuleService/ListAccessBindings',
            yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsRequest.SerializeToString,
            yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SetAccessBindings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.serverless.eventrouter.v1.RuleService/SetAccessBindings',
            yandex_dot_cloud_dot_access_dot_access__pb2.SetAccessBindingsRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateAccessBindings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.serverless.eventrouter.v1.RuleService/UpdateAccessBindings',
            yandex_dot_cloud_dot_access_dot_access__pb2.UpdateAccessBindingsRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListOperations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.serverless.eventrouter.v1.RuleService/ListOperations',
            yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_rule__service__pb2.ListRuleOperationsRequest.SerializeToString,
            yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_rule__service__pb2.ListRuleOperationsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
