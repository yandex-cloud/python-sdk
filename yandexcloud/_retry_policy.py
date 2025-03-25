import json
from enum import Enum
from typing import Tuple

import grpc


class ThrottlingMode(Enum):
    PERSISTENT = "persistent"
    TEMPORARY = "temporary"


class RetryPolicy:
    def __init__(
        self,
        max_attempts: int = 4,
        status_codes: Tuple["grpc.StatusCode"] = (grpc.StatusCode.UNAVAILABLE,),
        throttling_mode: ThrottlingMode = ThrottlingMode.TEMPORARY,
    ):
        self.__policy = {
            "methodConfig": [
                {
                    "name": [{}],
                    "retryPolicy": {
                        "maxAttempts": max_attempts,
                        "initialBackoff": "0.1s",
                        "maxBackoff": "20s",
                        "backoffMultiplier": 2,
                        "retryableStatusCodes": [status.name for status in status_codes],
                    },
                    "waitForReady": True,
                }
            ],
            "retryThrottling": (
                {"maxTokens": 100, "tokenRatio": 0.1}
                if throttling_mode == ThrottlingMode.PERSISTENT
                else {"maxTokens": 6, "tokenRatio": 0.1}
            ),
        }

    def to_json(self) -> str:
        return json.dumps(self.__policy)
