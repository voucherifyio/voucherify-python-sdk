# voucherify.AsyncActionsApi

All URIs are relative to *https://api.voucherify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_async_action**](AsyncActionsApi.md#get_async_action) | **GET** /v1/async-actions/{asyncActionId} | Get Async Action
[**list_async_actions**](AsyncActionsApi.md#list_async_actions) | **GET** /v1/async-actions | List Async Actions


# **get_async_action**
> AsyncActionGetResponseBody get_async_action(async_action_id)

Get Async Action

Check the result of a scheduled asynchronous operation.   The table below lists the possible types of async actions. The types are different for each endpoint generating the async action. If you would like to learn more about importing data into Voucherify, read more [here](https://support.voucherify.io/article/574-data-import).       

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.async_action_get_response_body import AsyncActionGetResponseBody
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
    api_instance = voucherify.AsyncActionsApi(api_client)
    async_action_id = 'async_action_id_example' # str | Unique ID of the asynchronous operation.

    try:
        # Get Async Action
        api_response = api_instance.get_async_action(async_action_id)
        print("The response of AsyncActionsApi->get_async_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AsyncActionsApi->get_async_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **async_action_id** | **str**| Unique ID of the asynchronous operation. | 

### Return type

[**AsyncActionGetResponseBody**](AsyncActionGetResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns detailed information about the async action result. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_async_actions**
> AsyncActionsListResponseBody list_async_actions(limit=limit, end_date=end_date)

List Async Actions

Track asynchronous operations scheduled in your project.   The table below lists the possible types of async actions. The types are different for each endpoint generating the async action. If you would like to learn more about importing data into Voucherify, read more [here](https://support.voucherify.io/article/574-data-import).       

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.async_actions_list_response_body import AsyncActionsListResponseBody
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
    api_instance = voucherify.AsyncActionsApi(api_client)
    limit = 56 # int | Limit the number of asynchronous actions that the API returns in the response. (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | Limits results to actions scheduled before the end_date. The date format needs to be consistent with ISO 8601 format (2016-11-16T14:14:31Z or 2016-11-16).  (optional)

    try:
        # List Async Actions
        api_response = api_instance.list_async_actions(limit=limit, end_date=end_date)
        print("The response of AsyncActionsApi->list_async_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AsyncActionsApi->list_async_actions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limit the number of asynchronous actions that the API returns in the response. | [optional] 
 **end_date** | **datetime**| Limits results to actions scheduled before the end_date. The date format needs to be consistent with ISO 8601 format (2016-11-16T14:14:31Z or 2016-11-16).  | [optional] 

### Return type

[**AsyncActionsListResponseBody**](AsyncActionsListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a list of all scheduled asynchronous actions and detailed information for each scheduled action. Note that a status &#x60;DONE&#x60;doesn&#39;t include the result of the completed action. If you need more information about the result, use the ID of the respective async action to call the &lt;!-- [Get Async Action](OpenAPI.json/paths/~1async-actions~1{asyncActionId}/get) --&gt;[Get Async Action](ref:get-async-action) endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

