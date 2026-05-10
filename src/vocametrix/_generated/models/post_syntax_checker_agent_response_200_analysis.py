from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostSyntaxCheckerAgentResponse200Analysis")


@_attrs_define
class PostSyntaxCheckerAgentResponse200Analysis:
    """Object: { overall_score, language_detected, text_length, analysis_timestamp, issues: [...], suggestions: [{category,
    type, description, examples}], statistics: {total_issues, by_severity: {high, medium, low}, by_type: {grammar,
    spelling, punctuation, style, clarity}}, corrected_text, readability: {grade_level, reading_ease,
    avg_sentence_length} }.

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        post_syntax_checker_agent_response_200_analysis = cls()

        post_syntax_checker_agent_response_200_analysis.additional_properties = d
        return post_syntax_checker_agent_response_200_analysis

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
