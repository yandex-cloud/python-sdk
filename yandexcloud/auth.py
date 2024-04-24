from yandex.cloud.iam.v1.iam_token_service_pb2_grpc import IamTokenServiceStub
from yandexcloud import SDK
from yandexcloud._auth_fabric import get_auth_token_requester


def get_iam_token(service_account_key=None):
    token_requester = get_auth_token_requester(service_account_key=service_account_key)
    if not service_account_key:
        return token_requester.get_token()

    sdk = SDK()
    client = sdk.client(IamTokenServiceStub)
    return client.Create(token_requester.get_token_request()).iam_token
