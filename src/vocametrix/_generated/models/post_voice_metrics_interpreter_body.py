from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_voice_metrics_interpreter_body_metrics import (
        PostVoiceMetricsInterpreterBodyMetrics,
    )
    from ..models.post_voice_metrics_interpreter_body_praat_results import (
        PostVoiceMetricsInterpreterBodyPraatResults,
    )


T = TypeVar("T", bound="PostVoiceMetricsInterpreterBody")


@_attrs_define
class PostVoiceMetricsInterpreterBody:
    """
    Attributes:
        metrics (PostVoiceMetricsInterpreterBodyMetrics): REQUIRED. Object of voice metrics — typical keys: jitter,
            shimmer, hnr, cpps, etc. (validated server-side).
        age (int): REQUIRED. Patient age in years (1–120).
        gender (str): REQUIRED. "male" | "female" | "other".
        language_code (str | Unset): Optional. Output language code — server applies a default via validateLanguageCode
            if omitted.
        thread_id (str | Unset): Optional. Azure AI Foundry thread ID for multi-turn continuity.
        praat_results (PostVoiceMetricsInterpreterBodyPraatResults | Unset): Optional. Full Praat output object — when
            present, the server merges F0 / expected-range fields into the metrics for richer interpretation.
        email (str | Unset): Optional. Used by anonymous-key validation flow.
    """

    metrics: PostVoiceMetricsInterpreterBodyMetrics
    age: int
    gender: str
    language_code: str | Unset = UNSET
    thread_id: str | Unset = UNSET
    praat_results: PostVoiceMetricsInterpreterBodyPraatResults | Unset = UNSET
    email: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metrics = self.metrics.to_dict()

        age = self.age

        gender = self.gender

        language_code = self.language_code

        thread_id = self.thread_id

        praat_results: dict[str, Any] | Unset = UNSET
        if not isinstance(self.praat_results, Unset):
            praat_results = self.praat_results.to_dict()

        email = self.email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metrics": metrics,
                "age": age,
                "gender": gender,
            }
        )
        if language_code is not UNSET:
            field_dict["languageCode"] = language_code
        if thread_id is not UNSET:
            field_dict["threadId"] = thread_id
        if praat_results is not UNSET:
            field_dict["praatResults"] = praat_results
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_voice_metrics_interpreter_body_metrics import (
            PostVoiceMetricsInterpreterBodyMetrics,
        )
        from ..models.post_voice_metrics_interpreter_body_praat_results import (
            PostVoiceMetricsInterpreterBodyPraatResults,
        )

        d = dict(src_dict)
        metrics = PostVoiceMetricsInterpreterBodyMetrics.from_dict(d.pop("metrics"))

        age = d.pop("age")

        gender = d.pop("gender")

        language_code = d.pop("languageCode", UNSET)

        thread_id = d.pop("threadId", UNSET)

        _praat_results = d.pop("praatResults", UNSET)
        praat_results: PostVoiceMetricsInterpreterBodyPraatResults | Unset
        if isinstance(_praat_results, Unset):
            praat_results = UNSET
        else:
            praat_results = PostVoiceMetricsInterpreterBodyPraatResults.from_dict(_praat_results)

        email = d.pop("email", UNSET)

        post_voice_metrics_interpreter_body = cls(
            metrics=metrics,
            age=age,
            gender=gender,
            language_code=language_code,
            thread_id=thread_id,
            praat_results=praat_results,
            email=email,
        )

        post_voice_metrics_interpreter_body.additional_properties = d
        return post_voice_metrics_interpreter_body

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
