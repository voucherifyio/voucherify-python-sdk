from testUtils import getConfiguredClient

voucherify = getConfiguredClient()


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
