from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCalculateFormantStatisticsResponse200")


@_attrs_define
class GetCalculateFormantStatisticsResponse200:
    """
    Attributes:
        f1_mean (float | Unset): Mean first formant frequency in Hz. Example: 685.4
        f1_std (float | Unset): F1 standard deviation in Hz. Example: 45.2
        f1_cv (str | Unset): F1 coefficient of variation in %. Example: 6.6
        f1_median (float | Unset): F1 median frequency in Hz. Example: 682.1
        f1_iqr (float | Unset): F1 interquartile range in Hz. Example: 38.7
        f1_range (float | Unset): F1 frequency range in Hz. Example: 142.5
        f2_mean (float | Unset): Mean second formant frequency in Hz. Example: 1247.8
        f2_std (float | Unset): F2 standard deviation in Hz. Example: 78.3
        f2_cv (str | Unset): F2 coefficient of variation in %. Example: 6.3
        f2_median (float | Unset): F2 median frequency in Hz. Example: 1245.6
        f2_iqr (float | Unset): F2 interquartile range in Hz. Example: 65.1
        f2_range (float | Unset): F2 frequency range in Hz. Example: 234.8
        f3_mean (float | Unset): Mean third formant frequency in Hz. Example: 2856.1
        f3_std (float | Unset): F3 standard deviation in Hz. Example: 112.4
        f3_cv (str | Unset): F3 coefficient of variation in %. Example: 3.9
        f3_median (float | Unset): F3 median frequency in Hz. Example: 2851.7
        f3_iqr (float | Unset): F3 interquartile range in Hz. Example: 89.3
        f3_range (float | Unset): F3 frequency range in Hz. Example: 387.2
        f4_mean (float | Unset): Mean fourth formant frequency in Hz. Example: 3847.5
        f4_std (float | Unset): F4 standard deviation in Hz. Example: 145.7
        f4_cv (str | Unset): F4 coefficient of variation in %. Example: 3.8
        f4_median (float | Unset): F4 median frequency in Hz. Example: 3842.9
        f4_iqr (float | Unset): F4 interquartile range in Hz. Example: 123.8
        f4_range (float | Unset): F4 frequency range in Hz. Example: 512.6
        f2_f1_diff (float | Unset): F2-F1 frequency difference in Hz. Example: 562.4
        f3_f2_diff (float | Unset): F3-F2 frequency difference in Hz. Example: 1608.3
        f4_f3_diff (float | Unset): F4-F3 frequency difference in Hz. Example: 991.4
        vowel_space_distance (float | Unset): Distance from neutral vowel in Hz. Example: 234.6
        formant_stability_index (float | Unset): Articulatory consistency (0-100). Example: 87.3
        articulatory_precision (str | Unset): Clinical precision level. Example: "Good articulatory precision"
        precision_level (str | Unset): Severity classification. Example: "Normal precision"
        vowel_quality (str | Unset): Gender-specific assessment. Example: "Normal female vowel production"
        hypernasality_risk (str | Unset): Hypernasality screening. Example: "Low risk"
        gender (str | Unset): Gender classification. Example: "Female"
        voice_pattern (str | Unset): Clinical pattern assessment. Example: "Normal formant pattern"
        patient_age (str | Unset): Patient age in years. Example: 35
        patient_gender (str | Unset): Patient gender classification. Example: "Female"
        age_group (str | Unset): Age-based grouping. Example: "Young Adult"
        age_note (str | Unset): Age-related clinical note. Example: "Age within normal vocal range"
        gender_formant_note (str | Unset): Gender-specific formant note. Example: "Formant frequencies consistent with
            female anatomy"
        expected_f1_range (float | Unset): Expected F1 range for demographics. Example: "650-720 Hz"
        expected_f2_range (float | Unset): Expected F2 range for demographics. Example: "1200-1300 Hz"
        expected_f3_range (float | Unset): Expected F3 range for demographics. Example: "2800-2900 Hz"
    """

    f1_mean: float | Unset = UNSET
    f1_std: float | Unset = UNSET
    f1_cv: str | Unset = UNSET
    f1_median: float | Unset = UNSET
    f1_iqr: float | Unset = UNSET
    f1_range: float | Unset = UNSET
    f2_mean: float | Unset = UNSET
    f2_std: float | Unset = UNSET
    f2_cv: str | Unset = UNSET
    f2_median: float | Unset = UNSET
    f2_iqr: float | Unset = UNSET
    f2_range: float | Unset = UNSET
    f3_mean: float | Unset = UNSET
    f3_std: float | Unset = UNSET
    f3_cv: str | Unset = UNSET
    f3_median: float | Unset = UNSET
    f3_iqr: float | Unset = UNSET
    f3_range: float | Unset = UNSET
    f4_mean: float | Unset = UNSET
    f4_std: float | Unset = UNSET
    f4_cv: str | Unset = UNSET
    f4_median: float | Unset = UNSET
    f4_iqr: float | Unset = UNSET
    f4_range: float | Unset = UNSET
    f2_f1_diff: float | Unset = UNSET
    f3_f2_diff: float | Unset = UNSET
    f4_f3_diff: float | Unset = UNSET
    vowel_space_distance: float | Unset = UNSET
    formant_stability_index: float | Unset = UNSET
    articulatory_precision: str | Unset = UNSET
    precision_level: str | Unset = UNSET
    vowel_quality: str | Unset = UNSET
    hypernasality_risk: str | Unset = UNSET
    gender: str | Unset = UNSET
    voice_pattern: str | Unset = UNSET
    patient_age: str | Unset = UNSET
    patient_gender: str | Unset = UNSET
    age_group: str | Unset = UNSET
    age_note: str | Unset = UNSET
    gender_formant_note: str | Unset = UNSET
    expected_f1_range: float | Unset = UNSET
    expected_f2_range: float | Unset = UNSET
    expected_f3_range: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        f1_mean = self.f1_mean

        f1_std = self.f1_std

        f1_cv = self.f1_cv

        f1_median = self.f1_median

        f1_iqr = self.f1_iqr

        f1_range = self.f1_range

        f2_mean = self.f2_mean

        f2_std = self.f2_std

        f2_cv = self.f2_cv

        f2_median = self.f2_median

        f2_iqr = self.f2_iqr

        f2_range = self.f2_range

        f3_mean = self.f3_mean

        f3_std = self.f3_std

        f3_cv = self.f3_cv

        f3_median = self.f3_median

        f3_iqr = self.f3_iqr

        f3_range = self.f3_range

        f4_mean = self.f4_mean

        f4_std = self.f4_std

        f4_cv = self.f4_cv

        f4_median = self.f4_median

        f4_iqr = self.f4_iqr

        f4_range = self.f4_range

        f2_f1_diff = self.f2_f1_diff

        f3_f2_diff = self.f3_f2_diff

        f4_f3_diff = self.f4_f3_diff

        vowel_space_distance = self.vowel_space_distance

        formant_stability_index = self.formant_stability_index

        articulatory_precision = self.articulatory_precision

        precision_level = self.precision_level

        vowel_quality = self.vowel_quality

        hypernasality_risk = self.hypernasality_risk

        gender = self.gender

        voice_pattern = self.voice_pattern

        patient_age = self.patient_age

        patient_gender = self.patient_gender

        age_group = self.age_group

        age_note = self.age_note

        gender_formant_note = self.gender_formant_note

        expected_f1_range = self.expected_f1_range

        expected_f2_range = self.expected_f2_range

        expected_f3_range = self.expected_f3_range

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if f1_mean is not UNSET:
            field_dict["F1_MEAN"] = f1_mean
        if f1_std is not UNSET:
            field_dict["F1_STD"] = f1_std
        if f1_cv is not UNSET:
            field_dict["F1_CV"] = f1_cv
        if f1_median is not UNSET:
            field_dict["F1_MEDIAN"] = f1_median
        if f1_iqr is not UNSET:
            field_dict["F1_IQR"] = f1_iqr
        if f1_range is not UNSET:
            field_dict["F1_RANGE"] = f1_range
        if f2_mean is not UNSET:
            field_dict["F2_MEAN"] = f2_mean
        if f2_std is not UNSET:
            field_dict["F2_STD"] = f2_std
        if f2_cv is not UNSET:
            field_dict["F2_CV"] = f2_cv
        if f2_median is not UNSET:
            field_dict["F2_MEDIAN"] = f2_median
        if f2_iqr is not UNSET:
            field_dict["F2_IQR"] = f2_iqr
        if f2_range is not UNSET:
            field_dict["F2_RANGE"] = f2_range
        if f3_mean is not UNSET:
            field_dict["F3_MEAN"] = f3_mean
        if f3_std is not UNSET:
            field_dict["F3_STD"] = f3_std
        if f3_cv is not UNSET:
            field_dict["F3_CV"] = f3_cv
        if f3_median is not UNSET:
            field_dict["F3_MEDIAN"] = f3_median
        if f3_iqr is not UNSET:
            field_dict["F3_IQR"] = f3_iqr
        if f3_range is not UNSET:
            field_dict["F3_RANGE"] = f3_range
        if f4_mean is not UNSET:
            field_dict["F4_MEAN"] = f4_mean
        if f4_std is not UNSET:
            field_dict["F4_STD"] = f4_std
        if f4_cv is not UNSET:
            field_dict["F4_CV"] = f4_cv
        if f4_median is not UNSET:
            field_dict["F4_MEDIAN"] = f4_median
        if f4_iqr is not UNSET:
            field_dict["F4_IQR"] = f4_iqr
        if f4_range is not UNSET:
            field_dict["F4_RANGE"] = f4_range
        if f2_f1_diff is not UNSET:
            field_dict["F2_F1_DIFF"] = f2_f1_diff
        if f3_f2_diff is not UNSET:
            field_dict["F3_F2_DIFF"] = f3_f2_diff
        if f4_f3_diff is not UNSET:
            field_dict["F4_F3_DIFF"] = f4_f3_diff
        if vowel_space_distance is not UNSET:
            field_dict["VOWEL_SPACE_DISTANCE"] = vowel_space_distance
        if formant_stability_index is not UNSET:
            field_dict["FORMANT_STABILITY_INDEX"] = formant_stability_index
        if articulatory_precision is not UNSET:
            field_dict["ARTICULATORY_PRECISION"] = articulatory_precision
        if precision_level is not UNSET:
            field_dict["PRECISION_LEVEL"] = precision_level
        if vowel_quality is not UNSET:
            field_dict["VOWEL_QUALITY"] = vowel_quality
        if hypernasality_risk is not UNSET:
            field_dict["HYPERNASALITY_RISK"] = hypernasality_risk
        if gender is not UNSET:
            field_dict["GENDER"] = gender
        if voice_pattern is not UNSET:
            field_dict["VOICE_PATTERN"] = voice_pattern
        if patient_age is not UNSET:
            field_dict["PATIENT_AGE"] = patient_age
        if patient_gender is not UNSET:
            field_dict["PATIENT_GENDER"] = patient_gender
        if age_group is not UNSET:
            field_dict["AGE_GROUP"] = age_group
        if age_note is not UNSET:
            field_dict["AGE_NOTE"] = age_note
        if gender_formant_note is not UNSET:
            field_dict["GENDER_FORMANT_NOTE"] = gender_formant_note
        if expected_f1_range is not UNSET:
            field_dict["EXPECTED_F1_RANGE"] = expected_f1_range
        if expected_f2_range is not UNSET:
            field_dict["EXPECTED_F2_RANGE"] = expected_f2_range
        if expected_f3_range is not UNSET:
            field_dict["EXPECTED_F3_RANGE"] = expected_f3_range

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        f1_mean = d.pop("F1_MEAN", UNSET)

        f1_std = d.pop("F1_STD", UNSET)

        f1_cv = d.pop("F1_CV", UNSET)

        f1_median = d.pop("F1_MEDIAN", UNSET)

        f1_iqr = d.pop("F1_IQR", UNSET)

        f1_range = d.pop("F1_RANGE", UNSET)

        f2_mean = d.pop("F2_MEAN", UNSET)

        f2_std = d.pop("F2_STD", UNSET)

        f2_cv = d.pop("F2_CV", UNSET)

        f2_median = d.pop("F2_MEDIAN", UNSET)

        f2_iqr = d.pop("F2_IQR", UNSET)

        f2_range = d.pop("F2_RANGE", UNSET)

        f3_mean = d.pop("F3_MEAN", UNSET)

        f3_std = d.pop("F3_STD", UNSET)

        f3_cv = d.pop("F3_CV", UNSET)

        f3_median = d.pop("F3_MEDIAN", UNSET)

        f3_iqr = d.pop("F3_IQR", UNSET)

        f3_range = d.pop("F3_RANGE", UNSET)

        f4_mean = d.pop("F4_MEAN", UNSET)

        f4_std = d.pop("F4_STD", UNSET)

        f4_cv = d.pop("F4_CV", UNSET)

        f4_median = d.pop("F4_MEDIAN", UNSET)

        f4_iqr = d.pop("F4_IQR", UNSET)

        f4_range = d.pop("F4_RANGE", UNSET)

        f2_f1_diff = d.pop("F2_F1_DIFF", UNSET)

        f3_f2_diff = d.pop("F3_F2_DIFF", UNSET)

        f4_f3_diff = d.pop("F4_F3_DIFF", UNSET)

        vowel_space_distance = d.pop("VOWEL_SPACE_DISTANCE", UNSET)

        formant_stability_index = d.pop("FORMANT_STABILITY_INDEX", UNSET)

        articulatory_precision = d.pop("ARTICULATORY_PRECISION", UNSET)

        precision_level = d.pop("PRECISION_LEVEL", UNSET)

        vowel_quality = d.pop("VOWEL_QUALITY", UNSET)

        hypernasality_risk = d.pop("HYPERNASALITY_RISK", UNSET)

        gender = d.pop("GENDER", UNSET)

        voice_pattern = d.pop("VOICE_PATTERN", UNSET)

        patient_age = d.pop("PATIENT_AGE", UNSET)

        patient_gender = d.pop("PATIENT_GENDER", UNSET)

        age_group = d.pop("AGE_GROUP", UNSET)

        age_note = d.pop("AGE_NOTE", UNSET)

        gender_formant_note = d.pop("GENDER_FORMANT_NOTE", UNSET)

        expected_f1_range = d.pop("EXPECTED_F1_RANGE", UNSET)

        expected_f2_range = d.pop("EXPECTED_F2_RANGE", UNSET)

        expected_f3_range = d.pop("EXPECTED_F3_RANGE", UNSET)

        get_calculate_formant_statistics_response_200 = cls(
            f1_mean=f1_mean,
            f1_std=f1_std,
            f1_cv=f1_cv,
            f1_median=f1_median,
            f1_iqr=f1_iqr,
            f1_range=f1_range,
            f2_mean=f2_mean,
            f2_std=f2_std,
            f2_cv=f2_cv,
            f2_median=f2_median,
            f2_iqr=f2_iqr,
            f2_range=f2_range,
            f3_mean=f3_mean,
            f3_std=f3_std,
            f3_cv=f3_cv,
            f3_median=f3_median,
            f3_iqr=f3_iqr,
            f3_range=f3_range,
            f4_mean=f4_mean,
            f4_std=f4_std,
            f4_cv=f4_cv,
            f4_median=f4_median,
            f4_iqr=f4_iqr,
            f4_range=f4_range,
            f2_f1_diff=f2_f1_diff,
            f3_f2_diff=f3_f2_diff,
            f4_f3_diff=f4_f3_diff,
            vowel_space_distance=vowel_space_distance,
            formant_stability_index=formant_stability_index,
            articulatory_precision=articulatory_precision,
            precision_level=precision_level,
            vowel_quality=vowel_quality,
            hypernasality_risk=hypernasality_risk,
            gender=gender,
            voice_pattern=voice_pattern,
            patient_age=patient_age,
            patient_gender=patient_gender,
            age_group=age_group,
            age_note=age_note,
            gender_formant_note=gender_formant_note,
            expected_f1_range=expected_f1_range,
            expected_f2_range=expected_f2_range,
            expected_f3_range=expected_f3_range,
        )

        get_calculate_formant_statistics_response_200.additional_properties = d
        return get_calculate_formant_statistics_response_200

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
