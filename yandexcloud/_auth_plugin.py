
import threading
from concurrent import futures
from datetime import datetime

import grpc

from yandex.cloud.iam.v1.iam_token_service_pb2 import CreateIamTokenRequest
from yandex.cloud.iam.v1.iam_token_service_pb2_grpc import IamTokenServiceStub

TIMEOUT_SECONDS = 20


class Credentials(grpc.AuthMetadataPlugin):
    def __init__(self, oauth_token, channel):
        self._oauth_token = oauth_token
        self._client = IamTokenServiceStub(channel)
        self._cached_iam_token = None
        self._iam_token_timestamp = None

    def __call__(self, context, callback):
        try:
            return self._call(context, callback)
        except Exception as exception:  # pylint: disable=broad-except
            callback(None, exception)

    def _call(self, context, callback):
        if context.service_url == '/yandex.cloud.iam.v1.IamTokenService' or \
            context.service_url == '/yandex.cloud.endpoint.ApiEndpointService':
            callback(None, None)
            return

        if self._cached_iam_token is None or not self._fresh():
            token_future = self._client.Create.future(CreateIamTokenRequest(
                yandex_passport_oauth_token=self._oauth_token))
            token_future.add_done_callback(self.create_done_callback(callback))
            return

        callback(self._metadata(), None)

    def create_done_callback(self, callback):
        def done_callback(future):
            try:
                resp = future.result()
            except Exception as exception:  # pylint: disable=broad-except
                callback(None, exception)
            else:
                self._save_token(resp)
                callback(self._metadata(), None)

        return done_callback

    def _metadata(self):
        metadata = (('authorization', 'Bearer ' + self._cached_iam_token),)
        return metadata

    def _save_token(self, resp):
        self._cached_iam_token = resp.iam_token
        self._iam_token_timestamp = datetime.now()

    def _fresh(self):
        if self._cached_iam_token is None:
            return False
        diff = datetime.now() - self._iam_token_timestamp
        return diff.total_seconds() < TIMEOUT_SECONDS
