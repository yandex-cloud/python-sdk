import random


def backoff_linear_with_jitter(wait_time, jitter):
    def func(attempt):
        multiplier = jitter * (random.random()*2 - 1)
        return wait_time * (1 + multiplier)

    return func


def backoff_exponential_with_jitter(base, cap):
    def func(attempt):
        try:
            res = (2 ** attempt) * base * random.random()
        except OverflowError:
            return cap

        if res > cap:
            return cap

        return res

    return func


def backoff_exponential_with_jitter_addition(base=2):
    def func(attempt):
        base_sleep_time = base ** attempt
        return base_sleep_time + random.random() * base_sleep_time

    return func


def default_backoff():
    return backoff_exponential_with_jitter(0.05, 60)
