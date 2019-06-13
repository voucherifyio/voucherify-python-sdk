from voucherify import Client as voucherifyClient
import time

voucherify = voucherifyClient(
    application_id="c70a6f00-cf91-4756-9df5-47628850002b",
    client_secret_key="3266b9f8-e246-4f79-bdf0-833929b1380c"
)

    tracking_id = 'PythonTestUser'
    testVoucher = {
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


    # test redeemVoucher
    result = voucherify.redemptions.redeem(testVoucher.get('code'))
    assert result.get('result') == 'SUCCESS'
    assert result.get('voucher', {}).get('code') == testVoucher.get('code')


    # test redeemVoucherWithTrackingId
    result = voucherify.redemptions.redeem(testVoucher.get('code'), tracking_id)
    assert result.get('result') == 'SUCCESS'
    assert result.get('voucher', {}).get('code') == testVoucher.get('code')
    assert result.get('tracking_id') == tracking_id


    # test redeemVoucherWithCustomerInfo
    customer = {
        "source_id": "alice.morgan",
        "name": "Alice Morgan",
        "email": "alice@morgan.com",
        "description": "",
        "metadata": {
            "locale": "en-GB",
            "shoeSize": 5
        }
    }
    payload = {
        "voucher": testVoucher.get('code'),
        "customer": customer
    }
    result = voucherify.redemptions.redeem(payload)
    assert result.get('result') == 'SUCCESS'
    assert result.get('voucher', {}).get('code') == testVoucher.get('code')
    assert result.get('tracking_id') == customer.get('source_id')


    # test getVoucherRedemption
    result = voucherify.redemptions.getForVoucher(testVoucher.get('code'))
    assert result.get('data_ref') == 'redemption_entries'
    assert isinstance(result.get('redemption_entries'), list)


    # test listVoucherRedemptions
    filter_params = {
        "limit": 1,
        "page": 1,
        "[created_at][before]": "2016-12-31T23:59:59Z",
        "[created_at][after]": "2015-01-01T00:00:00Z",
        "result": "SUCCESS"
    }
    redemptionsList = voucherify.redemptions.list(filter_params)
    assert redemptionsList.get('data_ref') == 'redemptions'
    assert isinstance(redemptionsList.get('redemptions'), list)

    # test voucherRedemptionRollback
    redemption = voucherify.redemptions.redeem(testVoucher.get('code'))
    redemptionId = redemption.get('id')
    reason = 'just testing'

    time.sleep(1)
    rollbackResult = voucherify.redemptions.rollback(redemptionId, reason)
    assert rollbackResult.get('result') == 'SUCCESS'
    assert rollbackResult.get('reason') == reason
