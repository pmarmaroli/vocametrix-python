from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCalculateDsiResponse200")


@_attrs_define
class GetCalculateDsiResponse200:
    """
    Attributes:
        dsi (float | Unset): number - Dysphonia Severity Index score (approx range -5 to +5). Example: 1.85
        jitter (float | Unset): number - Period Perturbation Quotient (PPQ5) as a percentage or fraction (parsed as
            number). Example: 0.45
        mpt (float | Unset): number - Maximum Phonation Time in seconds (echoes input MPT or measured). Example: 15.2
        minlevel (float | Unset): number - Minimum intensity level in dB SPL. Example: 45.5
        maxf0 (float | Unset): number - Maximum fundamental frequency in Hz. Example: 440.0
        patient_age (float | Unset): number - Patient age (integer). Example: 35
        patient_gender (str | Unset): string - Human-readable gender label (e.g. "Female")
        age_group (str | Unset): string - Age group label used for interpretation (e.g. "Young adult / Middle-aged")
        presbylaryngis_risk (float | Unset): number - Age-related voice change risk flag (0 or 1). Example: 0
        expected_f0_range (float | Unset): string - Gender-specific expected F0 range. Example: "150-350 Hz"
    """

    dsi: float | Unset = UNSET
    jitter: float | Unset = UNSET
    mpt: float | Unset = UNSET
    minlevel: float | Unset = UNSET
    maxf0: float | Unset = UNSET
    patient_age: float | Unset = UNSET
    patient_gender: str | Unset = UNSET
    age_group: str | Unset = UNSET
    presbylaryngis_risk: float | Unset = UNSET
    expected_f0_range: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dsi = self.dsi

        jitter = self.jitter

        mpt = self.mpt

        minlevel = self.minlevel

        maxf0 = self.maxf0

        patient_age = self.patient_age

        patient_gender = self.patient_gender

        age_group = self.age_group

        presbylaryngis_risk = self.presbylaryngis_risk

        expected_f0_range = self.expected_f0_range

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dsi is not UNSET:
            field_dict["DSI"] = dsi
        if jitter is not UNSET:
            field_dict["JITTER"] = jitter
        if mpt is not UNSET:
            field_dict["MPT"] = mpt
        if minlevel is not UNSET:
            field_dict["MINLEVEL"] = minlevel
        if maxf0 is not UNSET:
            field_dict["MAXF0"] = maxf0
        if patient_age is not UNSET:
            field_dict["PATIENT_AGE"] = patient_age
        if patient_gender is not UNSET:
            field_dict["PATIENT_GENDER"] = patient_gender
        if age_group is not UNSET:
            field_dict["AGE_GROUP"] = age_group
        if presbylaryngis_risk is not UNSET:
            field_dict["PRESBYLARYNGIS_RISK"] = presbylaryngis_risk
        if expected_f0_range is not UNSET:
            field_dict["EXPECTED_F0_RANGE"] = expected_f0_range

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dsi = d.pop("DSI", UNSET)

        jitter = d.pop("JITTER", UNSET)

        mpt = d.pop("MPT", UNSET)

        minlevel = d.pop("MINLEVEL", UNSET)

        maxf0 = d.pop("MAXF0", UNSET)

        patient_age = d.pop("PATIENT_AGE", UNSET)

        patient_gender = d.pop("PATIENT_GENDER", UNSET)

        age_group = d.pop("AGE_GROUP", UNSET)

        presbylaryngis_risk = d.pop("PRESBYLARYNGIS_RISK", UNSET)

        expected_f0_range = d.pop("EXPECTED_F0_RANGE", UNSET)

        get_calculate_dsi_response_200 = cls(
            dsi=dsi,
            jitter=jitter,
            mpt=mpt,
            minlevel=minlevel,
            maxf0=maxf0,
            patient_age=patient_age,
            patient_gender=patient_gender,
            age_group=age_group,
            presbylaryngis_risk=presbylaryngis_risk,
            expected_f0_range=expected_f0_range,
        )

        get_calculate_dsi_response_200.additional_properties = d
        return get_calculate_dsi_response_200

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
