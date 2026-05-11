# Fix 16 SDK Concerns Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix all 16 confirmed bugs, security issues, and API surface problems in the Vocametrix Python SDK.

**Architecture:** Changes touch four files (`exceptions.py`, `_http.py`, `_namespaces.py`, `client.py`). Each task is a minimal, targeted edit with a failing test written first. No new files are created except `tests/unit/test_http.py`.

**Tech Stack:** Python 3.9+, httpx, pytest, respx (HTTP mocking), pytest-asyncio

---

## File Map

| File | Changes |
|------|---------|
| `src/vocametrix/exceptions.py` | Add `retry_after` param to `raise_for_status` |
| `src/vocametrix/_http.py` | Backoff formula, unreachable code, retry_after pass-through, Azure auth leak, SSE URL auth, content type, streaming, SSE parser |
| `src/vocametrix/_namespaces.py` | Stuttering timeout error, start_sec raises, email default from client, docstrings |
| `src/vocametrix/client.py` | `AsyncVocametrixClient` namespaces, `email` client param, expose `AdvancedVoiceAnalysisNamespace` |
| `tests/unit/test_http.py` | New: HTTP layer unit tests |
| `tests/unit/test_client.py` | Update existing tests for sound_level and add async client tests |

---

## Task 1 — Fix `raise_for_status` to propagate `retry_after` (concern #3, part 1)

**Files:**
- Modify: `src/vocametrix/exceptions.py:44-59`
- Test: `tests/unit/test_exceptions.py` (already exists — add a test)

- [ ] **Step 1: Write the failing test**

Add to `tests/unit/test_exceptions.py`:

```python
from vocametrix.exceptions import raise_for_status, VocametrixRateLimitError

def test_raise_for_status_passes_retry_after_to_rate_limit_error():
    with pytest.raises(VocametrixRateLimitError) as exc_info:
        raise_for_status(429, {"error": "rate limited"}, retry_after=42)
    assert exc_info.value.retry_after == 42

def test_raise_for_status_retry_after_defaults_to_none():
    with pytest.raises(VocametrixRateLimitError) as exc_info:
        raise_for_status(429, {"error": "rate limited"})
    assert exc_info.value.retry_after is None
```

- [ ] **Step 2: Run test to verify it fails**

```
pytest tests/unit/test_exceptions.py::test_raise_for_status_passes_retry_after_to_rate_limit_error -v
```
Expected: FAIL — `raise_for_status` doesn't accept `retry_after` yet.

- [ ] **Step 3: Implement**

In `src/vocametrix/exceptions.py`, change:

```python
def raise_for_status(status_code: int, body: Any) -> None:
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
        raise VocametrixRateLimitError(msg, body=body)
    if status_code >= 500:
        raise VocametrixServerError(msg, status_code=status_code, body=body)
    raise VocametrixError(msg, status_code=status_code, body=body)
```

To:

```python
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
```

- [ ] **Step 4: Run test to verify it passes**

```
pytest tests/unit/test_exceptions.py -v
```
Expected: all PASS

- [ ] **Step 5: Commit**

```bash
git add src/vocametrix/exceptions.py tests/unit/test_exceptions.py
git commit -m "fix: raise_for_status propagates retry_after to VocametrixRateLimitError"
```

---

## Task 2 — Fix retry logic: backoff formula, unreachable code, retry_after passthrough (concerns #3 part 2, #4, #5)

**Files:**
- Modify: `src/vocametrix/_http.py:24-68`
- Create: `tests/unit/test_http.py`

- [ ] **Step 1: Write failing tests**

Create `tests/unit/test_http.py`:

```python
"""Unit tests for _http.py retry and upload helpers."""

import io
import pytest
import respx
import httpx

from vocametrix._http import _backoff, request_with_retry
from vocametrix.exceptions import VocametrixRateLimitError, VocametrixServerError

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
```

- [ ] **Step 2: Run tests to verify they fail**

```
pytest tests/unit/test_http.py -v
```
Expected: `test_backoff_gives_base_times_power_of_two` FAIL (currently gives 1.0 not 2.0).

- [ ] **Step 3: Implement fixes in `_http.py`**

**Fix 1 — Backoff formula** at line 27. Change:
```python
    return _BASE_BACKOFF ** attempt
```
To:
```python
    return _BASE_BACKOFF * (2 ** attempt)
```

**Fix 2 — Pass retry_after** at lines 52-56. Change:
```python
        retry_after = None
        if resp.status_code == 429:
            ra = resp.headers.get("Retry-After")
            retry_after = int(ra) if ra and ra.isdigit() else 60
            raise_for_status(resp.status_code, body)
        raise_for_status(resp.status_code, body)
```
To:
```python
        retry_after = None
        if resp.status_code == 429:
            ra = resp.headers.get("Retry-After")
            retry_after = int(ra) if ra and ra.isdigit() else 60
            raise_for_status(resp.status_code, body, retry_after=retry_after)
        raise_for_status(resp.status_code, body)
```

**Fix 3 — Remove unreachable code** at line 68. Delete this line entirely:
```python
    raise VocametrixServerError("Max retries exceeded")
```

- [ ] **Step 4: Run tests to verify they pass**

```
pytest tests/unit/test_http.py tests/unit/test_exceptions.py -v
```
Expected: all PASS

