"""Authenticated HTTP helper for Loyalty v2 admin paths not in the published Python SDK."""

from __future__ import annotations

import json
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Mapping, Optional

import spec_utils


class LoyaltyV2HttpError(Exception):
    def __init__(self, status: int, message: str, body: Any = None):
        super().__init__(message)
        self.status = status
        self.body = body


def _base_url() -> str:
    base = (spec_utils.HOST or "https://api.voucherify.io").strip().rstrip("/")
    if base.lower().endswith("/v1"):
        base = base[:-3].rstrip("/")
    return base


def _headers() -> dict[str, str]:
    return {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "X-App-Id": spec_utils.X_APP_ID or "",
        "X-App-Token": spec_utils.X_APP_TOKEN or "",
    }


def _build_url(path: str, query: Optional[Mapping[str, Any]] = None) -> str:
    normalized = path if path.startswith("/") else f"/{path}"
    url = f"{_base_url()}{normalized}"
    if not query:
        return url
    params = {
        key: value
        for key, value in query.items()
        if value is not None
    }
    if not params:
        return url
    return f"{url}?{urllib.parse.urlencode(params)}"


def _parse_body(text: str) -> Any:
    if text is None or text.strip() == "":
        return None
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return text


def _excerpt(data: Any, raw: str, limit: int = 500) -> str:
    if data is None:
        return (raw or "")[:limit]
    if isinstance(data, str):
        return data[:limit]
    try:
        return json.dumps(data)[:limit]
    except TypeError:
        return str(data)[:limit]


def request(
    method: str,
    path: str,
    body: Optional[Mapping[str, Any]] = None,
    query: Optional[Mapping[str, Any]] = None,
) -> Any:
    """Send an authenticated JSON request. Returns parsed JSON (dict/list) or None."""
    upper = method.upper()
    url = _build_url(path, query)
    data = None
    if upper not in ("GET", "DELETE"):
        payload = body if body is not None else {}
        data = json.dumps(payload).encode("utf-8")

    req = urllib.request.Request(url, data=data, headers=_headers(), method=upper)
    try:
        with urllib.request.urlopen(req, timeout=120) as response:
            raw = response.read().decode("utf-8")
            status = response.getcode()
            parsed = _parse_body(raw)
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        parsed = _parse_body(raw)
        raise LoyaltyV2HttpError(
            exc.code,
            f"{upper} {path}: {_excerpt(parsed, raw)}",
            parsed,
        ) from None
    except urllib.error.URLError as exc:
        detail = getattr(exc, "reason", None) or str(exc)
        raise LoyaltyV2HttpError(0, f"HTTP transport failed: {detail}", None) from None

    if status < 200 or status >= 300:
        raise LoyaltyV2HttpError(
            status,
            f"{upper} {path}: {_excerpt(parsed, raw)}",
            parsed,
        )
    return parsed


def create_program(body: Mapping[str, Any]) -> Any:
    return request("POST", "/v2/loyalties/programs", body)


def activate_program(program_id: str) -> Any:
    return request("POST", f"/v2/loyalties/programs/{program_id}/activate")


def deactivate_program(program_id: str) -> Any:
    return request("POST", f"/v2/loyalties/programs/{program_id}/deactivate")


def delete_program(program_id: str) -> Any:
    return request("DELETE", f"/v2/loyalties/programs/{program_id}")


def create_card_definition(body: Mapping[str, Any]) -> Any:
    return request("POST", "/v2/loyalties/card-definitions", body)


def activate_card_definition(card_definition_id: str) -> Any:
    return request(
        "POST", f"/v2/loyalties/card-definitions/{card_definition_id}/activate"
    )


def delete_card_definition(card_definition_id: str) -> Any:
    return request("DELETE", f"/v2/loyalties/card-definitions/{card_definition_id}")


def create_earning_rule(body: Mapping[str, Any]) -> Any:
    return request("POST", "/v2/loyalties/earning-rules", body)


def activate_earning_rule(earning_rule_id: str) -> Any:
    return request("POST", f"/v2/loyalties/earning-rules/{earning_rule_id}/activate")


def deactivate_earning_rule(earning_rule_id: str) -> Any:
    return request("POST", f"/v2/loyalties/earning-rules/{earning_rule_id}/deactivate")


def delete_earning_rule(earning_rule_id: str) -> Any:
    return request("DELETE", f"/v2/loyalties/earning-rules/{earning_rule_id}")


def create_reward(body: Mapping[str, Any]) -> Any:
    return request("POST", "/v2/loyalties/rewards", body)


def activate_reward(reward_id: str) -> Any:
    return request("POST", f"/v2/loyalties/rewards/{reward_id}/activate")


def deactivate_reward(reward_id: str) -> Any:
    return request("POST", f"/v2/loyalties/rewards/{reward_id}/deactivate")


def delete_reward(reward_id: str) -> Any:
    return request("DELETE", f"/v2/loyalties/rewards/{reward_id}")


def batch_assign_card_definitions(program_id: str, body: Mapping[str, Any]) -> Any:
    return request(
        "POST",
        f"/v2/loyalties/programs/{program_id}/card-definitions/batch",
        body,
    )


def batch_assign_earning_rules(program_id: str, body: Mapping[str, Any]) -> Any:
    return request(
        "POST",
        f"/v2/loyalties/programs/{program_id}/earning-rules/batch",
        body,
    )


def batch_assign_rewards(program_id: str, body: Mapping[str, Any]) -> Any:
    return request(
        "POST",
        f"/v2/loyalties/programs/{program_id}/rewards/batch",
        body,
    )


def resource_id(payload: Any) -> Optional[str]:
    if isinstance(payload, dict):
        value = payload.get("id")
        if isinstance(value, str):
            return value
    return None
