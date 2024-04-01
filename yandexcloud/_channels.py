from importlib.metadata import PackageNotFoundError, version

import grpc

from yandex.cloud.endpoint.api_endpoint_service_pb2 import ListApiEndpointsRequest
from yandex.cloud.endpoint.api_endpoint_service_pb2_grpc import ApiEndpointServiceStub
from yandexcloud import _auth_plugin
from yandexcloud._auth_fabric import YC_API_ENDPOINT, get_auth_token_requester

try:
    VERSION = version("yandexcloud")
except PackageNotFoundError:
    VERSION = "0.0.0"

SDK_USER_AGENT = "yandex-cloud-python-sdk/{version}".format(version=VERSION)


class Channels(object):
    def __init__(self, client_user_agent=None, **kwargs):
        self._channel_creds = grpc.ssl_channel_credentials(
            root_certificates=kwargs.get("root_certificates"),
            private_key=kwargs.get("private_key"),
            certificate_chain=kwargs.get("certificate_chain"),
        )
        self._endpoint = kwargs.get("endpoint", YC_API_ENDPOINT)
        self._token_requester = get_auth_token_requester(
            token=kwargs.get("token"),
            service_account_key=kwargs.get("service_account_key"),
            iam_token=kwargs.get("iam_token"),
            endpoint=self._endpoint,
        )

        self._unauthenticated_channel = None
        self._channels = None
        self._client_user_agent = client_user_agent

    def channel_options(self):
        return tuple(
            ("grpc.primary_user_agent", user_agent)
            for user_agent in [self._client_user_agent, SDK_USER_AGENT]
            if user_agent is not None
        )

    def channel(self, endpoint):
        if not self._channels:
            self._unauthenticated_channel = grpc.secure_channel(
                self._endpoint, self._channel_creds, options=self.channel_options()
            )
            endpoint_service = ApiEndpointServiceStub(self._unauthenticated_channel)
            resp = endpoint_service.List(ListApiEndpointsRequest())
            endpoints = resp.endpoints

            plugin = _auth_plugin.Credentials(self._token_requester, lambda: self._channels["iam"])
            call_creds = grpc.metadata_call_credentials(plugin)
            creds = grpc.composite_channel_credentials(self._channel_creds, call_creds)

            self._channels = {
                ep.id: grpc.secure_channel(ep.address, creds, options=self.channel_options()) for ep in endpoints
            }

        if endpoint not in self._channels:
            raise RuntimeError("Unknown endpoint: {}".format(endpoint))

        return self._channels[endpoint]
