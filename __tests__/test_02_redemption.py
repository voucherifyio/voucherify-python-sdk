import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../"))

import spec_utils
import unittest
import voucherify as voucherifyClient
import random

random_code = random.randint(0, 10000000)
voucher_code = "test_code_" + str(random_code)
specific_code_1 = "test_code_1_" + str(random_code)
specific_code_2 = "test_code_2_" + str(random_code)
customer_source_id = "test_customer_" + str(random_code)
customer_metadata = {"key_customer": "test"}


HAS_CREDENTIALS = (
    hasattr(spec_utils, "configuration") and spec_utils.configuration is not None
)


class TestRedemptionSDK(unittest.TestCase):
    delay = 2

    def setUp(self):
        self.created_campaigns = []

    def tearDown(self):
        if HAS_CREDENTIALS:
            with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
                campaigns_api = voucherifyClient.CampaignsApi(api_client)
                for campaign in getattr(self, "created_campaigns", []):
                    try:
                        campaigns_api.delete_campaign(campaign.id)
                    except Exception:
                        pass

    def helper_create_campaign_with_vouchers(self, campaign_name, voucher_codes):
        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            campaigns_api = voucherifyClient.CampaignsApi(api_client)

            campaign_body = voucherifyClient.CampaignsCreateRequestBody(
                name=campaign_name,
                voucher=voucherifyClient.CampaignsCreateRequestBodyVoucher(
                    type="DISCOUNT_VOUCHER",
                    discount=voucherifyClient.Discount(type="AMOUNT", amount_off=1000),
                ),
            )
            campaign = campaigns_api.create_campaign(campaign_body)
            self.created_campaigns.append(campaign)

            # Add specific vouchers
            for code in voucher_codes:
                campaigns_api.add_voucher_with_specific_code_to_campaign(
                    campaign.id, code
                )

            return campaign

    def test_01_validate_stacked_discounts(self):
        self.helper_create_campaign_with_vouchers(
            f"campaign_{random_code}", [specific_code_1, specific_code_2]
        )

        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            validations_api = voucherifyClient.ValidationsApi(api_client)
            validations_request = voucherifyClient.ValidationsValidateRequestBody(
                redeemables=[
                    voucherifyClient.ValidationsValidateRequestBodyRedeemablesItem(
                        id=specific_code_1, object="voucher"
                    ),
                    voucherifyClient.ValidationsValidateRequestBodyRedeemablesItem(
                        id=specific_code_2, object="voucher"
                    ),
                ],
                customer=voucherifyClient.Customer(
                    source_id=customer_source_id, metadata=customer_metadata
                ),
                order=voucherifyClient.Order(amount=20000, metadata=customer_metadata),
            )
            result = validations_api.validate_stacked_discounts(validations_request)
            self.assertIsNotNone(result)
            self.assertIsNotNone(result.redeemables)
            self.assertEqual(len(result.redeemables), 2)

    def test_02_redeem_stacked_discounts(self):
        self.helper_create_campaign_with_vouchers(
            f"campaign_{random_code}_redeem", [voucher_code]
        )

        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            redemptions_api = voucherifyClient.RedemptionsApi(api_client)
            redemptions_request = voucherifyClient.RedemptionsRedeemRequestBody(
                redeemables=[
                    voucherifyClient.RedemptionsRedeemRequestBodyRedeemablesItem(
                        id=voucher_code, object="voucher"
                    )
                ],
                customer=voucherifyClient.Customer(
                    source_id=customer_source_id, metadata=customer_metadata
                ),
                order=voucherifyClient.Order(
                    amount=30000, metadata={"key_customer": "test"}
                ),
                metadata={"key": "value"},
            )
            result = redemptions_api.redeem_stacked_discounts(redemptions_request)
            self.assertIsNotNone(result)
            self.assertEqual(result.redemptions[0].result, "SUCCESS")

    def test_03_list_redemptions(self):
        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            redemptions_api = voucherifyClient.RedemptionsApi(api_client)
            list_redemptions_filters = voucherifyClient.ParameterFiltersListRedemptions(
                voucher_code=voucherifyClient.ParameterFiltersListRedemptionsVoucherCode(
                    conditions=voucherifyClient.FilterConditionsString(
                        is_not=voucher_code
                    )
                )
            )
            result = redemptions_api.list_redemptions(
                100, None, None, None, None, None, None, list_redemptions_filters
            )
            self.assertEqual(result.object, "list")


if __name__ == "__main__":
    unittest.main()
