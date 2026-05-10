from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostPronunciationAssessmentResponse200")


@_attrs_define
class PostPronunciationAssessmentResponse200:
    """
    Attributes:
        accuracy_score (float | Unset): Phoneme-level pronunciation accuracy score (0-100)
        fluency_score (float | Unset): Natural speech flow and timing score (0-100)
        completeness_score (float | Unset): Coverage of reference text score (0-100)
        prosody_score (float | Unset): Speech qualities assessment score (0-100)
        pron_score (float | Unset): Overall weighted pronunciation score
        error (str | Unset): Error details with specific rejection reasons if applicable
    """

    accuracy_score: float | Unset = UNSET
    fluency_score: float | Unset = UNSET
    completeness_score: float | Unset = UNSET
    prosody_score: float | Unset = UNSET
    pron_score: float | Unset = UNSET
    error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accuracy_score = self.accuracy_score

        fluency_score = self.fluency_score

        completeness_score = self.completeness_score

        prosody_score = self.prosody_score

        pron_score = self.pron_score

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accuracy_score is not UNSET:
            field_dict["accuracyScore"] = accuracy_score
        if fluency_score is not UNSET:
            field_dict["fluencyScore"] = fluency_score
        if completeness_score is not UNSET:
            field_dict["completenessScore"] = completeness_score
        if prosody_score is not UNSET:
            field_dict["prosodyScore"] = prosody_score
        if pron_score is not UNSET:
            field_dict["pronScore"] = pron_score
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accuracy_score = d.pop("accuracyScore", UNSET)

        fluency_score = d.pop("fluencyScore", UNSET)

        completeness_score = d.pop("completenessScore", UNSET)

        prosody_score = d.pop("prosodyScore", UNSET)

        pron_score = d.pop("pronScore", UNSET)

        error = d.pop("error", UNSET)

        post_pronunciation_assessment_response_200 = cls(
            accuracy_score=accuracy_score,
            fluency_score=fluency_score,
            completeness_score=completeness_score,
            prosody_score=prosody_score,
            pron_score=pron_score,
            error=error,
        )

        post_pronunciation_assessment_response_200.additional_properties = d
        return post_pronunciation_assessment_response_200

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
