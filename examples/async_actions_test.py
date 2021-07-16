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
Get Async Action
"""
result = voucherify.asyncActions.get("id")
pprint.pprint("--- Get Async Action ---")
pprint.pprint(result)

waitForInput(args.wait)

"""
List Async Actions
"""
params = {
    "limit": 5,
    "end_date": "2021-07-16T15:36:26Z"
}

result = voucherify.asyncActions.list(params)
pprint.pprint("--- List Async Actions ---")
pprint.pprint(result)

waitForInput(args.wait)
