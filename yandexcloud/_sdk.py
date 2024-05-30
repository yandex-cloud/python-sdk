import inspect
from typing import TYPE_CHECKING, Any, Dict, Optional, Type, Union

import grpc

from yandexcloud import _channels, _helpers, _operation_waiter
from yandexcloud._backoff import backoff_exponential_with_jitter
from yandexcloud._retry_interceptor import RetryInterceptor
from yandexcloud._wrappers import Wrappers

if TYPE_CHECKING:
    import logging

    import google.protobuf.message

    from yandex.cloud.operation.operation_pb2 import Operation
    from yandexcloud._operation_waiter import OperationWaiter
    from yandexcloud.operations import OperationError, OperationResult


class SDK:
    def __init__(
        self,
        interceptor: Union[
            grpc.UnaryUnaryClientInterceptor,
            grpc.UnaryStreamClientInterceptor,
            grpc.StreamUnaryClientInterceptor,
            grpc.StreamStreamClientInterceptor,
            None,
        ] = None,
        user_agent: Optional[str] = None,
        endpoints: Optional[Dict[str, str]] = None,
        token: Optional[str] = None,
        iam_token: Optional[str] = None,
        endpoint: Optional[str] = None,
        service_account_key: Optional[Dict[str, str]] = None,
        root_certificates: Optional[bytes] = None,
        private_key: Optional[bytes] = None,
        certificate_chain: Optional[bytes] = None,
        **kwargs: str,
    ):
        """
        API entry-point object.

        :param interceptor: GRPC interceptor to be used instead of default RetryInterceptor
        :param user_agent: String to prepend User-Agent metadata header for all GRPC requests made via SDK object
        :param endpoints: Dict with services endpoints overrides. Example: {'vpc': 'new.vpc.endpoint:443'}

        """
        self._channels = _channels.Channels(
            user_agent,
            endpoints,
            token,
            iam_token,
            endpoint,
            service_account_key,
            root_certificates,
            private_key,
            certificate_chain,
            **kwargs,
        )
        if interceptor is None:
            interceptor = RetryInterceptor(
                max_retry_count=5,
                per_call_timeout=30,
                back_off_func=backoff_exponential_with_jitter(1, 30),
            )
        self._default_interceptor = interceptor
        self.helpers = _helpers.Helpers(self)
        self.wrappers = Wrappers(self)

    def client(
        self,
        stub_ctor: Type,
        interceptor: Union[
            grpc.UnaryUnaryClientInterceptor,
            grpc.UnaryStreamClientInterceptor,
            grpc.StreamUnaryClientInterceptor,
            grpc.StreamStreamClientInterceptor,
            None,
        ] = None,
        endpoint: Optional[str] = None,
        insecure: bool = False,
    ) -> Any:
        service = _service_for_ctor(stub_ctor)
        channel = self._channels.channel(service, endpoint, insecure)
        if interceptor is not None:
            channel = grpc.intercept_channel(channel, interceptor)
        elif self._default_interceptor is not None:
            channel = grpc.intercept_channel(channel, self._default_interceptor)
        return stub_ctor(channel)

    def waiter(self, operation_id: str, timeout: Optional[float] = None) -> "OperationWaiter":
        return _operation_waiter.operation_waiter(self, operation_id, timeout)

    def wait_operation_and_get_result(
        self,
        operation: "Operation",
        response_type: Optional[Type["google.protobuf.message.Message"]] = None,
        meta_type: Optional[Type["google.protobuf.message.Message"]] = None,
        timeout: Optional[float] = None,
        logger: Optional["logging.Logger"] = None,
    ) -> Union["OperationResult", "OperationError"]:
        return _operation_waiter.get_operation_result(self, operation, response_type, meta_type, timeout, logger)

    def create_operation_and_get_result(
        self,
        request: Type["google.protobuf.message.Message"],
        service: Any,
        method_name: str,
        response_type: Optional[Type["google.protobuf.message.Message"]] = None,
        meta_type: Optional[Type["google.protobuf.message.Message"]] = None,
        timeout: Optional[float] = None,
        logger: Optional["logging.Logger"] = None,
    ) -> Union["OperationResult", "OperationError"]:
        operation = getattr(self.client(service), method_name)(request)
        return self.wait_operation_and_get_result(
            operation,
            response_type=response_type,
            meta_type=meta_type,
            timeout=timeout,
            logger=logger,
        )


