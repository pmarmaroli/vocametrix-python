from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostPronunciationAssessmentBody")


@_attrs_define
class PostPronunciationAssessmentBody:
    """
    Attributes:
        blob_url (str): The secure URL received from get-blob-url endpoint
        reference_text (str): The text to compare against the audio
        locale (str): The language locale (e.g., en-US, fr-FR)
    """

    blob_url: str
    reference_text: str
    locale: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        blob_url = self.blob_url

        reference_text = self.reference_text

        locale = self.locale

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "blobURL": blob_url,
                "referenceText": reference_text,
                "locale": locale,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        blob_url = d.pop("blobURL")

        reference_text = d.pop("referenceText")

        locale = d.pop("locale")

        post_pronunciation_assessment_body = cls(
            blob_url=blob_url,
            reference_text=reference_text,
            locale=locale,
        )

        post_pronunciation_assessment_body.additional_properties = d
        return post_pronunciation_assessment_body

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
