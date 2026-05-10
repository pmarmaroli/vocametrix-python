from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostTherapyReviseBySessionIdBody")


@_attrs_define
class PostTherapyReviseBySessionIdBody:
    """
    Attributes:
        feedback (str): Body — required for the deprecation handler to confirm intent (returns 400 if missing).
        max_iterations (int | Unset): Body, optional. Accepted but unused.
    """

    feedback: str
    max_iterations: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        feedback = self.feedback

        max_iterations = self.max_iterations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "feedback": feedback,
            }
        )
        if max_iterations is not UNSET:
            field_dict["maxIterations"] = max_iterations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        feedback = d.pop("feedback")

        max_iterations = d.pop("maxIterations", UNSET)

        post_therapy_revise_by_session_id_body = cls(
            feedback=feedback,
            max_iterations=max_iterations,
        )

        post_therapy_revise_by_session_id_body.additional_properties = d
        return post_therapy_revise_by_session_id_body

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
