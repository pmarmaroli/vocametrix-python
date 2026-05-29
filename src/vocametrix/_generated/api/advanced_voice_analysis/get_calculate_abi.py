from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_calculate_abi_response_200 import GetCalculateAbiResponse200
from ...types import UNSET, Response


def _get_kwargs(
    *,
    cs_file_id: str,
    sv_file_id: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["csFileId"] = cs_file_id

    params["svFileId"] = sv_file_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/calculate-abi",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetCalculateAbiResponse200 | None:
    if response.status_code == 200:
        response_200 = GetCalculateAbiResponse200.from_dict(response.json())

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
) -> Response[Any | GetCalculateAbiResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    cs_file_id: str,
    sv_file_id: str,
) -> Response[Any | GetCalculateAbiResponse200]:
    """Calculate the Acoustic Breathiness Index (ABI) from a connected speech recording and a sustained
    vowel recording. The…

    Args:
        cs_file_id (str):
        sv_file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetCalculateAbiResponse200]
    """

    kwargs = _get_kwargs(
        cs_file_id=cs_file_id,
        sv_file_id=sv_file_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    cs_file_id: str,
    sv_file_id: str,
) -> Any | GetCalculateAbiResponse200 | None:
    """Calculate the Acoustic Breathiness Index (ABI) from a connected speech recording and a sustained
    vowel recording. The…

    Args:
        cs_file_id (str):
        sv_file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetCalculateAbiResponse200
    """

    return sync_detailed(
        client=client,
        cs_file_id=cs_file_id,
        sv_file_id=sv_file_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cs_file_id: str,
    sv_file_id: str,
) -> Response[Any | GetCalculateAbiResponse200]:
    """Calculate the Acoustic Breathiness Index (ABI) from a connected speech recording and a sustained
    vowel recording. The…

    Args:
        cs_file_id (str):
        sv_file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetCalculateAbiResponse200]
    """

    kwargs = _get_kwargs(
        cs_file_id=cs_file_id,
        sv_file_id=sv_file_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    cs_file_id: str,
    sv_file_id: str,
) -> Any | GetCalculateAbiResponse200 | None:
    """Calculate the Acoustic Breathiness Index (ABI) from a connected speech recording and a sustained
    vowel recording. The…

    Args:
        cs_file_id (str):
        sv_file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetCalculateAbiResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            cs_file_id=cs_file_id,
            sv_file_id=sv_file_id,
        )
    ).parsed
