import pprint

from voucherify import Client as voucherifyClient
from voucherify import utils

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
new_voucher = voucherify.create(voucher)
pprint.pprint(new_voucher)

"""
Get voucher
"""
pprint.pprint("=== Get voucher ===")
voucher = voucherify.get(voucher["code"])
pprint.pprint(voucher)

"""
List vouchers from category
"""
pprint.pprint("=== List vouchers from category ===")
pprint.pprint(voucher)
filter_params = {
    "limit": 10,
    "skip": 20,
    "category": "PythonTest"
}
vouchers_list = voucherify.list(filter_params)
pprint.pprint(vouchers_list)

"""
Disable Voucher
"""
pprint.pprint("=== Disable Voucher ===")
result = voucherify.disable(voucher["code"])
pprint.pprint(result)

"""
Enable Voucher
"""
pprint.pprint("=== Enable Voucher ===")
result = voucherify.enable(voucher["code"])
pprint.pprint(result)

"""
Redeem Voucher
"""
pprint.pprint("=== Redeem Voucher ===")
result = voucherify.redeem(voucher["code"])
redemption_id = result['id']
pprint.pprint(result)

pprint.pprint("=== Redeem Voucher with Tracking ID ===")
result = voucherify.redeem(voucher["code"], tracking_id)
pprint.pprint(result)

pprint.pprint("=== Redeem Voucher with Customer Info ===")
customer = {
    "id": "alice.morgan",
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
result = voucherify.redeem(payload)
pprint.pprint(result)

"""
Redemption Voucher
"""
pprint.pprint("=== Redemption Voucher ===")
redemptions_voucher_list = voucherify.redemption(voucher["code"])
pprint.pprint(redemptions_voucher_list)

"""
Redemptions List
"""
pprint.pprint("=== Redemptions Voucher ===")
filter_params = {
    "limit": 1000,
    "page": 0,
    "start_date": "2015-01-01T00:00:00Z",
    "end_date": "2016-12-31T23:59:59Z",
    "result": "Success"
}
redemptions_list = voucherify.redemptions(filter_params)
pprint.pprint(len(redemptions_list))

"""
Rollback Voucher
"""
pprint.pprint("=== Rollback Redemption ===")
rollback_reason = "Wrong Customer"
result = voucherify.rollback(redemption_id, rollback_reason)
pprint.pprint(result)

"""
Publish Voucher
"""
pprint.pprint("=== Publish Campaign with Campaign Name ===")
result = voucherify.publish("PythonTestCampaignName")
pprint.pprint(result)

pprint.pprint("=== Publish Campaign with Campaign Details ===")
payload = {
    "campaign": "PythonTestCampaignName",
    "channel": "Email",
    "customer": "donny.roll@mail.com"
}
result = voucherify.publish(payload)
pprint.pprint(result)

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
