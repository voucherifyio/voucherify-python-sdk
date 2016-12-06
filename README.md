## Voucherify Python SDK

[Voucherify](http://voucherify.io?utm_source=github&utm_medium=sdk&utm_campaign=acq) is an API-first platform for software developers who are dissatisfied with high-maintenance custom coupon software. Our product is a coupon infrastructure through API that provides a quicker way to build coupon generation, distribution and tracking. Unlike legacy coupon software we have:

* an API-first SaaS platform that enables customisation of every aspect of coupon campaigns
* a management console that helps cut down maintenance and reporting overhead
* an infrastructure to scale up coupon activity in no time

Here you can find a library that makes it easier to integrate Voucherify with your Python based application.

Full documentation is located at [voucherify.readme.io](https://voucherify.readme.io).

### Usage

#### Authentication

[Log-in](http://app.voucherify.io/#/login) to Voucherify web interface and obtain your Application Keys from [Configuration](https://app.voucherify.io/#/app/configuration):

![](https://www.filepicker.io/api/file/WKYkl2bSAWKHccEN9tEG)



#### Configure through a non-global API object

```python
from voucherify import Client as voucherifyClient

voucherify = voucherifyClient(
    application_id="c70a6f00-cf91-4756-9df5-47628850002b",
    client_secret_key="3266b9f8-e246-4f79-bdf0-833929b1380c"
)
```

#### Listing vouchers

`voucherify.list(filter)`

Filter parameters:

- code_query
- limit (default 10)
- skip (default 0)
- category
- campaign
- customer

Example:
```python
filter_params = {
  "limit": 10,
  "skip": 20,
  "category": "API Test"
}

vouchers_list = voucherify.list(filter_params)
```

Result:
```json
[{
    "code": "9mYBpIk",
    "campaign": null,
    "category": "API Test",
    "type": "DISCOUNT_VOUCHER",
    "discount": {
        "type": "AMOUNT",
        "amount_off": 400
    },
    "start_date": "2016-03-01T12:00:00Z",
    "expiration_date": null,
    "publish": {
        "object": "list",
        "count": 1,
        "data_ref": "entries",
        "entries": [{
            "channel": "Email",
            "published_at": "2016-04-10T12:00:00Z",
            "customer": "alice.morgan@mail.com",
            "customer_id": "cust_1fnSUBno3iimKTPNDCkjg4xV"
        }]
    },
    "redemption": {
        "object": "list",
        "quantity": 1,
        "data_ref": "redemption_entries",
        "redeemed_quantity": 0,
        "redemption_entries": []
    },
    "active": true,
    "additional_info": null,
    "metadata": null
},{
    "code": "AzTsIH",
    "campaign": null,
    "category": "API Test",
    "type": "GIFT_VOUCHER",
    "gift": {
         "amount": 10000,
         "balance": 5000
    },
    "start_date": "2016-03-01T10:00:00Z",
    "expiration_date": null,
    "publish": {
        "object": "list",
        "count": 0,
        "data_ref": "entries",
        "entries": []
    },
    "redemption": {
        "object": "list",
        "quantity": 1,
        "data_ref": "redemption_entries",
        "redeemed_quantity": 0,
        "redeemed_amount": 0,
        "redemption_entries": []
    },
    "active": true,
    "additional_info": null,
    "metadata": null
}]
```

#### Getting voucher details

`voucherify.get(voucher_code)`

Example:
```python
voucher = voucherify.get("Testing7fjWdr")
```

Result:
```json
{
    "code": "v1GiJYuuS",
    "campaign": "vip",
    "type": "DISCOUNT_VOUCHER",
    "discount": {
        "percent_off": 10.0,
        "type": "PERCENT"
    },
    "expiration_date": "2016-12-31T23:59:59Z",
    "publish": {
        "object": "list",
        "count": 1,
        "data_ref": "entries",
        "entries": [{
            "channel": "Email",
            "published_at": "2016-04-10T12:00:00Z",
            "customer": "alice.morgan@mail.com",
            "customer_id": "cust_1fnSUBno3iimKTPNDCkjg4xV"
        }]
    },
    "redemption": {
        "object": "list",
        "quantity": 1,
        "data_ref": "redemption_entries",
        "redeemed_quantity": 0,
        "redemption_entries": [{
            "id": "r_gQzOnTwmhn2nTLwW4sZslNKY",
            "object": "redemption",
            "date": "2016-04-24T06:03:35Z",
            "customer_id": "GENERATED-CUSTOMER-ID",
            "tracking_id": "GENERATED-OR-PROVIDED-TRACKING-ID"
        }]
    },
    "additional_info": ""
}
```
#### Creating a voucher

`voucherify.create(voucher)`

You can create a voucher with a specified code or let Voucherify generate one.
By default a generated code is a 8 characters long alphanumeric string, however,
you can define how to create the random code passing a `code_config` dict:
- `length` - Number of characters in a generated code (excluding prefix and postfix).
- `charset` - Characters that can appear in the code.
- `prefix` - A text appended before the code.
- `postfix` - A text appended after the code.
- `pattern` - A pattern for codes where hashes (#) will be replaced with random characters. Overrides `length`.

Example:

```python
payload = {
    "code_config": {
        "charset": "01234567890",
        "pattern": "TEST-#####"
    },
    "type": "DISCOUNT_VOUCHER",
    "discount": {
        "type": "AMOUNT",
        "amount_off": 1000  # 10.00
    },
    "category": "API Test",
    "start_date": "2016-01-01T00:00:00Z",
    "expiration_date": "2016-12-31T23:59:59Z"
}

new_voucher = voucherify.create(payload)
```

Result:

```json
{
    "code": "JxiJaV",
    "campaign": null,
    "category": "API Test",
    "type": "DISCOUNT_VOUCHER",
    "discount": {
        "type": "AMOUNT",
        "amount_off": 1000
    },
    "start_date": "2016-01-01T00:00:00Z",
    "expiration_date": "2016-12-31T23:59:59Z",
    "publish": {
        "object": "list",
        "count": 0,
        "data_ref": "entries",
        "entries": []
    },
    "redemption": {
        "object": "list",
        "quantity": 0,
        "data_ref": "redemption_entries",
        "redeemed_quantity": 0,
        "redemption_entries": []
    },
    "active": true,
    "additional_info": null,
    "metadata": null
}
```

#### Updating a voucher

You can change some properties of a voucher that has been already created:
- category
- start date
- expiration date
- active
- additinal info
- metadata

Other fields than listed above won't be modified. Even if provided they will be silently skipped.

Use `voucherify.update(voucher_update)` to update a voucher.

```python
voucher_update = {
  "code": "Summer-2016",
  "category": "Season",
  "start_date": "2016-07-01T00:00:00Z",
  "expiration_date": "2016-08-31T23:59:59Z",
}

updated_voucher = voucherify.update(voucher_update)
```

#### Disabling a voucher

`voucherify.disable(voucher_code)`

Example:

```python
result = voucherify.disable("JxiJaV")
```

Result:

**This method does not return result when succeed**

Error:

```json
{
  "code": 404,
  "message": "Resource not found",
  "details": "Cannot find Voucher with code: <voucher_code>"
}
```

```json
{
    "statusCode": 400,
    "error": "Bad Request"
}
```

#### Enabling a voucher

`voucherify.enable(voucher_code)`

Example:

```python
result = voucherify.enable("JxiJaV")
```

Result:

**This method does not return result when succeed**

Error:

```json
{
  "code": 404,
  "message": "Resource not found",
  "details": "Cannot find Voucher with code: <voucher_code>"
}
```

```json
{
    "statusCode": 400,
    "error": "Bad Request"
}
```

#### Getting voucher redemption

`voucherify.redemption(voucher_code)`

Example:
```python
result = voucherify.redemption("Testing7fjWdr")
```

Result:
```json
{
    "object": "list",
    "quantity": 3,
    "data_ref": "redemption_entries",
    "redeemed_quantity": 1,
    "redemption_entries": [
        {
            "id": "r_gQzOnTwmhn2nTLwW4sZslNKY",
            "object": "redemption",
            "date": "2016-04-24T06:03:35Z",
            "customer_id": "GENERATED-CUSTOMER-ID",
            "tracking_id": "GENERATED-OR-PROVIDED-TRACKING-ID"
        }
    ]
}
```

#### Publishing voucher

This method selects a voucher that is suitable for publication, adds a publish entry and returns the voucher.
A voucher is suitable for publication when it's active and has not been published more times than the redemption limit.

##### Publish using campaign name

`voucherify.publish(campaign_name)`

Example:

```python
result = voucherify.publish("First Ride")
```

##### Publish using params

`voucherify.publish(params)`

Using campaign name:

```python
payload = {
    "campaign": "First Ride",
    "channel": "SDK Test",
    "customer": "donny.roll@mail.com"
}
result = voucherify.publish(payload)
```

Using voucher code:

```python
payload = {
    "voucher": "FR-zT-u9I7zG",
    "channel": "Email",
    "customer": "donny.roll@mail.com"
}
result = voucherify.publish(payload)
```

Result *(for both)*:

```json
{
    "code": "FR-zT-u9I7zG",
    "campaign": "First Ride",
    "category": null,
    "type": "DISCOUNT_VOUCHER",
    "discount": {
        "type": "PERCENT",
        "amount_off": 50
    },
    "start_date": "2015-01-01T00:00:00Z",
    "expiration_date": "2016-12-31T23:59:59Z",
    "publish": {
        "object": "list",
        "count": 0,
        "data_ref": "entries",
        "entries": [{
            "channel": "Email",
            "customer": "donny.roll@mail.com",
            "customer_id": "cust_84LPwcHJ1jVEpxV1uF9nLLBB",
            "published_at": "2016-01-22T09:25:07Z"
        }]
    },
    "redemption": {
        "object": "list",
        "quantity": 0,
        "data_ref": "redemption_entries",
        "redeemed_quantity": 0,
        "redemption_entries": []
    },
    "active": true,
    "additional_info": null
}
```

Error:

```json
{
  "code": 400,
  "message": "Couldn't find any voucher suitable for publication."
}
```

#### Redeeming voucher

`voucherify.redeem(voucher_code, tracking_id|customer_profile*)`

##### 1. Just by code

Example:
```python
result = voucherify.redeem("Testing7fjWdr")
```

Result (voucher details after redemption):

```json
{
    "id": "r_yRmanaA6EgSE9uDYvMQ5Evfp",
    "object": "redemption",
    "date": "2016-04-25T10:34:57Z",
    "customer_id": null,
    "tracking_id": "(tracking_id not set)",
    "voucher": {
        "code": "v1GiJYuuS",
        "campaign": "vip",
        "type": "DISCOUNT_VOUCHER",
        "discount": {
            "percent_off": 10.0,
            "type": "PERCENT"
        },
        "expiration_date": "2016-12-31T23:59:59Z",
        "redemption": {
            "quantity": 3,
            "redeemed_quantity": 2,
            "redemption_entries": [
                {
                    "id": "r_gQzOnTwmhn2nTLwW4sZslNKY",
                    "object": "redemption",
                    "date": "2016-04-24T06:03:35Z",
                    "customer_id": null,
                    "tracking_id": "(tracking_id not set)"
                },
                {
                    "id": "r_yRmanaA6EgSE9uDYvMQ5Evfp",
                    "object": "redemption",
                    "date": "2016-04-25T10:34:57Z",
                    "customer_id": null,
                    "tracking_id": "(tracking_id not set)"
                }
            ]
        },
        "active": true,
        "additional_info": ""
    }
}
```

Error:

```json
{
  "code": 400,
  "message": "voucher expired or quantity exceeded",
  "details": "v1GiJYuuS"
}
```

##### 2. With tracking id

You can provide a tracking id (e.g. your customer's login or a generated id) to the voucher redemption request.

Example:

```python
result = voucherify.redeem("Testing7fjWdr", "alice.morgan")
```

Result:

```json
{
    "id": "r_yRmanaA6EgSE9uDYvMQ5Evfp",
    "object": "redemption",
    "date": "2016-04-25T10:34:57Z",
    "customer_id": "cust_84LPwcHJ1jVEpxV1uF9nLLBB",
    "tracking_id": "alice.morgan",
    "voucher": {
        "code": "v1GiJYuuS",
        "campaign": "vip",
        "type": "DISCOUNT_VOUCHER",
        "discount": {
            "percent_off": 10.0,
            "type": "PERCENT"
        },
        "expiration_date": "2016-12-31T23:59:59Z",
        "redemption": {
            "quantity": 3,
            "redeemed_quantity": 3,
            "redemption_entries": [
                {
                    "id": "r_gQzOnTwmhn2nTLwW4sZslNKY",
                    "object": "redemption",
                    "date": "2016-04-24T06:03:35Z",
                    "customer_id": null,
                    "tracking_id": "(tracking_id not set)"
                },
                {
                    "id": "r_yRmanaA6EgSE9uDYvMQ5Evfp",
                    "object": "redemption",
                    "date": "2016-04-25T10:34:57Z",
                    "customer_id": null,
                    "tracking_id": "(tracking_id not set)"
                },
                {
                    "id": "r_irOQWUTAjthQwnkn5JQM1V6N",
                    "object": "redemption",
                    "date": "2016-04-25T12:04:08Z",
                    "customer_id": "cust_84LPwcHJ1jVEpxV1uF9nLLBB",
                    "tracking_id": "alice.morgan"
                }
            ]
        },
        "active": true,
        "additional_info": ""
    }
}
```

##### 3. With customer profile

You can record a detailed customer profile consisting of an `source_id`, `name`, `email`, `description` and a `metadata` section that can include any data you wish.

Example:

```python
customer = {
    "source_id": "alice.morgan",
    "name": "Alice Morgan",
    "email": "alice@morgan.com",
    "description": "",
    "metadata": {
        "locale": "en-GB",
        "shoeSize": 5,
        "favourite_brands": ["Armani", "L'Autre Chose", "Vicini"]
    }
}
payload = {
    "voucher": "v1GiJYuuS",
    "customer": customer
}
voucherify.redeem(payload)
```

##### 4. With customer id

If you already created a customer profile in Voucherify's database, whether it was implicitly by providing it to the `redeem` function or explicitly by invoking the [`customer.create`](#create-customer) method, you can identify your customer in following redemptions by a generated id (starting with `cust_`). 

```python
voucherify.redeem({
        voucher: "v1GiJYuuS",
        customer: {
            id: "cust_C9qJ3xKgZFqkpMw7b21MF2ow"
        })
```

##### 5. With order amount

Redeeming a gift voucher requires passing order amount. The same applies to vouchers with validation rules on order's total amount.  
Order amount have to be expressed in cents, as an integer. For example $22.50 should be provided as 2250.
Gift voucher balance will be used to cover the order amount entirely or partially.

```python
voucherify.redeem({
        voucher: "91Ft4U",
        order: {
            amount: 2250
        })
```

##### 6. With order items

Vouchers with validation rules regarding products or SKUs require to pass `order.items`.
Items are a list of objects consisting of `product_id`, `sku_id` and `quantity`.

```python
voucherify.redeem({
        voucher: "91Ft4U",
        order: {
            items: [
                { product_id: "prod_ELvEXqF4qzB7Rs", sku_id: "sku_GoXSOI4FwJZafb", quantity: 1 },
                { product_id: "prod_wye1naw5JO5dh3", sku_id: "sku_U3rHSlfOCGUnbo", quantity: 2 }
            ]
        })
```

### Listing redemptions

Use `redemptions` to get a filtered list of redemptions.

Filter parameters:

- limit (default: 100)
- page (default: 0)
- start_date (default: beginning of current month)
- end_date (default: end of current month)
- result - Success | Failure-NotExist | Failure-Inactive
- customer - id or source_id

`voucherify.redemptions(filter)`

Example:

```python
filter_params = {
    "limit": 1000,
    "page": 0,
    "start_date": "2016-04-01T00:00:00",
    "end_date": "2016-04-30T23:59:59",
    "result": "Success"
}

redemptions = voucherify.redemptions(filter_params)
```

#### Rollback a redemption

Use `rollback` to revert a redemption.
It will create a rollback entry in `redemption.redemption_entries` and give 1 redemption back to the pool
(decrease `redeemed_quantity` by 1).

`voucherify.rollback(redemption_id, reason*)`

Example:

```python
result = voucherify.rollback("r_irOQWUTAjthQwnkn5JQM1V6N", "john.doe")
```

Result:
```json
{
    "id": "rr_1634wLkb8glgRXrTmsxRzDBd",
    "object": "redemption_rollback",
    "date": "2016-04-25T10:35:02Z",
    "customer_id": "cust_84LPwcHJ1jVEpxV1uF9nLLBB",
    "tracking_id": "alice.morgan",
    "redemption": "r_irOQWUTAjthQwnkn5JQM1V6N",
    "voucher": {
        "code": "v1GiJYuuS",
        "campaign": "vip",
        "type": "DISCOUNT_VOUCHER",
        "discount": {
            "percent_off": 10.0,
            "type": "PERCENT"
        },
        "expiration_date": "2016-12-31T23:59:59Z",
        "redemption": {
            "quantity": 3,
            "redeemed_quantity": 2,
            "redemption_entries": [
                {
                    "id": "r_gQzOnTwmhn2nTLwW4sZslNKY",
                    "object": "redemption",
                    "date": "2016-04-24T06:03:35Z",
                    "customer_id": null,
                    "tracking_id": "(tracking_id not set)"
                },
                {
                    "id": "r_yRmanaA6EgSE9uDYvMQ5Evfp",
                    "object": "redemption",
                    "date": "2016-04-25T10:34:57Z",
                    "customer_id": null,
                    "tracking_id": "(tracking_id not set)"
                },
                {
                    "id": "r_irOQWUTAjthQwnkn5JQM1V6N",
                    "object": "redemption",
                    "date": "2016-04-25T12:04:08Z",
                    "customer_id": "cust_84LPwcHJ1jVEpxV1uF9nLLBB",
                    "tracking_id": "alice.morgan"
                },
                {
                    "id": "rr_1634wLkb8glgRXrTmsxRzDBd",
                    "object": "redemption_rollback",
                    "date": "2016-04-25T10:35:02Z",
                    "customer_id": "cust_84LPwcHJ1jVEpxV1uF9nLLBB",
                    "tracking_id": "alice.morgan",
                    "redemption": "r_irOQWUTAjthQwnkn5JQM1V6N"
                }
            ]
        },
        "active": true,
        "additional_info": ""
    }
}
```

Possible errors are:
- 404 - Resource not found - if voucher with given `redemption_id` doesn't exist
- 400 - Already rolled back - if redemption with given `redemption_id` has been rolled back already
- 400 - Invalid redemption id - when trying to rollback a rollback.


#### Create customer

Example:

```python
payload = {
    "name": "John Doe",
    "email": "john@email.com",
    "description": "Sample description of customer",
    "metadata": {
        "lang": "en"
    }
}

result = voucherify.customer.create(payload)
```

Result:
```json
{
    "id": "cust_WGG615E92dhOHz7PV9Vo9gk9",
    "created_at": "2016-06-12T15:52:49Z",
    "description": "Sample description of customer",
    "email": "john@email.com",
    "metadata": {
        "lang": "en"
    },
    "name": "John Doe",
    "object": "customer"
}
```

#### Get customer

Example:

```python
result = voucherify.customer.get("cust_gVYAaioitMz3GO6HSKFLf7Or")
```

Result:
```json
{
    "id": "cust_gVYAaioitMz3GO6HSKFLf7Or",
    "created_at": "2016-06-12T16:03:36Z",
    "description": "Sample description of customer",
    "email": "john@email.com",
    "metadata": {
        "lang": "en"
    },
    "name": "John Doe",
    "object": "customer"
 }
```

#### Update customer

Example:

```python
payload = {
    "id": "cust_gVYAaioitMz3GO6HSKFLf7Or",
    "description": "Updated description for given customer ID"
}

result = voucherify.customer.update(payload)
```

Result:
```json
{
    "id": "cust_gVYAaioitMz3GO6HSKFLf7Or",
    "created_at": "2016-06-12T16:03:36Z",
    "description": "Updated description for given customer ID",
    "email": "john@email.com",
    "metadata": {
        "lang": "en"
    },
    "name": "John Doe",
    "object": "customer"
 }
```

#### Delete customer

Example:

```python
result = voucherify.customer.delete("cust_gVYAaioitMz3GO6HSKFLf7Or")
```

Result:
`Result is an empty body`

### Utils

Use our set of utils to calculate a price after discount or discount amount.

#### Available methods

- `utils.calculatePrice(basePrice, voucher, unit_price)` - Calculate discount amount
- `utils.calculateDiscount(basePrice, voucher, unit_price)` - Calculate new price after discount

#### Example

```Python
from voucherify import utils

# Example voucher object.
# You can use `get` method from API to get correct voucher dictionary shape.
voucher = {
  "code": "Testing7fjWdr",
  "discount": {
    "type": "AMOUNT",
    "amount_off": 1080  # 10.80
  },
  "category": "API Test",
  "start_date": "2016-01-01T00:00:00Z",
  "expiration_date": "2016-12-31T23:59:59Z"
}

# Price of one item
unit_price = 83.45

# Number of items
items_count = 13

# Total price
base_price = unit_price * items_count

# Calculate discount amount
discount = utils.calculate_discount(base_price, voucher, unit_price)

# Calculate new price after discount
new_price = utils.calculate_price(base_price, voucher, unit_price)
```

### Changelog

- **2016-12-02** - `1.4.2` - Support gift vouchers in utils
- **2016-10-04** - `1.4.1` - Publish update
- **2016-07-18** - `1.4.0` - Voucher code pattern
- **2016-07-18** - `1.3.0` - Update voucher
- **2016-06-23** - `1.2.1` - Gift vouchers
- **2016-06-16** - `1.2.0` - Unified naming convention
- **2016-06-16** - `1.1.0` - Added customer methods
- **2016-06-08** - `1.0.0` - Release version
- **2016-05-31** - `0.1.0` - First version:
  - Authentication
  - Voucher informations: *get*, *usage*
  - Voucher operations: *use*
  - Utils
