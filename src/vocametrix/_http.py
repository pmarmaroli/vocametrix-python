"""
Internal HTTP helpers: upload patterns, retry, SSE auth quirk.

Never import from _generated inside this module — keep the two layers decoupled
so the generated layer can be replaced without touching this code.
"""

from __future__ import annotations

import contextlib
import io
import mimetypes
import time
import warnings
from pathlib import Path
from typing import Any, Dict, Iterator, Optional, Union

import logging

import httpx

from .exceptions import VocametrixRateLimitError, VocametrixServerError, raise_for_status

_logger = logging.getLogger(__name__)

_AUDIO_MAGIC: list[tuple[bytes, str]] = [
    (b"ID3", "mp3"),
    (b"\xff\xfb", "mp3"),
    (b"\xff\xf3", "mp3"),
    (b"\xff\xf2", "mp3"),
    (b"OggS", "ogg"),
    (b"fLaC", "flac"),
    (b"RIFF", "wav"),
]


def _detect_audio_format(data: bytes) -> str:
    for magic, fmt in _AUDIO_MAGIC:
        if data[: len(magic)] == magic:
            return fmt
    return "wav"


_RETRYABLE = {429, 500, 502, 503, 504}
_MAX_RETRIES = 3
_BASE_BACKOFF = 2.0  # seconds
_MAX_RETRY_AFTER = 60  # seconds — cap server-supplied Retry-After


def _backoff(attempt: int, retry_after: Optional[int] = None) -> float:
    if retry_after is not None:
        return float(min(retry_after, _MAX_RETRY_AFTER))
    return _BASE_BACKOFF * (2 ** attempt)


def request_with_retry(
    client: httpx.Client,
    method: str,
    url: str,
    **kwargs: Any,
) -> httpx.Response:
    """Execute an HTTP request, retrying on transient errors."""
    for attempt in range(_MAX_RETRIES + 1):
        try:
            resp = client.request(method, url, **kwargs)
        except httpx.TransportError as exc:
            if attempt == _MAX_RETRIES:
                raise
            wait = _backoff(attempt)
            _logger.debug("TransportError on attempt %d, retrying in %.1fs: %s", attempt + 1, wait, exc)
            time.sleep(wait)
            continue

        if resp.status_code not in _RETRYABLE or attempt == _MAX_RETRIES:
            if not resp.is_success:
                try:
                    body = resp.json()
                except Exception:
                    body = resp.text
                retry_after = None
                if resp.status_code == 429:
                    ra = resp.headers.get("Retry-After")
                    retry_after = int(ra) if ra and ra.isdigit() else 60
                raise_for_status(resp.status_code, body, retry_after=retry_after)
            return resp

        retry_after = None
        if resp.status_code == 429:
            ra = resp.headers.get("Retry-After")
            retry_after = int(ra) if ra and ra.isdigit() else None
        wait = _backoff(attempt, retry_after)
        _logger.debug("HTTP %d on attempt %d, retrying in %.1fs", resp.status_code, attempt + 1, wait)
        time.sleep(wait)


# ── Upload helpers ────────────────────────────────────────────────────────────

AudioInput = Union[str, Path, bytes]


def _audio_content_type(audio: AudioInput) -> str:
    if isinstance(audio, bytes):
        return f"audio/{_detect_audio_format(audio)}"
    ct, _ = mimetypes.guess_type(str(audio))
    return ct if ct and ct.startswith("audio/") else "audio/wav"


@contextlib.contextmanager
def _open_audio(audio: AudioInput):  # type: ignore[return]
    """Yield (file_like, filename) without loading the whole file into memory."""
    if isinstance(audio, bytes):
        fmt = _detect_audio_format(audio)
        yield io.BytesIO(audio), f"audio.{fmt}"
    else:
        path = Path(audio)
        with open(path, "rb") as f:
            yield f, path.name


def upload_assign_file_id(
    client: httpx.Client,
    base_url: str,
    audio: AudioInput,
    email: str = "info@vocametrix.com",
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


# ── SSE streaming ─────────────────────────────────────────────────────────────

def sse_stream(
    base_url: str,
    transcription_id: str,
    api_key: str,
    timeout: float = 700.0,
) -> Iterator[Dict[str, Any]]:
    """
    Stream SSE events from /api/transcription-progress/:id.

    Auth is via X-API-Key header (not ?apiKey= query string — that was a
    browser EventSource workaround, but this is server-side httpx).
    """
    import json as _json

    url = f"{base_url}/api/transcription-progress/{transcription_id}"
    with httpx.stream("GET", url, timeout=timeout, headers={"X-API-Key": api_key}) as resp:
        if not resp.is_success:
            raise_for_status(resp.status_code, resp.text)
        buffer = ""
        for chunk in resp.iter_text():
            buffer += chunk
            # Normalise CRLF before splitting so both \n\n and \r\n\r\n are handled
            buffer = buffer.replace("\r\n", "\n")
            while "\n\n" in buffer:
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
                        _logger.debug("SSE: skipped non-JSON event: %r", raw)
