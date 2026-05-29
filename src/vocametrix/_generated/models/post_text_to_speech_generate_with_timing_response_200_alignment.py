from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostTextToSpeechGenerateWithTimingResponse200Alignment")


@_attrs_define
class PostTextToSpeechGenerateWithTimingResponse200Alignment:
    """Object with arrays of equal length: `{ characters: string[], character_start_times_seconds: number[],
    character_end_times_seconds: number[] }`. Each i-th entry gives the start/end time in seconds of the i-th character
    of the synthesized audio.

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        post_text_to_speech_generate_with_timing_response_200_alignment = cls()

        post_text_to_speech_generate_with_timing_response_200_alignment.additional_properties = d
        return post_text_to_speech_generate_with_timing_response_200_alignment

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
