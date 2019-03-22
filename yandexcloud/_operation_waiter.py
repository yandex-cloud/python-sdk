import time

from yandex.cloud.operation.operation_service_pb2_grpc import OperationServiceStub
from yandex.cloud.operation.operation_service_pb2 import GetOperationRequest


def operation_waiter(sdk, operation_id, timeout):
    operation_service = sdk.client(OperationServiceStub)
    return OperationWaiter(operation_id, operation_service, timeout)


class OperationWaiter:
    def __init__(self, operation_id, operation_service, timeout=None):
        self.__operation = None
        self.__operation_id = operation_id
        self.__operation_service = operation_service
        self.__deadline = time.time() + timeout if timeout else None

    @property
    def operation(self):
        return self.__operation

    @property
    def done(self):
        self.__operation = self.__operation_service.Get(GetOperationRequest(operation_id=self.__operation_id))
        return self.__operation is not None and self.__operation.done

    def __iter__(self):
        return self

    def __next__(self):
        if self.done or self.__deadline is not None and time.time() >= self.__deadline:
            raise StopIteration()

        return None

    next = __next__  # for Python 2
