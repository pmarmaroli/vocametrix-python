from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_gemaps_extract_response_200 import GetGemapsExtractResponse200
from ...types import UNSET, Response


def _get_kwargs(
    *,
    file_id: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["fileId"] = file_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/gemaps-extract",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetGemapsExtractResponse200 | None:
    if response.status_code == 200:
        response_200 = GetGemapsExtractResponse200.from_dict(response.json())

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
) -> Response[Any | GetGemapsExtractResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    file_id: str,
) -> Response[Any | GetGemapsExtractResponse200]:
    """Extract the full openSMILE eGeMAPSv02 feature set (88 features) from a previously uploaded audio
    file. Files longer t…

    Args:
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetGemapsExtractResponse200]
    """

    kwargs = _get_kwargs(
        file_id=file_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    file_id: str,
) -> Any | GetGemapsExtractResponse200 | None:
    """Extract the full openSMILE eGeMAPSv02 feature set (88 features) from a previously uploaded audio
    file. Files longer t…

    Args:
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetGemapsExtractResponse200
    """

    return sync_detailed(
        client=client,
        file_id=file_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    file_id: str,
) -> Response[Any | GetGemapsExtractResponse200]:
    """Extract the full openSMILE eGeMAPSv02 feature set (88 features) from a previously uploaded audio
    file. Files longer t…

    Args:
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetGemapsExtractResponse200]
    """

    kwargs = _get_kwargs(
        file_id=file_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    file_id: str,
) -> Any | GetGemapsExtractResponse200 | None:
    """Extract the full openSMILE eGeMAPSv02 feature set (88 features) from a previously uploaded audio
    file. Files longer t…

    Args:
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetGemapsExtractResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            file_id=file_id,
        )
    ).parsed
