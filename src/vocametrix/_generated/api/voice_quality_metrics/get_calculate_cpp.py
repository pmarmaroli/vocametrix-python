from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_calculate_cpp_response_200 import GetCalculateCppResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    sv_file_id: str,
    version: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["svFileId"] = sv_file_id

    params["version"] = version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/calculate-cpp",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetCalculateCppResponse200 | None:
    if response.status_code == 200:
        response_200 = GetCalculateCppResponse200.from_dict(response.json())

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
) -> Response[Any | GetCalculateCppResponse200]:
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
    version: str | Unset = UNSET,
) -> Response[Any | GetCalculateCppResponse200]:
    """Calculate CPP and complementary voice measures from sustained vowel recording

    Args:
        sv_file_id (str):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetCalculateCppResponse200]
    """

    kwargs = _get_kwargs(
        sv_file_id=sv_file_id,
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    sv_file_id: str,
    version: str | Unset = UNSET,
) -> Any | GetCalculateCppResponse200 | None:
    """Calculate CPP and complementary voice measures from sustained vowel recording

    Args:
        sv_file_id (str):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetCalculateCppResponse200
    """

    return sync_detailed(
        client=client,
        sv_file_id=sv_file_id,
        version=version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    sv_file_id: str,
    version: str | Unset = UNSET,
) -> Response[Any | GetCalculateCppResponse200]:
    """Calculate CPP and complementary voice measures from sustained vowel recording

    Args:
        sv_file_id (str):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetCalculateCppResponse200]
    """

    kwargs = _get_kwargs(
        sv_file_id=sv_file_id,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    sv_file_id: str,
    version: str | Unset = UNSET,
) -> Any | GetCalculateCppResponse200 | None:
    """Calculate CPP and complementary voice measures from sustained vowel recording

    Args:
        sv_file_id (str):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetCalculateCppResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            sv_file_id=sv_file_id,
            version=version,
        )
    ).parsed
