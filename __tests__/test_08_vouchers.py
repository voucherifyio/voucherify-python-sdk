import sys
import os
import unittest
import random
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../"))
import voucherify as voucherifyClient
import spec_utils

HAS_CREDENTIALS = (
    hasattr(spec_utils, "configuration") and spec_utils.configuration is not None
)


class TestVouchersSDK(unittest.TestCase):

    delay = 2
    initial_balance = 1000

    def setUp(self):
        if not HAS_CREDENTIALS:
            self.fail("Client credentials not provided")
        self.created_campaigns = []
        self.created_customers = []

    def tearDown(self):
        if HAS_CREDENTIALS:
            with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
                campaigns_api = voucherifyClient.CampaignsApi(api_client)
                customers_api = voucherifyClient.CustomersApi(api_client)

                for campaign in self.created_campaigns:
                    try:
                        campaigns_api.delete_campaign(campaign.id)
                    except Exception as e:
                        print(f"Failed to delete campaign {campaign.id}: {e}")

                for customer in self.created_customers:
                    try:
                        customers_api.delete_customer(customer.id)
                    except Exception as e:
                        print(f"Failed to delete customer {customer.id}: {e}")

    def test_01_enable_disable_voucher(self):
        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            campaigns_api = voucherifyClient.CampaignsApi(api_client)
            vouchers_api = voucherifyClient.VouchersApi(api_client)

            # create campaign with 1 voucher
            campaign_body = voucherifyClient.CampaignsCreateRequestBody(
                name=f"Campaign_{random.randint(0, 1000000)}",
                voucher=voucherifyClient.CampaignsCreateRequestBodyVoucher(
                    type="DISCOUNT_VOUCHER",
                    discount=voucherifyClient.Discount(type="AMOUNT", amount_off=1000),
                ),
                vouchers_count=1,
            )
            campaign = campaigns_api.create_campaign(campaign_body)
            self.created_campaigns.append(campaign)

            time.sleep(self.delay)

            vouchers_list = vouchers_api.list_vouchers(campaign_id=campaign.id, limit=1)
            self.assertGreater(len(vouchers_list.vouchers), 0)
            voucher = vouchers_list.vouchers[0]

            self.assertTrue(voucher.active)

            disabled = vouchers_api.disable_voucher(voucher.code)
            self.assertFalse(disabled.active)

            time.sleep(self.delay)

            enabled = vouchers_api.enable_voucher(voucher.code)
            self.assertTrue(enabled.active)

    def test_02_update_loyalty_card_balance(self):
        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            campaigns_api = voucherifyClient.CampaignsApi(api_client)
            customers_api = voucherifyClient.CustomersApi(api_client)
            publications_api = voucherifyClient.PublicationsApi(api_client)
            vouchers_api = voucherifyClient.VouchersApi(api_client)
            loyalties_api = voucherifyClient.LoyaltiesApi(api_client)

            # create loyalty campaign
            campaign_body = voucherifyClient.CampaignsCreateRequestBody(
                name=f"Loyalty_{random.randint(0, 1000000)}",
                voucher=voucherifyClient.CampaignsCreateRequestBodyVoucher(
                    type="LOYALTY_CARD",
                    loyalty_card=voucherifyClient.CampaignLoyaltyCard(
                        points=self.initial_balance
                    ),
                ),
                vouchers_count=1,
            )
            campaign = campaigns_api.create_campaign(campaign_body)
            self.created_campaigns.append(campaign)

            time.sleep(self.delay)

            vouchers_list = vouchers_api.list_vouchers(campaign_id=campaign.id, limit=1)
            self.assertGreater(len(vouchers_list.vouchers), 0)
            loyalty_voucher = vouchers_list.vouchers[0]

            # create customer
            customer_body = voucherifyClient.CustomersCreateRequestBody(
                source_id=f"Customer_{random.randint(0, 1000000)}"
            )
            customer = customers_api.create_customer(customer_body)
            self.created_customers.append(customer)

            # publish voucher to customer
            publication_body = voucherifyClient.PublicationsCreateRequestBody(
                customer={"id": customer.id}, voucher=loyalty_voucher.code
            )

            publications_api.create_publication(
                publications_create_request_body=publication_body
            )
            # update balance
            source_id = f"Source_{random.randint(0, 1000000)}"
            amount = 10000
            reason = "Regular customer"

            updated = loyalties_api.update_loyalty_card_balance(
                loyalty_voucher.code,
                voucherifyClient.LoyaltiesMembersBalanceUpdateRequestBody(
                    source_id=source_id, points=amount, reason=reason
                ),
            )

            self.assertIsNotNone(updated)
            self.assertEqual(updated.balance, self.initial_balance + amount)


if __name__ == "__main__":
    unittest.main()
