"""Async namespace classes for AsyncVocametrixClient."""

from __future__ import annotations

from typing import Any, AsyncIterator, Dict, Optional

import httpx

from ._http import (
    AudioInput,
    request_with_retry_async,
    upload_assign_file_id_async,
    upload_blob_url_async,
    sse_stream_async,
)
from ._namespaces import TranscriptionEvent
from ._response_types import (
    AbiResult,
    AvqiResult,
    CppResult,
    DsiResult,
    EgemapsResult,
    FormantStatisticsResult,
    GneResult,
    H1H2Result,
    HnrResult,
    JitterShimmerResult,
    PhonemeResult,
    PronunciationResult,
    ProsodySimilarityResult,
    SoundLevelResult,
    SpectralResult,
    SzRatioResult,
    TtsResult,
    VoiceDynamicsResult,
    VrpResult,
)


class AsyncAvqiNamespace:
    def __init__(self, client: httpx.AsyncClient, base_url: str, default_email: str = "info@vocametrix.com") -> None:
        self._c = client
        self._base = base_url
        self._default_email = default_email

    async def calculate(
        self,
        sustained_vowel: AudioInput,
        connected_speech: Optional[AudioInput] = None,
        email: Optional[str] = None,
    ) -> AvqiResult:
        effective_email = email if email is not None else self._default_email
        sv_id = await upload_assign_file_id_async(self._c, self._base, sustained_vowel, effective_email)
        params: Dict[str, str] = {"svFileId": sv_id}
        if connected_speech is not None:
            cs_id = await upload_assign_file_id_async(self._c, self._base, connected_speech, effective_email)
            params["csFileId"] = cs_id
        resp = await request_with_retry_async(self._c, "GET", f"{self._base}/api/calculate-avqi", params=params)
        return resp.json()


class AsyncDsiNamespace:
    def __init__(self, client: httpx.AsyncClient, base_url: str, default_email: str = "info@vocametrix.com") -> None:
        self._c = client
        self._base = base_url
        self._default_email = default_email

    async def calculate(self, sustained_vowel: AudioInput, email: Optional[str] = None) -> DsiResult:
        effective_email = email if email is not None else self._default_email
        sv_id = await upload_assign_file_id_async(self._c, self._base, sustained_vowel, effective_email)
        resp = await request_with_retry_async(self._c, "GET", f"{self._base}/api/calculate-dsi", params={"svFileId": sv_id})
        return resp.json()


class AsyncCppNamespace:
    def __init__(self, client: httpx.AsyncClient, base_url: str, default_email: str = "info@vocametrix.com") -> None:
        self._c = client
        self._base = base_url
        self._default_email = default_email

    async def calculate(self, sustained_vowel: AudioInput, email: Optional[str] = None) -> CppResult:
        effective_email = email if email is not None else self._default_email
        sv_id = await upload_assign_file_id_async(self._c, self._base, sustained_vowel, effective_email)
        resp = await request_with_retry_async(self._c, "GET", f"{self._base}/api/calculate-cpp", params={"svFileId": sv_id})
        return resp.json()


class AsyncHnrNamespace:
    def __init__(self, client: httpx.AsyncClient, base_url: str, default_email: str = "info@vocametrix.com") -> None:
        self._c = client
        self._base = base_url
        self._default_email = default_email

    async def calculate(self, sustained_vowel: AudioInput, gender: int = 1, email: Optional[str] = None) -> HnrResult:
        effective_email = email if email is not None else self._default_email
        sv_id = await upload_assign_file_id_async(self._c, self._base, sustained_vowel, effective_email)
        resp = await request_with_retry_async(self._c, "GET", f"{self._base}/api/calculate-hnr-multiband", params={"svFileId": sv_id, "gender": gender})
        return resp.json()


class AsyncJitterShimmerNamespace:
    def __init__(self, client: httpx.AsyncClient, base_url: str, default_email: str = "info@vocametrix.com") -> None:
        self._c = client
        self._base = base_url
        self._default_email = default_email

    async def calculate(self, sustained_vowel: AudioInput, email: Optional[str] = None) -> JitterShimmerResult:
        effective_email = email if email is not None else self._default_email
        sv_id = await upload_assign_file_id_async(self._c, self._base, sustained_vowel, effective_email)
        resp = await request_with_retry_async(self._c, "GET", f"{self._base}/api/jitter-shimmer", params={"svFileId": sv_id})
        return resp.json()


class AsyncVrpNamespace:
    def __init__(self, client: httpx.AsyncClient, base_url: str, default_email: str = "info@vocametrix.com") -> None:
        self._c = client
        self._base = base_url
        self._default_email = default_email

    async def calculate(self, sustained_vowel: AudioInput, age: int = 30, gender: int = 1, email: Optional[str] = None) -> VrpResult:
        effective_email = email if email is not None else self._default_email
        sv_id = await upload_assign_file_id_async(self._c, self._base, sustained_vowel, effective_email)
        resp = await request_with_retry_async(self._c, "GET", f"{self._base}/api/calculate-ambitus", params={"svFileId": sv_id, "age": age, "gender": gender})
        return resp.json()