- [ ] **Step 5: Commit**

```bash
git add src/vocametrix/_http.py tests/unit/test_http.py
git commit -m "fix: backoff formula, retry_after passthrough, remove unreachable code"
```

---

## Task 3 — Fix Azure API key leak + streaming + content type (concerns #6, #9, #10)

**Files:**
- Modify: `src/vocametrix/_http.py:71-127`

- [ ] **Step 1: Write failing tests**

Add to `tests/unit/test_http.py`:

```python
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
        # multipart body contains Content-Type
        for line in body.splitlines():
            if "Content-Type:" in line:
                captured_content_type["value"] = line.split("Content-Type:")[-1].strip()
                break
        return httpx.Response(200, json={"fileId": "mp3-file"})

    client = httpx.Client(headers={"X-API-Key": "key"})
    respx.post(f"{BASE}/api/assignFileId").mock(side_effect=capture_upload)

    from vocametrix._http import upload_assign_file_id
    upload_assign_file_id(client, BASE, str(mp3), email="test@example.com")

    assert captured_content_type.get("value") == "audio/mpeg"
```

- [ ] **Step 2: Run tests to verify they fail**

```
pytest tests/unit/test_http.py::test_azure_put_does_not_send_api_key tests/unit/test_http.py::test_upload_uses_mp3_content_type -v
```
Expected: `test_azure_put_does_not_send_api_key` FAIL (API key is currently forwarded).

- [ ] **Step 3: Implement in `_http.py`**

Replace the upload helpers section (lines 71-127) with:

```python
# ── Upload helpers ────────────────────────────────────────────────────────────

AudioInput = Union[str, Path, bytes]

import contextlib
import io
import mimetypes


def _audio_content_type(audio: AudioInput) -> str:
    if isinstance(audio, bytes):
        return "audio/wav"
    ct, _ = mimetypes.guess_type(str(audio))
    return ct if ct and ct.startswith("audio/") else "audio/wav"


@contextlib.contextmanager
def _open_audio(audio: AudioInput):  # type: ignore[return]
    """Yield (file_like, filename) without loading everything into memory."""
    if isinstance(audio, bytes):
        yield io.BytesIO(audio), "audio.wav"
    else:
        path = Path(audio)
        with open(path, "rb") as f:
            yield f, path.name


def upload_assign_file_id(
    client: httpx.Client,
    base_url: str,
    audio: AudioInput,
    email: str = "sdk@vocametrix.com",
) -> str:
    """
    assignFileId upload pattern — used by all Praat-backed calculators.
    Returns the fileId string.
    """
    content_type = _audio_content_type(audio)
    with _open_audio(audio) as (f, fname):
        resp = request_with_retry(
            client,
            "POST",
            f"{base_url}/api/assignFileId",
            files={"audio": (fname, f, content_type)},
            data={"email": email},
        )
    return resp.json()["fileId"]


def upload_blob_url(
    client: httpx.Client,
    base_url: str,
    audio: AudioInput,
) -> str:
    """
    get-blob-url pattern — used by pronunciation, STT, sound level.
    Returns the blobURL string.
    """
    resp = request_with_retry(client, "POST", f"{base_url}/api/get-blob-url")
    data = resp.json()
    upload_url: str = data["uploadURL"]
    blob_url: str = data["blobURL"]

    content_type = _audio_content_type(audio)
    # Use a bare client so the Vocametrix API key is NOT forwarded to Azure Storage.
    with _open_audio(audio) as (f, _fname), httpx.Client() as bare_client:
        put = bare_client.put(
            upload_url,
            content=f,
            headers={"x-ms-blob-type": "BlockBlob", "Content-Type": content_type},
        )
    if not put.is_success:
        raise VocametrixServerError(f"Azure upload failed: {put.status_code} {put.text}")

    return blob_url
```

Also remove the old `_read_audio` function entirely (lines 76-79 of the original).

Remove the now-unused `import contextlib` if it was not there before — `contextlib` is stdlib so it's fine. Add `import contextlib`, `import io`, `import mimetypes` to the top-level imports in `_http.py`.

- [ ] **Step 4: Run all tests**

```
pytest tests/unit/ -v
```
Expected: all PASS

- [ ] **Step 5: Commit**

```bash
git add src/vocametrix/_http.py tests/unit/test_http.py
git commit -m "fix: Azure upload uses headerless client; stream audio; detect content type from extension"
```

---

## Task 4 — Fix SSE API key in URL (concern #7)

**Files:**
- Modify: `src/vocametrix/_http.py:132-163`

- [ ] **Step 1: Write failing test**

Add to `tests/unit/test_http.py`:

```python
def test_sse_stream_uses_header_auth_not_url(monkeypatch):
    """API key must be in X-API-Key header, not ?apiKey= query string."""
    import vocametrix._http as _http

    captured_url = {}
    captured_headers = {}

    def fake_stream(method, url, **kwargs):
        captured_url["value"] = url
        captured_headers.update(kwargs.get("headers", {}))

        import contextlib

        @contextlib.contextmanager
        def ctx():
            class FakeResp:
                is_success = True
                status_code = 200

                def iter_text(self):
                    yield 'data: {"status":"Succeeded"}\n\n'

            yield FakeResp()

        return ctx()

    monkeypatch.setattr(_http.httpx, "stream", fake_stream)

    events = list(_http.sse_stream("https://api.example.com", "txn-123", "my-secret-key"))

    assert "apiKey" not in captured_url["value"]
    assert captured_headers.get("X-API-Key") == "my-secret-key"
    assert events[0]["status"] == "Succeeded"
```

