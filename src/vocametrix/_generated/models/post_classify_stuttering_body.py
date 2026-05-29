from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostClassifyStutteringBody")


@_attrs_define
class PostClassifyStutteringBody:
    """
    Attributes:
        file_id (str): REQUIRED. fileId from a prior /api/assignFileId upload.
        patient_id (str | Unset): Optional, default "unknown". Patient identifier — the literal value "PT-UNKNOWN" is
            explicitly rejected (use "unknown" or a real ID).
        chunk_overlap (str | Unset): Optional, default 0.25. Overlap fraction between analysis chunks.
        chunk_size (float | Unset): Optional, default 4. Chunk size in seconds.
        locale (str | Unset): Optional, default "en-US". Locale used by the speech-to-text step within the
            classification pipeline.
        transcribe (bool | Unset): optional (default true). When true, the recording is transcribed once (real-time STT)
            and each result block includes its transcription plus a `words` array of per-word timestamps. Set false to skip
            transcription for minimum latency.
        include_phonemes (bool | Unset): optional (default false). When true, per-block phonetic transcription is
            computed (slower). When false, each block's `phonemes` is "N/A".
    """

    file_id: str
    patient_id: str | Unset = UNSET
    chunk_overlap: str | Unset = UNSET
    chunk_size: float | Unset = UNSET
    locale: str | Unset = UNSET
    transcribe: bool | Unset = UNSET
    include_phonemes: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_id = self.file_id

        patient_id = self.patient_id

        chunk_overlap = self.chunk_overlap

        chunk_size = self.chunk_size

        locale = self.locale

        transcribe = self.transcribe

        include_phonemes = self.include_phonemes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fileId": file_id,
            }
        )
        if patient_id is not UNSET:
            field_dict["patientId"] = patient_id
        if chunk_overlap is not UNSET:
            field_dict["chunkOverlap"] = chunk_overlap
        if chunk_size is not UNSET:
            field_dict["chunkSize"] = chunk_size
        if locale is not UNSET:
            field_dict["locale"] = locale
        if transcribe is not UNSET:
            field_dict["transcribe"] = transcribe
        if include_phonemes is not UNSET:
            field_dict["includePhonemes"] = include_phonemes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_id = d.pop("fileId")

        patient_id = d.pop("patientId", UNSET)

        chunk_overlap = d.pop("chunkOverlap", UNSET)

        chunk_size = d.pop("chunkSize", UNSET)

        locale = d.pop("locale", UNSET)

        transcribe = d.pop("transcribe", UNSET)

        include_phonemes = d.pop("includePhonemes", UNSET)

        post_classify_stuttering_body = cls(
            file_id=file_id,
            patient_id=patient_id,
            chunk_overlap=chunk_overlap,
            chunk_size=chunk_size,
            locale=locale,
            transcribe=transcribe,
            include_phonemes=include_phonemes,
        )

        post_classify_stuttering_body.additional_properties = d
        return post_classify_stuttering_body

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
