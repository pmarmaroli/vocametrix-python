from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetTherapyResultBySessionIdResponse200")


@_attrs_define
class GetTherapyResultBySessionIdResponse200:
    """
    Attributes:
        therapy_session (str | Unset): { success, message, nodejs_session_id, ...result } — `result` is whatever the
            LangGraph workflow saved. Typical fields include `therapySession.sessionMetadata`, exercise plans, generated
            HTML paths (`html_clinician_final`, `output_file`), and free-form workflow output. The full keyset is determined
            by the Python workflow, not the JS layer.
        classification_session (float | Unset): { success, session_id, patient_id, classification,
            classificationMetadata, overallClassification, timestamp }. `classification` is an array of ~4s blocks; each: {
            blockId, startTime, stopTime (s), primaryType
            (fluent/block/Soundrepetition/Wordrepetition/prolongation/interjection), secondaryTypes, confidence,
            characteristics, transcription, words, phonemes }. `words` holds per-word timestamps { word, start, end } in
            seconds (present when transcribe=true; blocks overlap, so a word may repeat across adjacent blocks). `phonemes`
            is "N/A" unless includePhonemes=true.
    """

    therapy_session: str | Unset = UNSET
    classification_session: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        therapy_session = self.therapy_session

        classification_session = self.classification_session

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if therapy_session is not UNSET:
            field_dict["<therapy session>"] = therapy_session
        if classification_session is not UNSET:
            field_dict["<classification session>"] = classification_session

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        therapy_session = d.pop("<therapy session>", UNSET)

        classification_session = d.pop("<classification session>", UNSET)

        get_therapy_result_by_session_id_response_200 = cls(
            therapy_session=therapy_session,
            classification_session=classification_session,
        )

        get_therapy_result_by_session_id_response_200.additional_properties = d
        return get_therapy_result_by_session_id_response_200

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
