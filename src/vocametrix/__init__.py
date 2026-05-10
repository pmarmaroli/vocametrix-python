"""
vocametrix — Official Python SDK for the Vocametrix voice analysis API.

Quick start::

    from vocametrix import VocametrixClient

    client = VocametrixClient(api_key="your-key")  # or VOCAMETRIX_API_KEY env var
    result = client.avqi.calculate(sustained_vowel="vowel.wav")
    print(result["AVQI"])
"""

from .client import AsyncVocametrixClient, VocametrixClient
from .exceptions import (
    VocametrixAuthError,
    VocametrixError,
    VocametrixForbiddenError,
    VocametrixNotFoundError,
    VocametrixRateLimitError,
    VocametrixServerError,
    VocametrixValidationError,
)

__version__ = "0.1.0"

__all__ = [
    "VocametrixClient",
    "AsyncVocametrixClient",
    "VocametrixError",
    "VocametrixAuthError",
    "VocametrixForbiddenError",
    "VocametrixNotFoundError",
    "VocametrixRateLimitError",
    "VocametrixServerError",
    "VocametrixValidationError",
]
