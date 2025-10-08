import sys
import os
import unittest
import random

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../"))

import voucherify as voucherifyClient
import spec_utils

random_code = random.randint(0, 10000000)
customer_name = f"Customer_{random_code}"
customer_email = f"customer_{random_code}@example.com"
campaign_name = f"Campaign_{random_code}"
campaign_name_2 = f"Campaign_2_{random_code}"
campaign_name_3 = f"Campaign_3_{random_code}"
campaign_name_4 = f"Campaign_4_{random_code}"
voucher_code = "test_code_" + str(random_code)


HAS_CREDENTIALS = (
    hasattr(spec_utils, "configuration") and spec_utils.configuration is not None
)


class TestCampaignSDK(unittest.TestCase):
    delay = 3
    vouchers_count = 3

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
                    except Exception:
                        pass
                for customer in self.created_customers:
                    try:
                        customers_api.delete_customer(customer.id)
                    except Exception:
                        pass

    def test_01_publish_campaign_voucher(self):
        if not HAS_CREDENTIALS:
            raise RuntimeError("Client credentials not provided")

        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            campaigns_api = voucherifyClient.CampaignsApi(api_client)
            customers_api = voucherifyClient.CustomersApi(api_client)
            publications_api = voucherifyClient.PublicationsApi(api_client)

            # Step 1: Create a campaign with discount vouchers
            campaign_body = voucherifyClient.CampaignsCreateRequestBody(
                name=campaign_name,
                voucher=voucherifyClient.CampaignsCreateRequestBodyVoucher(
                    type="DISCOUNT_VOUCHER",
                    discount=voucherifyClient.Discount(type="AMOUNT", amount_off=1000),
                ),
            )
            campaign = campaigns_api.create_campaign(campaign_body)
            self.created_campaigns.append(campaign)

            # Assertions on campaign
            self.assertIsNotNone(campaign)
            self.assertEqual(campaign.name, campaign_name)
            self.assertTrue(campaign.id is not None and campaign.id != "")

            # Step 2: Add vouchers to the campaign
            first_voucher = campaigns_api.add_vouchers_to_campaign(campaign.id)
            self.assertIsNotNone(first_voucher)
            self.assertTrue(first_voucher.code is not None and first_voucher.code != "")

            bundle = campaigns_api.add_vouchers_to_campaign(
                campaign.id, vouchers_count=self.vouchers_count
            )
            self.assertIsNotNone(bundle)
            self.assertIsNotNone(bundle.async_action_id)

            # Step 3: Create a customer
            customer_body = voucherifyClient.CustomersCreateRequestBody(
                name=customer_name, email=customer_email
            )
            customer = customers_api.create_customer(customer_body)
            self.created_customers.append(customer)

            self.assertIsNotNone(customer)
            self.assertEqual(customer.name, customer_name)
            self.assertEqual(customer.email, customer_email)
            self.assertTrue(customer.id is not None and customer.id != "")

            # Step 4: Create a publication for the first voucher
            publication_body = voucherifyClient.PublicationsCreateRequestBody(
                voucher=first_voucher.code,
                customer=voucherifyClient.Customer(id=customer.id),
                channel=None,
                campaign=None,
                metadata=None,
            )

            publication = publications_api.create_publication(
                publications_create_request_body=publication_body,
                join_once=False,
            )
            self.assertIsNotNone(publication)
            self.assertTrue(publication.id is not None and publication.id != "")

    def test_02_create_campaign_and_add_vouchers_basic(self):
        if not HAS_CREDENTIALS:
                    raise RuntimeError("Client credentials not provided")

        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            api_instance = voucherifyClient.CampaignsApi(api_client)
            try:
                campaigns_create_request_body = (
                    voucherifyClient.CampaignsCreateRequestBody(
                        name=campaign_name_2,
                        voucher=voucherifyClient.CampaignsCreateRequestBodyVoucher(
                            type="DISCOUNT_VOUCHER",
                            discount=voucherifyClient.Discount(
                                type="AMOUNT", amount_off=1000
                            ),
                        ),
                        metadata={"mandatory_v": "test"}
                    )
                )
                campaign = api_instance.create_campaign(campaigns_create_request_body)
                self.created_campaigns.append(campaign)
                async_action_id = api_instance.add_vouchers_to_campaign(
                    campaign.id, vouchers_count=5
                ).async_action_id
                campaigns_vouchers_create_response_body = (
                    api_instance.add_vouchers_to_campaign(campaign.id)
                )
                campaigns_vouchers_specific_code_create_response_body = (
                    api_instance.add_voucher_with_specific_code_to_campaign(
                        campaign.id, voucher_code
                    )
                )

                self.assertIsNotNone(async_action_id)
                self.assertIsNotNone(campaigns_vouchers_create_response_body)
                self.assertIsNotNone(
                    campaigns_vouchers_specific_code_create_response_body
                )
            except voucherifyClient.ApiException as e:
                self.fail(e)

    def test_03_add_vouchers_to_campaign(self):
        if not HAS_CREDENTIALS:
                    raise RuntimeError("Client credentials not provided")

        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            campaigns_api = voucherifyClient.CampaignsApi(api_client)

            campaign_body = voucherifyClient.CampaignsCreateRequestBody(
                name=campaign_name_3,
                voucher=voucherifyClient.CampaignsCreateRequestBodyVoucher(
                    type="DISCOUNT_VOUCHER",
                    discount=voucherifyClient.Discount(type="AMOUNT", amount_off=1000),
                ),
            )
            campaign = campaigns_api.create_campaign(campaign_body)
            self.created_campaigns.append(campaign)

            self.assertIsNotNone(campaign)
            self.assertEqual(campaign.name, campaign_name_3)

            single_voucher = campaigns_api.add_vouchers_to_campaign(campaign.id)
            self.assertIsNotNone(single_voucher)
            self.assertIsNotNone(single_voucher.code)
            self.assertEqual(single_voucher.campaign_id, campaign.id)

            bundle = campaigns_api.add_vouchers_to_campaign(
                campaign.id, vouchers_count=5
            )
            self.assertIsNotNone(bundle)
            self.assertIsNotNone(bundle.async_action_id)

            all_voucher_codes = [single_voucher.code] + [
                f"generated_code_{i}" for i in range(5)
            ]
            self.assertEqual(len(all_voucher_codes), 6)

    def test_04_update_expiration_date_in_campaign(self):
        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            campaigns_api = voucherifyClient.CampaignsApi(api_client)
            expiration_date = "2090-10-08T12:57:09.386Z"

            campaign_body = voucherifyClient.CampaignsCreateRequestBody(
                name=campaign_name_4,
                voucher=voucherifyClient.CampaignsCreateRequestBodyVoucher(
                    type="DISCOUNT_VOUCHER",
                    discount=voucherifyClient.Discount(type="AMOUNT", amount_off=1000),
                ),
                expiration_date=expiration_date
            )
            campaign = campaigns_api.create_campaign(campaign_body)
            self.assertIsNotNone(campaign.expiration_date)

            update_campaign_body = voucherifyClient.CampaignsUpdateRequestBody(
                expiration_date=None
            )
            updated_campaign = campaigns_api.update_campaign(campaign.id, update_campaign_body)
            self.assertIsNone(updated_campaign.expiration_date)

if __name__ == "__main__":
    unittest.main()
