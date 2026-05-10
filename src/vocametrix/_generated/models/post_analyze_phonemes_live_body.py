from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostAnalyzePhonemesLiveBody")


@_attrs_define
class PostAnalyzePhonemesLiveBody:
    """
    Attributes:
        file_id (str | Unset): Optional (use this OR blobUrl). fileId from a prior /api/assignFileId upload.
        blob_url (str | Unset): Optional (use this OR fileId). HTTPS URL of the audio file. Will be downloaded server-
            side. If the host is `vocametrixstorageaccount.blob.core.windows.net` and `keepBlob` is false, the blob is
            deleted after processing.
        reference_word (str | Unset): Optional. Currently accepted by the API but not used by the JavaScript layer
            (passed through to the Python script which may use it).
        language (str | Unset): Optional, default "fr-FR". Accepted: "fr-FR" | "et-EE".
        model (str | Unset): Optional. Alias for an alternative ASR model (must pass server-side `isKnownAlias`).
            Resolved to a model URL internally.
        keep_blob (str | Unset): Optional, default false. If false and `blobUrl` was used, the source blob is deleted
            after success (only when hosted on the Vocametrix storage account).
    """

    file_id: str | Unset = UNSET
    blob_url: str | Unset = UNSET
    reference_word: str | Unset = UNSET
    language: str | Unset = UNSET
    model: str | Unset = UNSET
    keep_blob: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_id = self.file_id

        blob_url = self.blob_url

        reference_word = self.reference_word

        language = self.language

        model = self.model

        keep_blob = self.keep_blob

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_id is not UNSET:
            field_dict["fileId"] = file_id
        if blob_url is not UNSET:
            field_dict["blobUrl"] = blob_url
        if reference_word is not UNSET:
            field_dict["referenceWord"] = reference_word
        if language is not UNSET:
            field_dict["language"] = language
        if model is not UNSET:
            field_dict["model"] = model
        if keep_blob is not UNSET:
            field_dict["keepBlob"] = keep_blob

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_id = d.pop("fileId", UNSET)

        blob_url = d.pop("blobUrl", UNSET)

        reference_word = d.pop("referenceWord", UNSET)

        language = d.pop("language", UNSET)

        model = d.pop("model", UNSET)

        keep_blob = d.pop("keepBlob", UNSET)

        post_analyze_phonemes_live_body = cls(
            file_id=file_id,
            blob_url=blob_url,
            reference_word=reference_word,
            language=language,
            model=model,
            keep_blob=keep_blob,
        )

        post_analyze_phonemes_live_body.additional_properties = d
        return post_analyze_phonemes_live_body

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
