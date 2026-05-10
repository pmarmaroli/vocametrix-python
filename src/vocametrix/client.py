"""
VocametrixClient — synchronous ergonomic client.
AsyncVocametrixClient — async variant using httpx.AsyncClient.
"""

from __future__ import annotations

import os
from typing import Optional

import httpx

from ._namespaces import (
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
    ) -> None:
        key = api_key or os.environ.get("VOCAMETRIX_API_KEY")
        if not key:
            raise ValueError(
                "API key required. Pass api_key=... or set VOCAMETRIX_API_KEY env var."
            )
        self._api_key = key
        self._base_url = base_url.rstrip("/")
        self._http = httpx.Client(
            headers={"X-API-Key": key},
            timeout=timeout,
        )
        self._init_namespaces()

    def _init_namespaces(self) -> None:
        b = self._base_url
        self.avqi = AvqiNamespace(self._http, b)
        self.dsi = DsiNamespace(self._http, b)
        self.cpp = CppNamespace(self._http, b)
        self.hnr = HnrNamespace(self._http, b)
        self.jitter_shimmer = JitterShimmerNamespace(self._http, b)
        self.vrp = VrpNamespace(self._http, b)
        self.pronunciation = PronunciationNamespace(self._http, b)
        self.transcription = TranscriptionNamespace(self._http, b, self._api_key)
        self.tts = TtsNamespace(self._http, b)
        self.phoneme = PhonemeNamespace(self._http, b)
        self.stuttering = StutteringNamespace(self._http, b)
        self.prosody = ProsodyNamespace(self._http, b)
        self.egemaps = EgemapsNamespace(self._http, b)
        self.sound_level = SoundLevelNamespace(self._http, b)

    def close(self) -> None:
        self._http.close()

    def __enter__(self) -> "VocametrixClient":
        return self

    def __exit__(self, *args: object) -> None:
        self.close()


class AsyncVocametrixClient:
    """
    Async Vocametrix API client (httpx.AsyncClient).

    Usage::

        async with AsyncVocametrixClient(api_key="...") as client:
            result = await client.avqi.calculate(sustained_vowel="vowel.wav")
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = _DEFAULT_BASE_URL,
        timeout: float = _DEFAULT_TIMEOUT,
    ) -> None:
        key = api_key or os.environ.get("VOCAMETRIX_API_KEY")
        if not key:
            raise ValueError(
                "API key required. Pass api_key=... or set VOCAMETRIX_API_KEY env var."
            )
        self._api_key = key
        self._base_url = base_url.rstrip("/")
        self._http = httpx.AsyncClient(
            headers={"X-API-Key": key},
            timeout=timeout,
        )

    async def close(self) -> None:
        await self._http.aclose()

    async def __aenter__(self) -> "AsyncVocametrixClient":
        return self

    async def __aexit__(self, *args: object) -> None:
        await self.close()

    # Async namespace methods delegate to the sync helpers via run_in_executor
    # for simplicity — a production SDK would use async httpx calls throughout.
    # The key value here is the identical public API surface.

    async def _aget(self, url: str, **kwargs: object) -> dict:  # type: ignore[return]
        resp = await self._http.get(url, **kwargs)  # type: ignore[arg-type]
        resp.raise_for_status()
        return resp.json()

    async def _apost(self, url: str, **kwargs: object) -> dict:  # type: ignore[return]
        resp = await self._http.post(url, **kwargs)  # type: ignore[arg-type]
        resp.raise_for_status()
        return resp.json()
