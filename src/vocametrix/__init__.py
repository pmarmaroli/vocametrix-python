"""
vocametrix — Official Python SDK for the Vocametrix voice analysis API.

Quick start::

    from vocametrix import VocametrixClient

    client = VocametrixClient(api_key="your-key")  # or VOCAMETRIX_API_KEY env var
    result = client.avqi.calculate(sustained_vowel="vowel.wav")
    print(result["AVQI"])
"""

from importlib.metadata import PackageNotFoundError as _PackageNotFoundError
from importlib.metadata import version as _version

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
from ._namespaces import TranscriptionEvent

try:
    __version__ = _version("vocametrix")
except _PackageNotFoundError:
    __version__ = "0.0.0"

__all__ = [
    "VocametrixClient",
    "AsyncVocametrixClient",
    "TranscriptionEvent",
    "VocametrixError",
    "VocametrixAuthError",
    "VocametrixForbiddenError",
    "VocametrixNotFoundError",
    "VocametrixRateLimitError",
    "VocametrixServerError",
    "VocametrixValidationError",
]
