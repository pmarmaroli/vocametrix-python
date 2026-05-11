"""Unit tests for exception mapping."""

import pytest
from vocametrix.exceptions import (
    VocametrixAuthError,
    VocametrixForbiddenError,
    VocametrixNotFoundError,
    VocametrixRateLimitError,
    VocametrixServerError,
    VocametrixValidationError,
    raise_for_status,
)


@pytest.mark.parametrize("code,exc_type", [
    (401, VocametrixAuthError),
    (403, VocametrixForbiddenError),
    (404, VocametrixNotFoundError),
    (422, VocametrixValidationError),
    (429, VocametrixRateLimitError),
    (500, VocametrixServerError),
    (503, VocametrixServerError),
])
def test_raise_for_status_maps_correctly(code, exc_type):
    with pytest.raises(exc_type):
        raise_for_status(code, {"error": "test"})


def test_rate_limit_error_has_retry_after():
    err = VocametrixRateLimitError("limited", retry_after=60)
    assert err.retry_after == 60
    assert err.status_code == 429


def test_server_error_carries_body():
    err = VocametrixServerError("oops", status_code=500, body={"error": "crash"})
    assert err.body == {"error": "crash"}
    assert err.status_code == 500


def test_raise_for_status_passes_retry_after_to_rate_limit_error():
    with pytest.raises(VocametrixRateLimitError) as exc_info:
        raise_for_status(429, {"error": "rate limited"}, retry_after=42)
    assert exc_info.value.retry_after == 42


def test_raise_for_status_retry_after_defaults_to_none():
    with pytest.raises(VocametrixRateLimitError) as exc_info:
        raise_for_status(429, {"error": "rate limited"})
    assert exc_info.value.retry_after is None
