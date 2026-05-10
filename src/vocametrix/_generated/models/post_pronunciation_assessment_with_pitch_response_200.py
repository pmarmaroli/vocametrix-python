from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_pronunciation_assessment_with_pitch_response_200n_best_item import (
        PostPronunciationAssessmentWithPitchResponse200NBestItem,
    )


T = TypeVar("T", bound="PostPronunciationAssessmentWithPitchResponse200")


@_attrs_define
class PostPronunciationAssessmentWithPitchResponse200:
    """
    Attributes:
        recognition_status (str | Unset): Azure recognition status (e.g., "Success")
        offset (str | Unset): Recognition start offset in 100-nanosecond units
        duration (str | Unset): Recognition duration in 100-nanosecond units
        display_text (str | Unset): The recognized text with proper formatting
        n_best (list[PostPronunciationAssessmentWithPitchResponse200NBestItem] | Unset): Array of N-best recognition
            hypotheses. Each NBest[i] contains the standard Azure pronunciation fields (Confidence, Lexical, ITN, MaskedITN,
            Display, PronunciationAssessment, Words[]) — and each NBest[i].Words[j] is augmented with an additional `Pitch`
            array containing F0 samples (Hz) measured over the word's timespan via parselmouth. Words[j] also carry the
            standard Azure fields: Word, Offset, Duration, PronunciationAssessment {AccuracyScore, ErrorType}, Phonemes[],
            Syllables[].
    """

    recognition_status: str | Unset = UNSET
    offset: str | Unset = UNSET
    duration: str | Unset = UNSET
    display_text: str | Unset = UNSET
    n_best: list[PostPronunciationAssessmentWithPitchResponse200NBestItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        recognition_status = self.recognition_status

        offset = self.offset

        duration = self.duration

        display_text = self.display_text

        n_best: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.n_best, Unset):
            n_best = []
            for n_best_item_data in self.n_best:
                n_best_item = n_best_item_data.to_dict()
                n_best.append(n_best_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if recognition_status is not UNSET:
            field_dict["RecognitionStatus"] = recognition_status
        if offset is not UNSET:
            field_dict["Offset"] = offset
        if duration is not UNSET:
            field_dict["Duration"] = duration
        if display_text is not UNSET:
            field_dict["DisplayText"] = display_text
        if n_best is not UNSET:
            field_dict["NBest"] = n_best

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_pronunciation_assessment_with_pitch_response_200n_best_item import (
            PostPronunciationAssessmentWithPitchResponse200NBestItem,
        )

        d = dict(src_dict)
        recognition_status = d.pop("RecognitionStatus", UNSET)

        offset = d.pop("Offset", UNSET)

        duration = d.pop("Duration", UNSET)

        display_text = d.pop("DisplayText", UNSET)

        _n_best = d.pop("NBest", UNSET)
        n_best: list[PostPronunciationAssessmentWithPitchResponse200NBestItem] | Unset = UNSET
        if _n_best is not UNSET:
            n_best = []
            for n_best_item_data in _n_best:
                n_best_item = PostPronunciationAssessmentWithPitchResponse200NBestItem.from_dict(
                    n_best_item_data
                )

                n_best.append(n_best_item)

        post_pronunciation_assessment_with_pitch_response_200 = cls(
            recognition_status=recognition_status,
            offset=offset,
            duration=duration,
            display_text=display_text,
            n_best=n_best,
        )

        post_pronunciation_assessment_with_pitch_response_200.additional_properties = d
        return post_pronunciation_assessment_with_pitch_response_200

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