- [ ] **Step 2: Run test to verify it fails**

```
pytest tests/unit/test_http.py::test_sse_stream_uses_header_auth_not_url -v
```
Expected: FAIL — URL currently contains `?apiKey=`.

- [ ] **Step 3: Implement**

In `_http.py`, replace `sse_stream` (lines 132-163):

```python
def sse_stream(
    base_url: str,
    transcription_id: str,
    api_key: str,
    timeout: float = 700.0,
) -> Iterator[Dict[str, Any]]:
    """
    Stream SSE events from /api/transcription-progress/:id.

    Auth is via X-API-Key header (not ?apiKey= query string — the latter
    was used as a browser EventSource workaround, but this is server-side httpx).
    """
    import json as _json

    url = f"{base_url}/api/transcription-progress/{transcription_id}"
    with httpx.stream("GET", url, timeout=timeout, headers={"X-API-Key": api_key}) as resp:
        if not resp.is_success:
            raise_for_status(resp.status_code, resp.text)
        buffer = ""
        for chunk in resp.iter_text():
            buffer += chunk
            while "\n\n" in buffer or "\r\n\r\n" in buffer:
                # Normalise CRLF before splitting
                buffer = buffer.replace("\r\n", "\n")
                if "\n\n" not in buffer:
                    break
                event_text, buffer = buffer.split("\n\n", 1)
                data_lines = [
                    line[5:].lstrip(" ")
                    for line in event_text.splitlines()
                    if line.startswith("data:")
                ]
                if data_lines:
                    raw = "\n".join(data_lines)
                    try:
                        yield _json.loads(raw)
                    except _json.JSONDecodeError:
                        pass
```

This also fixes concern #15 (SSE parser): handles `\r\n\r\n`, strips leading space after `data:` correctly with `lstrip(" ")`, and concatenates multiple `data:` lines per event with `\n`.

- [ ] **Step 4: Run all tests**

```
pytest tests/unit/ -v
```
Expected: all PASS

- [ ] **Step 5: Commit**

```bash
git add src/vocametrix/_http.py tests/unit/test_http.py
git commit -m "fix: SSE uses header auth instead of URL query param; fix SSE parser for CRLF and multi-line data"
```

---

## Task 5 — Fix stuttering timeout raises instead of returning incomplete results (concern #2)

**Files:**
- Modify: `src/vocametrix/_namespaces.py:215-253`

- [ ] **Step 1: Write failing test**

Add to `tests/unit/test_http.py` (or a dedicated namespace test — add to `test_client.py`):

```python
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

    import vocametrix._namespaces as _ns
    import time as _time

    # Speed up: very short timeout and poll interval
    with pytest.raises(VocametrixServerError, match="timed out"):
        client.stuttering.classify(
            audio=str(wav),
            poll_interval=0.01,
            timeout=0.05,
        )
```

Note: the `client` fixture from `test_client.py` already creates a `VocametrixClient`. Add the test to `test_client.py`.

- [ ] **Step 2: Run test to verify it fails**

```
pytest tests/unit/test_client.py::test_stuttering_raises_on_timeout -v
```
Expected: FAIL — currently returns (incomplete) result instead of raising.

- [ ] **Step 3: Implement in `_namespaces.py`**

In `StutteringNamespace.classify`, change lines 236-253. Replace:

```python
        elapsed = 0.0
        while elapsed < timeout:
            _time.sleep(poll_interval)
            elapsed += poll_interval
            status_r = request_with_retry(
                self._c, "GET", f"{self._base}/api/therapy-status/{session_id}",
            )
            state = status_r.json().get("status", status_r.json().get("state", ""))
            if state in ("completed", "succeeded", "done"):
                break
            if state in ("failed", "error"):
                from .exceptions import VocametrixServerError
                raise VocametrixServerError(f"Stuttering classification failed: {status_r.json()}")

        result_r = request_with_retry(
            self._c, "GET", f"{self._base}/api/therapy-result/{session_id}",
        )
        return result_r.json()
```

With:

```python
        from .exceptions import VocametrixServerError

        elapsed = 0.0
        while elapsed < timeout:
            _time.sleep(poll_interval)
            elapsed += poll_interval
            status_r = request_with_retry(
                self._c, "GET", f"{self._base}/api/therapy-status/{session_id}",
            )
            payload = status_r.json()
            state = payload.get("status", payload.get("state", ""))
            if state in ("completed", "succeeded", "done"):
                break
            if state in ("failed", "error"):
                raise VocametrixServerError(f"Stuttering classification failed: {payload}")
        else:
            raise VocametrixServerError(
                f"Stuttering classification timed out after {timeout}s (session={session_id})"
            )

        result_r = request_with_retry(
            self._c, "GET", f"{self._base}/api/therapy-result/{session_id}",
        )
        return result_r.json()
```

Key: the `while...else` clause: the `else` block runs when the loop finishes without a `break`, i.e., on timeout.

- [ ] **Step 4: Run all tests**

