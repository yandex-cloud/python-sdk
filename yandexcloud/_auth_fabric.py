import time
from datetime import datetime
import six

# noinspection PyUnresolvedReferences
# jwt package depends on cryptography
import cryptography
import jwt
import requests

from yandex.cloud.iam.v1.iam_token_service_pb2 import CreateIamTokenRequest

_MDS_ADDR = "169.254.169.254"
_MDS_URL = "http://{}/computeMetadata/v1/instance/service-accounts/default/token"
_MDS_HEADERS = {"Metadata-Flavor": "Google"}
_MDS_TIMEOUT = (1.0, 1.0)  # 1sec connect, 1sec read


def __validate_service_account_key(sa_key):
    if not isinstance(sa_key, dict):
        raise RuntimeError("Invalid Service Account Key: expecting dictionary, actually got {}".format(type(sa_key)))

    obj_id = sa_key.get("id")
    sa_id = sa_key.get("service_account_id")
    private_key = sa_key.get("private_key")

    if not obj_id:
        raise RuntimeError("Invalid Service Account Key: missing key object id.")

    if not sa_id:
        raise RuntimeError("Invalid Service Account Key: missing service account id.")

    if not private_key:
        raise RuntimeError("Invalid Service Account Key: missing private key.")

    private_key_prefix = '-----BEGIN PRIVATE KEY-----'
    if not isinstance(private_key, six.string_types) or not private_key.startswith(private_key_prefix):
        raise RuntimeError(
            "Invalid Service Account Key: private key is in incorrect format. Should start with {prefix}.\n"
            "To obtain one you can use YC CLI: yc iam key create --output sa.json --service-account-id <id>"
        )


def get_auth_token_requester(token=None, service_account_key=None, metadata_addr=_MDS_ADDR):
    if token is not None and service_account_key is not None:
        raise RuntimeError("Conflicting API credentials properties 'token' and 'service_account_key' are set.")

    if token is not None:
        return TokenAuth(token=token)

    if service_account_key is not None:
        __validate_service_account_key(service_account_key)
        return ServiceAccountAuth(service_account_key)

    return MetadataAuth(metadata_addr=metadata_addr)


class MetadataAuth:
    def __init__(self, metadata_addr):
        self.__metadata_addr = metadata_addr

    def url(self):
        return _MDS_URL.format(self.__metadata_addr)

    def get_token(self):
        r = requests.get(self.url(), headers=_MDS_HEADERS, timeout=_MDS_TIMEOUT)
        r.raise_for_status()
        response = r.json()
        return response['access_token']


class TokenAuth:
    def __init__(self, token):
        self.__oauth_token = token

    def get_token_request(self):
        return CreateIamTokenRequest(yandex_passport_oauth_token=self.__oauth_token)


class ServiceAccountAuth:
    __SECONDS_IN_HOUR = 60. * 60.

    def __init__(self, sa_key):
        self.__sa_key = sa_key

    def get_token_request(self):
        return CreateIamTokenRequest(jwt=self.__prepare_request())

    def __prepare_request(self):
        now = time.time()
        now_utc = datetime.utcfromtimestamp(now)
        exp_utc = datetime.utcfromtimestamp(now + self.__SECONDS_IN_HOUR)
        payload = {
            "iss": self.__sa_key["service_account_id"],
            "aud": "https://iam.api.cloud.yandex.net/iam/v1/tokens",
            "iat": now_utc,
            "exp": exp_utc,
        }

        headers = {
            "typ": "JWT",
            "alg": "PS256",
            "kid": self.__sa_key["id"],
        }

        return jwt.encode(payload, self.__sa_key["private_key"], algorithm="PS256", headers=headers)
