from yandex.cloud.iam.v1.iam_token_service_pb2_grpc import IamTokenServiceStub
from yandexcloud import SDK
from yandexcloud._auth_fabric import MetadataAuth, get_auth_token_requester, YC_API_ENDPOINT


def get_auth_token(token=None, service_account_key=None, iam_token=None, metadata_addr=None, endpoint=YC_API_ENDPOINT):
    requester = get_auth_token_requester(token, service_account_key, iam_token, metadata_addr, endpoint=endpoint)
    if isinstance(requester, MetadataAuth):
        return requester.get_token()

    sdk = SDK()
    client = sdk.client(IamTokenServiceStub)
    return client.Create(requester.get_token_request()).iam_token
