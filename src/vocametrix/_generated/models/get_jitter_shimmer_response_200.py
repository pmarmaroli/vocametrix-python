from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetJitterShimmerResponse200")


@_attrs_define
class GetJitterShimmerResponse200:
    """
    Attributes:
        recording_quality (str | Unset): Quality assessment: "Good" (-25 to -10 dBFS), "Suboptimal" (-30 to -25 or -10
            to -6 dBFS), "Poor" (<-30 or >-6 dBFS). Example: "Good"
        recording_quality_warning (str | Unset): Detailed warning message if quality is suboptimal or poor. Empty string
            if good. Example: "CAUTION: Recording level is low (<-25 dBFS). Consider re-recording with slightly higher
            volume for more reliable results."
        mean_intensity_dbfs (str | Unset): Mean recording intensity in dBFS (decibels relative to full scale). Target
            range: -25 to -10 dBFS. Example: -18.3
        rms_amplitude (float | Unset): Root-mean-square amplitude (0-1 scale). Used to calculate dBFS. Example: 0.122
        jitter_local_percent (str | Unset): Local jitter (period-to-period variation) in percent. Primary jitter
            measure. Normal: ≤1.04%. Example: 0.85
        jitter_ppq5_percent (str | Unset): 5-period perturbation quotient in percent. Smoothed jitter over 5 periods.
            Example: 0.78
        jitter_rap_percent (str | Unset): Relative average perturbation in percent. Average over 3 consecutive periods.
            Example: 0.82
        jitter_ddp_percent (str | Unset): Difference of differences of periods in percent. Sensitive to small
            perturbations. Example: 1.23
        shimmer_local_percent (str | Unset): Local shimmer (peak-to-peak amplitude variation) in percent. Primary
            shimmer measure. Normal: ≤3.81%. Example: 2.45
        shimmer_local_db (str | Unset): Local shimmer in decibels. Logarithmic amplitude perturbation. Example: 0.215
        shimmer_apq3_percent (str | Unset): 3-period amplitude perturbation quotient in percent. Short-term shimmer.
            Example: 2.31
        shimmer_apq5_percent (str | Unset): 5-period amplitude perturbation quotient in percent. Medium-term shimmer.
            Example: 2.38
        shimmer_apq11_percent (str | Unset): 11-period amplitude perturbation quotient in percent. Long-term shimmer
            trends. Example: 2.52
        shimmer_dda_percent (str | Unset): Difference of differences of amplitudes in percent. Sensitive to amplitude
            changes. Example: 3.47
        mean_f0 (float | Unset): Mean fundamental frequency in Hz. Averaged across voiced segments. Example: 185.7
        f0_std (float | Unset): Standard deviation of F0 in Hz. Pitch variability indicator. Example: 7.2
        f0_cv (str | Unset): Coefficient of variation of F0 in percent. (F0_STD / MEAN_F0) × 100. Pitch stability
            metric. Example: 3.88
        voiceless_percent (float | Unset): Percentage of voiceless (unvoiced) frames. Indicates phonation breaks.
            Example: 5.2
        number_of_periods (float | Unset): Number of vocal fold vibration periods analyzed. Minimum 20 required, 100+
            optimal. Example: 245
        insufficient_periods (str | Unset): Flag indicating insufficient periods: 1 if <100 periods (reduced
            reliability), 0 if ≥100 periods. Example: 0
        jitter_severity (str | Unset): Jitter classification: "Normal" (≤1.04%) or "Elevated" (>1.04%). Example:
            "Normal"
        shimmer_severity (str | Unset): Shimmer classification: "Normal" (≤3.81%) or "Elevated" (>3.81%). Example:
            "Normal"
        jitter_interpretation (str | Unset): Clinical interpretation text for jitter results. Example: "Within normal
            limits (≤1.04%)"
        shimmer_interpretation (str | Unset): Clinical interpretation text for shimmer results. Example: "Within normal
            limits (≤3.81%)"
    """

    recording_quality: str | Unset = UNSET
    recording_quality_warning: str | Unset = UNSET
    mean_intensity_dbfs: str | Unset = UNSET
    rms_amplitude: float | Unset = UNSET
    jitter_local_percent: str | Unset = UNSET
    jitter_ppq5_percent: str | Unset = UNSET
    jitter_rap_percent: str | Unset = UNSET
    jitter_ddp_percent: str | Unset = UNSET
    shimmer_local_percent: str | Unset = UNSET
    shimmer_local_db: str | Unset = UNSET
    shimmer_apq3_percent: str | Unset = UNSET
    shimmer_apq5_percent: str | Unset = UNSET
    shimmer_apq11_percent: str | Unset = UNSET
    shimmer_dda_percent: str | Unset = UNSET
    mean_f0: float | Unset = UNSET
    f0_std: float | Unset = UNSET
    f0_cv: str | Unset = UNSET
    voiceless_percent: float | Unset = UNSET
    number_of_periods: float | Unset = UNSET
    insufficient_periods: str | Unset = UNSET
    jitter_severity: str | Unset = UNSET
    shimmer_severity: str | Unset = UNSET
    jitter_interpretation: str | Unset = UNSET
    shimmer_interpretation: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        recording_quality = self.recording_quality

        recording_quality_warning = self.recording_quality_warning

        mean_intensity_dbfs = self.mean_intensity_dbfs

        rms_amplitude = self.rms_amplitude

        jitter_local_percent = self.jitter_local_percent

        jitter_ppq5_percent = self.jitter_ppq5_percent

        jitter_rap_percent = self.jitter_rap_percent

        jitter_ddp_percent = self.jitter_ddp_percent

        shimmer_local_percent = self.shimmer_local_percent

        shimmer_local_db = self.shimmer_local_db

        shimmer_apq3_percent = self.shimmer_apq3_percent

        shimmer_apq5_percent = self.shimmer_apq5_percent

        shimmer_apq11_percent = self.shimmer_apq11_percent

        shimmer_dda_percent = self.shimmer_dda_percent

        mean_f0 = self.mean_f0

        f0_std = self.f0_std

        f0_cv = self.f0_cv

        voiceless_percent = self.voiceless_percent

        number_of_periods = self.number_of_periods

        insufficient_periods = self.insufficient_periods

        jitter_severity = self.jitter_severity

        shimmer_severity = self.shimmer_severity

        jitter_interpretation = self.jitter_interpretation

        shimmer_interpretation = self.shimmer_interpretation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if recording_quality is not UNSET:
            field_dict["RECORDING_QUALITY"] = recording_quality
        if recording_quality_warning is not UNSET:
            field_dict["RECORDING_QUALITY_WARNING"] = recording_quality_warning
        if mean_intensity_dbfs is not UNSET:
            field_dict["MEAN_INTENSITY_DBFS"] = mean_intensity_dbfs
        if rms_amplitude is not UNSET:
            field_dict["RMS_AMPLITUDE"] = rms_amplitude
        if jitter_local_percent is not UNSET:
            field_dict["JITTER_LOCAL_PERCENT"] = jitter_local_percent
        if jitter_ppq5_percent is not UNSET:
            field_dict["JITTER_PPQ5_PERCENT"] = jitter_ppq5_percent
        if jitter_rap_percent is not UNSET:
            field_dict["JITTER_RAP_PERCENT"] = jitter_rap_percent
        if jitter_ddp_percent is not UNSET:
            field_dict["JITTER_DDP_PERCENT"] = jitter_ddp_percent
        if shimmer_local_percent is not UNSET:
            field_dict["SHIMMER_LOCAL_PERCENT"] = shimmer_local_percent
        if shimmer_local_db is not UNSET:
            field_dict["SHIMMER_LOCAL_DB"] = shimmer_local_db
        if shimmer_apq3_percent is not UNSET:
            field_dict["SHIMMER_APQ3_PERCENT"] = shimmer_apq3_percent
        if shimmer_apq5_percent is not UNSET:
            field_dict["SHIMMER_APQ5_PERCENT"] = shimmer_apq5_percent
        if shimmer_apq11_percent is not UNSET:
            field_dict["SHIMMER_APQ11_PERCENT"] = shimmer_apq11_percent
        if shimmer_dda_percent is not UNSET:
            field_dict["SHIMMER_DDA_PERCENT"] = shimmer_dda_percent
        if mean_f0 is not UNSET:
            field_dict["MEAN_F0"] = mean_f0
        if f0_std is not UNSET:
            field_dict["F0_STD"] = f0_std
        if f0_cv is not UNSET:
            field_dict["F0_CV"] = f0_cv
        if voiceless_percent is not UNSET:
            field_dict["VOICELESS_PERCENT"] = voiceless_percent
        if number_of_periods is not UNSET:
            field_dict["NUMBER_OF_PERIODS"] = number_of_periods
        if insufficient_periods is not UNSET:
            field_dict["INSUFFICIENT_PERIODS"] = insufficient_periods
        if jitter_severity is not UNSET:
            field_dict["JITTER_SEVERITY"] = jitter_severity
        if shimmer_severity is not UNSET:
            field_dict["SHIMMER_SEVERITY"] = shimmer_severity
        if jitter_interpretation is not UNSET:
            field_dict["JITTER_INTERPRETATION"] = jitter_interpretation
        if shimmer_interpretation is not UNSET:
            field_dict["SHIMMER_INTERPRETATION"] = shimmer_interpretation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        recording_quality = d.pop("RECORDING_QUALITY", UNSET)

        recording_quality_warning = d.pop("RECORDING_QUALITY_WARNING", UNSET)

        mean_intensity_dbfs = d.pop("MEAN_INTENSITY_DBFS", UNSET)

        rms_amplitude = d.pop("RMS_AMPLITUDE", UNSET)

        jitter_local_percent = d.pop("JITTER_LOCAL_PERCENT", UNSET)

        jitter_ppq5_percent = d.pop("JITTER_PPQ5_PERCENT", UNSET)

        jitter_rap_percent = d.pop("JITTER_RAP_PERCENT", UNSET)

        jitter_ddp_percent = d.pop("JITTER_DDP_PERCENT", UNSET)

        shimmer_local_percent = d.pop("SHIMMER_LOCAL_PERCENT", UNSET)

        shimmer_local_db = d.pop("SHIMMER_LOCAL_DB", UNSET)

        shimmer_apq3_percent = d.pop("SHIMMER_APQ3_PERCENT", UNSET)

        shimmer_apq5_percent = d.pop("SHIMMER_APQ5_PERCENT", UNSET)

        shimmer_apq11_percent = d.pop("SHIMMER_APQ11_PERCENT", UNSET)

        shimmer_dda_percent = d.pop("SHIMMER_DDA_PERCENT", UNSET)

        mean_f0 = d.pop("MEAN_F0", UNSET)

        f0_std = d.pop("F0_STD", UNSET)

        f0_cv = d.pop("F0_CV", UNSET)

        voiceless_percent = d.pop("VOICELESS_PERCENT", UNSET)

        number_of_periods = d.pop("NUMBER_OF_PERIODS", UNSET)

        insufficient_periods = d.pop("INSUFFICIENT_PERIODS", UNSET)

        jitter_severity = d.pop("JITTER_SEVERITY", UNSET)

        shimmer_severity = d.pop("SHIMMER_SEVERITY", UNSET)

        jitter_interpretation = d.pop("JITTER_INTERPRETATION", UNSET)

        shimmer_interpretation = d.pop("SHIMMER_INTERPRETATION", UNSET)

        get_jitter_shimmer_response_200 = cls(
            recording_quality=recording_quality,
            recording_quality_warning=recording_quality_warning,
            mean_intensity_dbfs=mean_intensity_dbfs,
            rms_amplitude=rms_amplitude,
            jitter_local_percent=jitter_local_percent,
            jitter_ppq5_percent=jitter_ppq5_percent,
            jitter_rap_percent=jitter_rap_percent,
            jitter_ddp_percent=jitter_ddp_percent,
            shimmer_local_percent=shimmer_local_percent,
            shimmer_local_db=shimmer_local_db,
            shimmer_apq3_percent=shimmer_apq3_percent,
            shimmer_apq5_percent=shimmer_apq5_percent,
            shimmer_apq11_percent=shimmer_apq11_percent,
            shimmer_dda_percent=shimmer_dda_percent,
            mean_f0=mean_f0,
            f0_std=f0_std,
            f0_cv=f0_cv,
            voiceless_percent=voiceless_percent,
            number_of_periods=number_of_periods,
            insufficient_periods=insufficient_periods,
            jitter_severity=jitter_severity,
            shimmer_severity=shimmer_severity,
            jitter_interpretation=jitter_interpretation,
            shimmer_interpretation=shimmer_interpretation,
        )

        get_jitter_shimmer_response_200.additional_properties = d
        return get_jitter_shimmer_response_200

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
