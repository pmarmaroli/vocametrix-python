from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostTherapyApproveBySessionIdResponse200")


@_attrs_define
class PostTherapyApproveBySessionIdResponse200:
    """
    Attributes:
        success (bool | Unset): Boolean.
        therapy_session_id (str | Unset): Echo of the session ID.
        action (str | Unset): Echo of the action.
        feedback (str | Unset): Echo of the feedback (or null).
        delivery_status (str | Unset): On approve: "approved_pending_delivery". On reject: "rejected".
        status (str | Unset): On modify: "processing" — the workflow re-runs and the client must poll again.
        status_message (str | Unset): Human-readable description.
        status_url (str | Unset): (modify only) URL to poll the new run.
        result_url (str | Unset): (modify only) URL to fetch the new result.
        timestamp (datetime.datetime | Unset): ISO 8601.
        message (str | Unset): Human-readable confirmation.
    """

    success: bool | Unset = UNSET
    therapy_session_id: str | Unset = UNSET
    action: str | Unset = UNSET
    feedback: str | Unset = UNSET
    delivery_status: str | Unset = UNSET
    status: str | Unset = UNSET
    status_message: str | Unset = UNSET
    status_url: str | Unset = UNSET
    result_url: str | Unset = UNSET
    timestamp: datetime.datetime | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        therapy_session_id = self.therapy_session_id

        action = self.action

        feedback = self.feedback

        delivery_status = self.delivery_status

        status = self.status

        status_message = self.status_message

        status_url = self.status_url

        result_url = self.result_url

        timestamp: str | Unset = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if therapy_session_id is not UNSET:
            field_dict["therapy_session_id"] = therapy_session_id
        if action is not UNSET:
            field_dict["action"] = action
        if feedback is not UNSET:
            field_dict["feedback"] = feedback
        if delivery_status is not UNSET:
            field_dict["delivery_status"] = delivery_status
        if status is not UNSET:
            field_dict["status"] = status
        if status_message is not UNSET:
            field_dict["status_message"] = status_message
        if status_url is not UNSET:
            field_dict["status_url"] = status_url
        if result_url is not UNSET:
            field_dict["result_url"] = result_url
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success", UNSET)

        therapy_session_id = d.pop("therapy_session_id", UNSET)

        action = d.pop("action", UNSET)

        feedback = d.pop("feedback", UNSET)

        delivery_status = d.pop("delivery_status", UNSET)

        status = d.pop("status", UNSET)

        status_message = d.pop("status_message", UNSET)

        status_url = d.pop("status_url", UNSET)

        result_url = d.pop("result_url", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: datetime.datetime | Unset
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        message = d.pop("message", UNSET)

        post_therapy_approve_by_session_id_response_200 = cls(
            success=success,
            therapy_session_id=therapy_session_id,
            action=action,
            feedback=feedback,
            delivery_status=delivery_status,
            status=status,
            status_message=status_message,
            status_url=status_url,
            result_url=result_url,
            timestamp=timestamp,
            message=message,
        )

        post_therapy_approve_by_session_id_response_200.additional_properties = d
        return post_therapy_approve_by_session_id_response_200

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
