from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post_word_list_generator_body_selected_sound import (
        PostWordListGeneratorBodySelectedSound,
    )


T = TypeVar("T", bound="PostWordListGeneratorBody")


@_attrs_define
class PostWordListGeneratorBody:
    """
    Attributes:
        language (str): Target language for words (english, french, spanish, german)
        age (int): Patient age range (e.g., "3-6 years", "7-12 years", "adults")
        selected_sound (PostWordListGeneratorBodySelectedSound): Object containing symbol (IPA phoneme) and position
            (beginning/middle/end/random)
    """

    language: str
    age: int
    selected_sound: PostWordListGeneratorBodySelectedSound
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        language = self.language

        age = self.age

        selected_sound = self.selected_sound.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "language": language,
                "age": age,
                "selectedSound": selected_sound,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_word_list_generator_body_selected_sound import (
            PostWordListGeneratorBodySelectedSound,
        )

        d = dict(src_dict)
        language = d.pop("language")

        age = d.pop("age")

        selected_sound = PostWordListGeneratorBodySelectedSound.from_dict(d.pop("selectedSound"))

        post_word_list_generator_body = cls(
            language=language,
            age=age,
            selected_sound=selected_sound,
        )

        post_word_list_generator_body.additional_properties = d
        return post_word_list_generator_body

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
