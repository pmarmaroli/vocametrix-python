from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_french_to_ipa_agent_body_phonetic_input_item import (
        PostFrenchToIpaAgentBodyPhoneticInputItem,
    )


T = TypeVar("T", bound="PostFrenchToIpaAgentBody")


@_attrs_define
class PostFrenchToIpaAgentBody:
    """
    Attributes:
        phonetic_input (list[PostFrenchToIpaAgentBodyPhoneticInputItem]): REQUIRED. Either a single French word as a
            string, OR a JSON-stringified array of up to 20 strings. The server detects which by attempting JSON.parse.
        thread_id (str | Unset): Optional. Thread ID for multi-turn continuity.
        email (str | Unset): Optional. Used by anonymous-key validation flow.
    """

    phonetic_input: list[PostFrenchToIpaAgentBodyPhoneticInputItem]
    thread_id: str | Unset = UNSET
    email: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phonetic_input = []
        for phonetic_input_item_data in self.phonetic_input:
            phonetic_input_item = phonetic_input_item_data.to_dict()
            phonetic_input.append(phonetic_input_item)

        thread_id = self.thread_id

        email = self.email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "phoneticInput": phonetic_input,
            }
        )
        if thread_id is not UNSET:
            field_dict["threadId"] = thread_id
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_french_to_ipa_agent_body_phonetic_input_item import (
            PostFrenchToIpaAgentBodyPhoneticInputItem,
        )

        d = dict(src_dict)
        phonetic_input = []
        _phonetic_input = d.pop("phoneticInput")
        for phonetic_input_item_data in _phonetic_input:
            phonetic_input_item = PostFrenchToIpaAgentBodyPhoneticInputItem.from_dict(
                phonetic_input_item_data
            )

            phonetic_input.append(phonetic_input_item)

        thread_id = d.pop("threadId", UNSET)

        email = d.pop("email", UNSET)

        post_french_to_ipa_agent_body = cls(
            phonetic_input=phonetic_input,
            thread_id=thread_id,
            email=email,
        )

        post_french_to_ipa_agent_body.additional_properties = d
        return post_french_to_ipa_agent_body

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
