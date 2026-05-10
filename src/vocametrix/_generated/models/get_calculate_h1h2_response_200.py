from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCalculateH1H2Response200")


@_attrs_define
class GetCalculateH1H2Response200:
    """
    Attributes:
        h1_h2 (float | Unset): Raw (uncorrected) H1-H2 in dB. Amplitude difference between first and second harmonics
            without formant correction. Use for comparison with corrected value. Example: 5.88
        h1_h2_corrected (float | Unset): Formant-corrected H1*-H2* in dB. Primary measure accounting for vocal tract
            resonance effects using Iseli & Alwan (2004) algorithm. Higher values may indicate breathier voice quality.
            Example: 10.93
        mean_f0 (float | Unset): Mean fundamental frequency in Hz. Averaged across all valid frames in the stable vowel
            portion. Example: 134.76
        f1_mean (float | Unset): Mean first formant frequency in Hz. Extracted using Praat Burg algorithm. Vowel height
            correlate. Example: 473.00
        f2_mean (float | Unset): Mean second formant frequency in Hz. Extracted using Praat Burg algorithm. Vowel
            frontness/backness correlate. Example: 1183.97
        b1_mean (float | Unset): Estimated first formant bandwidth in Hz. Calculated using Hawk & Miller (1995) formula:
            B1 = 50 + (F1/10). Used for formant correction. Example: 97.30
        b2_mean (float | Unset): Estimated second formant bandwidth in Hz. Calculated using Hawk & Miller (1995)
            formula: B2 = 70 + (F2/50). Used for formant correction. Example: 93.68
        frames_analyzed (float | Unset): Number of valid frames analyzed. Frame shift = 1ms, window = 3 pitch periods.
            Higher counts indicate longer recordings or more stable voicing. Example: 2977
        gender (float | Unset): Gender classification used for formant analysis. Determines formant ceiling frequency.
            Example: "Male" or "Female (F0-based)"
    """

    h1_h2: float | Unset = UNSET
    h1_h2_corrected: float | Unset = UNSET
    mean_f0: float | Unset = UNSET
    f1_mean: float | Unset = UNSET
    f2_mean: float | Unset = UNSET
    b1_mean: float | Unset = UNSET
    b2_mean: float | Unset = UNSET
    frames_analyzed: float | Unset = UNSET
    gender: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        h1_h2 = self.h1_h2

        h1_h2_corrected = self.h1_h2_corrected

        mean_f0 = self.mean_f0

        f1_mean = self.f1_mean

        f2_mean = self.f2_mean

        b1_mean = self.b1_mean

        b2_mean = self.b2_mean

        frames_analyzed = self.frames_analyzed

        gender = self.gender

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if h1_h2 is not UNSET:
            field_dict["H1_H2"] = h1_h2
        if h1_h2_corrected is not UNSET:
            field_dict["H1_H2_CORRECTED"] = h1_h2_corrected
        if mean_f0 is not UNSET:
            field_dict["MEAN_F0"] = mean_f0
        if f1_mean is not UNSET:
            field_dict["F1_MEAN"] = f1_mean
        if f2_mean is not UNSET:
            field_dict["F2_MEAN"] = f2_mean
        if b1_mean is not UNSET:
            field_dict["B1_MEAN"] = b1_mean
        if b2_mean is not UNSET:
            field_dict["B2_MEAN"] = b2_mean
        if frames_analyzed is not UNSET:
            field_dict["FRAMES_ANALYZED"] = frames_analyzed
        if gender is not UNSET:
            field_dict["GENDER"] = gender

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        h1_h2 = d.pop("H1_H2", UNSET)

        h1_h2_corrected = d.pop("H1_H2_CORRECTED", UNSET)

        mean_f0 = d.pop("MEAN_F0", UNSET)

        f1_mean = d.pop("F1_MEAN", UNSET)

        f2_mean = d.pop("F2_MEAN", UNSET)

        b1_mean = d.pop("B1_MEAN", UNSET)

        b2_mean = d.pop("B2_MEAN", UNSET)

        frames_analyzed = d.pop("FRAMES_ANALYZED", UNSET)

        gender = d.pop("GENDER", UNSET)

        get_calculate_h1h2_response_200 = cls(
            h1_h2=h1_h2,
            h1_h2_corrected=h1_h2_corrected,
            mean_f0=mean_f0,
            f1_mean=f1_mean,
            f2_mean=f2_mean,
            b1_mean=b1_mean,
            b2_mean=b2_mean,
            frames_analyzed=frames_analyzed,
            gender=gender,
        )

        get_calculate_h1h2_response_200.additional_properties = d
        return get_calculate_h1h2_response_200

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
