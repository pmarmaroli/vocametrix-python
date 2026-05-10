from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_therapy_planning_agent_body_session_metadata import (
        PostTherapyPlanningAgentBodySessionMetadata,
    )
    from ..models.post_therapy_planning_agent_body_wav_2_vec_output import (
        PostTherapyPlanningAgentBodyWav2VecOutput,
    )


T = TypeVar("T", bound="PostTherapyPlanningAgentBody")


@_attrs_define
class PostTherapyPlanningAgentBody:
    """
    Attributes:
        session_metadata (PostTherapyPlanningAgentBodySessionMetadata): REQUIRED. Object — must include `patient_id`
            (string). May also include `session_id`, `timestamp`, `audio_file`.
        wav2vec_output (PostTherapyPlanningAgentBodyWav2VecOutput): REQUIRED. Object — must include `summary_statistics`
            (typically `{disfluency_types_detected, overall_fluency_rate, total_segments, ...}`).
        patient_anamnesis (str | Unset): Optional. Patient context — `demographics: {age}`, `clinical_history:
            {diagnosis, severity}`, `therapy_information: {current_treatment_approach, total_sessions_completed}`, etc.
        email (str | Unset): Optional. Used by anonymous-key validation flow.
    """

    session_metadata: PostTherapyPlanningAgentBodySessionMetadata
    wav2vec_output: PostTherapyPlanningAgentBodyWav2VecOutput
    patient_anamnesis: str | Unset = UNSET
    email: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        session_metadata = self.session_metadata.to_dict()

        wav2vec_output = self.wav2vec_output.to_dict()

        patient_anamnesis = self.patient_anamnesis

        email = self.email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "session_metadata": session_metadata,
                "wav2vec_output": wav2vec_output,
            }
        )
        if patient_anamnesis is not UNSET:
            field_dict["patient_anamnesis"] = patient_anamnesis
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_therapy_planning_agent_body_session_metadata import (
            PostTherapyPlanningAgentBodySessionMetadata,
        )
        from ..models.post_therapy_planning_agent_body_wav_2_vec_output import (
            PostTherapyPlanningAgentBodyWav2VecOutput,
        )

        d = dict(src_dict)
        session_metadata = PostTherapyPlanningAgentBodySessionMetadata.from_dict(
            d.pop("session_metadata")
        )

        wav2vec_output = PostTherapyPlanningAgentBodyWav2VecOutput.from_dict(
            d.pop("wav2vec_output")
        )

        patient_anamnesis = d.pop("patient_anamnesis", UNSET)

        email = d.pop("email", UNSET)

        post_therapy_planning_agent_body = cls(
            session_metadata=session_metadata,
            wav2vec_output=wav2vec_output,
            patient_anamnesis=patient_anamnesis,
            email=email,
        )

        post_therapy_planning_agent_body.additional_properties = d
        return post_therapy_planning_agent_body

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
