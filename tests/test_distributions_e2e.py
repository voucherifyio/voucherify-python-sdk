import warnings
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


def test_publishVoucher():
    params = {
        "channel": "Email",
        "customer": "donny.roll@mail.com"
    }
    result = voucherify.distributions.publish(params)
    assert result.get('active') is True
    assert result.get('type') == 'DISCOUNT_VOUCHER'


def checkDeprecationWarnings(deprecatedMethod, expectedWarningsCount=1):
    with warnings.catch_warnings(record=True) as warningList:
        # Cause all warnings to always be triggered.
        warnings.simplefilter("always")
        # Trigger a warning.
        deprecatedMethod()
        # Verify some things
        assert len(warningList) == expectedWarningsCount
        assert len(filter(lambda item: issubclass(item.category, DeprecationWarning), warningList)) == expectedWarningsCount
