from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostVocabularyTutorAgentBody")


@_attrs_define
class PostVocabularyTutorAgentBody:
    """
    Attributes:
        message (str): REQUIRED. The learner's message in the target language.
        native_language (str): REQUIRED. The learner's native language code.
        target_language (str): REQUIRED. The language the learner is studying.
        age_group (str): REQUIRED. Categorical age group label.
        topic (str): REQUIRED. Conversation topic.
        thread_id (str | Unset): Optional. Thread ID for multi-turn continuity.
    """

    message: str
    native_language: str
    target_language: str
    age_group: str
    topic: str
    thread_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        native_language = self.native_language

        target_language = self.target_language

        age_group = self.age_group

        topic = self.topic

        thread_id = self.thread_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "nativeLanguage": native_language,
                "targetLanguage": target_language,
                "ageGroup": age_group,
                "topic": topic,
            }
        )
        if thread_id is not UNSET:
            field_dict["threadId"] = thread_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message")

        native_language = d.pop("nativeLanguage")

        target_language = d.pop("targetLanguage")

        age_group = d.pop("ageGroup")

        topic = d.pop("topic")

        thread_id = d.pop("threadId", UNSET)

        post_vocabulary_tutor_agent_body = cls(
            message=message,
            native_language=native_language,
            target_language=target_language,
            age_group=age_group,
            topic=topic,
            thread_id=thread_id,
        )

        post_vocabulary_tutor_agent_body.additional_properties = d
        return post_vocabulary_tutor_agent_body

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
