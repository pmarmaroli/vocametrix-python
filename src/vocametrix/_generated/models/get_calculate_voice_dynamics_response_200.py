from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCalculateVoiceDynamicsResponse200")


@_attrs_define
class GetCalculateVoiceDynamicsResponse200:
    """
    Attributes:
        intensity_mean (float | Unset): Mean intensity in dB.
        intensity_std (float | Unset): Intensity standard deviation in dB.
        intensity_cv (str | Unset): Intensity coefficient of variation (%).
        intensity_min (float | Unset): Minimum intensity in dB.
        intensity_max (float | Unset): Maximum intensity in dB.
        intensity_range (float | Unset): Intensity range (max − min) in dB.
        intensity_median (float | Unset): Median intensity in dB.
        intensity_q25 (float | Unset): 25th percentile of intensity in dB.
        intensity_q75 (float | Unset): 75th percentile of intensity in dB.
        intensity_iqr (float | Unset): Inter-quartile range of intensity in dB.
        intensity_slope (str | Unset): Slope of intensity over time (dB/sec) — fatigue indicator if strongly negative.
        pitch_slope (str | Unset): Slope of pitch over time (Hz/sec).
        pitch_intensity_correlation (str | Unset): Correlation between pitch and intensity contours.
        mean_f0 (float | Unset): Mean fundamental frequency in Hz.
        f0_std (float | Unset): F0 standard deviation in Hz.
        analysis_duration (float | Unset): Analyzed duration in seconds.
        n_frames (float | Unset): Number of frames analyzed.
        time_step (str | Unset): Echo of the timeStep parameter used.
        window_length (str | Unset): Echo of the windowLength parameter used.
        fatigue_threshold (str | Unset): Echo of the fatigueThreshold parameter used.
        mild_fatigue_threshold (str | Unset): Echo of the mildFatigueThreshold parameter used.
        monotonicity_cv_threshold (str | Unset): Echo of monotonicityCV.
        monotonicity_range_threshold (str | Unset): Echo of monotonicityRange.
        projection_score (int | Unset): Integer score (0–N) — vocal projection capability.
        stability_score (int | Unset): Integer score — intensity stability.
        effort_score (int | Unset): Integer score — vocal effort level.
        control_score (int | Unset): Integer score — pitch/intensity coordination.
        monotonicity_score (int | Unset): Integer score — monotonicity (lower is better).
        reliability_flag (int | Unset): Integer flag indicating whether the analysis is reliable.
        relative_max_threshold_high (str | Unset): Computed reference threshold (high).
        relative_max_threshold_moderate (str | Unset): Computed reference threshold (moderate).
        gender_detected (str | Unset): Gender inferred from F0 statistics.
        gender_provided (str | Unset): Echo of the gender parameter as supplied.
        projection_capability (str | Unset): Categorical: e.g. "Strong", "Adequate", "Reduced".
        intensity_stability (str | Unset): Categorical clinical label for intensity stability.
        vocal_effort (str | Unset): Categorical: e.g. "Normal", "Increased", "Reduced".
        coordination (str | Unset): Categorical: how well pitch and intensity co-vary.
        fatigue_indicator (str | Unset): Categorical: "None" | "Mild" | "Severe".
        fatigue_risk (str | Unset): Categorical risk level.
        monotonicity (str | Unset): Categorical: "Monotonous" | "Normal variation" | etc.
        monotonicity_level (str | Unset): Categorical severity of monotonicity.
        monotonicity_confidence (str | Unset): Categorical confidence: "High" | "Moderate" | "Low".
        intensity_control (str | Unset): Categorical assessment of intensity control.
        clinical_interpretation (str | Unset): Free-form clinical text summary.
        clinical_recommendation (str | Unset): Free-form clinical recommendation text.
        professional_voice (str | Unset): Categorical: assessment of professional-voice readiness.
        calibration_note (float | Unset): Note about absolute dB calibration (recordings are typically uncalibrated).
        visualization_note (str | Unset): Hint for downstream visualizers.
        patient_age (str | Unset): Echo of the input age.
        age_group (str | Unset): Categorical age group (Child / Adolescent / Adult / Older Adult).
        presbylaryngis_risk (str | Unset): Categorical: presbylaryngis (age-related laryngeal change) risk.
        presbylaryngis_age_threshold (str | Unset): Threshold age above which presbylaryngis is suspected.
        expected_intensity_range (str | Unset): Expected intensity range string for this demographic.
    """

    intensity_mean: float | Unset = UNSET
    intensity_std: float | Unset = UNSET
    intensity_cv: str | Unset = UNSET
    intensity_min: float | Unset = UNSET
    intensity_max: float | Unset = UNSET
    intensity_range: float | Unset = UNSET
    intensity_median: float | Unset = UNSET
    intensity_q25: float | Unset = UNSET
    intensity_q75: float | Unset = UNSET
    intensity_iqr: float | Unset = UNSET
    intensity_slope: str | Unset = UNSET
    pitch_slope: str | Unset = UNSET
    pitch_intensity_correlation: str | Unset = UNSET
    mean_f0: float | Unset = UNSET
    f0_std: float | Unset = UNSET
    analysis_duration: float | Unset = UNSET
    n_frames: float | Unset = UNSET
    time_step: str | Unset = UNSET
    window_length: str | Unset = UNSET
    fatigue_threshold: str | Unset = UNSET
    mild_fatigue_threshold: str | Unset = UNSET
    monotonicity_cv_threshold: str | Unset = UNSET
    monotonicity_range_threshold: str | Unset = UNSET
    projection_score: int | Unset = UNSET
    stability_score: int | Unset = UNSET
    effort_score: int | Unset = UNSET
    control_score: int | Unset = UNSET
    monotonicity_score: int | Unset = UNSET
    reliability_flag: int | Unset = UNSET
    relative_max_threshold_high: str | Unset = UNSET
    relative_max_threshold_moderate: str | Unset = UNSET
    gender_detected: str | Unset = UNSET
    gender_provided: str | Unset = UNSET
    projection_capability: str | Unset = UNSET
    intensity_stability: str | Unset = UNSET
    vocal_effort: str | Unset = UNSET
    coordination: str | Unset = UNSET
    fatigue_indicator: str | Unset = UNSET
    fatigue_risk: str | Unset = UNSET
    monotonicity: str | Unset = UNSET
    monotonicity_level: str | Unset = UNSET
    monotonicity_confidence: str | Unset = UNSET
    intensity_control: str | Unset = UNSET
    clinical_interpretation: str | Unset = UNSET
    clinical_recommendation: str | Unset = UNSET
    professional_voice: str | Unset = UNSET
    calibration_note: float | Unset = UNSET
    visualization_note: str | Unset = UNSET
    patient_age: str | Unset = UNSET
    age_group: str | Unset = UNSET
    presbylaryngis_risk: str | Unset = UNSET
    presbylaryngis_age_threshold: str | Unset = UNSET
    expected_intensity_range: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        intensity_mean = self.intensity_mean

        intensity_std = self.intensity_std

        intensity_cv = self.intensity_cv

        intensity_min = self.intensity_min

        intensity_max = self.intensity_max

        intensity_range = self.intensity_range

        intensity_median = self.intensity_median

        intensity_q25 = self.intensity_q25

        intensity_q75 = self.intensity_q75

        intensity_iqr = self.intensity_iqr

        intensity_slope = self.intensity_slope

        pitch_slope = self.pitch_slope

        pitch_intensity_correlation = self.pitch_intensity_correlation

        mean_f0 = self.mean_f0

        f0_std = self.f0_std

        analysis_duration = self.analysis_duration

        n_frames = self.n_frames

        time_step = self.time_step

        window_length = self.window_length

        fatigue_threshold = self.fatigue_threshold

        mild_fatigue_threshold = self.mild_fatigue_threshold

        monotonicity_cv_threshold = self.monotonicity_cv_threshold

        monotonicity_range_threshold = self.monotonicity_range_threshold

        projection_score = self.projection_score

        stability_score = self.stability_score

        effort_score = self.effort_score

        control_score = self.control_score

        monotonicity_score = self.monotonicity_score

        reliability_flag = self.reliability_flag

        relative_max_threshold_high = self.relative_max_threshold_high

        relative_max_threshold_moderate = self.relative_max_threshold_moderate

        gender_detected = self.gender_detected

        gender_provided = self.gender_provided

        projection_capability = self.projection_capability

        intensity_stability = self.intensity_stability

        vocal_effort = self.vocal_effort

        coordination = self.coordination

        fatigue_indicator = self.fatigue_indicator

        fatigue_risk = self.fatigue_risk

        monotonicity = self.monotonicity

        monotonicity_level = self.monotonicity_level

        monotonicity_confidence = self.monotonicity_confidence

        intensity_control = self.intensity_control

        clinical_interpretation = self.clinical_interpretation

        clinical_recommendation = self.clinical_recommendation

        professional_voice = self.professional_voice

        calibration_note = self.calibration_note

        visualization_note = self.visualization_note

        patient_age = self.patient_age

        age_group = self.age_group

        presbylaryngis_risk = self.presbylaryngis_risk

        presbylaryngis_age_threshold = self.presbylaryngis_age_threshold

        expected_intensity_range = self.expected_intensity_range

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if intensity_mean is not UNSET:
            field_dict["INTENSITY_MEAN"] = intensity_mean
        if intensity_std is not UNSET:
            field_dict["INTENSITY_STD"] = intensity_std
        if intensity_cv is not UNSET:
            field_dict["INTENSITY_CV"] = intensity_cv
        if intensity_min is not UNSET:
            field_dict["INTENSITY_MIN"] = intensity_min
        if intensity_max is not UNSET:
            field_dict["INTENSITY_MAX"] = intensity_max
        if intensity_range is not UNSET:
            field_dict["INTENSITY_RANGE"] = intensity_range
        if intensity_median is not UNSET:
            field_dict["INTENSITY_MEDIAN"] = intensity_median
        if intensity_q25 is not UNSET:
            field_dict["INTENSITY_Q25"] = intensity_q25
        if intensity_q75 is not UNSET:
            field_dict["INTENSITY_Q75"] = intensity_q75
        if intensity_iqr is not UNSET:
            field_dict["INTENSITY_IQR"] = intensity_iqr
        if intensity_slope is not UNSET:
            field_dict["INTENSITY_SLOPE"] = intensity_slope
        if pitch_slope is not UNSET:
            field_dict["PITCH_SLOPE"] = pitch_slope
        if pitch_intensity_correlation is not UNSET:
            field_dict["PITCH_INTENSITY_CORRELATION"] = pitch_intensity_correlation
        if mean_f0 is not UNSET:
            field_dict["MEAN_F0"] = mean_f0
        if f0_std is not UNSET:
            field_dict["F0_STD"] = f0_std
        if analysis_duration is not UNSET:
            field_dict["ANALYSIS_DURATION"] = analysis_duration
        if n_frames is not UNSET:
            field_dict["N_FRAMES"] = n_frames
        if time_step is not UNSET:
            field_dict["TIME_STEP"] = time_step
        if window_length is not UNSET:
            field_dict["WINDOW_LENGTH"] = window_length
        if fatigue_threshold is not UNSET:
            field_dict["FATIGUE_THRESHOLD"] = fatigue_threshold
        if mild_fatigue_threshold is not UNSET:
            field_dict["MILD_FATIGUE_THRESHOLD"] = mild_fatigue_threshold
        if monotonicity_cv_threshold is not UNSET:
            field_dict["MONOTONICITY_CV_THRESHOLD"] = monotonicity_cv_threshold
        if monotonicity_range_threshold is not UNSET:
            field_dict["MONOTONICITY_RANGE_THRESHOLD"] = monotonicity_range_threshold
        if projection_score is not UNSET:
            field_dict["PROJECTION_SCORE"] = projection_score
        if stability_score is not UNSET:
            field_dict["STABILITY_SCORE"] = stability_score
        if effort_score is not UNSET:
            field_dict["EFFORT_SCORE"] = effort_score
        if control_score is not UNSET:
            field_dict["CONTROL_SCORE"] = control_score
        if monotonicity_score is not UNSET:
            field_dict["MONOTONICITY_SCORE"] = monotonicity_score
        if reliability_flag is not UNSET:
            field_dict["RELIABILITY_FLAG"] = reliability_flag
        if relative_max_threshold_high is not UNSET:
            field_dict["RELATIVE_MAX_THRESHOLD_HIGH"] = relative_max_threshold_high
        if relative_max_threshold_moderate is not UNSET:
            field_dict["RELATIVE_MAX_THRESHOLD_MODERATE"] = relative_max_threshold_moderate
        if gender_detected is not UNSET:
            field_dict["GENDER_DETECTED"] = gender_detected
        if gender_provided is not UNSET:
            field_dict["GENDER_PROVIDED"] = gender_provided
        if projection_capability is not UNSET:
            field_dict["PROJECTION_CAPABILITY"] = projection_capability
        if intensity_stability is not UNSET:
            field_dict["INTENSITY_STABILITY"] = intensity_stability
        if vocal_effort is not UNSET:
            field_dict["VOCAL_EFFORT"] = vocal_effort
        if coordination is not UNSET:
            field_dict["COORDINATION"] = coordination
        if fatigue_indicator is not UNSET:
            field_dict["FATIGUE_INDICATOR"] = fatigue_indicator
        if fatigue_risk is not UNSET:
            field_dict["FATIGUE_RISK"] = fatigue_risk
        if monotonicity is not UNSET:
            field_dict["MONOTONICITY"] = monotonicity
        if monotonicity_level is not UNSET:
            field_dict["MONOTONICITY_LEVEL"] = monotonicity_level
        if monotonicity_confidence is not UNSET:
            field_dict["MONOTONICITY_CONFIDENCE"] = monotonicity_confidence
        if intensity_control is not UNSET:
            field_dict["INTENSITY_CONTROL"] = intensity_control
        if clinical_interpretation is not UNSET:
            field_dict["CLINICAL_INTERPRETATION"] = clinical_interpretation
        if clinical_recommendation is not UNSET:
            field_dict["CLINICAL_RECOMMENDATION"] = clinical_recommendation
        if professional_voice is not UNSET:
            field_dict["PROFESSIONAL_VOICE"] = professional_voice
        if calibration_note is not UNSET:
            field_dict["CALIBRATION_NOTE"] = calibration_note
        if visualization_note is not UNSET:
            field_dict["VISUALIZATION_NOTE"] = visualization_note
        if patient_age is not UNSET:
            field_dict["PATIENT_AGE"] = patient_age
        if age_group is not UNSET:
            field_dict["AGE_GROUP"] = age_group
        if presbylaryngis_risk is not UNSET:
            field_dict["PRESBYLARYNGIS_RISK"] = presbylaryngis_risk
        if presbylaryngis_age_threshold is not UNSET:
            field_dict["PRESBYLARYNGIS_AGE_THRESHOLD"] = presbylaryngis_age_threshold
        if expected_intensity_range is not UNSET:
            field_dict["EXPECTED_INTENSITY_RANGE"] = expected_intensity_range

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        intensity_mean = d.pop("INTENSITY_MEAN", UNSET)

        intensity_std = d.pop("INTENSITY_STD", UNSET)

        intensity_cv = d.pop("INTENSITY_CV", UNSET)

        intensity_min = d.pop("INTENSITY_MIN", UNSET)

        intensity_max = d.pop("INTENSITY_MAX", UNSET)

        intensity_range = d.pop("INTENSITY_RANGE", UNSET)

        intensity_median = d.pop("INTENSITY_MEDIAN", UNSET)

        intensity_q25 = d.pop("INTENSITY_Q25", UNSET)

        intensity_q75 = d.pop("INTENSITY_Q75", UNSET)

        intensity_iqr = d.pop("INTENSITY_IQR", UNSET)

        intensity_slope = d.pop("INTENSITY_SLOPE", UNSET)

        pitch_slope = d.pop("PITCH_SLOPE", UNSET)

        pitch_intensity_correlation = d.pop("PITCH_INTENSITY_CORRELATION", UNSET)

        mean_f0 = d.pop("MEAN_F0", UNSET)

        f0_std = d.pop("F0_STD", UNSET)

        analysis_duration = d.pop("ANALYSIS_DURATION", UNSET)

        n_frames = d.pop("N_FRAMES", UNSET)

        time_step = d.pop("TIME_STEP", UNSET)

        window_length = d.pop("WINDOW_LENGTH", UNSET)

        fatigue_threshold = d.pop("FATIGUE_THRESHOLD", UNSET)

        mild_fatigue_threshold = d.pop("MILD_FATIGUE_THRESHOLD", UNSET)

        monotonicity_cv_threshold = d.pop("MONOTONICITY_CV_THRESHOLD", UNSET)

        monotonicity_range_threshold = d.pop("MONOTONICITY_RANGE_THRESHOLD", UNSET)

        projection_score = d.pop("PROJECTION_SCORE", UNSET)

        stability_score = d.pop("STABILITY_SCORE", UNSET)

        effort_score = d.pop("EFFORT_SCORE", UNSET)

        control_score = d.pop("CONTROL_SCORE", UNSET)

        monotonicity_score = d.pop("MONOTONICITY_SCORE", UNSET)

        reliability_flag = d.pop("RELIABILITY_FLAG", UNSET)

        relative_max_threshold_high = d.pop("RELATIVE_MAX_THRESHOLD_HIGH", UNSET)

        relative_max_threshold_moderate = d.pop("RELATIVE_MAX_THRESHOLD_MODERATE", UNSET)

        gender_detected = d.pop("GENDER_DETECTED", UNSET)

        gender_provided = d.pop("GENDER_PROVIDED", UNSET)

        projection_capability = d.pop("PROJECTION_CAPABILITY", UNSET)

        intensity_stability = d.pop("INTENSITY_STABILITY", UNSET)

        vocal_effort = d.pop("VOCAL_EFFORT", UNSET)

        coordination = d.pop("COORDINATION", UNSET)

        fatigue_indicator = d.pop("FATIGUE_INDICATOR", UNSET)

        fatigue_risk = d.pop("FATIGUE_RISK", UNSET)

        monotonicity = d.pop("MONOTONICITY", UNSET)

        monotonicity_level = d.pop("MONOTONICITY_LEVEL", UNSET)

        monotonicity_confidence = d.pop("MONOTONICITY_CONFIDENCE", UNSET)

        intensity_control = d.pop("INTENSITY_CONTROL", UNSET)

        clinical_interpretation = d.pop("CLINICAL_INTERPRETATION", UNSET)

        clinical_recommendation = d.pop("CLINICAL_RECOMMENDATION", UNSET)

        professional_voice = d.pop("PROFESSIONAL_VOICE", UNSET)

        calibration_note = d.pop("CALIBRATION_NOTE", UNSET)

        visualization_note = d.pop("VISUALIZATION_NOTE", UNSET)

        patient_age = d.pop("PATIENT_AGE", UNSET)

        age_group = d.pop("AGE_GROUP", UNSET)

        presbylaryngis_risk = d.pop("PRESBYLARYNGIS_RISK", UNSET)

        presbylaryngis_age_threshold = d.pop("PRESBYLARYNGIS_AGE_THRESHOLD", UNSET)

        expected_intensity_range = d.pop("EXPECTED_INTENSITY_RANGE", UNSET)

        get_calculate_voice_dynamics_response_200 = cls(
            intensity_mean=intensity_mean,
            intensity_std=intensity_std,
            intensity_cv=intensity_cv,
            intensity_min=intensity_min,
            intensity_max=intensity_max,
            intensity_range=intensity_range,
            intensity_median=intensity_median,
            intensity_q25=intensity_q25,
            intensity_q75=intensity_q75,
            intensity_iqr=intensity_iqr,
            intensity_slope=intensity_slope,
            pitch_slope=pitch_slope,
            pitch_intensity_correlation=pitch_intensity_correlation,
            mean_f0=mean_f0,
            f0_std=f0_std,
            analysis_duration=analysis_duration,
            n_frames=n_frames,
            time_step=time_step,
            window_length=window_length,
            fatigue_threshold=fatigue_threshold,
            mild_fatigue_threshold=mild_fatigue_threshold,
            monotonicity_cv_threshold=monotonicity_cv_threshold,
            monotonicity_range_threshold=monotonicity_range_threshold,
            projection_score=projection_score,
            stability_score=stability_score,
            effort_score=effort_score,
            control_score=control_score,
            monotonicity_score=monotonicity_score,
            reliability_flag=reliability_flag,
            relative_max_threshold_high=relative_max_threshold_high,
            relative_max_threshold_moderate=relative_max_threshold_moderate,
            gender_detected=gender_detected,
            gender_provided=gender_provided,
            projection_capability=projection_capability,
            intensity_stability=intensity_stability,
            vocal_effort=vocal_effort,
            coordination=coordination,
            fatigue_indicator=fatigue_indicator,
            fatigue_risk=fatigue_risk,
            monotonicity=monotonicity,
            monotonicity_level=monotonicity_level,
            monotonicity_confidence=monotonicity_confidence,
            intensity_control=intensity_control,
            clinical_interpretation=clinical_interpretation,
            clinical_recommendation=clinical_recommendation,
            professional_voice=professional_voice,
            calibration_note=calibration_note,
            visualization_note=visualization_note,
            patient_age=patient_age,
            age_group=age_group,
            presbylaryngis_risk=presbylaryngis_risk,
            presbylaryngis_age_threshold=presbylaryngis_age_threshold,
            expected_intensity_range=expected_intensity_range,
        )

        get_calculate_voice_dynamics_response_200.additional_properties = d
        return get_calculate_voice_dynamics_response_200

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
