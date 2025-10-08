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


class TestClientSDK(unittest.TestCase):

    delay = 2
    voucher_discount_amount = 15

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

                # delete campaign
                for campaign in self.created_campaigns:
                    try:
                        campaigns_api.delete_campaign(campaign.id)
                    except Exception as e:
                        print(f"Failed to delete campaign {campaign.id}: {e}")

                # delete customer
                for customer in getattr(self, "created_customers", []):
                    try:
                        customers_api.delete_customer(customer.id)
                    except Exception as e:
                        print(f"Failed to delete customer {customer.id}: {e}")

    def test_01_client_configuration(self):
        self.assertIsNotNone(spec_utils.configuration)
        self.assertTrue(hasattr(spec_utils.configuration, "host"))

    def test_02_csv_file_exists(self):
        random_code = f"Voucher_{random.randint(0, 1000000)}"
        csv_content = (
            "Code,Voucher Type,Active,Start Date,Expiration Date,Discount Type,Value,Category,Redemption Limit,Additional Info,Region\n"
            f"{random_code},DISCOUNT_VOUCHER,TRUE,,,AMOUNT,{self.voucher_discount_amount},New,,Planned release in Fall 2022,Europe"
        )
        csv_path = os.path.join(
            os.getcwd(), "standalone_discount_vouchers_template_voucherify_client.csv"
        )
        with open(csv_path, "w") as f:
            f.write(csv_content)
        self.assertTrue(os.path.exists(csv_path))

    def test_03_import_csv_with_vouchers(self):
        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            campaigns_api = voucherifyClient.CampaignsApi(api_client)
            vouchers_api = voucherifyClient.VouchersApi(api_client)
            async_actions_api = voucherifyClient.AsyncActionsApi(api_client)

            campaign_body = voucherifyClient.CampaignsCreateRequestBody(
                name=f"Campaign_{random.randint(0, 1000000)}",
                voucher=voucherifyClient.CampaignsCreateRequestBodyVoucher(
                    type="DISCOUNT_VOUCHER",
                    discount=voucherifyClient.Discount(
                        type="AMOUNT", amount_off=self.voucher_discount_amount
                    ),
                ),
            )
            campaign = campaigns_api.create_campaign(campaign_body)
            self.assertIsNotNone(campaign)
            self.assertIsNotNone(campaign.id)
            self.created_campaigns.append(campaign)

            random_code = f"Voucher_{random.randint(0, 1000000)}"
            csv_content = (
                "Code,Voucher Type,Active,Start Date,Expiration Date,Discount Type,Value,Category,Redemption Limit,Additional Info,Region\n"
                f"{random_code},DISCOUNT_VOUCHER,TRUE,,,AMOUNT,{self.voucher_discount_amount},New,,Planned release in Fall 2022,Europe"
            )
            csv_path = os.path.join(
                os.getcwd(),
                "standalone_discount_vouchers_template_voucherify_client.csv",
            )
        try:
            with open(csv_path, "w", encoding="utf-8") as f:
                f.write(csv_content)

            with open(csv_path, "rb") as f:
                import_result = campaigns_api.import_vouchers_to_campaign_using_csv(
                    campaign.id, file=csv_path
                )

            self.assertIsNotNone(import_result)
            self.assertIsNotNone(import_result.async_action_id)

            max_attempts = 10
            attempt = 0
            while attempt < max_attempts:
                attempt += 1
                time.sleep(self.delay)
                action = async_actions_api.get_async_action(
                    import_result.async_action_id
                )
                if action.operation_status == "SUCCESS":
                    vouchers_list = vouchers_api.list_vouchers(campaign_id=campaign.id)
                    self.assertGreater(len(vouchers_list.vouchers), 0)
                    break
                elif action.operation_status == "FAILED":
                    self.fail("Async action failed")
            else:
                self.fail("Async action did not complete after max attempts")
        finally:
            if os.path.exists(csv_path):
                os.remove(csv_path)


if __name__ == "__main__":
    unittest.main()
