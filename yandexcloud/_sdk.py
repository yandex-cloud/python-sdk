import grpc
import inspect
import re

from yandexcloud import _channels
from yandexcloud import _helpers
from yandexcloud import _operation_waiter
from yandexcloud._backoff import backoff_exponential_with_jitter
from yandexcloud._retry_interceptor import RetryInterceptor
from yandexcloud._wrappers import Wrappers


class SDK(object):
    def __init__(self, interceptor=None, user_agent=None, **kwargs):
        """
        API entry-point object.

        :param interceptor: GRPC interceptor to be used instead of default RetryInterceptor
        :type interceptor: Union[
            UnaryUnaryClientInterceptor,
            UnaryStreamClientInterceptor,
            StreamUnaryClientInterceptor,
            StreamStreamClientInterceptor
        ]
        :param user_agent: String to prepend User-Agent metadata header for all GRPC requests made via SDK object
        :type user_agent: Optional[str]
        """
        self._channels = _channels.Channels(client_user_agent=user_agent, **kwargs)
        if interceptor is None:
            interceptor = RetryInterceptor(
                max_retry_count=5,
                per_call_timeout=30,
                back_off_func=backoff_exponential_with_jitter(1, 30),
            )
        self._default_interceptor = interceptor
        self.helpers = _helpers.Helpers(self)
        self.wrappers = Wrappers(self)

    def set_interceptor(self, interceptor):
        self._default_interceptor = interceptor

    def client(self, stub_ctor, interceptor=None):
        service = _service_for_ctor(stub_ctor)
        try:
            channel = self._channels.channel(service)
        except self._channels.UnknownEndpointException:
            raise RuntimeError('Unknown service {}'.format(stub_ctor))

        if interceptor is not None:
            channel = grpc.intercept_channel(channel, interceptor)
        elif self._default_interceptor is not None:
            channel = grpc.intercept_channel(channel, self._default_interceptor)
        return stub_ctor(channel)

    def waiter(self, operation_id, timeout=None):
        return _operation_waiter.operation_waiter(self, operation_id, timeout)

    def wait_operation_and_get_result(self, operation, response_type=None, meta_type=None, timeout=None, logger=None):
        return _operation_waiter.get_operation_result(self, operation, response_type, meta_type, timeout, logger)

    def create_operation_and_get_result(
            self,
            request,
            service,
            method_name,
            response_type=None,
            meta_type=None,
            timeout=None,
            logger=None,
    ):
        operation = getattr(self.client(service), method_name)(request)
        return self.wait_operation_and_get_result(
            operation,
            response_type=response_type,
            meta_type=meta_type,
            timeout=timeout,
            logger=logger,
        )


def _service_for_ctor(stub_ctor):
    package = _get_stub_package(stub_ctor)
    if not package.startswith('yandex.cloud'):
        raise RuntimeError('Not a yandex.cloud service {}'.format(stub_ctor))

    for k, v in _NON_STANDARD_ENDPOINT_IDS:
        if package.startswith(k):
            return v

    return _get_default_endpoint_id(package)


def _get_stub_package(stub_ctor):
    module = inspect.getmodule(stub_ctor)
    package, module_name = module.__name__.rsplit('.', 1)
    return package


def _get_default_endpoint_id(module_path):
    """
    Something like:
    "yandex.cloud.ai.stt" -> "ai-stt"
    "yandex.cloud.serverless.triggers.v1" -> "serverless-triggers"
    "yandex.cloud.ai.translate.v2" -> "ai-translate"
    "yandex.cloud.compute.v1.instancegroup" -> "compute-instancegroup"
    """
    without_yc = module_path[len("yandex.cloud."):]
    pieces = [
        piece for piece in without_yc.split(".")
        if re.match(r"v\d+", piece) is None
    ]
    return "-".join(pieces)


_NON_STANDARD_ENDPOINT_IDS = [
    ('yandex.cloud.apploadbalancer.v1', 'alb'),
    ('yandex.cloud.containerregistry', 'container-registry'),
    ('yandex.cloud.k8s', 'managed-kubernetes'),
    ('yandex.cloud.kms.v1.symmetric_crypto_service', 'kms-crypto'),
    ('yandex.cloud.loadbalancer', 'load-balancer'),
    ('yandex.cloud.lockbox.v1.payload_service', 'lockbox-payload'),
    ('yandex.cloud.logging.v1.log_ingestion_service', 'log-ingestion'),
    ('yandex.cloud.logging.v1.log_reading_service', 'log-reading'),
    ('yandex.cloud.logging', 'logging'),
    ('yandex.cloud.marketplace', 'marketplace'),
    ('yandex.cloud.mdb.clickhouse', 'managed-clickhouse'),
    ('yandex.cloud.mdb.kafka', 'managed-kafka'),
    ('yandex.cloud.mdb.mongodb', 'managed-mongodb'),
    ('yandex.cloud.mdb.mysql', 'managed-mysql'),
    ('yandex.cloud.mdb.postgresql', 'managed-postgresql'),
    ('yandex.cloud.mdb.redis', 'managed-redis'),
    ('yandex.cloud.mdb.sqlserver', 'managed-sqlserver'),
    ('yandex.cloud.mdb.elasticsearch', 'managed-elasticsearch'),
    ('yandex.cloud.organizationmanager', 'organization-manager'),
    ('yandex.cloud.resourcemanager', 'resource-manager'),
]
