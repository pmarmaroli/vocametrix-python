from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_syntax_checker_agent_response_200_analysis import (
        PostSyntaxCheckerAgentResponse200Analysis,
    )
    from ..models.post_syntax_checker_agent_response_200_metadata import (
        PostSyntaxCheckerAgentResponse200Metadata,
    )


T = TypeVar("T", bound="PostSyntaxCheckerAgentResponse200")


@_attrs_define
class PostSyntaxCheckerAgentResponse200:
    """
    Attributes:
        success (bool | Unset): Boolean.
        analysis (PostSyntaxCheckerAgentResponse200Analysis | Unset): Object: { overall_score, language_detected,
            text_length, analysis_timestamp, issues: [...], suggestions: [{category, type, description, examples}],
            statistics: {total_issues, by_severity: {high, medium, low}, by_type: {grammar, spelling, punctuation, style,
            clarity}}, corrected_text, readability: {grade_level, reading_ease, avg_sentence_length} }.
        metadata (PostSyntaxCheckerAgentResponse200Metadata | Unset): Object: { locale, textLength, threadId, agentName,
            processingTimeSeconds, timestamp }.
        remaining_credits (float | Unset): Number.
        is_anonymous_session (bool | Unset): Boolean.
    """

    success: bool | Unset = UNSET
    analysis: PostSyntaxCheckerAgentResponse200Analysis | Unset = UNSET
    metadata: PostSyntaxCheckerAgentResponse200Metadata | Unset = UNSET
    remaining_credits: float | Unset = UNSET
    is_anonymous_session: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        analysis: dict[str, Any] | Unset = UNSET
        if not isinstance(self.analysis, Unset):
            analysis = self.analysis.to_dict()

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
        if analysis is not UNSET:
            field_dict["analysis"] = analysis
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if remaining_credits is not UNSET:
            field_dict["remaining_credits"] = remaining_credits
        if is_anonymous_session is not UNSET:
            field_dict["isAnonymousSession"] = is_anonymous_session

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_syntax_checker_agent_response_200_analysis import (
            PostSyntaxCheckerAgentResponse200Analysis,
        )
        from ..models.post_syntax_checker_agent_response_200_metadata import (
            PostSyntaxCheckerAgentResponse200Metadata,
        )

        d = dict(src_dict)
        success = d.pop("success", UNSET)

        _analysis = d.pop("analysis", UNSET)
        analysis: PostSyntaxCheckerAgentResponse200Analysis | Unset
        if isinstance(_analysis, Unset):
            analysis = UNSET
        else:
            analysis = PostSyntaxCheckerAgentResponse200Analysis.from_dict(_analysis)

        _metadata = d.pop("metadata", UNSET)
        metadata: PostSyntaxCheckerAgentResponse200Metadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PostSyntaxCheckerAgentResponse200Metadata.from_dict(_metadata)

        remaining_credits = d.pop("remaining_credits", UNSET)

        is_anonymous_session = d.pop("isAnonymousSession", UNSET)

        post_syntax_checker_agent_response_200 = cls(
            success=success,
            analysis=analysis,
            metadata=metadata,
            remaining_credits=remaining_credits,
            is_anonymous_session=is_anonymous_session,
        )

        post_syntax_checker_agent_response_200.additional_properties = d
        return post_syntax_checker_agent_response_200

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
