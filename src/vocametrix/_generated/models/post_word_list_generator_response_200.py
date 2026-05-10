from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_word_list_generator_response_200_word_hint_pairs_item import (
        PostWordListGeneratorResponse200WordHintPairsItem,
    )


T = TypeVar("T", bound="PostWordListGeneratorResponse200")


@_attrs_define
class PostWordListGeneratorResponse200:
    """
    Attributes:
        words (str | Unset): String containing 20 words separated by semicolons
        hints (str | Unset): String containing 20 corresponding hints separated by semicolons
        word_hint_pairs (list[PostWordListGeneratorResponse200WordHintPairsItem] | Unset): Array of objects with word
            and hint properties
    """

    words: str | Unset = UNSET
    hints: str | Unset = UNSET
    word_hint_pairs: list[PostWordListGeneratorResponse200WordHintPairsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        words = self.words

        hints = self.hints

        word_hint_pairs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.word_hint_pairs, Unset):
            word_hint_pairs = []
            for word_hint_pairs_item_data in self.word_hint_pairs:
                word_hint_pairs_item = word_hint_pairs_item_data.to_dict()
                word_hint_pairs.append(word_hint_pairs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if words is not UNSET:
            field_dict["words"] = words
        if hints is not UNSET:
            field_dict["hints"] = hints
        if word_hint_pairs is not UNSET:
            field_dict["wordHintPairs"] = word_hint_pairs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_word_list_generator_response_200_word_hint_pairs_item import (
            PostWordListGeneratorResponse200WordHintPairsItem,
        )

        d = dict(src_dict)
        words = d.pop("words", UNSET)

        hints = d.pop("hints", UNSET)

        _word_hint_pairs = d.pop("wordHintPairs", UNSET)
        word_hint_pairs: list[PostWordListGeneratorResponse200WordHintPairsItem] | Unset = UNSET
        if _word_hint_pairs is not UNSET:
            word_hint_pairs = []
            for word_hint_pairs_item_data in _word_hint_pairs:
                word_hint_pairs_item = PostWordListGeneratorResponse200WordHintPairsItem.from_dict(
                    word_hint_pairs_item_data
                )

                word_hint_pairs.append(word_hint_pairs_item)

        post_word_list_generator_response_200 = cls(
            words=words,
            hints=hints,
            word_hint_pairs=word_hint_pairs,
        )

        post_word_list_generator_response_200.additional_properties = d
        return post_word_list_generator_response_200

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
