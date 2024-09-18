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
    def test_01_import_products(self):
        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            api_instance = voucherifyClient.ProductsApi(api_client)

            try:
                file_path = os.path.join(os.path.dirname(__file__), './products_voucherify.csv')
                result = api_instance.import_products_using_csv(file_path)

                self.assertIsNotNone(result.async_action_id)

            except voucherifyClient.ApiException as e:
                self.fail(e)


if __name__ == '__main__':
    unittest.main()
