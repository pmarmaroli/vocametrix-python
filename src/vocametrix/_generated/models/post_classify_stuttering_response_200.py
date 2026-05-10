from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostClassifyStutteringResponse200")


@_attrs_define
class PostClassifyStutteringResponse200:
    """
    Attributes:
        success (bool | Unset): Boolean — true when the job has been queued.
        session_id (str | Unset): String of the form "cls-<uuid>". Pass to /api/therapy-status/:sessionId and
            /api/therapy-result/:sessionId to poll and retrieve.
        message (str | Unset): Human-readable confirmation, e.g. "Classification started. Use session_id to poll for
            progress."
    """

    success: bool | Unset = UNSET
    session_id: str | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        session_id = self.session_id

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if session_id is not UNSET:
            field_dict["session_id"] = session_id
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success", UNSET)

        session_id = d.pop("session_id", UNSET)

        message = d.pop("message", UNSET)

        post_classify_stuttering_response_200 = cls(
            success=success,
            session_id=session_id,
            message=message,
        )

        post_classify_stuttering_response_200.additional_properties = d
        return post_classify_stuttering_response_200

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
