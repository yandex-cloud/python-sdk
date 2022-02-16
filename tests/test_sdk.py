import pytest

from yandexcloud import _sdk
from yandex.cloud.serverless.functions.v1 import function_service_pb2_grpc


@pytest.mark.parametrize(
    "module_path, expected_endpoint_id",
    [
        ("yandex.cloud.ai.stt", "ai-stt"),
        ("yandex.cloud.serverless.triggers.v1", "serverless-triggers"),
        ("yandex.cloud.ai.translate.v2", "ai-translate"),
        ("yandex.cloud.compute.v1.instancegroup", "compute-instancegroup"),
        (
            _sdk._get_stub_package(function_service_pb2_grpc.FunctionServiceStub),
            "serverless-functions"
        ),
    ]
)
def test_get_default_endpoint_id(module_path, expected_endpoint_id):
    assert _sdk._get_default_endpoint_id(module_path) == expected_endpoint_id
