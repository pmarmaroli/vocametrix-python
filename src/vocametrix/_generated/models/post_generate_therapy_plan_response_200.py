from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostGenerateTherapyPlanResponse200")


@_attrs_define
class PostGenerateTherapyPlanResponse200:
    """
    Attributes:
        success (bool | Unset): Boolean — true when the job has been queued.
        message (str | Unset): Human-readable status message.
        therapy_session_id (str | Unset): Session ID of the form "THERAPY-<patientId>-<uuid>".
        status (str | Unset): "pending" — the initial state.
        status_url (str | Unset): Convenience URL to poll status (/api/therapy-status/<id>).
        result_url (str | Unset): Convenience URL to fetch result once complete (/api/therapy-result/<id>).
        estimated_time_seconds (str | Unset): Approximate wall-clock estimate (e.g., 120 s).
        timestamp (datetime.datetime | Unset): ISO 8601 timestamp.
    """

    success: bool | Unset = UNSET
    message: str | Unset = UNSET
    therapy_session_id: str | Unset = UNSET
    status: str | Unset = UNSET
    status_url: str | Unset = UNSET
    result_url: str | Unset = UNSET
    estimated_time_seconds: str | Unset = UNSET
    timestamp: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        message = self.message

        therapy_session_id = self.therapy_session_id

        status = self.status

        status_url = self.status_url

        result_url = self.result_url

        estimated_time_seconds = self.estimated_time_seconds

        timestamp: str | Unset = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if message is not UNSET:
            field_dict["message"] = message
        if therapy_session_id is not UNSET:
            field_dict["therapy_session_id"] = therapy_session_id
        if status is not UNSET:
            field_dict["status"] = status
        if status_url is not UNSET:
            field_dict["status_url"] = status_url
        if result_url is not UNSET:
            field_dict["result_url"] = result_url
        if estimated_time_seconds is not UNSET:
            field_dict["estimated_time_seconds"] = estimated_time_seconds
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success", UNSET)

        message = d.pop("message", UNSET)

        therapy_session_id = d.pop("therapy_session_id", UNSET)

        status = d.pop("status", UNSET)

        status_url = d.pop("status_url", UNSET)

        result_url = d.pop("result_url", UNSET)

        estimated_time_seconds = d.pop("estimated_time_seconds", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: datetime.datetime | Unset
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        post_generate_therapy_plan_response_200 = cls(
            success=success,
            message=message,
            therapy_session_id=therapy_session_id,
            status=status,
            status_url=status_url,
            result_url=result_url,
            estimated_time_seconds=estimated_time_seconds,
            timestamp=timestamp,
        )

        post_generate_therapy_plan_response_200.additional_properties = d
        return post_generate_therapy_plan_response_200

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
