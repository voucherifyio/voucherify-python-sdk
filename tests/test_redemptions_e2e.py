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


def test_redeemVoucher(voucherifyInstance=voucherify.redemptions):
    result = voucherifyInstance.redeem(testVoucher.get('code'))
    assert result.get('result') == 'SUCCESS'
    assert result.get('voucher', {}).get('code') == testVoucher.get('code')


def test_redeemVoucherWithTrackingId(voucherifyInstance=voucherify.redemptions):
    result = voucherifyInstance.redeem(testVoucher.get('code'), tracking_id)
    assert result.get('result') == 'SUCCESS'
    assert result.get('voucher', {}).get('code') == testVoucher.get('code')
    assert len(result.get('tracking_id')) > 0


def test_redeemVoucherWithCustomerInfo(voucherifyInstance=voucherify.redemptions):
    customer = {
        "source_id": "alice.morgan",
        "name": "Alice Morgan",
        "email": "alice@morgan.com",
        "description": "",
        "metadata": {
            "locale": "en-GB",
            "shoeSize": 5,
            "favourite_brands": "Armani"
        }
    }
    payload = {
        "voucher": testVoucher.get('code'),
        "customer": customer
    }
    result = voucherifyInstance.redeem(payload)
    assert result.get('result') == 'SUCCESS'
    assert result.get('voucher', {}).get('code') == testVoucher.get('code')


def test_getVoucherRedemption(testedMethod=voucherify.redemptions.getForVoucher):
    result = testedMethod(testVoucher.get('code'))
    assert result.get('data_ref') == 'redemption_entries'
    assert isinstance(result.get('redemption_entries'), list)


def test_listVoucherRedemptions(testedMethod=voucherify.redemptions.list):
    filter_params = {
        "limit": 1,
        "page": 1,
        "[created_at][before]": "2016-12-31T23:59:59Z",
        "[created_at][after]": "2015-01-01T00:00:00Z",
        "result": "SUCCESS"
    }
    redemptionsList = testedMethod(filter_params)
    assert redemptionsList.get('data_ref') == 'redemptions'
    assert isinstance(redemptionsList.get('redemptions'), list)

def test_voucherRedemptionRollback(voucherifyInstance=voucherify.redemptions):
    redemption = voucherifyInstance.redeem(testVoucher.get('code'))
    redemptionId = redemption.get('id')
    reason = 'just testing'

    time.sleep(1)
    rollbackResult = voucherifyInstance.rollback(redemptionId, reason)
    assert rollbackResult.get('result') == 'SUCCESS'
    assert rollbackResult.get('reason') == reason
