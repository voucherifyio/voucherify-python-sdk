from voucherify import Client as voucherifyClient

voucherify = voucherifyClient(
    application_id="c70a6f00-cf91-4756-9df5-47628850002b",
    client_secret_key="3266b9f8-e246-4f79-bdf0-833929b1380c"
)


def test_publishVoucher():
    params = {
        "channel": "Email",
        "customer": "donny.roll@mail.com"
    }
    result = voucherify.distributions.publish(params)
    assert result.get('active') is True
    assert result.get('type') == 'DISCOUNT_VOUCHER'
