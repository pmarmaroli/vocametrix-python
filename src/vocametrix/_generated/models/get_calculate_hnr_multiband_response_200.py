from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCalculateHnrMultibandResponse200")


@_attrs_define
class GetCalculateHnrMultibandResponse200:
    """
    Attributes:
        hnr_full (float | Unset): Full-spectrum HNR (80-8000 Hz) in dB. Example: 15.4
        hnr_low (float | Unset): Low-frequency HNR (80-500 Hz) in dB. Example: 18.2
        hnr_mid (float | Unset): Mid-frequency HNR (500-1500 Hz) in dB. Example: 16.8
        hnr_high (float | Unset): High-frequency HNR (1500-3500 Hz) in dB. Example: 12.3
        mean_f0 (float | Unset): Mean fundamental frequency in Hz. Example: 195.4
        f0_std (str | Unset): Standard deviation of F0. Example: 8.5
        gender (str | Unset): Gender classification result. Example: "Female"
        noise_ratio_low (float | Unset): Low-frequency noise percentage. Example: 12.5
        noise_ratio_mid (float | Unset): Mid-frequency noise percentage. Example: 18.2
        noise_ratio_high (float | Unset): High-frequency noise percentage. Example: 25.7
        hnr_slope (float | Unset): Spectral tilt across frequency bands. Example: -0.68
        overall_quality (str | Unset): Clinical voice quality assessment. Example: "Good voice quality"
        severity (str | Unset): Voice quality severity classification. Example: "Normal"
        noise_pattern (float | Unset): Dominant noise pattern classification. Example: "Low-frequency emphasis"
        breathiness (str | Unset): Breathiness assessment. Example: "Minimal breathiness"
        patient_age (str | Unset): Patient age used in analysis. Example: 35
        patient_gender (str | Unset): Patient gender classification. Example: "Female"
        age_group (str | Unset): Age group classification. Example: "Young Adult"
        age_note (str | Unset): Age-related clinical note. Example: "Age within normal vocal range"
        f0_note (str | Unset): F0 validation note. Example: "F0 within expected range for gender/age"
        gender_note (str | Unset): Gender-specific note. Example: "Female vocal characteristics confirmed"
        expected_f0_min (str | Unset): Expected minimum F0 for age/gender. Example: 165.4
        expected_f0_max (str | Unset): Expected maximum F0 for age/gender. Example: 294.3
        hnr_adjustment (str | Unset): Age-based threshold adjustment applied. Example: 0.8
        adjusted_hnr_full (str | Unset): Age-adjusted full-spectrum HNR. Example: 16.2
    """

    hnr_full: float | Unset = UNSET
    hnr_low: float | Unset = UNSET
    hnr_mid: float | Unset = UNSET
    hnr_high: float | Unset = UNSET
    mean_f0: float | Unset = UNSET
    f0_std: str | Unset = UNSET
    gender: str | Unset = UNSET
    noise_ratio_low: float | Unset = UNSET
    noise_ratio_mid: float | Unset = UNSET
    noise_ratio_high: float | Unset = UNSET
    hnr_slope: float | Unset = UNSET
    overall_quality: str | Unset = UNSET
    severity: str | Unset = UNSET
    noise_pattern: float | Unset = UNSET
    breathiness: str | Unset = UNSET
    patient_age: str | Unset = UNSET
    patient_gender: str | Unset = UNSET
    age_group: str | Unset = UNSET
    age_note: str | Unset = UNSET
    f0_note: str | Unset = UNSET
    gender_note: str | Unset = UNSET
    expected_f0_min: str | Unset = UNSET
    expected_f0_max: str | Unset = UNSET
    hnr_adjustment: str | Unset = UNSET
    adjusted_hnr_full: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hnr_full = self.hnr_full

        hnr_low = self.hnr_low

        hnr_mid = self.hnr_mid

        hnr_high = self.hnr_high

        mean_f0 = self.mean_f0

        f0_std = self.f0_std

        gender = self.gender

        noise_ratio_low = self.noise_ratio_low

        noise_ratio_mid = self.noise_ratio_mid

        noise_ratio_high = self.noise_ratio_high

        hnr_slope = self.hnr_slope

        overall_quality = self.overall_quality

        severity = self.severity

        noise_pattern = self.noise_pattern

        breathiness = self.breathiness

        patient_age = self.patient_age

        patient_gender = self.patient_gender

        age_group = self.age_group

        age_note = self.age_note

        f0_note = self.f0_note

        gender_note = self.gender_note

        expected_f0_min = self.expected_f0_min

        expected_f0_max = self.expected_f0_max

        hnr_adjustment = self.hnr_adjustment

        adjusted_hnr_full = self.adjusted_hnr_full

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hnr_full is not UNSET:
            field_dict["HNR_FULL"] = hnr_full
        if hnr_low is not UNSET:
            field_dict["HNR_LOW"] = hnr_low
        if hnr_mid is not UNSET:
            field_dict["HNR_MID"] = hnr_mid
        if hnr_high is not UNSET:
            field_dict["HNR_HIGH"] = hnr_high
        if mean_f0 is not UNSET:
            field_dict["MEAN_F0"] = mean_f0
        if f0_std is not UNSET:
            field_dict["F0_STD"] = f0_std
        if gender is not UNSET:
            field_dict["GENDER"] = gender
        if noise_ratio_low is not UNSET:
            field_dict["NOISE_RATIO_LOW"] = noise_ratio_low
        if noise_ratio_mid is not UNSET:
            field_dict["NOISE_RATIO_MID"] = noise_ratio_mid
        if noise_ratio_high is not UNSET:
            field_dict["NOISE_RATIO_HIGH"] = noise_ratio_high
        if hnr_slope is not UNSET:
            field_dict["HNR_SLOPE"] = hnr_slope
        if overall_quality is not UNSET:
            field_dict["OVERALL_QUALITY"] = overall_quality
        if severity is not UNSET:
            field_dict["SEVERITY"] = severity
        if noise_pattern is not UNSET:
            field_dict["NOISE_PATTERN"] = noise_pattern
        if breathiness is not UNSET:
            field_dict["BREATHINESS"] = breathiness
        if patient_age is not UNSET:
            field_dict["PATIENT_AGE"] = patient_age
        if patient_gender is not UNSET:
            field_dict["PATIENT_GENDER"] = patient_gender
        if age_group is not UNSET:
            field_dict["AGE_GROUP"] = age_group
        if age_note is not UNSET:
            field_dict["AGE_NOTE"] = age_note
        if f0_note is not UNSET:
            field_dict["F0_NOTE"] = f0_note
        if gender_note is not UNSET:
            field_dict["GENDER_NOTE"] = gender_note
        if expected_f0_min is not UNSET:
            field_dict["EXPECTED_F0_MIN"] = expected_f0_min
        if expected_f0_max is not UNSET:
            field_dict["EXPECTED_F0_MAX"] = expected_f0_max
        if hnr_adjustment is not UNSET:
            field_dict["HNR_ADJUSTMENT"] = hnr_adjustment
        if adjusted_hnr_full is not UNSET:
            field_dict["ADJUSTED_HNR_FULL"] = adjusted_hnr_full

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hnr_full = d.pop("HNR_FULL", UNSET)

        hnr_low = d.pop("HNR_LOW", UNSET)

        hnr_mid = d.pop("HNR_MID", UNSET)

        hnr_high = d.pop("HNR_HIGH", UNSET)

        mean_f0 = d.pop("MEAN_F0", UNSET)

        f0_std = d.pop("F0_STD", UNSET)

        gender = d.pop("GENDER", UNSET)

        noise_ratio_low = d.pop("NOISE_RATIO_LOW", UNSET)

        noise_ratio_mid = d.pop("NOISE_RATIO_MID", UNSET)

        noise_ratio_high = d.pop("NOISE_RATIO_HIGH", UNSET)

        hnr_slope = d.pop("HNR_SLOPE", UNSET)

        overall_quality = d.pop("OVERALL_QUALITY", UNSET)

        severity = d.pop("SEVERITY", UNSET)

        noise_pattern = d.pop("NOISE_PATTERN", UNSET)

        breathiness = d.pop("BREATHINESS", UNSET)

        patient_age = d.pop("PATIENT_AGE", UNSET)

        patient_gender = d.pop("PATIENT_GENDER", UNSET)

        age_group = d.pop("AGE_GROUP", UNSET)

        age_note = d.pop("AGE_NOTE", UNSET)

        f0_note = d.pop("F0_NOTE", UNSET)

        gender_note = d.pop("GENDER_NOTE", UNSET)

        expected_f0_min = d.pop("EXPECTED_F0_MIN", UNSET)

        expected_f0_max = d.pop("EXPECTED_F0_MAX", UNSET)

        hnr_adjustment = d.pop("HNR_ADJUSTMENT", UNSET)

        adjusted_hnr_full = d.pop("ADJUSTED_HNR_FULL", UNSET)

        get_calculate_hnr_multiband_response_200 = cls(
            hnr_full=hnr_full,
            hnr_low=hnr_low,
            hnr_mid=hnr_mid,
            hnr_high=hnr_high,
            mean_f0=mean_f0,
            f0_std=f0_std,
            gender=gender,
            noise_ratio_low=noise_ratio_low,
            noise_ratio_mid=noise_ratio_mid,
            noise_ratio_high=noise_ratio_high,
            hnr_slope=hnr_slope,
            overall_quality=overall_quality,
            severity=severity,
            noise_pattern=noise_pattern,
            breathiness=breathiness,
            patient_age=patient_age,
            patient_gender=patient_gender,
            age_group=age_group,
            age_note=age_note,
            f0_note=f0_note,
            gender_note=gender_note,
            expected_f0_min=expected_f0_min,
            expected_f0_max=expected_f0_max,
            hnr_adjustment=hnr_adjustment,
            adjusted_hnr_full=adjusted_hnr_full,
        )

        get_calculate_hnr_multiband_response_200.additional_properties = d
        return get_calculate_hnr_multiband_response_200

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
