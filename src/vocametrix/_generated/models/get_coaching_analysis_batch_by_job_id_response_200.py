from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_coaching_analysis_batch_by_job_id_response_200_downloads import (
        GetCoachingAnalysisBatchByJobIdResponse200Downloads,
    )
    from ..models.get_coaching_analysis_batch_by_job_id_response_200_results_item import (
        GetCoachingAnalysisBatchByJobIdResponse200ResultsItem,
    )


T = TypeVar("T", bound="GetCoachingAnalysisBatchByJobIdResponse200")


@_attrs_define
class GetCoachingAnalysisBatchByJobIdResponse200:
    """
    Attributes:
        job_id (str | Unset): Echo of the job identifier.
        status (str | Unset): "queued" | "running" | "complete" | "failed".
        created_at (datetime.datetime | Unset): ISO 8601 timestamp.
        updated_at (datetime.datetime | Unset): ISO 8601 timestamp of the last state change.
        n_files (int | Unset): Total number of manifest rows.
        n_processed (int | Unset): How many rows have been processed (succeeded or failed).
        n_succeeded (int | Unset): How many rows succeeded.
        n_failed (int | Unset): How many rows failed.
        results (list[GetCoachingAnalysisBatchByJobIdResponse200ResultsItem] | Unset): Array of per-file orchestrator
            outputs (same shape as POST /api/coaching-analysis), in manifest order. Populated incrementally as the batch
            progresses.
        downloads (GetCoachingAnalysisBatchByJobIdResponse200Downloads | Unset): Object with download URLs once the
            batch is complete (e.g., dataset.csv). Null while running.
        error (str | Unset): String describing why the job failed, or null.
        pipeline_version (str | Unset): Echo of the orchestrator pipeline version.
    """

    job_id: str | Unset = UNSET
    status: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    n_files: int | Unset = UNSET
    n_processed: int | Unset = UNSET
    n_succeeded: int | Unset = UNSET
    n_failed: int | Unset = UNSET
    results: list[GetCoachingAnalysisBatchByJobIdResponse200ResultsItem] | Unset = UNSET
    downloads: GetCoachingAnalysisBatchByJobIdResponse200Downloads | Unset = UNSET
    error: str | Unset = UNSET
    pipeline_version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_id = self.job_id

        status = self.status

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        n_files = self.n_files

        n_processed = self.n_processed

        n_succeeded = self.n_succeeded

        n_failed = self.n_failed

        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)

        downloads: dict[str, Any] | Unset = UNSET
        if not isinstance(self.downloads, Unset):
            downloads = self.downloads.to_dict()

        error = self.error

        pipeline_version = self.pipeline_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if status is not UNSET:
            field_dict["status"] = status
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if n_files is not UNSET:
            field_dict["n_files"] = n_files
        if n_processed is not UNSET:
            field_dict["n_processed"] = n_processed
        if n_succeeded is not UNSET:
            field_dict["n_succeeded"] = n_succeeded
        if n_failed is not UNSET:
            field_dict["n_failed"] = n_failed
        if results is not UNSET:
            field_dict["results"] = results
        if downloads is not UNSET:
            field_dict["downloads"] = downloads
        if error is not UNSET:
            field_dict["error"] = error
        if pipeline_version is not UNSET:
            field_dict["pipeline_version"] = pipeline_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_coaching_analysis_batch_by_job_id_response_200_downloads import (
            GetCoachingAnalysisBatchByJobIdResponse200Downloads,
        )
        from ..models.get_coaching_analysis_batch_by_job_id_response_200_results_item import (
            GetCoachingAnalysisBatchByJobIdResponse200ResultsItem,
        )

        d = dict(src_dict)
        job_id = d.pop("job_id", UNSET)

        status = d.pop("status", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        n_files = d.pop("n_files", UNSET)

        n_processed = d.pop("n_processed", UNSET)

        n_succeeded = d.pop("n_succeeded", UNSET)

        n_failed = d.pop("n_failed", UNSET)

        _results = d.pop("results", UNSET)
        results: list[GetCoachingAnalysisBatchByJobIdResponse200ResultsItem] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = GetCoachingAnalysisBatchByJobIdResponse200ResultsItem.from_dict(
                    results_item_data
                )

                results.append(results_item)

        _downloads = d.pop("downloads", UNSET)
        downloads: GetCoachingAnalysisBatchByJobIdResponse200Downloads | Unset
        if isinstance(_downloads, Unset):
            downloads = UNSET
        else:
            downloads = GetCoachingAnalysisBatchByJobIdResponse200Downloads.from_dict(_downloads)

        error = d.pop("error", UNSET)

        pipeline_version = d.pop("pipeline_version", UNSET)

        get_coaching_analysis_batch_by_job_id_response_200 = cls(
            job_id=job_id,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            n_files=n_files,
            n_processed=n_processed,
            n_succeeded=n_succeeded,
            n_failed=n_failed,
            results=results,
            downloads=downloads,
            error=error,
            pipeline_version=pipeline_version,
        )

        get_coaching_analysis_batch_by_job_id_response_200.additional_properties = d
        return get_coaching_analysis_batch_by_job_id_response_200

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
