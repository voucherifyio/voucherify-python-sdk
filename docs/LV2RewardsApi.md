# voucherify.LV2RewardsApi

All URIs are relative to *https://api.voucherify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_reward**](LV2RewardsApi.md#get_reward) | **GET** /v2/loyalties/rewards/{rewardId} | Get reward by ID


# **get_reward**
> V2LoyaltiesRewardsGetResponseBody get_reward(reward_id)

Get reward by ID

Returns a single reward by its ID.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.v2_loyalties_rewards_get_response_body import V2LoyaltiesRewardsGetResponseBody
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
    api_instance = voucherify.LV2RewardsApi(api_client)
    reward_id = 'reward_id_example' # str | Identifies the reward. Format lrew_[a-f0-9]+.

    try:
        # Get reward by ID
        api_response = api_instance.get_reward(reward_id)
        print("The response of LV2RewardsApi->get_reward:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2RewardsApi->get_reward: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reward_id** | **str**| Identifies the reward. Format lrew_[a-f0-9]+. | 

### Return type

[**V2LoyaltiesRewardsGetResponseBody**](V2LoyaltiesRewardsGetResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | The reward. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

