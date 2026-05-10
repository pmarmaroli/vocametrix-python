from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostTherapyReviseBySessionIdResponse200")


@_attrs_define
class PostTherapyReviseBySessionIdResponse200:
    """
    Attributes:
        success (bool | Unset): Always false.
        error (str | Unset): "Endpoint deprecated".
        recommended_endpoint (str | Unset): "POST /api/therapy-approve/:sessionId".
        recommended_payload (str | Unset): { action: "modify", feedback }.
    """

    success: bool | Unset = UNSET
    error: str | Unset = UNSET
    recommended_endpoint: str | Unset = UNSET
    recommended_payload: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        error = self.error

        recommended_endpoint = self.recommended_endpoint

        recommended_payload = self.recommended_payload

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if error is not UNSET:
            field_dict["error"] = error
        if recommended_endpoint is not UNSET:
            field_dict["recommended_endpoint"] = recommended_endpoint
        if recommended_payload is not UNSET:
            field_dict["recommended_payload"] = recommended_payload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success", UNSET)

        error = d.pop("error", UNSET)

        recommended_endpoint = d.pop("recommended_endpoint", UNSET)

        recommended_payload = d.pop("recommended_payload", UNSET)

        post_therapy_revise_by_session_id_response_200 = cls(
            success=success,
            error=error,
            recommended_endpoint=recommended_endpoint,
            recommended_payload=recommended_payload,
        )

        post_therapy_revise_by_session_id_response_200.additional_properties = d
        return post_therapy_revise_by_session_id_response_200

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
