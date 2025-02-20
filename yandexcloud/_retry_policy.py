import json
from typing import Tuple

import grpc


class RetryPolicy:
    def __init__(
        self,
        max_attempts: int = 4,
        status_codes: Tuple["grpc.StatusCode"] = (grpc.StatusCode.UNAVAILABLE,),
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
                }
            ],
            "retryThrottling": {"maxTokens": 100, "tokenRatio": 0.1},
            "waitForReady": True,
        }

    def to_json(self) -> str:
        return json.dumps(self.__policy)
