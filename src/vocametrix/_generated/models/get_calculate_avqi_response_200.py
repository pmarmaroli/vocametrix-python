from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCalculateAvqiResponse200")


@_attrs_define
class GetCalculateAvqiResponse200:
    """
    Attributes:
        avqi (float | Unset): Acoustic Voice Quality Index - final composite score (0-10 scale, dimensionless). Values
            above language-specific threshold indicate potential voice pathology
        cpps (str | Unset): Smoothed Cepstral Peak Prominence measuring harmonic structure (dB). Higher values indicate
            better periodicity and voice quality
        hnr (str | Unset): Mean Harmonics-to-Noise Ratio across concatenated CS+SV signal (dB). Higher values indicate
            less noise relative to harmonic content
        shimmer (float | Unset): Period-to-period amplitude variation expressed as percentage (%). Lower values indicate
            more stable amplitude control
        shimmer_d_b (str | Unset): Period-to-period amplitude variation in logarithmic scale (dB). Lower values indicate
            better amplitude stability
        ltas_slope (float | Unset): Spectral slope between 0-1kHz and 1-10kHz frequency ranges (dB/octave). More
            negative values indicate steeper spectral roll-off
        ltas_tilt (str | Unset): Spectral tilt of trend line through long-term average spectrum 1-10kHz (dB/octave).
            Indicates overall spectral balance and voice quality
    """

    avqi: float | Unset = UNSET
    cpps: str | Unset = UNSET
    hnr: str | Unset = UNSET
    shimmer: float | Unset = UNSET
    shimmer_d_b: str | Unset = UNSET
    ltas_slope: float | Unset = UNSET
    ltas_tilt: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avqi = self.avqi

        cpps = self.cpps

        hnr = self.hnr

        shimmer = self.shimmer

        shimmer_d_b = self.shimmer_d_b

        ltas_slope = self.ltas_slope

        ltas_tilt = self.ltas_tilt

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avqi is not UNSET:
            field_dict["AVQI"] = avqi
        if cpps is not UNSET:
            field_dict["CPPS"] = cpps
        if hnr is not UNSET:
            field_dict["HNR"] = hnr
        if shimmer is not UNSET:
            field_dict["Shimmer"] = shimmer
        if shimmer_d_b is not UNSET:
            field_dict["Shimmer_dB"] = shimmer_d_b
        if ltas_slope is not UNSET:
            field_dict["LTAS_slope"] = ltas_slope
        if ltas_tilt is not UNSET:
            field_dict["LTAS_tilt"] = ltas_tilt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avqi = d.pop("AVQI", UNSET)

        cpps = d.pop("CPPS", UNSET)

        hnr = d.pop("HNR", UNSET)

        shimmer = d.pop("Shimmer", UNSET)

        shimmer_d_b = d.pop("Shimmer_dB", UNSET)

        ltas_slope = d.pop("LTAS_slope", UNSET)

        ltas_tilt = d.pop("LTAS_tilt", UNSET)

        get_calculate_avqi_response_200 = cls(
            avqi=avqi,
            cpps=cpps,
            hnr=hnr,
            shimmer=shimmer,
            shimmer_d_b=shimmer_d_b,
            ltas_slope=ltas_slope,
            ltas_tilt=ltas_tilt,
        )

        get_calculate_avqi_response_200.additional_properties = d
        return get_calculate_avqi_response_200

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
