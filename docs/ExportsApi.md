# voucherify.ExportsApi

All URIs are relative to *https://api.voucherify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_export**](ExportsApi.md#create_export) | **POST** /v1/exports | Create Export
[**delete_export**](ExportsApi.md#delete_export) | **DELETE** /v1/exports/{exportId} | Delete Export
[**download_export**](ExportsApi.md#download_export) | **GET** /v1/exports/{export_Id} | Download Export
[**get_export**](ExportsApi.md#get_export) | **GET** /v1/exports/{exportId} | Get Export
[**list_exports**](ExportsApi.md#list_exports) | **GET** /v1/exports | List Exports


# **create_export**
> ExportsCreateResponseBody create_export(exports_create_request_body=exports_create_request_body)

Create Export

Create export object. The export can be any of the following types: voucher, redemption, publication, customer, order, points_expiration, or voucher_transactions.   # Defaults If you only specify the object type in the request body without specifying the fields, the API will return the following fields per export object:   # Fetching particular data sets Using the parameters body parameter, you can narrow down which fields to export and how to filter the results. The fields are an array of strings containing the data that you would like to export. These fields define the headers in the CSV file. The array can be a combination of any of the following available fields: # Orders     # Vouchers        # Publications   # Redemptions    # Customers       # Points Expirations    # Gift Card Transactions    # Loyalty Card Transactions   

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.exports_create_request_body import ExportsCreateRequestBody
from voucherify.models.exports_create_response_body import ExportsCreateResponseBody
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
    api_instance = voucherify.ExportsApi(api_client)
    exports_create_request_body = voucherify.ExportsCreateRequestBody() # ExportsCreateRequestBody | Specify the details of the export that you would like to create. (optional)

    try:
        # Create Export
        api_response = api_instance.create_export(exports_create_request_body=exports_create_request_body)
        print("The response of ExportsApi->create_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->create_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exports_create_request_body** | [**ExportsCreateRequestBody**](ExportsCreateRequestBody.md)| Specify the details of the export that you would like to create. | [optional] 

### Return type

[**ExportsCreateResponseBody**](ExportsCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns export object and URL of CSV file. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_export**
> delete_export(export_id)

Delete Export

This method deletes a previously created export object.

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
    api_instance = voucherify.ExportsApi(api_client)
    export_id = 'export_id_example' # str | Unique export object ID of previously created export. This object can be a: voucher, redemption, publication, customer, order, points_expiration, or voucher_transactions.

    try:
        # Delete Export
        api_instance.delete_export(export_id)
    except Exception as e:
        print("Exception when calling ExportsApi->delete_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_id** | **str**| Unique export object ID of previously created export. This object can be a: voucher, redemption, publication, customer, order, points_expiration, or voucher_transactions. | 

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

# **download_export**
> str download_export(export_id, token=token)

Download Export

Download the contents of the exported CSV file.   📘 Important notes  **Base URL:**   - https://download.voucherify.io (Europe)   - https://us1.download.voucherify.io (US)   - https://as1.download.voucherify.io (Asia)   **Token:** Can be found within the result parameter of the Get Export method response.

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
    api_instance = voucherify.ExportsApi(api_client)
    export_id = 'exp_ex6zq0x0EEa9S0N68QcqhxcQ' # str | Unique export object ID.
    token = 'token_example' # str | Token that was issued to the export, to get this token, get the export first (optional)

    try:
        # Download Export
        api_response = api_instance.download_export(export_id, token=token)
        print("The response of ExportsApi->download_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->download_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_id** | **str**| Unique export object ID. | 
 **token** | **str**| Token that was issued to the export, to get this token, get the export first | [optional] 

### Return type

**str**

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns contents of CSV file. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_export**
> ExportsGetResponseBody get_export(export_id)

Get Export

Retrieves the URL of the downloadable file, which was generated via the Create Export method.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.exports_get_response_body import ExportsGetResponseBody
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
    api_instance = voucherify.ExportsApi(api_client)
    export_id = 'export_id_example' # str | Unique export object ID of previously created export. This object can be a: voucher, redemption, publication, customer, order, points_expiration, or voucher_transactions.

    try:
        # Get Export
        api_response = api_instance.get_export(export_id)
        print("The response of ExportsApi->get_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->get_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_id** | **str**| Unique export object ID of previously created export. This object can be a: voucher, redemption, publication, customer, order, points_expiration, or voucher_transactions. | 

### Return type

[**ExportsGetResponseBody**](ExportsGetResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the export object if a valid identifier was provided in the path. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_exports**
> ExportsListResponseBody list_exports(limit=limit, page=page, order=order)

List Exports

List all exports. 

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.exports_list_response_body import ExportsListResponseBody
from voucherify.models.parameter_order_list_exports import ParameterOrderListExports
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
    api_instance = voucherify.ExportsApi(api_client)
    limit = 56 # int | Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. (optional)
    page = 56 # int | Which page of results to return. The lowest value is 1. (optional)
    order = voucherify.ParameterOrderListExports() # ParameterOrderListExports | Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. (optional)

    try:
        # List Exports
        api_response = api_instance.list_exports(limit=limit, page=page, order=order)
        print("The response of ExportsApi->list_exports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->list_exports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. | [optional] 
 **page** | **int**| Which page of results to return. The lowest value is 1. | [optional] 
 **order** | [**ParameterOrderListExports**](.md)| Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. | [optional] 

### Return type

[**ExportsListResponseBody**](ExportsListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | A dictionary with an exports property that contains an array of exports. Each entry in the array is a separate export object. The list will return the following types of exported objects: &#x60;voucher&#x60;, &#x60;redemption&#x60;, &#x60;publication&#x60;, &#x60;customer&#x60;, &#x60;order&#x60;, &#x60;points_expiration&#x60;, or &#x60;voucher_transactions&#x60;.   The &#x60;channel&#x60; parameter in the response body returns the channel that was used to generate the particular export. The &#x60;user_id&#x60; identifies the specific user who initiated the export through the Voucherify Dashboard; this &#x60;user_id&#x60; is returned when the channel value is &#x60;WEBSITE&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

