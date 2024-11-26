# voucherify.VouchersApi

All URIs are relative to *https://api.voucherify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_voucher**](VouchersApi.md#create_voucher) | **POST** /v1/vouchers/{code} | Create Voucher
[**delete_voucher**](VouchersApi.md#delete_voucher) | **DELETE** /v1/vouchers/{code} | Delete Voucher
[**disable_voucher**](VouchersApi.md#disable_voucher) | **POST** /v1/vouchers/{code}/disable | Disable Voucher
[**enable_voucher**](VouchersApi.md#enable_voucher) | **POST** /v1/vouchers/{code}/enable | Enable Voucher
[**export_voucher_transactions**](VouchersApi.md#export_voucher_transactions) | **POST** /v1/vouchers/{code}/transactions/export | Export Voucher Transactions
[**generate_random_code**](VouchersApi.md#generate_random_code) | **POST** /v1/vouchers | Generate Random Code
[**get_voucher**](VouchersApi.md#get_voucher) | **GET** /v1/vouchers/{code} | Get Voucher
[**import_vouchers**](VouchersApi.md#import_vouchers) | **POST** /v1/vouchers/import | Import Vouchers
[**import_vouchers_using_csv**](VouchersApi.md#import_vouchers_using_csv) | **POST** /v1/vouchers/importCSV | Import Vouchers using CSV
[**list_voucher_transactions**](VouchersApi.md#list_voucher_transactions) | **GET** /v1/vouchers/{code}/transactions | List Voucher Transactions
[**list_vouchers**](VouchersApi.md#list_vouchers) | **GET** /v1/vouchers | List Vouchers
[**release_validation_session**](VouchersApi.md#release_validation_session) | **DELETE** /v1/vouchers/{code}/sessions/{sessionKey} | Release Validation Session
[**update_voucher**](VouchersApi.md#update_voucher) | **PUT** /v1/vouchers/{code} | Update Voucher
[**update_voucher_balance**](VouchersApi.md#update_voucher_balance) | **POST** /v1/vouchers/{code}/balance | Add or Remove Voucher Balance
[**update_vouchers_in_bulk**](VouchersApi.md#update_vouchers_in_bulk) | **POST** /v1/vouchers/bulk/async | Update Vouchers in Bulk
[**update_vouchers_metadata_in_bulk**](VouchersApi.md#update_vouchers_metadata_in_bulk) | **POST** /v1/vouchers/metadata/async | Update Vouchers&#39; Metadata in Bulk


# **create_voucher**
> VouchersCreateResponseBody create_voucher(code, vouchers_create_with_specific_code_request_body=vouchers_create_with_specific_code_request_body)

Create Voucher

Create a standalone voucher. You can choose to create a GIFT_VOUCHER, a DISCOUNT_VOUCHER, or a LOYALTY_CARD. The code path parameter can use all letters of the English alphabet, Arabic numerals and special characters. When you create a new voucher, you can specify a type to create it. Creating a new voucher will create a new standalone voucher if no campaign name or campaign_id is provided. However, if an ID or name of a campaign with the type set to STANDALONE is provided, the voucher will be added to such campaign. In the case of the loyalty card, a campaign name or ID is required. 🚧 Standalone Vouchers and Campaigns In version [v20241004](https://support.voucherify.io/article/23-whats-new-in-voucherify#v20241004), standalone vouchers created through the Voucherify dashboard create a campaign for that voucher. However, vouchers created through the API do not have a campaign attached, so the values for campaign and campaign_id are null. Voucherify developers work on adding an optional feature to create a standalone voucher campaign through the API. Follow the [Voucherify Release Notes](https://support.voucherify.io/article/23-whats-new-in-voucherify#v20241004) for more details about released features.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.vouchers_create_response_body import VouchersCreateResponseBody
from voucherify.models.vouchers_create_with_specific_code_request_body import VouchersCreateWithSpecificCodeRequestBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.VouchersApi(api_client)
    code = 'code_example' # str | A unique **code** that identifies the voucher.
    vouchers_create_with_specific_code_request_body = {"category":"New Customers","type":"DISCOUNT_VOUCHER","discount":{"percent_off":10,"type":"PERCENT","effect":"APPLY_TO_ORDER"},"start_date":"2022-01-01T00:00:00Z","expiration_date":"2022-12-31T23:59:59Z","validity_timeframe":{"duration":"PT1H","interval":"P2D"},"validity_day_of_week":[1,2,3,4,5],"active":false,"additional_info":"This voucher will remain inactive until enabled.","redemption":{"quantity":10},"metadata":{"test":true,"locale":"de-en"},"validation_rules":["val_4j7DCRm2IS59"]} # VouchersCreateWithSpecificCodeRequestBody | Specify the details of the voucher that you would like to create. (optional)

    try:
        # Create Voucher
        api_response = api_instance.create_voucher(code, vouchers_create_with_specific_code_request_body=vouchers_create_with_specific_code_request_body)
        print("The response of VouchersApi->create_voucher:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VouchersApi->create_voucher: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| A unique **code** that identifies the voucher. | 
 **vouchers_create_with_specific_code_request_body** | [**VouchersCreateWithSpecificCodeRequestBody**](VouchersCreateWithSpecificCodeRequestBody.md)| Specify the details of the voucher that you would like to create. | [optional] 

### Return type

[**VouchersCreateResponseBody**](VouchersCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a voucher object if the call succeeded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_voucher**
> delete_voucher(code, force=force)

Delete Voucher

Deletes a voucher. This operation cannot be undone. Additionally, this operation removes any redemptions on the voucher. If the force parameter is set to false or not set at all, the voucher will be moved to the bin.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.VouchersApi(api_client)
    code = 'code_example' # str | A unique **code** that identifies the voucher.
    force = True # bool | If this flag is set to true, the voucher will be removed permanently. If it is set to false or not set at all, the voucher will be moved to the bin. Going forward, the user will be able to create another voucher with exactly the same code. (optional)

    try:
        # Delete Voucher
        api_instance.delete_voucher(code, force=force)
    except Exception as e:
        print("Exception when calling VouchersApi->delete_voucher: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| A unique **code** that identifies the voucher. | 
 **force** | **bool**| If this flag is set to true, the voucher will be removed permanently. If it is set to false or not set at all, the voucher will be moved to the bin. Going forward, the user will be able to create another voucher with exactly the same code. | [optional] 

### Return type

void (empty response body)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns no content if deletion is successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_voucher**
> VouchersDisableResponseBody disable_voucher(code)

Disable Voucher

There are various times when youll want to manage a vouchers accessibility. This can be done by two API methods for managing the voucher state - *enable* and *disable*.   ___ This method sets the voucher state to **inactive**. The voucher cannot be redeemed.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.vouchers_disable_response_body import VouchersDisableResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.VouchersApi(api_client)
    code = 'code_example' # str | A **code** that identifies the voucher or a unique voucher ID assigned by Voucherify, i.e. v_TzD19aeNiqGc9LWciMWknyEZT8IW7u4u.

    try:
        # Disable Voucher
        api_response = api_instance.disable_voucher(code)
        print("The response of VouchersApi->disable_voucher:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VouchersApi->disable_voucher: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| A **code** that identifies the voucher or a unique voucher ID assigned by Voucherify, i.e. v_TzD19aeNiqGc9LWciMWknyEZT8IW7u4u. | 

### Return type

[**VouchersDisableResponseBody**](VouchersDisableResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a voucher object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_voucher**
> VouchersEnableResponseBody enable_voucher(code)

Enable Voucher

There are various times when youll want to manage a vouchers accessibility. This can be done by two API methods for managing the voucher state - *enable* and *disable*.   ___ The method sets the voucher state to **active**. The voucher can be redeemed - only if the redemption occurs after the start date and the voucher is not expired.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.vouchers_enable_response_body import VouchersEnableResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.VouchersApi(api_client)
    code = 'code_example' # str | A **code** that identifies the voucher or a unique voucher ID assigned by Voucherify, i.e. v_TzD19aeNiqGc9LWciMWknyEZT8IW7u4u.

    try:
        # Enable Voucher
        api_response = api_instance.enable_voucher(code)
        print("The response of VouchersApi->enable_voucher:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VouchersApi->enable_voucher: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| A **code** that identifies the voucher or a unique voucher ID assigned by Voucherify, i.e. v_TzD19aeNiqGc9LWciMWknyEZT8IW7u4u. | 

### Return type

[**VouchersEnableResponseBody**](VouchersEnableResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a voucher object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_voucher_transactions**
> VouchersTransactionsExportCreateResponseBody export_voucher_transactions(code, vouchers_transactions_export_create_request_body=vouchers_transactions_export_create_request_body)

Export Voucher Transactions

Export transactions that are associated with credit movements on a gift card or loyalty card.   

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.vouchers_transactions_export_create_request_body import VouchersTransactionsExportCreateRequestBody
from voucherify.models.vouchers_transactions_export_create_response_body import VouchersTransactionsExportCreateResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.VouchersApi(api_client)
    code = 'GIFT-CARD-1' # str | A **code** that identifies the voucher or a unique voucher ID assigned by Voucherify, i.e. v_TzD19aeNiqGc9LWciMWknyEZT8IW7u4u.
    vouchers_transactions_export_create_request_body = {"parameters":{"order":"-created_at","fields":["id","type","source_id","reason","balance","amount","created_at","voucher_id","campaign_id","details","source"]}} # VouchersTransactionsExportCreateRequestBody | Specify the parameters for the camapign transaction export. (optional)

    try:
        # Export Voucher Transactions
        api_response = api_instance.export_voucher_transactions(code, vouchers_transactions_export_create_request_body=vouchers_transactions_export_create_request_body)
        print("The response of VouchersApi->export_voucher_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VouchersApi->export_voucher_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| A **code** that identifies the voucher or a unique voucher ID assigned by Voucherify, i.e. v_TzD19aeNiqGc9LWciMWknyEZT8IW7u4u. | 
 **vouchers_transactions_export_create_request_body** | [**VouchersTransactionsExportCreateRequestBody**](VouchersTransactionsExportCreateRequestBody.md)| Specify the parameters for the camapign transaction export. | [optional] 

### Return type

[**VouchersTransactionsExportCreateResponseBody**](VouchersTransactionsExportCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns an export object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_random_code**
> VouchersCreateResponseBody generate_random_code(vouchers_create_request_body=vouchers_create_request_body)

Generate Random Code

Create a standalone voucher. You can choose to create a GIFT_VOUCHER, a DISCOUNT_VOUCHER, or a LOYALTY_CARD.  When you create a new voucher, you can specify a type to create it. Creating a new voucher will create a new standalone voucher if no campaign name or campaign_id is provided. However, if an ID or name of a campaign with the type set to STANDALONE is provided, the voucher will be added to such campaign. In case of the loyalty card, a campaign name is required. You can optionally use the code parameter to define a specific code or the code_config parameter to design rules for Voucherify API to create a random code. If neither of the two parameters are passed, then a random code is generated by the Voucherify API. This method will return an error when trying to create a voucher that already exists. 🚧 Standalone Vouchers and Campaigns In version [v20241004](https://support.voucherify.io/article/23-whats-new-in-voucherify#v20241004), standalone vouchers created through the Voucherify dashboard create a campaign for that voucher. However, vouchers created through the API do not have a campaign attached, so the values for campaign and campaign_id are null. Voucherify developers work on adding an optional feature to create a standalone voucher campaign through the API. Follow the [Voucherify Release Notes](https://support.voucherify.io/article/23-whats-new-in-voucherify#v20241004) for more details about released features.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.vouchers_create_request_body import VouchersCreateRequestBody
from voucherify.models.vouchers_create_response_body import VouchersCreateResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.VouchersApi(api_client)
    vouchers_create_request_body = {"category":"New Customers","code":"NEW-WELCOME-COUPON","type":"DISCOUNT_VOUCHER","campaign_id":"camp_Y6dLsYIZloGqP8izufXY6SSJ","discount":{"percent_off":10,"type":"PERCENT","effect":"APPLY_TO_ORDER"},"start_date":"2016-01-01T00:00:00Z","expiration_date":"2022-12-31T23:59:59Z","validity_timeframe":{"duration":"PT1H","interval":"P2D"},"validity_day_of_week":[1,2,3,4,5],"active":false,"additional_info":"This voucher will remain inactive until enabled.","redemption":{"quantity":10},"metadata":{"test":true,"locale":"de-en"},"validation_rules":["val_4j7DCRm2IS59"]} # VouchersCreateRequestBody | Specify the details of the voucher that you would like to create. (optional)

    try:
        # Generate Random Code
        api_response = api_instance.generate_random_code(vouchers_create_request_body=vouchers_create_request_body)
        print("The response of VouchersApi->generate_random_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VouchersApi->generate_random_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vouchers_create_request_body** | [**VouchersCreateRequestBody**](VouchersCreateRequestBody.md)| Specify the details of the voucher that you would like to create. | [optional] 

### Return type

[**VouchersCreateResponseBody**](VouchersCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a voucher object if the call succeeded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_voucher**
> VouchersGetResponseBody get_voucher(code)

Get Voucher

Retrieves the voucher with the given code or unique Voucherify ID. You can either pass the voucher ID which was assigned by Voucherify, e.g., v_7HxHkf4VAkMuc8u4lZs78lyRwhRze5UE, or the code of the voucher as the path parameter value, e.g., 7fjWdr.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.vouchers_get_response_body import VouchersGetResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.VouchersApi(api_client)
    code = 'code_example' # str | A unique **code** that identifies the voucher.

    try:
        # Get Voucher
        api_response = api_instance.get_voucher(code)
        print("The response of VouchersApi->get_voucher:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VouchersApi->get_voucher: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| A unique **code** that identifies the voucher. | 

### Return type

[**VouchersGetResponseBody**](VouchersGetResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a voucher object if a valid identifier was provided.   Additionally, the response returns validation rules related to the voucher object. They can be inherited from a campaign. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_vouchers**
> VouchersImportCreateResponseBody import_vouchers(vouchers_import_create_item_request_body)

Import Vouchers

Import standalone vouchers and gift cards into the repository.  📘 Important notes  - **Start and expiration dates** need to be provided in compliance with the ISO 8601 norms. For example, 2020-03-11T09:00:00.000Z.  - Custom code attributes (not supported by-default) need to be added as code **metadata**.  - You **cannot import the same codes** to a single Voucherify Project. Any parameters not provided in the payload will be left blank or null. For both **standalone discount vouchers and gift cards**, you can import the following fields:   - code - category - active - type - start_date - expiration_date - redemption.quantity - additional_info - metadata For **gift cards**, you can also import the following field: - gift.amount For **discount vouchers**, you can import the discount object. The object will slightly vary depending on the type of discount. Each discount type **requires** the type to be defined in the import.   Fields other than the ones listed above wont be imported. Even if provided, they will be silently skipped. This API request starts a process that affects Voucherify data in bulk.  In case of small jobs (like bulk update) the request is put into a queue and processed once every other bulk request placed in the queue prior to this request is finished. However, when the job takes a longer time (like vouchers generation) then it is processed in small portions in a round-robin fashion. When there is a list of vouchers generation scheduled, then they will all have the IN_PROGRESS status shortly. This way, small jobs added just after scheduling big jobs of the same type will be processed in a short time window.  The result will return the async ID. You can verify the status of your request via this API request. 🚧 Standalone Vouchers and Campaigns In version [v20241004](https://support.voucherify.io/article/23-whats-new-in-voucherify#v20241004), standalone vouchers created through the Voucherify dashboard create a campaign for that voucher. However, vouchers imported through the dashboard in the Vouchers section or through the API do not have a campaign attached, so the values for campaign and campaign_id are null.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.vouchers_import_create_item_request_body import VouchersImportCreateItemRequestBody
from voucherify.models.vouchers_import_create_response_body import VouchersImportCreateResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.VouchersApi(api_client)
    vouchers_import_create_item_request_body = [{"code":"PROMO-CODE30OFF-NO-EFFECT","category":"new customer acquisition","type":"DISCOUNT_VOUCHER","active":true,"discount":{"amount_off":3000,"type":"AMOUNT"},"start_date":"2020-12-01T23:00:00Z","expiration_date":"2023-12-19T23:00:00Z","redemption":{"quantity":1},"metadata":{"unit":"EUR"},"additional_info":"secret-code1"},{"code":"PROMO-CODE30-PERCENT-NO-EFFECT","type":"DISCOUNT_VOUCHER","active":false,"discount":{"percent_off":30,"type":"PERCENT"},"start_date":"2020-12-10T23:00:00Z","expiration_date":"2023-12-31T23:00:00Z","redemption":{"quantity":1},"metadata":{"unit":"EUR"},"additional_info":"secret-code2"},{"code":"GIFT-CARD-100","type":"GIFT_VOUCHER","active":true,"category":"new customer acquisition","gift":{"amount":10000},"start_date":"2020-12-10T23:00:00Z","expiration_date":"2023-12-31T23:00:00Z","redemption":{"quantity":5},"metadata":{"unit":"EUR"},"additional_info":"secret-GIFT-code2"},{"code":"PROMO-CODE1-PERCENT-EFFECT-ORDER","type":"DISCOUNT_VOUCHER","active":false,"discount":{"percent_off":30,"type":"PERCENT","effect":"APPLY_TO_ORDER"},"start_date":"2020-12-10T23:00:00Z","expiration_date":"2023-12-31T23:00:00Z","redemption":{"quantity":1},"metadata":{"unit":"EUR"},"additional_info":"secret-code2"},{"code":"PROMO-CODE2-PERCENT-EFFECT-ITEM","type":"DISCOUNT_VOUCHER","active":false,"discount":{"percent_off":30,"type":"PERCENT","effect":"APPLY_TO_ITEMS"},"start_date":"2020-12-10T23:00:00Z","expiration_date":"2023-12-31T23:00:00Z","redemption":{"quantity":1},"metadata":{"unit":"EUR"},"additional_info":"secret-code2"},{"code":"PROMO-CODE1-PERCENT-NO-EFFECT-REDEEMED-QUANTITY-ATTRIBUTE-DOESNT-GET-PASSED","type":"DISCOUNT_VOUCHER","active":false,"discount":{"percent_off":30,"type":"PERCENT"},"start_date":"2020-12-10T23:00:00Z","expiration_date":"2023-12-31T23:00:00Z","redemption":{"quantity":1,"redeemed_quantity":1},"metadata":{"unit":"EUR"},"additional_info":"secret-code2"},{"code":"PROMO-CODE1-AMOUNT-EFFECT-ITEMS-PROPORTIONALLY","type":"DISCOUNT_VOUCHER","active":false,"discount":{"amount_off":30,"type":"AMOUNT","effect":"APPLY_TO_ITEMS_PROPORTIONALLY"},"start_date":"2020-12-10T23:00:00Z","expiration_date":"2023-12-31T23:00:00Z","redemption":{"quantity":1},"metadata":{"unit":"EUR"},"additional_info":"secret-code2"},{"code":"PROMO-CODE1-FIXED-EFFECT-ORDER","type":"DISCOUNT_VOUCHER","active":false,"discount":{"fixed_amount":30,"type":"FIXED","effect":"APPLY_TO_ORDER"},"start_date":"2020-12-10T23:00:00Z","expiration_date":"2023-12-31T23:00:00Z","redemption":{"quantity":1},"metadata":{"unit":"EUR"},"additional_info":"secret-code2"},{"code":"PROMO-CODE1-UNIT-SINGLE-ITEM-EFFECT-MISSING","type":"DISCOUNT_VOUCHER","active":false,"discount":{"unit_off":1,"unit_type":"prod_0a9f9aeddb019a42db","type":"UNIT","effect":"ADD_MISSING_ITEMS"},"start_date":"2020-12-10T23:00:00Z","expiration_date":"2023-12-31T23:00:00Z","redemption":{"quantity":1},"metadata":{"unit":"EUR"},"additional_info":"secret-code2"},{"code":"PROMO-CODE2-UNIT-MULTIPLE-ITEMS","type":"DISCOUNT_VOUCHER","active":true,"discount":{"type":"UNIT","effect":"ADD_MANY_ITEMS","units":[{"unit_off":1,"unit_type":"prod_0a9f9aeddb019a42db","effect":"ADD_MISSING_ITEMS"},{"unit_off":1,"unit_type":"prod_0a9f9aeddb019a42db","effect":"ADD_NEW_ITEMS"}]},"start_date":"2020-12-10T23:00:00Z","expiration_date":"2023-12-31T23:00:00Z","redemption":{"quantity":1},"metadata":{"unit":"EUR"},"additional_info":"secret-code2"},{"code":"PROMO-CODE1-SHIPPING","type":"DISCOUNT_VOUCHER","active":false,"discount":{"type":"UNIT","unit_off":1,"unit_type":"prod_5h1pp1ng","effect":"ADD_MISSING_ITEMS"},"start_date":"2020-12-10T23:00:00Z","expiration_date":"2023-12-31T23:00:00Z","redemption":{"quantity":1},"metadata":{"unit":"EUR"},"additional_info":"secret-code2"}] # List[VouchersImportCreateItemRequestBody] | The request body is an array of objects. Each object contains details about a specific voucher. 

    try:
        # Import Vouchers
        api_response = api_instance.import_vouchers(vouchers_import_create_item_request_body)
        print("The response of VouchersApi->import_vouchers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VouchersApi->import_vouchers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vouchers_import_create_item_request_body** | [**List[VouchersImportCreateItemRequestBody]**](VouchersImportCreateItemRequestBody.md)| The request body is an array of objects. Each object contains details about a specific voucher.  | 

### Return type

[**VouchersImportCreateResponseBody**](VouchersImportCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns ID of the scheduled async action. The response informs you that your request has been accepted and vouchers will be added to the repository asynchronously. To check the import status and result, copy the &#x60;async_action_id&#x60; from the response and pass it using the &lt;!-- [Get Async Action](OpenAPI.json/paths/~1async-actions~1{asyncActionId}/get) --&gt;[Get Async Action](ref:get-async-action) endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_vouchers_using_csv**
> VouchersImportCsvCreateResponseBody import_vouchers_using_csv(file=file)

Import Vouchers using CSV

Import standalone vouchers into the repository using a CSV file. The CSV file has to include headers in the first line. All properties listed in the file headers that cannot be mapped to standard voucher fields will be added to the metadata object.   You can find an example CSV file [here](https://support.voucherify.io/article/45-import-codes-and-share-them-digitally#coupons). ___  📘 Standard voucher fields mapping  - Go to the import vouchers endpoint to see all standard CSV fields description (body params section).  - Supported CSV file headers: Code,Voucher Type,Value,Discount Type,Category,Start Date,Expiration Date,Redemption Limit,Redeemed Quantity, Redeemed Amount,Active,Additional Info,Custom Metadata Property Name - **Start and expiration dates** need to be provided in compliance with the ISO 8601 norms. For example, 2020-03-11T09:00:00.000Z.       - YYYY-MM-DD     - YYYY-MM-DDTHH     - YYYY-MM-DDTHH:mm     - YYYY-MM-DDTHH:mm:ss     - YYYY-MM-DDTHH:mm:ssZ     - YYYY-MM-DDTHH:mm:ssZ     - YYYY-MM-DDTHH:mm:ss.SSSZ  - Custom code attributes (not supported by-default) need to be added as code **metadata**.  - You **cannot import the same codes** to a single Voucherify Project.  📘 Categories  In the structure representing your data, you can define a category that the voucher belongs to. You can later use the category of a voucher to group and search by specific criteria in the Dashboard and using the List Vouchers endpoint. This API request starts a process that affects Voucherify data in bulk.  In case of small jobs (like bulk update) the request is put into a queue and processed once every other bulk request placed in the queue prior to this request is finished. However, when the job takes a longer time (like vouchers generation) then it is processed in small portions in a round-robin fashion. When there is a list of vouchers generation scheduled, then they will all have the IN_PROGRESS status shortly. This way, small jobs added just after scheduling big jobs of the same type will be processed in a short time window.  The result will return the async ID. You can verify the status of your request via this API request. 🚧 Standalone Vouchers and Campaigns In version [v20241004](https://support.voucherify.io/article/23-whats-new-in-voucherify#v20241004), standalone vouchers created through the Voucherify dashboard create a campaign for that voucher. However, vouchers imported through the dashboard in the Vouchers section or through the API do not have a campaign attached, so the values for campaign and campaign_id are null.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.vouchers_import_csv_create_response_body import VouchersImportCsvCreateResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.VouchersApi(api_client)
    file = None # bytearray | File path. (optional)

    try:
        # Import Vouchers using CSV
        api_response = api_instance.import_vouchers_using_csv(file=file)
        print("The response of VouchersApi->import_vouchers_using_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VouchersApi->import_vouchers_using_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**| File path. | [optional] 

### Return type

[**VouchersImportCsvCreateResponseBody**](VouchersImportCsvCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns ID of the scheduled async action. The response informs you that your request has been accepted and vouchers will be added to the repository asynchronously. To check the import status and result, copy the &#x60;async_action_id&#x60; from the **response** and pass it using the &lt;!-- [Get Async Action](OpenAPI.json/paths/~1async-actions~1{asyncActionId}/get) --&gt;[Get Async Action](ref:get-async-action) endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_voucher_transactions**
> VouchersTransactionsListResponseBody list_voucher_transactions(code, limit=limit, order=order, starting_after_id=starting_after_id)

List Voucher Transactions

List transactions that are associated with credit movements on a gift card or loyalty card.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.parameter_order_list_transactions import ParameterOrderListTransactions
from voucherify.models.vouchers_transactions_list_response_body import VouchersTransactionsListResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.VouchersApi(api_client)
    code = 'code_example' # str | A **code** that identifies the voucher or a unique voucher ID assigned by Voucherify, i.e. v_TzD19aeNiqGc9LWciMWknyEZT8IW7u4u.
    limit = 56 # int | Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. (optional)
    order = voucherify.ParameterOrderListTransactions() # ParameterOrderListTransactions | Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. (optional)
    starting_after_id = 'starting_after_id_example' # str | A cursor for pagination. It retrieves the transactions starting after a transaction with the given ID. (optional)

    try:
        # List Voucher Transactions
        api_response = api_instance.list_voucher_transactions(code, limit=limit, order=order, starting_after_id=starting_after_id)
        print("The response of VouchersApi->list_voucher_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VouchersApi->list_voucher_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| A **code** that identifies the voucher or a unique voucher ID assigned by Voucherify, i.e. v_TzD19aeNiqGc9LWciMWknyEZT8IW7u4u. | 
 **limit** | **int**| Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. | [optional] 
 **order** | [**ParameterOrderListTransactions**](.md)| Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. | [optional] 
 **starting_after_id** | **str**| A cursor for pagination. It retrieves the transactions starting after a transaction with the given ID. | [optional] 

### Return type

[**VouchersTransactionsListResponseBody**](VouchersTransactionsListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a dictionary of transaction objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_vouchers**
> VouchersListResponseBody list_vouchers(limit=limit, page=page, category=category, campaign_id=campaign_id, customer=customer, campaign=campaign, created_at=created_at, updated_at=updated_at, order=order, code=code, ids=ids)

List Vouchers

Returns a list of vouchers. By default, the vouchers are returned sorted by creation date, with the most recent vouchers appearing first. A maximum of 100 vouchers are returned in the response. When you get a list of vouchers, you can optionally specify query parameters to customize the number of vouchers returned per call using limit, which page of vouchers to return using page, sort the vouchers using the order query parameter and more. This method will return an error when trying to return a limit of more than 100 vouchers. 

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.parameter_created_before_after import ParameterCreatedBeforeAfter
from voucherify.models.parameter_order_vouchers import ParameterOrderVouchers
from voucherify.models.parameter_updated_before_after import ParameterUpdatedBeforeAfter
from voucherify.models.vouchers_list_response_body import VouchersListResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.VouchersApi(api_client)
    limit = 56 # int | Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. (optional)
    page = 56 # int | Which page of results to return. The lowest value is 1. (optional)
    category = 'category_example' # str | Limit search results to vouchers within the specified category. (optional)
    campaign_id = 'campaign_id_example' # str | Limit search results to vouchers within the specified campaign (optional)
    customer = 'customer_example' # str | A tracking identifier of a customer who is the holder of the vouchers. It can be an id generated by Voucherify or the source_id. Remember to use the proper URL escape codes if the source_id contains special characters. (optional)
    campaign = 'campaign_example' # str | A unique campaign name, identifies the parent campaign. (optional)
    created_at = voucherify.ParameterCreatedBeforeAfter() # ParameterCreatedBeforeAfter | A filter on the list based on the object created_at field. The value is a dictionary with the following options: before, after. A date value must be presented in ISO 8601 format (2016-11-16T14:14:31Z or 2016-11-16). An example: [created_at][before] 2017-09-08T13:52:18.227Z (optional)
    updated_at = voucherify.ParameterUpdatedBeforeAfter() # ParameterUpdatedBeforeAfter | A filter on the list based on the object updated_at field. The value is a dictionary with the following options: before, after. A date value must be presented in ISO 8601 format (2016-11-16T14:14:31Z or 2016-11-16). An example: [updated_at][before] 2017-09-08T13:52:18.227Z (optional)
    order = voucherify.ParameterOrderVouchers() # ParameterOrderVouchers | Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. (optional)
    code = 'code_example' # str |  (optional)
    ids = ['ids_example'] # List[str] |  (optional)

    try:
        # List Vouchers
        api_response = api_instance.list_vouchers(limit=limit, page=page, category=category, campaign_id=campaign_id, customer=customer, campaign=campaign, created_at=created_at, updated_at=updated_at, order=order, code=code, ids=ids)
        print("The response of VouchersApi->list_vouchers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VouchersApi->list_vouchers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. | [optional] 
 **page** | **int**| Which page of results to return. The lowest value is 1. | [optional] 
 **category** | **str**| Limit search results to vouchers within the specified category. | [optional] 
 **campaign_id** | **str**| Limit search results to vouchers within the specified campaign | [optional] 
 **customer** | **str**| A tracking identifier of a customer who is the holder of the vouchers. It can be an id generated by Voucherify or the source_id. Remember to use the proper URL escape codes if the source_id contains special characters. | [optional] 
 **campaign** | **str**| A unique campaign name, identifies the parent campaign. | [optional] 
 **created_at** | [**ParameterCreatedBeforeAfter**](.md)| A filter on the list based on the object created_at field. The value is a dictionary with the following options: before, after. A date value must be presented in ISO 8601 format (2016-11-16T14:14:31Z or 2016-11-16). An example: [created_at][before] 2017-09-08T13:52:18.227Z | [optional] 
 **updated_at** | [**ParameterUpdatedBeforeAfter**](.md)| A filter on the list based on the object updated_at field. The value is a dictionary with the following options: before, after. A date value must be presented in ISO 8601 format (2016-11-16T14:14:31Z or 2016-11-16). An example: [updated_at][before] 2017-09-08T13:52:18.227Z | [optional] 
 **order** | [**ParameterOrderVouchers**](.md)| Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. | [optional] 
 **code** | **str**|  | [optional] 
 **ids** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**VouchersListResponseBody**](VouchersListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a dictionary that contains an array of vouchers. Each entry in the array is a separate voucher object. If no more vouchers are available (query parameter &#x60;page&#x60; incremented over and above the voucher count), the resulting array will be empty. The result can be narrowed down according to specified (or default) filters. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **release_validation_session**
> release_validation_session(code, session_key)

Release Validation Session

Manually release a validation session that has been set up for the voucher. This method undos the actions that are explained in our guide on how a validation session was established, you can read more here.   📘 Release Session using Dashboard  You can also use the Validations Manager in the Dashboard to unlock sessions. [Read more](https://support.voucherify.io/article/16-dashboard-sections#validations).

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.VouchersApi(api_client)
    code = 'code_example' # str | A **code** that identifies the voucher or a unique voucher ID assigned by Voucherify.
    session_key = 'ssn_yQGMTeKBSw8OOuFPwlBEjzGy8d8VA9Ts' # str | A unique session identifier.

    try:
        # Release Validation Session
        api_instance.release_validation_session(code, session_key)
    except Exception as e:
        print("Exception when calling VouchersApi->release_validation_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| A **code** that identifies the voucher or a unique voucher ID assigned by Voucherify. | 
 **session_key** | **str**| A unique session identifier. | 

### Return type

void (empty response body)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns no content if the validation session was released successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_voucher**
> VouchersUpdateResponseBody update_voucher(code, vouchers_update_request_body)

Update Voucher

Updates the specified voucher by setting the values of the parameters passed in the request body. Any parameters not provided in the payload will be left unchanged. Fields other than the ones listed in the request body wont be modified. Even if provided, they will be silently skipped.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.vouchers_update_request_body import VouchersUpdateRequestBody
from voucherify.models.vouchers_update_response_body import VouchersUpdateResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.VouchersApi(api_client)
    code = 'code_example' # str | A unique **code** that identifies the voucher.
    vouchers_update_request_body = {"category":"Second","type":"DISCOUNT_VOUCHER","discount":{"type":"PERCENT","percent_off":45,"percent_off_formula":"IF(ORDER_AMOUNT > 100;CUSTOMER_METADATA(\"age\");CUSTOMER_METADATA(\"age\") / 2)","amount_limit":1800,"effect":"APPLY_TO_ORDER"},"start_date":"2020-02-01T00:00:00Z","expiration_date":"2023-12-31T23:59:59Z","validity_timeframe":{"duration":"PT2H","interval":"P3D"},"validity_day_of_week":[0,1,2],"active":false,"additional_info":"This voucher can be used with other coupons. Please feel free to do so.","metadata":{"Season":"Winter"}} # VouchersUpdateRequestBody | Specify the parameters to be updated.

    try:
        # Update Voucher
        api_response = api_instance.update_voucher(code, vouchers_update_request_body)
        print("The response of VouchersApi->update_voucher:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VouchersApi->update_voucher: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| A unique **code** that identifies the voucher. | 
 **vouchers_update_request_body** | [**VouchersUpdateRequestBody**](VouchersUpdateRequestBody.md)| Specify the parameters to be updated. | 

### Return type

[**VouchersUpdateResponseBody**](VouchersUpdateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the voucher object if the update succeeded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_voucher_balance**
> VouchersBalanceUpdateResponseBody update_voucher_balance(code, vouchers_balance_update_request_body)

Add or Remove Voucher Balance

Add balance to an existing gift card or loyalty card.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.vouchers_balance_update_request_body import VouchersBalanceUpdateRequestBody
from voucherify.models.vouchers_balance_update_response_body import VouchersBalanceUpdateResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.VouchersApi(api_client)
    code = 'code_example' # str | A **code** that identifies the voucher or a unique voucher ID assigned by Voucherify, i.e. v_TzD19aeNiqGc9LWciMWknyEZT8IW7u4u.
    vouchers_balance_update_request_body = {"amount":10000} # VouchersBalanceUpdateRequestBody | Provide the amount to be added to/subtracted from the voucher.

    try:
        # Add or Remove Voucher Balance
        api_response = api_instance.update_voucher_balance(code, vouchers_balance_update_request_body)
        print("The response of VouchersApi->update_voucher_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VouchersApi->update_voucher_balance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| A **code** that identifies the voucher or a unique voucher ID assigned by Voucherify, i.e. v_TzD19aeNiqGc9LWciMWknyEZT8IW7u4u. | 
 **vouchers_balance_update_request_body** | [**VouchersBalanceUpdateRequestBody**](VouchersBalanceUpdateRequestBody.md)| Provide the amount to be added to/subtracted from the voucher. | 

### Return type

[**VouchersBalanceUpdateResponseBody**](VouchersBalanceUpdateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a balance object if the operation succeeded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vouchers_in_bulk**
> VouchersUpdateInBulkResponseBody update_vouchers_in_bulk(vouchers_update_in_bulk_item_request_body)

Update Vouchers in Bulk

Updates specific metadata parameters for each code, respectively, in one asynchronous operation. The request can include up to **10 MB** of data. Upserts are not supported.  🚧    Currently, only **metadata** updates are supported. The response returns a unique asynchronous action ID. Use this ID in the query paramater of the GET Async Action endpoint to check, e.g.: - The status of your request (in queue, in progress, done, or failed) - Resources that failed to be updated - The report file with details about the update This API request starts a process that affects Voucherify data in bulk. In the case of small jobs (like bulk update), the request is put into a queue and processed when every other bulk request placed in the queue prior to this request is finished.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.vouchers_update_in_bulk_item_request_body import VouchersUpdateInBulkItemRequestBody
from voucherify.models.vouchers_update_in_bulk_response_body import VouchersUpdateInBulkResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.VouchersApi(api_client)
    vouchers_update_in_bulk_item_request_body = [{"code":"example_code","metadata":{"lang":"en","test":false,"MetadataTest":"Update metadata","update_value":1,"next_update_date":"2022-11-11T09:00:00.000Z"}},{"code":"example_code2","metadata":{"lang":"pl","test":false,"MetadataTest":"Update metadata","update_value":2}}] # List[VouchersUpdateInBulkItemRequestBody] | List the codes to be updated with the metadata key/value pairs for that code.

    try:
        # Update Vouchers in Bulk
        api_response = api_instance.update_vouchers_in_bulk(vouchers_update_in_bulk_item_request_body)
        print("The response of VouchersApi->update_vouchers_in_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VouchersApi->update_vouchers_in_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vouchers_update_in_bulk_item_request_body** | [**List[VouchersUpdateInBulkItemRequestBody]**](VouchersUpdateInBulkItemRequestBody.md)| List the codes to be updated with the metadata key/value pairs for that code. | 

### Return type

[**VouchersUpdateInBulkResponseBody**](VouchersUpdateInBulkResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the ID of the scheduled asynchronous action. The response informs you that the request has been accepted and the resources will be updated in the repository asynchronously. To check the status and result, copy the &#x60;async_action_id&#x60; from the response and use it as a query parameter in the [GET Async Action](ref:get-async-action) endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vouchers_metadata_in_bulk**
> VouchersMetadataUpdateInBulkResponseBody update_vouchers_metadata_in_bulk(vouchers_metadata_update_in_bulk_request_body)

Update Vouchers' Metadata in Bulk

Updates metadata parameters for a list of codes. Every resource in the list will receive the metadata defined in the request. The request can include up to **10 MB** of data. Upserts are not supported. The response returns a unique asynchronous action ID. Use this ID in the query paramater of the GET Async Action endpoint to check, e.g.: - The status of your request (in queue, in progress, done, or failed) - Resources that failed to be updated - The report file with details about the update This API request starts a process that affects Voucherify data in bulk. In the case of small jobs (like bulk update), the request is put into a queue and processed when every other bulk request placed in the queue prior to this request is finished.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.vouchers_metadata_update_in_bulk_request_body import VouchersMetadataUpdateInBulkRequestBody
from voucherify.models.vouchers_metadata_update_in_bulk_response_body import VouchersMetadataUpdateInBulkResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.VouchersApi(api_client)
    vouchers_metadata_update_in_bulk_request_body = {"codes":["PROMO-CODE810","PROMO-CODE726"],"metadata":{"lang":"en","authorized_internally":true}} # VouchersMetadataUpdateInBulkRequestBody | List the codes of the vouchers you would like to update with the metadata key/value pairs.

    try:
        # Update Vouchers' Metadata in Bulk
        api_response = api_instance.update_vouchers_metadata_in_bulk(vouchers_metadata_update_in_bulk_request_body)
        print("The response of VouchersApi->update_vouchers_metadata_in_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VouchersApi->update_vouchers_metadata_in_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vouchers_metadata_update_in_bulk_request_body** | [**VouchersMetadataUpdateInBulkRequestBody**](VouchersMetadataUpdateInBulkRequestBody.md)| List the codes of the vouchers you would like to update with the metadata key/value pairs. | 

### Return type

[**VouchersMetadataUpdateInBulkResponseBody**](VouchersMetadataUpdateInBulkResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the ID of the scheduled asynchronous action. The response informs you that the request has been accepted and the resources will be updated in the repository asynchronously. To check the status and result, copy the &#x60;async_action_id&#x60; from the response and use it as a query parameter in the [GET Async Action](ref:get-async-action) endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

