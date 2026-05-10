from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_therapy_approve_by_session_id_body import PostTherapyApproveBySessionIdBody
from ...models.post_therapy_approve_by_session_id_response_200 import (
    PostTherapyApproveBySessionIdResponse200,
)
from ...types import Response


def _get_kwargs(
    session_id: str,
    *,
    body: PostTherapyApproveBySessionIdBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/therapy-approve/{session_id}".format(
            session_id=quote(str(session_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostTherapyApproveBySessionIdResponse200 | None:
    if response.status_code == 200:
        response_200 = PostTherapyApproveBySessionIdResponse200.from_dict(response.json())

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
) -> Response[Any | PostTherapyApproveBySessionIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient,
    body: PostTherapyApproveBySessionIdBody,
) -> Response[Any | PostTherapyApproveBySessionIdResponse200]:
    r"""Approve, modify, or reject a generated therapy plan. The action determines the next step:
    \"approve\" locks the plan as…

    Args:
        session_id (str):
        body (PostTherapyApproveBySessionIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostTherapyApproveBySessionIdResponse200]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    session_id: str,
    *,
    client: AuthenticatedClient,
    body: PostTherapyApproveBySessionIdBody,
) -> Any | PostTherapyApproveBySessionIdResponse200 | None:
    r"""Approve, modify, or reject a generated therapy plan. The action determines the next step:
    \"approve\" locks the plan as…

    Args:
        session_id (str):
        body (PostTherapyApproveBySessionIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostTherapyApproveBySessionIdResponse200
    """

    return sync_detailed(
        session_id=session_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient,
    body: PostTherapyApproveBySessionIdBody,
) -> Response[Any | PostTherapyApproveBySessionIdResponse200]:
    r"""Approve, modify, or reject a generated therapy plan. The action determines the next step:
    \"approve\" locks the plan as…

    Args:
        session_id (str):
        body (PostTherapyApproveBySessionIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostTherapyApproveBySessionIdResponse200]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    session_id: str,
    *,
    client: AuthenticatedClient,
    body: PostTherapyApproveBySessionIdBody,
) -> Any | PostTherapyApproveBySessionIdResponse200 | None:
    r"""Approve, modify, or reject a generated therapy plan. The action determines the next step:
    \"approve\" locks the plan as…

    Args:
        session_id (str):
        body (PostTherapyApproveBySessionIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostTherapyApproveBySessionIdResponse200
    """

    return (
        await asyncio_detailed(
            session_id=session_id,
            client=client,
            body=body,
        )
    ).parsed
