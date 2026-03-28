from unittest.mock import patch

import grpc
import pytest

from yandexcloud import SDK
from yandexcloud._channels import Channels

ENDPOINTS = {
    "iam": "iam.api.cloud.yandex.net:443",
    "compute": "compute.api.cloud.yandex.net:443",
    "vpc": "vpc.api.cloud.yandex.net:443",
}


@pytest.fixture
def mock_channels():
    with patch.multiple(
        Channels,
        _get_creds=lambda self, endpoint: grpc.local_channel_credentials(),
        _get_endpoints=lambda self: dict(ENDPOINTS),
    ):
        yield


class TestChannelCache:
    def test_same_service_returns_same_channel(self, mock_channels):
        sdk = SDK()
        channels = sdk._channels

        ch1 = channels.channel("compute")
        ch2 = channels.channel("compute")

        assert ch1 is ch2

    def test_different_services_return_different_channels(self, mock_channels):
        sdk = SDK()
        channels = sdk._channels

        ch_compute = channels.channel("compute")
        ch_vpc = channels.channel("vpc")

        assert ch_compute is not ch_vpc

    def test_same_service_with_explicit_endpoint_returns_same_channel(self, mock_channels):
        sdk = SDK()
        channels = sdk._channels

        ch1 = channels.channel("compute", endpoint="custom:443")
        ch2 = channels.channel("compute", endpoint="custom:443")

        assert ch1 is ch2

    def test_different_endpoints_return_different_channels(self, mock_channels):
        sdk = SDK()
        channels = sdk._channels

        ch1 = channels.channel("compute", endpoint="host1:443")
        ch2 = channels.channel("compute", endpoint="host2:443")

        assert ch1 is not ch2

    def test_insecure_and_secure_return_different_channels(self, mock_channels):
        sdk = SDK(endpoints={"compute": "localhost:50051"})
        channels = sdk._channels

        ch_secure = channels.channel("compute", insecure=False)
        ch_insecure = channels.channel("compute", insecure=True)

        assert ch_secure is not ch_insecure

    def test_repeated_calls_do_not_grow_channel_count(self, mock_channels):
        sdk = SDK()
        channels = sdk._channels

        for _ in range(100):
            channels.channel("compute")
            channels.channel("vpc")

        assert len(channels._channels) == 2

    def test_default_endpoint_cached_separately_from_explicit(self, mock_channels):
        sdk = SDK()
        channels = sdk._channels

        ch_default = channels.channel("compute")
        ch_explicit = channels.channel("compute", endpoint="custom:443")

        assert ch_default is not ch_explicit
        assert len(channels._channels) == 2
