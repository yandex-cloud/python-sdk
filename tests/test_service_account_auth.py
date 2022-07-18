import pytest
import jwt
import time

from yandexcloud._auth_fabric import get_auth_token_requester


def test_both_params_error(token, service_account_key):
    with pytest.raises(RuntimeError) as e:
        get_auth_token_requester(token=token, service_account_key=service_account_key).get_token_request()

    assert str(e.value) == "Conflicting API credentials properties are set: ['token', 'service_account_key']."


def test_invalid_service_account_type():
    with pytest.raises(RuntimeError) as e:
        get_auth_token_requester(service_account_key=[]).get_token_request()

    assert str(e.value).startswith("Invalid Service Account Key: expecting dictionary, actually got")


@pytest.mark.parametrize("key, error_msg", [
    ("id", "Invalid Service Account Key: missing key object id."),
    ("service_account_id", "Invalid Service Account Key: missing service account id."),
    ("private_key", "Invalid Service Account Key: missing private key."),
])
def test_service_account_no_id(service_account_key, key, error_msg):
    service_account_key.pop(key)

    with pytest.raises(RuntimeError) as e:
        get_auth_token_requester(service_account_key=service_account_key).get_token_request()

    assert str(e.value) == error_msg


def test_oauth_token(token):
    request_func = get_auth_token_requester(token=token).get_token_request
    request = request_func()
    assert token == request.yandex_passport_oauth_token


def test_service_account_key(service_account_key):
    request_func = get_auth_token_requester(service_account_key=service_account_key).get_token_request
    request = request_func()
    now = int(time.time())
    headers = jwt.get_unverified_header(request.jwt)
    parsed = jwt.decode(
        request.jwt,
        key=service_account_key["public_key"],
        algorithms=['PS256'],
        audience="https://iam.api.cloud.yandex.net/iam/v1/tokens",
    )
    assert headers["typ"] == "JWT"
    assert headers["alg"] == "PS256"
    assert headers["kid"] == service_account_key["id"]

    assert parsed["iss"] == service_account_key["service_account_id"]
    assert parsed["aud"] == "https://iam.api.cloud.yandex.net/iam/v1/tokens"
    assert now - 60 <= int(parsed["iat"]) <= now

def test_iam_token(iam_token):
    token_func = get_auth_token_requester(iam_token=iam_token).get_token
    token = token_func()
    assert token == iam_token 