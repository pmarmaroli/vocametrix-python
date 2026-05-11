"""Unit tests for VocametrixClient wrapper logic."""

import os
import pytest
import respx
import httpx

from vocametrix import VocametrixClient, VocametrixAuthError, VocametrixRateLimitError
from vocametrix._http import AudioInput

BASE = "https://platform.vocametrix.com"


@pytest.fixture
def client():
    c = VocametrixClient(api_key="test-key-123")
    yield c
    c.close()


def test_client_requires_api_key(monkeypatch):
    monkeypatch.delenv("VOCAMETRIX_API_KEY", raising=False)
    with pytest.raises(ValueError, match="API key required"):
        VocametrixClient()


def test_client_reads_key_from_env(monkeypatch):
    monkeypatch.setenv("VOCAMETRIX_API_KEY", "env-key")
    c = VocametrixClient()
    assert c._api_key == "env-key"
    c.close()


def test_client_context_manager():
    with VocametrixClient(api_key="key") as c:
        assert c._api_key == "key"


@respx.mock
def test_avqi_calculate_sends_correct_requests(tmp_path, client):
    # Create a dummy WAV file
    wav = tmp_path / "vowel.wav"
    wav.write_bytes(b"RIFF" + b"\x00" * 40)

    # Mock assignFileId
    respx.post(f"{BASE}/api/assignFileId").mock(
        return_value=httpx.Response(200, json={"fileId": "file-abc"})
    )
    # Mock calculate-avqi
    respx.get(f"{BASE}/api/calculate-avqi").mock(
        return_value=httpx.Response(200, json={"AVQI": 1.8, "CPP": 12.3})
    )

    result = client.avqi.calculate(sustained_vowel=str(wav))
    assert result["AVQI"] == 1.8
    assert result["CPP"] == 12.3


@respx.mock
def test_avqi_with_connected_speech_sends_two_uploads(tmp_path, client):
    sv = tmp_path / "sv.wav"
    cs = tmp_path / "cs.wav"
    sv.write_bytes(b"RIFF" + b"\x00" * 40)
    cs.write_bytes(b"RIFF" + b"\x00" * 40)

    call_count = 0

    def assign_side_effect(request):
        nonlocal call_count
        call_count += 1
        return httpx.Response(200, json={"fileId": f"file-{call_count}"})

    respx.post(f"{BASE}/api/assignFileId").mock(side_effect=assign_side_effect)
    respx.get(f"{BASE}/api/calculate-avqi").mock(
        return_value=httpx.Response(200, json={"AVQI": 2.1})
    )

    client.avqi.calculate(sustained_vowel=str(sv), connected_speech=str(cs))
    assert call_count == 2


@respx.mock
def test_pronunciation_uses_blob_url_pattern(tmp_path, client):
    wav = tmp_path / "speech.wav"
    wav.write_bytes(b"RIFF" + b"\x00" * 40)

    respx.post(f"{BASE}/api/get-blob-url").mock(
        return_value=httpx.Response(200, json={"uploadURL": "https://az.example.com/put", "blobURL": "https://az.example.com/blob"})
    )
    respx.put("https://az.example.com/put").mock(return_value=httpx.Response(201))
    respx.post(f"{BASE}/api/pronunciation-assessment").mock(
        return_value=httpx.Response(200, json={"accuracyScore": 92.5})
    )

    result = client.pronunciation.assess(audio=str(wav), reference_text="Hello", locale="en-US")
    assert result["accuracyScore"] == 92.5


@respx.mock
def test_sound_level_rejects_start_sec_zero(tmp_path, client):
    from vocametrix.exceptions import VocametrixValidationError

    wav = tmp_path / "audio.wav"
    wav.write_bytes(b"RIFF" + b"\x00" * 40)

    with pytest.raises(VocametrixValidationError, match="start_sec=0"):
        client.sound_level.measure(audio=str(wav), start_sec=0.0)


@respx.mock
def test_retry_on_429(tmp_path, client):
    wav = tmp_path / "sv.wav"
    wav.write_bytes(b"RIFF" + b"\x00" * 40)

    call_count = 0

    def flaky_assign(request):
        nonlocal call_count
        call_count += 1
        if call_count < 3:
            return httpx.Response(429, json={"error": "rate limited"})
        return httpx.Response(200, json={"fileId": "ok-file"})

    respx.post(f"{BASE}/api/assignFileId").mock(side_effect=flaky_assign)
    respx.get(f"{BASE}/api/calculate-dsi").mock(
        return_value=httpx.Response(200, json={"DSI": 3.1})
    )

    # Patch sleep to avoid actual waiting in tests
    import vocametrix._http as _http
    original_sleep = _http.time.sleep
    _http.time.sleep = lambda s: None

    try:
        result = client.dsi.calculate(sustained_vowel=str(wav))
        assert result["DSI"] == 3.1
        assert call_count == 3
    finally:
        _http.time.sleep = original_sleep


@respx.mock
def test_auth_error_not_retried(tmp_path, client):
    wav = tmp_path / "sv.wav"
    wav.write_bytes(b"RIFF" + b"\x00" * 40)

    call_count = 0

    def auth_fail(request):
        nonlocal call_count
        call_count += 1
        return httpx.Response(401, json={"error": "invalid key"})

    respx.post(f"{BASE}/api/assignFileId").mock(side_effect=auth_fail)

    with pytest.raises(VocametrixAuthError):
        client.dsi.calculate(sustained_vowel=str(wav))

    assert call_count == 1  # not retried


@respx.mock
def test_stuttering_raises_on_timeout(tmp_path, client):
    from vocametrix.exceptions import VocametrixServerError

    wav = tmp_path / "audio.wav"
    wav.write_bytes(b"RIFF" + b"\x00" * 40)

    respx.post(f"{BASE}/api/assignFileId").mock(
        return_value=httpx.Response(200, json={"fileId": "f1"})
    )
    respx.post(f"{BASE}/api/classify-stuttering").mock(
        return_value=httpx.Response(200, json={"session_id": "sess-1"})
    )
    # Always return "processing" — never completes
    respx.get(f"{BASE}/api/therapy-status/sess-1").mock(
        return_value=httpx.Response(200, json={"status": "processing"})
    )

    # Patch sleep to avoid actual waiting in tests
    import vocametrix._namespaces as _ns
    original_sleep = _ns._time.sleep if hasattr(_ns, '_time') else None
    _ns._time = __import__('time')
    _ns._time.sleep = lambda s: None

    try:
        with pytest.raises(VocametrixServerError, match="timed out"):
            client.stuttering.classify(
                audio=str(wav),
                poll_interval=0.01,
                timeout=0.05,
            )
    finally:
        if original_sleep:
            _ns._time.sleep = original_sleep