class AsyncPronunciationNamespace:
    def __init__(self, client: httpx.AsyncClient, base_url: str) -> None:
        self._c = client
        self._base = base_url

    async def assess(self, audio: AudioInput, reference_text: str, locale: str = "en-US") -> PronunciationResult:
        blob_url = await upload_blob_url_async(self._c, self._base, audio)
        resp = await request_with_retry_async(
            self._c, "POST", f"{self._base}/api/pronunciation-assessment",
            json={"blobURL": blob_url, "referenceText": reference_text, "locale": locale},
        )
        return resp.json()


class AsyncTranscriptionNamespace:
    def __init__(self, client: httpx.AsyncClient, base_url: str, api_key: str) -> None:
        self._c = client
        self._base = base_url
        self._key = api_key

    async def stream(self, audio: AudioInput, locale: str = "en-US") -> AsyncIterator[TranscriptionEvent]:
        blob_url = await upload_blob_url_async(self._c, self._base, audio)
        resp = await request_with_retry_async(
            self._c, "POST", f"{self._base}/api/offline-speech-to-text",
            json={"blobUrl": blob_url, "locale": locale},
        )
        transcription_id: str = resp.json()["transcriptionId"]
        async for payload in sse_stream_async(self._base, transcription_id, self._key):
            yield TranscriptionEvent(
                status=payload.get("status", ""),
                progress=payload.get("progress"),
                display_text=payload.get("displayText"),
                raw=payload,
            )


class AsyncTtsNamespace:
    def __init__(self, client: httpx.AsyncClient, base_url: str) -> None:
        self._c = client
        self._base = base_url

    async def synthesize(self, text: str, locale: str = "en-US", voice_name: Optional[str] = None) -> TtsResult:
        body: Dict[str, Any] = {"text": text, "locale": locale}
        if voice_name:
            body["voiceName"] = voice_name
        resp = await request_with_retry_async(self._c, "POST", f"{self._base}/api/text-to-speech", json=body)
        return resp.json()


class AsyncPhonemeNamespace:
    def __init__(self, client: httpx.AsyncClient, base_url: str, default_email: str = "info@vocametrix.com") -> None:
        self._c = client
        self._base = base_url
        self._default_email = default_email

    async def detect(self, audio: AudioInput, language: str = "fr", email: Optional[str] = None) -> PhonemeResult:
        effective_email = email if email is not None else self._default_email
        file_id = await upload_assign_file_id_async(self._c, self._base, audio, effective_email)
        resp = await request_with_retry_async(
            self._c, "POST", f"{self._base}/api/classify-phoneme",
            json={"fileId": file_id, "language": language},
        )
        return resp.json()


class AsyncStutteringNamespace:
    def __init__(self, client: httpx.AsyncClient, base_url: str, default_email: str = "info@vocametrix.com") -> None:
        self._c = client
        self._base = base_url
        self._default_email = default_email

    async def classify(
        self,
        audio: AudioInput,
        email: Optional[str] = None,
        poll_interval: float = 5.0,
        timeout: float = 620.0,
    ) -> Dict[str, Any]:
        import asyncio
        from .exceptions import VocametrixServerError

        effective_email = email if email is not None else self._default_email
        file_id = await upload_assign_file_id_async(self._c, self._base, audio, effective_email)
        resp = await request_with_retry_async(
            self._c, "POST", f"{self._base}/api/classify-stuttering",
            json={"fileId": file_id},
        )
        session_id: str = resp.json()["session_id"]

        elapsed = 0.0
        while elapsed < timeout:
            await asyncio.sleep(poll_interval)
            elapsed += poll_interval
            status_r = await request_with_retry_async(self._c, "GET", f"{self._base}/api/therapy-status/{session_id}")
            payload = status_r.json()
            state = payload.get("status", payload.get("state", ""))
            if state in ("completed", "succeeded", "done"):
                break
            if state in ("failed", "error"):
                raise VocametrixServerError(f"Stuttering classification failed: {payload}")
        else:
            raise VocametrixServerError(f"Stuttering classification timed out after {timeout}s (session={session_id})")

        result_r = await request_with_retry_async(self._c, "GET", f"{self._base}/api/therapy-result/{session_id}")
        return result_r.json()


class AsyncProsodyNamespace:
    def __init__(self, client: httpx.AsyncClient, base_url: str, default_email: str = "info@vocametrix.com") -> None:
        self._c = client
        self._base = base_url
        self._default_email = default_email

    async def similarity(self, model: AudioInput, learner: AudioInput, email: Optional[str] = None) -> ProsodySimilarityResult:
        effective_email = email if email is not None else self._default_email
        sv_id = await upload_assign_file_id_async(self._c, self._base, model, effective_email)
        cs_id = await upload_assign_file_id_async(self._c, self._base, learner, effective_email)
        resp = await request_with_retry_async(
            self._c, "GET", f"{self._base}/api/calculate-prosody-similarity",
            params={"svFileId": sv_id, "csFileId": cs_id},
        )
        return resp.json()


