from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_calculate_voice_dynamics_response_200 import GetCalculateVoiceDynamicsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    sv_file_id: str,
    age: int,
    gender: str,
    time_step: float | Unset = UNSET,
    min_pitch: float | Unset = UNSET,
    subtract_mean: str | Unset = UNSET,
    window_length: float | Unset = UNSET,
    fatigue_threshold: float | Unset = UNSET,
    mild_fatigue_threshold: str | Unset = UNSET,
    monotonicity_cv: str | Unset = UNSET,
    monotonicity_range: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["svFileId"] = sv_file_id

    params["age"] = age

    params["gender"] = gender

    params["timeStep"] = time_step

    params["minPitch"] = min_pitch

    params["subtractMean"] = subtract_mean

    params["windowLength"] = window_length

    params["fatigueThreshold"] = fatigue_threshold

    params["mildFatigueThreshold"] = mild_fatigue_threshold

    params["monotonicityCV"] = monotonicity_cv

    params["monotonicityRange"] = monotonicity_range

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/calculate-voice-dynamics",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetCalculateVoiceDynamicsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetCalculateVoiceDynamicsResponse200.from_dict(response.json())

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
) -> Response[Any | GetCalculateVoiceDynamicsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    sv_file_id: str,
    age: int,
    gender: str,
    time_step: float | Unset = UNSET,
    min_pitch: float | Unset = UNSET,
    subtract_mean: str | Unset = UNSET,
    window_length: float | Unset = UNSET,
    fatigue_threshold: float | Unset = UNSET,
    mild_fatigue_threshold: str | Unset = UNSET,
    monotonicity_cv: str | Unset = UNSET,
    monotonicity_range: str | Unset = UNSET,
) -> Response[Any | GetCalculateVoiceDynamicsResponse200]:
    """Compute intensity dynamics, pitch-intensity correlation, and
    projection/stability/effort/control/monotonicity scores …

    Args:
        sv_file_id (str):
        age (int):
        gender (str):
        time_step (float | Unset):
        min_pitch (float | Unset):
        subtract_mean (str | Unset):
        window_length (float | Unset):
        fatigue_threshold (float | Unset):
        mild_fatigue_threshold (str | Unset):
        monotonicity_cv (str | Unset):
        monotonicity_range (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetCalculateVoiceDynamicsResponse200]
    """

    kwargs = _get_kwargs(
        sv_file_id=sv_file_id,
        age=age,
        gender=gender,
        time_step=time_step,
        min_pitch=min_pitch,
        subtract_mean=subtract_mean,
        window_length=window_length,
        fatigue_threshold=fatigue_threshold,
        mild_fatigue_threshold=mild_fatigue_threshold,
        monotonicity_cv=monotonicity_cv,
        monotonicity_range=monotonicity_range,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    sv_file_id: str,
    age: int,
    gender: str,
    time_step: float | Unset = UNSET,
    min_pitch: float | Unset = UNSET,
    subtract_mean: str | Unset = UNSET,
    window_length: float | Unset = UNSET,
    fatigue_threshold: float | Unset = UNSET,
    mild_fatigue_threshold: str | Unset = UNSET,
    monotonicity_cv: str | Unset = UNSET,
    monotonicity_range: str | Unset = UNSET,
) -> Any | GetCalculateVoiceDynamicsResponse200 | None:
    """Compute intensity dynamics, pitch-intensity correlation, and
    projection/stability/effort/control/monotonicity scores …

    Args:
        sv_file_id (str):
        age (int):
        gender (str):
        time_step (float | Unset):
        min_pitch (float | Unset):
        subtract_mean (str | Unset):
        window_length (float | Unset):
        fatigue_threshold (float | Unset):
        mild_fatigue_threshold (str | Unset):
        monotonicity_cv (str | Unset):
        monotonicity_range (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetCalculateVoiceDynamicsResponse200
    """

    return sync_detailed(
        client=client,
        sv_file_id=sv_file_id,
        age=age,
        gender=gender,
        time_step=time_step,
        min_pitch=min_pitch,
        subtract_mean=subtract_mean,
        window_length=window_length,
        fatigue_threshold=fatigue_threshold,
        mild_fatigue_threshold=mild_fatigue_threshold,
        monotonicity_cv=monotonicity_cv,
        monotonicity_range=monotonicity_range,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    sv_file_id: str,
    age: int,
    gender: str,
    time_step: float | Unset = UNSET,
    min_pitch: float | Unset = UNSET,
    subtract_mean: str | Unset = UNSET,
    window_length: float | Unset = UNSET,
    fatigue_threshold: float | Unset = UNSET,
    mild_fatigue_threshold: str | Unset = UNSET,
    monotonicity_cv: str | Unset = UNSET,
    monotonicity_range: str | Unset = UNSET,
) -> Response[Any | GetCalculateVoiceDynamicsResponse200]:
    """Compute intensity dynamics, pitch-intensity correlation, and
    projection/stability/effort/control/monotonicity scores …

    Args:
        sv_file_id (str):
        age (int):
        gender (str):
        time_step (float | Unset):
        min_pitch (float | Unset):
        subtract_mean (str | Unset):
        window_length (float | Unset):
        fatigue_threshold (float | Unset):
        mild_fatigue_threshold (str | Unset):
        monotonicity_cv (str | Unset):
        monotonicity_range (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetCalculateVoiceDynamicsResponse200]
    """

    kwargs = _get_kwargs(
        sv_file_id=sv_file_id,
        age=age,
        gender=gender,
        time_step=time_step,
        min_pitch=min_pitch,
        subtract_mean=subtract_mean,
        window_length=window_length,
        fatigue_threshold=fatigue_threshold,
        mild_fatigue_threshold=mild_fatigue_threshold,
        monotonicity_cv=monotonicity_cv,
        monotonicity_range=monotonicity_range,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    sv_file_id: str,
    age: int,
    gender: str,
    time_step: float | Unset = UNSET,
    min_pitch: float | Unset = UNSET,
    subtract_mean: str | Unset = UNSET,
    window_length: float | Unset = UNSET,
    fatigue_threshold: float | Unset = UNSET,
    mild_fatigue_threshold: str | Unset = UNSET,
    monotonicity_cv: str | Unset = UNSET,
    monotonicity_range: str | Unset = UNSET,
) -> Any | GetCalculateVoiceDynamicsResponse200 | None:
    """Compute intensity dynamics, pitch-intensity correlation, and
    projection/stability/effort/control/monotonicity scores …

    Args:
        sv_file_id (str):
        age (int):
        gender (str):
        time_step (float | Unset):
        min_pitch (float | Unset):
        subtract_mean (str | Unset):
        window_length (float | Unset):
        fatigue_threshold (float | Unset):
        mild_fatigue_threshold (str | Unset):
        monotonicity_cv (str | Unset):
        monotonicity_range (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetCalculateVoiceDynamicsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            sv_file_id=sv_file_id,
            age=age,
            gender=gender,
            time_step=time_step,
            min_pitch=min_pitch,
            subtract_mean=subtract_mean,
            window_length=window_length,
            fatigue_threshold=fatigue_threshold,
            mild_fatigue_threshold=mild_fatigue_threshold,
            monotonicity_cv=monotonicity_cv,
            monotonicity_range=monotonicity_range,
        )
    ).parsed
