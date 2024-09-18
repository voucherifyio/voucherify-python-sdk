import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../'))

import spec_utils
import unittest
import responses
import voucherify as voucherifyClient
from pprint import pprint
import random
import spec_utils
import time

voucher_code=None
random_code = random.randint(0, 10000000)
email = "voucherify+" + str(random_code) + "@example.com"
campaign_name = "test_campaign_" + str(random_code)

class TestYourSDK(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestYourSDK, self).__init__(*args, **kwargs)

    @responses.activate
    def test_01_test_publications(self):
        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            campaigns_api_instance = voucherifyClient.CampaignsApi(api_client)
            publications_api_instance = voucherifyClient.PublicationsApi(api_client)

            campaigns_create_request_body = voucherifyClient.CampaignsCreateRequestBody(
                name=campaign_name,
                type='AUTO_UPDATE',
                voucher=voucherifyClient.CampaignsCreateRequestBodyVoucher(
                    type="DISCOUNT_VOUCHER",
                    discount=voucherifyClient.Discount(
                        type="AMOUNT",
                        amount_off=1000
                    )
                ),
                metadata={
                    "mandatory_v": "test"
                }
            )
            campaigns_api_instance.create_campaign(campaigns_create_request_body)
            publication = publications_api_instance.create_publication(
                True,
                voucherifyClient.PublicationsCreateRequestBody(
                    campaign=voucherifyClient.CreatePublicationCampaign(name=campaign_name),
                    customer=voucherifyClient.PublicationsCreateRequestBodyCustomer(
                        email=email
                    )
                )
            )
            self.assertIsNotNone(publication.id)


if __name__ == '__main__':
    unittest.main()
