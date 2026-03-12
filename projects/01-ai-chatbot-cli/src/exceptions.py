"""Custom execeptions for the AI chatbot CLI"""


class ChatBotError(Exception):
    """BaseExeception for chatbot-related errros"""

    pass


class APIError(ChatBotError):
    """Exception for API-related errors"""

    def __init__(self, message, status_code=None, original_error=None) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.original_error = original_error


class AuthenticationError(APIError):
    """Raised when API authentication fails"""

    pass


class ProviderURLNotFound(APIError):
    """Raised when provider url not found"""

    pass


class RateLimitError(APIError):
    """Raised when network connectivity issues occur"""

    pass


class ValidationError(ChatBotError):
    """Raised when validation fails"""


class FileNotFoundException(ChatBotError):
    """Raised when file cannot be found"""

    pass


class ContextTooLongError(ChatBotError):
    """Raised when converstain limit exceeded"""

    pass
