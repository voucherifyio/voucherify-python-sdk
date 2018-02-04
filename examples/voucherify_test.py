import pprint
from example_utils import getArgs, waitForInput

from voucherify import Client as voucherifyClient
from voucherify import utils

args = getArgs()

"""
Initialization
"""
voucherify = voucherifyClient(
    application_id="c70a6f00-cf91-4756-9df5-47628850002b",
    client_secret_key="3266b9f8-e246-4f79-bdf0-833929b1380c"
)

tracking_id = "PythonTestUser"
voucher = {
    "code": "PythonVoucherTest",
    "discount": {
        "type": "AMOUNT",
        "amount_off": 12436
    },
    "category": "PythonTestCategory",
    "start_date": "2016-01-01T00:00:00Z",
    "expiration_date": None,
    "redemption": {
        "quantity": None,
        "redeemed_quantity": 0
    },
    "active": True
}

"""
Create voucher
"""
pprint.pprint("=== Create voucher ===")
new_voucher = voucherify.vouchers.create(voucher)
pprint.pprint(new_voucher)

waitForInput(args.wait)

"""
Get voucher
"""
pprint.pprint("=== Get voucher ===")
voucher = voucherify.vouchers.get(voucher["code"])
pprint.pprint(voucher)

waitForInput(args.wait)

"""
List vouchers from category
"""
pprint.pprint("=== List vouchers from category ===")
filter_params = {
    "limit": 10,
    "skip": 20,
    "category": "PythonTestCategory"
}
vouchers_list = voucherify.vouchers.list(filter_params)
pprint.pprint(vouchers_list)

waitForInput(args.wait)

"""
Disable Voucher
"""
pprint.pprint("=== Disable Voucher ===")
result = voucherify.vouchers.disable(voucher["code"])
pprint.pprint(result)

waitForInput(args.wait)

pprint.pprint("=== Disable not existing Voucher ===")
result = voucherify.vouchers.disable("TotallyRandomVoucher")
pprint.pprint(result)

waitForInput(args.wait)

"""
Enable Voucher
"""
pprint.pprint("=== Enable Voucher ===")
result = voucherify.vouchers.enable(voucher["code"])
pprint.pprint(result)

waitForInput(args.wait)

pprint.pprint("=== Disable not existing Voucher ===")
result = voucherify.vouchers.enable("TotallyRandomVoucher")
pprint.pprint(result)

waitForInput(args.wait)

"""
Redeem Voucher
"""
pprint.pprint("=== Redeem Voucher ===")
result = voucherify.redemptions.redeem(voucher["code"])
redemption_id = result['id']
pprint.pprint(result)

waitForInput(args.wait)

pprint.pprint("=== Redeem Voucher with Tracking ID ===")
result = voucherify.redemptions.redeem(voucher["code"], tracking_id)
pprint.pprint(result)

waitForInput(args.wait)

pprint.pprint("=== Redeem Voucher with Customer Info ===")
customer = {
    "source_id": "alice.morgan",
    "name": "Alice Morgan",
    "email": "alice@morgan.com",
    "description": "",
    "metadata": {
        "locale": "en-GB",
        "shoeSize": 5,
        "favourite_brands": ["Armani", "L'Autre Chose", "Vicini"]
    }
}
payload = {
    "voucher": voucher['code'],
    "customer": customer
}
result = voucherify.redemptions.redeem(payload)
pprint.pprint(result)

waitForInput(args.wait)

"""
Redemption Voucher
"""
pprint.pprint("=== Redemption Voucher ===")
redemptions_voucher_list = voucherify.redemptions.getForVoucher(voucher["code"])
pprint.pprint(redemptions_voucher_list)

waitForInput(args.wait)

"""
Redemptions List
"""
pprint.pprint("=== Redemptions Voucher ===")
filter_params = {
    "limit": 1,
    "page": 0,
    "[created_at][before]": "2016-12-31T23:59:59Z",
    "[created_at][after]": "2015-01-01T00:00:00Z",
    "result": "SUCCESS"
}
redemptions_list = voucherify.redemptions.list(filter_params)
pprint.pprint(redemptions_list)

waitForInput(args.wait)

"""
Rollback Voucher
"""
pprint.pprint("=== Rollback Redemption ===")
rollback_reason = "Wrong Customer"
result = voucherify.redemptions.rollback(redemption_id, rollback_reason)
pprint.pprint(result)

waitForInput(args.wait)

"""
Publish Voucher
"""
pprint.pprint("=== Publish Voucher with customer details and channel ===")
payload = {
    "channel": "Email",
    "customer": "donny.roll@mail.com"
}
result = voucherify.distributions.publish(payload)
pprint.pprint(result)

waitForInput(args.wait)

"""
Utils
"""
pprint.pprint("=== Calculate Discount Amount and Price after discount===")

unit_price = 83.45
items_count = 13
base_price = unit_price * items_count

discount = utils.calculate_discount(base_price, voucher, unit_price)
new_price = utils.calculate_price(base_price, voucher, unit_price)
pprint.pprint(unit_price)
pprint.pprint(items_count)
pprint.pprint(base_price)
pprint.pprint(new_price)
pprint.pprint(discount)
