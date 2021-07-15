import time
from datetime import datetime
import logging

import grpc
from google.protobuf.empty_pb2 import Empty

from yandex.cloud.operation.operation_service_pb2_grpc import OperationServiceStub
from yandex.cloud.operation.operation_service_pb2 import GetOperationRequest
from yandexcloud._retry_interceptor import RetryInterceptor
from yandexcloud.operations import OperationResult, OperationError


def operation_waiter(sdk, operation_id, timeout):
    retriable_codes = (
        grpc.StatusCode.UNAVAILABLE,
        grpc.StatusCode.RESOURCE_EXHAUSTED,
        grpc.StatusCode.INTERNAL,
    )
    operation_service = sdk.client(
        OperationServiceStub,
        interceptor=RetryInterceptor(max_retry_count=5, retriable_codes=retriable_codes),
    )
    return OperationWaiter(operation_id, operation_service, timeout)


def wait_for_operation(sdk, operation_id, timeout):
    waiter = operation_waiter(sdk, operation_id, timeout)
    for _ in waiter:
        time.sleep(1)
    return waiter.operation


def get_operation_result(sdk, operation, response_type=None, meta_type=None, timeout=None, logger=None):
    if not logger:
        logger = logging.getLogger()
        logger.addHandler(logging.NullHandler())
    operation_result = OperationResult(operation)
    created_at = datetime.fromtimestamp(operation.created_at.seconds)
    message = 'Running Yandex.Cloud operation. ID: {id}. ' + \
              'Description: {description}. Created at: {created_at}. ' + \
              'Created by: {created_by}.'
    message = message.format(
        id=operation.id,
        description=operation.description,
        created_at=created_at,
        created_by=operation.created_by,
    )
    if meta_type and meta_type is not Empty:
        unpacked_meta = meta_type()
        operation.metadata.Unpack(unpacked_meta)
        operation_result.meta = unpacked_meta
        message += ' Meta: {unpacked_meta}.'.format(unpacked_meta=unpacked_meta)
    logger.info(message)
    result = wait_for_operation(sdk, operation.id, timeout=timeout)
    if result.error and result.error.code:
        error_message = 'Error Yandex.Cloud operation. ID: {id}. ' + \
                        'Error code: {code}. Details: {details}. ' + \
                        'Message: {message}.'
        error_message = error_message.format(
            id=result.id,
            code=result.error.code,
            details=result.error.details,
            message=result.error.message,
        )
        logger.error(error_message)
        raise OperationError(message=error_message, operation_result=result)
    else:
        log_message = 'Done Yandex.Cloud operation. ID: {id}.'.format(id=operation.id)
        if response_type and response_type is not Empty:
            unpacked_response = response_type()
            result.response.Unpack(unpacked_response)
            operation_result.response = unpacked_response
            log_message += ' Response: {unpacked_response}.'.format(unpacked_response=unpacked_response)
        logger.info(log_message)
    return operation_result


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
