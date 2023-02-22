import time
from datetime import datetime

# noinspection PyUnresolvedReferences
# jwt package depends on cryptography
import cryptography  # noqa: F401; pylint: disable=unused-import
import jwt
import requests
import six

from yandex.cloud.iam.v1.iam_token_service_pb2 import CreateIamTokenRequest

_MDS_ADDR = "169.254.169.254"
_MDS_URL = "http://{}/computeMetadata/v1/instance/service-accounts/default/token"
_MDS_HEADERS = {"Metadata-Flavor": "Google"}
_MDS_TIMEOUT = (1.0, 1.0)  # 1sec connect, 1sec read

YC_API_ENDPOINT = "api.cloud.yandex.net"


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

    private_key_prefix = "-----BEGIN PRIVATE KEY-----"
    if not isinstance(private_key, six.string_types) or not private_key.startswith(private_key_prefix):
        error_message = (
            "Invalid Service Account Key: private key is in incorrect format."
            + "Should start with {prefix}.\n".format(prefix=private_key_prefix)
            + "To obtain one you can use YC CLI: yc iam key create --output sa.json --service-account-id <id>"
        )
        raise RuntimeError(error_message)


def get_auth_token_requester(
    token=None, service_account_key=None, iam_token=None, metadata_addr=_MDS_ADDR, endpoint=YC_API_ENDPOINT
):
    auth_methods = [("token", token), ("service_account_key", service_account_key), ("iam_token", iam_token)]
    auth_methods = [(auth_type, value) for auth_type, value in auth_methods if value is not None]

    if len(auth_methods) == 0:
        return MetadataAuth(metadata_addr=metadata_addr)

    if len(auth_methods) > 1:
        raise RuntimeError(
            "Conflicting API credentials properties are set: {}.".format([auth[0] for auth in auth_methods])
        )

    auth_name, _ = auth_methods[0]
    if auth_name == "token":
        return TokenAuth(token=token)
    if auth_name == "service_account_key":
        __validate_service_account_key(service_account_key)
        return ServiceAccountAuth(service_account_key, endpoint)
    if auth_name == "iam_token":
        return IamTokenAuth(iam_token)

    raise RuntimeError("Unknown auth method: {}".format(auth_name))


class MetadataAuth:
    def __init__(self, metadata_addr):
        self.__metadata_addr = metadata_addr

    def url(self):
        return _MDS_URL.format(self.__metadata_addr)

    def get_token(self):
        r = requests.get(self.url(), headers=_MDS_HEADERS, timeout=_MDS_TIMEOUT)
        r.raise_for_status()
        response = r.json()
        return response["access_token"]


class TokenAuth:
    def __init__(self, token):
        self.__oauth_token = token

    def get_token_request(self):
        return CreateIamTokenRequest(yandex_passport_oauth_token=self.__oauth_token)


class ServiceAccountAuth:
    __SECONDS_IN_HOUR = 60.0 * 60.0

    def __init__(self, sa_key, endpoint=YC_API_ENDPOINT):
        self.__sa_key = sa_key
        self._endpoint = endpoint

    def get_token_request(self):
        return CreateIamTokenRequest(jwt=self.__prepare_request(self._endpoint))

    def __prepare_request(self, endpoint):
        now = time.time()
        now_utc = datetime.utcfromtimestamp(now)
        exp_utc = datetime.utcfromtimestamp(now + self.__SECONDS_IN_HOUR)
        url = "https://iam.{}/iam/v1/tokens".format(endpoint)
        payload = {
            "iss": self.__sa_key["service_account_id"],
            "aud": url,
            "iat": now_utc,
            "exp": exp_utc,
        }

        headers = {
            "typ": "JWT",
            "alg": "PS256",
            "kid": self.__sa_key["id"],
        }

        return jwt.encode(payload, self.__sa_key["private_key"], algorithm="PS256", headers=headers)


class IamTokenAuth:
    def __init__(self, iam_token):
        self.__iam_token = iam_token

    def get_token(self):
        return self.__iam_token
