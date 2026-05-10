from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_text_to_speech_generate_with_timing_response_200_alignment import (
        PostTextToSpeechGenerateWithTimingResponse200Alignment,
    )


T = TypeVar("T", bound="PostTextToSpeechGenerateWithTimingResponse200")


@_attrs_define
class PostTextToSpeechGenerateWithTimingResponse200:
    """
    Attributes:
        success (bool | Unset): Boolean — true on a successful synthesis
        audio_base64 (str | Unset): Base64-encoded MP3 audio (ElevenLabs default format)
        alignment (PostTextToSpeechGenerateWithTimingResponse200Alignment | Unset): Object with arrays of equal length:
            `{ characters: string[], character_start_times_seconds: number[], character_end_times_seconds: number[] }`. Each
            i-th entry gives the start/end time in seconds of the i-th character of the synthesized audio.
        normalized_alignment (str | Unset): Same shape as `alignment`, but computed against the post-text-normalization
            sequence (numbers expanded, abbreviations expanded, etc.) — use this when your highlighter must follow what was
            actually pronounced, not the literal input text.
    """

    success: bool | Unset = UNSET
    audio_base64: str | Unset = UNSET
    alignment: PostTextToSpeechGenerateWithTimingResponse200Alignment | Unset = UNSET
    normalized_alignment: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        audio_base64 = self.audio_base64

        alignment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.alignment, Unset):
            alignment = self.alignment.to_dict()

        normalized_alignment = self.normalized_alignment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if audio_base64 is not UNSET:
            field_dict["audio_base64"] = audio_base64
        if alignment is not UNSET:
            field_dict["alignment"] = alignment
        if normalized_alignment is not UNSET:
            field_dict["normalized_alignment"] = normalized_alignment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_text_to_speech_generate_with_timing_response_200_alignment import (
            PostTextToSpeechGenerateWithTimingResponse200Alignment,
        )

        d = dict(src_dict)
        success = d.pop("success", UNSET)

        audio_base64 = d.pop("audio_base64", UNSET)

        _alignment = d.pop("alignment", UNSET)
        alignment: PostTextToSpeechGenerateWithTimingResponse200Alignment | Unset
        if isinstance(_alignment, Unset):
            alignment = UNSET
        else:
            alignment = PostTextToSpeechGenerateWithTimingResponse200Alignment.from_dict(_alignment)

        normalized_alignment = d.pop("normalized_alignment", UNSET)

        post_text_to_speech_generate_with_timing_response_200 = cls(
            success=success,
            audio_base64=audio_base64,
            alignment=alignment,
            normalized_alignment=normalized_alignment,
        )

        post_text_to_speech_generate_with_timing_response_200.additional_properties = d
        return post_text_to_speech_generate_with_timing_response_200

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
