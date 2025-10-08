import sys
import os
import unittest
import random
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../"))

import voucherify as voucherifyClient
import spec_utils

random_code = random.randint(0, 10000000)
product_name = "test_product_" + str(random_code)
sku_name = "test_sku_" + str(random_code)


class TestProductsSDK(unittest.TestCase):
    delay = 3

    def setUp(self):
        if not hasattr(spec_utils, "configuration") or spec_utils.configuration is None:
            raise RuntimeError(
                "Client credentials not provided in spec_utils.configuration"
            )
        self.created_products = []

    def tearDown(self):
        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            products_api = voucherifyClient.ProductsApi(api_client)
            for product in getattr(self, "created_products", []):
                try:
                    products_api.delete_product(product.id)
                except voucherifyClient.ApiException as e:
                    if e.status != 404:
                        print(f"Failed to delete product {product.id}: {e}")

    def test_01_create_and_get_product(self):
        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            api_instance = voucherifyClient.ProductsApi(api_client)
            product = api_instance.create_product(
                voucherifyClient.ProductsCreateRequestBody(
                    name=product_name, price=20000
                )
            )
            self.created_products.append(product)

            self.assertIsNotNone(product)
            self.assertIsNotNone(product.id)

            time.sleep(self.delay)
            fetched = api_instance.get_product(product.id)
            self.assertIsNotNone(fetched)
            self.assertEqual(fetched.id, product.id)

    def test_02_update_product(self):
        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            api_instance = voucherifyClient.ProductsApi(api_client)
            product = api_instance.create_product(
                voucherifyClient.ProductsCreateRequestBody(
                    name=product_name, price=20000
                )
            )
            self.created_products.append(product)
            time.sleep(self.delay)

            updated_product = api_instance.update_product(
                product.id, voucherifyClient.ProductsUpdateRequestBody(price=55000)
            )
            self.assertIsNotNone(updated_product)
            self.assertEqual(updated_product.price, 55000)

    def test_03_list_products(self):
        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            api_instance = voucherifyClient.ProductsApi(api_client)

            p1 = api_instance.create_product(
                voucherifyClient.ProductsCreateRequestBody(
                    name=product_name + "_1", price=60000
                )
            )
            p2 = api_instance.create_product(
                voucherifyClient.ProductsCreateRequestBody(
                    name=product_name + "_2", price=60000
                )
            )
            self.created_products.extend([p1, p2])
            time.sleep(self.delay)

            products = api_instance.list_products()
            self.assertIsNotNone(products)
            self.assertGreaterEqual(len(products.products), 2)

    def test_04_update_products_in_bulk(self):
        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            api_instance = voucherifyClient.ProductsApi(api_client)
            async_action = api_instance.update_products_in_bulk()
            self.assertIsNotNone(async_action)

    def test_05_update_metadata_in_bulk(self):
        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            api_instance = voucherifyClient.ProductsApi(api_client)

            p1 = api_instance.create_product(
                voucherifyClient.ProductsCreateRequestBody(
                    name=product_name + "_1", price=20000
                )
            )
            p2 = api_instance.create_product(
                voucherifyClient.ProductsCreateRequestBody(
                    name=product_name + "_2", price=20000
                )
            )
            self.created_products.extend([p1, p2])
            time.sleep(self.delay)

            async_action = api_instance.update_products_metadata_in_bulk(
                voucherifyClient.ProductsMetadataUpdateInBulkRequestBody(
                    product_ids=[p1.id, p2.id]
                )
            )
            self.assertIsNotNone(async_action)

    def test_06_create_and_update_sku(self):
        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            api_instance = voucherifyClient.ProductsApi(api_client)

            product = api_instance.create_product(
                voucherifyClient.ProductsCreateRequestBody(
                    name=product_name, price=20000
                )
            )
            self.created_products.append(product)
            time.sleep(self.delay)

            sku = api_instance.create_sku(
                product.id,
                voucherifyClient.ProductsSkusCreateRequestBody(
                    name=sku_name, price=5000
                ),
            )
            self.assertIsNotNone(sku)
            self.assertIsNotNone(sku.id)

            time.sleep(self.delay)
            updated_sku = api_instance.update_sku(
                product.id,
                sku.id,
                voucherifyClient.ProductsSkusUpdateRequestBody(price=2000),
            )
            self.assertIsNotNone(updated_sku)
            self.assertEqual(updated_sku.price, 2000)

            api_instance.delete_sku(product.id, sku.id)

    def test_07_get_and_list_skus(self):
        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            api_instance = voucherifyClient.ProductsApi(api_client)

            product = api_instance.create_product(
                voucherifyClient.ProductsCreateRequestBody(
                    name=product_name, price=20000
                )
            )
            self.created_products.append(product)

            sku = api_instance.create_sku(
                product.id,
                voucherifyClient.ProductsSkusCreateRequestBody(
                    name=sku_name, price=5000
                ),
            )
            time.sleep(self.delay)

            fetched_sku = api_instance.get_sku(sku.id)
            self.assertIsNotNone(fetched_sku)
            self.assertEqual(fetched_sku.id, sku.id)

            skus = api_instance.list_skus_in_product(product.id)
            self.assertIsNotNone(skus)
            self.assertGreaterEqual(len(skus.skus), 1)

            api_instance.delete_sku(product.id, sku.id)

    def test_08_delete_product(self):
        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            api_instance = voucherifyClient.ProductsApi(api_client)

            product = api_instance.create_product(
                voucherifyClient.ProductsCreateRequestBody(
                    name=product_name, price=20000
                )
            )
            time.sleep(self.delay)
            api_instance.delete_product(product.id)

            with self.assertRaises(voucherifyClient.ApiException):
                api_instance.get_product(product.id)

    def test_09_delete_sku(self):
        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            api_instance = voucherifyClient.ProductsApi(api_client)

            product = api_instance.create_product(
                voucherifyClient.ProductsCreateRequestBody(
                    name=product_name, price=20000
                )
            )
            self.created_products.append(product)

            sku = api_instance.create_sku(
                product.id,
                voucherifyClient.ProductsSkusCreateRequestBody(
                    name=sku_name, price=5000
                ),
            )
            time.sleep(self.delay)
            api_instance.delete_sku(product.id, sku.id)

            with self.assertRaises(voucherifyClient.ApiException):
                api_instance.get_sku(sku.id)

    def test_10_import_products(self):
        with voucherifyClient.ApiClient(spec_utils.configuration) as api_client:
            api_instance = voucherifyClient.ProductsApi(api_client)

            file_path = os.path.join(
                os.path.dirname(__file__), "./products_voucherify.csv"
            )
            result = api_instance.import_products_using_csv(file_path)
            self.assertIsNotNone(result.async_action_id)


if __name__ == "__main__":
    unittest.main()
