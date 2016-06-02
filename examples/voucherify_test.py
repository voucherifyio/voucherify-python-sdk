import voucherify
import pprint

'''
Initialization
'''
client = voucherify.Client(
    application_id='c70a6f00-cf91-4756-9df5-47628850002b',
    client_secret_key='3266b9f8-e246-4f79-bdf0-833929b1380c'
)

voucher = {
    'code': 'PyThonTeSt',
    'discount': {
        'type': 'AMOUNT',
        'amount_off': 1000
    },
    'category': 'PythonTest',
    'start_date': '2016-01-01T00:00:00Z',
    'active': True
}

'''
Create voucher
'''

pprint.pprint('=== Create voucher ===')
result = client.create(voucher)
pprint.pprint(result)

'''
Get voucher
'''

pprint.pprint('=== Get voucher ===')
voucher = client.get(voucher['code'])
pprint.pprint(voucher)

'''
Utils
'''

pprint.pprint('=== Calculate Discount Amount and Price after discount===')

unit_price = 83.45
items_count = 13
base_price = unit_price * items_count

discount = voucherify.utils.calculate_discount(base_price, voucher, unit_price)
new_price = voucherify.utils.calculate_price(base_price, voucher, unit_price)
pprint.pprint(unit_price)
pprint.pprint(items_count)
pprint.pprint(base_price)
pprint.pprint(new_price)
pprint.pprint(discount)
