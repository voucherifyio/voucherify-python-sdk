import datetime
from voucherify import Client as voucherifyClient

voucherify = voucherifyClient(
    application_id="c70a6f00-cf91-4756-9df5-47628850002b",
    client_secret_key="3266b9f8-e246-4f79-bdf0-833929b1380c"
)

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


    # test createExistingVoucher
    result = voucherify.vouchers.create(testVoucher)
    assert result.get('code') == 400
    assert result.get('message') == 'Duplicate resource key'


    # test updateVoucher
    uniquePerRun = str(datetime.datetime.utcnow())
    testVoucher['additional_info'] = uniquePerRun
    result = voucherify.vouchers.update(testVoucher)
    assert result.get('additional_info') == uniquePerRun


    # test getVoucher
    voucher = voucherify.vouchers.get(testVoucher.get('code'))
    assert voucher.get('code') == testVoucher.get('code')


    # test listVouchersFromCategory
    filter_params = {
        "limit": 1,
        "category": "PythonTestCategory"
    }
    vouchers = voucherify.vouchers.list(filter_params)
    assert len(vouchers.get('vouchers')) == 1
    voucher = vouchers.get('vouchers')[0]
    assert voucher.get('code') == testVoucher.get('code')


    # test disableEnableActiveVoucher
    voucher = voucherify.vouchers.get(testVoucher.get('code'))
    assert voucher.get('active') is True
    disable_result = voucherify.vouchers.disable(testVoucher.get('code'))
    assert voucherify.vouchers.get(testVoucher.get('code')).get('active') is False
    assert disable_result.get('active') is False

    enable_result = voucherify.vouchers.enable(testVoucher.get('code'))
    assert voucherify.vouchers.get(testVoucher.get('code')).get('active') is True
    assert enable_result.get('active') is True


    # test enableVoucherThatDoesntExist
    randomVoucherCode = 'oaewhiuraowutehaowuet'
    result = voucherify.vouchers.enable(randomVoucherCode)
    #  assert result is VoucherifyError
    assert result.get('code') == 404

    # test disableVoucherThatDoesntExist
    result = voucherify.vouchers.disable(randomVoucherCode)
    #  assert result is VoucherifyError
    assert result.get('code') == 404
