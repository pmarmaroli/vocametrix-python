from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostCoachingAnalysisBody")


@_attrs_define
class PostCoachingAnalysisBody:
    """
    Attributes:
        audio (str): REQUIRED (multipart file field). Any audio format ffmpeg can decode (the server normalizes to 16
            kHz mono internally).
        language (str): REQUIRED (form field). Either "fr" or "en". Other values are rejected.
        reference_text (str): Required when mode="known_text" — the text the speaker is supposed to read. Ignored in
            free_speech mode.
        mode (str | Unset): Optional (form field, default "free_speech"). "free_speech" or "known_text".
        label (str | Unset): Optional (form field). Free-form classification tag passed through into the response
            (useful for batch ergonomics).
        filename (str | Unset): Optional (form field). Overrides the multipart originalname when echoing the result.
    """

    audio: str
    language: str
    reference_text: str
    mode: str | Unset = UNSET
    label: str | Unset = UNSET
    filename: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        audio = self.audio

        language = self.language

        reference_text = self.reference_text

        mode = self.mode

        label = self.label

        filename = self.filename

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "audio": audio,
                "language": language,
                "reference_text": reference_text,
            }
        )
        if mode is not UNSET:
            field_dict["mode"] = mode
        if label is not UNSET:
            field_dict["label"] = label
        if filename is not UNSET:
            field_dict["filename"] = filename

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("audio", (None, str(self.audio).encode(), "text/plain")))

        files.append(("language", (None, str(self.language).encode(), "text/plain")))

        files.append(("reference_text", (None, str(self.reference_text).encode(), "text/plain")))

        if not isinstance(self.mode, Unset):
            files.append(("mode", (None, str(self.mode).encode(), "text/plain")))

        if not isinstance(self.label, Unset):
            files.append(("label", (None, str(self.label).encode(), "text/plain")))

        if not isinstance(self.filename, Unset):
            files.append(("filename", (None, str(self.filename).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        audio = d.pop("audio")

        language = d.pop("language")

        reference_text = d.pop("reference_text")

        mode = d.pop("mode", UNSET)

        label = d.pop("label", UNSET)

        filename = d.pop("filename", UNSET)

        post_coaching_analysis_body = cls(
            audio=audio,
            language=language,
            reference_text=reference_text,
            mode=mode,
            label=label,
            filename=filename,
        )

        post_coaching_analysis_body.additional_properties = d
        return post_coaching_analysis_body

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
