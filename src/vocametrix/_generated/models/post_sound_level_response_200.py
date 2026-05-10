from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostSoundLevelResponse200")


@_attrs_define
class PostSoundLevelResponse200:
    """
    Attributes:
        sound_level (float | Unset): Number — dB value rounded to 2 decimals.
        unit (str | Unset): String — currently "dB SPL".
        frequency_range (float | Unset): String — currently "20-8000 Hz".
    """

    sound_level: float | Unset = UNSET
    unit: str | Unset = UNSET
    frequency_range: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sound_level = self.sound_level

        unit = self.unit

        frequency_range = self.frequency_range

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sound_level is not UNSET:
            field_dict["soundLevel"] = sound_level
        if unit is not UNSET:
            field_dict["unit"] = unit
        if frequency_range is not UNSET:
            field_dict["frequencyRange"] = frequency_range

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sound_level = d.pop("soundLevel", UNSET)

        unit = d.pop("unit", UNSET)

        frequency_range = d.pop("frequencyRange", UNSET)

        post_sound_level_response_200 = cls(
            sound_level=sound_level,
            unit=unit,
            frequency_range=frequency_range,
        )

        post_sound_level_response_200.additional_properties = d
        return post_sound_level_response_200

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
