"""
Ergonomic namespace classes exposed on VocametrixClient.

Each namespace hides upload patterns, case-style differences, SSE auth quirks,
and the start_sec=0 falsy bug from callers. Parameters and return values use
plain Python snake_case dicts; typed Pydantic wrappers are in _models.py.
"""

from __future__ import annotations

import warnings
from dataclasses import dataclass
from typing import Any, Dict, Iterator, Optional, Union
from pathlib import Path

import httpx

from ._http import (
    AudioInput,
    request_with_retry,
    upload_assign_file_id,
    upload_blob_url,
    sse_stream,
)


@dataclass
class TranscriptionEvent:
    status: str
    progress: Optional[float]
    display_text: Optional[str]
    raw: Dict[str, Any]

    @property
    def is_terminal_success(self) -> bool:
        return self.status == "Succeeded"

    @property
    def is_terminal_failure(self) -> bool:
        return self.status.lower() in ("failed", "error")


class AvqiNamespace:
    def __init__(self, client: httpx.Client, base_url: str) -> None:
        self._c = client
        self._base = base_url

    def calculate(
        self,
        sustained_vowel: AudioInput,
        connected_speech: Optional[AudioInput] = None,
        email: str = "sdk@vocametrix.com",
    ) -> Dict[str, Any]:
        sv_id = upload_assign_file_id(self._c, self._base, sustained_vowel, email)
        params: Dict[str, str] = {"svFileId": sv_id}
        if connected_speech is not None:
            cs_id = upload_assign_file_id(self._c, self._base, connected_speech, email)
            params["csFileId"] = cs_id
        resp = request_with_retry(self._c, "GET", f"{self._base}/api/calculate-avqi", params=params)
        return resp.json()


class DsiNamespace:
    def __init__(self, client: httpx.Client, base_url: str) -> None:
        self._c = client
        self._base = base_url

    def calculate(self, sustained_vowel: AudioInput, email: str = "sdk@vocametrix.com") -> Dict[str, Any]:
        sv_id = upload_assign_file_id(self._c, self._base, sustained_vowel, email)
        resp = request_with_retry(self._c, "GET", f"{self._base}/api/calculate-dsi", params={"svFileId": sv_id})
        return resp.json()


class CppNamespace:
    def __init__(self, client: httpx.Client, base_url: str) -> None:
        self._c = client
        self._base = base_url

    def calculate(self, sustained_vowel: AudioInput, email: str = "sdk@vocametrix.com") -> Dict[str, Any]:
        sv_id = upload_assign_file_id(self._c, self._base, sustained_vowel, email)
        resp = request_with_retry(self._c, "GET", f"{self._base}/api/calculate-cpp", params={"svFileId": sv_id})
        return resp.json()


class HnrNamespace:
    def __init__(self, client: httpx.Client, base_url: str) -> None:
        self._c = client
        self._base = base_url

    def calculate(
        self,
        sustained_vowel: AudioInput,
        gender: int = 1,
        email: str = "sdk@vocametrix.com",
    ) -> Dict[str, Any]:
        sv_id = upload_assign_file_id(self._c, self._base, sustained_vowel, email)
        resp = request_with_retry(
            self._c, "GET", f"{self._base}/api/calculate-hnr-multiband",
            params={"svFileId": sv_id, "gender": gender},
        )
        return resp.json()


class JitterShimmerNamespace:
    def __init__(self, client: httpx.Client, base_url: str) -> None:
        self._c = client
        self._base = base_url

    def calculate(self, sustained_vowel: AudioInput, email: str = "sdk@vocametrix.com") -> Dict[str, Any]:
        sv_id = upload_assign_file_id(self._c, self._base, sustained_vowel, email)
        resp = request_with_retry(self._c, "GET", f"{self._base}/api/jitter-shimmer", params={"svFileId": sv_id})
        return resp.json()


class VrpNamespace:
    def __init__(self, client: httpx.Client, base_url: str) -> None:
        self._c = client
        self._base = base_url

    def calculate(
        self,
        sustained_vowel: AudioInput,
        age: int = 30,
        gender: int = 1,
        email: str = "sdk@vocametrix.com",
    ) -> Dict[str, Any]:
        sv_id = upload_assign_file_id(self._c, self._base, sustained_vowel, email)
        resp = request_with_retry(
            self._c, "GET", f"{self._base}/api/calculate-ambitus",
            params={"svFileId": sv_id, "age": age, "gender": gender},
        )
        return resp.json()


class PronunciationNamespace:
    def __init__(self, client: httpx.Client, base_url: str) -> None:
        self._c = client
        self._base = base_url

    def assess(
        self,
        audio: AudioInput,
        reference_text: str,
        locale: str = "en-US",
    ) -> Dict[str, Any]:
        blob_url = upload_blob_url(self._c, self._base, audio)
        resp = request_with_retry(
            self._c, "POST", f"{self._base}/api/pronunciation-assessment",
            json={"blobURL": blob_url, "referenceText": reference_text, "locale": locale},
        )
        return resp.json()


