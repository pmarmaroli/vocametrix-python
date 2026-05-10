from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostSpeechExerciseGeneratorBody")


@_attrs_define
class PostSpeechExerciseGeneratorBody:
    """
    Attributes:
        message (str): REQUIRED. Instructions or context for the exercise generation (e.g., "Generate 5 articulation
            exercises for /r/").
        age_level (str): Patient age range (e.g., "3-6 years", "7-12 years", "adults")
        speech_challenge (str): The specific speech challenge to address (e.g., "R sounds", "S sounds")
        language (str): Target language for exercises (English, French, Spanish)
    """

    message: str
    age_level: str
    speech_challenge: str
    language: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        age_level = self.age_level

        speech_challenge = self.speech_challenge

        language = self.language

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "ageLevel": age_level,
                "speechChallenge": speech_challenge,
                "language": language,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message")

        age_level = d.pop("ageLevel")

        speech_challenge = d.pop("speechChallenge")

        language = d.pop("language")

        post_speech_exercise_generator_body = cls(
            message=message,
            age_level=age_level,
            speech_challenge=speech_challenge,
            language=language,
        )

        post_speech_exercise_generator_body.additional_properties = d
        return post_speech_exercise_generator_body

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
