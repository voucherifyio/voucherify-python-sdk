import sys
import os
import unittest
import random
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../"))
import voucherify as voucherifyClient
import spec_utils

random_code = random.randint(0, 10000000)

customer_source_id = "test_customer_" + str(random_code)

HAS_CREDENTIALS = (
    hasattr(spec_utils, "configuration") and spec_utils.configuration is not None
)


class TestCustomerSDK(unittest.TestCase):

    delay = 2

    def setUp(self):
        if not HAS_CREDENTIALS:
            self.fail("Client credentials not provided")
        self.created_customers = []

    def tearDown(self):
        if HAS_CREDENTIALS:
            with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
                customers_api = voucherifyClient.CustomersApi(api_client)
                for customer in getattr(self, "created_customers", []):
                    try:
                        customers_api.delete_customer(customer.id)
                    except voucherifyClient.ApiException as e:
                        if e.status == 404:
                            # customer already deleted, ignore
                            continue
                        print(f"Failed to delete customer {customer.id}: {e}")

    def test_01_create_customer_basic(self):
        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            api_instance = voucherifyClient.CustomersApi(api_client)
            try:
                result = api_instance.create_customer(
                    voucherifyClient.CustomersCreateRequestBody(
                        source_id=customer_source_id
                    )
                )
                self.created_customers.append(result)
                self.assertIsNotNone(result)
            except voucherifyClient.ApiException as e:
                self.fail(e)

    def test_02_create_and_delete_customer(self):
        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            customers_api = voucherifyClient.CustomersApi(api_client)

            customer_body = voucherifyClient.CustomersCreateRequestBody(
                source_id=f"Customer_{random.randint(0, 1000000)}",
                name="Test User",
                email=f"test_{random.randint(0,1000000)}@example.com",
            )
            created_customer = customers_api.create_customer(customer_body)
            self.created_customers.append(created_customer)

            self.assertIsNotNone(created_customer)
            self.assertIsNotNone(created_customer.id)

            time.sleep(self.delay)

            customers_api.delete_customer(created_customer.id)

            with self.assertRaises(voucherifyClient.ApiException):
                customers_api.get_customer(created_customer.id)


if __name__ == "__main__":
    unittest.main()
