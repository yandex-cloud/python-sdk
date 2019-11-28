import inspect
import grpc

from yandexcloud import _channels
from yandexcloud import _operation_waiter


class SDK(object):
    def __init__(self, interceptor=None, **kwargs):
        self._channels = _channels.Channels(**kwargs)
        self._default_interceptor = interceptor

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

    def waiter(self, operation_id):
        return _operation_waiter.operation_waiter(self, operation_id, timeout=None)


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
    'yandex.cloud.dataproc': 'dataproc',
    'yandex.cloud.dataproc.manager': 'dataproc-manager',
    'yandex.cloud.endpoint': 'endpoint',
    'yandex.cloud.iam': 'iam',
    'yandex.cloud.iot.devices': 'iot-devices',
    'yandex.cloud.k8s': 'managed-kubernetes',
    'yandex.cloud.kms': 'kms',
    'yandex.cloud.loadbalancer': 'load-balancer',
    'yandex.cloud.mdb.clickhouse': 'managed-clickhouse',
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
