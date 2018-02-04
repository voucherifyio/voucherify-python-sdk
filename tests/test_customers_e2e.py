from voucherify import Client as voucherifyClient

"""
Initialization
"""
voucherify = voucherifyClient(
    application_id="c70a6f00-cf91-4756-9df5-47628850002b",
    client_secret_key="3266b9f8-e246-4f79-bdf0-833929b1380c"
)


def test_customerCRUD():
    payload = {
        "name": "John Doe",
        "email": "john@email.com",
        "description": "Sample description of customer",
        "metadata": {
            "lang": "en"
        }
    }

    result = voucherify.customers.create(payload)
# create
    assert result.get('description') == payload.get('description')
    assert result.get('email') == payload.get('email')
# retrieve
    customer = voucherify.customers.get(result.get('id'))
    assert customer.get('description') == result.get('description')
    assert customer.get('email') == result.get('email')
# update
    updatePayload = {
        "id": customer.get('id'),
        "description": 'changed description for customer'
    }
    updatedCustomer = voucherify.customers.update(updatePayload)
    assert updatedCustomer.get('description') == updatePayload.get('description')
# delete
    voucherify.customers.delete(updatedCustomer.get('id'))
    result = voucherify.customers.get(updatedCustomer.get('id'))
    assert result.get('code') == 404
