import warnings
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


def test_createExistingVoucher(voucherifyInstance=voucherify.vouchers):
    result = voucherifyInstance.create(testVoucher)
    assert result.get('code') == 400
    assert result.get('message') == 'Duplicate resource key'


def test_updateVoucher(voucherifyInstance=voucherify.vouchers):
    uniquePerRun = str(datetime.datetime.utcnow())
    testVoucher['additional_info'] = uniquePerRun
    result = voucherifyInstance.update(testVoucher)
    assert result.get('additional_info') == uniquePerRun


def test_getVoucher(voucherifyInstance=voucherify.vouchers):
    voucher = voucherifyInstance.get(testVoucher.get('code'))
    assert voucher.get('code') == testVoucher.get('code')


def test_listVouchersFromCategory(voucherifyInstance=voucherify.vouchers):
    filter_params = {
        "limit": 1,
        "category": "PythonTestCategory"
    }
    vouchers = voucherifyInstance.list(filter_params)
    assert len(vouchers) == 1
    voucher = vouchers[0]
    assert voucher.get('code') == testVoucher.get('code')


def test_disableEnableActiveVoucher(voucherifyInstance=voucherify.vouchers):
    voucher = voucherifyInstance.get(testVoucher.get('code'))
    assert voucher.get('active') is True
    disable_result = voucherifyInstance.disable(testVoucher.get('code'))
    assert voucherifyInstance.get(testVoucher.get('code')).get('active') is False
    assert disable_result.get('active') is False

    enable_result = voucherifyInstance.enable(testVoucher.get('code'))
    assert voucherifyInstance.get(testVoucher.get('code')).get('active') is True
    assert enable_result.get('active') is True


def test_disableEnableVoucherThatDoesntExist(voucherifyInstance=voucherify.vouchers):
    randomVoucherCode = 'oaewhiuraowutehaowuet'

    def testEnable():
        result = voucherifyInstance.enable(randomVoucherCode)
        #  assert result is VoucherifyError
        assert result.get('code') == 404

    def testDisable():
        result = voucherifyInstance.enable(randomVoucherCode)
        #  assert result is VoucherifyError
        assert result.get('code') == 404
    testEnable()
    testDisable()


def test_deprecated_createExistingVoucher():
    checkDeprecationWarnings(lambda: test_createExistingVoucher(voucherify))


def test_deprecated_updateVoucher():
    checkDeprecationWarnings(lambda: test_updateVoucher(voucherify))


def test_deprecated_getVoucher():
    checkDeprecationWarnings(lambda: test_getVoucher(voucherify))


def test_deprecated_listVouchersFromCategory():
    checkDeprecationWarnings(lambda: test_listVouchersFromCategory(voucherify))


def test_deprecated_disableEnableActiveVoucher():
    expectedWarnings = 5
    checkDeprecationWarnings(lambda: test_disableEnableActiveVoucher(voucherify), expectedWarnings)


def test_deprecated_disableEnableVoucherThatDoesntExist():
    expectedWarnings = 2
    checkDeprecationWarnings(lambda: test_disableEnableVoucherThatDoesntExist(voucherify), expectedWarnings)


def checkDeprecationWarnings(deprecatedMethod, expectedWarningsCount=1):
    with warnings.catch_warnings(record=True) as warningList:
        # Cause all warnings to always be triggered.
        warnings.simplefilter("always")
        # Trigger a warning.
        deprecatedMethod()
        # Verify some things
        assert len(warningList) == expectedWarningsCount
        assert len(filter(lambda item: issubclass(item.category, DeprecationWarning), warningList)) == expectedWarningsCount
