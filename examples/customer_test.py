import pprint
from example_utils import getArgs, waitForInput

from voucherify import Client as voucherifyClient

args = getArgs()

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

result = voucherify.customers.create(payload)
pprint.pprint("--- Create ---")
pprint.pprint(result)


waitForInput(args.wait)


"""
Get Customer
"""
result = voucherify.customers.get(result.get("id"))
pprint.pprint("--- Get customer ---")
pprint.pprint(result)

waitForInput(args.wait)

"""
Update Customer
"""
payload = result
payload['description'] = "Sample description of customer with changes"

result = voucherify.customers.update(payload)
pprint.pprint("--- Update ---")
pprint.pprint(result)

waitForInput(args.wait)

"""
Delete Customer
"""
result = voucherify.customers.delete(result["id"])
result = pprint.pprint("--- Delete ---")
pprint.pprint(result)
