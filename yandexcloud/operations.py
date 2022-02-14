class OperationError(RuntimeError):
    def __init__(self, message, operation_result):
        super(OperationError, self).__init__(message)  # pylint: disable=super-with-arguments
        self.message = message
        self.operation_result = operation_result


class OperationResult(object):
    def __init__(self, operation, response=None, meta=None):
        self.operation = operation
        self.response = response
        self.meta = meta