class TranscriptionNamespace:
    def __init__(self, client: httpx.Client, base_url: str, api_key: str) -> None:
        self._c = client
        self._base = base_url
        self._key = api_key

    def stream(self, audio: AudioInput, locale: str = "en-US") -> Iterator[TranscriptionEvent]:
        """Upload audio and stream SSE transcription progress events."""
        blob_url = upload_blob_url(self._c, self._base, audio)
        resp = request_with_retry(
            self._c, "POST", f"{self._base}/api/offline-speech-to-text",
            json={"blobUrl": blob_url, "locale": locale},
        )
        transcription_id: str = resp.json()["transcriptionId"]

        for payload in sse_stream(self._base, transcription_id, self._key):
            yield TranscriptionEvent(
                status=payload.get("status", ""),
                progress=payload.get("progress"),
                display_text=payload.get("displayText"),
                raw=payload,
            )


class TtsNamespace:
    def __init__(self, client: httpx.Client, base_url: str) -> None:
        self._c = client
        self._base = base_url

    def synthesize(
        self,
        text: str,
        locale: str = "en-US",
        voice_name: Optional[str] = None,
    ) -> Dict[str, Any]:
        body: Dict[str, Any] = {"text": text, "locale": locale}
        if voice_name:
            body["voiceName"] = voice_name
        resp = request_with_retry(self._c, "POST", f"{self._base}/api/text-to-speech", json=body)
        return resp.json()


class PhonemeNamespace:
    def __init__(self, client: httpx.Client, base_url: str) -> None:
        self._c = client
        self._base = base_url

    def detect(
        self,
        audio: AudioInput,
        language: str = "fr",
        email: str = "sdk@vocametrix.com",
    ) -> Dict[str, Any]:
        file_id = upload_assign_file_id(self._c, self._base, audio, email)
        resp = request_with_retry(
            self._c, "POST", f"{self._base}/api/classify-phoneme",
            json={"fileId": file_id, "language": language},
        )
        return resp.json()


class StutteringNamespace:
    def __init__(self, client: httpx.Client, base_url: str) -> None:
        self._c = client
        self._base = base_url

    def classify(
        self,
        audio: AudioInput,
        email: str = "sdk@vocametrix.com",
        poll_interval: float = 5.0,
        timeout: float = 620.0,
    ) -> Dict[str, Any]:
        import time as _time

        file_id = upload_assign_file_id(self._c, self._base, audio, email)
        resp = request_with_retry(
            self._c, "POST", f"{self._base}/api/classify-stuttering",
            json={"fileId": file_id},
        )
        session_id: str = resp.json()["session_id"]

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


class ProsodyNamespace:
    def __init__(self, client: httpx.Client, base_url: str) -> None:
        self._c = client
        self._base = base_url

    def similarity(
        self,
        model: AudioInput,
        learner: AudioInput,
        email: str = "sdk@vocametrix.com",
    ) -> Dict[str, Any]:
        sv_id = upload_assign_file_id(self._c, self._base, model, email)
        cs_id = upload_assign_file_id(self._c, self._base, learner, email)
        resp = request_with_retry(
            self._c, "GET", f"{self._base}/api/calculate-prosody-similarity",
            params={"svFileId": sv_id, "csFileId": cs_id},
        )
        return resp.json()


class EgemapsNamespace:
    def __init__(self, client: httpx.Client, base_url: str) -> None:
        self._c = client
        self._base = base_url

    def extract(self, audio: AudioInput, email: str = "sdk@vocametrix.com") -> Dict[str, Any]:
        file_id = upload_assign_file_id(self._c, self._base, audio, email)
        resp = request_with_retry(
            self._c, "GET", f"{self._base}/api/gemaps-extract",
            params={"svFileId": file_id},
        )
        return resp.json()


class SoundLevelNamespace:
    def __init__(self, client: httpx.Client, base_url: str) -> None:
        self._c = client
        self._base = base_url

    def measure(
        self,
        audio: AudioInput,
        start_sec: float = 0.0,
        end_sec: Optional[float] = None,
    ) -> Dict[str, Any]:
        # start_sec=0 is treated as falsy by the backend — silently fix it
        if start_sec == 0.0:
            warnings.warn(
                "start_sec=0 is treated as falsy by the backend; using 0.001 instead. "
                "Pass start_sec=0.001 explicitly to suppress this warning.",
                UserWarning,
                stacklevel=2,
            )
            start_sec = 0.001

        blob_url = upload_blob_url(self._c, self._base, audio)
        body: Dict[str, Any] = {"blobURL": blob_url, "start_sec": start_sec}
        if end_sec is not None:
            body["end_sec"] = end_sec
        resp = request_with_retry(self._c, "POST", f"{self._base}/api/soundLevel", json=body)
        return resp.json()
