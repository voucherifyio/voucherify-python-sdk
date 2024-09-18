# voucherify.ProductCollectionsApi

All URIs are relative to *https://api.voucherify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_product_collection**](ProductCollectionsApi.md#create_product_collection) | **POST** /v1/product-collections | Create Product Collection
[**delete_product_collection**](ProductCollectionsApi.md#delete_product_collection) | **DELETE** /v1/product-collections/{productCollectionId} | Delete Product Collection
[**get_product_collection**](ProductCollectionsApi.md#get_product_collection) | **GET** /v1/product-collections/{productCollectionId} | Get Product Collection
[**list_product_collections**](ProductCollectionsApi.md#list_product_collections) | **GET** /v1/product-collections | List Product Collections
[**list_products_in_collection**](ProductCollectionsApi.md#list_products_in_collection) | **GET** /v1/product-collections/{productCollectionId}/products | List Products in Collection


# **create_product_collection**
> ProductCollectionsCreateResponseBody create_product_collection(product_collections_create_request_body=product_collections_create_request_body)

Create Product Collection

This method creates a new product collection.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.product_collections_create_request_body import ProductCollectionsCreateRequestBody
from voucherify.models.product_collections_create_response_body import ProductCollectionsCreateResponseBody
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
    api_instance = voucherify.ProductCollectionsApi(api_client)
    product_collections_create_request_body = voucherify.ProductCollectionsCreateRequestBody() # ProductCollectionsCreateRequestBody |  (optional)

    try:
        # Create Product Collection
        api_response = api_instance.create_product_collection(product_collections_create_request_body=product_collections_create_request_body)
        print("The response of ProductCollectionsApi->create_product_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductCollectionsApi->create_product_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_collections_create_request_body** | [**ProductCollectionsCreateRequestBody**](ProductCollectionsCreateRequestBody.md)|  | [optional] 

### Return type

[**ProductCollectionsCreateResponseBody**](ProductCollectionsCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns information about the newly created collection, as well as an array containing the products. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_product_collection**
> delete_product_collection(product_collection_id)

Delete Product Collection

This method deletes a product collection.

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
    api_instance = voucherify.ProductCollectionsApi(api_client)
    product_collection_id = 'product_collection_id_example' # str | A unique product collection ID.

    try:
        # Delete Product Collection
        api_instance.delete_product_collection(product_collection_id)
    except Exception as e:
        print("Exception when calling ProductCollectionsApi->delete_product_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_collection_id** | **str**| A unique product collection ID. | 

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

# **get_product_collection**
> ProductCollectionsGetResponseBody get_product_collection(product_collection_id)

Get Product Collection

Retrieves the product collection.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.product_collections_get_response_body import ProductCollectionsGetResponseBody
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
    api_instance = voucherify.ProductCollectionsApi(api_client)
    product_collection_id = 'product_collection_id_example' # str | A unique product collection ID.

    try:
        # Get Product Collection
        api_response = api_instance.get_product_collection(product_collection_id)
        print("The response of ProductCollectionsApi->get_product_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductCollectionsApi->get_product_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_collection_id** | **str**| A unique product collection ID. | 

### Return type

[**ProductCollectionsGetResponseBody**](ProductCollectionsGetResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a product collection object if a valid identifier was provided in the path. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_product_collections**
> ProductCollectionsListResponseBody list_product_collections(limit=limit, page=page, order=order)

List Product Collections

This method returns a list of product collections.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.parameter_order import ParameterOrder
from voucherify.models.product_collections_list_response_body import ProductCollectionsListResponseBody
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
    api_instance = voucherify.ProductCollectionsApi(api_client)
    limit = 56 # int | Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. (optional)
    page = 56 # int | Which page of results to return. The lowest value is 1. (optional)
    order = voucherify.ParameterOrder() # ParameterOrder | Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. (optional)

    try:
        # List Product Collections
        api_response = api_instance.list_product_collections(limit=limit, page=page, order=order)
        print("The response of ProductCollectionsApi->list_product_collections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductCollectionsApi->list_product_collections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. | [optional] 
 **page** | **int**| Which page of results to return. The lowest value is 1. | [optional] 
 **order** | [**ParameterOrder**](.md)| Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. | [optional] 

### Return type

[**ProductCollectionsListResponseBody**](ProductCollectionsListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a dictionary containing a list of product collections and details about each product collection. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_products_in_collection**
> ProductCollectionsProductsListResponseBody list_products_in_collection(product_collection_id, limit=limit, page=page, order=order, starting_after=starting_after)

List Products in Collection

Retrieves list of products from a product collection; works for both dynamic and static product collections.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.parameter_order import ParameterOrder
from voucherify.models.product_collections_products_list_response_body import ProductCollectionsProductsListResponseBody
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
    api_instance = voucherify.ProductCollectionsApi(api_client)
    product_collection_id = 'product_collection_id_example' # str | Unique product collection ID.
    limit = 56 # int | Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. (optional)
    page = 56 # int | Which page of results to return. The lowest value is 1. (optional)
    order = voucherify.ParameterOrder() # ParameterOrder | Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. (optional)
    starting_after = '2013-10-20T19:20:30+01:00' # datetime | Timestamp representing the date and time to use in starting_after cursor to get more data. Represented in ISO 8601 format. (optional)

    try:
        # List Products in Collection
        api_response = api_instance.list_products_in_collection(product_collection_id, limit=limit, page=page, order=order, starting_after=starting_after)
        print("The response of ProductCollectionsApi->list_products_in_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductCollectionsApi->list_products_in_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_collection_id** | **str**| Unique product collection ID. | 
 **limit** | **int**| Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. | [optional] 
 **page** | **int**| Which page of results to return. The lowest value is 1. | [optional] 
 **order** | [**ParameterOrder**](.md)| Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. | [optional] 
 **starting_after** | **datetime**| Timestamp representing the date and time to use in starting_after cursor to get more data. Represented in ISO 8601 format. | [optional] 

### Return type

[**ProductCollectionsProductsListResponseBody**](ProductCollectionsProductsListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a dictionary of products and/or SKUs grouped in the collection with each product&#39;s/SKU&#39;s details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

