from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCalculateCppResponse200")


@_attrs_define
class GetCalculateCppResponse200:
    """
    Attributes:
        cpp (float | Unset): Cepstral Peak Prominence value in dB. Example: 12.45
        voice_quality (str | Unset): Clinical voice quality assessment. Example: "Good voice quality"
        severity (str | Unset): Dysphonia severity classification. Example: "Normal"
    """

    cpp: float | Unset = UNSET
    voice_quality: str | Unset = UNSET
    severity: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpp = self.cpp

        voice_quality = self.voice_quality

        severity = self.severity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpp is not UNSET:
            field_dict["CPP"] = cpp
        if voice_quality is not UNSET:
            field_dict["VOICE_QUALITY"] = voice_quality
        if severity is not UNSET:
            field_dict["SEVERITY"] = severity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cpp = d.pop("CPP", UNSET)

        voice_quality = d.pop("VOICE_QUALITY", UNSET)

        severity = d.pop("SEVERITY", UNSET)

        get_calculate_cpp_response_200 = cls(
            cpp=cpp,
            voice_quality=voice_quality,
            severity=severity,
        )

        get_calculate_cpp_response_200.additional_properties = d
        return get_calculate_cpp_response_200

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
