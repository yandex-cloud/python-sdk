import random


def backoff_linear_with_jitter(wait_time, jitter):
    def func(attempt):  # pylint: disable=unused-argument
        multiplier = jitter * (random.random() * 2 - 1)
        return wait_time * (1 + multiplier)

    return func


def backoff_exponential_with_jitter(base, cap):
    def func(attempt):
        try:
            res = (2**attempt) * base * random.random()
        except OverflowError:
            return cap

        if res > cap:
            return cap

        return res

    return func


def backoff_exponential_jittered_min_interval(base=0.05, cap=60):
    def func(attempt):
        try:
            base_interval = (2**attempt) * base
            res = base_interval / 2 + base_interval * random.random()
        except OverflowError:
            return cap

        if res > cap:
            return cap

        return res

    return func


def default_backoff():
    return backoff_exponential_with_jitter(0.05, 60)
