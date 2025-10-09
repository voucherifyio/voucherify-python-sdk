import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../"))
import random
import unittest
import voucherify as voucherifyClient
import spec_utils

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../"))

random_code = random.randint(0, 10000000)
email = f"voucherify+{random_code}@example.com"
campaign_name = f"test_campaign_{random_code}"


class TestPublicationsSDK(unittest.TestCase):
    def setUp(self):
        self.created_campaigns = []

    def tearDown(self):
        if hasattr(spec_utils, "configuration") and spec_utils.configuration:
            with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
                campaigns_api_instance = voucherifyClient.CampaignsApi(api_client)

                for campaign in getattr(self, "created_campaigns", []):
                    try:
                        campaigns_api_instance.delete_campaign(campaign.id)
                    except voucherifyClient.ApiException as e:
                        if e.status != 404:
                            print(f"Failed to delete campaign {campaign.id}: {e}")

    def test_01_test_publications(self):
        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            campaigns_api_instance = voucherifyClient.CampaignsApi(api_client)
            publications_api_instance = voucherifyClient.PublicationsApi(api_client)

            campaigns_create_request_body = voucherifyClient.CampaignsCreateRequestBody(
                name=campaign_name,
                type="AUTO_UPDATE",
                voucher=voucherifyClient.CampaignsCreateRequestBodyVoucher(
                    type="DISCOUNT_VOUCHER",
                    discount=voucherifyClient.Discount(type="AMOUNT", amount_off=1000),
                ),
                metadata={"mandatory_v": "test"},
            )
            campaign = campaigns_api_instance.create_campaign(campaigns_create_request_body)
            self.created_campaigns.append(campaign)

            publication_request_body = voucherifyClient.PublicationsCreateRequestBody(
                campaign=voucherifyClient.CreatePublicationCampaign(name=campaign_name),
                customer=voucherifyClient.Customer(email=email),
            )
            publication = publications_api_instance.create_publication(True, publication_request_body)

            self.assertIsNotNone(publication.id)


if __name__ == "__main__":
    unittest.main()
