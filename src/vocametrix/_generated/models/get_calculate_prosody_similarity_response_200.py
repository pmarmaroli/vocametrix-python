from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_calculate_prosody_similarity_response_200curvedata_item import (
        GetCalculateProsodySimilarityResponse200CURVEDATAItem,
    )
    from ..models.get_calculate_prosody_similarity_response_200visualizationmetadata import (
        GetCalculateProsodySimilarityResponse200VISUALIZATIONMETADATA,
    )


T = TypeVar("T", bound="GetCalculateProsodySimilarityResponse200")


@_attrs_define
class GetCalculateProsodySimilarityResponse200:
    """
    Attributes:
        overall_score (float | Unset): Composite similarity score on a 0–100 scale.
        pitch_score (float | Unset): Pitch-similarity sub-score (0–100).
        rhythm_score (float | Unset): Rhythm-similarity sub-score (0–100).
        intensity_score (float | Unset): Intensity-similarity sub-score (0–100).
        performance_level (str | Unset): Categorical label (e.g. "Excellent", "Good", "Needs work").
        overall_feedback (str | Unset): Free-form coaching text (English).
        best_match (str | Unset): Free-form description of the best-matching dimension.
        needs_work (str | Unset): Free-form description of the dimension that needs the most work.
        speech_rate_similarity (float | Unset): Speech-rate similarity (0–1 or 0–100 depending on metric).
        duration_similarity (str | Unset): Total-duration similarity.
        pitch_contour_similarity (str | Unset): Pitch-contour shape similarity.
        intensity_contour_similarity (str | Unset): Intensity-contour shape similarity.
        dynamic_range_similarity (str | Unset): Dynamic-range similarity.
        model_f0_mean (str | Unset): Mean F0 of the model recording (Hz).
        user_f0_mean (str | Unset): Mean F0 of the learner recording (Hz).
        model_speech_rate (str | Unset): Speech rate of the model (e.g., syllables/sec).
        user_speech_rate (str | Unset): Speech rate of the learner.
        model_duration (str | Unset): Duration of the model recording (sec).
        user_duration (str | Unset): Duration of the learner recording (sec).
        curve_data (list[GetCalculateProsodySimilarityResponse200CURVEDATAItem] | Unset): Visualization-ready curves: `{
            pitch: [{time, model, user}, …], intensity: [...], rhythm: [...] }`. Each array is sampled at common time points
            and includes both signals so the UI can overlay them directly.
        visualization_metadata (GetCalculateProsodySimilarityResponse200VISUALIZATIONMETADATA | Unset): Object: `{
            model_duration, user_duration, total_samples, pitch_range: { model_median, user_median } }`.
        analysis_type (str | Unset): String — currently "Prosody_Similarity_Game".
        algorithm_version (str | Unset): String — currently "v01_with_curves".
    """

    overall_score: float | Unset = UNSET
    pitch_score: float | Unset = UNSET
    rhythm_score: float | Unset = UNSET
    intensity_score: float | Unset = UNSET
    performance_level: str | Unset = UNSET
    overall_feedback: str | Unset = UNSET
    best_match: str | Unset = UNSET
    needs_work: str | Unset = UNSET
    speech_rate_similarity: float | Unset = UNSET
    duration_similarity: str | Unset = UNSET
    pitch_contour_similarity: str | Unset = UNSET
    intensity_contour_similarity: str | Unset = UNSET
    dynamic_range_similarity: str | Unset = UNSET
    model_f0_mean: str | Unset = UNSET
    user_f0_mean: str | Unset = UNSET
    model_speech_rate: str | Unset = UNSET
    user_speech_rate: str | Unset = UNSET
    model_duration: str | Unset = UNSET
    user_duration: str | Unset = UNSET
    curve_data: list[GetCalculateProsodySimilarityResponse200CURVEDATAItem] | Unset = UNSET
    visualization_metadata: (
        GetCalculateProsodySimilarityResponse200VISUALIZATIONMETADATA | Unset
    ) = UNSET
    analysis_type: str | Unset = UNSET
    algorithm_version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        overall_score = self.overall_score

        pitch_score = self.pitch_score

        rhythm_score = self.rhythm_score

        intensity_score = self.intensity_score

        performance_level = self.performance_level

        overall_feedback = self.overall_feedback

        best_match = self.best_match

        needs_work = self.needs_work

        speech_rate_similarity = self.speech_rate_similarity

        duration_similarity = self.duration_similarity

        pitch_contour_similarity = self.pitch_contour_similarity

        intensity_contour_similarity = self.intensity_contour_similarity

        dynamic_range_similarity = self.dynamic_range_similarity

        model_f0_mean = self.model_f0_mean

        user_f0_mean = self.user_f0_mean

        model_speech_rate = self.model_speech_rate

        user_speech_rate = self.user_speech_rate

        model_duration = self.model_duration

        user_duration = self.user_duration

        curve_data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.curve_data, Unset):
            curve_data = []
            for curve_data_item_data in self.curve_data:
                curve_data_item = curve_data_item_data.to_dict()
                curve_data.append(curve_data_item)

        visualization_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.visualization_metadata, Unset):
            visualization_metadata = self.visualization_metadata.to_dict()

        analysis_type = self.analysis_type

        algorithm_version = self.algorithm_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if overall_score is not UNSET:
            field_dict["OVERALL_SCORE"] = overall_score
        if pitch_score is not UNSET:
            field_dict["PITCH_SCORE"] = pitch_score
        if rhythm_score is not UNSET:
            field_dict["RHYTHM_SCORE"] = rhythm_score
        if intensity_score is not UNSET:
            field_dict["INTENSITY_SCORE"] = intensity_score
        if performance_level is not UNSET:
            field_dict["PERFORMANCE_LEVEL"] = performance_level
        if overall_feedback is not UNSET:
            field_dict["OVERALL_FEEDBACK"] = overall_feedback
        if best_match is not UNSET:
            field_dict["BEST_MATCH"] = best_match
        if needs_work is not UNSET:
            field_dict["NEEDS_WORK"] = needs_work
        if speech_rate_similarity is not UNSET:
            field_dict["SPEECH_RATE_SIMILARITY"] = speech_rate_similarity
        if duration_similarity is not UNSET:
            field_dict["DURATION_SIMILARITY"] = duration_similarity
        if pitch_contour_similarity is not UNSET:
            field_dict["PITCH_CONTOUR_SIMILARITY"] = pitch_contour_similarity
        if intensity_contour_similarity is not UNSET:
            field_dict["INTENSITY_CONTOUR_SIMILARITY"] = intensity_contour_similarity
        if dynamic_range_similarity is not UNSET:
            field_dict["DYNAMIC_RANGE_SIMILARITY"] = dynamic_range_similarity
        if model_f0_mean is not UNSET:
            field_dict["MODEL_F0_MEAN"] = model_f0_mean
        if user_f0_mean is not UNSET:
            field_dict["USER_F0_MEAN"] = user_f0_mean
        if model_speech_rate is not UNSET:
            field_dict["MODEL_SPEECH_RATE"] = model_speech_rate
        if user_speech_rate is not UNSET:
            field_dict["USER_SPEECH_RATE"] = user_speech_rate
        if model_duration is not UNSET:
            field_dict["MODEL_DURATION"] = model_duration
        if user_duration is not UNSET:
            field_dict["USER_DURATION"] = user_duration
        if curve_data is not UNSET:
            field_dict["CURVE_DATA"] = curve_data
        if visualization_metadata is not UNSET:
            field_dict["VISUALIZATION_METADATA"] = visualization_metadata
        if analysis_type is not UNSET:
            field_dict["ANALYSIS_TYPE"] = analysis_type
        if algorithm_version is not UNSET:
            field_dict["ALGORITHM_VERSION"] = algorithm_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_calculate_prosody_similarity_response_200curvedata_item import (
            GetCalculateProsodySimilarityResponse200CURVEDATAItem,
        )
        from ..models.get_calculate_prosody_similarity_response_200visualizationmetadata import (
            GetCalculateProsodySimilarityResponse200VISUALIZATIONMETADATA,
        )

        d = dict(src_dict)
        overall_score = d.pop("OVERALL_SCORE", UNSET)

        pitch_score = d.pop("PITCH_SCORE", UNSET)

        rhythm_score = d.pop("RHYTHM_SCORE", UNSET)

        intensity_score = d.pop("INTENSITY_SCORE", UNSET)

        performance_level = d.pop("PERFORMANCE_LEVEL", UNSET)

        overall_feedback = d.pop("OVERALL_FEEDBACK", UNSET)

        best_match = d.pop("BEST_MATCH", UNSET)

        needs_work = d.pop("NEEDS_WORK", UNSET)

        speech_rate_similarity = d.pop("SPEECH_RATE_SIMILARITY", UNSET)

        duration_similarity = d.pop("DURATION_SIMILARITY", UNSET)

        pitch_contour_similarity = d.pop("PITCH_CONTOUR_SIMILARITY", UNSET)

        intensity_contour_similarity = d.pop("INTENSITY_CONTOUR_SIMILARITY", UNSET)

        dynamic_range_similarity = d.pop("DYNAMIC_RANGE_SIMILARITY", UNSET)

        model_f0_mean = d.pop("MODEL_F0_MEAN", UNSET)

        user_f0_mean = d.pop("USER_F0_MEAN", UNSET)

        model_speech_rate = d.pop("MODEL_SPEECH_RATE", UNSET)

        user_speech_rate = d.pop("USER_SPEECH_RATE", UNSET)

        model_duration = d.pop("MODEL_DURATION", UNSET)

        user_duration = d.pop("USER_DURATION", UNSET)

        _curve_data = d.pop("CURVE_DATA", UNSET)
        curve_data: list[GetCalculateProsodySimilarityResponse200CURVEDATAItem] | Unset = UNSET
        if _curve_data is not UNSET:
            curve_data = []
            for curve_data_item_data in _curve_data:
                curve_data_item = GetCalculateProsodySimilarityResponse200CURVEDATAItem.from_dict(
                    curve_data_item_data
                )

                curve_data.append(curve_data_item)

        _visualization_metadata = d.pop("VISUALIZATION_METADATA", UNSET)
        visualization_metadata: (
            GetCalculateProsodySimilarityResponse200VISUALIZATIONMETADATA | Unset
        )
        if isinstance(_visualization_metadata, Unset):
            visualization_metadata = UNSET
        else:
            visualization_metadata = (
                GetCalculateProsodySimilarityResponse200VISUALIZATIONMETADATA.from_dict(
                    _visualization_metadata
                )
            )

        analysis_type = d.pop("ANALYSIS_TYPE", UNSET)

        algorithm_version = d.pop("ALGORITHM_VERSION", UNSET)

        get_calculate_prosody_similarity_response_200 = cls(
            overall_score=overall_score,
            pitch_score=pitch_score,
            rhythm_score=rhythm_score,
            intensity_score=intensity_score,
            performance_level=performance_level,
            overall_feedback=overall_feedback,
            best_match=best_match,
            needs_work=needs_work,
            speech_rate_similarity=speech_rate_similarity,
            duration_similarity=duration_similarity,
            pitch_contour_similarity=pitch_contour_similarity,
            intensity_contour_similarity=intensity_contour_similarity,
            dynamic_range_similarity=dynamic_range_similarity,
            model_f0_mean=model_f0_mean,
            user_f0_mean=user_f0_mean,
            model_speech_rate=model_speech_rate,
            user_speech_rate=user_speech_rate,
            model_duration=model_duration,
            user_duration=user_duration,
            curve_data=curve_data,
            visualization_metadata=visualization_metadata,
            analysis_type=analysis_type,
            algorithm_version=algorithm_version,
        )

        get_calculate_prosody_similarity_response_200.additional_properties = d
        return get_calculate_prosody_similarity_response_200

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
