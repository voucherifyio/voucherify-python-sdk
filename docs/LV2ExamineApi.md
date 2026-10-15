# voucherify.LV2ExamineApi

All URIs are relative to *https://api.voucherify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**examine_earning_rules**](LV2ExamineApi.md#examine_earning_rules) | **POST** /v2/loyalties/examine/earning-rules | Examine earning rules
[**examine_rewards**](LV2ExamineApi.md#examine_rewards) | **POST** /v2/loyalties/examine/rewards | Examine rewards


# **examine_earning_rules**
> LoyaltiesExamineEarningRulesExamineResponseBody examine_earning_rules(loyalties_examine_earning_rules_examine_request_body=loyalties_examine_earning_rules_examine_request_body)

Examine earning rules

Estimates earning opportunities for a customer without triggering any actual earning for loyalty v2 earning rules. The trigger selects whether all trigger events or one specific event is examined. When a specific event is selected, exactly one matching context object is required: customer_order_paid for customer.order.paid, customer_segment_entered for customer.segment.entered, and customer_custom_event for customer.custom_event. The other context objects must not be present. This endpoint can examine earning rules for all loyalty programs the customer belongs to by using customer_identification with customer_id or customer_source_id. To examine earning rules only for one program, use member_id in customer_identification, as member_id is loyalty program-specific. A customer who exists but has no active membership returns 200 with an empty memberships array.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_examine_earning_rules_examine_request_body import LoyaltiesExamineEarningRulesExamineRequestBody
from voucherify.models.loyalties_examine_earning_rules_examine_response_body import LoyaltiesExamineEarningRulesExamineResponseBody
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
    api_instance = voucherify.LV2ExamineApi(api_client)
    loyalties_examine_earning_rules_examine_request_body = {"trigger":{"type":"ALL"},"customer_identification":{"type":"member_id","member_id":"lmbr_128f962dbc8c4ba5dc"},"customer_order_paid":{"customer":{"metadata":{"tier":"gold"}},"member":{"metadata":{"channel":"mobile"}},"order":{"amount":10000,"metadata":{"source":"pos"}}},"customer_segment_entered":{"customer":{"metadata":{"is_premium":"true","loyalty_score":10}}},"customer_custom_event":{"type":"ALL","all":{"customer":{"metadata":{"plan":"pro"}},"custom_event":{"metadata":{"source":"mobile","score":40}}}}} # LoyaltiesExamineEarningRulesExamineRequestBody |  (optional)

    try:
        # Examine earning rules
        api_response = api_instance.examine_earning_rules(loyalties_examine_earning_rules_examine_request_body=loyalties_examine_earning_rules_examine_request_body)
        print("The response of LV2ExamineApi->examine_earning_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ExamineApi->examine_earning_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loyalties_examine_earning_rules_examine_request_body** | [**LoyaltiesExamineEarningRulesExamineRequestBody**](LoyaltiesExamineEarningRulesExamineRequestBody.md)|  | [optional] 

### Return type

[**LoyaltiesExamineEarningRulesExamineResponseBody**](LoyaltiesExamineEarningRulesExamineResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Earning rules examination result. An empty &#x60;memberships&#x60; array means no active membership has earning rules for the examined trigger. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **examine_rewards**
> LoyaltiesExamineRewardsExamineResponseBody examine_rewards(loyalties_examine_rewards_examine_request_body=loyalties_examine_rewards_examine_request_body)

Examine rewards

Evaluates rewards assigned to a customers active Loyalty v2 program memberships. Applies temporary customer and member metadata overrides without updating stored data. Returns reward availability by card, including points costs and applicable unavailability reasons. Omits a reward when it is inactive, out of stock, has no matching cost, or the member has no card for that cost. This endpoint can examine rewards for all loyalty programs the customer belongs to by using customer_identification with customer_id or customer_source_id. To examine rewards only for one program, use member_id in customer_identification, as member_id is loyalty program-specific. A customer who exists but has no active membership returns 200 with an empty memberships array.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_examine_rewards_examine_request_body import LoyaltiesExamineRewardsExamineRequestBody
from voucherify.models.loyalties_examine_rewards_examine_response_body import LoyaltiesExamineRewardsExamineResponseBody
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
    api_instance = voucherify.LV2ExamineApi(api_client)
    loyalties_examine_rewards_examine_request_body = voucherify.LoyaltiesExamineRewardsExamineRequestBody() # LoyaltiesExamineRewardsExamineRequestBody |  (optional)

    try:
        # Examine rewards
        api_response = api_instance.examine_rewards(loyalties_examine_rewards_examine_request_body=loyalties_examine_rewards_examine_request_body)
        print("The response of LV2ExamineApi->examine_rewards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ExamineApi->examine_rewards: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loyalties_examine_rewards_examine_request_body** | [**LoyaltiesExamineRewardsExamineRequestBody**](LoyaltiesExamineRewardsExamineRequestBody.md)|  | [optional] 

### Return type

[**LoyaltiesExamineRewardsExamineResponseBody**](LoyaltiesExamineRewardsExamineResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Rewards examination result. An empty &#x60;memberships&#x60; array means the customer has no active membership. An empty &#x60;cards&#x60; array means no assigned reward resolved onto a card. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

