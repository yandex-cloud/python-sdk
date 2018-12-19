import time
from datetime import datetime

# jwt package depends on cryptography
import cryptography
import jwt


from yandex.cloud.iam.v1.iam_token_service_pb2 import CreateIamTokenRequest


def __validate_service_account_key(sa_key):
    obj_id = sa_key.get("id")
    sa_id = sa_key.get("service_account_id")
    private_key = sa_key.get("private_key")

    if not obj_id:
        raise RuntimeError("Invalid Service Account Key: missing key object id.")

    if not sa_id:
        raise RuntimeError("Invalid Service Account Key: missing service account id.")

    if not private_key:
        raise RuntimeError("Invalid Service Account Key: missing private key.")


def get_auth_token_request_func(token=None, service_account_key=None):
    if token and service_account_key:
        raise RuntimeError("Conflicting API credentials properties 'token' and 'service-account-key' are set.")

    if token:
        return TokenAuth(token=token).get_token_request

    __validate_service_account_key(service_account_key)
    return ServiceAccountAuth(service_account_key).get_token_request


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
