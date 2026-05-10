from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_classify_estonian_vowel_body import PostClassifyEstonianVowelBody
from ...models.post_classify_estonian_vowel_response_200 import PostClassifyEstonianVowelResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: PostClassifyEstonianVowelBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/classify-estonian-vowel",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostClassifyEstonianVowelResponse200 | None:
    if response.status_code == 200:
        response_200 = PostClassifyEstonianVowelResponse200.from_dict(response.json())

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
) -> Response[Any | PostClassifyEstonianVowelResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostClassifyEstonianVowelBody,
) -> Response[Any | PostClassifyEstonianVowelResponse200]:
    """Synchronous Estonian vowel classifier. Submit a fileId, receive the predicted vowel and confidence
    in the response.

    Args:
        body (PostClassifyEstonianVowelBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostClassifyEstonianVowelResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: PostClassifyEstonianVowelBody,
) -> Any | PostClassifyEstonianVowelResponse200 | None:
    """Synchronous Estonian vowel classifier. Submit a fileId, receive the predicted vowel and confidence
    in the response.

    Args:
        body (PostClassifyEstonianVowelBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostClassifyEstonianVowelResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostClassifyEstonianVowelBody,
) -> Response[Any | PostClassifyEstonianVowelResponse200]:
    """Synchronous Estonian vowel classifier. Submit a fileId, receive the predicted vowel and confidence
    in the response.

    Args:
        body (PostClassifyEstonianVowelBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostClassifyEstonianVowelResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostClassifyEstonianVowelBody,
) -> Any | PostClassifyEstonianVowelResponse200 | None:
    """Synchronous Estonian vowel classifier. Submit a fileId, receive the predicted vowel and confidence
    in the response.

    Args:
        body (PostClassifyEstonianVowelBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostClassifyEstonianVowelResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
