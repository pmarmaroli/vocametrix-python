from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostTextToSpeechResponse200")


@_attrs_define
class PostTextToSpeechResponse200:
    """
    Attributes:
        success (bool | Unset): Boolean indicating if synthesis was successful
        audio (str | Unset): Base64 encoded audio data
        format_ (str | Unset): Audio format (wav)
        voice (str | Unset): Voice used for synthesis
        style (str | Unset): Speaking style applied
        text_length (str | Unset): Length of input text processed
    """

    success: bool | Unset = UNSET
    audio: str | Unset = UNSET
    format_: str | Unset = UNSET
    voice: str | Unset = UNSET
    style: str | Unset = UNSET
    text_length: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        audio = self.audio

        format_ = self.format_

        voice = self.voice

        style = self.style

        text_length = self.text_length

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if audio is not UNSET:
            field_dict["audio"] = audio
        if format_ is not UNSET:
            field_dict["format"] = format_
        if voice is not UNSET:
            field_dict["voice"] = voice
        if style is not UNSET:
            field_dict["style"] = style
        if text_length is not UNSET:
            field_dict["textLength"] = text_length

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success", UNSET)

        audio = d.pop("audio", UNSET)

        format_ = d.pop("format", UNSET)

        voice = d.pop("voice", UNSET)

        style = d.pop("style", UNSET)

        text_length = d.pop("textLength", UNSET)

        post_text_to_speech_response_200 = cls(
            success=success,
            audio=audio,
            format_=format_,
            voice=voice,
            style=style,
            text_length=text_length,
        )

        post_text_to_speech_response_200.additional_properties = d
        return post_text_to_speech_response_200

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
