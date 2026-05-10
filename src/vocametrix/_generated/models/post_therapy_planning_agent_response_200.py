from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_therapy_planning_agent_response_200_all_messages_item import (
        PostTherapyPlanningAgentResponse200AllMessagesItem,
    )
    from ..models.post_therapy_planning_agent_response_200_metadata import (
        PostTherapyPlanningAgentResponse200Metadata,
    )
    from ..models.post_therapy_planning_agent_response_200_recommendation import (
        PostTherapyPlanningAgentResponse200Recommendation,
    )


T = TypeVar("T", bound="PostTherapyPlanningAgentResponse200")


@_attrs_define
class PostTherapyPlanningAgentResponse200:
    """
    Attributes:
        success (bool | Unset): Boolean.
        thread_id (str | Unset): Azure AI Foundry thread ID (always a new thread for this endpoint).
        run_id (str | Unset): Run ID.
        agent_name (str | Unset): Agent identifier.
        status (str | Unset): Run status string.
        timestamp (datetime.datetime | Unset): ISO 8601 timestamp.
        recommendation (PostTherapyPlanningAgentResponse200Recommendation | Unset): Object — preferred shape contains
            `primary_recommendation` and related structured fields when the agent's JSON parses successfully. Fallback shape
            on parse failure: { raw_response, structured_content: bool, analysis_summary }.
        all_messages (list[PostTherapyPlanningAgentResponse200AllMessagesItem] | Unset): Array — full thread message
            history.
        remaining_credits (float | Unset): Number.
        is_anonymous_session (bool | Unset): Boolean.
        metadata (PostTherapyPlanningAgentResponse200Metadata | Unset): Object: { patient_id, session_id,
            processing_time_seconds, disfluency_types, fluency_rate, total_segments_analyzed, response_metadata:
            {responseLength, containsStructuredData, parseSuccess} }.
    """

    success: bool | Unset = UNSET
    thread_id: str | Unset = UNSET
    run_id: str | Unset = UNSET
    agent_name: str | Unset = UNSET
    status: str | Unset = UNSET
    timestamp: datetime.datetime | Unset = UNSET
    recommendation: PostTherapyPlanningAgentResponse200Recommendation | Unset = UNSET
    all_messages: list[PostTherapyPlanningAgentResponse200AllMessagesItem] | Unset = UNSET
    remaining_credits: float | Unset = UNSET
    is_anonymous_session: bool | Unset = UNSET
    metadata: PostTherapyPlanningAgentResponse200Metadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        thread_id = self.thread_id

        run_id = self.run_id

        agent_name = self.agent_name

        status = self.status

        timestamp: str | Unset = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        recommendation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.recommendation, Unset):
            recommendation = self.recommendation.to_dict()

        all_messages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.all_messages, Unset):
            all_messages = []
            for all_messages_item_data in self.all_messages:
                all_messages_item = all_messages_item_data.to_dict()
                all_messages.append(all_messages_item)

        remaining_credits = self.remaining_credits

        is_anonymous_session = self.is_anonymous_session

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if thread_id is not UNSET:
            field_dict["threadId"] = thread_id
        if run_id is not UNSET:
            field_dict["runId"] = run_id
        if agent_name is not UNSET:
            field_dict["agentName"] = agent_name
        if status is not UNSET:
            field_dict["status"] = status
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if recommendation is not UNSET:
            field_dict["recommendation"] = recommendation
        if all_messages is not UNSET:
            field_dict["allMessages"] = all_messages
        if remaining_credits is not UNSET:
            field_dict["remaining_credits"] = remaining_credits
        if is_anonymous_session is not UNSET:
            field_dict["isAnonymousSession"] = is_anonymous_session
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_therapy_planning_agent_response_200_all_messages_item import (
            PostTherapyPlanningAgentResponse200AllMessagesItem,
        )
        from ..models.post_therapy_planning_agent_response_200_metadata import (
            PostTherapyPlanningAgentResponse200Metadata,
        )
        from ..models.post_therapy_planning_agent_response_200_recommendation import (
            PostTherapyPlanningAgentResponse200Recommendation,
        )

        d = dict(src_dict)
        success = d.pop("success", UNSET)

        thread_id = d.pop("threadId", UNSET)

        run_id = d.pop("runId", UNSET)

        agent_name = d.pop("agentName", UNSET)

        status = d.pop("status", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: datetime.datetime | Unset
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        _recommendation = d.pop("recommendation", UNSET)
        recommendation: PostTherapyPlanningAgentResponse200Recommendation | Unset
        if isinstance(_recommendation, Unset):
            recommendation = UNSET
        else:
            recommendation = PostTherapyPlanningAgentResponse200Recommendation.from_dict(
                _recommendation
            )

        _all_messages = d.pop("allMessages", UNSET)
        all_messages: list[PostTherapyPlanningAgentResponse200AllMessagesItem] | Unset = UNSET
        if _all_messages is not UNSET:
            all_messages = []
            for all_messages_item_data in _all_messages:
                all_messages_item = PostTherapyPlanningAgentResponse200AllMessagesItem.from_dict(
                    all_messages_item_data
                )

                all_messages.append(all_messages_item)

        remaining_credits = d.pop("remaining_credits", UNSET)

        is_anonymous_session = d.pop("isAnonymousSession", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: PostTherapyPlanningAgentResponse200Metadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PostTherapyPlanningAgentResponse200Metadata.from_dict(_metadata)

        post_therapy_planning_agent_response_200 = cls(
            success=success,
            thread_id=thread_id,
            run_id=run_id,
            agent_name=agent_name,
            status=status,
            timestamp=timestamp,
            recommendation=recommendation,
            all_messages=all_messages,
            remaining_credits=remaining_credits,
            is_anonymous_session=is_anonymous_session,
            metadata=metadata,
        )

        post_therapy_planning_agent_response_200.additional_properties = d
        return post_therapy_planning_agent_response_200

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