```
pytest tests/unit/ -v
```
Expected: all PASS

- [ ] **Step 5: Commit**

```bash
git add src/vocametrix/_namespaces.py tests/unit/test_client.py
git commit -m "fix: stuttering classify raises VocametrixServerError on poll timeout instead of returning incomplete result"
```

---

## Task 6 — Fix start_sec=0 raises instead of silently mutating (concern #8)

**Files:**
- Modify: `src/vocametrix/_namespaces.py:295-316`
- Modify: `tests/unit/test_client.py:99-120` (update existing test)

- [ ] **Step 1: Update the existing test to expect an error**

In `tests/unit/test_client.py`, find `test_sound_level_fixes_start_sec_zero` (lines 99-120) and replace it with:

```python
@respx.mock
def test_sound_level_rejects_start_sec_zero(tmp_path, client):
    from vocametrix.exceptions import VocametrixValidationError

    wav = tmp_path / "audio.wav"
    wav.write_bytes(b"RIFF" + b"\x00" * 40)

    with pytest.raises(VocametrixValidationError, match="start_sec=0"):
        client.sound_level.measure(audio=str(wav), start_sec=0.0)
```

- [ ] **Step 2: Run test to verify it fails (currently warns, not raises)**

```
pytest tests/unit/test_client.py::test_sound_level_rejects_start_sec_zero -v
```
Expected: FAIL — currently issues a `UserWarning` instead of raising.

- [ ] **Step 3: Implement in `_namespaces.py`**

In `SoundLevelNamespace.measure`, replace lines 301-309:

```python
        # start_sec=0 is treated as falsy by the backend — silently fix it
        if start_sec == 0.0:
            warnings.warn(
                "start_sec=0 is treated as falsy by the backend; using 0.001 instead. "
                "Pass start_sec=0.001 explicitly to suppress this warning.",
                UserWarning,
                stacklevel=2,
            )
            start_sec = 0.001
```

With:

```python
        if start_sec == 0.0:
            from .exceptions import VocametrixValidationError
            raise VocametrixValidationError(
                "start_sec=0 is rejected by the backend (treated as falsy). "
                "Pass start_sec=0.001 as the minimum offset."
            )
```

Also remove the `import warnings` at the top of `_namespaces.py` if it's no longer used elsewhere. Check: `warnings` is only used in that block, so remove the import.

- [ ] **Step 4: Run all tests**

```
pytest tests/unit/ -v
```
Expected: all PASS

- [ ] **Step 5: Commit**

```bash
git add src/vocametrix/_namespaces.py tests/unit/test_client.py
git commit -m "fix: sound_level.measure raises VocametrixValidationError for start_sec=0 instead of silently mutating"
```

---

## Task 7 — Client-level email default (concern #14)

**Files:**
- Modify: `src/vocametrix/client.py:34-90`
- Modify: `src/vocametrix/_namespaces.py` — all namespace `__init__` and method signatures

- [ ] **Step 1: Write failing test**

Add to `tests/unit/test_client.py`:

```python
@respx.mock
def test_client_email_used_as_namespace_default(tmp_path):
    """email set at client level should appear in upload requests."""
    client = VocametrixClient(api_key="key", email="user@example.com")
    wav = tmp_path / "vowel.wav"
    wav.write_bytes(b"RIFF" + b"\x00" * 40)

    captured_email = {}

    def capture_assign(request):
        # multipart body — find the email field value
        body = request.content.decode("latin-1")
        lines = body.splitlines()
        for i, line in enumerate(lines):
            if 'name="email"' in line and i + 2 < len(lines):
                captured_email["value"] = lines[i + 2].strip()
        return httpx.Response(200, json={"fileId": "f1"})

    respx.post(f"{BASE}/api/assignFileId").mock(side_effect=capture_assign)
    respx.get(f"{BASE}/api/calculate-avqi").mock(
        return_value=httpx.Response(200, json={"AVQI": 1.5})
    )

    client.avqi.calculate(sustained_vowel=str(wav))
    client.close()

    assert captured_email.get("value") == "user@example.com"


@respx.mock
def test_per_call_email_overrides_client_default(tmp_path):
    client = VocametrixClient(api_key="key", email="client@example.com")
    wav = tmp_path / "vowel.wav"
    wav.write_bytes(b"RIFF" + b"\x00" * 40)

    captured_email = {}

    def capture_assign(request):
        body = request.content.decode("latin-1")
        lines = body.splitlines()
        for i, line in enumerate(lines):
            if 'name="email"' in line and i + 2 < len(lines):
                captured_email["value"] = lines[i + 2].strip()
        return httpx.Response(200, json={"fileId": "f1"})

    respx.post(f"{BASE}/api/assignFileId").mock(side_effect=capture_assign)
    respx.get(f"{BASE}/api/calculate-dsi").mock(
        return_value=httpx.Response(200, json={"DSI": 2.0})
    )

    client.dsi.calculate(sustained_vowel=str(wav), email="override@example.com")
    client.close()

    assert captured_email.get("value") == "override@example.com"
```

- [ ] **Step 2: Run tests to verify they fail**

```
pytest tests/unit/test_client.py::test_client_email_used_as_namespace_default -v
```
Expected: FAIL — `VocametrixClient` doesn't accept `email` param.

- [ ] **Step 3: Implement — `client.py` changes**

