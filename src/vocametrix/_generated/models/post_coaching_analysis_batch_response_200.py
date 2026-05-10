from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostCoachingAnalysisBatchResponse200")


@_attrs_define
class PostCoachingAnalysisBatchResponse200:
    """
    Attributes:
        job_id (str | Unset): String — opaque job identifier (format: "ca_batch_<uuid>"). Pass this to /api/coaching-
            analysis/batch/:job_id to poll.
        status (str | Unset): "queued" — the initial state. The job transitions to "running" / "complete" / "failed" as
            it progresses.
        n_files (float | Unset): Number of manifest rows the server will process.
        poll_url (str | Unset): Convenience URL to poll the job state.
        created_at (datetime.datetime | Unset): ISO 8601 timestamp.
    """

    job_id: str | Unset = UNSET
    status: str | Unset = UNSET
    n_files: float | Unset = UNSET
    poll_url: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_id = self.job_id

        status = self.status

        n_files = self.n_files

        poll_url = self.poll_url

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if status is not UNSET:
            field_dict["status"] = status
        if n_files is not UNSET:
            field_dict["n_files"] = n_files
        if poll_url is not UNSET:
            field_dict["poll_url"] = poll_url
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        job_id = d.pop("job_id", UNSET)

        status = d.pop("status", UNSET)

        n_files = d.pop("n_files", UNSET)

        poll_url = d.pop("poll_url", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        post_coaching_analysis_batch_response_200 = cls(
            job_id=job_id,
            status=status,
            n_files=n_files,
            poll_url=poll_url,
            created_at=created_at,
        )

        post_coaching_analysis_batch_response_200.additional_properties = d
        return post_coaching_analysis_batch_response_200

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
