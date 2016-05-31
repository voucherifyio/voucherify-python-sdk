## Voucherify Python SDK

[Voucherify](http://voucherify.io?utm_source=inbound&utm_medium=github&utm_campaign=voucherify-python-sdk) has a new platform that will help your team automate voucher campaigns. It does this by providing composable API and the marketer-friendly interface that increases teams' productivity:

- **roll-out thousands** of vouchers **in minutes** instead of weeks,
- **check status** or disable **every single** promo code in real time,
- **track redemption** history and build reports on the fly.

Here you can find a library that makes it easier to integrate Voucherify with your Python based application.

Full documentation is located at [voucherify.readme.io](https://voucherify.readme.io).

### Usage

#### Authentication

[Log-in](http://app.voucherify.io/#/login) to Voucherify web interface and obtain your Application Keys from [Configuration](https://app.voucherify.io/#/app/configuration):

![](https://www.filepicker.io/api/file/WKYkl2bSAWKHccEN9tEG)



#### Configure through a non-global API object

```python
import voucherify

voucherifyClient = voucherify.client(
    application_id="YOUR-APPLICATION-ID-OBTAINED-FROM-CONFIGURATION",
    client_secret_key="YOUR-CLIENT-SECRET-KEY-OBTAINED-FROM-CONFIGURATION"
)
```

#### Listing vouchers

`voucherifyClient.list(filter)`

Filter parameters:

- code_query
- limit (default 10)
- skip (default 0)
- category
- campaign
- customer

Example:
```python
voucherifyClient.list({limit: 10, skip: 20, category: "API Test"})
```

Result:
```json
[{
     "code": "9mYBpIk",
     "campaign": null,
     "category": "API Test",
     "discount": {
       "type": "AMOUNT",
       "amount_off": 400
     },
     "start_date": "2016-03-01T12:00:00Z",
     "expiration_date": null,
     "redemption": {
       "quantity": 1,
       "redeemed_quantity": 0,
       "redemption_entries": []
     },
     "active": true,
     "additional_info": null,
     "metadata": null
   },
   {
       "code": "AzTsIH",
       "campaign": null,
       "category": "API Test",
       "discount": {
        "type": "AMOUNT",
        "amount_off": 400
       },
       "start_date": "2016-03-01T10:00:00Z",
       "expiration_date": null,
       "redemption": {
        "quantity": 1,
        "redeemed_quantity": 0,
        "redemption_entries": []
       },
       "active": true,
       "additional_info": null,
       "metadata": null
   },
   ...
]
```

#### Getting voucher details

`voucherify.get(voucher_code)`

Example:
```python
voucherifyClient.get('v1GiJYuuS')
```

Result:
```json
{
    "code": "v1GiJYuuS",
    "campaign": "vip",
    "discount": {
        "percent_off": 10.0,
        "type": "PERCENT"
    },
    "expiration_date": "2016-12-31T23:59:59Z",
    "redemption": {
        "quantity": 3,
        "redeemed_quantity": 1,
        "redemption_entries": [
            {
                "id": "r_gQzOnTwmhn2nTLwW4sZslNKY",
                "object": "redemption",
                "date": "2016-04-24T06:03:35Z",
                "tracking_id": "GENERATED-OR-PROVIDED-TRACKING-ID"
            }
        ]
    },
    "additional_info": ""
}
```
#### Creating a voucher

`voucherifyClient.create(voucher)`

Example:

```python
voucherifyClient.create({
    discount: {
        type: 'AMOUNT',
        amount_off: 1000 // 10.00
    },
    category: 'Test',
    start_date: '2016-01-01T00:00:00Z'
    expiration_date: '2016-12-31T23:59:59Z'
})
```

#### Disabling a voucher

`voucherifyClient.disable(voucher_code)`

Example:

```python
voucherifyClient.disable('v1GiJYuuS')
```

#### Enabling a voucher

`voucherifyClient.enable(voucher_code)`

Example:

```python
voucherifyClient.enable('v1GiJYuuS')
```

#### Getting voucher redemption

`voucherify.redemption(voucher_code)`

Example:
```python
voucherifyClient.redemption('v1GiJYuuS')
```

Result:
```json
{
    "quantity": 3,
    "redeemed_quantity": 1,
    "redemption_entries": [
        {
            "id": "r_gQzOnTwmhn2nTLwW4sZslNKY",
            "object": "redemption",
            "date": "2016-04-24T06:03:35Z",
            "tracking_id": "GENERATED-OR-PROVIDED-TRACKING-ID"
        }
    ]
}
```

#### Publishing voucher

`voucherifyClient.publish(campaign_name)`

`voucherifyClient.publish(params)`

This method selects a voucher that is suitable for publication, adds a publish entry and returns the voucher.
A voucher is suitable for publication when it's active and has not been published more times than the redemption limit.

Example:

```python
voucherifyClient.publish({
    campaign: 'First Ride',
    channel: 'Email',
    customer: 'donny.roll@mail.com'
})
```

Positive result:

```json
{
   "code": "FR-zT-u9I7zG",
   "campaign": "First Ride",
   "category": null,
   "discount": {
      "type": "PERCENT",
      "amount_off": 50
   },
   "start_date": "2015-01-01T00:00:00Z",
   "expiration_date": "2016-12-31T23:59:59Z",
   "publish": {
        "count": 1,
        "entries": [{
            "channel": "Email",
            "customer": "donny.roll@mail.com",
            "published_at": "2016-01-22T09:25:07Z"
        }]
   },
   "redemption": {
      "quantity": 1,
      "redeemed_quantity": 0,
      "redemption_entries": []
   },
   "active": true,
   "additional_info": null
}
```

Possible error:

```json
{
  "code": 400,
  "message": "Couldn't find any voucher suitable for publication."
}
```

#### Redeeming voucher

`voucherifyClient.redeem(voucher_code, tracking_id|customer_profile*)`

##### 1. Just by code

Example:
```python
voucherifyClient.redeem('v1GiJYuuS')
```

Result (voucher details after redemption):

```json
{
    "id": "r_yRmanaA6EgSE9uDYvMQ5Evfp",
    "object": "redemption",
    "date": "2016-04-25T10:34:57Z",
    "tracking_id": "(tracking_id not set)",
    "voucher": {
        "code": "v1GiJYuuS",
        "campaign": "vip",
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
                    "tracking_id": "(tracking_id not set)"
                },
                {
                    "id": "r_yRmanaA6EgSE9uDYvMQ5Evfp",
                    "object": "redemption",
                    "date": "2016-04-25T10:34:57Z",
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

```python
voucherifyClient.redeem('v1GiJYuuS', 'alice.morgan')
```

Result:
```json
{
    "id": "r_yRmanaA6EgSE9uDYvMQ5Evfp",
    "object": "redemption",
    "date": "2016-04-25T10:34:57Z",
    "tracking_id": "(tracking_id not set)",
    "voucher": {
        "code": "v1GiJYuuS",
        "campaign": "vip",
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
                    "tracking_id": "(tracking_id not set)"
                },
                {
                    "id": "r_yRmanaA6EgSE9uDYvMQ5Evfp",
                    "object": "redemption",
                    "date": "2016-04-25T10:34:57Z",
                    "tracking_id": "(tracking_id not set)"
                },
                {
                    "id": "r_irOQWUTAjthQwnkn5JQM1V6N",
                    "object": "redemption",
                    "date": "2016-04-25T12:04:08Z",
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

You can record a detailed customer profile consisting of an `id` (obligatory), `name`, `email`, `description` and a `metadata` section that can include any data you wish.

```python
voucherifyClient.redeem({
    voucher: "v1GiJYuuS",
    customer: {
        id: "alice.morgan",
        name: "Alice Morgan",
        email: "alice@morgan.com",
        description: "",
        metadata: {
            locale: "en-GB",
            shoeSize: 5,
            favourite_brands: ["Armani", "L’Autre Chose", "Vicini"]
        }
    }
})
```

### Listing redemptions

Use `voucherify.redemptions(filter)` to get a filtered list of redemptions.
Filter parameters:

- limit (default: 100)
- page (default: 0)
- start_date (default: beginning of current month)
- end_date (default: end of current month)
- result - Success | Failure-NotExist | Failure-Inactive
- customer

Example - 1000 successful redemptions from April 2016:

```python
voucherifyClient.redemptions({
    limit: 1000,
    page: 0,
    start_date: "2016-04-01T00:00:00",
    end_date: "2016-04-30T23:59:59",
    result: "Success"
})
```

#### Rollback a redemption

Use `voucherify.rollback(redemption_id, tracking_id*, reason*)` to revert a redemption.
It will create a rollback entry in `redemption.redemption_entries` and give 1 redemption back to the pool
(decrease `redeemed_quantity` by 1).

Possible errors are:
- 404 - Resource not found - if voucher with given `redemption_id` doesn't exist
- 400 - Already rolled back - if redemption with given `redemption_id` has been rolled back already
- 400 - Invalid redemption id - when trying to rollback a rollback.

Example:

```python
voucherifyClient.rollback('r_irOQWUTAjthQwnkn5JQM1V6N', 'alice.morgan')
```

Result:
```json
{
    "id": "rr_1634wLkb8glgRXrTmsxRzDBd",
    "object": "redemption_rollback",
    "date": "2016-04-25T10:35:02Z",
    "tracking_id": "alice.morgan",
    "redemption": "r_irOQWUTAjthQwnkn5JQM1V6N",
    "voucher": {
        "code": "v1GiJYuuS",
        "campaign": "vip",
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
                    "tracking_id": "(tracking_id not set)"
                },
                {
                    "id": "r_yRmanaA6EgSE9uDYvMQ5Evfp",
                    "object": "redemption",
                    "date": "2016-04-25T10:34:57Z",
                    "tracking_id": "(tracking_id not set)"
                },
                {
                    "id": "r_irOQWUTAjthQwnkn5JQM1V6N",
                    "object": "redemption",
                    "date": "2016-04-25T12:04:08Z",
                    "tracking_id": "alice.morgan"
                },
                {
                    "id": "rr_1634wLkb8glgRXrTmsxRzDBd",
                    "object": "redemption_rollback",
                    "date": "2016-04-25T10:35:02Z",
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


### Utils

#### Usage

```
from voucherify import utils
```

#### Available methods

- `utils.calculatePrice(basePrice, voucher)`
- `utils.calculateDiscount(basePrice, voucher)`

### Changelog

- **2016-05-31** - `0.1.0` - First version:
  - Authentication
  - Voucher informations: *get*, *usage*
  - Voucher operations: *use*