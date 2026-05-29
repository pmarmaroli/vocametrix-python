from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_calculate_sz_ratio_response_200 import GetCalculateSzRatioResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    s_file_id: str,
    z_file_id: str,
    patient_age: float,
    gender: str,
    clinical_context: str | Unset = UNSET,
    silence_threshold: float | Unset = UNSET,
    min_voiced_duration: float | Unset = UNSET,
    min_voiceless_duration: float | Unset = UNSET,
    edge_padding: float | Unset = UNSET,
    max_recording_duration: float | Unset = UNSET,
    chunk_duration: float | Unset = UNSET,
    version: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["sFileId"] = s_file_id

    params["zFileId"] = z_file_id

    params["patientAge"] = patient_age

    params["gender"] = gender

    params["clinicalContext"] = clinical_context

    params["silenceThreshold"] = silence_threshold

    params["minVoicedDuration"] = min_voiced_duration

    params["minVoicelessDuration"] = min_voiceless_duration

    params["edgePadding"] = edge_padding

    params["maxRecordingDuration"] = max_recording_duration

    params["chunkDuration"] = chunk_duration

    params["version"] = version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/calculate-sz-ratio",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetCalculateSzRatioResponse200 | None:
    if response.status_code == 200:
        response_200 = GetCalculateSzRatioResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetCalculateSzRatioResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    s_file_id: str,
    z_file_id: str,
    patient_age: float,
    gender: str,
    clinical_context: str | Unset = UNSET,
    silence_threshold: float | Unset = UNSET,
    min_voiced_duration: float | Unset = UNSET,
    min_voiceless_duration: float | Unset = UNSET,
    edge_padding: float | Unset = UNSET,
    max_recording_duration: float | Unset = UNSET,
    chunk_duration: float | Unset = UNSET,
    version: str | Unset = UNSET,
) -> Response[Any | GetCalculateSzRatioResponse200]:
    """Calculate S/Z ratio with age-specific interpretation and quality assessment

    Args:
        s_file_id (str):
        z_file_id (str):
        patient_age (float):
        gender (str):
        clinical_context (str | Unset):
        silence_threshold (float | Unset):
        min_voiced_duration (float | Unset):
        min_voiceless_duration (float | Unset):
        edge_padding (float | Unset):
        max_recording_duration (float | Unset):
        chunk_duration (float | Unset):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetCalculateSzRatioResponse200]
    """

    kwargs = _get_kwargs(
        s_file_id=s_file_id,
        z_file_id=z_file_id,
        patient_age=patient_age,
        gender=gender,
        clinical_context=clinical_context,
        silence_threshold=silence_threshold,
        min_voiced_duration=min_voiced_duration,
        min_voiceless_duration=min_voiceless_duration,
        edge_padding=edge_padding,
        max_recording_duration=max_recording_duration,
        chunk_duration=chunk_duration,
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    s_file_id: str,
    z_file_id: str,
    patient_age: float,
    gender: str,
    clinical_context: str | Unset = UNSET,
    silence_threshold: float | Unset = UNSET,
    min_voiced_duration: float | Unset = UNSET,
    min_voiceless_duration: float | Unset = UNSET,
    edge_padding: float | Unset = UNSET,
    max_recording_duration: float | Unset = UNSET,
    chunk_duration: float | Unset = UNSET,
    version: str | Unset = UNSET,
) -> Any | GetCalculateSzRatioResponse200 | None:
    """Calculate S/Z ratio with age-specific interpretation and quality assessment

    Args:
        s_file_id (str):
        z_file_id (str):
        patient_age (float):
        gender (str):
        clinical_context (str | Unset):
        silence_threshold (float | Unset):
        min_voiced_duration (float | Unset):
        min_voiceless_duration (float | Unset):
        edge_padding (float | Unset):
        max_recording_duration (float | Unset):
        chunk_duration (float | Unset):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetCalculateSzRatioResponse200
    """

    return sync_detailed(
        client=client,
        s_file_id=s_file_id,
        z_file_id=z_file_id,
        patient_age=patient_age,
        gender=gender,
        clinical_context=clinical_context,
        silence_threshold=silence_threshold,
        min_voiced_duration=min_voiced_duration,
        min_voiceless_duration=min_voiceless_duration,
        edge_padding=edge_padding,
        max_recording_duration=max_recording_duration,
        chunk_duration=chunk_duration,
        version=version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    s_file_id: str,
    z_file_id: str,
    patient_age: float,
    gender: str,
    clinical_context: str | Unset = UNSET,
    silence_threshold: float | Unset = UNSET,
    min_voiced_duration: float | Unset = UNSET,
    min_voiceless_duration: float | Unset = UNSET,
    edge_padding: float | Unset = UNSET,
    max_recording_duration: float | Unset = UNSET,
    chunk_duration: float | Unset = UNSET,
    version: str | Unset = UNSET,
) -> Response[Any | GetCalculateSzRatioResponse200]:
    """Calculate S/Z ratio with age-specific interpretation and quality assessment

    Args:
        s_file_id (str):
        z_file_id (str):
        patient_age (float):
        gender (str):
        clinical_context (str | Unset):
        silence_threshold (float | Unset):
        min_voiced_duration (float | Unset):
        min_voiceless_duration (float | Unset):
        edge_padding (float | Unset):
        max_recording_duration (float | Unset):
        chunk_duration (float | Unset):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetCalculateSzRatioResponse200]
    """

    kwargs = _get_kwargs(
        s_file_id=s_file_id,
        z_file_id=z_file_id,
        patient_age=patient_age,
        gender=gender,
        clinical_context=clinical_context,
        silence_threshold=silence_threshold,
        min_voiced_duration=min_voiced_duration,
        min_voiceless_duration=min_voiceless_duration,
        edge_padding=edge_padding,
        max_recording_duration=max_recording_duration,
        chunk_duration=chunk_duration,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    s_file_id: str,
    z_file_id: str,
    patient_age: float,
    gender: str,
    clinical_context: str | Unset = UNSET,
    silence_threshold: float | Unset = UNSET,
    min_voiced_duration: float | Unset = UNSET,
    min_voiceless_duration: float | Unset = UNSET,
    edge_padding: float | Unset = UNSET,
    max_recording_duration: float | Unset = UNSET,
    chunk_duration: float | Unset = UNSET,
    version: str | Unset = UNSET,
) -> Any | GetCalculateSzRatioResponse200 | None:
    """Calculate S/Z ratio with age-specific interpretation and quality assessment

    Args:
        s_file_id (str):
        z_file_id (str):
        patient_age (float):
        gender (str):
        clinical_context (str | Unset):
        silence_threshold (float | Unset):
        min_voiced_duration (float | Unset):
        min_voiceless_duration (float | Unset):
        edge_padding (float | Unset):
        max_recording_duration (float | Unset):
        chunk_duration (float | Unset):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetCalculateSzRatioResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            s_file_id=s_file_id,
            z_file_id=z_file_id,
            patient_age=patient_age,
            gender=gender,
            clinical_context=clinical_context,
            silence_threshold=silence_threshold,
            min_voiced_duration=min_voiced_duration,
            min_voiceless_duration=min_voiceless_duration,
            edge_padding=edge_padding,
            max_recording_duration=max_recording_duration,
            chunk_duration=chunk_duration,
            version=version,
        )
    ).parsed
