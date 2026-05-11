"""Typed exceptions for the Vocametrix SDK."""

from __future__ import annotations
from typing import Any, Optional


class VocametrixError(Exception):
    """Base class for all Vocametrix SDK errors."""

    def __init__(self, message: str, status_code: Optional[int] = None, body: Any = None):
        super().__init__(message)
        self.status_code = status_code
        self.body = body


class VocametrixAuthError(VocametrixError):
    """401 — missing or invalid API key."""


class VocametrixForbiddenError(VocametrixError):
    """403 — valid key but insufficient permissions or quota exhausted."""


class VocametrixNotFoundError(VocametrixError):
    """404 — resource not found (unknown fileId, expired session, etc.)."""


class VocametrixValidationError(VocametrixError):
    """422 — validation error (invalid parameter values)."""


class VocametrixRateLimitError(VocametrixError):
    """429 — rate limit exceeded. SDK retries automatically with backoff."""

    def __init__(self, message: str, retry_after: Optional[int] = None, body: Any = None):
        super().__init__(message, status_code=429, body=body)
        self.retry_after = retry_after  # seconds, if server provided it


class VocametrixServerError(VocametrixError):
    """5xx — server error. SDK retries automatically with backoff."""


def raise_for_status(status_code: int, body: Any, retry_after: Optional[int] = None) -> None:
    """Raise the appropriate exception for a non-2xx status code."""
    msg = str(body) if body else f"HTTP {status_code}"
    if status_code == 401:
        raise VocametrixAuthError(msg, status_code=status_code, body=body)
    if status_code == 403:
        raise VocametrixForbiddenError(msg, status_code=status_code, body=body)
    if status_code == 404:
        raise VocametrixNotFoundError(msg, status_code=status_code, body=body)
    if status_code == 422:
        raise VocametrixValidationError(msg, status_code=status_code, body=body)
    if status_code == 429:
        raise VocametrixRateLimitError(msg, retry_after=retry_after, body=body)
    if status_code >= 500:
        raise VocametrixServerError(msg, status_code=status_code, body=body)
    raise VocametrixError(msg, status_code=status_code, body=body)
