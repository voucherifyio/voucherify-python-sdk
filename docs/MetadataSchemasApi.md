# voucherify.MetadataSchemasApi

All URIs are relative to *https://api.voucherify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_metadata_schema**](MetadataSchemasApi.md#get_metadata_schema) | **GET** /v1/metadata-schemas/{resource} | Get Metadata Schema
[**list_metadata_schemas**](MetadataSchemasApi.md#list_metadata_schemas) | **GET** /v1/metadata-schemas | List Metadata Schemas


# **get_metadata_schema**
> MetadataSchemasGetResponseBody get_metadata_schema(resource)

Get Metadata Schema

Retrieves a metadata schema per resource type. # Resource types ## Standard You can retrieve metadata schemas for the standard metadata schema definitions listed below. Add one of these types as the resource path parameter. - campaign - customer - earning_rule - loyalty_tier - order - order_item - product - promotion_tier - publication - redemption - reward - voucher ## Custom If you have defined a [custom metadata schema](https://support.voucherify.io/article/99-schema-validation-metadata#add-metadata), provide its name in the resource field to retrieve its details. 📘 Management API If you have Management API enabled, you can also use the Get Metadata Schemas endpoint to retrieve a metadata schema using its ID.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.metadata_schemas_get_response_body import MetadataSchemasGetResponseBody
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
    api_instance = voucherify.MetadataSchemasApi(api_client)
    resource = 'resource_example' # str | There is an infinite number of possibilities for retrieving metadata schemas by the resource type because you can define custom metadata schemas.

    try:
        # Get Metadata Schema
        api_response = api_instance.get_metadata_schema(resource)
        print("The response of MetadataSchemasApi->get_metadata_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataSchemasApi->get_metadata_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| There is an infinite number of possibilities for retrieving metadata schemas by the resource type because you can define custom metadata schemas. | 

### Return type

[**MetadataSchemasGetResponseBody**](MetadataSchemasGetResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | The response does not include unknown metadata properties in the response, i.e. those that have been defined outside of the **Project Settings** &gt; **Metadata Schema** definitions. For example, an unknown metadata property can be defined in the campaign manager. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_metadata_schemas**
> MetadataSchemasListResponseBody list_metadata_schemas()

List Metadata Schemas

Retrieve metadata schema definitions. 📘 Management API If you have Management API enabled, you can also use the List Metadata Schemas endpoint to list all metadata schemas.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.metadata_schemas_list_response_body import MetadataSchemasListResponseBody
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
    api_instance = voucherify.MetadataSchemasApi(api_client)

    try:
        # List Metadata Schemas
        api_response = api_instance.list_metadata_schemas()
        print("The response of MetadataSchemasApi->list_metadata_schemas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataSchemasApi->list_metadata_schemas: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MetadataSchemasListResponseBody**](MetadataSchemasListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns an array of metadata schema definitions. The response does not include unknown metadata properties in the response, i.e. those that have been defined outside of the **Project Settings** &gt; **Metadata Schema** definitions. For example, an unknown metadata property can be defined in the campaign manager while creating a campaign. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

