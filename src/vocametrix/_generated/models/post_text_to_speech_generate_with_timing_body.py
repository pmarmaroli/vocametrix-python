from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostTextToSpeechGenerateWithTimingBody")


@_attrs_define
class PostTextToSpeechGenerateWithTimingBody:
    """
    Attributes:
        text (str): Text to synthesize (1–2500 characters). REQUIRED.
        is_ssml (bool | Unset): Boolean (optional, default false). Currently accepted but not applied to the request
            body — flag is reserved for future SSML support.
    """

    text: str
    is_ssml: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        is_ssml = self.is_ssml

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
            }
        )
        if is_ssml is not UNSET:
            field_dict["isSSML"] = is_ssml

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text = d.pop("text")

        is_ssml = d.pop("isSSML", UNSET)

        post_text_to_speech_generate_with_timing_body = cls(
            text=text,
            is_ssml=is_ssml,
        )

        post_text_to_speech_generate_with_timing_body.additional_properties = d
        return post_text_to_speech_generate_with_timing_body

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
