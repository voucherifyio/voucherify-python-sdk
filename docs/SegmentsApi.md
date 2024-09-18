# voucherify.SegmentsApi

All URIs are relative to *https://api.voucherify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_segment**](SegmentsApi.md#create_segment) | **POST** /v1/segments | Create Segment
[**delete_segment**](SegmentsApi.md#delete_segment) | **DELETE** /v1/segments/{segmentId} | Delete Segment
[**get_segment**](SegmentsApi.md#get_segment) | **GET** /v1/segments/{segmentId} | Get Segment


# **create_segment**
> SegmentsCreateResponseBody create_segment(segments_create_request_body=segments_create_request_body)

Create Segment

Create a customer segment.  🚧 Limit on Static Segments  There is a cap on the number of customers that you can assign to a static segment: **20,000**. If you would like to create a bigger segment, then you can use the unlimited auto-update segment instead and use some customer metadata to build this segment.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.segments_create_request_body import SegmentsCreateRequestBody
from voucherify.models.segments_create_response_body import SegmentsCreateResponseBody
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
    api_instance = voucherify.SegmentsApi(api_client)
    segments_create_request_body = {"name":"Customers in a new Segment","type":"static","customers":["cust_iajsExT2QB4sGWzABY85WRqV","cust_sehkNIi8Uq2qQuRqSr7xn4Zi"]} # SegmentsCreateRequestBody | Specify the boundary conditions for the customer segment. (optional)

    try:
        # Create Segment
        api_response = api_instance.create_segment(segments_create_request_body=segments_create_request_body)
        print("The response of SegmentsApi->create_segment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentsApi->create_segment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segments_create_request_body** | [**SegmentsCreateRequestBody**](SegmentsCreateRequestBody.md)| Specify the boundary conditions for the customer segment. | [optional] 

### Return type

[**SegmentsCreateResponseBody**](SegmentsCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a customer segment object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_segment**
> delete_segment(segment_id)

Delete Segment

This method deletes a customer segment.

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
    api_instance = voucherify.SegmentsApi(api_client)
    segment_id = 'segment_id_example' # str | A unique customer segment ID.

    try:
        # Delete Segment
        api_instance.delete_segment(segment_id)
    except Exception as e:
        print("Exception when calling SegmentsApi->delete_segment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_id** | **str**| A unique customer segment ID. | 

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

# **get_segment**
> SegmentsGetResponseBody get_segment(segment_id)

Get Segment

Retrieves the segment with given segment ID.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.segments_get_response_body import SegmentsGetResponseBody
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
    api_instance = voucherify.SegmentsApi(api_client)
    segment_id = 'segment_id_example' # str | A unique customer segment ID.

    try:
        # Get Segment
        api_response = api_instance.get_segment(segment_id)
        print("The response of SegmentsApi->get_segment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentsApi->get_segment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_id** | **str**| A unique customer segment ID. | 

### Return type

[**SegmentsGetResponseBody**](SegmentsGetResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns segment object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

