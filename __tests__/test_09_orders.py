import sys
import os
import unittest
import time
import random

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../"))
import voucherify as voucherifyClient
from __tests__ import spec_utils


HAS_CREDENTIALS = (
    hasattr(spec_utils, "configuration") and spec_utils.configuration is not None
)


class TestOrdersSDK(unittest.TestCase):
    def setUp(self):
        if not HAS_CREDENTIALS:
            self.fail("Client credentials not provided")
        self.created_orders = []

    def test_01_create_order(self):
        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            orders_api = voucherifyClient.OrdersApi(api_client)

            order_body = voucherifyClient.OrdersCreateRequestBody(
                amount=1000,
                currency="USD",
                customer=voucherifyClient.Customer(
                    name="Test Customer",
                    email=f"customer_{random.randint(0,100000)}@example.com",
                ),
                source_id=f"order_{random.randint(0,100000)}",
            )
            created_order = orders_api.create_order(order_body)
            self.created_orders.append(created_order)

            self.assertIsNotNone(created_order)
            self.assertIsNotNone(created_order.id)
            self.assertEqual(created_order.status, "CREATED")

            time.sleep(2)

            order = orders_api.get_order(created_order.id)
            self.assertIsNotNone(order)
            self.assertEqual(order.id, created_order.id)
            self.assertEqual(order.status, "CREATED")

    def test_02_update_order(self):
        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            orders_api = voucherifyClient.OrdersApi(api_client)

            order_body = voucherifyClient.OrdersCreateRequestBody(
                amount=1500,
                currency="USD",
                customer=voucherifyClient.Customer(
                    name="Update Customer",
                    email=f"update_{random.randint(0,100000)}@example.com",
                ),
                source_id=f"order_{random.randint(0,100000)}",
            )
            created_order = orders_api.create_order(order_body)
            self.created_orders.append(created_order)
            self.assertIsNotNone(created_order.id)

            time.sleep(2)

            update_body = voucherifyClient.OrdersUpdateRequestBody(status="PAID")
            updated_order = orders_api.update_order(created_order.id, update_body)

            self.assertIsNotNone(updated_order)
            self.assertEqual(updated_order.id, created_order.id)
            self.assertEqual(updated_order.status, "PAID")

    def test_03_list_orders(self):
        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            orders_api = voucherifyClient.OrdersApi(api_client)

            orders = orders_api.list_orders(limit=10)

            self.assertIsNotNone(orders)
            self.assertIsNotNone(orders.orders)
            self.assertGreaterEqual(len(orders.orders), 1)
            self.assertLessEqual(len(orders.orders), 10)


if __name__ == "__main__":
    unittest.main()
