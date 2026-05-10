from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types

T = TypeVar("T", bound="PostCoachingAnalysisBatchBody")


@_attrs_define
class PostCoachingAnalysisBatchBody:
    """
    Attributes:
        archive (str): REQUIRED (multipart file field, ZIP). Must contain manifest.csv at the root plus the audio files
            referenced by manifest rows. Manifest schema: filename, label, language, mode, reference_text (one row per
            audio).
    """

    archive: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        archive = self.archive

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "archive": archive,
            }
        )

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("archive", (None, str(self.archive).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        archive = d.pop("archive")

        post_coaching_analysis_batch_body = cls(
            archive=archive,
        )

        post_coaching_analysis_batch_body.additional_properties = d
        return post_coaching_analysis_batch_body

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
