from typing import Any, Dict, Optional

from fastapi import HTTPException, status


class BaseAPIException(HTTPException):
    """Base exception for all API exceptions."""

    def __init__(
        self,
        status_code: int,
        detail: str,
        headers: Optional[Dict[str, Any]] = None,
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)


class BadRequestException(BaseAPIException):
    """Exception for bad requests."""

    def __init__(self, detail: str = "Bad request") -> None:
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail,
        )


class UnauthorizedException(BaseAPIException):
    """Exception for unauthorized access."""

    def __init__(self, detail: str = "Unauthorized") -> None:
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
        )


class ForbiddenException(BaseAPIException):
    """Exception for forbidden access."""

    def __init__(self, detail: str = "Forbidden") -> None:
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=detail,
        )


class NotFoundException(BaseAPIException):
    """Exception for not found resources."""

    def __init__(self, detail: str = "Not found") -> None:
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=detail,
        )


class ConflictException(BaseAPIException):
    """Exception for resource conflicts."""

    def __init__(self, detail: str = "Conflict") -> None:
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail=detail,
        )


class ValidationException(BaseAPIException):
    """Exception for validation errors."""

    def __init__(self, detail: str = "Validation error") -> None:
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=detail,
        )


class RateLimitException(BaseAPIException):
    """Exception for rate limiting."""

    def __init__(self, detail: str = "Rate limit exceeded") -> None:
        super().__init__(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=detail,
        )


class InternalServerException(BaseAPIException):
    """Exception for internal server errors."""

    def __init__(self, detail: str = "Internal server error") -> None:
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail,
        )


class ServiceUnavailableException(BaseAPIException):
    """Exception for service unavailable."""

    def __init__(self, detail: str = "Service unavailable") -> None:
        super().__init__(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=detail,
        )


class DatabaseException(BaseAPIException):
    """Exception for database errors."""

    def __init__(self, detail: str = "Database error") -> None:
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail,
        )


class CacheException(BaseAPIException):
    """Exception for cache errors."""

    def __init__(self, detail: str = "Cache error") -> None:
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail,
        )


class MessageQueueException(BaseAPIException):
    """Exception for message queue errors."""

    def __init__(self, detail: str = "Message queue error") -> None:
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail,
        )


class SearchException(BaseAPIException):
    """Exception for search errors."""

    def __init__(self, detail: str = "Search error") -> None:
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail,
        )


class StorageException(BaseAPIException):
    """Exception for storage errors."""

    def __init__(self, detail: str = "Storage error") -> None:
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail,
        )


class EmailException(BaseAPIException):
    """Exception for email errors."""

    def __init__(self, detail: str = "Email error") -> None:
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail,
        )


class AuthenticationException(BaseAPIException):
    """Exception for authentication errors."""

    def __init__(self, detail: str = "Authentication error") -> None:
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
        ) 