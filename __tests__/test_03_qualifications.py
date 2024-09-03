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

class TestYourSDK(unittest.TestCase):
    @classmethod
    @responses.activate
    def setUpClass(cls):
        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            api_instance = voucherifyClient.QualificationsApi(api_client)

            qualifications_check_eligibility_request_body = voucherifyClient.QualificationsCheckEligibilityRequestBody(
                scenario='ALL',
                options=voucherifyClient.QualificationsOption(
                    filters=voucherifyClient.QualificationsOptionFilters(
                        resource_type=voucherifyClient.QualificationsOptionFiltersResourceType(
                            conditions=voucherifyClient.QualificationsOptionFiltersResourceTypeConditions(
                                var_in=['voucher']
                            )
                        )
                    )
                )
            )
            qualifications = api_instance.check_eligibility(qualifications_check_eligibility_request_body)
            cls.voucher_code = qualifications.redeemables.data[0].id

    @responses.activate
    def test_01_check_if_voucher_code_was_returned(self):
        self.assertIsNotNone(self.voucher_code)

    @responses.activate
    def test_02_validate_stacked_discounts(self):
        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            api_instance = voucherifyClient.ValidationsApi(api_client)

            try:
                validations_validate_request_body = voucherifyClient.ValidationsValidateRequestBody(
                    redeemables=[voucherifyClient.ValidationsValidateRequestBodyRedeemablesItem(
                        id=self.voucher_code,
                        object='voucher'
                    )],
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
