"""HTTP-only setup and teardown for Loyalty v2 e2e tests."""

from __future__ import annotations

import time
import uuid
from dataclasses import dataclass
from typing import Any, Callable, Optional

import loyalty_v2_http as http


@dataclass
class LoyaltyV2Context:
    suffix: str
    program_id: str
    card_definition_id: str
    reward_card_definition_id: str
    earning_rule_id: str
    reward_id: str
    program_name: str


def _require_id(payload: Any, label: str) -> str:
    value = http.resource_id(payload)
    if not value:
        raise http.LoyaltyV2HttpError(0, f"{label} returned no id", payload)
    return value


def _card_definition_body(name: str, enable_pay_with_points: bool) -> dict:
    pay_with_points: dict
    if enable_pay_with_points:
        pay_with_points = {
            "type": "EXCHANGE_RATIO",
            "exchange_ratio": {"formula": 1},
        }
    else:
        pay_with_points = {"type": "NO_PAYMENTS"}

    return {
        "name": name,
        "type": "INDIVIDUAL",
        "status": "DRAFT",
        "points_expiration": {"type": "NO_EXPIRATION"},
        "pending_points": {"type": "IMMEDIATE"},
        "spending_limits": {
            "global": {"type": "NO_LIMIT", "limits": None},
            "transactions": {"type": "NO_LIMIT", "limits": None},
        },
        "pay_with_points": pay_with_points,
    }


def _earning_rule_body(name: str, card_definition_id: str) -> dict:
    return {
        "name": name,
        "status": "DRAFT",
        "trigger": {"event": "customer.order.paid"},
        "earnings": [
            {
                "effects": [
                    {
                        "type": "POINTS",
                        "points": {
                            "value": 100,
                            "card_definition_id": card_definition_id,
                        },
                    }
                ]
            }
        ],
    }


def _reward_body(
    name: str, spend_card_definition_id: str, credit_card_definition_id: str
) -> dict:
    return {
        "name": name,
        "type": "DIGITAL",
        "status": "DRAFT",
        "material": None,
        "digital": {
            "type": "LOYALTY_CARD_POINTS",
            "discount_coupons": None,
            "gift_vouchers": None,
            "loyalty_card_points": {
                "points": 5,
                "card_definition_id": credit_card_definition_id,
            },
        },
        "costs": [
            {
                "spending": [
                    {
                        "points": 10,
                        "card_definition_id": spend_card_definition_id,
                    }
                ]
            }
        ],
    }


def setup() -> LoyaltyV2Context:
    suffix = f"{int(time.time() * 1000)}_{uuid.uuid4().hex[:6]}"
    program_name = f"py_sdk_lv2_program_{suffix}"
    card_name = f"py_sdk_lv2_card_{suffix}"
    reward_card_name = f"py_sdk_lv2_reward_card_{suffix}"
    earning_rule_name = f"py_sdk_lv2_earn_{suffix}"
    reward_name = f"py_sdk_lv2_reward_{suffix}"

    program_id = _require_id(
        http.create_program({"name": program_name}), "create_program"
    )

    card_definition_id = _require_id(
        http.create_card_definition(_card_definition_body(card_name, True)),
        "create_card_definition",
    )
    http.activate_card_definition(card_definition_id)

    reward_card_definition_id = _require_id(
        http.create_card_definition(_card_definition_body(reward_card_name, False)),
        "create_card_definition (reward target)",
    )
    http.activate_card_definition(reward_card_definition_id)

    earning_rule_id = _require_id(
        http.create_earning_rule(
            _earning_rule_body(earning_rule_name, card_definition_id)
        ),
        "create_earning_rule",
    )
    http.activate_earning_rule(earning_rule_id)

    reward_id = _require_id(
        http.create_reward(
            _reward_body(reward_name, card_definition_id, reward_card_definition_id)
        ),
        "create_reward",
    )
    http.activate_reward(reward_id)

    http.batch_assign_card_definitions(
        program_id,
        {
            "assign": [
                {"id": card_definition_id},
                {"id": reward_card_definition_id},
            ]
        },
    )
    http.batch_assign_earning_rules(
        program_id, {"assign": [{"id": earning_rule_id}]}
    )
    http.batch_assign_rewards(
        program_id,
        {
            "assign": [
                {
                    "id": reward_id,
                    "stock": {"type": "UNLIMITED"},
                }
            ]
        },
    )
    http.activate_program(program_id)

    return LoyaltyV2Context(
        suffix=suffix,
        program_id=program_id,
        card_definition_id=card_definition_id,
        reward_card_definition_id=reward_card_definition_id,
        earning_rule_id=earning_rule_id,
        reward_id=reward_id,
        program_name=program_name,
    )


def _ignore(label: str, action: Callable[[], Any]) -> bool:
    """Run cleanup action. Returns True on success / 404; False when skipped after error."""
    try:
        action()
        return True
    except http.LoyaltyV2HttpError as exc:
        if exc.status == 404:
            return True
        print(f"Loyalty v2 teardown {label}: {exc}")
        return False


def _delete_after_deactivate(
    label: str,
    deactivate: Optional[Callable[[], Any]],
    delete: Callable[[], Any],
) -> None:
    if deactivate is not None:
        _ignore(f"deactivate_{label}", deactivate)
    if not _ignore(f"delete_{label}", delete) and deactivate is not None:
        # Delete rejected (e.g. 423); leave deactivated and do not fail the suite.
        _ignore(f"deactivate_{label}_after_delete_reject", deactivate)


def teardown(ctx: Optional[LoyaltyV2Context]) -> None:
    """
    Cleanup order that avoids 423 on card definitions:
    1. Deactivate + delete program (drops assignments)
    2. Deactivate + delete earning rule and reward
    3. Delete card definitions
    """
    if ctx is None:
        return

    if ctx.program_id:
        _delete_after_deactivate(
            "program",
            lambda: http.deactivate_program(ctx.program_id),
            lambda: http.delete_program(ctx.program_id),
        )

    if ctx.earning_rule_id:
        _delete_after_deactivate(
            "earning_rule",
            lambda: http.deactivate_earning_rule(ctx.earning_rule_id),
            lambda: http.delete_earning_rule(ctx.earning_rule_id),
        )
    if ctx.reward_id:
        _delete_after_deactivate(
            "reward",
            lambda: http.deactivate_reward(ctx.reward_id),
            lambda: http.delete_reward(ctx.reward_id),
        )

    time.sleep(0.5)

    for card_id in (ctx.card_definition_id, ctx.reward_card_definition_id):
        if card_id:
            _delete_after_deactivate(
                "card_definition",
                None,
                lambda card_id=card_id: http.delete_card_definition(card_id),
            )
