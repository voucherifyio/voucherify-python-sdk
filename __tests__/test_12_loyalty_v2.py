import json
import os
import sys
import time
import unittest
from datetime import date, timedelta

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../"))
sys.path.insert(0, os.path.dirname(__file__))

import voucherify as voucherifyClient
import spec_utils
import loyalty_v2_fixture as fixture


HAS_CREDENTIALS = bool(
    getattr(spec_utils, "X_APP_ID", None) and getattr(spec_utils, "X_APP_TOKEN", None)
)


@unittest.skipUnless(HAS_CREDENTIALS, "Missing X_APP_ID / X_APP_TOKEN")
class TestLoyaltyV2SDK(unittest.TestCase):
    fixture_ctx = None
    customer = None
    member = None
    member_id = None
    primary_card_id = None

    @classmethod
    def setUpClass(cls):
        cls.api_client = voucherifyClient.ApiClient(spec_utils.configuration)
        cls.programs_api = voucherifyClient.LV2ProgramsApi(cls.api_client)
        cls.examine_api = voucherifyClient.LV2ExamineApi(cls.api_client)
        cls.earning_rules_api = voucherifyClient.LV2EarningRulesApi(cls.api_client)
        cls.rewards_api = voucherifyClient.LV2RewardsApi(cls.api_client)
        cls.customers_api = voucherifyClient.CustomersApi(cls.api_client)
        cls.orders_api = voucherifyClient.OrdersApi(cls.api_client)

        cls.fixture_ctx = fixture.setup()

        cls.customer = cls.customers_api.create_customer(
            voucherifyClient.CustomersCreateRequestBody(
                source_id=f"lv2_customer_{cls.fixture_ctx.suffix}",
                name="Loyalty v2 Python SDK test",
            )
        )

        created = cls.programs_api.create_program_member(
            cls.fixture_ctx.program_id,
            voucherifyClient.V2LoyaltiesProgramsMembersCreateRequestBody(
                customer_identification={
                    "type": "customer_id",
                    "customer_id": cls.customer.id,
                    "customer_source_id": None,
                }
            ),
        )
        cls.member_id = created.id
        cls.member = cls.programs_api.get_program_member(
            cls.fixture_ctx.program_id, cls.member_id
        )
        cls.primary_card_id = cls._resolve_primary_card_id(
            cls.member.cards, cls.fixture_ctx.card_definition_id
        )

    @classmethod
    def tearDownClass(cls):
        try:
            if cls.fixture_ctx is not None and cls.member_id is not None:
                cls._ignore_api(
                    "deactivate_program_member",
                    lambda: cls.programs_api.deactivate_program_member(
                        cls.fixture_ctx.program_id, cls.member_id
                    ),
                )
                cls._ignore_api(
                    "delete_program_member",
                    lambda: cls.programs_api.delete_program_member(
                        cls.fixture_ctx.program_id, cls.member_id
                    ),
                )
            if cls.customer is not None:
                cls._ignore_api(
                    "delete_customer",
                    lambda: cls.customers_api.delete_customer(cls.customer.id),
                )
            if cls.fixture_ctx is not None:
                fixture.teardown(cls.fixture_ctx)
        finally:
            cls.fixture_ctx = None
            cls.member = None
            cls.member_id = None
            cls.customer = None
            cls.primary_card_id = None

    @staticmethod
    def _ignore_api(label, action):
        try:
            action()
        except voucherifyClient.ApiException as exc:
            if exc.status == 404:
                return
            print(f"{label}: {exc}")

    @staticmethod
    def _resolve_primary_card_id(cards, card_definition_id):
        if not cards:
            raise AssertionError("No loyalty card on member")
        for entry in cards:
            card = getattr(entry, "card", None)
            if card is not None and card.card_definition_id == card_definition_id:
                return card.id
        first = cards[0].card
        if first is None or first.id is None:
            raise AssertionError("No loyalty card on member")
        return first.id

    def test_01_setup_creates_activated_program_resources(self):
        self.assertIsNotNone(self.fixture_ctx.program_id)
        self.assertTrue(self.fixture_ctx.program_id.startswith("lprg_"))
        self.assertTrue(self.fixture_ctx.card_definition_id.startswith("lcdef_"))
        self.assertTrue(self.fixture_ctx.earning_rule_id.startswith("lern_"))
        self.assertTrue(self.fixture_ctx.reward_id.startswith("lrew_"))

    def test_02_member_lifecycle_via_sdk(self):
        self.assertIsNotNone(self.member_id)
        self.assertIsNotNone(self.member.customer_id)
        self.assertTrue(self.member.cards)

        fetched = self.programs_api.get_program_member(
            self.fixture_ctx.program_id, self.member_id
        )
        self.assertIsNotNone(fetched.id)

        listed = self.programs_api.list_program_members(self.fixture_ctx.program_id)
        self.assertTrue(any(item.id == self.member_id for item in listed.data or []))

        membership = self.programs_api.get_program_membership(
            self.fixture_ctx.program_id, self.customer.id
        )
        self.assertIsNotNone(membership)

        if self.member.status == "INACTIVE":
            activated = self.programs_api.activate_program_member(
                self.fixture_ctx.program_id, self.member_id
            )
            self.assertIsNotNone(activated.status)

        self.programs_api.deactivate_program_member(
            self.fixture_ctx.program_id, self.member_id
        )
        deactivated = self.programs_api.get_program_member(
            self.fixture_ctx.program_id, self.member_id
        )
        self.assertNotEqual(deactivated.status, "ACTIVE")

        self.programs_api.activate_program_member(
            self.fixture_ctx.program_id, self.member_id
        )
        type(self).member = self.programs_api.get_program_member(
            self.fixture_ctx.program_id, self.member_id
        )
        self.assertEqual(self.member.status, "ACTIVE")
        type(self).primary_card_id = self._resolve_primary_card_id(
            self.member.cards, self.fixture_ctx.card_definition_id
        )
        self.assertTrue(self.primary_card_id.startswith("lcrd_"))

    def test_03_adjust_card_points_and_list_transactions(self):
        self.programs_api.adjust_card_points(
            self.fixture_ctx.program_id,
            self.member_id,
            self.primary_card_id,
            voucherifyClient.V2LoyaltiesProgramsMembersCardsPointsAdjustRequestBody(
                points=100,
                reason="python sdk loyalty v2 e2e",
            ),
        )

        time.sleep(3)

        type(self).member = self.programs_api.get_program_member(
            self.fixture_ctx.program_id, self.member_id
        )
        primary = None
        for entry in self.member.cards or []:
            if entry.card and entry.card.id == self.primary_card_id:
                primary = entry
                break
        self.assertIsNotNone(primary)
        self.assertIsNotNone(primary.card.balance)
        self.assertGreater(primary.card.balance.points or 0, 0)

        transactions = self.programs_api.list_card_transactions(
            self.fixture_ctx.program_id,
            self.member_id,
            self.primary_card_id,
        )
        self.assertTrue(transactions.data)

    def test_04_create_member_order_payment_dry_run(self):
        order = self.orders_api.create_order(
            voucherifyClient.OrdersCreateRequestBody(
                amount=2500,
                source_id=f"lv2_order_{self.fixture_ctx.suffix}",
                customer=voucherifyClient.Customer(id=self.customer.id),
            )
        )
        self.assertTrue(order.id.startswith("ord_"))

        self.programs_api.create_member_order_payment(
            self.fixture_ctx.program_id,
            self.member_id,
            voucherifyClient.V2LoyaltiesProgramsMembersOrdersPaymentsCreateRequestBody(
                card_id=self.primary_card_id,
                order=voucherifyClient.OrderPaymentOrder(id=order.id),
                payment_limit=voucherifyClient.LoyaltiesProgramsMembersOrdersPaymentsCreateRequestBodyLimit(
                    type="CARD_BALANCE"
                ),
                mode="DRY_RUN",
            ),
        )

        listed = self.programs_api.list_member_order_payments(
            self.fixture_ctx.program_id, self.member_id
        )
        self.assertIsNotNone(listed)

    def test_05_purchase_member_reward_and_refund(self):
        self.programs_api.purchase_member_reward(
            self.fixture_ctx.program_id,
            self.member_id,
            voucherifyClient.V2LoyaltiesProgramsMembersRewardsPurchasesCreateRequestBody(
                reward_id=self.fixture_ctx.reward_id,
                mode="DRY_RUN",
            ),
        )

        # Generated transaction model types card_transaction_id as object; live API
        # returns a string. Read raw JSON so the suite does not depend on that bug.
        raw = self.programs_api.purchase_member_reward_without_preload_content(
            self.fixture_ctx.program_id,
            self.member_id,
            voucherifyClient.V2LoyaltiesProgramsMembersRewardsPurchasesCreateRequestBody(
                reward_id=self.fixture_ctx.reward_id,
                mode="TRANSACTION",
            ),
        )
        purchase = json.loads(raw.data.decode("utf-8"))
        self.assertIsNotNone(purchase)
        reward_transaction_id = (purchase.get("transaction") or {}).get("id")
        self.assertIsNotNone(reward_transaction_id)

        approved_row = None
        for _ in range(15):
            time.sleep(1)
            listed = self.programs_api.list_member_reward_purchases(
                self.fixture_ctx.program_id, self.member_id
            )
            rows = listed.data or []
            self.assertTrue(rows)
            for row in rows:
                if row.id == reward_transaction_id and row.status == "APPROVED":
                    approved_row = row
                    break
            if approved_row is None and rows and rows[0].status == "APPROVED":
                approved_row = rows[0]
            if approved_row is not None:
                break

        self.assertIsNotNone(approved_row)
        refund_id = approved_row.id or reward_transaction_id
        self.programs_api.refund_reward_purchase(
            self.fixture_ctx.program_id,
            refund_id,
            voucherifyClient.V2LoyaltiesProgramsRewardsPurchasesRefundRequestBody(
                policies=voucherifyClient.RewardPurchaseRefundPolicies(
                    refund="ALLOW",
                    stock="DEFAULT",
                )
            ),
        )

    def test_06_examine_and_reports_via_sdk(self):
        identification = voucherifyClient.ExamineCustomerIdentification(
            type="member_id",
            member_id=self.member_id,
        )
        earning_rules_body = (
            voucherifyClient.LoyaltiesExamineEarningRulesExamineRequestBody(
                trigger=voucherifyClient.LoyaltiesExamineEarningRulesExamineRequestBodyTrigger(
                    type="SPECIFIC",
                    specific=voucherifyClient.LoyaltiesExamineEarningRulesExamineRequestBodyTriggerSpecific(
                        event="customer.order.paid",
                    ),
                ),
                customer_identification=identification,
                customer_order_paid=voucherifyClient.LoyaltiesExamineEarningRulesExamineRequestBodyCustomerOrderPaid(
                    order=voucherifyClient.LoyaltiesExamineEarningRulesExamineRequestBodyOrder(
                        amount=5000,
                    )
                ),
            )
        )
        self.assertIsNotNone(
            self.examine_api.examine_earning_rules(earning_rules_body)
        )

        rewards_body = voucherifyClient.LoyaltiesExamineRewardsExamineRequestBody(
            customer_identification=identification,
        )
        self.assertIsNotNone(self.examine_api.examine_rewards(rewards_body))

        members_summary = self.programs_api.list_program_members_summary_reports(
            self.fixture_ctx.program_id
        )
        self.assertIsNotNone(members_summary.data)

        rewards_summary = self.programs_api.list_program_rewards_summary_reports(
            self.fixture_ctx.program_id
        )
        self.assertIsNotNone(rewards_summary.data)

        end_date = date.today()
        start_date = end_date - timedelta(days=1)
        members_daily = self.programs_api.list_program_members_daily_reports(
            self.fixture_ctx.program_id, start_date, end_date, "day"
        )
        self.assertIsNotNone(members_daily.data)

        card_daily = self.programs_api.list_member_card_daily_reports(
            self.fixture_ctx.program_id,
            self.member_id,
            self.primary_card_id,
            start_date,
            end_date,
            "day",
        )
        self.assertIsNotNone(card_daily.data)

        earning_rule = self.earning_rules_api.get_earning_rule(
            self.fixture_ctx.earning_rule_id
        )
        self.assertEqual(earning_rule.id, self.fixture_ctx.earning_rule_id)

        reward = self.rewards_api.get_reward(self.fixture_ctx.reward_id)
        self.assertEqual(reward.id, self.fixture_ctx.reward_id)


if __name__ == "__main__":
    unittest.main()
