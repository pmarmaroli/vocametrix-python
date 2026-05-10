from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostTextToSpeechBody")


@_attrs_define
class PostTextToSpeechBody:
    """
    Attributes:
        text (str): The text to convert to speech (max 1000 characters)
        voice (str | Unset): Voice name (optional, default: en-US-AriaNeural)
        style (str | Unset): Speaking style (optional, default: friendly)
        rate (str | Unset): Speaking rate (optional, default: 1.0)
        language (str | Unset): Language locale (optional, default: en-US)
    """

    text: str
    voice: str | Unset = UNSET
    style: str | Unset = UNSET
    rate: str | Unset = UNSET
    language: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        voice = self.voice

        style = self.style

        rate = self.rate

        language = self.language

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
            }
        )
        if voice is not UNSET:
            field_dict["voice"] = voice
        if style is not UNSET:
            field_dict["style"] = style
        if rate is not UNSET:
            field_dict["rate"] = rate
        if language is not UNSET:
            field_dict["language"] = language

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text = d.pop("text")

        voice = d.pop("voice", UNSET)

        style = d.pop("style", UNSET)

        rate = d.pop("rate", UNSET)

        language = d.pop("language", UNSET)

        post_text_to_speech_body = cls(
            text=text,
            voice=voice,
            style=style,
            rate=rate,
            language=language,
        )

        post_text_to_speech_body.additional_properties = d
        return post_text_to_speech_body

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
