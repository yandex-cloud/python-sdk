from yandexcloud._backoff import backoff_exponential_jittered_min_interval


def test_backoff_exponential_jittered_min_interval():
    backoff_function = backoff_exponential_jittered_min_interval()
    assert backoff_function(attempt=12) == 60
    for _ in range(100):
        assert 0.025 <= backoff_function(attempt=0) <= 0.075
        assert 51.2 <= backoff_function(attempt=11) <= 60
