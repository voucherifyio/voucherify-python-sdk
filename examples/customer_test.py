import pprint

from voucherify import Client as voucherifyClient

"""
Initialization
"""
voucherify = voucherifyClient(
    application_id="c70a6f00-cf91-4756-9df5-47628850002b",
    client_secret_key="3266b9f8-e246-4f79-bdf0-833929b1380c"
)

"""
Create Customer
"""
payload = {
    "name": "John Doe",
    "email": "john@email.com",
    "description": "Sample description of customer",
    "metadata": {
        "lang": "en"
    }
}

result = voucherify.customer.create(payload)
pprint.pprint("--- Create ---")
pprint.pprint(result)

"""
Fetch Customer
"""
result = voucherify.customer.fetch(result.get("id"))
pprint.pprint("--- Fetch ---")
pprint.pprint(result)

"""
Update Customer
"""
payload = result
payload['description'] = "Sample description of customer with changes"

result = voucherify.customer.update(payload)
pprint.pprint("--- Update ---")
pprint.pprint(result)

"""
Delete Customer
"""
result = voucherify.customer.delete(result["id"])
pprint.pprint("--- Delete ---")
pprint.pprint(result)
