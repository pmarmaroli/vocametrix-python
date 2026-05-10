from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCalculateSzRatioResponse200")


@_attrs_define
class GetCalculateSzRatioResponse200:
    """
    Attributes:
        s_phonation_time (float | Unset): Total sustained /s/ phonation duration in seconds. Example: 18.7
        z_phonation_time (float | Unset): Total sustained /z/ phonation duration in seconds. Example: 19.2
        sz_ratio (str | Unset): S/Z phonation time ratio (primary clinical measure). Example: 0.97
        s_efficiency (float | Unset): Percentage of /s/ recording with actual phonation. Example: 85.4
        z_efficiency (float | Unset): Percentage of /z/ recording with actual phonation. Example: 87.2
        s_phonation_segments (float | Unset): Number of continuous /s/ phonation segments. Example: 3
        z_phonation_segments (float | Unset): Number of continuous /z/ phonation segments. Example: 2
        s_longest_segment (float | Unset): /s/ longest continuous segment duration in seconds. Example: 12.5
        z_longest_segment (float | Unset): /z/ longest continuous segment duration in seconds. Example: 15.8
        mean_f0_z (float | Unset): Mean fundamental frequency during /z/ phonation in Hz. Example: 195.8
        f0_std_z (float | Unset): Standard deviation of F0 during /z/ phonation in Hz. Example: 8.3
        f0_cv_z (str | Unset): Coefficient of variation of F0 during /z/ in %. Example: 4.2
        reliability_score (float | Unset): Composite reliability score (0-4). Example: 3.8
        presbylaryngis_risk (str | Unset): Age-related voice changes risk (0/1). Example: 0
        sz_interpretation (str | Unset): Clinical classification with age adjustment. Example: "Normal S/Z ratio"
        clinical_significance (str | Unset): Pathophysiology interpretation. Example: "No evidence of vocal fold mass
            lesions"
        risk_level (str | Unset): Stratified risk assessment. Example: "Low"
        reliability (str | Unset): Test reliability classification. Example: "High reliability"
        age_adjustment (str | Unset): Age-specific interpretation note. Example: "No age-related adjustments needed"
        gender (str | Unset): Gender classification. Example: "Female"
        patient_age (str | Unset): Patient age in years. Example: 35
        patient_gender (str | Unset): Patient gender classification. Example: "Female"
        age_group (str | Unset): Age-based clinical grouping. Example: "Young Adult"
        age_note (str | Unset): Age-related clinical note. Example: "Age within normal vocal range"
        gender_note (str | Unset): Gender-specific clinical note. Example: "Female-typical phonation patterns"
        expected_sz_range (str | Unset): Expected S/Z ratio range for demographics. Example: "0.85-1.15"
        phonation_quality (str | Unset): Overall phonation quality assessment. Example: "Good phonatory control"
    """

    s_phonation_time: float | Unset = UNSET
    z_phonation_time: float | Unset = UNSET
    sz_ratio: str | Unset = UNSET
    s_efficiency: float | Unset = UNSET
    z_efficiency: float | Unset = UNSET
    s_phonation_segments: float | Unset = UNSET
    z_phonation_segments: float | Unset = UNSET
    s_longest_segment: float | Unset = UNSET
    z_longest_segment: float | Unset = UNSET
    mean_f0_z: float | Unset = UNSET
    f0_std_z: float | Unset = UNSET
    f0_cv_z: str | Unset = UNSET
    reliability_score: float | Unset = UNSET
    presbylaryngis_risk: str | Unset = UNSET
    sz_interpretation: str | Unset = UNSET
    clinical_significance: str | Unset = UNSET
    risk_level: str | Unset = UNSET
    reliability: str | Unset = UNSET
    age_adjustment: str | Unset = UNSET
    gender: str | Unset = UNSET
    patient_age: str | Unset = UNSET
    patient_gender: str | Unset = UNSET
    age_group: str | Unset = UNSET
    age_note: str | Unset = UNSET
    gender_note: str | Unset = UNSET
    expected_sz_range: str | Unset = UNSET
    phonation_quality: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        s_phonation_time = self.s_phonation_time

        z_phonation_time = self.z_phonation_time

        sz_ratio = self.sz_ratio

        s_efficiency = self.s_efficiency

        z_efficiency = self.z_efficiency

        s_phonation_segments = self.s_phonation_segments

        z_phonation_segments = self.z_phonation_segments

        s_longest_segment = self.s_longest_segment

        z_longest_segment = self.z_longest_segment

        mean_f0_z = self.mean_f0_z

        f0_std_z = self.f0_std_z

        f0_cv_z = self.f0_cv_z

        reliability_score = self.reliability_score

        presbylaryngis_risk = self.presbylaryngis_risk

        sz_interpretation = self.sz_interpretation

        clinical_significance = self.clinical_significance

        risk_level = self.risk_level

        reliability = self.reliability

        age_adjustment = self.age_adjustment

        gender = self.gender

        patient_age = self.patient_age

        patient_gender = self.patient_gender

        age_group = self.age_group

        age_note = self.age_note

        gender_note = self.gender_note

        expected_sz_range = self.expected_sz_range

        phonation_quality = self.phonation_quality

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if s_phonation_time is not UNSET:
            field_dict["S_PHONATION_TIME"] = s_phonation_time
        if z_phonation_time is not UNSET:
            field_dict["Z_PHONATION_TIME"] = z_phonation_time
        if sz_ratio is not UNSET:
            field_dict["SZ_RATIO"] = sz_ratio
        if s_efficiency is not UNSET:
            field_dict["S_EFFICIENCY"] = s_efficiency
        if z_efficiency is not UNSET:
            field_dict["Z_EFFICIENCY"] = z_efficiency
        if s_phonation_segments is not UNSET:
            field_dict["S_PHONATION_SEGMENTS"] = s_phonation_segments
        if z_phonation_segments is not UNSET:
            field_dict["Z_PHONATION_SEGMENTS"] = z_phonation_segments
        if s_longest_segment is not UNSET:
            field_dict["S_LONGEST_SEGMENT"] = s_longest_segment
        if z_longest_segment is not UNSET:
            field_dict["Z_LONGEST_SEGMENT"] = z_longest_segment
        if mean_f0_z is not UNSET:
            field_dict["MEAN_F0_Z"] = mean_f0_z
        if f0_std_z is not UNSET:
            field_dict["F0_STD_Z"] = f0_std_z
        if f0_cv_z is not UNSET:
            field_dict["F0_CV_Z"] = f0_cv_z
        if reliability_score is not UNSET:
            field_dict["RELIABILITY_SCORE"] = reliability_score
        if presbylaryngis_risk is not UNSET:
            field_dict["PRESBYLARYNGIS_RISK"] = presbylaryngis_risk
        if sz_interpretation is not UNSET:
            field_dict["SZ_INTERPRETATION"] = sz_interpretation
        if clinical_significance is not UNSET:
            field_dict["CLINICAL_SIGNIFICANCE"] = clinical_significance
        if risk_level is not UNSET:
            field_dict["RISK_LEVEL"] = risk_level
        if reliability is not UNSET:
            field_dict["RELIABILITY"] = reliability
        if age_adjustment is not UNSET:
            field_dict["AGE_ADJUSTMENT"] = age_adjustment
        if gender is not UNSET:
            field_dict["GENDER"] = gender
        if patient_age is not UNSET:
            field_dict["PATIENT_AGE"] = patient_age
        if patient_gender is not UNSET:
            field_dict["PATIENT_GENDER"] = patient_gender
        if age_group is not UNSET:
            field_dict["AGE_GROUP"] = age_group
        if age_note is not UNSET:
            field_dict["AGE_NOTE"] = age_note
        if gender_note is not UNSET:
            field_dict["GENDER_NOTE"] = gender_note
        if expected_sz_range is not UNSET:
            field_dict["EXPECTED_SZ_RANGE"] = expected_sz_range
        if phonation_quality is not UNSET:
            field_dict["PHONATION_QUALITY"] = phonation_quality

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        s_phonation_time = d.pop("S_PHONATION_TIME", UNSET)

        z_phonation_time = d.pop("Z_PHONATION_TIME", UNSET)

        sz_ratio = d.pop("SZ_RATIO", UNSET)

        s_efficiency = d.pop("S_EFFICIENCY", UNSET)

        z_efficiency = d.pop("Z_EFFICIENCY", UNSET)

        s_phonation_segments = d.pop("S_PHONATION_SEGMENTS", UNSET)

        z_phonation_segments = d.pop("Z_PHONATION_SEGMENTS", UNSET)

        s_longest_segment = d.pop("S_LONGEST_SEGMENT", UNSET)

        z_longest_segment = d.pop("Z_LONGEST_SEGMENT", UNSET)

        mean_f0_z = d.pop("MEAN_F0_Z", UNSET)

        f0_std_z = d.pop("F0_STD_Z", UNSET)

        f0_cv_z = d.pop("F0_CV_Z", UNSET)

        reliability_score = d.pop("RELIABILITY_SCORE", UNSET)

        presbylaryngis_risk = d.pop("PRESBYLARYNGIS_RISK", UNSET)

        sz_interpretation = d.pop("SZ_INTERPRETATION", UNSET)

        clinical_significance = d.pop("CLINICAL_SIGNIFICANCE", UNSET)

        risk_level = d.pop("RISK_LEVEL", UNSET)

        reliability = d.pop("RELIABILITY", UNSET)

        age_adjustment = d.pop("AGE_ADJUSTMENT", UNSET)

        gender = d.pop("GENDER", UNSET)

        patient_age = d.pop("PATIENT_AGE", UNSET)

        patient_gender = d.pop("PATIENT_GENDER", UNSET)

        age_group = d.pop("AGE_GROUP", UNSET)

        age_note = d.pop("AGE_NOTE", UNSET)

        gender_note = d.pop("GENDER_NOTE", UNSET)

        expected_sz_range = d.pop("EXPECTED_SZ_RANGE", UNSET)

        phonation_quality = d.pop("PHONATION_QUALITY", UNSET)

        get_calculate_sz_ratio_response_200 = cls(
            s_phonation_time=s_phonation_time,
            z_phonation_time=z_phonation_time,
            sz_ratio=sz_ratio,
            s_efficiency=s_efficiency,
            z_efficiency=z_efficiency,
            s_phonation_segments=s_phonation_segments,
            z_phonation_segments=z_phonation_segments,
            s_longest_segment=s_longest_segment,
            z_longest_segment=z_longest_segment,
            mean_f0_z=mean_f0_z,
            f0_std_z=f0_std_z,
            f0_cv_z=f0_cv_z,
            reliability_score=reliability_score,
            presbylaryngis_risk=presbylaryngis_risk,
            sz_interpretation=sz_interpretation,
            clinical_significance=clinical_significance,
            risk_level=risk_level,
            reliability=reliability,
            age_adjustment=age_adjustment,
            gender=gender,
            patient_age=patient_age,
            patient_gender=patient_gender,
            age_group=age_group,
            age_note=age_note,
            gender_note=gender_note,
            expected_sz_range=expected_sz_range,
            phonation_quality=phonation_quality,
        )

        get_calculate_sz_ratio_response_200.additional_properties = d
        return get_calculate_sz_ratio_response_200

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
