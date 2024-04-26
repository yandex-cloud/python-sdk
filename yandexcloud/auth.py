from yandex.cloud.iam.v1.iam_token_service_pb2_grpc import IamTokenServiceStub
from yandexcloud import SDK
from yandexcloud._auth_fabric import ServiceAccountAuth, get_auth_token_requester


def get_iam_token_by_metadata(metadata_addr=None):
    return get_auth_token_requester(metadata_addr=metadata_addr).get_token()


def get_iam_token_by_sa_key(service_account_key):
    sdk = SDK()
    client = sdk.client(IamTokenServiceStub)
    sa_auth = ServiceAccountAuth(sa_key=service_account_key)
    return client.Create(sa_auth.get_token_request()).iam_token
