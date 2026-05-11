"""
Ergonomic namespace classes exposed on VocametrixClient.

Each namespace hides upload patterns, case-style differences, and SSE auth
quirks. Parameters and return values are plain Python dicts (snake_case).
Endpoints not covered here are accessible via the generated client in
`vocametrix._generated`.
"""

from __future__ import annotations

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


class DsiNamespace:
    def __init__(self, client: httpx.Client, base_url: str, default_email: str = "sdk@vocametrix.com") -> None:
        self._c = client
        self._base = base_url
        self._default_email = default_email

    def calculate(self, sustained_vowel: AudioInput, email: Optional[str] = None) -> Dict[str, Any]:
        effective_email = email if email is not None else self._default_email
        sv_id = upload_assign_file_id(self._c, self._base, sustained_vowel, effective_email)
        resp = request_with_retry(self._c, "GET", f"{self._base}/api/calculate-dsi", params={"svFileId": sv_id})
        return resp.json()


class CppNamespace:
    def __init__(self, client: httpx.Client, base_url: str, default_email: str = "sdk@vocametrix.com") -> None:
        self._c = client
        self._base = base_url
        self._default_email = default_email

    def calculate(self, sustained_vowel: AudioInput, email: Optional[str] = None) -> Dict[str, Any]:
        effective_email = email if email is not None else self._default_email
        sv_id = upload_assign_file_id(self._c, self._base, sustained_vowel, effective_email)
        resp = request_with_retry(self._c, "GET", f"{self._base}/api/calculate-cpp", params={"svFileId": sv_id})
        return resp.json()


class HnrNamespace:
    def __init__(self, client: httpx.Client, base_url: str, default_email: str = "sdk@vocametrix.com") -> None:
        self._c = client
        self._base = base_url
        self._default_email = default_email

    def calculate(
        self,
        sustained_vowel: AudioInput,
        gender: int = 1,
        email: Optional[str] = None,
    ) -> Dict[str, Any]:
        effective_email = email if email is not None else self._default_email
        sv_id = upload_assign_file_id(self._c, self._base, sustained_vowel, effective_email)
        resp = request_with_retry(
            self._c, "GET", f"{self._base}/api/calculate-hnr-multiband",
            params={"svFileId": sv_id, "gender": gender},
        )
        return resp.json()


class JitterShimmerNamespace:
    def __init__(self, client: httpx.Client, base_url: str, default_email: str = "sdk@vocametrix.com") -> None:
        self._c = client
        self._base = base_url
        self._default_email = default_email

    def calculate(self, sustained_vowel: AudioInput, email: Optional[str] = None) -> Dict[str, Any]:
        effective_email = email if email is not None else self._default_email
        sv_id = upload_assign_file_id(self._c, self._base, sustained_vowel, effective_email)
        resp = request_with_retry(self._c, "GET", f"{self._base}/api/jitter-shimmer", params={"svFileId": sv_id})
        return resp.json()


class VrpNamespace:
    """
    Voice Range Profile (VRP) — also known as phonetogram or ambitus.

    The backend endpoint is /api/calculate-ambitus; "ambitus" and "VRP" refer
    to the same measurement (the pitch/intensity envelope of a speaker's vocal
    range). This namespace is named VRP for clinical clarity.
    """
    def __init__(self, client: httpx.Client, base_url: str, default_email: str = "sdk@vocametrix.com") -> None:
        self._c = client
        self._base = base_url
        self._default_email = default_email

    def calculate(
        self,
        sustained_vowel: AudioInput,
        age: int = 30,
        gender: int = 1,
        email: Optional[str] = None,
    ) -> Dict[str, Any]:
        effective_email = email if email is not None else self._default_email
        sv_id = upload_assign_file_id(self._c, self._base, sustained_vowel, effective_email)
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
    def __init__(self, client: httpx.Client, base_url: str, default_email: str = "sdk@vocametrix.com") -> None:
        self._c = client
        self._base = base_url
        self._default_email = default_email

    def detect(
        self,
        audio: AudioInput,
        language: str = "fr",
        email: Optional[str] = None,
    ) -> Dict[str, Any]:
        effective_email = email if email is not None else self._default_email
        file_id = upload_assign_file_id(self._c, self._base, audio, effective_email)
        resp = request_with_retry(
            self._c, "POST", f"{self._base}/api/classify-phoneme",
            json={"fileId": file_id, "language": language},
        )
        return resp.json()


class StutteringNamespace:
    def __init__(self, client: httpx.Client, base_url: str, default_email: str = "sdk@vocametrix.com") -> None:
        self._c = client
        self._base = base_url
        self._default_email = default_email

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
        /api/therapy-result/{session_id}. The server reuses its therapy-planning
        job system for stuttering classification — these therapy endpoints are
        intentional, not a routing mistake.

        Raises VocametrixServerError if the job fails or does not complete within
        `timeout` seconds.
        """
        import time as _time
        from .exceptions import VocametrixServerError

        effective_email = email if email is not None else self._default_email
        file_id = upload_assign_file_id(self._c, self._base, audio, effective_email)
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


class ProsodyNamespace:
    def __init__(self, client: httpx.Client, base_url: str, default_email: str = "sdk@vocametrix.com") -> None:
        self._c = client
        self._base = base_url
        self._default_email = default_email

    def similarity(
        self,
        model: AudioInput,
        learner: AudioInput,
        email: Optional[str] = None,
    ) -> Dict[str, Any]:
        effective_email = email if email is not None else self._default_email
        sv_id = upload_assign_file_id(self._c, self._base, model, effective_email)
        cs_id = upload_assign_file_id(self._c, self._base, learner, effective_email)
        resp = request_with_retry(
            self._c, "GET", f"{self._base}/api/calculate-prosody-similarity",
            params={"svFileId": sv_id, "csFileId": cs_id},
        )
        return resp.json()


class EgemapsNamespace:
    def __init__(self, client: httpx.Client, base_url: str, default_email: str = "sdk@vocametrix.com") -> None:
        self._c = client
        self._base = base_url
        self._default_email = default_email

    def extract(self, audio: AudioInput, email: Optional[str] = None) -> Dict[str, Any]:
        effective_email = email if email is not None else self._default_email
        file_id = upload_assign_file_id(self._c, self._base, audio, effective_email)
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
        if start_sec == 0.0:
            from .exceptions import VocametrixValidationError
            raise VocametrixValidationError(
                "start_sec=0 is rejected by the backend (treated as falsy). "
                "Pass start_sec=0.001 as the minimum offset."
            )

        blob_url = upload_blob_url(self._c, self._base, audio)
        body: Dict[str, Any] = {"blobURL": blob_url, "start_sec": start_sec}
        if end_sec is not None:
            body["end_sec"] = end_sec
        resp = request_with_retry(self._c, "POST", f"{self._base}/api/soundLevel", json=body)
        return resp.json()


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
