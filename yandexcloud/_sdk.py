import inspect

import grpc

from yandexcloud._retry_interceptor import RetryInterceptor
from yandexcloud import _channels
from yandexcloud import _operation_waiter
from yandexcloud import _helpers
from yandexcloud._wrappers import Wrappers


class SDK(object):
    def __init__(self, interceptor=None, **kwargs):
        self._channels = _channels.Channels(**kwargs)
        if interceptor is None:
            interceptor = RetryInterceptor(
                max_retry_count=5,
                per_call_timeout=1,
            )
        self._default_interceptor = interceptor
        self.helpers = _helpers.Helpers(self)
        self.wrappers = Wrappers(self)

    def set_interceptor(self, interceptor):
        self._default_interceptor = interceptor

    def client(self, stub_ctor, interceptor=None):
        service = _service_for_ctor(stub_ctor)
        channel = self._channels.channel(service)
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
    m = inspect.getmodule(stub_ctor)
    name = m.__name__
    if not name.startswith('yandex.cloud'):
        raise RuntimeError('Not a yandex.cloud service {}'.format(stub_ctor))

    for k, v in _supported_modules.items():
        if name.startswith(k):
            return v

    raise RuntimeError('Unknown service {}'.format(stub_ctor))


_supported_modules = {
    'yandex.cloud.ai.stt': 'ai-stt',
    'yandex.cloud.ai.translate': 'ai-translate',
    'yandex.cloud.ai.vision': 'ai-vision',
    'yandex.cloud.compute': 'compute',
    'yandex.cloud.containerregistry': 'container-registry',
    'yandex.cloud.dataproc.manager': 'dataproc-manager',
    'yandex.cloud.dataproc': 'dataproc',
    'yandex.cloud.endpoint': 'endpoint',
    'yandex.cloud.iam': 'iam',
    'yandex.cloud.iot.devices': 'iot-devices',
    'yandex.cloud.k8s': 'managed-kubernetes',
    'yandex.cloud.kms': 'kms',
    'yandex.cloud.loadbalancer': 'load-balancer',
    'yandex.cloud.marketplace': 'marketplace',
    'yandex.cloud.mdb.clickhouse': 'managed-clickhouse',
    'yandex.cloud.mdb.kafka': 'managed-kafka',
    'yandex.cloud.mdb.mongodb': 'managed-mongodb',
    'yandex.cloud.mdb.mysql': 'managed-mysql',
    'yandex.cloud.mdb.postgresql': 'managed-postgresql',
    'yandex.cloud.mdb.redis': 'managed-redis',
    'yandex.cloud.operation': 'operation',
    'yandex.cloud.resourcemanager': 'resource-manager',
    'yandex.cloud.serverless.functions': 'serverless-functions',
    'yandex.cloud.serverless.triggers': 'serverless-triggers',
    'yandex.cloud.vpc': 'vpc',
}
