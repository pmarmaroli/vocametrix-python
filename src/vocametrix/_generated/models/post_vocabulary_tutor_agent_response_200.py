from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_vocabulary_tutor_agent_response_200_metadata import (
        PostVocabularyTutorAgentResponse200Metadata,
    )


T = TypeVar("T", bound="PostVocabularyTutorAgentResponse200")


@_attrs_define
class PostVocabularyTutorAgentResponse200:
    """
    Attributes:
        success (bool | Unset): Boolean.
        response (str | Unset): String — the agent's free-form text reply.
        thread_id (str | Unset): Thread ID for the conversation (use to continue).
        metadata (PostVocabularyTutorAgentResponse200Metadata | Unset): Object: { nativeLanguage, targetLanguage,
            ageGroup, topic, runId, runStatus }.
    """

    success: bool | Unset = UNSET
    response: str | Unset = UNSET
    thread_id: str | Unset = UNSET
    metadata: PostVocabularyTutorAgentResponse200Metadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        response = self.response

        thread_id = self.thread_id

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if response is not UNSET:
            field_dict["response"] = response
        if thread_id is not UNSET:
            field_dict["threadId"] = thread_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_vocabulary_tutor_agent_response_200_metadata import (
            PostVocabularyTutorAgentResponse200Metadata,
        )

        d = dict(src_dict)
        success = d.pop("success", UNSET)

        response = d.pop("response", UNSET)

        thread_id = d.pop("threadId", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: PostVocabularyTutorAgentResponse200Metadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PostVocabularyTutorAgentResponse200Metadata.from_dict(_metadata)

        post_vocabulary_tutor_agent_response_200 = cls(
            success=success,
            response=response,
            thread_id=thread_id,
            metadata=metadata,
        )

        post_vocabulary_tutor_agent_response_200.additional_properties = d
        return post_vocabulary_tutor_agent_response_200

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
