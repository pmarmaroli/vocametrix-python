"""
VocametrixClient — synchronous ergonomic client.
AsyncVocametrixClient — async variant using httpx.AsyncClient.
"""

from __future__ import annotations

import os
from typing import Optional

import httpx

from ._namespaces import (
    AdvancedVoiceAnalysisNamespace,
    AiAgentsNamespace,
    AvqiNamespace,
    CppNamespace,
    DsiNamespace,
    EgemapsNamespace,
    HnrNamespace,
    JitterShimmerNamespace,
    PhonemeNamespace,
    PronunciationNamespace,
    ProsodyNamespace,
    SoundLevelNamespace,
    StutteringNamespace,
    TranscriptionNamespace,
    TtsNamespace,
    VrpNamespace,
)

_DEFAULT_BASE_URL = "https://platform.vocametrix.com"
_DEFAULT_TIMEOUT = 120.0
_DEFAULT_EMAIL = "info@vocametrix.com"


class VocametrixClient:
    """
    Synchronous Vocametrix API client.

    Usage::

        from vocametrix import VocametrixClient

        client = VocametrixClient(api_key="...")
        result = client.avqi.calculate(sustained_vowel="vowel.wav")
        print(result["AVQI"])
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = _DEFAULT_BASE_URL,
        timeout: float = _DEFAULT_TIMEOUT,
        email: str = _DEFAULT_EMAIL,
    ) -> None:
        raw_key = api_key or os.environ.get("VOCAMETRIX_API_KEY")
        key = raw_key.strip() if raw_key else None
        if not key:
            raise ValueError(
                "API key required. Pass api_key=... or set VOCAMETRIX_API_KEY env var."
            )
        self._api_key = key
        self._base_url = base_url.rstrip("/")
        self._email = email
        self._http = httpx.Client(
            headers={"X-API-Key": key},
            timeout=timeout,
        )
        self._init_namespaces()

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
        self.advanced = AdvancedVoiceAnalysisNamespace(self._http, b, e)
        self.ai_agents = AiAgentsNamespace(self._http, b)

    def close(self) -> None:
        self._http.close()

    def __enter__(self) -> "VocametrixClient":
        return self

    def __exit__(self, *args: object) -> None:
        self.close()


class AsyncVocametrixClient:
    """
    Async Vocametrix API client using httpx.AsyncClient for true async I/O.

    Usage::

        async with AsyncVocametrixClient(api_key="...") as client:
            result = await client.avqi.calculate(sustained_vowel="vowel.wav")
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = _DEFAULT_BASE_URL,
        timeout: float = _DEFAULT_TIMEOUT,
        email: str = _DEFAULT_EMAIL,
    ) -> None:
        raw_key = api_key or os.environ.get("VOCAMETRIX_API_KEY")
        key = raw_key.strip() if raw_key else None
        if not key:
            raise ValueError(
                "API key required. Pass api_key=... or set VOCAMETRIX_API_KEY env var."
            )
        self._api_key = key
        self._email = email
        self._base_url = base_url.rstrip("/")
        self._http = httpx.AsyncClient(
            headers={"X-API-Key": key},
            timeout=timeout,
        )
        self._init_namespaces()

    def _init_namespaces(self) -> None:
        from ._async_namespaces import (
            AsyncAdvancedVoiceAnalysisNamespace,
            AsyncAiAgentsNamespace,
            AsyncAvqiNamespace,
            AsyncCppNamespace,
            AsyncDsiNamespace,
            AsyncEgemapsNamespace,
            AsyncHnrNamespace,
            AsyncJitterShimmerNamespace,
            AsyncPhonemeNamespace,
            AsyncPronunciationNamespace,
            AsyncProsodyNamespace,
            AsyncSoundLevelNamespace,
            AsyncStutteringNamespace,
            AsyncTranscriptionNamespace,
            AsyncTtsNamespace,
            AsyncVrpNamespace,
        )
        b = self._base_url
        e = self._email
        h = self._http
        self.avqi = AsyncAvqiNamespace(h, b, e)
        self.dsi = AsyncDsiNamespace(h, b, e)
        self.cpp = AsyncCppNamespace(h, b, e)
        self.hnr = AsyncHnrNamespace(h, b, e)
        self.jitter_shimmer = AsyncJitterShimmerNamespace(h, b, e)
        self.vrp = AsyncVrpNamespace(h, b, e)
        self.pronunciation = AsyncPronunciationNamespace(h, b)
        self.transcription = AsyncTranscriptionNamespace(h, b, self._api_key)
        self.tts = AsyncTtsNamespace(h, b)
        self.phoneme = AsyncPhonemeNamespace(h, b, e)
        self.stuttering = AsyncStutteringNamespace(h, b, e)
        self.prosody = AsyncProsodyNamespace(h, b, e)
        self.egemaps = AsyncEgemapsNamespace(h, b, e)
        self.sound_level = AsyncSoundLevelNamespace(h, b)
        self.advanced = AsyncAdvancedVoiceAnalysisNamespace(h, b, e)
        self.ai_agents = AsyncAiAgentsNamespace(h, b)

    async def close(self) -> None:
        await self._http.aclose()

    async def __aenter__(self) -> "AsyncVocametrixClient":
        return self

    async def __aexit__(self, *args: object) -> None:
        await self.close()
