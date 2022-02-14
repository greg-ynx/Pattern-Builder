class CustomException(Exception):
    """
    Exception raised when exception is specific to this application
    """
    pass


class IdNotFound(CustomException):
    """
    Exception raised when an id is not found in table widget.
    """
    pass


class ProtectedRowError(CustomException):
    """
    Exception raised when delete attempt is made to protected row.
    """
    pass


class TableMaxItemError(CustomException):
    """
    Exception raised when add attempt is made to fully load table.
    """
