import os
import sys
import unittest

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
        cls.customers_api = voucherifyClient.CustomersApi(cls.api_client)

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


if __name__ == "__main__":
    unittest.main()
