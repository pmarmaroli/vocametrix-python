from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCalculateAbiResponse200")


@_attrs_define
class GetCalculateAbiResponse200:
    """
    Attributes:
        abi_score (float | Unset): Acoustic Breathiness Index — composite multi-component score (number).
        cpps (float | Unset): Cepstral Peak Prominence (Smoothed) in dB — harmonic-to-aperiodic structure indicator.
        jitter_percent (float | Unset): Local jitter as a percentage — period perturbation.
        gne_approximation (str | Unset): Approximate Glottal-to-Noise Excitation ratio.
        hnr_6khz (str | Unset): Harmonics-to-Noise Ratio computed in the 0–6 kHz band (dB).
        hnr_dejonckere (str | Unset): HNR computed using De Jonckere's method (dB).
        h1_h2_diff (float | Unset): Difference between the first two harmonic amplitudes (H1 − H2) in dB — voice source
            quality indicator.
        shimmer_db (str | Unset): Shimmer in logarithmic scale (dB).
        shimmer_percent (float | Unset): Shimmer as a percentage.
        period_std (str | Unset): Standard deviation of glottal period (period stability).
        cs_duration (float | Unset): Connected speech recording duration in seconds.
        sv_duration (float | Unset): Sustained vowel recording duration in seconds.
        cs_duration_used (str | Unset): Portion of CS actually analyzed (after silence trimming).
        sv_duration_used (str | Unset): Portion of SV actually analyzed.
        total_analysis_duration (str | Unset): Sum of CS_DURATION_USED + SV_DURATION_USED.
        abi_reference (str | Unset): Clinical reference text emitted by the analysis script (interpretive guidance).
        analysis_version (str | Unset): Algorithm version, e.g. "ABI_v01".
    """

    abi_score: float | Unset = UNSET
    cpps: float | Unset = UNSET
    jitter_percent: float | Unset = UNSET
    gne_approximation: str | Unset = UNSET
    hnr_6khz: str | Unset = UNSET
    hnr_dejonckere: str | Unset = UNSET
    h1_h2_diff: float | Unset = UNSET
    shimmer_db: str | Unset = UNSET
    shimmer_percent: float | Unset = UNSET
    period_std: str | Unset = UNSET
    cs_duration: float | Unset = UNSET
    sv_duration: float | Unset = UNSET
    cs_duration_used: str | Unset = UNSET
    sv_duration_used: str | Unset = UNSET
    total_analysis_duration: str | Unset = UNSET
    abi_reference: str | Unset = UNSET
    analysis_version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        abi_score = self.abi_score

        cpps = self.cpps

        jitter_percent = self.jitter_percent

        gne_approximation = self.gne_approximation

        hnr_6khz = self.hnr_6khz

        hnr_dejonckere = self.hnr_dejonckere

        h1_h2_diff = self.h1_h2_diff

        shimmer_db = self.shimmer_db

        shimmer_percent = self.shimmer_percent

        period_std = self.period_std

        cs_duration = self.cs_duration

        sv_duration = self.sv_duration

        cs_duration_used = self.cs_duration_used

        sv_duration_used = self.sv_duration_used

        total_analysis_duration = self.total_analysis_duration

        abi_reference = self.abi_reference

        analysis_version = self.analysis_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if abi_score is not UNSET:
            field_dict["ABI_SCORE"] = abi_score
        if cpps is not UNSET:
            field_dict["CPPS"] = cpps
        if jitter_percent is not UNSET:
            field_dict["JITTER_PERCENT"] = jitter_percent
        if gne_approximation is not UNSET:
            field_dict["GNE_APPROXIMATION"] = gne_approximation
        if hnr_6khz is not UNSET:
            field_dict["HNR_6KHZ"] = hnr_6khz
        if hnr_dejonckere is not UNSET:
            field_dict["HNR_DEJONCKERE"] = hnr_dejonckere
        if h1_h2_diff is not UNSET:
            field_dict["H1_H2_DIFF"] = h1_h2_diff
        if shimmer_db is not UNSET:
            field_dict["SHIMMER_DB"] = shimmer_db
        if shimmer_percent is not UNSET:
            field_dict["SHIMMER_PERCENT"] = shimmer_percent
        if period_std is not UNSET:
            field_dict["PERIOD_STD"] = period_std
        if cs_duration is not UNSET:
            field_dict["CS_DURATION"] = cs_duration
        if sv_duration is not UNSET:
            field_dict["SV_DURATION"] = sv_duration
        if cs_duration_used is not UNSET:
            field_dict["CS_DURATION_USED"] = cs_duration_used
        if sv_duration_used is not UNSET:
            field_dict["SV_DURATION_USED"] = sv_duration_used
        if total_analysis_duration is not UNSET:
            field_dict["TOTAL_ANALYSIS_DURATION"] = total_analysis_duration
        if abi_reference is not UNSET:
            field_dict["ABI_REFERENCE"] = abi_reference
        if analysis_version is not UNSET:
            field_dict["ANALYSIS_VERSION"] = analysis_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        abi_score = d.pop("ABI_SCORE", UNSET)

        cpps = d.pop("CPPS", UNSET)

        jitter_percent = d.pop("JITTER_PERCENT", UNSET)

        gne_approximation = d.pop("GNE_APPROXIMATION", UNSET)

        hnr_6khz = d.pop("HNR_6KHZ", UNSET)

        hnr_dejonckere = d.pop("HNR_DEJONCKERE", UNSET)

        h1_h2_diff = d.pop("H1_H2_DIFF", UNSET)

        shimmer_db = d.pop("SHIMMER_DB", UNSET)

        shimmer_percent = d.pop("SHIMMER_PERCENT", UNSET)

        period_std = d.pop("PERIOD_STD", UNSET)

        cs_duration = d.pop("CS_DURATION", UNSET)

        sv_duration = d.pop("SV_DURATION", UNSET)

        cs_duration_used = d.pop("CS_DURATION_USED", UNSET)

        sv_duration_used = d.pop("SV_DURATION_USED", UNSET)

        total_analysis_duration = d.pop("TOTAL_ANALYSIS_DURATION", UNSET)

        abi_reference = d.pop("ABI_REFERENCE", UNSET)

        analysis_version = d.pop("ANALYSIS_VERSION", UNSET)

        get_calculate_abi_response_200 = cls(
            abi_score=abi_score,
            cpps=cpps,
            jitter_percent=jitter_percent,
            gne_approximation=gne_approximation,
            hnr_6khz=hnr_6khz,
            hnr_dejonckere=hnr_dejonckere,
            h1_h2_diff=h1_h2_diff,
            shimmer_db=shimmer_db,
            shimmer_percent=shimmer_percent,
            period_std=period_std,
            cs_duration=cs_duration,
            sv_duration=sv_duration,
            cs_duration_used=cs_duration_used,
            sv_duration_used=sv_duration_used,
            total_analysis_duration=total_analysis_duration,
            abi_reference=abi_reference,
            analysis_version=analysis_version,
        )

        get_calculate_abi_response_200.additional_properties = d
        return get_calculate_abi_response_200

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
