from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCalculateGneResponse200")


@_attrs_define
class GetCalculateGneResponse200:
    """
    Attributes:
        gne_value (float | Unset): Glottal-to-Noise Excitation Ratio on 0-1 scale. Example: 0.425
        gne_db (str | Unset): GNE expressed in decibel scale for clinical interpretation. Example: -7.4
        mean_f0 (float | Unset): Average fundamental frequency in Hz. Example: 185.3
        f0_std (float | Unset): F0 standard deviation indicating pitch stability in Hz. Example: 8.3
        hnr (float | Unset): Harmonics-to-noise ratio in dB (for comparison with GNE). Example: 12.8
        gender (str | Unset): Gender classification based on F0 range. Example: "Female"
        voice_quality (str | Unset): Qualitative assessment of voice quality. Example: "Borderline normal"
        clinical_recommendation (str | Unset): Contextual clinical guidance based on GNE value. Example: "Monitor voice
            quality. Consider vocal hygiene if symptoms persist."
        method (str | Unset): Calculation method identifier. Example: "Native_Praat_GNE"
        analysis_type (str | Unset): Analysis type descriptor. Example: "Native_Praat_GNE"
        frequency_range (float | Unset): Frequency range analyzed. Example: "500-4500 Hz"
        bandwidth (float | Unset): Bandwidth used in analysis. Example: "1000 Hz"
        step_size (float | Unset): Step size for frequency analysis. Example: "80 Hz"
        algorithm (str | Unset): Algorithm reference. Example: "Michaelis_et_al_1997"
    """

    gne_value: float | Unset = UNSET
    gne_db: str | Unset = UNSET
    mean_f0: float | Unset = UNSET
    f0_std: float | Unset = UNSET
    hnr: float | Unset = UNSET
    gender: str | Unset = UNSET
    voice_quality: str | Unset = UNSET
    clinical_recommendation: str | Unset = UNSET
    method: str | Unset = UNSET
    analysis_type: str | Unset = UNSET
    frequency_range: float | Unset = UNSET
    bandwidth: float | Unset = UNSET
    step_size: float | Unset = UNSET
    algorithm: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gne_value = self.gne_value

        gne_db = self.gne_db

        mean_f0 = self.mean_f0

        f0_std = self.f0_std

        hnr = self.hnr

        gender = self.gender

        voice_quality = self.voice_quality

        clinical_recommendation = self.clinical_recommendation

        method = self.method

        analysis_type = self.analysis_type

        frequency_range = self.frequency_range

        bandwidth = self.bandwidth

        step_size = self.step_size

        algorithm = self.algorithm

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gne_value is not UNSET:
            field_dict["GNE_VALUE"] = gne_value
        if gne_db is not UNSET:
            field_dict["GNE_DB"] = gne_db
        if mean_f0 is not UNSET:
            field_dict["MEAN_F0"] = mean_f0
        if f0_std is not UNSET:
            field_dict["F0_STD"] = f0_std
        if hnr is not UNSET:
            field_dict["HNR"] = hnr
        if gender is not UNSET:
            field_dict["GENDER"] = gender
        if voice_quality is not UNSET:
            field_dict["VOICE_QUALITY"] = voice_quality
        if clinical_recommendation is not UNSET:
            field_dict["CLINICAL_RECOMMENDATION"] = clinical_recommendation
        if method is not UNSET:
            field_dict["METHOD"] = method
        if analysis_type is not UNSET:
            field_dict["ANALYSIS_TYPE"] = analysis_type
        if frequency_range is not UNSET:
            field_dict["FREQUENCY_RANGE"] = frequency_range
        if bandwidth is not UNSET:
            field_dict["BANDWIDTH"] = bandwidth
        if step_size is not UNSET:
            field_dict["STEP_SIZE"] = step_size
        if algorithm is not UNSET:
            field_dict["ALGORITHM"] = algorithm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        gne_value = d.pop("GNE_VALUE", UNSET)

        gne_db = d.pop("GNE_DB", UNSET)

        mean_f0 = d.pop("MEAN_F0", UNSET)

        f0_std = d.pop("F0_STD", UNSET)

        hnr = d.pop("HNR", UNSET)

        gender = d.pop("GENDER", UNSET)

        voice_quality = d.pop("VOICE_QUALITY", UNSET)

        clinical_recommendation = d.pop("CLINICAL_RECOMMENDATION", UNSET)

        method = d.pop("METHOD", UNSET)

        analysis_type = d.pop("ANALYSIS_TYPE", UNSET)

        frequency_range = d.pop("FREQUENCY_RANGE", UNSET)

        bandwidth = d.pop("BANDWIDTH", UNSET)

        step_size = d.pop("STEP_SIZE", UNSET)

        algorithm = d.pop("ALGORITHM", UNSET)

        get_calculate_gne_response_200 = cls(
            gne_value=gne_value,
            gne_db=gne_db,
            mean_f0=mean_f0,
            f0_std=f0_std,
            hnr=hnr,
            gender=gender,
            voice_quality=voice_quality,
            clinical_recommendation=clinical_recommendation,
            method=method,
            analysis_type=analysis_type,
            frequency_range=frequency_range,
            bandwidth=bandwidth,
            step_size=step_size,
            algorithm=algorithm,
        )

        get_calculate_gne_response_200.additional_properties = d
        return get_calculate_gne_response_200

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
