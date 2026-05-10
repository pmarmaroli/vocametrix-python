from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostSpeechTherapistAssistantResponse200")


@_attrs_define
class PostSpeechTherapistAssistantResponse200:
    """
    Attributes:
        response (str | Unset): The AI assistant's detailed answer with evidence-based recommendations and resources
        thread_id (str | Unset): Conversation thread ID for continuing the conversation
        remaining_credits (float | Unset): Number of API credits remaining in your account
    """

    response: str | Unset = UNSET
    thread_id: str | Unset = UNSET
    remaining_credits: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        response = self.response

        thread_id = self.thread_id

        remaining_credits = self.remaining_credits

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if response is not UNSET:
            field_dict["response"] = response
        if thread_id is not UNSET:
            field_dict["threadId"] = thread_id
        if remaining_credits is not UNSET:
            field_dict["remaining_credits"] = remaining_credits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        response = d.pop("response", UNSET)

        thread_id = d.pop("threadId", UNSET)

        remaining_credits = d.pop("remaining_credits", UNSET)

        post_speech_therapist_assistant_response_200 = cls(
            response=response,
            thread_id=thread_id,
            remaining_credits=remaining_credits,
        )

        post_speech_therapist_assistant_response_200.additional_properties = d
        return post_speech_therapist_assistant_response_200

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
