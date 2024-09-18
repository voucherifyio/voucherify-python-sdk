# voucherify.RedemptionsApi

All URIs are relative to *https://api.voucherify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_redemption**](RedemptionsApi.md#get_redemption) | **GET** /v1/redemptions/{redemptionId} | Get Redemption
[**get_voucher_redemptions**](RedemptionsApi.md#get_voucher_redemptions) | **GET** /v1/vouchers/{code}/redemption | Get Voucher&#39;s Redemptions
[**list_redemptions**](RedemptionsApi.md#list_redemptions) | **GET** /v1/redemptions | List Redemptions
[**redeem_stacked_discounts**](RedemptionsApi.md#redeem_stacked_discounts) | **POST** /v1/redemptions | Redeem Stackable Discounts
[**rollback_redemption**](RedemptionsApi.md#rollback_redemption) | **POST** /v1/redemptions/{redemptionId}/rollback | Rollback Redemption
[**rollback_stacked_redemptions**](RedemptionsApi.md#rollback_stacked_redemptions) | **POST** /v1/redemptions/{parentRedemptionId}/rollbacks | Rollback Stackable Redemptions


# **get_redemption**
> RedemptionsGetResponseBody get_redemption(redemption_id)

Get Redemption

Return a redemption or redemption rollback object. This object can either be a successfull or failed redemption or redemption rollback.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.redemptions_get_response_body import RedemptionsGetResponseBody
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
    api_instance = voucherify.RedemptionsApi(api_client)
    redemption_id = 'redemption_id_example' # str | ID of previously created redemption.

    try:
        # Get Redemption
        api_response = api_instance.get_redemption(redemption_id)
        print("The response of RedemptionsApi->get_redemption:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RedemptionsApi->get_redemption: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redemption_id** | **str**| ID of previously created redemption. | 

### Return type

[**RedemptionsGetResponseBody**](RedemptionsGetResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a redemption object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_voucher_redemptions**
> VouchersRedemptionGetResponseBody get_voucher_redemptions(code)

Get Voucher's Redemptions

Retrieve the number of times a voucher was redeemed and each of the redemption details.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.vouchers_redemption_get_response_body import VouchersRedemptionGetResponseBody
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
    api_instance = voucherify.RedemptionsApi(api_client)
    code = 'code_example' # str | A **code** that identifies the voucher.

    try:
        # Get Voucher's Redemptions
        api_response = api_instance.get_voucher_redemptions(code)
        print("The response of RedemptionsApi->get_voucher_redemptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RedemptionsApi->get_voucher_redemptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| A **code** that identifies the voucher. | 

### Return type

[**VouchersRedemptionGetResponseBody**](VouchersRedemptionGetResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | A dictionary with a &#x60;redemption_entries&#x60; property that contains an array of voucher&#39;s redemptions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_redemptions**
> RedemptionsListResponseBody list_redemptions(limit=limit, page=page, result=result, campaign=campaign, customer=customer, order=order, created_at=created_at, filters=filters)

List Redemptions

Returns a list of redemptions previously created. The redemptions are returned in a sorted order, with the most recent redemptions appearing first. The response returns a list of redemptions of all vouchers.  # Filtering results The result can be narrowed according to specified (or default) filters, for example, you can sort redemptions by date: https://api.voucherify.io/v1/redemptions?limit 3&[created_at][before] 2017-09-08T13:52:18.227Z. A filter based on the object created_at field narrows down the results and lists redemptions done before or after a particular date time. You can use the following options: [created_at][after], [created_at][before]. A date value must be presented in ISO 8601 format (2016-11-16T14:14:31Z or 2016-11-16). An example: [created_at][before] 2017-09-08T13:52:18.227Z. # Failed Redemptions A redemption may fail for various reasons. You can figure out an exact reason from the failure_code: - resource_not_found - voucher with given code does not exist - voucher_not_active - voucher is not active yet (before start date) - voucher_expired - voucher has already expired (after expiration date) - voucher_disabled -  voucher has been disabled (active: false) - quantity_exceeded - vouchers redemptions limit has been exceeded - gift_amount_exceeded - gift amount has been exceeded - customer_rules_violated - customer did not match the segment - order_rules_violated - order did not match validation rules - invalid_order - order was specified incorrectly - invalid_amount - order amount was specified incorrectly - missing_amount - order amount was not specified - missing_order_items - order items were not specified - missing_customer - customer was not specified

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.parameter_created_before_after import ParameterCreatedBeforeAfter
from voucherify.models.parameter_filters_list_redemptions import ParameterFiltersListRedemptions
from voucherify.models.parameter_order_list_redemptions import ParameterOrderListRedemptions
from voucherify.models.redemptions_list_response_body import RedemptionsListResponseBody
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
    api_instance = voucherify.RedemptionsApi(api_client)
    limit = 56 # int | Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. (optional)
    page = 56 # int | Which page of results to return. The lowest value is 1. (optional)
    result = 'result_example' # str | A filter on the list based on the redemption result. Available options are: SUCCESS, FAILURE. You can provide multiple values by repeating the param. (optional)
    campaign = 'campaign_example' # str | A filter by the campaign **name** that the redemption resources originate from. (optional)
    customer = 'customer_example' # str | Return redemptions performed by the customer with given id or source_id. (optional)
    order = voucherify.ParameterOrderListRedemptions() # ParameterOrderListRedemptions | Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. (optional)
    created_at = voucherify.ParameterCreatedBeforeAfter() # ParameterCreatedBeforeAfter | A filter on the list based on the object created_at field. The value is a dictionary with the following options: before, after. A date value must be presented in ISO 8601 format (2016-11-16T14:14:31Z or 2016-11-16). An example: [created_at][before] 2017-09-08T13:52:18.227Z (optional)
    filters = voucherify.ParameterFiltersListRedemptions() # ParameterFiltersListRedemptions | Filters for listing responses. (optional)

    try:
        # List Redemptions
        api_response = api_instance.list_redemptions(limit=limit, page=page, result=result, campaign=campaign, customer=customer, order=order, created_at=created_at, filters=filters)
        print("The response of RedemptionsApi->list_redemptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RedemptionsApi->list_redemptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. | [optional] 
 **page** | **int**| Which page of results to return. The lowest value is 1. | [optional] 
 **result** | **str**| A filter on the list based on the redemption result. Available options are: SUCCESS, FAILURE. You can provide multiple values by repeating the param. | [optional] 
 **campaign** | **str**| A filter by the campaign **name** that the redemption resources originate from. | [optional] 
 **customer** | **str**| Return redemptions performed by the customer with given id or source_id. | [optional] 
 **order** | [**ParameterOrderListRedemptions**](.md)| Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. | [optional] 
 **created_at** | [**ParameterCreatedBeforeAfter**](.md)| A filter on the list based on the object created_at field. The value is a dictionary with the following options: before, after. A date value must be presented in ISO 8601 format (2016-11-16T14:14:31Z or 2016-11-16). An example: [created_at][before] 2017-09-08T13:52:18.227Z | [optional] 
 **filters** | [**ParameterFiltersListRedemptions**](.md)| Filters for listing responses. | [optional] 

### Return type

[**RedemptionsListResponseBody**](RedemptionsListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a list of redemption objects. Each entry in the array is a separate redemption object. If no more redemptions are available, the resulting array will be empty. If you provide a non-existent customer ID, this call returns an empty object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redeem_stacked_discounts**
> RedemptionsRedeemResponseBody redeem_stacked_discounts(redemptions_redeem_request_body=redemptions_redeem_request_body)

Redeem Stackable Discounts

# How API returns calculated discounts and order amounts in the response In the table below, you can see the logic the API follows to calculate discounts and amounts:    📘 Rollbacks  You cant roll back a child redemption. When you call rollback on a stacked redemption, all child redemptions will be rolled back. You need to refer to a parent redemption ID in your rollback request.      📘 Also available on client-side  This method is also accessible through public keys which you can use in client-side​ apps: mobile and web browser apps. Go to the dedicated endpoint to learn more.  - Use X-Client-Application-Id as the application ID header.  - Use X-Client-Token as the appliction secret key header.  - Use client-side base URL.  - Use an origin header for your custom domain.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.redemptions_redeem_request_body import RedemptionsRedeemRequestBody
from voucherify.models.redemptions_redeem_response_body import RedemptionsRedeemResponseBody
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
    api_instance = voucherify.RedemptionsApi(api_client)
    redemptions_redeem_request_body = {"customer":{"source_id":"sample_customer","metadata":{"key":"value"}},"options":{"expand":["order","redeemable","category"]},"redeemables":[{"object":"voucher","id":"voucher-code"}],"session":{"type":"LOCK","key":"session_key"},"order":{"amount":55000,"status":"PAID","items":[{"quantity":2,"price":20000,"source_id":"sample product1","related_object":"product","product":{"metadata":{"key":"value"}}},{"quantity":1,"price":15000,"source_id":"sample product2","related_object":"product","product":{"metadata":{"key":"value"}}}],"metadata":{"key":"value"}}} # RedemptionsRedeemRequestBody |  (optional)

    try:
        # Redeem Stackable Discounts
        api_response = api_instance.redeem_stacked_discounts(redemptions_redeem_request_body=redemptions_redeem_request_body)
        print("The response of RedemptionsApi->redeem_stacked_discounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RedemptionsApi->redeem_stacked_discounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redemptions_redeem_request_body** | [**RedemptionsRedeemRequestBody**](RedemptionsRedeemRequestBody.md)|  | [optional] 

### Return type

[**RedemptionsRedeemResponseBody**](RedemptionsRedeemResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Depending on your project settings: all redeemables must be valid or just one must be valid to result as valid redemption. See https://support.voucherify.io/article/604-stacking-rules#application-rules |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rollback_redemption**
> RedemptionsRollbackCreateResponseBody rollback_redemption(redemption_id, reason=reason, tracking_id=tracking_id, redemptions_rollback_create_request_body=redemptions_rollback_create_request_body)

Rollback Redemption

Your business logic may include a case when you need to undo a redemption. You can revert a redemption by calling this API endpoint.  🚧  You can roll back a redemption up to 3 months back.   # Effect  The operation  - creates a rollback entry in vouchers redemption history (redemption.redemption_entries) and  - gives 1 redemption back to the pool (decreases redeemed_quantity by 1).  # Returned funds  In case of *gift card vouchers*, this method returns funds back according to the source redemption. In case of *loyalty card vouchers*, this method returns points back according to the source redemption.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.redemptions_rollback_create_request_body import RedemptionsRollbackCreateRequestBody
from voucherify.models.redemptions_rollback_create_response_body import RedemptionsRollbackCreateResponseBody
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
    api_instance = voucherify.RedemptionsApi(api_client)
    redemption_id = 'redemption_id_example' # str | The original redemption ID to be rolled back (undone).
    reason = 'reason_example' # str | Reason for the rollback. (optional)
    tracking_id = 'tracking_id_example' # str | Customers source_id. (optional)
    redemptions_rollback_create_request_body = {"customer":{"id":"cust_SolpIN5N4oZbCnrxZ5NHrbVB","name":"Annie Lemons","email":"annie@lemon.com","phone":"+1 933 222 3334","birthday":"1900-12-02","birthdate":"1900-12-01","address":{"city":"New York","state":"NY","line_1":"123 Main St.","line_2":"APT 3 BLG 5","country":"United States","postal_code":"100012"},"metadata":{"age":23}},"order":{"source_id":"test_rollback_8"},"metadata":{"location_id":["L2"]}} # RedemptionsRollbackCreateRequestBody | Add information about the original customer and order. Customer data and Redemption metadata can be updated in Voucherify when passing the customer data in the request body. (optional)

    try:
        # Rollback Redemption
        api_response = api_instance.rollback_redemption(redemption_id, reason=reason, tracking_id=tracking_id, redemptions_rollback_create_request_body=redemptions_rollback_create_request_body)
        print("The response of RedemptionsApi->rollback_redemption:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RedemptionsApi->rollback_redemption: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redemption_id** | **str**| The original redemption ID to be rolled back (undone). | 
 **reason** | **str**| Reason for the rollback. | [optional] 
 **tracking_id** | **str**| Customers source_id. | [optional] 
 **redemptions_rollback_create_request_body** | [**RedemptionsRollbackCreateRequestBody**](RedemptionsRollbackCreateRequestBody.md)| Add information about the original customer and order. Customer data and Redemption metadata can be updated in Voucherify when passing the customer data in the request body. | [optional] 

### Return type

[**RedemptionsRollbackCreateResponseBody**](RedemptionsRollbackCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a redemption rollback object indicating the result of the rollback. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rollback_stacked_redemptions**
> RedemptionsRollbacksCreateResponseBody rollback_stacked_redemptions(parent_redemption_id, reason=reason, tracking_id=tracking_id, redemptions_rollbacks_create_request_body=redemptions_rollbacks_create_request_body)

Rollback Stackable Redemptions

Rollback a stackable redemption. When you rollback a stacked redemption, all child redemptions will be rolled back. Provide the parent redemption ID as the path parameter.  🚧   You can roll back a redemption up to 3 months back.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.redemptions_rollbacks_create_request_body import RedemptionsRollbacksCreateRequestBody
from voucherify.models.redemptions_rollbacks_create_response_body import RedemptionsRollbacksCreateResponseBody
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
    api_instance = voucherify.RedemptionsApi(api_client)
    parent_redemption_id = 'parent_redemption_id_example' # str | Unique identifier of a parent redemption, e.g. r_JQfm73zWSJFQxs3bGxweYjgm.
    reason = 'reason_example' # str | Reason for the rollback. (optional)
    tracking_id = 'tracking_id_example' # str | Customers source_id. (optional)
    redemptions_rollbacks_create_request_body = {"customer":{"id":"cust_SolpIN5N4oZbCnrxZ5NHrbVB","name":"Annie Lemons","email":"annie@lemon.com","phone":"+1 933 222 3334","birthday":"1900-12-02","birthdate":"1900-12-01","address":{"city":"New York","state":"NY","line_1":"123 Main St.","line_2":"APT 3 BLG 5","country":"United States","postal_code":"100012"},"metadata":{"age":23}},"order":{"source_id":"test_rollback_8"},"metadata":{"location_id":["L2"]}} # RedemptionsRollbacksCreateRequestBody | Add information about the original customer and order. Customer data and Redemption metadata can be updated in Voucherify when passing the customer data in the request body. (optional)

    try:
        # Rollback Stackable Redemptions
        api_response = api_instance.rollback_stacked_redemptions(parent_redemption_id, reason=reason, tracking_id=tracking_id, redemptions_rollbacks_create_request_body=redemptions_rollbacks_create_request_body)
        print("The response of RedemptionsApi->rollback_stacked_redemptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RedemptionsApi->rollback_stacked_redemptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_redemption_id** | **str**| Unique identifier of a parent redemption, e.g. r_JQfm73zWSJFQxs3bGxweYjgm. | 
 **reason** | **str**| Reason for the rollback. | [optional] 
 **tracking_id** | **str**| Customers source_id. | [optional] 
 **redemptions_rollbacks_create_request_body** | [**RedemptionsRollbacksCreateRequestBody**](RedemptionsRollbacksCreateRequestBody.md)| Add information about the original customer and order. Customer data and Redemption metadata can be updated in Voucherify when passing the customer data in the request body. | [optional] 

### Return type

[**RedemptionsRollbacksCreateResponseBody**](RedemptionsRollbacksCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns an array with the individual redemption rollback results along with the parent rollback result and related order. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

