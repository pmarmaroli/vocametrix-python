from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_language_chat_pronunciation_body_assessment_history_item import (
        PostLanguageChatPronunciationBodyAssessmentHistoryItem,
    )


T = TypeVar("T", bound="PostLanguageChatPronunciationBody")


@_attrs_define
class PostLanguageChatPronunciationBody:
    """
    Attributes:
        message (str): REQUIRED. The learner's message in the target language.
        language (str): REQUIRED. Target language being learned.
        age_level (str): REQUIRED. Categorical age/level label.
        topic (str): REQUIRED. Conversation topic.
        native_language (str | Unset): Optional. The learner's native language code.
        thread_id (str | Unset): Optional. Thread ID for multi-turn continuity.
        email (str | Unset): Optional. Used by anonymous-key validation flow.
        assessment_history (list[PostLanguageChatPronunciationBodyAssessmentHistoryItem] | Unset): Optional. Array or
            object of prior pronunciation-assessment results to feed into the coach for grounded feedback.
    """

    message: str
    language: str
    age_level: str
    topic: str
    native_language: str | Unset = UNSET
    thread_id: str | Unset = UNSET
    email: str | Unset = UNSET
    assessment_history: list[PostLanguageChatPronunciationBodyAssessmentHistoryItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        language = self.language

        age_level = self.age_level

        topic = self.topic

        native_language = self.native_language

        thread_id = self.thread_id

        email = self.email

        assessment_history: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.assessment_history, Unset):
            assessment_history = []
            for assessment_history_item_data in self.assessment_history:
                assessment_history_item = assessment_history_item_data.to_dict()
                assessment_history.append(assessment_history_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "language": language,
                "ageLevel": age_level,
                "topic": topic,
            }
        )
        if native_language is not UNSET:
            field_dict["nativeLanguage"] = native_language
        if thread_id is not UNSET:
            field_dict["threadId"] = thread_id
        if email is not UNSET:
            field_dict["email"] = email
        if assessment_history is not UNSET:
            field_dict["assessmentHistory"] = assessment_history

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_language_chat_pronunciation_body_assessment_history_item import (
            PostLanguageChatPronunciationBodyAssessmentHistoryItem,
        )

        d = dict(src_dict)
        message = d.pop("message")

        language = d.pop("language")

        age_level = d.pop("ageLevel")

        topic = d.pop("topic")

        native_language = d.pop("nativeLanguage", UNSET)

        thread_id = d.pop("threadId", UNSET)

        email = d.pop("email", UNSET)

        _assessment_history = d.pop("assessmentHistory", UNSET)
        assessment_history: list[PostLanguageChatPronunciationBodyAssessmentHistoryItem] | Unset = (
            UNSET
        )
        if _assessment_history is not UNSET:
            assessment_history = []
            for assessment_history_item_data in _assessment_history:
                assessment_history_item = (
                    PostLanguageChatPronunciationBodyAssessmentHistoryItem.from_dict(
                        assessment_history_item_data
                    )
                )

                assessment_history.append(assessment_history_item)

        post_language_chat_pronunciation_body = cls(
            message=message,
            language=language,
            age_level=age_level,
            topic=topic,
            native_language=native_language,
            thread_id=thread_id,
            email=email,
            assessment_history=assessment_history,
        )

        post_language_chat_pronunciation_body.additional_properties = d
        return post_language_chat_pronunciation_body

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
