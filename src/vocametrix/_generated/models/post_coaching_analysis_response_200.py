from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_coaching_analysis_response_200_audio import (
        PostCoachingAnalysisResponse200Audio,
    )
    from ..models.post_coaching_analysis_response_200_errors import (
        PostCoachingAnalysisResponse200Errors,
    )
    from ..models.post_coaching_analysis_response_200_results import (
        PostCoachingAnalysisResponse200Results,
    )
    from ..models.post_coaching_analysis_response_200_warnings_item import (
        PostCoachingAnalysisResponse200WarningsItem,
    )


T = TypeVar("T", bound="PostCoachingAnalysisResponse200")


@_attrs_define
class PostCoachingAnalysisResponse200:
    """
    Attributes:
        status (str | Unset): "ok" if all sub-calls succeeded, "partial" if at least one failed (the response is still
            returned with whatever succeeded).
        filename (str | Unset): Echo of the input filename.
        label (str | Unset): Echo of the input label.
        language (str | Unset): Echo of the input language.
        mode (str | Unset): Echo of the input mode.
        reference_text (str | Unset): Echo of the reference text (null in free_speech mode).
        transcript_used (str | Unset): The transcript actually used downstream — either the user-provided
            reference_text, or the Azure STT result, or null.
        transcript_source (str | Unset): "user_provided" | "azure_stt" | null.
        audio (PostCoachingAnalysisResponse200Audio | Unset): Object describing the normalized audio: `{
            duration_seconds, sample_rate: 16000, channels: 1 }`.
        results (PostCoachingAnalysisResponse200Results | Unset): Object with one entry per successful sub-call.
            Possible keys: `pitch`, `intensity`, `speech_segments`, `speech_percentage`, `gemaps`, `stuttering`,
            `azure_stt`, `azure_pronunciation`. Each value is the raw payload of the corresponding sub-endpoint.
        errors (PostCoachingAnalysisResponse200Errors | Unset): Object with one entry per FAILED sub-call (same key set
            as `results`). Each value is `{ message, status }`.
        warnings (list[PostCoachingAnalysisResponse200WarningsItem] | Unset): Array of strings — non-fatal advisories
            (e.g., "voice quality not yet wired into orchestrator").
        pipeline_version (str | Unset): String identifying the orchestrator pipeline version. Use this to detect
            behavior changes across deploys.
        processed_at (datetime.datetime | Unset): ISO 8601 timestamp.
        processing_time_ms (str | Unset): Total wall-clock time in milliseconds.
    """

    status: str | Unset = UNSET
    filename: str | Unset = UNSET
    label: str | Unset = UNSET
    language: str | Unset = UNSET
    mode: str | Unset = UNSET
    reference_text: str | Unset = UNSET
    transcript_used: str | Unset = UNSET
    transcript_source: str | Unset = UNSET
    audio: PostCoachingAnalysisResponse200Audio | Unset = UNSET
    results: PostCoachingAnalysisResponse200Results | Unset = UNSET
    errors: PostCoachingAnalysisResponse200Errors | Unset = UNSET
    warnings: list[PostCoachingAnalysisResponse200WarningsItem] | Unset = UNSET
    pipeline_version: str | Unset = UNSET
    processed_at: datetime.datetime | Unset = UNSET
    processing_time_ms: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        filename = self.filename

        label = self.label

        language = self.language

        mode = self.mode

        reference_text = self.reference_text

        transcript_used = self.transcript_used

        transcript_source = self.transcript_source

        audio: dict[str, Any] | Unset = UNSET
        if not isinstance(self.audio, Unset):
            audio = self.audio.to_dict()

        results: dict[str, Any] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = self.results.to_dict()

        errors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors.to_dict()

        warnings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for warnings_item_data in self.warnings:
                warnings_item = warnings_item_data.to_dict()
                warnings.append(warnings_item)

        pipeline_version = self.pipeline_version

        processed_at: str | Unset = UNSET
        if not isinstance(self.processed_at, Unset):
            processed_at = self.processed_at.isoformat()

        processing_time_ms = self.processing_time_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if filename is not UNSET:
            field_dict["filename"] = filename
        if label is not UNSET:
            field_dict["label"] = label
        if language is not UNSET:
            field_dict["language"] = language
        if mode is not UNSET:
            field_dict["mode"] = mode
        if reference_text is not UNSET:
            field_dict["reference_text"] = reference_text
        if transcript_used is not UNSET:
            field_dict["transcript_used"] = transcript_used
        if transcript_source is not UNSET:
            field_dict["transcript_source"] = transcript_source
        if audio is not UNSET:
            field_dict["audio"] = audio
        if results is not UNSET:
            field_dict["results"] = results
        if errors is not UNSET:
            field_dict["errors"] = errors
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if pipeline_version is not UNSET:
            field_dict["pipeline_version"] = pipeline_version
        if processed_at is not UNSET:
            field_dict["processed_at"] = processed_at
        if processing_time_ms is not UNSET:
            field_dict["processing_time_ms"] = processing_time_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_coaching_analysis_response_200_audio import (
            PostCoachingAnalysisResponse200Audio,
        )
        from ..models.post_coaching_analysis_response_200_errors import (
            PostCoachingAnalysisResponse200Errors,
        )
        from ..models.post_coaching_analysis_response_200_results import (
            PostCoachingAnalysisResponse200Results,
        )
        from ..models.post_coaching_analysis_response_200_warnings_item import (
            PostCoachingAnalysisResponse200WarningsItem,
        )

        d = dict(src_dict)
        status = d.pop("status", UNSET)

        filename = d.pop("filename", UNSET)

        label = d.pop("label", UNSET)

        language = d.pop("language", UNSET)

        mode = d.pop("mode", UNSET)

        reference_text = d.pop("reference_text", UNSET)

        transcript_used = d.pop("transcript_used", UNSET)

        transcript_source = d.pop("transcript_source", UNSET)

        _audio = d.pop("audio", UNSET)
        audio: PostCoachingAnalysisResponse200Audio | Unset
        if isinstance(_audio, Unset):
            audio = UNSET
        else:
            audio = PostCoachingAnalysisResponse200Audio.from_dict(_audio)

        _results = d.pop("results", UNSET)
        results: PostCoachingAnalysisResponse200Results | Unset
        if isinstance(_results, Unset):
            results = UNSET
        else:
            results = PostCoachingAnalysisResponse200Results.from_dict(_results)

        _errors = d.pop("errors", UNSET)
        errors: PostCoachingAnalysisResponse200Errors | Unset
        if isinstance(_errors, Unset):
            errors = UNSET
        else:
            errors = PostCoachingAnalysisResponse200Errors.from_dict(_errors)

        _warnings = d.pop("warnings", UNSET)
        warnings: list[PostCoachingAnalysisResponse200WarningsItem] | Unset = UNSET
        if _warnings is not UNSET:
            warnings = []
            for warnings_item_data in _warnings:
                warnings_item = PostCoachingAnalysisResponse200WarningsItem.from_dict(
                    warnings_item_data
                )

                warnings.append(warnings_item)

        pipeline_version = d.pop("pipeline_version", UNSET)

        _processed_at = d.pop("processed_at", UNSET)
        processed_at: datetime.datetime | Unset
        if isinstance(_processed_at, Unset):
            processed_at = UNSET
        else:
            processed_at = isoparse(_processed_at)

        processing_time_ms = d.pop("processing_time_ms", UNSET)

        post_coaching_analysis_response_200 = cls(
            status=status,
            filename=filename,
            label=label,
            language=language,
            mode=mode,
            reference_text=reference_text,
            transcript_used=transcript_used,
            transcript_source=transcript_source,
            audio=audio,
            results=results,
            errors=errors,
            warnings=warnings,
            pipeline_version=pipeline_version,
            processed_at=processed_at,
            processing_time_ms=processing_time_ms,
        )

        post_coaching_analysis_response_200.additional_properties = d
        return post_coaching_analysis_response_200

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
