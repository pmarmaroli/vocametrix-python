from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCalculateAmbitusResponse200")


@_attrs_define
class GetCalculateAmbitusResponse200:
    """
    Attributes:
        ambitus_semitones (str | Unset): Voice range in semitones (12 × log₂(F0_max/F0_min))
        ambitus_octaves (str | Unset): Voice range in octaves (semitones ÷ 12)
        frequency_ratio (float | Unset): Ratio of highest to lowest frequency (F0_max/F0_min)
        range_classification (str | Unset): Age-appropriate range assessment (Excellent/Normal/Reduced/Severely reduced)
        f0_min (float | Unset): Minimum fundamental frequency in Hz
        f0_max (float | Unset): Maximum fundamental frequency in Hz
        f0_mean (float | Unset): Mean fundamental frequency in Hz
        f0_median (float | Unset): Median fundamental frequency in Hz
        patient_age (str | Unset): Patient age used in analysis
        patient_gender (str | Unset): Patient gender (Male/Female)
        age_group (str | Unset): Age category (Child/Adolescent/Adult)
        pitch_floor (float | Unset): Lower limit for pitch tracking in Hz
        pitch_ceiling (float | Unset): Upper limit for pitch tracking in Hz
        analysis_method (str | Unset): Analysis technique used (Voice Range Profile)
    """

    ambitus_semitones: str | Unset = UNSET
    ambitus_octaves: str | Unset = UNSET
    frequency_ratio: float | Unset = UNSET
    range_classification: str | Unset = UNSET
    f0_min: float | Unset = UNSET
    f0_max: float | Unset = UNSET
    f0_mean: float | Unset = UNSET
    f0_median: float | Unset = UNSET
    patient_age: str | Unset = UNSET
    patient_gender: str | Unset = UNSET
    age_group: str | Unset = UNSET
    pitch_floor: float | Unset = UNSET
    pitch_ceiling: float | Unset = UNSET
    analysis_method: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ambitus_semitones = self.ambitus_semitones

        ambitus_octaves = self.ambitus_octaves

        frequency_ratio = self.frequency_ratio

        range_classification = self.range_classification

        f0_min = self.f0_min

        f0_max = self.f0_max

        f0_mean = self.f0_mean

        f0_median = self.f0_median

        patient_age = self.patient_age

        patient_gender = self.patient_gender

        age_group = self.age_group

        pitch_floor = self.pitch_floor

        pitch_ceiling = self.pitch_ceiling

        analysis_method = self.analysis_method

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ambitus_semitones is not UNSET:
            field_dict["AMBITUS_SEMITONES"] = ambitus_semitones
        if ambitus_octaves is not UNSET:
            field_dict["AMBITUS_OCTAVES"] = ambitus_octaves
        if frequency_ratio is not UNSET:
            field_dict["FREQUENCY_RATIO"] = frequency_ratio
        if range_classification is not UNSET:
            field_dict["RANGE_CLASSIFICATION"] = range_classification
        if f0_min is not UNSET:
            field_dict["F0_MIN"] = f0_min
        if f0_max is not UNSET:
            field_dict["F0_MAX"] = f0_max
        if f0_mean is not UNSET:
            field_dict["F0_MEAN"] = f0_mean
        if f0_median is not UNSET:
            field_dict["F0_MEDIAN"] = f0_median
        if patient_age is not UNSET:
            field_dict["PATIENT_AGE"] = patient_age
        if patient_gender is not UNSET:
            field_dict["PATIENT_GENDER"] = patient_gender
        if age_group is not UNSET:
            field_dict["AGE_GROUP"] = age_group
        if pitch_floor is not UNSET:
            field_dict["PITCH_FLOOR"] = pitch_floor
        if pitch_ceiling is not UNSET:
            field_dict["PITCH_CEILING"] = pitch_ceiling
        if analysis_method is not UNSET:
            field_dict["ANALYSIS_METHOD"] = analysis_method

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ambitus_semitones = d.pop("AMBITUS_SEMITONES", UNSET)

        ambitus_octaves = d.pop("AMBITUS_OCTAVES", UNSET)

        frequency_ratio = d.pop("FREQUENCY_RATIO", UNSET)

        range_classification = d.pop("RANGE_CLASSIFICATION", UNSET)

        f0_min = d.pop("F0_MIN", UNSET)

        f0_max = d.pop("F0_MAX", UNSET)

        f0_mean = d.pop("F0_MEAN", UNSET)

        f0_median = d.pop("F0_MEDIAN", UNSET)

        patient_age = d.pop("PATIENT_AGE", UNSET)

        patient_gender = d.pop("PATIENT_GENDER", UNSET)

        age_group = d.pop("AGE_GROUP", UNSET)

        pitch_floor = d.pop("PITCH_FLOOR", UNSET)

        pitch_ceiling = d.pop("PITCH_CEILING", UNSET)

        analysis_method = d.pop("ANALYSIS_METHOD", UNSET)

        get_calculate_ambitus_response_200 = cls(
            ambitus_semitones=ambitus_semitones,
            ambitus_octaves=ambitus_octaves,
            frequency_ratio=frequency_ratio,
            range_classification=range_classification,
            f0_min=f0_min,
            f0_max=f0_max,
            f0_mean=f0_mean,
            f0_median=f0_median,
            patient_age=patient_age,
            patient_gender=patient_gender,
            age_group=age_group,
            pitch_floor=pitch_floor,
            pitch_ceiling=pitch_ceiling,
            analysis_method=analysis_method,
        )

        get_calculate_ambitus_response_200.additional_properties = d
        return get_calculate_ambitus_response_200

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
