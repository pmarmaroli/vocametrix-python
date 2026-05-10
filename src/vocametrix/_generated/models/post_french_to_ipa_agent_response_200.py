from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_french_to_ipa_agent_response_200_result import (
        PostFrenchToIpaAgentResponse200Result,
    )


T = TypeVar("T", bound="PostFrenchToIpaAgentResponse200")


@_attrs_define
class PostFrenchToIpaAgentResponse200:
    """
    Attributes:
        success (bool | Unset): Boolean.
        result (PostFrenchToIpaAgentResponse200Result | Unset): Object OR array of objects, mirroring the input shape.
            Each entry has the form { word, ipa: [...], ... }. The server checks `result.ipa.length` to count
            transcriptions; the rest of the shape is determined by the agent.
        thread_id (str | Unset): Thread ID.
        agent_name (str | Unset): Agent identifier.
        remaining_credits (float | Unset): Number.
        is_anonymous_session (bool | Unset): Boolean.
    """

    success: bool | Unset = UNSET
    result: PostFrenchToIpaAgentResponse200Result | Unset = UNSET
    thread_id: str | Unset = UNSET
    agent_name: str | Unset = UNSET
    remaining_credits: float | Unset = UNSET
    is_anonymous_session: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        thread_id = self.thread_id

        agent_name = self.agent_name

        remaining_credits = self.remaining_credits

        is_anonymous_session = self.is_anonymous_session

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if result is not UNSET:
            field_dict["result"] = result
        if thread_id is not UNSET:
            field_dict["threadId"] = thread_id
        if agent_name is not UNSET:
            field_dict["agentName"] = agent_name
        if remaining_credits is not UNSET:
            field_dict["remaining_credits"] = remaining_credits
        if is_anonymous_session is not UNSET:
            field_dict["isAnonymousSession"] = is_anonymous_session

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_french_to_ipa_agent_response_200_result import (
            PostFrenchToIpaAgentResponse200Result,
        )

        d = dict(src_dict)
        success = d.pop("success", UNSET)

        _result = d.pop("result", UNSET)
        result: PostFrenchToIpaAgentResponse200Result | Unset
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = PostFrenchToIpaAgentResponse200Result.from_dict(_result)

        thread_id = d.pop("threadId", UNSET)

        agent_name = d.pop("agentName", UNSET)

        remaining_credits = d.pop("remaining_credits", UNSET)

        is_anonymous_session = d.pop("isAnonymousSession", UNSET)

        post_french_to_ipa_agent_response_200 = cls(
            success=success,
            result=result,
            thread_id=thread_id,
            agent_name=agent_name,
            remaining_credits=remaining_credits,
            is_anonymous_session=is_anonymous_session,
        )

        post_french_to_ipa_agent_response_200.additional_properties = d
        return post_french_to_ipa_agent_response_200

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
