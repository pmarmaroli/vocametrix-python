from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_calculate_prosody_similarity_response_200 import (
    GetCalculateProsodySimilarityResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    model_file_id: str,
    user_file_id: str,
    model_start_time: float | Unset = UNSET,
    user_start_time: float | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["modelFileId"] = model_file_id

    params["userFileId"] = user_file_id

    params["modelStartTime"] = model_start_time

    params["userStartTime"] = user_start_time

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/calculate-prosody-similarity",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetCalculateProsodySimilarityResponse200 | None:
    if response.status_code == 200:
        response_200 = GetCalculateProsodySimilarityResponse200.from_dict(response.json())

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
) -> Response[Any | GetCalculateProsodySimilarityResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    model_file_id: str,
    user_file_id: str,
    model_start_time: float | Unset = UNSET,
    user_start_time: float | Unset = UNSET,
) -> Response[Any | GetCalculateProsodySimilarityResponse200]:
    r"""Compare two recordings (a reference \"model\" and a learner \"user\") on prosodic dimensions.
    Returns per-dimension score…

    Args:
        model_file_id (str):
        user_file_id (str):
        model_start_time (float | Unset):
        user_start_time (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetCalculateProsodySimilarityResponse200]
    """

    kwargs = _get_kwargs(
        model_file_id=model_file_id,
        user_file_id=user_file_id,
        model_start_time=model_start_time,
        user_start_time=user_start_time,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    model_file_id: str,
    user_file_id: str,
    model_start_time: float | Unset = UNSET,
    user_start_time: float | Unset = UNSET,
) -> Any | GetCalculateProsodySimilarityResponse200 | None:
    r"""Compare two recordings (a reference \"model\" and a learner \"user\") on prosodic dimensions.
    Returns per-dimension score…

    Args:
        model_file_id (str):
        user_file_id (str):
        model_start_time (float | Unset):
        user_start_time (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetCalculateProsodySimilarityResponse200
    """

    return sync_detailed(
        client=client,
        model_file_id=model_file_id,
        user_file_id=user_file_id,
        model_start_time=model_start_time,
        user_start_time=user_start_time,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    model_file_id: str,
    user_file_id: str,
    model_start_time: float | Unset = UNSET,
    user_start_time: float | Unset = UNSET,
) -> Response[Any | GetCalculateProsodySimilarityResponse200]:
    r"""Compare two recordings (a reference \"model\" and a learner \"user\") on prosodic dimensions.
    Returns per-dimension score…

    Args:
        model_file_id (str):
        user_file_id (str):
        model_start_time (float | Unset):
        user_start_time (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetCalculateProsodySimilarityResponse200]
    """

    kwargs = _get_kwargs(
        model_file_id=model_file_id,
        user_file_id=user_file_id,
        model_start_time=model_start_time,
        user_start_time=user_start_time,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    model_file_id: str,
    user_file_id: str,
    model_start_time: float | Unset = UNSET,
    user_start_time: float | Unset = UNSET,
) -> Any | GetCalculateProsodySimilarityResponse200 | None:
    r"""Compare two recordings (a reference \"model\" and a learner \"user\") on prosodic dimensions.
    Returns per-dimension score…

    Args:
        model_file_id (str):
        user_file_id (str):
        model_start_time (float | Unset):
        user_start_time (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetCalculateProsodySimilarityResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            model_file_id=model_file_id,
            user_file_id=user_file_id,
            model_start_time=model_start_time,
            user_start_time=user_start_time,
        )
    ).parsed
