from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostLanguageChatVocabularyBody")


@_attrs_define
class PostLanguageChatVocabularyBody:
    """
    Attributes:
        message (str): REQUIRED. The user's message in their target language
        language (str): REQUIRED. Target language the user is learning (en-US, fr-FR, es-ES, de-DE, etc.)
        native_language (str): REQUIRED. The user's native language code — used to localize vocabulary hints and
            corrections
        age_level (str): Age/level (child-beginner, teen-intermediate, adult-advanced, etc.)
        topic (str): Conversation topic (family, travel, food, work, hobbies, etc.)
        thread_id (str | Unset): Optional thread ID to continue previous conversation
        email (str | Unset): Optional user email for tracking
    """

    message: str
    language: str
    native_language: str
    age_level: str
    topic: str
    thread_id: str | Unset = UNSET
    email: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        language = self.language

        native_language = self.native_language

        age_level = self.age_level

        topic = self.topic

        thread_id = self.thread_id

        email = self.email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "language": language,
                "nativeLanguage": native_language,
                "ageLevel": age_level,
                "topic": topic,
            }
        )
        if thread_id is not UNSET:
            field_dict["threadId"] = thread_id
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message")

        language = d.pop("language")

        native_language = d.pop("nativeLanguage")

        age_level = d.pop("ageLevel")

        topic = d.pop("topic")

        thread_id = d.pop("threadId", UNSET)

        email = d.pop("email", UNSET)

        post_language_chat_vocabulary_body = cls(
            message=message,
            language=language,
            native_language=native_language,
            age_level=age_level,
            topic=topic,
            thread_id=thread_id,
            email=email,
        )

        post_language_chat_vocabulary_body.additional_properties = d
        return post_language_chat_vocabulary_body

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