def _service_for_ctor(stub_ctor: Any) -> str:
    m = inspect.getmodule(stub_ctor)
    if m is not None:
        name = m.__name__
        if not name.startswith("yandex.cloud"):
            raise RuntimeError(f"Not a yandex.cloud service {stub_ctor}")

        for k, v in _supported_modules:
            if name.startswith(k):
                return v

    raise RuntimeError(f"Unknown service {stub_ctor}")


_supported_modules = [
    ("yandex.cloud.ai.foundation_models", "ai-foundation-models"),
    ("yandex.cloud.ai.llm", "ai-llm"),
    ("yandex.cloud.ai.stt", "ai-stt"),
    ("yandex.cloud.ai.translate", "ai-translate"),
    ("yandex.cloud.ai.tts", "ai-speechkit"),
    ("yandex.cloud.ai.vision", "ai-vision"),
    ("yandex.cloud.apploadbalancer", "alb"),
    ("yandex.cloud.billing", "billing"),
    ("yandex.cloud.cdn", "cdn"),
    ("yandex.cloud.certificatemanager.v1.certificate_content_service", "certificate-manager-data"),
    ("yandex.cloud.certificatemanager", "certificate-manager"),
    ("yandex.cloud.compute", "compute"),
    ("yandex.cloud.containerregistry", "container-registry"),
    ("yandex.cloud.dataproc.manager", "dataproc-manager"),
    ("yandex.cloud.dataproc", "dataproc"),
    ("yandex.cloud.datatransfer", "datatransfer"),
    ("yandex.cloud.dns", "dns"),
    ("yandex.cloud.endpoint", "endpoint"),
    ("yandex.cloud.iam", "iam"),
    ("yandex.cloud.iot.devices", "iot-devices"),
    ("yandex.cloud.k8s", "managed-kubernetes"),
    ("yandex.cloud.kms", "kms"),
    ("yandex.cloud.kms.v1.symmetric_crypto_service", "kms-crypto"),
    ("yandex.cloud.loadbalancer", "load-balancer"),
    ("yandex.cloud.loadtesting", "loadtesting"),
    ("yandex.cloud.lockbox.v1.payload_service", "lockbox-payload"),
    ("yandex.cloud.lockbox", "lockbox"),
    ("yandex.cloud.logging.v1.log_ingestion_service", "log-ingestion"),
    ("yandex.cloud.logging.v1.log_reading_service", "log-reading"),
    ("yandex.cloud.logging", "logging"),
    ("yandex.cloud.marketplace", "marketplace"),
    ("yandex.cloud.mdb.clickhouse", "managed-clickhouse"),
    ("yandex.cloud.mdb.elasticsearch", "managed-elasticsearch"),
    ("yandex.cloud.mdb.greenplum", "managed-greenplum"),
    ("yandex.cloud.mdb.kafka", "managed-kafka"),
    ("yandex.cloud.mdb.mongodb", "managed-mongodb"),
    ("yandex.cloud.mdb.mysql", "managed-mysql"),
    ("yandex.cloud.mdb.opensearch", "managed-opensearch"),
    ("yandex.cloud.mdb.postgresql", "managed-postgresql"),
    ("yandex.cloud.mdb.redis", "managed-redis"),
    ("yandex.cloud.mdb.sqlserver", "managed-sqlserver"),
    ("yandex.cloud.operation", "operation"),
    ("yandex.cloud.organizationmanager", "organization-manager"),
    ("yandex.cloud.resourcemanager", "resource-manager"),
    ("yandex.cloud.serverless.apigateway", "serverless-apigateway"),
    ("yandex.cloud.serverless.apigateway.websocket", "apigateway-connections"),
    ("yandex.cloud.serverless.containers", "serverless-containers"),
    ("yandex.cloud.serverless.functions", "serverless-functions"),
    ("yandex.cloud.serverless.triggers", "serverless-triggers"),
    ("yandex.cloud.storage", "storage-api"),
    ("yandex.cloud.vpc", "vpc"),
    ("yandex.cloud.ydb", "ydb"),
]
