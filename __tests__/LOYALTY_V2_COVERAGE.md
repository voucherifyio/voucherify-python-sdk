# Loyalty v2 e2e coverage (Python SDK)

This document describes what `test_12_loyalty_v2.py` exercises for Loyalty v2 in the Python SDK, and which admin calls still go through `loyalty_v2_http.py` because they are not on the published allowlist.

It is **not** a full API contract suite. Coverage is one happy-path flow against a live project.

## Files

| File | Role |
|------|------|
| `test_12_loyalty_v2.py` | unittest suite (SDK runtime + light reports/examine) |
| `test_12a_loyalty_v2_fixture.py` | Optional fixture-only setup/teardown smoke |
| `loyalty_v2_fixture.py` | HTTP setup / teardown |
| `loyalty_v2_http.py` | stdlib `urllib.request` for unpublished admin paths |
| `spec_utils.py` | Shared credentials and `ApiClient` configuration |

`npm run generate-sdk-python` overwrites `voucherify/` and `test/`. It does **not** delete `__tests__/`, so this file and the Loyalty v2 tests stay. Do not put e2e under the generated `test/` tree. Do not call unpublished admin paths through the SDK.

## Client split

| Concern | Client | Why |
|---------|--------|-----|
| Program / card definition / earning rule / reward admin | **HTTP** (`loyalty_v2_http`) | Not on the published Python SDK allowlist |
| Member lifecycle, points, payments, purchases, examine, selected reports | **SDK** (`LV2ProgramsApi`, `LV2ExamineApi`) | Allowlisted Loyalty v2 operations |
| Optional GET of fixture earning rule / reward | **SDK** (`LV2EarningRulesApi`, `LV2RewardsApi`) | Allowlisted GETs |
| Test customer + order | **SDK** (`CustomersApi`, `OrdersApi`) | Existing v1 helpers |

## Depth legend

| Depth | Meaning |
|-------|---------|
| **Smoke** | Call succeeds; body present; light shape checks |
| **Basic** | Smoke + id/status/list membership checks |
| **Flow** | Multi-step happy path |
| **Setup only** | Used to build the fixture; no per-call assertion beyond setup ids |

---

## Covered via published SDK

### Members (`LV2ProgramsApi`)

| Method | HTTP | Depth | Notes |
|--------|------|-------|-------|
| `create_program_member` | `POST .../members` | Flow | `customer_id` identification |
| `get_program_member` | `GET .../members/{memberId}` | Basic | Id match; cards present |
| `list_program_members` | `GET .../members` | Basic | Created member in list |
| `get_program_membership` | `GET .../memberships/{customerId}` | Smoke | Response present |
| `activate_program_member` | `POST .../activate` | Basic | Status becomes `ACTIVE` |
| `deactivate_program_member` | `POST .../deactivate` | Basic | Status not `ACTIVE` |
| `delete_program_member` | `DELETE .../members/{memberId}` | Smoke | Cleanup in `tearDownClass` |

Not covered: `batch_create_program_members`, `update_program_member`, member activities.

### Cards / points (`LV2ProgramsApi`)

| Method | HTTP | Depth | Notes |
|--------|------|-------|-------|
| `adjust_card_points` | `POST .../cards/{cardId}/points` | Flow | +100 admin credit; 3s wait |
| `list_card_transactions` | `GET .../cards/{cardId}/transactions` | Basic | Non-empty after adjust |

Pending-point activate/cancel is skipped: the fixture uses `pending_points.type = IMMEDIATE` (no pending bucket).

### Order payments (`LV2ProgramsApi` + `OrdersApi`)

| Method | HTTP | Depth | Notes |
|--------|------|-------|-------|
| `create_order` | `POST /v1/orders` | Smoke | Fixture order |
| `create_member_order_payment` | `POST .../orders/payments` | Flow | `DRY_RUN`, `CARD_BALANCE` |
| `list_member_order_payments` | `GET .../orders/payments` | Smoke | Response present |

Requires spend card with `pay_with_points.type = EXCHANGE_RATIO` (fixture).

### Reward purchases (`LV2ProgramsApi`)

| Method | HTTP | Depth | Notes |
|--------|------|-------|-------|
| `purchase_member_reward` | `POST .../rewards/purchases` | Flow | Dry-run typed; transaction via raw response (see note) |
| `list_member_reward_purchases` | `GET .../rewards/purchases` | Basic | Poll until `APPROVED` |
| `refund_reward_purchase` | `POST .../rewards/purchases/{id}/refund` | Flow | `policies.refund = ALLOW` |

