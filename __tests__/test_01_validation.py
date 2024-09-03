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

random_code = random.randint(0, 10000000)
voucher_code = "test_code_" + str(random_code)
campaign_name = "test_campaign_" + str(random_code)
customer_source_id = "test_customer_" + str(random_code)

class TestYourSDK(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestYourSDK, self).__init__(*args, **kwargs)

    @responses.activate
    def test_01_add_vouchers_to_campaign(self):
        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            api_instance = voucherifyClient.CampaignsApi(api_client)

            try:
                campaigns_create_request_body = voucherifyClient.CampaignsCreateRequestBody(
                    name=campaign_name,
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
                campaign = api_instance.create_campaign(campaigns_create_request_body)

                async_action_id = api_instance.add_vouchers_to_campaign(campaign.id, vouchers_count=5).async_action_id
                campaigns_vouchers_create_response_body = api_instance.add_vouchers_to_campaign(campaign.id)
                campaigns_vouchers_specific_code_create_response_body = api_instance.add_voucher_with_specific_code_to_campaign(campaign.id, voucher_code)

                self.assertIsNotNone(async_action_id)
                self.assertIsNotNone(campaigns_vouchers_create_response_body)
                self.assertIsNotNone(campaigns_vouchers_specific_code_create_response_body)

            except voucherifyClient.ApiException as e:
                self.fail(e)

    @responses.activate
    def test_02_create_customer(self):
        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            api_instance = voucherifyClient.CustomersApi(api_client)

            try:
                result = api_instance.create_customer(voucherifyClient.CustomersCreateRequestBody(
                    source_id=customer_source_id
                ))
                self.assertIsNotNone(result)

            except voucherifyClient.ApiException as e:
                self.fail(e)

    @responses.activate
    def test_03_validate_stacked_discounts(self):
        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            api_instance = voucherifyClient.ValidationsApi(api_client)

            try:
                validations_validate_request_body = voucherifyClient.ValidationsValidateRequestBody(
                    redeemables=[voucherifyClient.ValidationsValidateRequestBodyRedeemablesItem(
                        id=voucher_code,
                        object='voucher'
                    )],
                    customer=voucherifyClient.Customer(
                        source_id=customer_source_id
                    ),
                    order=voucherifyClient.Order(
                        amount=30000,
                        metadata={
                            "key_customer": "test"
                        }
                    ),
                    metadata={
                        "key": "value"
                    }
                )
                result = api_instance.validate_stacked_discounts(validations_validate_request_body)
                self.assertIsNotNone(result)
                self.assertEqual(result.valid, True)

            except voucherifyClient.ApiException as e:
                self.fail(e)


if __name__ == '__main__':
    unittest.main()
