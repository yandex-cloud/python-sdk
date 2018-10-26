
import grpc

from yandex.cloud.endpoint.api_endpoint_service_pb2_grpc import ApiEndpointServiceStub
from yandex.cloud.endpoint.api_endpoint_service_pb2 import ListApiEndpointsRequest

from yandexcloud import _auth_plugin


def _fill_defaults(opts):
    opts['root_certificates'] = opts.get('root_certificates')
    opts['private_key'] = opts.get('private_key')
    opts['certificate_chain'] = opts.get('certificate_chain')
    opts['endpoint'] = opts.get('endpoint', 'api.cloud.yandex.net')


class Channels(object):
    def __init__(self, **kwargs):
        opts = {x: y for x, y in kwargs.items()}
        _fill_defaults(opts)

        self._channel_creds = grpc.ssl_channel_credentials(
            root_certificates=opts['root_certificates'],
            private_key=opts['private_key'],
            certificate_chain=opts['certificate_chain'],
        )
        self._endpoint = opts['endpoint']
        self._token = opts['token']

        self._unauthenticated_channel = None
        self._channels = None

    def channel(self, endpoint):
        if not self._channels:
            self._unauthenticated_channel = grpc.secure_channel(
                self._endpoint, self._channel_creds)
            endpoint_service = ApiEndpointServiceStub(
                self._unauthenticated_channel)
            resp = endpoint_service.List(ListApiEndpointsRequest())
            endpoints = resp.endpoints

            plugin = _auth_plugin.Credentials(
                self._token, lambda: self._channels["iam"])
            call_creds = grpc.metadata_call_credentials(plugin)
            creds = grpc.composite_channel_credentials(
                self._channel_creds, call_creds)

            self._channels = {
                ep.id: grpc.secure_channel(ep.address, creds)
                for ep in endpoints
            }

        if endpoint not in self._channels:
            raise RuntimeError('Unknown endpoint: {}'.format(endpoint))

        return self._channels[endpoint]
