from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostTherapyApproveBySessionIdBody")


@_attrs_define
class PostTherapyApproveBySessionIdBody:
    """
    Attributes:
        action (str): REQUIRED in body. "approve" | "modify" | "reject" (case-insensitive).
        feedback (str | Unset): REQUIRED when action="modify". Free-form clinician notes describing what to change.
            Optional otherwise.
    """

    action: str
    feedback: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        feedback = self.feedback

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
            }
        )
        if feedback is not UNSET:
            field_dict["feedback"] = feedback

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = d.pop("action")

        feedback = d.pop("feedback", UNSET)

        post_therapy_approve_by_session_id_body = cls(
            action=action,
            feedback=feedback,
        )

        post_therapy_approve_by_session_id_body.additional_properties = d
        return post_therapy_approve_by_session_id_body

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
