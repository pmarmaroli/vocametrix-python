from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostOfflineSpeechToTextResponse200")


@_attrs_define
class PostOfflineSpeechToTextResponse200:
    """
    Attributes:
        success (bool | Unset): Boolean indicating the job was accepted
        transcription_id (str | Unset): Job identifier — pass this to /api/transcription-progress/:transcriptionId to
            subscribe to progress and final result
        message (str | Unset): Human-readable status message confirming the job was queued
    """

    success: bool | Unset = UNSET
    transcription_id: str | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        transcription_id = self.transcription_id

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if transcription_id is not UNSET:
            field_dict["transcriptionId"] = transcription_id
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success", UNSET)

        transcription_id = d.pop("transcriptionId", UNSET)

        message = d.pop("message", UNSET)

        post_offline_speech_to_text_response_200 = cls(
            success=success,
            transcription_id=transcription_id,
            message=message,
        )

        post_offline_speech_to_text_response_200.additional_properties = d
        return post_offline_speech_to_text_response_200

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
