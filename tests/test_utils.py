from voucherify import utils

unit_price = 83.45
items_count = 13
base_price = unit_price * items_count


def test_shouldCalculateAmountPriceDiscount():
    voucher = {
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
    discount = utils.calculate_discount(base_price, voucher, unit_price)
    price = utils.calculate_price(base_price, voucher, unit_price)
    assert discount == 124.36
    assert price == 960.49


def test_shouldCalculateAmountDiscountWhenGiftIsNone():
    voucher = {
        "code": "PythonVoucherTest",
        "discount": {
            "type": "AMOUNT",
            "amount_off": 12436
        },
        "gift": None,
        "category": "PythonTestCategory",
        "start_date": "2016-01-01T00:00:00Z",
        "expiration_date": None,
        "redemption": {
            "quantity": None,
            "redeemed_quantity": 0
        },
        "active": True
    }
    discount = utils.calculate_discount(base_price, voucher, unit_price)
    price = utils.calculate_price(base_price, voucher, unit_price)
    assert discount == 124.36
    assert price == 960.49