In `VocametrixClient.__init__`, add `email` parameter:

```python
    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = _DEFAULT_BASE_URL,
        timeout: float = _DEFAULT_TIMEOUT,
        email: str = "sdk@vocametrix.com",
    ) -> None:
        key = api_key or os.environ.get("VOCAMETRIX_API_KEY")
        if not key:
            raise ValueError(
                "API key required. Pass api_key=... or set VOCAMETRIX_API_KEY env var."
            )
        self._api_key = key
        self._email = email
        self._base_url = base_url.rstrip("/")
        self._http = httpx.Client(
            headers={"X-API-Key": key},
            timeout=timeout,
        )
        self._init_namespaces()
```

In `_init_namespaces`, pass `self._email` to each namespace:

```python
    def _init_namespaces(self) -> None:
        b = self._base_url
        e = self._email
        self.avqi = AvqiNamespace(self._http, b, e)
        self.dsi = DsiNamespace(self._http, b, e)
        self.cpp = CppNamespace(self._http, b, e)
        self.hnr = HnrNamespace(self._http, b, e)
        self.jitter_shimmer = JitterShimmerNamespace(self._http, b, e)
        self.vrp = VrpNamespace(self._http, b, e)
        self.pronunciation = PronunciationNamespace(self._http, b)
        self.transcription = TranscriptionNamespace(self._http, b, self._api_key)
        self.tts = TtsNamespace(self._http, b)
        self.phoneme = PhonemeNamespace(self._http, b, e)
        self.stuttering = StutteringNamespace(self._http, b, e)
        self.prosody = ProsodyNamespace(self._http, b, e)
        self.egemaps = EgemapsNamespace(self._http, b, e)
        self.sound_level = SoundLevelNamespace(self._http, b)
```

Note: `PronunciationNamespace`, `TranscriptionNamespace`, `TtsNamespace`, `SoundLevelNamespace` don't use the `email` param (they use the blob-URL upload pattern, not assignFileId).

- [ ] **Step 4: Implement — `_namespaces.py` changes**

For every namespace that uses the `assignFileId` pattern, update `__init__` and methods.

**Pattern** (apply to `AvqiNamespace`, `DsiNamespace`, `CppNamespace`, `HnrNamespace`, `JitterShimmerNamespace`, `VrpNamespace`, `PhonemeNamespace`, `StutteringNamespace`, `ProsodyNamespace`, `EgemapsNamespace`):

```python
class AvqiNamespace:
    def __init__(self, client: httpx.Client, base_url: str, default_email: str = "sdk@vocametrix.com") -> None:
        self._c = client
        self._base = base_url
        self._default_email = default_email

    def calculate(
        self,
        sustained_vowel: AudioInput,
        connected_speech: Optional[AudioInput] = None,
        email: Optional[str] = None,
    ) -> Dict[str, Any]:
        effective_email = email if email is not None else self._default_email
        sv_id = upload_assign_file_id(self._c, self._base, sustained_vowel, effective_email)
        params: Dict[str, str] = {"svFileId": sv_id}
        if connected_speech is not None:
            cs_id = upload_assign_file_id(self._c, self._base, connected_speech, effective_email)
            params["csFileId"] = cs_id
        resp = request_with_retry(self._c, "GET", f"{self._base}/api/calculate-avqi", params=params)
        return resp.json()
```

Apply the same pattern to every other namespace that has an `email` param (change `email: str = "sdk@vocametrix.com"` → `email: Optional[str] = None`, add `default_email` to `__init__`, compute `effective_email`).

- [ ] **Step 5: Run all tests**

```
pytest tests/unit/ -v
```
Expected: all PASS

- [ ] **Step 6: Commit**

```bash
git add src/vocametrix/client.py src/vocametrix/_namespaces.py tests/unit/test_client.py
git commit -m "feat: add client-level email param; namespace methods accept per-call override"
```

---

## Task 8 — Fix docstrings: _models.py ref, stuttering coupling, VRP/ambitus (concerns #11, #13, #16)

**Files:**
- Modify: `src/vocametrix/_namespaces.py:1-8` (module docstring)
- Modify: `src/vocametrix/_namespaces.py:215-230` (StutteringNamespace class/method docstring)
- Modify: `src/vocametrix/_namespaces.py:115-132` (VrpNamespace)

These are doc-only changes — no tests needed.

