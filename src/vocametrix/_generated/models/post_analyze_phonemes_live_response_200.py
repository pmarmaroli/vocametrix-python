from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostAnalyzePhonemesLiveResponse200")


@_attrs_define
class PostAnalyzePhonemesLiveResponse200:
    """
    Attributes:
        python_output (str | Unset): JSON shape produced by the underlying phoneme client. Typical fields: `phonemes: [{
            label, start_ms, end_ms, confidence }, ...]`, `language`, `model_used`. Exact shape is not enumerated by the JS
            layer and is determined by the per-language Python client (see python/phonemes/french/phoneme_client.py and
            python/phonemes/estonian/phoneme_client.py).
    """

    python_output: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        python_output = self.python_output

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if python_output is not UNSET:
            field_dict["<python output>"] = python_output

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        python_output = d.pop("<python output>", UNSET)

        post_analyze_phonemes_live_response_200 = cls(
            python_output=python_output,
        )

        post_analyze_phonemes_live_response_200.additional_properties = d
        return post_analyze_phonemes_live_response_200

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
