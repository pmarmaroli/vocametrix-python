from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostAdaptiveExerciseAgentBody")


@_attrs_define
class PostAdaptiveExerciseAgentBody:
    """
    Attributes:
        exercise_text (str): REQUIRED. The original exercise text.
        profile (str): REQUIRED. One of "adhd" | "dyslexia" | "dysgraphia" | "dyspraxia" | "tourette" | "autism" (case-
            insensitive). Other values return 400 with a `validProfiles` field.
        include_tips (str | Unset): Optional, default false. If true, the agent includes practitioner tips alongside the
            adapted exercise.
        email (str | Unset): Optional. Used by anonymous-key validation flow.
    """

    exercise_text: str
    profile: str
    include_tips: str | Unset = UNSET
    email: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exercise_text = self.exercise_text

        profile = self.profile

        include_tips = self.include_tips

        email = self.email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "exerciseText": exercise_text,
                "profile": profile,
            }
        )
        if include_tips is not UNSET:
            field_dict["includeTips"] = include_tips
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        exercise_text = d.pop("exerciseText")

        profile = d.pop("profile")

        include_tips = d.pop("includeTips", UNSET)

        email = d.pop("email", UNSET)

        post_adaptive_exercise_agent_body = cls(
            exercise_text=exercise_text,
            profile=profile,
            include_tips=include_tips,
            email=email,
        )

        post_adaptive_exercise_agent_body.additional_properties = d
        return post_adaptive_exercise_agent_body

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
