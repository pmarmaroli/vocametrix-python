from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_adaptive_exercise_agent_response_200_metadata import (
        PostAdaptiveExerciseAgentResponse200Metadata,
    )


T = TypeVar("T", bound="PostAdaptiveExerciseAgentResponse200")


@_attrs_define
class PostAdaptiveExerciseAgentResponse200:
    """
    Attributes:
        success (bool | Unset): Boolean.
        adapted_html (str | Unset): String — HTML version of the exercise adapted for the chosen profile.
        metadata (PostAdaptiveExerciseAgentResponse200Metadata | Unset): Object: { profile, includeTips, threadId,
            agentName, processingTimeSeconds, timestamp }.
        remaining_credits (float | Unset): Number.
        is_anonymous_session (bool | Unset): Boolean.
    """

    success: bool | Unset = UNSET
    adapted_html: str | Unset = UNSET
    metadata: PostAdaptiveExerciseAgentResponse200Metadata | Unset = UNSET
    remaining_credits: float | Unset = UNSET
    is_anonymous_session: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        adapted_html = self.adapted_html

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
        if adapted_html is not UNSET:
            field_dict["adaptedHTML"] = adapted_html
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if remaining_credits is not UNSET:
            field_dict["remaining_credits"] = remaining_credits
        if is_anonymous_session is not UNSET:
            field_dict["isAnonymousSession"] = is_anonymous_session

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_adaptive_exercise_agent_response_200_metadata import (
            PostAdaptiveExerciseAgentResponse200Metadata,
        )

        d = dict(src_dict)
        success = d.pop("success", UNSET)

        adapted_html = d.pop("adaptedHTML", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: PostAdaptiveExerciseAgentResponse200Metadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PostAdaptiveExerciseAgentResponse200Metadata.from_dict(_metadata)

        remaining_credits = d.pop("remaining_credits", UNSET)

        is_anonymous_session = d.pop("isAnonymousSession", UNSET)

        post_adaptive_exercise_agent_response_200 = cls(
            success=success,
            adapted_html=adapted_html,
            metadata=metadata,
            remaining_credits=remaining_credits,
            is_anonymous_session=is_anonymous_session,
        )

        post_adaptive_exercise_agent_response_200.additional_properties = d
        return post_adaptive_exercise_agent_response_200

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
