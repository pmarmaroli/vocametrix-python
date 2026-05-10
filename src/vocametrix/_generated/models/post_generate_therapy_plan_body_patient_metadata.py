from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostGenerateTherapyPlanBodyPatientMetadata")


@_attrs_define
class PostGenerateTherapyPlanBodyPatientMetadata:
    """Optional. Object describing the patient. Max 10,000 bytes when JSON-serialized. Optional sub-fields:
    demographics.age (0–120), clinical_history.severity ("Mild"|"Moderate"|"Severe"|"Very Severe"), current_goals (max
    20 entries), recent_progress_notes (max 50), previous_exercises (max 30).

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        post_generate_therapy_plan_body_patient_metadata = cls()

        post_generate_therapy_plan_body_patient_metadata.additional_properties = d
        return post_generate_therapy_plan_body_patient_metadata

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
