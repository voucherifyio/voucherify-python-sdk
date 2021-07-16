<p align="center" >
  <img src="./voucherify-python-sdk.png" />
</p>

<h3 align="center">Official <a href="https://voucherify.io?utm_source=github&utm_medium=sdk&utm_campaign=acq">Voucherify</a> SDK for Python</h3>

<p align="center">
<b><a href="#setup">Setup</a></b>
|
<b><a href="#contributing">Contributing</a></b>
|
<b><a href="#changelog">Changelog</a></b>
</p>

<p align="center">
API:
<a href="#vouchers-api">Vouchers</a>
|
<a href="#distributions-api">Distributions</a>
|
<a href="#redemptions-api">Redemptions</a>
|
<a href="#customers-api">Customers</a>
|
<a href="#utils">Utils</a>
</p>


---

## Setup

`pip install 'Voucherify'`

[Log-in](https://app.voucherify.io/?utm_source=github&utm_medium=sdk&utm_campaign=acq#/login) to Voucherify web interface and obtain your Application Keys from [Configuration](https://app.voucherify.io/?utm_source=github&utm_medium=sdk&utm_campaign=acq#/app/configuration):

```python
from voucherify import Client as voucherifyClient

client = voucherifyClient(
    application_id='YOUR-APPLICATION-ID',
    client_secret_key='YOUR-CLIENT-SECRET-KEY'
)
```

### API Endpoint

Optionally, you can add `api_endpoint` to the client options if you want to use Voucherify running in a specific region.
Optionally, you can add `timeout` to specify request's timeout in seconds. Default value is set to 3 minutes.

```python
from voucherify import Client as voucherifyClient

client = voucherifyClient(
    application_id='YOUR-APPLICATION-ID',
    client_secret_key='YOUR-CLIENT-SECRET-KEY',
    api_endpoint='https://<region>.api.voucherify.io',
    timeout=180
)
```

## API

This SDK is consistent with restful API Voucherify provides.
Not all API methods are currently supported in this SDK, but they are coming soon.

You will find detailed description and example responses at [official docs](https://docs.voucherify.io/reference?utm_source=github&utm_medium=sdk&utm_campaign=acq).
Method headers point to more detailed descriptions of params you can use.

### Vouchers API
Methods are provided within `client.vouchers.*` namespace.
- [Create Voucher](#create-voucher)
- [Get Voucher](#get-voucher)
- [Update Voucher](#update-voucher)
- [List Vouchers](#list-vouchers)
- [Enable Voucher](#enable-voucher)
- [Disable Voucher](#disable-voucher)

#### [Create Voucher]
```python
client.vouchers.create(voucher)
```
Check [voucher object](https://docs.voucherify.io/reference?utm_source=github&utm_medium=sdk&utm_campaign=acq#the-voucher-object).

#### [Get Voucher]
```python
client.vouchers.get(code)
```
#### [Update Voucher]
```python
client.vouchers.update(voucher)
```
#### [List Vouchers]
```python
client.vouchers.list(params)
```
#### [Enable Voucher]
```python
client.vouchers.enable(code)
```
#### [Disable Voucher]
```python
client.vouchers.disable(code)
```

---

### Distributions API
Methods are provided within `client.distributions.*` namespace.

- [Publish Voucher](#publish-voucher)

#### [Publish Voucher]
```python
client.distributions.publish(params)
```

---
### Validations API
Methods are provided within `client.validations.*` namespace.

- [Validate Voucher](#validate-voucher)

#### [Validate Voucher]
```python
client.validations.validateVoucher(code, params)
```

---

### Redemptions API
Methods are provided within `client.redemptions.*` namespace.

- [Redeem Voucher](#redeem-voucher)
- [List Redemptions](#list-redemptions)
- [Get Voucher's Redemptions](#get-vouchers-redemptions)
- [Rollback Redemption](#rollback-redemption)

#### [Redeem Voucher]
```python
client.redemptions.redeem(code, tracking_id)
```
#### [List Redemptions]
```python
client.redemptions.list(params)
```
#### [Get Voucher's Redemptions]
```python
client.redemptions.getForVoucher(code)
```
#### [Rollback Redemption]
```python
client.redemptions.rollback(redemptionId)
client.redemptions.rollback(redemptionId, reason)
```
Check [redemption rollback object](https://docs.voucherify.io/reference?utm_source=github&utm_medium=sdk&utm_campaign=acq#the-redemption-rollback-object).

---

### Customers API
Methods are provided within `client.customers.*` namespace.

- [Create Customer](#create-customer)
- [Get Customer](#get-customer)
- [Update Customer](#update-customer)
- [Delete Customer](#delete-customer)

#### [Create Customer]
```python
client.customers.create(customer)
```
Check [customer object](https://docs.voucherify.io/reference?utm_source=github&utm_medium=sdk&utm_campaign=acq#the-customer-object).
#### [Get Customer]
```python
client.customers.get(customerId)
```
#### [Update Customer]
`customer` object must contain `id` or `source_id`.

```python
client.customers.update(customer)
```
#### [Delete Customer]
```python
client.customers.delete(customerId)
```

### Async Actions API
Methods are provided within `client.asyncActions.*` namespace.
- [Get Async Action](#get-async-action)
- [List Async Actions](#list-async-actions)

#### [Get Async Action]
```python
client.asyncActions.get(id);
```
#### [List Async Actions]
```python
client.asyncActions.list(params);
```

---

### Utils

```python
from voucherify import utils
```

#### Available methods

- `utils.calculate_price(base_price, voucher, unit_price)`
- `utils.calculate_discount(base_price, voucher, unit_price)`

---

## Contributing

Bug reports and pull requests are welcome through [GitHub Issues](https://github.com/voucherifyio/voucherify-python-sdk/issues).

## Changelog

- **2021-05-26** - `2.2.1`
  - Upload new version to pypi.org. No changes compared to `2.2.0`
- **2021-05-20** - `2.2.0`
  - Added `client.validations*` member
  - Added method `validateVoucher` to `client.validations`
  - Changed default timeout from  500 minutes to 3 minutes. Made timeout configurable
  - Bugfix: Fixed raising exception when response json contains property "error"
- **2019-06-19** - `2.1.0` Added support for custom API endpoint, that allows to connect to projects created in specific Voucherify region.
- **2018-01-20** - `2.0.0`
  - Moved vouchers related methods to `client.vouchers.*` namespace
  - Moved redemptions related methods to `client.redemptions.*` namespace
  - Moved distributions related methods to `client.distributions.*` namespace
  - Renamed `client.customer.*` to `client.customers.*`
  - Removed outdated `client.distributions.publish(campaignName)` method interface
  - Fixed utils methods to accept vouchers with `None` gift
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

[Get Async Action]: https://docs.voucherify.io/reference?utm_source=github&utm_medium=sdk&utm_campaign=acq#get-async-actions-1
[List Async Actions]: https://docs.voucherify.io/reference?utm_source=github&utm_medium=sdk&utm_campaign=acq#list-async-actions

[Create Voucher]: https://docs.voucherify.io/reference?utm_source=github&utm_medium=sdk&utm_campaign=acq#create-voucher
[Get Voucher]: https://docs.voucherify.io/reference?utm_source=github&utm_medium=sdk&utm_campaign=acq#vouchers-get
[Update Voucher]: https://docs.voucherify.io/reference?utm_source=github&utm_medium=sdk&utm_campaign=acq#update-voucher
[List Vouchers]: https://docs.voucherify.io/reference?utm_source=github&utm_medium=sdk&utm_campaign=acq#list-vouchers
[Enable Voucher]: https://docs.voucherify.io/reference?utm_source=github&utm_medium=sdk&utm_campaign=acq#enable-voucher
[Disable Voucher]: https://docs.voucherify.io/reference?utm_source=github&utm_medium=sdk&utm_campaign=acq#disable-voucher

[Publish Voucher]: https://docs.voucherify.io/reference?utm_source=github&utm_medium=sdk&utm_campaign=acq#create-publication

[Validate Voucher]: https://docs.voucherify.io/reference?utm_source=github&utm_medium=sdk&utm_campaign=acq#validate-voucher

[Redeem Voucher]: https://docs.voucherify.io/reference?utm_source=github&utm_medium=sdk&utm_campaign=acq#redeem-voucher
[List Redemptions]: https://docs.voucherify.io/reference?utm_source=github&utm_medium=sdk&utm_campaign=acq#list-redemptions
[Get Voucher's Redemptions]: https://docs.voucherify.io/reference?utm_source=github&utm_medium=sdk&utm_campaign=acq#vouchers-redemptions
[Rollback Redemption]: https://docs.voucherify.io/reference?utm_source=github&utm_medium=sdk&utm_campaign=acq#rollback-redemption

[Create Customer]: https://docs.voucherify.io/reference?utm_source=github&utm_medium=sdk&utm_campaign=acq#create-customer
[Get Customer]: https://docs.voucherify.io/reference?utm_source=github&utm_medium=sdk&utm_campaign=acq#read-customer
[Update Customer]: https://docs.voucherify.io/reference?utm_source=github&utm_medium=sdk&utm_campaign=acq#update-customer
[Delete Customer]: https://docs.voucherify.io/reference?utm_source=github&utm_medium=sdk&utm_campaign=acq#delete-customer
