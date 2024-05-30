"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class HealthCheck(google.protobuf.message.Message):
    """A HealthCheck resource. For more information, see [Health check](/docs/network-load-balancer/concepts/health-check)."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class TcpOptions(google.protobuf.message.Message):
        """Configuration option for a TCP health check."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        PORT_FIELD_NUMBER: builtins.int
        port: builtins.int
        """Port to use for TCP health checks."""
        def __init__(
            self,
            *,
            port: builtins.int = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["port", b"port"]) -> None: ...

    @typing.final
    class HttpOptions(google.protobuf.message.Message):
        """Configuration option for an HTTP health check."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        PORT_FIELD_NUMBER: builtins.int
        PATH_FIELD_NUMBER: builtins.int
        port: builtins.int
        """Port to use for HTTP health checks."""
        path: builtins.str
        """URL path to set for health checking requests for every target in the target group. 
        For example `` /ping ``. The default path is `` / ``.
        """
        def __init__(
            self,
            *,
            port: builtins.int = ...,
            path: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["path", b"path", "port", b"port"]) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    INTERVAL_FIELD_NUMBER: builtins.int
    TIMEOUT_FIELD_NUMBER: builtins.int
    UNHEALTHY_THRESHOLD_FIELD_NUMBER: builtins.int
    HEALTHY_THRESHOLD_FIELD_NUMBER: builtins.int
    TCP_OPTIONS_FIELD_NUMBER: builtins.int
    HTTP_OPTIONS_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the health check. The name must be unique for each target group that attached to a single load balancer. 3-63 characters long."""
    unhealthy_threshold: builtins.int
    """Number of failed health checks before changing the status to `` UNHEALTHY ``. The default is 2."""
    healthy_threshold: builtins.int
    """Number of successful health checks required in order to set the `` HEALTHY `` status for the target. The default is 2."""
    @property
    def interval(self) -> google.protobuf.duration_pb2.Duration:
        """The interval between health checks. The default is 2 seconds."""

    @property
    def timeout(self) -> google.protobuf.duration_pb2.Duration:
        """Timeout for a target to return a response for the health check. The default is 1 second."""

    @property
    def tcp_options(self) -> global___HealthCheck.TcpOptions:
        """Options for TCP health check."""

    @property
    def http_options(self) -> global___HealthCheck.HttpOptions:
        """Options for HTTP health check."""

    def __init__(
        self,
        *,
        name: builtins.str = ...,
        interval: google.protobuf.duration_pb2.Duration | None = ...,
        timeout: google.protobuf.duration_pb2.Duration | None = ...,
        unhealthy_threshold: builtins.int = ...,
        healthy_threshold: builtins.int = ...,
        tcp_options: global___HealthCheck.TcpOptions | None = ...,
        http_options: global___HealthCheck.HttpOptions | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["http_options", b"http_options", "interval", b"interval", "options", b"options", "tcp_options", b"tcp_options", "timeout", b"timeout"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["healthy_threshold", b"healthy_threshold", "http_options", b"http_options", "interval", b"interval", "name", b"name", "options", b"options", "tcp_options", b"tcp_options", "timeout", b"timeout", "unhealthy_threshold", b"unhealthy_threshold"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["options", b"options"]) -> typing.Literal["tcp_options", "http_options"] | None: ...

global___HealthCheck = HealthCheck
