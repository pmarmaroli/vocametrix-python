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
        email: str = "sdk@vocametrix.com",
    ) -> None:
        key = api_key or os.environ.get("VOCAMETRIX_API_KEY")
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

    def close(self) -> None:
        self._http.close()

    def __enter__(self) -> "VocametrixClient":
        return self

    def __exit__(self, *args: object) -> None:
        self.close()


class _AsyncNamespaceProxy:
    """
    Wraps a sync namespace so every callable attribute becomes an awaitable via
    asyncio.to_thread. Namespace implementations must be stateless or thread-safe,
    since methods run in the default thread pool.
    """

    def __init__(self, sync_ns: object) -> None:
        self._sync = sync_ns

    def __getattr__(self, name: str):  # type: ignore[return]
        import asyncio
        attr = getattr(self._sync, name)
        if not callable(attr):
            return attr

        async def wrapper(*args: object, **kwargs: object) -> object:
            return await asyncio.to_thread(attr, *args, **kwargs)

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
        self.advanced = _AsyncNamespaceProxy(AdvancedVoiceAnalysisNamespace(self._sync_http, b, e))

    async def close(self) -> None:
        self._sync_http.close()
        await self._async_http.aclose()

    async def __aenter__(self) -> "AsyncVocametrixClient":
        return self

    async def __aexit__(self, *args: object) -> None:
        await self.close()
