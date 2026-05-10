from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostSpellAgentBody")


@_attrs_define
class PostSpellAgentBody:
    """
    Attributes:
        text (str): The speech-to-text transcription of user's spoken spelling attempt
        word (str): The target word to compare against (with proper accents if applicable)
        language (str): Language code (e.g., "en-US", "fr-FR", "es-ES") for language-appropriate feedback
    """

    text: str
    word: str
    language: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        word = self.word

        language = self.language

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
                "word": word,
                "language": language,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text = d.pop("text")

        word = d.pop("word")

        language = d.pop("language")

        post_spell_agent_body = cls(
            text=text,
            word=word,
            language=language,
        )

        post_spell_agent_body.additional_properties = d
        return post_spell_agent_body

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
