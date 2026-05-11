"""TypedDict definitions for namespace method return types.

These provide IDE autocomplete and mypy/pyright field-level checking.
Fields are total=False (all optional) since API response shapes vary
by input parameters and backend version.
"""

from __future__ import annotations

from typing import Any, Dict, List, TypedDict


class AvqiResult(TypedDict, total=False):
    AVQI: float
    CPP: float
    HNR: float
    Jitter: float
    Shimmer: float
    MPT: float


class DsiResult(TypedDict, total=False):
    DSI: float
    F0_high: float
    F0_low: float
    I_high: float
    I_low: float
    MPT: float


class CppResult(TypedDict, total=False):
    CPP: float
    CPPS: float


class HnrResult(TypedDict, total=False):
    HNR: float
    HNR_500: float
    HNR_1500: float
    HNR_2500: float
    HNR_3500: float


class JitterShimmerResult(TypedDict, total=False):
    Jitter_local: float
    Jitter_rap: float
    Jitter_ppq5: float
    Shimmer_local: float
    Shimmer_apq3: float
    Shimmer_apq5: float


class VrpResult(TypedDict, total=False):
    ambitus: float
    F0_min: float
    F0_max: float
    I_min: float
    I_max: float


class PronunciationResult(TypedDict, total=False):
    accuracyScore: float
    completenessScore: float
    fluencyScore: float
    pronScore: float
    words: List[Dict[str, Any]]


class TtsResult(TypedDict, total=False):
    audioUrl: str
    duration: float


class PhonemeResult(TypedDict, total=False):
    phonemes: List[Dict[str, Any]]
    language: str


class ProsodySimilarityResult(TypedDict, total=False):
    similarity: float
    score: float


class EgemapsResult(TypedDict, total=False):
    features: Dict[str, float]
    metadata: Dict[str, Any]


class SoundLevelResult(TypedDict, total=False):
    dB: float
    dB_SPL: float


class H1H2Result(TypedDict, total=False):
    H1: float
    H2: float
    H1H2: float


class SpectralResult(TypedDict, total=False):
    H1H2: float
    H2H4: float
    H4H2kHz: float
    H2kHz5kHz: float


class SzRatioResult(TypedDict, total=False):
    sz_ratio: float
    s_duration: float
    z_duration: float


class GneResult(TypedDict, total=False):
    GNE: float


class FormantStatisticsResult(TypedDict, total=False):
    F1_mean: float
    F2_mean: float
    F3_mean: float
    F1_std: float
    F2_std: float
    F3_std: float


class AbiResult(TypedDict, total=False):
    ABI: float


class VoiceDynamicsResult(TypedDict, total=False):
    perturbation: Dict[str, float]
