import grpc

from datetime import datetime
from six.moves.urllib.parse import urlparse

from yandex.cloud.iam.v1.iam_token_service_pb2_grpc import IamTokenServiceStub

TIMEOUT_SECONDS = 20


class Credentials(grpc.AuthMetadataPlugin):
    def __init__(self, token_requester, lazy_channel):
        # pylint: disable=super-init-not-called
        self.__token_requester = token_requester
        self._lazy_channel = lazy_channel
        self._channel = None
        self._cached_iam_token = None
        self._iam_token_timestamp = None

    def __call__(self, context, callback):
        try:
            return self._call(context, callback)
        except Exception as exception:  # pylint: disable=broad-except
            callback(None, exception)

    def _call(self, context, callback):
        u = urlparse(context.service_url)
        if u.path == '/yandex.cloud.iam.v1.IamTokenService' or u.path == '/yandex.cloud.endpoint.ApiEndpointService':
            callback(None, None)
            return

        if not self._channel:
            self._channel = self._lazy_channel()

        if self._cached_iam_token is None or not self._fresh():
            get_token = getattr(self.__token_requester, "get_token", None)
            if callable(get_token):
                self._cached_iam_token = get_token()
                self._iam_token_timestamp = datetime.now()
                callback(self._metadata(), None)
                return

            get_token_request = getattr(self.__token_requester, "get_token_request", None)
            if callable(get_token_request):
                token_future = IamTokenServiceStub(self._channel).Create.future(get_token_request())
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
