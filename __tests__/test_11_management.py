import unittest
import random
import time
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../"))
import voucherify as voucherifyClient
import spec_utils

HAS_MANAGEMENT_CREDENTIALS = (
    hasattr(spec_utils, "management_configuration")
    and spec_utils.management_configuration is not None
)

PROJECT_ID = getattr(spec_utils, "TEST_PROJECT_ID", None)


class TestManagementSDK(unittest.TestCase):

    delay = 2

    def setUp(self):
        self.created_schemas = []

    def tearDown(self):
        if HAS_MANAGEMENT_CREDENTIALS and PROJECT_ID:
            with voucherifyClient.ApiClient(spec_utils.management_configuration) as api_client:
                management_api = voucherifyClient.ManagementApi(api_client)
                for schema_id in getattr(self, "created_schemas", []):
                    try:
                        management_api.delete_metadata_schema(PROJECT_ID, schema_id)
                    except Exception as e:
                        print(f"Failed to delete metadata schema {schema_id}: {e}")

    def test_01_management_configuration(self):
        if not HAS_MANAGEMENT_CREDENTIALS:
            raise RuntimeError("Management credentials not provided")

        config = spec_utils.management_configuration
        if config is None or not hasattr(config, "host") or not config.host:
            raise RuntimeError("Invalid management configuration")

        print(f"Management API host: {config.host}")

    def test_02_query_projects(self):
        if not HAS_MANAGEMENT_CREDENTIALS:
            raise RuntimeError("Management credentials not provided")

        with voucherifyClient.ApiClient(
            spec_utils.management_configuration
        ) as api_client:
            management_api = voucherifyClient.ManagementApi(api_client)
            projects_response = management_api.list_projects()

            self.assertGreater(len(projects_response.data), 0)
            project = projects_response.data[0]
            self.assertIsNotNone(project.id)
            self.assertIsNotNone(project.name)
            print(f"Found {len(projects_response.data)} projects")

    def test_03_list_metadata_schemas(self):
        if not HAS_MANAGEMENT_CREDENTIALS:
            raise RuntimeError("Management credentials not provided")
        if not PROJECT_ID:
            raise RuntimeError("PROJECT_ID not provided")

        with voucherifyClient.ApiClient(
            spec_utils.management_configuration
        ) as api_client:
            management_api = voucherifyClient.ManagementApi(api_client)
            schemas = management_api.list_metadata_schemas1(PROJECT_ID)
            print(f"Found {len(schemas.data)} metadata schemas")

    def test_04_update_metadata_schema(self):
        if not HAS_MANAGEMENT_CREDENTIALS:
            raise RuntimeError("Management credentials not provided")
        if not PROJECT_ID:
            raise RuntimeError("PROJECT_ID not provided")

        with voucherifyClient.ApiClient(
            spec_utils.management_configuration
        ) as api_client:
            management_api = voucherifyClient.ManagementApi(api_client)

            schemas = management_api.list_metadata_schemas1(PROJECT_ID)
            self.assertIsNotNone(schemas)
            self.assertIsNotNone(schemas.data)
            self.assertIsInstance(schemas.data, list)
            schema_name = f"test-python-sdk-{random.randint(0,1000000)}"

            create_request = voucherifyClient.ManagementProjectsMetadataSchemasCreateRequestBody(
                related_object=schema_name,
                allow_defined_only=False,
                properties={
                    "Test": {
                        "type": "string",
                        "array": False,
                        "optional": True,
                        "eq": ["Test-01", "Test-02", "Test-03", "Test-04"],
                    }
                },
            )
            created_schema = management_api.create_metadata_schema(PROJECT_ID, create_request)
            self.created_schemas.append(created_schema.id)

            time.sleep(self.delay)
            properties = {
                f"SchemaUpdate_{random.randint(0,1000000)}": {
                    "type": "string",
                    "array": False,
                    "optional": True,
                    "eq": ["Test-01", "Test-02", "Test-03", "Test-04"],
                }
            }
            update_request = voucherifyClient.ManagementProjectsMetadataSchemasUpdateRequestBody(
                allow_defined_only=created_schema.allow_defined_only,
                properties=properties,
            )
            update_result = management_api.update_metadata_schema(
                PROJECT_ID, created_schema.id, update_request
            )
            self.assertIsNotNone(update_result)
            print(f"Successfully updated schema: {schema_name}")


if __name__ == "__main__":
    unittest.main()