Note: the generated combined purchase response types `card_transaction_id` as an object; the live API returns a string. The TRANSACTION call uses `purchase_member_reward_without_preload_content` and parses JSON.

### Examine (`LV2ExamineApi`)

| Method | HTTP | Depth |
|--------|------|-------|
| `examine_earning_rules` | `POST /v2/loyalties/examine/earning-rules` | Smoke |
| `examine_rewards` | `POST /v2/loyalties/examine/rewards` | Smoke |

### Reports (`LV2ProgramsApi`) — subset

| Method | Depth |
|--------|-------|
| `list_program_members_summary_reports` | Smoke |
| `list_program_rewards_summary_reports` | Smoke |
| `list_program_members_daily_reports` | Smoke |
| `list_member_card_daily_reports` | Smoke |

Empty report lists are a pass. Transport or 4xx errors fail the suite. Other report endpoints are intentionally not called.

### Allowlisted GETs

| Method | API | Depth |
|--------|-----|-------|
| `get_earning_rule` | `LV2EarningRulesApi` | Smoke |
| `get_reward` | `LV2RewardsApi` | Smoke |

---

## HTTP helper — migration map

When an operation is added to `scripts/shared/get-take-list.ts` and regenerated into the Python SDK, replace the `loyalty_v2_http` wrapper with the generated API class (expected tag prefix `LV2ProgramsApi`, `LV2EarningRulesApi`, or `LV2RewardsApi` depending on the OpenAPI tag).

| `loyalty_v2_http` | HTTP | Why HTTP today | Future SDK target (when allowlisted) | Depth |
|-------------------|------|----------------|--------------------------------------|-------|
| `create_program` | `POST /v2/loyalties/programs` | Not on allowlist | programs admin API `create_program` | Setup only |
| `activate_program` | `POST .../programs/{id}/activate` | Not on allowlist | matching activate method | Setup only |
| `deactivate_program` | `POST .../programs/{id}/deactivate` | Not on allowlist | matching deactivate method | Setup only |
| `delete_program` | `DELETE .../programs/{id}` | Not on allowlist | matching delete method | Setup only |
| `create_card_definition` | `POST /v2/loyalties/card-definitions` | Not on allowlist | card-definitions admin API | Setup only |
| `activate_card_definition` | `POST .../card-definitions/{id}/activate` | Not on allowlist | matching activate | Setup only |
| `delete_card_definition` | `DELETE .../card-definitions/{id}` | Not on allowlist | matching delete | Setup only |
| `create_earning_rule` | `POST /v2/loyalties/earning-rules` | Not on allowlist | earning-rules admin API | Setup only |
| `activate_earning_rule` | `POST .../earning-rules/{id}/activate` | Not on allowlist | matching activate | Setup only |
| `deactivate_earning_rule` | `POST .../earning-rules/{id}/deactivate` | Not on allowlist | matching deactivate | Setup only |
| `delete_earning_rule` | `DELETE .../earning-rules/{id}` | Not on allowlist | matching delete | Setup only |
| `create_reward` | `POST /v2/loyalties/rewards` | Not on allowlist | rewards admin API | Setup only |
| `activate_reward` | `POST .../rewards/{id}/activate` | Not on allowlist | matching activate | Setup only |
| `deactivate_reward` | `POST .../rewards/{id}/deactivate` | Not on allowlist | matching deactivate | Setup only |
| `delete_reward` | `DELETE .../rewards/{id}` | Not on allowlist | matching delete | Setup only |
| `batch_assign_card_definitions` | `POST .../card-definitions/batch` | Not on allowlist | batch assign on programs API | Setup only |
| `batch_assign_earning_rules` | `POST .../earning-rules/batch` | Not on allowlist | batch assign | Setup only |
| `batch_assign_rewards` | `POST .../rewards/batch` | Not on allowlist | batch assign | Setup only |

Card definitions have no deactivate path in OpenAPI; only activate + delete are wrapped.

### Teardown order (`loyalty_v2_fixture.teardown` + suite cleanup)

1. SDK: deactivate/delete member and customer (`TestLoyaltyV2SDK._cleanup_resources`)
2. HTTP: deactivate + delete program (drops assignments)
3. HTTP: deactivate + delete earning rule and reward
4. HTTP: delete both card definitions

---

## How to run

From the OpenAPI repo (Docker, same `.env` as other Python tests):

```bash
npm run test-python-sdk
```

Or locally in `sdks/python` (with dependencies installed):

```bash
python ./__tests__/test_12_loyalty_v2.py -v
```
