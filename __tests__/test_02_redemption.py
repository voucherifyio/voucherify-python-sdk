import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../'))

import unittest
import responses
import voucherify as voucherifyClient
import spec_utils
from pprint import pprint
import random
import time

random_code = random.randint(0, 10000000)
voucher_code = "test_code_" + str(random_code)
campaign_name = "test_campaign_" + str(random_code)
customer_source_id = "test_customer_" + str(random_code)
redemption_id = None
customer_metadata = {
    "key_customer": "test"
}

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

                async_action = api_instance.add_vouchers_to_campaign(campaign.id, 5)
                campaigns_vouchers_create_response_body = api_instance.add_vouchers_to_campaign(campaign.id)
                campaigns_vouchers_specific_code_create_response_body = api_instance.add_voucher_with_specific_code_to_campaign(campaign.id, voucher_code)

                self.assertIsNotNone(async_action)
                self.assertIsNotNone(campaigns_vouchers_create_response_body)
                self.assertIsNotNone(campaigns_vouchers_specific_code_create_response_body)

            except voucherifyClient.ApiException as e:
                self.fail(e)

    @responses.activate
    def test_02_redeem_stacked_discounts(self):
        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            api_instance = voucherifyClient.RedemptionsApi(api_client)

            try:
                redemptions_redeem_request_body = voucherifyClient.RedemptionsRedeemRequestBody(
                    redeemables=[voucherifyClient.RedemptionsRedeemRequestBodyRedeemablesItem(
                        id=voucher_code,
                        object='voucher'
                    )],
                    customer=voucherifyClient.Customer(
                        source_id=customer_source_id,
                        metadata=customer_metadata
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
                result = api_instance.redeem_stacked_discounts(redemptions_redeem_request_body)
                self.assertIsNotNone(result)
                self.assertEqual(result.redemptions[0].result, 'SUCCESS')

            except voucherifyClient.ApiException as e:
                self.fail(e)

    @responses.activate
    def test_03_get_customer(self):
        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            api_instance = voucherifyClient.CustomersApi(api_client)

            try:
                time.sleep(1)
                result = api_instance.get_customer(customer_source_id)
                self.assertIsNotNone(result)
                self.assertEqual(result.metadata, customer_metadata)

            except voucherifyClient.ApiException as e:
                self.fail(e)

    @responses.activate
    def test_04_list_redemptions(self):
        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            api_instance = voucherifyClient.RedemptionsApi(api_client)

            list_redemptions_filters = voucherifyClient.ParameterFiltersListRedemptions(
                        voucher_code=voucherifyClient.ParameterFiltersListRedemptionsVoucherCode(
                            conditions=voucherifyClient.FilterConditionsString(
                                is_not=voucher_code
                            )
                        )
                    )
            try:
                result = api_instance.list_redemptions(
                    100,
                    None,None,None,None,None,None,
                    list_redemptions_filters
                )
                self.assertEqual(result.object, 'list')
            except voucherifyClient.ApiException as e:
                self.fail(e)


if __name__ == '__main__':
    unittest.main()
