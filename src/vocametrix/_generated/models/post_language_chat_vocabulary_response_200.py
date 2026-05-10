from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_language_chat_vocabulary_response_200_configuration import (
        PostLanguageChatVocabularyResponse200Configuration,
    )


T = TypeVar("T", bound="PostLanguageChatVocabularyResponse200")


@_attrs_define
class PostLanguageChatVocabularyResponse200:
    """
    Attributes:
        response (str | Unset): The AI assistant's conversational reply with vocabulary enhancements
        thread_id (str | Unset): Thread ID for continuing the conversation
        remaining_credits (float | Unset): Number of API credits remaining in your account
        configuration (PostLanguageChatVocabularyResponse200Configuration | Unset): Object containing the current
            language, age level, and topic
    """

    response: str | Unset = UNSET
    thread_id: str | Unset = UNSET
    remaining_credits: float | Unset = UNSET
    configuration: PostLanguageChatVocabularyResponse200Configuration | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        response = self.response

        thread_id = self.thread_id

        remaining_credits = self.remaining_credits

        configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = self.configuration.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if response is not UNSET:
            field_dict["response"] = response
        if thread_id is not UNSET:
            field_dict["threadId"] = thread_id
        if remaining_credits is not UNSET:
            field_dict["remaining_credits"] = remaining_credits
        if configuration is not UNSET:
            field_dict["configuration"] = configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_language_chat_vocabulary_response_200_configuration import (
            PostLanguageChatVocabularyResponse200Configuration,
        )

        d = dict(src_dict)
        response = d.pop("response", UNSET)

        thread_id = d.pop("threadId", UNSET)

        remaining_credits = d.pop("remaining_credits", UNSET)

        _configuration = d.pop("configuration", UNSET)
        configuration: PostLanguageChatVocabularyResponse200Configuration | Unset
        if isinstance(_configuration, Unset):
            configuration = UNSET
        else:
            configuration = PostLanguageChatVocabularyResponse200Configuration.from_dict(
                _configuration
            )

        post_language_chat_vocabulary_response_200 = cls(
            response=response,
            thread_id=thread_id,
            remaining_credits=remaining_credits,
            configuration=configuration,
        )

        post_language_chat_vocabulary_response_200.additional_properties = d
        return post_language_chat_vocabulary_response_200

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
