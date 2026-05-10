from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostSpellAgentResponse200")


@_attrs_define
class PostSpellAgentResponse200:
    """
    Attributes:
        output (str | Unset): Spelled word in uppercase with any recognized accents
        match (bool | Unset): Boolean indicating whether the spelling matches the target word
        explanation (str | Unset): Detailed explanation in the target language providing educational feedback
        remaining_credits (float | Unset): Number of remaining API credits
    """

    output: str | Unset = UNSET
    match: bool | Unset = UNSET
    explanation: str | Unset = UNSET
    remaining_credits: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        output = self.output

        match = self.match

        explanation = self.explanation

        remaining_credits = self.remaining_credits

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if output is not UNSET:
            field_dict["output"] = output
        if match is not UNSET:
            field_dict["match"] = match
        if explanation is not UNSET:
            field_dict["explanation"] = explanation
        if remaining_credits is not UNSET:
            field_dict["remaining_credits"] = remaining_credits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        output = d.pop("output", UNSET)

        match = d.pop("match", UNSET)

        explanation = d.pop("explanation", UNSET)

        remaining_credits = d.pop("remaining_credits", UNSET)

        post_spell_agent_response_200 = cls(
            output=output,
            match=match,
            explanation=explanation,
            remaining_credits=remaining_credits,
        )

        post_spell_agent_response_200.additional_properties = d
        return post_spell_agent_response_200

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
