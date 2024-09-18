# voucherify.ValidationsApi

All URIs are relative to *https://api.voucherify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**validate_stacked_discounts**](ValidationsApi.md#validate_stacked_discounts) | **POST** /v1/validations | Validate Stackable Discounts


# **validate_stacked_discounts**
> ValidationsValidateResponseBody validate_stacked_discounts(validations_validate_request_body=validations_validate_request_body)

Validate Stackable Discounts

Verify redeemables provided in the request. This method is designed for server side integration which means that it is accessible only through private keys.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.validations_validate_request_body import ValidationsValidateRequestBody
from voucherify.models.validations_validate_response_body import ValidationsValidateResponseBody
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
    api_instance = voucherify.ValidationsApi(api_client)
    validations_validate_request_body = {"customer":{"source_id":"sample_customer","metadata":{"key":"value"}},"options":{"expand":["order","redeemable","category"]},"redeemables":[{"object":"voucher","id":"voucher-code"}],"session":{"type":"LOCK"},"order":{"amount":55000,"status":"PAID","items":[{"quantity":2,"price":20000,"source_id":"sample product1","related_object":"product","product":{"metadata":{"key":"value"}}},{"quantity":1,"price":15000,"source_id":"sample product2","related_object":"product","product":{"metadata":{"key":"value"}}}],"metadata":{"key":"value"}}} # ValidationsValidateRequestBody |  (optional)

    try:
        # Validate Stackable Discounts
        api_response = api_instance.validate_stacked_discounts(validations_validate_request_body=validations_validate_request_body)
        print("The response of ValidationsApi->validate_stacked_discounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValidationsApi->validate_stacked_discounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validations_validate_request_body** | [**ValidationsValidateRequestBody**](ValidationsValidateRequestBody.md)|  | [optional] 

### Return type

[**ValidationsValidateResponseBody**](ValidationsValidateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Depending on your project settings: all redeemables must be valid or just one must be valid to result as valid validation. See https://support.voucherify.io/article/604-stacking-rules#application-rules |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

