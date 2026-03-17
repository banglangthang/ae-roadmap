"""Custom execeptions for the AI chatbot CLI"""


class RAGException(Exception):
    """BaseExeception for chatbot-related errros"""

    pass


class APIException(RAGException):
    """Exception for API-related errors"""

    def __init__(self, message, status_code=None, original_error=None) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.original_error = original_error


class AuthenticationException(APIException):
    """Raised when API authentication fails"""

    pass


class ProviderURLNotFoundException(APIException):
    """Raised when provider url not found"""

    pass


class RateLimitException(APIException):
    """Raised when network connectivity issues occur"""

    pass


class FileNotFoundException(RAGException):
    """Raised when file cannot be found"""

    pass


class FileExtensionNotSupportedException(RAGException):
    """Raised when file exetension not in supported list"""

    pass
