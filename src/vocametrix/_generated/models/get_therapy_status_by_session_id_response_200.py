from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_therapy_status_by_session_id_response_200_generated_prompts_item import (
        GetTherapyStatusBySessionIdResponse200GeneratedPromptsItem,
    )


T = TypeVar("T", bound="GetTherapyStatusBySessionIdResponse200")


@_attrs_define
class GetTherapyStatusBySessionIdResponse200:
    """
    Attributes:
        success (bool | Unset): Boolean.
        session_id (str | Unset): String — may be normalized from the input (the server does flexible lookup).
        status (str | Unset): "pending" | "processing" | "complete" | "pending_approval" | "failed".
        progress_percent (float | Unset): Number 0–100.
        progress (float | Unset): Number — alias for progress_percent (kept for back-compat).
        status_message (str | Unset): Free-form progress description.
        error_message (str | Unset): String, or null.
        created_at (datetime.datetime | Unset): ISO 8601 timestamp.
        updated_at (datetime.datetime | Unset): ISO 8601 timestamp.
        completed_at (datetime.datetime | Unset): ISO 8601 timestamp, or null until complete.
        result_available (bool | Unset): Boolean — true when status is "complete" or "pending_approval".
        approval_required (bool | Unset): Boolean — true when status is "pending_approval".
        generated_prompts (list[GetTherapyStatusBySessionIdResponse200GeneratedPromptsItem] | Unset): Array, or null.
            Workflow-internal prompts (mostly for debugging).
        timestamp (datetime.datetime | Unset): ISO 8601 server time.
    """

    success: bool | Unset = UNSET
    session_id: str | Unset = UNSET
    status: str | Unset = UNSET
    progress_percent: float | Unset = UNSET
    progress: float | Unset = UNSET
    status_message: str | Unset = UNSET
    error_message: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    completed_at: datetime.datetime | Unset = UNSET
    result_available: bool | Unset = UNSET
    approval_required: bool | Unset = UNSET
    generated_prompts: list[GetTherapyStatusBySessionIdResponse200GeneratedPromptsItem] | Unset = (
        UNSET
    )
    timestamp: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        session_id = self.session_id

        status = self.status

        progress_percent = self.progress_percent

        progress = self.progress

        status_message = self.status_message

        error_message = self.error_message

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        completed_at: str | Unset = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat()

        result_available = self.result_available

        approval_required = self.approval_required

        generated_prompts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.generated_prompts, Unset):
            generated_prompts = []
            for generated_prompts_item_data in self.generated_prompts:
                generated_prompts_item = generated_prompts_item_data.to_dict()
                generated_prompts.append(generated_prompts_item)

        timestamp: str | Unset = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if session_id is not UNSET:
            field_dict["session_id"] = session_id
        if status is not UNSET:
            field_dict["status"] = status
        if progress_percent is not UNSET:
            field_dict["progress_percent"] = progress_percent
        if progress is not UNSET:
            field_dict["progress"] = progress
        if status_message is not UNSET:
            field_dict["status_message"] = status_message
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if result_available is not UNSET:
            field_dict["result_available"] = result_available
        if approval_required is not UNSET:
            field_dict["approval_required"] = approval_required
        if generated_prompts is not UNSET:
            field_dict["generated_prompts"] = generated_prompts
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_therapy_status_by_session_id_response_200_generated_prompts_item import (
            GetTherapyStatusBySessionIdResponse200GeneratedPromptsItem,
        )

        d = dict(src_dict)
        success = d.pop("success", UNSET)

        session_id = d.pop("session_id", UNSET)

        status = d.pop("status", UNSET)

        progress_percent = d.pop("progress_percent", UNSET)

        progress = d.pop("progress", UNSET)

        status_message = d.pop("status_message", UNSET)

        error_message = d.pop("error_message", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        _completed_at = d.pop("completed_at", UNSET)
        completed_at: datetime.datetime | Unset
        if isinstance(_completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = isoparse(_completed_at)

        result_available = d.pop("result_available", UNSET)

        approval_required = d.pop("approval_required", UNSET)

        _generated_prompts = d.pop("generated_prompts", UNSET)
        generated_prompts: (
            list[GetTherapyStatusBySessionIdResponse200GeneratedPromptsItem] | Unset
        ) = UNSET
        if _generated_prompts is not UNSET:
            generated_prompts = []
            for generated_prompts_item_data in _generated_prompts:
                generated_prompts_item = (
                    GetTherapyStatusBySessionIdResponse200GeneratedPromptsItem.from_dict(
                        generated_prompts_item_data
                    )
                )

                generated_prompts.append(generated_prompts_item)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: datetime.datetime | Unset
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        get_therapy_status_by_session_id_response_200 = cls(
            success=success,
            session_id=session_id,
            status=status,
            progress_percent=progress_percent,
            progress=progress,
            status_message=status_message,
            error_message=error_message,
            created_at=created_at,
            updated_at=updated_at,
            completed_at=completed_at,
            result_available=result_available,
            approval_required=approval_required,
            generated_prompts=generated_prompts,
            timestamp=timestamp,
        )

        get_therapy_status_by_session_id_response_200.additional_properties = d
        return get_therapy_status_by_session_id_response_200

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
