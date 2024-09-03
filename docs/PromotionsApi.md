# voucherify.PromotionsApi

All URIs are relative to *https://api.voucherify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_promotion_tier_to_campaign**](PromotionsApi.md#add_promotion_tier_to_campaign) | **POST** /v1/promotions/{campaignId}/tiers | Add Promotion Tier to Campaign
[**create_promotion_stack**](PromotionsApi.md#create_promotion_stack) | **POST** /v1/promotions/{campaignId}/stacks | Create Promotion Stack
[**delete_promotion_stack**](PromotionsApi.md#delete_promotion_stack) | **DELETE** /v1/promotions/{campaignId}/stacks/{stackId} | Delete Promotion Stack
[**delete_promotion_tier**](PromotionsApi.md#delete_promotion_tier) | **DELETE** /v1/promotions/tiers/{promotionTierId} | Delete Promotion Tier
[**disable_promotion_tier**](PromotionsApi.md#disable_promotion_tier) | **POST** /v1/promotions/tiers/{promotionTierId}/disable | Disable Promotion Tier
[**enable_promotion_tier**](PromotionsApi.md#enable_promotion_tier) | **POST** /v1/promotions/tiers/{promotionTierId}/enable | Enable Promotion Tier
[**get_promotion_stack**](PromotionsApi.md#get_promotion_stack) | **GET** /v1/promotions/{campaignId}/stacks/{stackId} | Get Promotion Stack
[**get_promotion_tier**](PromotionsApi.md#get_promotion_tier) | **GET** /v1/promotions/tiers/{promotionTierId} | Get Promotion Tier
[**list_all_promotion_stacks**](PromotionsApi.md#list_all_promotion_stacks) | **GET** /v1/promotions/stacks | List Promotion Stacks
[**list_promotion_stacks_in_campaign**](PromotionsApi.md#list_promotion_stacks_in_campaign) | **GET** /v1/promotions/{campaignId}/stacks | List Promotion Stacks in Campaign
[**list_promotion_tiers**](PromotionsApi.md#list_promotion_tiers) | **GET** /v1/promotions/tiers | List Promotion Tiers
[**list_promotion_tiers_from_campaign**](PromotionsApi.md#list_promotion_tiers_from_campaign) | **GET** /v1/promotions/{campaignId}/tiers | List Promotion Tiers from Campaign
[**update_promotion_stack**](PromotionsApi.md#update_promotion_stack) | **PUT** /v1/promotions/{campaignId}/stacks/{stackId} | Update Promotion Stack
[**update_promotion_tier**](PromotionsApi.md#update_promotion_tier) | **PUT** /v1/promotions/tiers/{promotionTierId} | Update Promotion Tier


# **add_promotion_tier_to_campaign**
> PromotionsTiersCreateResponseBody add_promotion_tier_to_campaign(campaign_id, promotions_tiers_create_request_body=promotions_tiers_create_request_body)

Add Promotion Tier to Campaign

This method allows you to add a new promotion tier to an existing campaign. The tier hierarchy will be set as the next consequtive integer following the lowest ranking tier.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.promotions_tiers_create_request_body import PromotionsTiersCreateRequestBody
from voucherify.models.promotions_tiers_create_response_body import PromotionsTiersCreateResponseBody
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
    api_instance = voucherify.PromotionsApi(api_client)
    campaign_id = 'campaign_id_example' # str | Unique campaign ID assigned by Voucherify.
    promotions_tiers_create_request_body = {"name":"Order more than $100","banner":"Order more than $100","action":{"discount":{"type":"AMOUNT","amount_off":3000,"effect":"APPLY_TO_ORDER"}},"metadata":{},"active":true,"start_date":"2022-09-21T00:00:00.000Z","expiration_date":"2022-09-30T00:00:00.000Z","validity_timeframe":{"interval":"P2D","duration":"P1D"},"validity_day_of_week":[1,2,3,4],"validation_rules":["val_q8qUBMOh5qIQ"]} # PromotionsTiersCreateRequestBody | Specify the promotion tier parameters. (optional)

    try:
        # Add Promotion Tier to Campaign
        api_response = api_instance.add_promotion_tier_to_campaign(campaign_id, promotions_tiers_create_request_body=promotions_tiers_create_request_body)
        print("The response of PromotionsApi->add_promotion_tier_to_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionsApi->add_promotion_tier_to_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Unique campaign ID assigned by Voucherify. | 
 **promotions_tiers_create_request_body** | [**PromotionsTiersCreateRequestBody**](PromotionsTiersCreateRequestBody.md)| Specify the promotion tier parameters. | [optional] 

### Return type

[**PromotionsTiersCreateResponseBody**](PromotionsTiersCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a promotion tier object if the promotion tier was successfully added to the campaign. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_promotion_stack**
> PromotionsStacksCreateResponseBody create_promotion_stack(campaign_id, promotions_stacks_create_request_body=promotions_stacks_create_request_body)

Create Promotion Stack

This method creates one promotion stack. The sequence of promotion tier IDs will determine the promotion stacking order.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.promotions_stacks_create_request_body import PromotionsStacksCreateRequestBody
from voucherify.models.promotions_stacks_create_response_body import PromotionsStacksCreateResponseBody
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
    api_instance = voucherify.PromotionsApi(api_client)
    campaign_id = 'campaign_id_example' # str | Unique campaign ID.
    promotions_stacks_create_request_body = {"name":"Fifth Stack","tiers":{"ids":["promo_aaAF8mVAzA0PF1igia2OC63d","promo_t9zdL6XMFk7B8fQ23zxELtdE","promo_dJNhAEeV5sR5oPQq1UrUdnMC"],"hierarchy_mode":"MANUAL"}} # PromotionsStacksCreateRequestBody | Specify the order of promotion tiers for the promotion stack. (optional)

    try:
        # Create Promotion Stack
        api_response = api_instance.create_promotion_stack(campaign_id, promotions_stacks_create_request_body=promotions_stacks_create_request_body)
        print("The response of PromotionsApi->create_promotion_stack:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionsApi->create_promotion_stack: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Unique campaign ID. | 
 **promotions_stacks_create_request_body** | [**PromotionsStacksCreateRequestBody**](PromotionsStacksCreateRequestBody.md)| Specify the order of promotion tiers for the promotion stack. | [optional] 

### Return type

[**PromotionsStacksCreateResponseBody**](PromotionsStacksCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a new stack object if a valid promotion campaign identifier was provided in the path and available promotion IDs in the payload. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_promotion_stack**
> delete_promotion_stack(campaign_id, stack_id)

Delete Promotion Stack

This method deletes a promotion stack.

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
    api_instance = voucherify.PromotionsApi(api_client)
    campaign_id = 'campaign_id_example' # str | ID of the promotion campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty Campaign. 
    stack_id = 'stack_id_example' # str | Promotion stack ID.

    try:
        # Delete Promotion Stack
        api_instance.delete_promotion_stack(campaign_id, stack_id)
    except Exception as e:
        print("Exception when calling PromotionsApi->delete_promotion_stack: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| ID of the promotion campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty Campaign.  | 
 **stack_id** | **str**| Promotion stack ID. | 

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

# **delete_promotion_tier**
> delete_promotion_tier(promotion_tier_id)

Delete Promotion Tier

This method deletes a promotion tier.

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
    api_instance = voucherify.PromotionsApi(api_client)
    promotion_tier_id = 'promotion_tier_id_example' # str | Unique promotion tier ID.

    try:
        # Delete Promotion Tier
        api_instance.delete_promotion_tier(promotion_tier_id)
    except Exception as e:
        print("Exception when calling PromotionsApi->delete_promotion_tier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **promotion_tier_id** | **str**| Unique promotion tier ID. | 

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

# **disable_promotion_tier**
> PromotionsTiersDisableResponseBody disable_promotion_tier(promotion_tier_id)

Disable Promotion Tier

This method disables a promotion tier, i.e. makes the active parameter   false.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.promotions_tiers_disable_response_body import PromotionsTiersDisableResponseBody
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
    api_instance = voucherify.PromotionsApi(api_client)
    promotion_tier_id = 'promotion_tier_id_example' # str | Unique promotion tier ID.

    try:
        # Disable Promotion Tier
        api_response = api_instance.disable_promotion_tier(promotion_tier_id)
        print("The response of PromotionsApi->disable_promotion_tier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionsApi->disable_promotion_tier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **promotion_tier_id** | **str**| Unique promotion tier ID. | 

### Return type

[**PromotionsTiersDisableResponseBody**](PromotionsTiersDisableResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the promotion tier object with an updated &#x60;active&#x60; parameter. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_promotion_tier**
> PromotionsTiersEnableResponseBody enable_promotion_tier(promotion_tier_id)

Enable Promotion Tier

This method enables a promotion tier, i.e. makes the active parameter   true.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.promotions_tiers_enable_response_body import PromotionsTiersEnableResponseBody
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
    api_instance = voucherify.PromotionsApi(api_client)
    promotion_tier_id = 'promotion_tier_id_example' # str | Unique promotion tier ID.

    try:
        # Enable Promotion Tier
        api_response = api_instance.enable_promotion_tier(promotion_tier_id)
        print("The response of PromotionsApi->enable_promotion_tier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionsApi->enable_promotion_tier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **promotion_tier_id** | **str**| Unique promotion tier ID. | 

### Return type

[**PromotionsTiersEnableResponseBody**](PromotionsTiersEnableResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the promotion tier object with an updated &#x60;active&#x60; parameter. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_promotion_stack**
> PromotionsStacksGetResponseBody get_promotion_stack(campaign_id, stack_id)

Get Promotion Stack

This method returns the details of a promotion stack, including the promotion tiers grouped within the stack.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.promotions_stacks_get_response_body import PromotionsStacksGetResponseBody
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
    api_instance = voucherify.PromotionsApi(api_client)
    campaign_id = 'campaign_id_example' # str | ID of the promotion campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty Campaign. 
    stack_id = 'stack_id_example' # str | Promotion stack ID.

    try:
        # Get Promotion Stack
        api_response = api_instance.get_promotion_stack(campaign_id, stack_id)
        print("The response of PromotionsApi->get_promotion_stack:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionsApi->get_promotion_stack: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| ID of the promotion campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty Campaign.  | 
 **stack_id** | **str**| Promotion stack ID. | 

### Return type

[**PromotionsStacksGetResponseBody**](PromotionsStacksGetResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a stack object if valid identifiers were provided in the path. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_promotion_tier**
> PromotionsTiersGetResponseBody get_promotion_tier(promotion_tier_id)

Get Promotion Tier

This method enables you to retrieve a specific promotion tier.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.promotions_tiers_get_response_body import PromotionsTiersGetResponseBody
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
    api_instance = voucherify.PromotionsApi(api_client)
    promotion_tier_id = 'promotion_tier_id_example' # str | Unique promotion tier ID.

    try:
        # Get Promotion Tier
        api_response = api_instance.get_promotion_tier(promotion_tier_id)
        print("The response of PromotionsApi->get_promotion_tier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionsApi->get_promotion_tier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **promotion_tier_id** | **str**| Unique promotion tier ID. | 

### Return type

[**PromotionsTiersGetResponseBody**](PromotionsTiersGetResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a promotion tier object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_promotion_stacks**
> PromotionsStacksListResponseBody list_all_promotion_stacks(limit=limit, page=page, order=order, created_at=created_at, updated_at=updated_at)

List Promotion Stacks

This method enables you to list promotion stacks irrespective of the campaign they are associated with.  You can use filters in the query parameters to specify the stacks to be returned in the response. # Advanced filters for fetching promotion stacks  

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.parameter_created_before_after import ParameterCreatedBeforeAfter
from voucherify.models.parameter_order_list_all_promotion_stacks import ParameterOrderListAllPromotionStacks
from voucherify.models.parameter_updated_before_after import ParameterUpdatedBeforeAfter
from voucherify.models.promotions_stacks_list_response_body import PromotionsStacksListResponseBody
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
    api_instance = voucherify.PromotionsApi(api_client)
    limit = 56 # int | Limits the number of objects to be returned. The limit can range between 1 and 100 items. (optional)
    page = 56 # int | Which page of results to return. The lowest value is 1. (optional)
    order = voucherify.ParameterOrderListAllPromotionStacks() # ParameterOrderListAllPromotionStacks | Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. (optional)
    created_at = voucherify.ParameterCreatedBeforeAfter() # ParameterCreatedBeforeAfter | A filter on the list based on the object created_at field. The value is a dictionary with the following options: before, after. A date value must be presented in ISO 8601 format (2016-11-16T14:14:31Z or 2016-11-16). An example: [created_at][before] 2017-09-08T13:52:18.227Z (optional)
    updated_at = voucherify.ParameterUpdatedBeforeAfter() # ParameterUpdatedBeforeAfter | A filter on the list based on the object updated_at field. The value is a dictionary with the following options: before, after. A date value must be presented in ISO 8601 format (2016-11-16T14:14:31Z or 2016-11-16). An example: [updated_at][before] 2017-09-08T13:52:18.227Z (optional)

    try:
        # List Promotion Stacks
        api_response = api_instance.list_all_promotion_stacks(limit=limit, page=page, order=order, created_at=created_at, updated_at=updated_at)
        print("The response of PromotionsApi->list_all_promotion_stacks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionsApi->list_all_promotion_stacks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limits the number of objects to be returned. The limit can range between 1 and 100 items. | [optional] 
 **page** | **int**| Which page of results to return. The lowest value is 1. | [optional] 
 **order** | [**ParameterOrderListAllPromotionStacks**](.md)| Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. | [optional] 
 **created_at** | [**ParameterCreatedBeforeAfter**](.md)| A filter on the list based on the object created_at field. The value is a dictionary with the following options: before, after. A date value must be presented in ISO 8601 format (2016-11-16T14:14:31Z or 2016-11-16). An example: [created_at][before] 2017-09-08T13:52:18.227Z | [optional] 
 **updated_at** | [**ParameterUpdatedBeforeAfter**](.md)| A filter on the list based on the object updated_at field. The value is a dictionary with the following options: before, after. A date value must be presented in ISO 8601 format (2016-11-16T14:14:31Z or 2016-11-16). An example: [updated_at][before] 2017-09-08T13:52:18.227Z | [optional] 

### Return type

[**PromotionsStacksListResponseBody**](PromotionsStacksListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a dictionary with a &#x60;data&#x60; property that contains an array of promotion stacks across all your campaigns. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_promotion_stacks_in_campaign**
> PromotionsStacksListResponseBody list_promotion_stacks_in_campaign(campaign_id)

List Promotion Stacks in Campaign

This method enables you to list promotion stacks from a specified campaign.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.promotions_stacks_list_response_body import PromotionsStacksListResponseBody
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
    api_instance = voucherify.PromotionsApi(api_client)
    campaign_id = 'campaign_id_example' # str | Unique campaign ID.

    try:
        # List Promotion Stacks in Campaign
        api_response = api_instance.list_promotion_stacks_in_campaign(campaign_id)
        print("The response of PromotionsApi->list_promotion_stacks_in_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionsApi->list_promotion_stacks_in_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Unique campaign ID. | 

### Return type

[**PromotionsStacksListResponseBody**](PromotionsStacksListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a list of promotion stack objects. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_promotion_tiers**
> PromotionsTiersListResponseBody list_promotion_tiers(is_available=is_available, limit=limit, page=page, order=order)

List Promotion Tiers

This method enables you to list promotion tiers.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.parameter_order_list_promotion_tiers import ParameterOrderListPromotionTiers
from voucherify.models.promotions_tiers_list_response_body import PromotionsTiersListResponseBody
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
    api_instance = voucherify.PromotionsApi(api_client)
    is_available = True # bool | This parameter allows filtering promotions that are only available at the moment. When set to true, it selects only non-expired and active promotions. (optional)
    limit = 56 # int | Limits the number of objects to be returned. The limit can range between 1 and 100 items. (optional)
    page = 56 # int | Which page of results to return. The lowest value is 1. (optional)
    order = voucherify.ParameterOrderListPromotionTiers() # ParameterOrderListPromotionTiers | Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. (optional)

    try:
        # List Promotion Tiers
        api_response = api_instance.list_promotion_tiers(is_available=is_available, limit=limit, page=page, order=order)
        print("The response of PromotionsApi->list_promotion_tiers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionsApi->list_promotion_tiers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_available** | **bool**| This parameter allows filtering promotions that are only available at the moment. When set to true, it selects only non-expired and active promotions. | [optional] 
 **limit** | **int**| Limits the number of objects to be returned. The limit can range between 1 and 100 items. | [optional] 
 **page** | **int**| Which page of results to return. The lowest value is 1. | [optional] 
 **order** | [**ParameterOrderListPromotionTiers**](.md)| Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. | [optional] 

### Return type

[**PromotionsTiersListResponseBody**](PromotionsTiersListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a dictionary with a &#x60;tiers&#x60; property that contains an array of promotion tiers. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_promotion_tiers_from_campaign**
> PromotionsTiersListResponseBody list_promotion_tiers_from_campaign(campaign_id)

List Promotion Tiers from Campaign

This method enables you to list promotion tiers from a specified campaign.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.promotions_tiers_list_response_body import PromotionsTiersListResponseBody
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
    api_instance = voucherify.PromotionsApi(api_client)
    campaign_id = 'campaign_id_example' # str | Unique campaign ID assigned by Voucherify.

    try:
        # List Promotion Tiers from Campaign
        api_response = api_instance.list_promotion_tiers_from_campaign(campaign_id)
        print("The response of PromotionsApi->list_promotion_tiers_from_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionsApi->list_promotion_tiers_from_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Unique campaign ID assigned by Voucherify. | 

### Return type

[**PromotionsTiersListResponseBody**](PromotionsTiersListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a dictionary with a &#x60;tiers&#x60; property that contains an array of promotion tiers. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_promotion_stack**
> PromotionsStacksUpdateResponseBody update_promotion_stack(campaign_id, stack_id, promotions_stacks_update_request_body=promotions_stacks_update_request_body)

Update Promotion Stack

This methods allows for editing an existing stack.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.promotions_stacks_update_request_body import PromotionsStacksUpdateRequestBody
from voucherify.models.promotions_stacks_update_response_body import PromotionsStacksUpdateResponseBody
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
    api_instance = voucherify.PromotionsApi(api_client)
    campaign_id = 'campaign_id_example' # str | ID of the promotion campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty Campaign. 
    stack_id = 'stack_id_example' # str | Promotion stack ID.
    promotions_stacks_update_request_body = {"name":"Fifth Stack Modified","tiers":{"ids":["promo_aaAF8mVAzA0PF1igia2OC63d","promo_t9zdL6XMFk7B8fQ23zxELtdE"],"hierarchy_mode":"MANUAL"}} # PromotionsStacksUpdateRequestBody | Specify the promotion stack parameters that you would like to update. (optional)

    try:
        # Update Promotion Stack
        api_response = api_instance.update_promotion_stack(campaign_id, stack_id, promotions_stacks_update_request_body=promotions_stacks_update_request_body)
        print("The response of PromotionsApi->update_promotion_stack:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionsApi->update_promotion_stack: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| ID of the promotion campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty Campaign.  | 
 **stack_id** | **str**| Promotion stack ID. | 
 **promotions_stacks_update_request_body** | [**PromotionsStacksUpdateRequestBody**](PromotionsStacksUpdateRequestBody.md)| Specify the promotion stack parameters that you would like to update. | [optional] 

### Return type

[**PromotionsStacksUpdateResponseBody**](PromotionsStacksUpdateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a promotion stack with updated parameters if the update was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_promotion_tier**
> PromotionsTiersUpdateResponseBody update_promotion_tier(promotion_tier_id, promotions_tiers_update_request_body=promotions_tiers_update_request_body)

Update Promotion Tier

This method updates a promotion tier.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.promotions_tiers_update_request_body import PromotionsTiersUpdateRequestBody
from voucherify.models.promotions_tiers_update_response_body import PromotionsTiersUpdateResponseBody
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
    api_instance = voucherify.PromotionsApi(api_client)
    promotion_tier_id = 'promotion_tier_id_example' # str | Unique promotion tier ID.
    promotions_tiers_update_request_body = {"name":"Order more than $100 USD","banner":"Order more than $100 USD","action":{"discount":{"type":"PERCENT","percent_off":25,"effect":"APPLY_TO_ORDER"}},"metadata":{"level":"A-21"},"hierarchy":1,"start_date":"2022-09-22T00:00:00.000Z","expiration_date":"2022-09-29T00:00:00.000Z","validity_timeframe":{"interval":"P3D","duration":"P2D"},"validity_day_of_week":[1,2,3]} # PromotionsTiersUpdateRequestBody | Specify the promotion tier parameters that you would like to update. (optional)

    try:
        # Update Promotion Tier
        api_response = api_instance.update_promotion_tier(promotion_tier_id, promotions_tiers_update_request_body=promotions_tiers_update_request_body)
        print("The response of PromotionsApi->update_promotion_tier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionsApi->update_promotion_tier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **promotion_tier_id** | **str**| Unique promotion tier ID. | 
 **promotions_tiers_update_request_body** | [**PromotionsTiersUpdateRequestBody**](PromotionsTiersUpdateRequestBody.md)| Specify the promotion tier parameters that you would like to update. | [optional] 

### Return type

[**PromotionsTiersUpdateResponseBody**](PromotionsTiersUpdateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a promotion tier object if the update was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