class AsyncEgemapsNamespace:
    def __init__(self, client: httpx.AsyncClient, base_url: str, default_email: str = "info@vocametrix.com") -> None:
        self._c = client
        self._base = base_url
        self._default_email = default_email

    async def extract(self, audio: AudioInput, email: Optional[str] = None) -> EgemapsResult:
        effective_email = email if email is not None else self._default_email
        file_id = await upload_assign_file_id_async(self._c, self._base, audio, effective_email)
        resp = await request_with_retry_async(self._c, "GET", f"{self._base}/api/gemaps-extract", params={"svFileId": file_id})
        return resp.json()


class AsyncSoundLevelNamespace:
    def __init__(self, client: httpx.AsyncClient, base_url: str) -> None:
        self._c = client
        self._base = base_url

    async def measure(self, audio: AudioInput, start_sec: float = 0.0, end_sec: Optional[float] = None) -> SoundLevelResult:
        if start_sec == 0.0:
            from .exceptions import VocametrixValidationError
            raise VocametrixValidationError(
                "start_sec=0 is rejected by the backend (treated as falsy). "
                "Pass start_sec=0.001 as the minimum offset."
            )
        blob_url = await upload_blob_url_async(self._c, self._base, audio)
        body: Dict[str, Any] = {"blobURL": blob_url, "start_sec": start_sec}
        if end_sec is not None:
            body["end_sec"] = end_sec
        resp = await request_with_retry_async(self._c, "POST", f"{self._base}/api/soundLevel", json=body)
        return resp.json()


class AsyncAdvancedVoiceAnalysisNamespace:
    def __init__(self, client: httpx.AsyncClient, base_url: str, default_email: str = "info@vocametrix.com") -> None:
        self._c = client
        self._base = base_url
        self._default_email = default_email

    async def calculate_h1h2(self, sustained_vowel: AudioInput, gender: int = 1, email: Optional[str] = None) -> H1H2Result:
        effective_email = email if email is not None else self._default_email
        sv_id = await upload_assign_file_id_async(self._c, self._base, sustained_vowel, effective_email)
        resp = await request_with_retry_async(self._c, "GET", f"{self._base}/api/calculate-h1-h2", params={"svFileId": sv_id, "gender": gender})
        return resp.json()

    async def calculate_spectral(self, sustained_vowel: AudioInput, gender: int = 1, email: Optional[str] = None) -> SpectralResult:
        effective_email = email if email is not None else self._default_email
        sv_id = await upload_assign_file_id_async(self._c, self._base, sustained_vowel, effective_email)
        resp = await request_with_retry_async(self._c, "GET", f"{self._base}/api/calculate-spectral-advanced", params={"svFileId": sv_id, "gender": gender})
        return resp.json()

    async def calculate_sz_ratio(self, sustained_vowel: AudioInput, connected_speech: AudioInput, email: Optional[str] = None) -> SzRatioResult:
        effective_email = email if email is not None else self._default_email
        sv_id = await upload_assign_file_id_async(self._c, self._base, sustained_vowel, effective_email)
        cs_id = await upload_assign_file_id_async(self._c, self._base, connected_speech, effective_email)
        resp = await request_with_retry_async(self._c, "GET", f"{self._base}/api/calculate-sz-ratio", params={"svFileId": sv_id, "csFileId": cs_id})
        return resp.json()

    async def calculate_gne(self, sustained_vowel: AudioInput, email: Optional[str] = None) -> GneResult:
        effective_email = email if email is not None else self._default_email
        sv_id = await upload_assign_file_id_async(self._c, self._base, sustained_vowel, effective_email)
        resp = await request_with_retry_async(self._c, "GET", f"{self._base}/api/calculate-gne", params={"svFileId": sv_id})
        return resp.json()

    async def calculate_formant_statistics(self, sustained_vowel: AudioInput, gender: int = 1, email: Optional[str] = None) -> FormantStatisticsResult:
        effective_email = email if email is not None else self._default_email
        sv_id = await upload_assign_file_id_async(self._c, self._base, sustained_vowel, effective_email)
        resp = await request_with_retry_async(self._c, "GET", f"{self._base}/api/calculate-formant-statistics", params={"svFileId": sv_id, "gender": gender})
        return resp.json()

    async def calculate_abi(self, sustained_vowel: AudioInput, email: Optional[str] = None) -> AbiResult:
        effective_email = email if email is not None else self._default_email
        sv_id = await upload_assign_file_id_async(self._c, self._base, sustained_vowel, effective_email)
        resp = await request_with_retry_async(self._c, "GET", f"{self._base}/api/calculate-abi", params={"svFileId": sv_id})
        return resp.json()

    async def calculate_voice_dynamics(self, sustained_vowel: AudioInput, email: Optional[str] = None) -> VoiceDynamicsResult:
        effective_email = email if email is not None else self._default_email
        sv_id = await upload_assign_file_id_async(self._c, self._base, sustained_vowel, effective_email)
        resp = await request_with_retry_async(self._c, "GET", f"{self._base}/api/calculate-voice-dynamics", params={"svFileId": sv_id})
        return resp.json()
