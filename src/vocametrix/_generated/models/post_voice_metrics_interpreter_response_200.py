from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_voice_metrics_interpreter_response_200_interpretation import (
        PostVoiceMetricsInterpreterResponse200Interpretation,
    )
    from ..models.post_voice_metrics_interpreter_response_200_metadata import (
        PostVoiceMetricsInterpreterResponse200Metadata,
    )
    from ..models.post_voice_metrics_interpreter_response_200_problematic_metrics_item import (
        PostVoiceMetricsInterpreterResponse200ProblematicMetricsItem,
    )


T = TypeVar("T", bound="PostVoiceMetricsInterpreterResponse200")


@_attrs_define
class PostVoiceMetricsInterpreterResponse200:
    """
    Attributes:
        success (bool | Unset): Boolean.
        overall_score (float | Unset): Number 0–100, or -1 if the agent's response could not be parsed.
        pathology_level (str | Unset): Categorical string describing pathology severity.
        problematic_metrics (list[PostVoiceMetricsInterpreterResponse200ProblematicMetricsItem] | Unset): Array of
            metric names flagged as problematic.
        interpretation (PostVoiceMetricsInterpreterResponse200Interpretation | Unset): Object: { summary,
            overallAssessment, metrics: [...], additionalNotes: [...], recommendedActions: [{category, recommendation}],
            riskLevel, nextSteps }.
        metadata (PostVoiceMetricsInterpreterResponse200Metadata | Unset): Object: { languageCode, age, gender,
            metricsProcessed, threadId, agentName, processingTimeSeconds, timestamp, genderValidation: {detectedF0,
            expectedRange, f0Validity, note} | null }.
        remaining_credits (float | Unset): Number.
        is_anonymous_session (bool | Unset): Boolean — true if the call used an anonymous_<sessionId> key.
    """

    success: bool | Unset = UNSET
    overall_score: float | Unset = UNSET
    pathology_level: str | Unset = UNSET
    problematic_metrics: (
        list[PostVoiceMetricsInterpreterResponse200ProblematicMetricsItem] | Unset
    ) = UNSET
    interpretation: PostVoiceMetricsInterpreterResponse200Interpretation | Unset = UNSET
    metadata: PostVoiceMetricsInterpreterResponse200Metadata | Unset = UNSET
    remaining_credits: float | Unset = UNSET
    is_anonymous_session: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        overall_score = self.overall_score

        pathology_level = self.pathology_level

        problematic_metrics: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.problematic_metrics, Unset):
            problematic_metrics = []
            for problematic_metrics_item_data in self.problematic_metrics:
                problematic_metrics_item = problematic_metrics_item_data.to_dict()
                problematic_metrics.append(problematic_metrics_item)

        interpretation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.interpretation, Unset):
            interpretation = self.interpretation.to_dict()

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        remaining_credits = self.remaining_credits

        is_anonymous_session = self.is_anonymous_session

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if overall_score is not UNSET:
            field_dict["overallScore"] = overall_score
        if pathology_level is not UNSET:
            field_dict["pathologyLevel"] = pathology_level
        if problematic_metrics is not UNSET:
            field_dict["problematicMetrics"] = problematic_metrics
        if interpretation is not UNSET:
            field_dict["interpretation"] = interpretation
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if remaining_credits is not UNSET:
            field_dict["remaining_credits"] = remaining_credits
        if is_anonymous_session is not UNSET:
            field_dict["isAnonymousSession"] = is_anonymous_session

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_voice_metrics_interpreter_response_200_interpretation import (
            PostVoiceMetricsInterpreterResponse200Interpretation,
        )
        from ..models.post_voice_metrics_interpreter_response_200_metadata import (
            PostVoiceMetricsInterpreterResponse200Metadata,
        )
        from ..models.post_voice_metrics_interpreter_response_200_problematic_metrics_item import (
            PostVoiceMetricsInterpreterResponse200ProblematicMetricsItem,
        )

        d = dict(src_dict)
        success = d.pop("success", UNSET)

        overall_score = d.pop("overallScore", UNSET)

        pathology_level = d.pop("pathologyLevel", UNSET)

        _problematic_metrics = d.pop("problematicMetrics", UNSET)
        problematic_metrics: (
            list[PostVoiceMetricsInterpreterResponse200ProblematicMetricsItem] | Unset
        ) = UNSET
        if _problematic_metrics is not UNSET:
            problematic_metrics = []
            for problematic_metrics_item_data in _problematic_metrics:
                problematic_metrics_item = (
                    PostVoiceMetricsInterpreterResponse200ProblematicMetricsItem.from_dict(
                        problematic_metrics_item_data
                    )
                )

                problematic_metrics.append(problematic_metrics_item)

        _interpretation = d.pop("interpretation", UNSET)
        interpretation: PostVoiceMetricsInterpreterResponse200Interpretation | Unset
        if isinstance(_interpretation, Unset):
            interpretation = UNSET
        else:
            interpretation = PostVoiceMetricsInterpreterResponse200Interpretation.from_dict(
                _interpretation
            )

        _metadata = d.pop("metadata", UNSET)
        metadata: PostVoiceMetricsInterpreterResponse200Metadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PostVoiceMetricsInterpreterResponse200Metadata.from_dict(_metadata)

        remaining_credits = d.pop("remaining_credits", UNSET)

        is_anonymous_session = d.pop("isAnonymousSession", UNSET)

        post_voice_metrics_interpreter_response_200 = cls(
            success=success,
            overall_score=overall_score,
            pathology_level=pathology_level,
            problematic_metrics=problematic_metrics,
            interpretation=interpretation,
            metadata=metadata,
            remaining_credits=remaining_credits,
            is_anonymous_session=is_anonymous_session,
        )

        post_voice_metrics_interpreter_response_200.additional_properties = d
        return post_voice_metrics_interpreter_response_200

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
