from testUtils import getConfig, getConfiguredClient

voucherify = getConfiguredClient()


def test_publishVoucher():
    params = {
        "campaign": getConfig()['campaignName'],
        "channel": "Email",
        "customer": "donny.roll@mail.com"
    }
    result = voucherify.distributions.publish(params)
    voucher = result.get('voucher')
    assert voucher.get('active') is True
    assert voucher.get('type') == 'DISCOUNT_VOUCHER'
