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


@respx.mock
def test_azure_put_does_not_send_api_key(tmp_path):
    """Azure PUT must use a headerless client — API key must not be forwarded."""
    wav = tmp_path / "test.wav"
    wav.write_bytes(b"RIFF" + b"\x00" * 40)

    captured_headers = {}

    def capture_put(request):
        captured_headers.update(dict(request.headers))
        return httpx.Response(201)

    client = httpx.Client(headers={"X-API-Key": "secret-key"})
    respx.post(f"{BASE}/api/get-blob-url").mock(
        return_value=httpx.Response(200, json={
            "uploadURL": "https://blob.windows.net/put",
            "blobURL": "https://blob.windows.net/read",
        })
    )
    respx.put("https://blob.windows.net/put").mock(side_effect=capture_put)

    from vocametrix._http import upload_blob_url
    upload_blob_url(client, BASE, str(wav))

    assert "x-api-key" not in {k.lower() for k in captured_headers}


@respx.mock
def test_upload_uses_mp3_content_type(tmp_path):
    """Content-Type must match file extension, not always audio/wav."""
    mp3 = tmp_path / "audio.mp3"
    mp3.write_bytes(b"\xff\xfb" + b"\x00" * 40)

    captured_content_type = {}

    def capture_upload(request):
        body = request.content.decode("latin-1")
        for line in body.splitlines():
            if "Content-Type:" in line and "audio" in line:
                captured_content_type["value"] = line.split("Content-Type:")[-1].strip()
                break
        return httpx.Response(200, json={"fileId": "mp3-file"})

    client = httpx.Client(headers={"X-API-Key": "key"})
    respx.post(f"{BASE}/api/assignFileId").mock(side_effect=capture_upload)

    from vocametrix._http import upload_assign_file_id
    upload_assign_file_id(client, BASE, str(mp3), email="test@example.com")

    assert captured_content_type.get("value") == "audio/mpeg"
