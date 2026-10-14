# voucherify.LV2EarningRulesApi

All URIs are relative to *https://api.voucherify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_earning_rule**](LV2EarningRulesApi.md#get_earning_rule) | **GET** /v2/loyalties/earning-rules/{earningRuleId} | Get earning rule


# **get_earning_rule**
> V2LoyaltiesEarningRulesGetResponseBody get_earning_rule(earning_rule_id)

Get earning rule

Returns a single earning rule by its ID.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.v2_loyalties_earning_rules_get_response_body import V2LoyaltiesEarningRulesGetResponseBody
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
    api_instance = voucherify.LV2EarningRulesApi(api_client)
    earning_rule_id = 'earning_rule_id_example' # str | Earning rule ID.

    try:
        # Get earning rule
        api_response = api_instance.get_earning_rule(earning_rule_id)
        print("The response of LV2EarningRulesApi->get_earning_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2EarningRulesApi->get_earning_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **earning_rule_id** | **str**| Earning rule ID. | 

### Return type

[**V2LoyaltiesEarningRulesGetResponseBody**](V2LoyaltiesEarningRulesGetResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Earning rule |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

