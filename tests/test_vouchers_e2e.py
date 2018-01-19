import pprint
import datetime
from voucherify import Client as voucherifyClient

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


def test_createExistingVoucher():
    result = voucherify.create(testVoucher)
    assert result.get('code') == 400
    assert result.get('message') == 'Duplicate resource key'


def test_updateVoucher():
    uniquePerRun = str(datetime.datetime.utcnow())
    testVoucher['additional_info'] = uniquePerRun
    result = voucherify.update(testVoucher)
    assert result.get('additional_info') == uniquePerRun


def test_getVoucher():
    voucher = voucherify.get(testVoucher.get('code'))
    assert voucher.get('code') == testVoucher.get('code')


def test_listVouchersFromCategory():
    filter_params = {
        "limit": 1,
        "category": "PythonTestCategory"
    }
    vouchers = voucherify.list(filter_params)
    assert len(vouchers) == 1
    voucher = vouchers[0]
    assert voucher.get('code') == testVoucher.get('code')


def test_disableEnableActiveVoucher():
    voucher = voucherify.get(testVoucher.get('code'))
    assert voucher.get('active') is True
    disable_result = voucherify.disable(testVoucher.get('code'))
    assert voucherify.get(testVoucher.get('code')).get('active') is False
    assert disable_result.get('active') is False

    enable_result = voucherify.enable(testVoucher.get('code'))
    assert voucherify.get(testVoucher.get('code')).get('active') is True
    assert enable_result.get('active') is True


def test_disableEnableVoucherThatDoesntExist():
    randomVoucherCode = 'oaewhiuraowutehaowuet'

    def testEnable():
        result = voucherify.enable(randomVoucherCode)
        #  assert result is VoucherifyError
        assert result.get('code') == 404

    def testDisable():
        result = voucherify.enable(randomVoucherCode)
        #  assert result is VoucherifyError
        assert result.get('code') == 404
    testEnable()
    testDisable()

