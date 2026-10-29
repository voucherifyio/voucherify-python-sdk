import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../"))
sys.path.insert(0, os.path.dirname(__file__))

try:
    import spec_utils

    HAS_CREDENTIALS = bool(spec_utils.X_APP_ID and spec_utils.X_APP_TOKEN)
except Exception:
    HAS_CREDENTIALS = False

import loyalty_v2_fixture as fixture


@unittest.skipUnless(HAS_CREDENTIALS, "Missing X_APP_ID / X_APP_TOKEN")
class TestLoyaltyV2Fixture(unittest.TestCase):
    def test_setup_and_teardown_creates_program_resources(self):
        ctx = fixture.setup()
        try:
            self.assertIsNotNone(ctx.program_id)
            self.assertTrue(ctx.program_id.startswith("lprg_"))
            self.assertIsNotNone(ctx.card_definition_id)
            self.assertTrue(ctx.card_definition_id.startswith("lcdef_"))
            self.assertIsNotNone(ctx.reward_card_definition_id)
            self.assertTrue(ctx.reward_card_definition_id.startswith("lcdef_"))
            self.assertIsNotNone(ctx.earning_rule_id)
            self.assertTrue(ctx.earning_rule_id.startswith("lern_"))
            self.assertIsNotNone(ctx.reward_id)
            self.assertTrue(ctx.reward_id.startswith("lrew_"))
        finally:
            fixture.teardown(ctx)


if __name__ == "__main__":
    unittest.main()
