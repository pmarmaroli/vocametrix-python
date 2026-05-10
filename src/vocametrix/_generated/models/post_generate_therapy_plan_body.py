from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_generate_therapy_plan_body_patient_metadata import (
        PostGenerateTherapyPlanBodyPatientMetadata,
    )


T = TypeVar("T", bound="PostGenerateTherapyPlanBody")


@_attrs_define
class PostGenerateTherapyPlanBody:
    """
    Attributes:
        file_id (str): REQUIRED. fileId from a prior /api/assignFileId upload.
        patient_id (str): REQUIRED. Patient identifier matching ^[a-zA-Z0-9_-]{1,100}$. The literal "PT-UNKNOWN" is
            explicitly rejected.
        patient_metadata (PostGenerateTherapyPlanBodyPatientMetadata | Unset): Optional. Object describing the patient.
            Max 10,000 bytes when JSON-serialized. Optional sub-fields: demographics.age (0–120), clinical_history.severity
            ("Mild"|"Moderate"|"Severe"|"Very Severe"), current_goals (max 20 entries), recent_progress_notes (max 50),
            previous_exercises (max 30).
        max_iterations (int | Unset): Optional integer 1–5, default 2. Max critic-agent iterations within the workflow.
        therapy_agent_temperature (float | Unset): Optional number, default 0.3. Generation temperature for the therapy-
            planner LLM.
        critic_agent_temperature (float | Unset): Optional number, default 0. Generation temperature for the critic LLM.
        classification_session_id (str | Unset): Optional string. If present, links the new therapy session to a prior
            /api/classify-stuttering session so the workflow can use those classification results.
        use_azure_ml (bool | Unset): Optional boolean, default true. Whether to use Azure ML inside the workflow.
    """

    file_id: str
    patient_id: str
    patient_metadata: PostGenerateTherapyPlanBodyPatientMetadata | Unset = UNSET
    max_iterations: int | Unset = UNSET
    therapy_agent_temperature: float | Unset = UNSET
    critic_agent_temperature: float | Unset = UNSET
    classification_session_id: str | Unset = UNSET
    use_azure_ml: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_id = self.file_id

        patient_id = self.patient_id

        patient_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.patient_metadata, Unset):
            patient_metadata = self.patient_metadata.to_dict()

        max_iterations = self.max_iterations

        therapy_agent_temperature = self.therapy_agent_temperature

        critic_agent_temperature = self.critic_agent_temperature

        classification_session_id = self.classification_session_id

        use_azure_ml = self.use_azure_ml

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fileId": file_id,
                "patientId": patient_id,
            }
        )
        if patient_metadata is not UNSET:
            field_dict["patientMetadata"] = patient_metadata
        if max_iterations is not UNSET:
            field_dict["maxIterations"] = max_iterations
        if therapy_agent_temperature is not UNSET:
            field_dict["therapyAgentTemperature"] = therapy_agent_temperature
        if critic_agent_temperature is not UNSET:
            field_dict["criticAgentTemperature"] = critic_agent_temperature
        if classification_session_id is not UNSET:
            field_dict["classificationSessionId"] = classification_session_id
        if use_azure_ml is not UNSET:
            field_dict["useAzureML"] = use_azure_ml

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_generate_therapy_plan_body_patient_metadata import (
            PostGenerateTherapyPlanBodyPatientMetadata,
        )

        d = dict(src_dict)
        file_id = d.pop("fileId")

        patient_id = d.pop("patientId")

        _patient_metadata = d.pop("patientMetadata", UNSET)
        patient_metadata: PostGenerateTherapyPlanBodyPatientMetadata | Unset
        if isinstance(_patient_metadata, Unset):
            patient_metadata = UNSET
        else:
            patient_metadata = PostGenerateTherapyPlanBodyPatientMetadata.from_dict(
                _patient_metadata
            )

        max_iterations = d.pop("maxIterations", UNSET)

        therapy_agent_temperature = d.pop("therapyAgentTemperature", UNSET)

        critic_agent_temperature = d.pop("criticAgentTemperature", UNSET)

        classification_session_id = d.pop("classificationSessionId", UNSET)

        use_azure_ml = d.pop("useAzureML", UNSET)

        post_generate_therapy_plan_body = cls(
            file_id=file_id,
            patient_id=patient_id,
            patient_metadata=patient_metadata,
            max_iterations=max_iterations,
            therapy_agent_temperature=therapy_agent_temperature,
            critic_agent_temperature=critic_agent_temperature,
            classification_session_id=classification_session_id,
            use_azure_ml=use_azure_ml,
        )

        post_generate_therapy_plan_body.additional_properties = d
        return post_generate_therapy_plan_body

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
