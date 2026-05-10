from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostSyntaxCheckerAgentBody")


@_attrs_define
class PostSyntaxCheckerAgentBody:
    """
    Attributes:
        text (str): REQUIRED. Text to analyze (≤ 5000 characters).
        locale (str): REQUIRED. Language code (validated via validateLanguageCode).
        thread_id (str | Unset): Optional. Thread ID for multi-turn continuity.
        email (str | Unset): Optional. Used by anonymous-key validation flow.
    """

    text: str
    locale: str
    thread_id: str | Unset = UNSET
    email: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        locale = self.locale

        thread_id = self.thread_id

        email = self.email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
                "locale": locale,
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
        text = d.pop("text")

        locale = d.pop("locale")

        thread_id = d.pop("threadId", UNSET)

        email = d.pop("email", UNSET)

        post_syntax_checker_agent_body = cls(
            text=text,
            locale=locale,
            thread_id=thread_id,
            email=email,
        )

        post_syntax_checker_agent_body.additional_properties = d
        return post_syntax_checker_agent_body

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
