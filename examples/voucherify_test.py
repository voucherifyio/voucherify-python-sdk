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

'''
Validate voucher
'''
