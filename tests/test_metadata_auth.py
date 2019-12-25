from .metadata_server_mock import metadata_server

from yandexcloud._auth_fabric import get_auth_token_requester


def test_metadata_auth(iam_token):
    with metadata_server(iam_token) as srv:
        requester = get_auth_token_requester(metadata_addr=srv.addr)
        token = requester.get_token()
        assert token == iam_token
