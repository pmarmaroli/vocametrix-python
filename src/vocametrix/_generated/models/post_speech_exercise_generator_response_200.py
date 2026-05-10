from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostSpeechExerciseGeneratorResponse200")


@_attrs_define
class PostSpeechExerciseGeneratorResponse200:
    """
    Attributes:
        response (str | Unset): The agent reply containing the generated exercises as structured text
        thread_id (str | Unset): Conversation thread ID — pass it back to continue the same session
        agent_name (str | Unset): Identifier of the agent that produced the reply
        run_status (str | Unset): Internal run state (e.g., "completed")
        remaining_credits (float | Unset): Number of API credits remaining in your account
        is_anonymous_session (bool | Unset): Boolean — true if the call used an anonymous_<sessionId> key
        parameters (str | Unset): Echo of the parameters used to produce the reply (ageLevel, speechChallenge, language)
    """

    response: str | Unset = UNSET
    thread_id: str | Unset = UNSET
    agent_name: str | Unset = UNSET
    run_status: str | Unset = UNSET
    remaining_credits: float | Unset = UNSET
    is_anonymous_session: bool | Unset = UNSET
    parameters: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        response = self.response

        thread_id = self.thread_id

        agent_name = self.agent_name

        run_status = self.run_status

        remaining_credits = self.remaining_credits

        is_anonymous_session = self.is_anonymous_session

        parameters = self.parameters

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if response is not UNSET:
            field_dict["response"] = response
        if thread_id is not UNSET:
            field_dict["threadId"] = thread_id
        if agent_name is not UNSET:
            field_dict["agentName"] = agent_name
        if run_status is not UNSET:
            field_dict["runStatus"] = run_status
        if remaining_credits is not UNSET:
            field_dict["remaining_credits"] = remaining_credits
        if is_anonymous_session is not UNSET:
            field_dict["isAnonymousSession"] = is_anonymous_session
        if parameters is not UNSET:
            field_dict["parameters"] = parameters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        response = d.pop("response", UNSET)

        thread_id = d.pop("threadId", UNSET)

        agent_name = d.pop("agentName", UNSET)

        run_status = d.pop("runStatus", UNSET)

        remaining_credits = d.pop("remaining_credits", UNSET)

        is_anonymous_session = d.pop("isAnonymousSession", UNSET)

        parameters = d.pop("parameters", UNSET)

        post_speech_exercise_generator_response_200 = cls(
            response=response,
            thread_id=thread_id,
            agent_name=agent_name,
            run_status=run_status,
            remaining_credits=remaining_credits,
            is_anonymous_session=is_anonymous_session,
            parameters=parameters,
        )

        post_speech_exercise_generator_response_200.additional_properties = d
        return post_speech_exercise_generator_response_200

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
