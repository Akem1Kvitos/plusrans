class ServiceException(Exception):
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message
        super().__init__(message)


class NotFoundException(ServiceException):
    def __init__(self, message: str):
        self.code = 404
        self.message = message
        super().__init__(self.code, self.message)


class DatabaseException(ServiceException):
    def __init__(self, message: str):
        self.code = 666
        self.message = message
        super().__init__(self.code, self.message)