- [ ] **Step 1: Fix module docstring (concern #11)**

Replace `_namespaces.py` lines 1-7:

```python
"""
Ergonomic namespace classes exposed on VocametrixClient.

Each namespace hides upload patterns, case-style differences, SSE auth quirks,
and the start_sec=0 falsy bug from callers. Parameters and return values use
plain Python snake_case dicts; typed Pydantic wrappers are in _models.py.
"""
```

With:

```python
"""
Ergonomic namespace classes exposed on VocametrixClient.

Each namespace hides upload patterns, case-style differences, and SSE auth
quirks. Parameters and return values are plain Python dicts (snake_case).
Endpoints not covered here are accessible via the generated client in
`vocametrix._generated`.
"""
```

- [ ] **Step 2: Add docstring to StutteringNamespace.classify (concern #13)**

Add a docstring to the `classify` method in `StutteringNamespace`:

```python
    def classify(
        self,
        audio: AudioInput,
        email: Optional[str] = None,
        poll_interval: float = 5.0,
        timeout: float = 620.0,
    ) -> Dict[str, Any]:
        """
        Classify stuttering events in the audio file.

        Polls /api/therapy-status/{session_id} and fetches results from
        /api/therapy-result/{session_id}. The server reuses the therapy-planning
        job system for stuttering jobs, so these therapy-planning endpoints are
        intentional — not a routing mistake.

        Raises VocametrixServerError if the job fails or does not complete within
        `timeout` seconds.
        """
```

- [ ] **Step 3: Add docstring to VrpNamespace (concern #16)**

Add a docstring to `VrpNamespace`:

```python
class VrpNamespace:
    """
    Voice Range Profile (VRP) — also known as phonetogram or ambitus.

    The backend endpoint is /api/calculate-ambitus; "ambitus" and "VRP" refer
    to the same measurement (the pitch/intensity envelope of a singer's or
    speaker's vocal range). This namespace is named VRP for clinical clarity.
    """
```

- [ ] **Step 4: Commit**

```bash
git add src/vocametrix/_namespaces.py
git commit -m "docs: fix _models.py reference, document stuttering endpoint coupling, explain VRP/ambitus naming"
```

---

## Task 9 — Fix AsyncVocametrixClient namespaces (concern #1)

**Files:**
- Modify: `src/vocametrix/client.py:93-143`

- [ ] **Step 1: Write failing test**

Add to `tests/unit/test_client.py`:

```python
import asyncio
import pytest
from vocametrix import AsyncVocametrixClient


@pytest.mark.asyncio
@respx.mock
async def test_async_client_has_avqi_namespace(tmp_path):
    wav = tmp_path / "vowel.wav"
    wav.write_bytes(b"RIFF" + b"\x00" * 40)

    respx.post(f"{BASE}/api/assignFileId").mock(
        return_value=httpx.Response(200, json={"fileId": "async-f1"})
    )
    respx.get(f"{BASE}/api/calculate-avqi").mock(
        return_value=httpx.Response(200, json={"AVQI": 3.5})
    )

    async with AsyncVocametrixClient(api_key="test-key") as client:
        result = await client.avqi.calculate(sustained_vowel=str(wav))

    assert result["AVQI"] == 3.5


@pytest.mark.asyncio
async def test_async_client_requires_api_key(monkeypatch):
    monkeypatch.delenv("VOCAMETRIX_API_KEY", raising=False)
    with pytest.raises(ValueError, match="API key required"):
        AsyncVocametrixClient()
```

- [ ] **Step 2: Run test to verify it fails**

```
pytest tests/unit/test_client.py::test_async_client_has_avqi_namespace -v
```
Expected: FAIL with `AttributeError: 'AsyncVocametrixClient' object has no attribute 'avqi'`.

- [ ] **Step 3: Implement in `client.py`**

Replace the entire `AsyncVocametrixClient` class:

```python
class _AsyncNamespaceProxy:
    """Wraps a sync namespace so every method becomes an awaitable via asyncio.to_thread."""

    def __init__(self, sync_ns: object) -> None:
        self._sync = sync_ns

    def __getattr__(self, name: str):  # type: ignore[return]
        method = getattr(self._sync, name)
        import asyncio

        async def wrapper(*args: object, **kwargs: object) -> object:
            return await asyncio.to_thread(method, *args, **kwargs)

        return wrapper


class AsyncVocametrixClient:
    """
    Async Vocametrix API client.

    Usage::

        async with AsyncVocametrixClient(api_key="...") as client:
            result = await client.avqi.calculate(sustained_vowel="vowel.wav")

    Every namespace method is a coroutine that runs the underlying sync call
    in a thread pool via asyncio.to_thread, keeping the event loop unblocked.
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = _DEFAULT_BASE_URL,
        timeout: float = _DEFAULT_TIMEOUT,
        email: str = "sdk@vocametrix.com",
    ) -> None:
        key = api_key or os.environ.get("VOCAMETRIX_API_KEY")
        if not key:
            raise ValueError(
                "API key required. Pass api_key=... or set VOCAMETRIX_API_KEY env var."
            )
        self._api_key = key
        self._email = email
        self._base_url = base_url.rstrip("/")
        self._sync_http = httpx.Client(
            headers={"X-API-Key": key},
            timeout=timeout,
        )
        self._async_http = httpx.AsyncClient(
            headers={"X-API-Key": key},
            timeout=timeout,
        )
        self._init_namespaces()

    def _init_namespaces(self) -> None:
        b = self._base_url
        e = self._email
        self.avqi = _AsyncNamespaceProxy(AvqiNamespace(self._sync_http, b, e))
        self.dsi = _AsyncNamespaceProxy(DsiNamespace(self._sync_http, b, e))
        self.cpp = _AsyncNamespaceProxy(CppNamespace(self._sync_http, b, e))
        self.hnr = _AsyncNamespaceProxy(HnrNamespace(self._sync_http, b, e))
        self.jitter_shimmer = _AsyncNamespaceProxy(JitterShimmerNamespace(self._sync_http, b, e))
        self.vrp = _AsyncNamespaceProxy(VrpNamespace(self._sync_http, b, e))
        self.pronunciation = _AsyncNamespaceProxy(PronunciationNamespace(self._sync_http, b))
        self.transcription = _AsyncNamespaceProxy(TranscriptionNamespace(self._sync_http, b, self._api_key))
        self.tts = _AsyncNamespaceProxy(TtsNamespace(self._sync_http, b))
        self.phoneme = _AsyncNamespaceProxy(PhonemeNamespace(self._sync_http, b, e))
        self.stuttering = _AsyncNamespaceProxy(StutteringNamespace(self._sync_http, b, e))
        self.prosody = _AsyncNamespaceProxy(ProsodyNamespace(self._sync_http, b, e))
        self.egemaps = _AsyncNamespaceProxy(EgemapsNamespace(self._sync_http, b, e))
        self.sound_level = _AsyncNamespaceProxy(SoundLevelNamespace(self._sync_http, b))

    async def close(self) -> None:
        self._sync_http.close()
        await self._async_http.aclose()

    async def __aenter__(self) -> "AsyncVocametrixClient":
        return self

    async def __aexit__(self, *args: object) -> None:
        await self.close()
```

- [ ] **Step 4: Run all tests**

```
pytest tests/unit/ -v
```
Expected: all PASS

- [ ] **Step 5: Commit**

```bash
git add src/vocametrix/client.py tests/unit/test_client.py
git commit -m "fix: AsyncVocametrixClient now exposes all namespaces via asyncio.to_thread proxy"
```

---

## Task 10 — Expose AdvancedVoiceAnalysisNamespace (concern #12)

**Files:**
- Modify: `src/vocametrix/_namespaces.py` — add `AdvancedVoiceAnalysisNamespace`
- Modify: `src/vocametrix/client.py` — wire it in

This task adds ergonomic wrappers for the 7 advanced voice analysis endpoints that currently require reaching into `_generated`. All use the `assignFileId` upload pattern.

Endpoint params (confirmed from `_generated/api/advanced_voice_analysis/`):
- `/api/calculate-h1-h2` → params: `svFileId`, `gender` (str e.g. `"1"` or `"2"`)
- `/api/calculate-spectral-advanced` → params: `svFileId`, `gender`
- `/api/calculate-sz-ratio` → params: `svFileId`, `csFileId` (both required)
- `/api/calculate-gne` → params: `svFileId`
- `/api/calculate-formant-statistics` → params: `svFileId`, `gender`
- `/api/calculate-abi` → params: `svFileId`
- `/api/calculate-voice-dynamics` → params: `svFileId`

- [ ] **Step 1: Write failing test**

Add to `tests/unit/test_client.py`:

```python
@respx.mock
def test_advanced_voice_h1h2_calculate(tmp_path, client):
    wav = tmp_path / "sv.wav"
    wav.write_bytes(b"RIFF" + b"\x00" * 40)

    respx.post(f"{BASE}/api/assignFileId").mock(
        return_value=httpx.Response(200, json={"fileId": "f-h1h2"})
    )
    respx.get(f"{BASE}/api/calculate-h1-h2").mock(
        return_value=httpx.Response(200, json={"H1": 5.2, "H2": 3.1})
    )

    result = client.advanced.calculate_h1h2(sustained_vowel=str(wav), gender=1)
    assert result["H1"] == 5.2
```

- [ ] **Step 2: Run test to verify it fails**

```
pytest tests/unit/test_client.py::test_advanced_voice_h1h2_calculate -v
```
Expected: FAIL — `client.advanced` doesn't exist.

- [ ] **Step 3: Add `AdvancedVoiceAnalysisNamespace` to `_namespaces.py`**

Append to `_namespaces.py`:

```python
class AdvancedVoiceAnalysisNamespace:
    """
    Advanced voice analysis endpoints — all require a sustained vowel recording.
    All use the assignFileId upload pattern.
    """

    def __init__(self, client: httpx.Client, base_url: str, default_email: str = "sdk@vocametrix.com") -> None:
        self._c = client
        self._base = base_url
        self._default_email = default_email

    def calculate_h1h2(
        self,
        sustained_vowel: AudioInput,
        gender: int = 1,
        email: Optional[str] = None,
    ) -> Dict[str, Any]:
        """H1*-H2*: formant-corrected harmonic difference, a measure of vocal fold adduction."""
        effective_email = email if email is not None else self._default_email
        sv_id = upload_assign_file_id(self._c, self._base, sustained_vowel, effective_email)
        resp = request_with_retry(
            self._c, "GET", f"{self._base}/api/calculate-h1-h2",
            params={"svFileId": sv_id, "gender": gender},
        )
        return resp.json()

    def calculate_spectral(
        self,
        sustained_vowel: AudioInput,
        gender: int = 1,
        email: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Advanced spectral measures (H1H2, H2H4, H4H2kHz, etc.)."""
        effective_email = email if email is not None else self._default_email
        sv_id = upload_assign_file_id(self._c, self._base, sustained_vowel, effective_email)
        resp = request_with_retry(
            self._c, "GET", f"{self._base}/api/calculate-spectral-advanced",
            params={"svFileId": sv_id, "gender": gender},
        )
        return resp.json()

    def calculate_sz_ratio(
        self,
        sustained_vowel: AudioInput,
        connected_speech: AudioInput,
        email: Optional[str] = None,
    ) -> Dict[str, Any]:
        """S/Z ratio: sustained /s/ vs /z/ duration, a screening tool for vocal pathology."""
        effective_email = email if email is not None else self._default_email
        sv_id = upload_assign_file_id(self._c, self._base, sustained_vowel, effective_email)
        cs_id = upload_assign_file_id(self._c, self._base, connected_speech, effective_email)
        resp = request_with_retry(
            self._c, "GET", f"{self._base}/api/calculate-sz-ratio",
            params={"svFileId": sv_id, "csFileId": cs_id},
        )
        return resp.json()

    def calculate_gne(
        self,
        sustained_vowel: AudioInput,
        email: Optional[str] = None,
    ) -> Dict[str, Any]:
        """GNE: Glottal-to-Noise Excitation ratio."""
        effective_email = email if email is not None else self._default_email
        sv_id = upload_assign_file_id(self._c, self._base, sustained_vowel, effective_email)
        resp = request_with_retry(
            self._c, "GET", f"{self._base}/api/calculate-gne",
            params={"svFileId": sv_id},
        )
        return resp.json()

    def calculate_formant_statistics(
        self,
        sustained_vowel: AudioInput,
        gender: int = 1,
        email: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Formant statistics (F1, F2, F3 means and ranges)."""
        effective_email = email if email is not None else self._default_email
        sv_id = upload_assign_file_id(self._c, self._base, sustained_vowel, effective_email)
        resp = request_with_retry(
            self._c, "GET", f"{self._base}/api/calculate-formant-statistics",
            params={"svFileId": sv_id, "gender": gender},
        )
        return resp.json()

    def calculate_abi(
        self,
        sustained_vowel: AudioInput,
        email: Optional[str] = None,
    ) -> Dict[str, Any]:
        """ABI: Acoustic Breathiness Index."""
        effective_email = email if email is not None else self._default_email
        sv_id = upload_assign_file_id(self._c, self._base, sustained_vowel, effective_email)
        resp = request_with_retry(
            self._c, "GET", f"{self._base}/api/calculate-abi",
            params={"svFileId": sv_id},
        )
        return resp.json()

    def calculate_voice_dynamics(
        self,
        sustained_vowel: AudioInput,
        email: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Voice dynamics: perturbation measures over time."""
        effective_email = email if email is not None else self._default_email
        sv_id = upload_assign_file_id(self._c, self._base, sustained_vowel, effective_email)
        resp = request_with_retry(
            self._c, "GET", f"{self._base}/api/calculate-voice-dynamics",
            params={"svFileId": sv_id},
        )
        return resp.json()
```

- [ ] **Step 4: Wire into `client.py`**

Add `AdvancedVoiceAnalysisNamespace` to both `VocametrixClient._init_namespaces` and `AsyncVocametrixClient._init_namespaces`:

```python
# In VocametrixClient._init_namespaces:
        self.advanced = AdvancedVoiceAnalysisNamespace(self._http, b, e)

# In AsyncVocametrixClient._init_namespaces:
        self.advanced = _AsyncNamespaceProxy(AdvancedVoiceAnalysisNamespace(self._sync_http, b, e))
```

Also add `AdvancedVoiceAnalysisNamespace` to the import block at the top of `client.py`.

- [ ] **Step 5: Run all tests**

```
pytest tests/unit/ -v
```
Expected: all PASS

- [ ] **Step 6: Commit**

```bash
git add src/vocametrix/_namespaces.py src/vocametrix/client.py tests/unit/test_client.py
git commit -m "feat: expose AdvancedVoiceAnalysisNamespace (h1h2, spectral, sz_ratio, gne, formant_statistics, abi, voice_dynamics)"
```

---

## Final Verification

- [ ] Run full test suite

```
pytest tests/unit/ -v --cov=src/vocametrix --cov-report=term-missing
```

- [ ] Run type checker

```
mypy src/vocametrix
```

- [ ] Run linter

```
ruff check src/ tests/
```

---

## Self-Review

**Spec coverage:**

| Concern | Task | Status |
|---------|------|--------|
| #1 AsyncVocametrixClient broken | Task 9 | Covered |
| #2 Stuttering incomplete on timeout | Task 5 | Covered |
| #3 retry_after not passed | Tasks 1 + 2 | Covered |
| #4 Unreachable code | Task 2 | Covered |
| #5 Backoff formula | Task 2 | Covered |
| #6 Azure API key leak | Task 3 | Covered |
| #7 SSE API key in URL | Task 4 | Covered |
| #8 Silent start_sec mutation | Task 6 | Covered |
| #9 Hardcoded audio/wav | Task 3 | Covered |
| #10 Whole-file reads | Task 3 | Covered |
| #11 _models.py doesn't exist | Task 8 | Covered (docstring fix) |
| #12 ~75% API hidden | Task 10 | Partially covered (AdvancedVoice group; AI agents, speech coaching, therapy planning deferred — separate plan) |
| #13 Endpoint coupling undocumented | Task 8 | Covered |
| #14 email default leaks identity | Task 7 | Covered |
| #15 SSE parser issues | Task 4 | Covered |
| #16 VrpNamespace/ambitus mismatch | Task 8 | Covered |

**Known deferred:** AI agents, speech coaching, and therapy planning namespaces (concern #12 partial). These follow the same pattern established in Task 10 and can be added incrementally.
