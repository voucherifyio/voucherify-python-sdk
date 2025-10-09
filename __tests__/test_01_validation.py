import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../"))

import spec_utils
import unittest
import voucherify as voucherifyClient
import random

random_code_1 = random.randint(0, 10000000)
voucher_code_1 = f"test_code_{random_code_1}"

random_code_2 = random.randint(0, 10000000)
voucher_code_2 = f"test_code_{random_code_2}"

campaign_name = "test_campaign_" + str(random_code_1)
customer_source_id = "test_customer_" + str(random_code_2)

HAS_CREDENTIALS = (
    hasattr(spec_utils, "configuration") and spec_utils.configuration is not None
)


class TestValidationSDK(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestValidationSDK, self).__init__(*args, **kwargs)

    def setUp(self):
        self.created_campaigns = []

    def tearDown(self):
        if HAS_CREDENTIALS:
            with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
                campaigns_api = voucherifyClient.CampaignsApi(api_client)
                for campaign in getattr(self, "created_campaigns", []):
                    try:
                        campaigns_api.delete_campaign(campaign.id)
                    except voucherifyClient.ApiException as e:
                        if e.status != 404:
                            print(f"Failed to delete campaign {campaign.id}: {e}")

    def test_01_validate_stacked_discounts_all_applicable(self):
        # Open a Voucherify API client context
        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            campaigns_api = voucherifyClient.CampaignsApi(api_client)
            validations_api = voucherifyClient.ValidationsApi(api_client)

            # Step 1: Create a new campaign with a discount voucher
            campaign_body = voucherifyClient.CampaignsCreateRequestBody(
                name=campaign_name,
                voucher=voucherifyClient.CampaignsCreateRequestBodyVoucher(
                    type="DISCOUNT_VOUCHER",
                    discount=voucherifyClient.Discount(type="AMOUNT", amount_off=1000),
                ),
            )
            campaign = campaigns_api.create_campaign(campaign_body)
            self.created_campaigns.append(campaign)

            # Step 2: Add a specific voucher code to the campaign
            voucher = campaigns_api.add_voucher_with_specific_code_to_campaign(
                campaign.id, voucher_code_1
            )

            # Step 3: Prepare a stacked discount validation request
            validations_validate_request_body = (
                voucherifyClient.ValidationsValidateRequestBody(
                    redeemables=[
                        voucherifyClient.ValidationsValidateRequestBodyRedeemablesItem(
                            id=voucher.code, object="voucher"
                        )
                    ],
                    customer=None,  # No customer assigned
                    order=voucherifyClient.Order(amount=20000),  # Order details
                )
            )

            # Step 4: Perform the stacked discount validation
            result = validations_api.validate_stacked_discounts(
                validations_validate_request_body
            )

            # Step 5: Basic checks on the validation result
            self.assertIsNotNone(result)  # Result should exist
            self.assertTrue(result.valid)  # All vouchers should be applicable
            self.assertIsNotNone(result.redeemables)  # Redeemables list should exist
            self.assertIsNone(
                result.inapplicable_redeemables
            )  # No inapplicable vouchers

            # Step 6: Check order details
            self.assertIsNotNone(result.order)
            self.assertEqual(result.order.amount, 20000)
            self.assertEqual(
                result.order.total_amount, 20000 - 1000
            )  # Discount applied

            # Step 7: Inspect the first redeemable item
            redeemable = result.redeemables[0]
            self.assertIsInstance(
                redeemable.result,
                voucherifyClient.ValidationsValidateResponseBodyRedeemablesItemResult,
            )
            self.assertIsInstance(
                redeemable.applicable_to, voucherifyClient.ApplicableToResultList
            )
            self.assertIsInstance(
                redeemable.inapplicable_to, voucherifyClient.InapplicableToResultList
            )

            # Step 8: Check the discount applied to the redeemable
            discount = redeemable.result.discount
            self.assertEqual(discount.type, "AMOUNT")
            self.assertEqual(discount.amount_off, 1000)

            # Step 9: Verify all redeemables are of the correct type
            for r in result.redeemables:
                self.assertIsInstance(
                    r, voucherifyClient.ValidationsValidateResponseBodyRedeemablesItem
                )

    def test_02_validate_stacked_discounts_with_inapplicable(self):
        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            api_instance = voucherifyClient.ValidationsApi(api_client)
            try:
                validations_validate_request_body = voucherifyClient.ValidationsValidateRequestBody(
                    redeemables=[
                        voucherifyClient.ValidationsValidateRequestBodyRedeemablesItem(
                            id=voucher_code_2, object="voucher"
                        ),
                        voucherifyClient.ValidationsValidateRequestBodyRedeemablesItem(
                            id="non_existing_voucher", object="voucher"
                        ),
                    ],
                    customer=voucherifyClient.Customer(source_id=customer_source_id),
                    order=voucherifyClient.Order(amount=1000),
                )
                result = api_instance.validate_stacked_discounts(
                    validations_validate_request_body
                )

                self.assertIsNotNone(result)
                for r in result.redeemables:
                    self.assertIsInstance(
                        r,
                        voucherifyClient.ValidationsValidateResponseBodyRedeemablesItem,
                    )
                self.assertFalse(result.valid)
                self.assertIsNotNone(result.inapplicable_redeemables)
                # Check the first inapplicable redeemable
                inapplicable = result.inapplicable_redeemables[0]
                self.assertIsNotNone(inapplicable)
                self.assertIsInstance(
                    inapplicable, voucherifyClient.ValidationsRedeemableInapplicable
                )
                self.assertEqual(inapplicable.status, "INAPPLICABLE")
                self.assertIsNotNone(inapplicable.id)
                self.assertIsNotNone(inapplicable.object)
                self.assertIsNotNone(inapplicable.result)
                self.assertIsInstance(
                    inapplicable.result,
                    voucherifyClient.ValidationsRedeemableInapplicableResult,
                )
                self.assertIsNotNone(inapplicable.result.error)
                self.assertIsInstance(inapplicable.result.error, voucherifyClient.Error)
            except voucherifyClient.ApiException as e:
                self.fail(e)

    def test_03_validate_stacked_discounts_without_customer(self):
        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            api_instance = voucherifyClient.ValidationsApi(api_client)
            try:
                validations_validate_request_body = voucherifyClient.ValidationsValidateRequestBody(
                    redeemables=[
                        voucherifyClient.ValidationsValidateRequestBodyRedeemablesItem(
                            id="random_voucher", object="voucher"
                        )
                    ],
                    customer=None,
                    order=voucherifyClient.Order(amount=1000),
                )
                result = api_instance.validate_stacked_discounts(
                    validations_validate_request_body
                )
                self.assertIsNotNone(result)
                self.assertFalse(result.valid)
                self.assertIsNotNone(result.redeemables)
                self.assertIsNotNone(result.inapplicable_redeemables)
                self.assertEqual(
                    len(result.redeemables), len(result.inapplicable_redeemables)
                )
            except voucherifyClient.ApiException as e:
                self.fail(e)


if __name__ == "__main__":
    unittest.main()
