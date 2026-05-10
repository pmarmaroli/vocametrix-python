from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostSpeechTherapistAssistantBody")


@_attrs_define
class PostSpeechTherapistAssistantBody:
    """
    Attributes:
        input_ (str): The user's query or question about speech therapy
        account_type (str): User role: "slt" (therapist), "patient", or "parent" for role-based responses
        thread_id (str): Conversation thread ID for maintaining context between messages
    """

    input_: str
    account_type: str
    thread_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_ = self.input_

        account_type = self.account_type

        thread_id = self.thread_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "input": input_,
                "accountType": account_type,
                "threadId": thread_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        input_ = d.pop("input")

        account_type = d.pop("accountType")

        thread_id = d.pop("threadId")

        post_speech_therapist_assistant_body = cls(
            input_=input_,
            account_type=account_type,
            thread_id=thread_id,
        )

        post_speech_therapist_assistant_body.additional_properties = d
        return post_speech_therapist_assistant_body

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
