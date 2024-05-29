import pytest


@pytest.fixture()
def token():
    return "AAAA00000000000000000000000000000000000"


@pytest.fixture()
def iam_token():
    return "xxxxxx"


@pytest.fixture()
def service_account_key():
    return {
        "id": "ajeboa0du6edu6m43c3t",
        "service_account_id": "ajeq7dsmihqple6761c5",
        "created_at": "2018-10-31T09:30:52Z",
        "key_algorithm": "RSA_4096",
        "public_key": "-----BEGIN PUBLIC KEY-----\n"
        "MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEA0q4HXY6/7jzA3iwofyTq\n"
        "xJ+VPR2fQGrhd+nEi32lemw8XEqVpr4wvzaJHdW2921Z7nsEKJPJq9ZCaDpnkdpS\n"
        "pGPnJCUtJSYQvjs5yrYbEB00LGGi4pERDNWbsX+MyyMl+0Mqd3G3wiu/T8k31T5F\n"
        "gmOK1KPnlDQ6JjZ+OQWkBojBTGGkaCsYKuDwuKfsHZQCqhTt8pLIN7ZiiXWRIB4Q\n"
        "4GfBuBWUfhgncbNCj+PBEBvy1auFnI0CHQ8T9cHqnh9UQIi0qsxVslICv4Z5iX4y\n"
        "YCrRfSw3UJOqQ+mkttSNBjnJC7TpC4uQyc98XC+kLzP1i8/nNv967K9eWA6MVsHF\n"
        "ZqAkFJYcUn6Bx/f3FDiIcW0tR5P/FgDtVTvQAAdUW+l02P27JOqRyD9oDX/y889/\n"
        "c1TGbXlhmaWCqjIVoUnUBlnlHAB7v8X4aqlCu9vwP0DUaXdI/Yxf7VcG6B7wFFZN\n"
        "oM2k6X1J3LSMdrFTXSLbduv/n0mMLUurUx1D0YIIrk2Kv1N63YNiVtPWdFkGHQs6\n"
        "shVgrpiTBUm0VBME7EYKwKQUK7pZ0gn6/IeZpgel0aPCQtaF9FIffLi8KJaMVbJi\n"
        "NGgvr4HTejzn/jabWuLc3rN62AexNYUqnRMfmfNPXyArJ0A54tl2u/TKoPmw0w5t\n"
        "YAwgJ+mSGlylBJbZy2CBp2sCAwEAAQ==\n"
        "-----END PUBLIC KEY-----\n",
        "private_key": "PLEASE DO NOT REMOVE THIS LINE! Yandex.Cloud SA Key ID <ajeboa0du6edu6m43c3t>\n"
        "-----BEGIN PRIVATE KEY-----\n"
        "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\n"
        "awxDbYxnTunk1YxP7KA0/bDnu/OZlQ==\n"
        "-----END PRIVATE KEY-----\n",
    }
