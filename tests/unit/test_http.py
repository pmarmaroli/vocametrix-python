"""Unit tests for _http.py retry and upload helpers."""

import pytest
import respx
import httpx

from vocametrix._http import _backoff, request_with_retry
from vocametrix.exceptions import VocametrixRateLimitError

BASE = "https://platform.vocametrix.com"


def test_backoff_gives_base_times_power_of_two():
    # _BASE_BACKOFF=2, attempt 0 → 2, attempt 1 → 4, attempt 2 → 8
    assert _backoff(0) == 2.0
    assert _backoff(1) == 4.0
    assert _backoff(2) == 8.0


def test_backoff_respects_retry_after():
    assert _backoff(0, retry_after=30) == 30.0
    assert _backoff(2, retry_after=60) == 60.0


@respx.mock
def test_rate_limit_error_carries_retry_after(monkeypatch):
    import vocametrix._http as _http
    monkeypatch.setattr(_http.time, "sleep", lambda s: None)

    client = httpx.Client()
    respx.post(f"{BASE}/api/assignFileId").mock(
        return_value=httpx.Response(
            429,
            json={"error": "rate limited"},
            headers={"Retry-After": "45"},
        )
    )

    with pytest.raises(VocametrixRateLimitError) as exc_info:
        request_with_retry(client, "POST", f"{BASE}/api/assignFileId")

    assert exc_info.value.retry_after == 45
