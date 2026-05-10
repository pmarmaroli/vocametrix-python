from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCalculateSpectralAdvancedResponse200")


@_attrs_define
class GetCalculateSpectralAdvancedResponse200:
    """
    Attributes:
        spectral_mean (float | Unset): Weighted average frequency (center of gravity) in Hz. Example: 1847.3
        spectral_sd (float | Unset): Standard deviation of spectral distribution in Hz. Example: 623.8
        spectral_skewness (str | Unset): Third moment indicating spectral asymmetry. Example: 0.85
        spectral_kurtosis (str | Unset): Fourth moment indicating spectral peakedness. Example: 2.34
        alpha_ratio (float | Unset): Energy ratio below/above 1 kHz in dB. Example: 4.2
        l1_l0 (float | Unset): First formant to fundamental energy difference in dB. Example: -8.5
        h1_h2 (float | Unset): First to second harmonic amplitude difference in dB. Example: 3.8
        h1_a1 (float | Unset): First harmonic to first formant amplitude difference in dB. Example: -5.2
        h1_a3 (float | Unset): First harmonic to third formant amplitude difference in dB. Example: -15.7
        spectral_flux (float | Unset): Rate of spectral change in Hz. Example: 234.6
        ltas_slope (float | Unset): Spectral slope 0-1 kHz vs 1-4 kHz in dB/octave. Example: -12.4
        ltas_tilt (float | Unset): Trend line slope across 1-4 kHz in dB/octave. Example: -8.9
        mean_f0 (float | Unset): Mean fundamental frequency in Hz. Example: 195.8
        f1_mean (float | Unset): Mean first formant frequency in Hz. Example: 685.4
        f2_mean (float | Unset): Mean second formant frequency in Hz. Example: 1247.8
        f3_mean (float | Unset): Mean third formant frequency in Hz. Example: 2856.1
        gender (str | Unset): Gender classification result. Example: "Female"
        voice_pattern (str | Unset): Clinical classification. Example: "Balanced voice pattern"
        breathiness_level (str | Unset): Breathiness assessment. Example: "Minimal breathiness"
        voice_stability (str | Unset): Stability classification. Example: "Good stability"
        spectral_health (str | Unset): Overall spectral assessment. Example: "Healthy spectral characteristics"
        patient_age (str | Unset): Patient age used in analysis. Example: 35
        patient_gender (str | Unset): Patient gender classification. Example: "Female"
        age_group (str | Unset): Age group classification. Example: "Young Adult"
        age_note (str | Unset): Age-related clinical note. Example: "Age within normal vocal range"
        f0_note (str | Unset): F0 validation note. Example: "F0 within expected range"
        f0_validity (str | Unset): F0 validation status. Example: "Valid"
        gender_spectral_note (str | Unset): Gender-specific spectral note. Example: "Female spectral characteristics
            confirmed"
        expected_f0_min (str | Unset): Expected minimum F0 for age/gender. Example: 165.4
        expected_f0_max (str | Unset): Expected maximum F0 for age/gender. Example: 294.3
        spectral_mean_expected (str | Unset): Expected spectral mean for demographics. Example: 1923.5
    """

    spectral_mean: float | Unset = UNSET
    spectral_sd: float | Unset = UNSET
    spectral_skewness: str | Unset = UNSET
    spectral_kurtosis: str | Unset = UNSET
    alpha_ratio: float | Unset = UNSET
    l1_l0: float | Unset = UNSET
    h1_h2: float | Unset = UNSET
    h1_a1: float | Unset = UNSET
    h1_a3: float | Unset = UNSET
    spectral_flux: float | Unset = UNSET
    ltas_slope: float | Unset = UNSET
    ltas_tilt: float | Unset = UNSET
    mean_f0: float | Unset = UNSET
    f1_mean: float | Unset = UNSET
    f2_mean: float | Unset = UNSET
    f3_mean: float | Unset = UNSET
    gender: str | Unset = UNSET
    voice_pattern: str | Unset = UNSET
    breathiness_level: str | Unset = UNSET
    voice_stability: str | Unset = UNSET
    spectral_health: str | Unset = UNSET
    patient_age: str | Unset = UNSET
    patient_gender: str | Unset = UNSET
    age_group: str | Unset = UNSET
    age_note: str | Unset = UNSET
    f0_note: str | Unset = UNSET
    f0_validity: str | Unset = UNSET
    gender_spectral_note: str | Unset = UNSET
    expected_f0_min: str | Unset = UNSET
    expected_f0_max: str | Unset = UNSET
    spectral_mean_expected: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        spectral_mean = self.spectral_mean

        spectral_sd = self.spectral_sd

        spectral_skewness = self.spectral_skewness

        spectral_kurtosis = self.spectral_kurtosis

        alpha_ratio = self.alpha_ratio

        l1_l0 = self.l1_l0

        h1_h2 = self.h1_h2

        h1_a1 = self.h1_a1

        h1_a3 = self.h1_a3

        spectral_flux = self.spectral_flux

        ltas_slope = self.ltas_slope

        ltas_tilt = self.ltas_tilt

        mean_f0 = self.mean_f0

        f1_mean = self.f1_mean

        f2_mean = self.f2_mean

        f3_mean = self.f3_mean

        gender = self.gender

        voice_pattern = self.voice_pattern

        breathiness_level = self.breathiness_level

        voice_stability = self.voice_stability

        spectral_health = self.spectral_health

        patient_age = self.patient_age

        patient_gender = self.patient_gender

        age_group = self.age_group

        age_note = self.age_note

        f0_note = self.f0_note

        f0_validity = self.f0_validity

        gender_spectral_note = self.gender_spectral_note

        expected_f0_min = self.expected_f0_min

        expected_f0_max = self.expected_f0_max

        spectral_mean_expected = self.spectral_mean_expected

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if spectral_mean is not UNSET:
            field_dict["SPECTRAL_MEAN"] = spectral_mean
        if spectral_sd is not UNSET:
            field_dict["SPECTRAL_SD"] = spectral_sd
        if spectral_skewness is not UNSET:
            field_dict["SPECTRAL_SKEWNESS"] = spectral_skewness
        if spectral_kurtosis is not UNSET:
            field_dict["SPECTRAL_KURTOSIS"] = spectral_kurtosis
        if alpha_ratio is not UNSET:
            field_dict["ALPHA_RATIO"] = alpha_ratio
        if l1_l0 is not UNSET:
            field_dict["L1_L0"] = l1_l0
        if h1_h2 is not UNSET:
            field_dict["H1_H2"] = h1_h2
        if h1_a1 is not UNSET:
            field_dict["H1_A1"] = h1_a1
        if h1_a3 is not UNSET:
            field_dict["H1_A3"] = h1_a3
        if spectral_flux is not UNSET:
            field_dict["SPECTRAL_FLUX"] = spectral_flux
        if ltas_slope is not UNSET:
            field_dict["LTAS_SLOPE"] = ltas_slope
        if ltas_tilt is not UNSET:
            field_dict["LTAS_TILT"] = ltas_tilt
        if mean_f0 is not UNSET:
            field_dict["MEAN_F0"] = mean_f0
        if f1_mean is not UNSET:
            field_dict["F1_MEAN"] = f1_mean
        if f2_mean is not UNSET:
            field_dict["F2_MEAN"] = f2_mean
        if f3_mean is not UNSET:
            field_dict["F3_MEAN"] = f3_mean
        if gender is not UNSET:
            field_dict["GENDER"] = gender
        if voice_pattern is not UNSET:
            field_dict["VOICE_PATTERN"] = voice_pattern
        if breathiness_level is not UNSET:
            field_dict["BREATHINESS_LEVEL"] = breathiness_level
        if voice_stability is not UNSET:
            field_dict["VOICE_STABILITY"] = voice_stability
        if spectral_health is not UNSET:
            field_dict["SPECTRAL_HEALTH"] = spectral_health
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
        if f0_validity is not UNSET:
            field_dict["F0_VALIDITY"] = f0_validity
        if gender_spectral_note is not UNSET:
            field_dict["GENDER_SPECTRAL_NOTE"] = gender_spectral_note
        if expected_f0_min is not UNSET:
            field_dict["EXPECTED_F0_MIN"] = expected_f0_min
        if expected_f0_max is not UNSET:
            field_dict["EXPECTED_F0_MAX"] = expected_f0_max
        if spectral_mean_expected is not UNSET:
            field_dict["SPECTRAL_MEAN_EXPECTED"] = spectral_mean_expected

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        spectral_mean = d.pop("SPECTRAL_MEAN", UNSET)

        spectral_sd = d.pop("SPECTRAL_SD", UNSET)

        spectral_skewness = d.pop("SPECTRAL_SKEWNESS", UNSET)

        spectral_kurtosis = d.pop("SPECTRAL_KURTOSIS", UNSET)

        alpha_ratio = d.pop("ALPHA_RATIO", UNSET)

        l1_l0 = d.pop("L1_L0", UNSET)

        h1_h2 = d.pop("H1_H2", UNSET)

        h1_a1 = d.pop("H1_A1", UNSET)

        h1_a3 = d.pop("H1_A3", UNSET)

        spectral_flux = d.pop("SPECTRAL_FLUX", UNSET)

        ltas_slope = d.pop("LTAS_SLOPE", UNSET)

        ltas_tilt = d.pop("LTAS_TILT", UNSET)

        mean_f0 = d.pop("MEAN_F0", UNSET)

        f1_mean = d.pop("F1_MEAN", UNSET)

        f2_mean = d.pop("F2_MEAN", UNSET)

        f3_mean = d.pop("F3_MEAN", UNSET)

        gender = d.pop("GENDER", UNSET)

        voice_pattern = d.pop("VOICE_PATTERN", UNSET)

        breathiness_level = d.pop("BREATHINESS_LEVEL", UNSET)

        voice_stability = d.pop("VOICE_STABILITY", UNSET)

        spectral_health = d.pop("SPECTRAL_HEALTH", UNSET)

        patient_age = d.pop("PATIENT_AGE", UNSET)

        patient_gender = d.pop("PATIENT_GENDER", UNSET)

        age_group = d.pop("AGE_GROUP", UNSET)

        age_note = d.pop("AGE_NOTE", UNSET)

        f0_note = d.pop("F0_NOTE", UNSET)

        f0_validity = d.pop("F0_VALIDITY", UNSET)

        gender_spectral_note = d.pop("GENDER_SPECTRAL_NOTE", UNSET)

        expected_f0_min = d.pop("EXPECTED_F0_MIN", UNSET)

        expected_f0_max = d.pop("EXPECTED_F0_MAX", UNSET)

        spectral_mean_expected = d.pop("SPECTRAL_MEAN_EXPECTED", UNSET)

        get_calculate_spectral_advanced_response_200 = cls(
            spectral_mean=spectral_mean,
            spectral_sd=spectral_sd,
            spectral_skewness=spectral_skewness,
            spectral_kurtosis=spectral_kurtosis,
            alpha_ratio=alpha_ratio,
            l1_l0=l1_l0,
            h1_h2=h1_h2,
            h1_a1=h1_a1,
            h1_a3=h1_a3,
            spectral_flux=spectral_flux,
            ltas_slope=ltas_slope,
            ltas_tilt=ltas_tilt,
            mean_f0=mean_f0,
            f1_mean=f1_mean,
            f2_mean=f2_mean,
            f3_mean=f3_mean,
            gender=gender,
            voice_pattern=voice_pattern,
            breathiness_level=breathiness_level,
            voice_stability=voice_stability,
            spectral_health=spectral_health,
            patient_age=patient_age,
            patient_gender=patient_gender,
            age_group=age_group,
            age_note=age_note,
            f0_note=f0_note,
            f0_validity=f0_validity,
            gender_spectral_note=gender_spectral_note,
            expected_f0_min=expected_f0_min,
            expected_f0_max=expected_f0_max,
            spectral_mean_expected=spectral_mean_expected,
        )

        get_calculate_spectral_advanced_response_200.additional_properties = d
        return get_calculate_spectral_advanced_response_200

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
