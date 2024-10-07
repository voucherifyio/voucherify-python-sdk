# voucherify.ClientSideApi

All URIs are relative to *https://api.voucherify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_eligibility_client_side**](ClientSideApi.md#check_eligibility_client_side) | **POST** /client/v1/qualifications | Check Eligibility (client-side)
[**list_promotion_tiers_client_side**](ClientSideApi.md#list_promotion_tiers_client_side) | **GET** /client/v1/promotions/tiers | List Promotion Tiers (client-side)
[**redeem_stacked_discounts_client_side**](ClientSideApi.md#redeem_stacked_discounts_client_side) | **POST** /client/v1/redemptions | Redeem Stackable Discounts (client-side)
[**track_custom_event_client_side**](ClientSideApi.md#track_custom_event_client_side) | **POST** /client/v1/events | Track Custom Event (client-side)
[**validate_stacked_discounts_client_side**](ClientSideApi.md#validate_stacked_discounts_client_side) | **POST** /client/v1/validations | Validate Stackable Discounts (client-side)


# **check_eligibility_client_side**
> ClientQualificationsCheckEligibilityResponseBody check_eligibility_client_side(client_qualifications_check_eligibility_request_body=client_qualifications_check_eligibility_request_body)

Check Eligibility (client-side)

Generate a list of redeemables that are applicable in the context of the customer and order. The new qualifications method is an improved version of Campaign Qualifications, Voucher Qualifications, and Promotions Validation API requests. The new qualification method introduces the following improvements: - Qualification results are returned faster - No limit on the number of returned redeemables - Introduces new qualification scenarios, not available in the previous version  👍 Scenario Guide  Read our dedicated guide to learn about some use cases this endpoint can cover here. # Paging  The Voucherify Qualifications API request will return to you all of the redeemables available for the customer in batches of up to 50 redeemables. To get the next batch of redeemables, you need to use the starting_after cursor. To process of paging the redeemables works in the following manner: - You send the first API request for Qualifications without the starting_after parameter. - The response will contain a parameter named has_more. If the parameters value is set to true, then more redeemables are available. - Get the value of the created_at parameter of the last returned redeemable. The value of this parameter will be used as a cursor to retrieve the next page of redeemables. - Send another API request for Qualification with the starting_after parameter set to the value taken from the created_at parameter from the last returned redeemable. - Voucherify will return the next page of redeemables. - If the has_more parameter is set to true, apply steps 3-5 to get the next page of redeemables.

### Example

* Api Key Authentication (X-Client-Application-Id):
* Api Key Authentication (X-Client-Token):

```python
import voucherify
from voucherify.models.client_qualifications_check_eligibility_request_body import ClientQualificationsCheckEligibilityRequestBody
from voucherify.models.client_qualifications_check_eligibility_response_body import ClientQualificationsCheckEligibilityResponseBody
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

# Configure API key authorization: X-Client-Application-Id
configuration.api_key['X-Client-Application-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Client-Application-Id'] = 'Bearer'

# Configure API key authorization: X-Client-Token
configuration.api_key['X-Client-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Client-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ClientSideApi(api_client)
    client_qualifications_check_eligibility_request_body = voucherify.ClientQualificationsCheckEligibilityRequestBody() # ClientQualificationsCheckEligibilityRequestBody | Define order and customer context. (optional)

    try:
        # Check Eligibility (client-side)
        api_response = api_instance.check_eligibility_client_side(client_qualifications_check_eligibility_request_body=client_qualifications_check_eligibility_request_body)
        print("The response of ClientSideApi->check_eligibility_client_side:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientSideApi->check_eligibility_client_side: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_qualifications_check_eligibility_request_body** | [**ClientQualificationsCheckEligibilityRequestBody**](ClientQualificationsCheckEligibilityRequestBody.md)| Define order and customer context. | [optional] 

### Return type

[**ClientQualificationsCheckEligibilityResponseBody**](ClientQualificationsCheckEligibilityResponseBody.md)

### Authorization

[X-Client-Application-Id](../README.md#X-Client-Application-Id), [X-Client-Token](../README.md#X-Client-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a qualifications object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_promotion_tiers_client_side**
> ClientPromotionsTiersListResponseBody list_promotion_tiers_client_side(origin, is_available=is_available, limit=limit, page=page, order=order)

List Promotion Tiers (client-side)

This method enables you to list promotion tiers.

### Example

* Api Key Authentication (X-Client-Application-Id):
* Api Key Authentication (X-Client-Token):

```python
import voucherify
from voucherify.models.client_promotions_tiers_list_response_body import ClientPromotionsTiersListResponseBody
from voucherify.models.parameter_order_list_promotion_tiers_client_side import ParameterOrderListPromotionTiersClientSide
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

# Configure API key authorization: X-Client-Application-Id
configuration.api_key['X-Client-Application-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Client-Application-Id'] = 'Bearer'

# Configure API key authorization: X-Client-Token
configuration.api_key['X-Client-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Client-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ClientSideApi(api_client)
    origin = 'origin_example' # str | Indicates the origin (scheme, hostname, and port).
    is_available = True # bool | This parameter allows filtering promotions that are only available at the moment. When set to true, it selects only non-expired and active promotions. (optional)
    limit = 56 # int | Limits the number of objects to be returned. The limit can range between 1 and 100 items. (optional)
    page = 56 # int | Which page of results to return. The lowest value is 1. (optional)
    order = voucherify.ParameterOrderListPromotionTiersClientSide() # ParameterOrderListPromotionTiersClientSide | Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. (optional)

    try:
        # List Promotion Tiers (client-side)
        api_response = api_instance.list_promotion_tiers_client_side(origin, is_available=is_available, limit=limit, page=page, order=order)
        print("The response of ClientSideApi->list_promotion_tiers_client_side:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientSideApi->list_promotion_tiers_client_side: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin** | **str**| Indicates the origin (scheme, hostname, and port). | 
 **is_available** | **bool**| This parameter allows filtering promotions that are only available at the moment. When set to true, it selects only non-expired and active promotions. | [optional] 
 **limit** | **int**| Limits the number of objects to be returned. The limit can range between 1 and 100 items. | [optional] 
 **page** | **int**| Which page of results to return. The lowest value is 1. | [optional] 
 **order** | [**ParameterOrderListPromotionTiersClientSide**](.md)| Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. | [optional] 

### Return type

[**ClientPromotionsTiersListResponseBody**](ClientPromotionsTiersListResponseBody.md)

### Authorization

[X-Client-Application-Id](../README.md#X-Client-Application-Id), [X-Client-Token](../README.md#X-Client-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a dictionary with a &#x60;tiers&#x60; property that contains an array of promotion tiers. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redeem_stacked_discounts_client_side**
> ClientRedemptionsRedeemResponseBody redeem_stacked_discounts_client_side(origin, client_redemptions_redeem_request_body=client_redemptions_redeem_request_body)

Redeem Stackable Discounts (client-side)

This method is accessible through public keys which you can use in client side requests coming from mobile and web browser applications. # How API returns calculated discounts and order amounts in the response In the table below, you can see the logic the API follows to calculate discounts and amounts:    📘 Rollbacks  You cant roll back a child redemption. When you call rollback on a stacked redemption, all child redemptions will be rolled back. You need to refer to a parent redemption ID in your rollback request.

### Example

* Api Key Authentication (X-Client-Application-Id):
* Api Key Authentication (X-Client-Token):

```python
import voucherify
from voucherify.models.client_redemptions_redeem_request_body import ClientRedemptionsRedeemRequestBody
from voucherify.models.client_redemptions_redeem_response_body import ClientRedemptionsRedeemResponseBody
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

# Configure API key authorization: X-Client-Application-Id
configuration.api_key['X-Client-Application-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Client-Application-Id'] = 'Bearer'

# Configure API key authorization: X-Client-Token
configuration.api_key['X-Client-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Client-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ClientSideApi(api_client)
    origin = 'origin_example' # str | Indicates the origin (scheme, hostname, and port).
    client_redemptions_redeem_request_body = {"customer":{"source_id":"sample_customer","metadata":{"key":"value"}},"options":{"expand":["order","redeemable","category"]},"redeemables":[{"object":"voucher","id":"voucher-code"}],"session":{"type":"LOCK","key":"session_key"},"order":{"amount":55000,"status":"PAID","items":[{"quantity":2,"price":20000,"source_id":"sample product1","related_object":"product","product":{"metadata":{"key":"value"}}},{"quantity":1,"price":15000,"source_id":"sample product2","related_object":"product","product":{"metadata":{"key":"value"}}}],"metadata":{"key":"value"}}} # ClientRedemptionsRedeemRequestBody |  (optional)

    try:
        # Redeem Stackable Discounts (client-side)
        api_response = api_instance.redeem_stacked_discounts_client_side(origin, client_redemptions_redeem_request_body=client_redemptions_redeem_request_body)
        print("The response of ClientSideApi->redeem_stacked_discounts_client_side:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientSideApi->redeem_stacked_discounts_client_side: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin** | **str**| Indicates the origin (scheme, hostname, and port). | 
 **client_redemptions_redeem_request_body** | [**ClientRedemptionsRedeemRequestBody**](ClientRedemptionsRedeemRequestBody.md)|  | [optional] 

### Return type

[**ClientRedemptionsRedeemResponseBody**](ClientRedemptionsRedeemResponseBody.md)

### Authorization

[X-Client-Application-Id](../README.md#X-Client-Application-Id), [X-Client-Token](../README.md#X-Client-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Depending on your project settings: all redeemables must be valid or just one must be valid to result as valid redemption. Read more in the [Stacking Rule Documentation](https://support.voucherify.io/article/604-stacking-rules). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **track_custom_event_client_side**
> ClientEventsCreateResponseBody track_custom_event_client_side(origin, client_events_create_request_body=client_events_create_request_body)

Track Custom Event (client-side)

To track a custom event, you create an event object.   The event object must be linked to the customer who performs the action. If a customer doesnt exist in Voucherify, the customer will be created.

### Example

* Api Key Authentication (X-Client-Application-Id):
* Api Key Authentication (X-Client-Token):

```python
import voucherify
from voucherify.models.client_events_create_request_body import ClientEventsCreateRequestBody
from voucherify.models.client_events_create_response_body import ClientEventsCreateResponseBody
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

# Configure API key authorization: X-Client-Application-Id
configuration.api_key['X-Client-Application-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Client-Application-Id'] = 'Bearer'

# Configure API key authorization: X-Client-Token
configuration.api_key['X-Client-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Client-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ClientSideApi(api_client)
    origin = 'origin_example' # str | Indicates the origin (scheme, hostname, and port).
    client_events_create_request_body = {"event":"user_subscribed","customer":{"source_id":"source_customer_event"},"referral":{"code":"46jL0kYI","referrer_id":"cust_Vzck5i8U3OhcEUFY6MKhN9Rv"},"metadata":{"login":"bob","pricing_plan":"PP1","volume_number":4}} # ClientEventsCreateRequestBody | Specify the details of the custom event. (optional)

    try:
        # Track Custom Event (client-side)
        api_response = api_instance.track_custom_event_client_side(origin, client_events_create_request_body=client_events_create_request_body)
        print("The response of ClientSideApi->track_custom_event_client_side:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientSideApi->track_custom_event_client_side: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin** | **str**| Indicates the origin (scheme, hostname, and port). | 
 **client_events_create_request_body** | [**ClientEventsCreateRequestBody**](ClientEventsCreateRequestBody.md)| Specify the details of the custom event. | [optional] 

### Return type

[**ClientEventsCreateResponseBody**](ClientEventsCreateResponseBody.md)

### Authorization

[X-Client-Application-Id](../README.md#X-Client-Application-Id), [X-Client-Token](../README.md#X-Client-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the event type if the event was received by the application. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_stacked_discounts_client_side**
> ClientValidationsValidateResponseBody validate_stacked_discounts_client_side(origin, client_validations_validate_request_body=client_validations_validate_request_body)

Validate Stackable Discounts (client-side)

Verify redeemables provided in the request. This method is accessible through public keys which you can use in client side requests coming from mobile and web browser applications.

### Example

* Api Key Authentication (X-Client-Application-Id):
* Api Key Authentication (X-Client-Token):

```python
import voucherify
from voucherify.models.client_validations_validate_request_body import ClientValidationsValidateRequestBody
from voucherify.models.client_validations_validate_response_body import ClientValidationsValidateResponseBody
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

# Configure API key authorization: X-Client-Application-Id
configuration.api_key['X-Client-Application-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Client-Application-Id'] = 'Bearer'

# Configure API key authorization: X-Client-Token
configuration.api_key['X-Client-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Client-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ClientSideApi(api_client)
    origin = 'origin_example' # str | Indicates the origin (scheme, hostname, and port).
    client_validations_validate_request_body = {"customer":{"source_id":"sample_customer","metadata":{"key":"value"}},"options":{"expand":["order","redeemable","category"]},"redeemables":[{"object":"voucher","id":"voucher-code"}],"session":{"type":"LOCK"},"order":{"amount":55000,"status":"PAID","items":[{"quantity":2,"price":20000,"source_id":"sample product1","related_object":"product","product":{"metadata":{"key":"value"}}},{"quantity":1,"price":15000,"source_id":"sample product2","related_object":"product","product":{"metadata":{"key":"value"}}}],"metadata":{"key":"value"}}} # ClientValidationsValidateRequestBody |  (optional)

    try:
        # Validate Stackable Discounts (client-side)
        api_response = api_instance.validate_stacked_discounts_client_side(origin, client_validations_validate_request_body=client_validations_validate_request_body)
        print("The response of ClientSideApi->validate_stacked_discounts_client_side:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientSideApi->validate_stacked_discounts_client_side: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin** | **str**| Indicates the origin (scheme, hostname, and port). | 
 **client_validations_validate_request_body** | [**ClientValidationsValidateRequestBody**](ClientValidationsValidateRequestBody.md)|  | [optional] 

### Return type

[**ClientValidationsValidateResponseBody**](ClientValidationsValidateResponseBody.md)

### Authorization

[X-Client-Application-Id](../README.md#X-Client-Application-Id), [X-Client-Token](../README.md#X-Client-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Depending on your project settings: all redeemables must be valid or just one must be valid to result as valid validation. Read more in the [Stacking Rule Documentation](https://support.voucherify.io/article/604-stacking-rules). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

