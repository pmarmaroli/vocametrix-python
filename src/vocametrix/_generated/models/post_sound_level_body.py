from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostSoundLevelBody")


@_attrs_define
class PostSoundLevelBody:
    """
    Attributes:
        blob_url (str): REQUIRED. URL of the audio file (typically obtained via /api/get-blob-url + upload).
        start_sec (float): REQUIRED. Start of the analysis window in seconds. CAVEAT: The server uses a falsy check
            (`!start_sec`), so the literal value 0 is rejected — pass a tiny positive value like 0.001 if you mean 'from the
            beginning'.
        stop_sec (float): REQUIRED. End of the analysis window in seconds. Must be > start_sec.
    """

    blob_url: str
    start_sec: float
    stop_sec: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        blob_url = self.blob_url

        start_sec = self.start_sec

        stop_sec = self.stop_sec

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "blobUrl": blob_url,
                "start_sec": start_sec,
                "stop_sec": stop_sec,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        blob_url = d.pop("blobUrl")

        start_sec = d.pop("start_sec")

        stop_sec = d.pop("stop_sec")

        post_sound_level_body = cls(
            blob_url=blob_url,
            start_sec=start_sec,
            stop_sec=stop_sec,
        )

        post_sound_level_body.additional_properties = d
        return post_sound_level_body

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
