# voucherify.ProductsApi

All URIs are relative to *https://api.voucherify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_product**](ProductsApi.md#create_product) | **POST** /v1/products | Create Product
[**create_sku**](ProductsApi.md#create_sku) | **POST** /v1/products/{productId}/skus | Create SKU
[**delete_product**](ProductsApi.md#delete_product) | **DELETE** /v1/products/{productId} | Delete Product
[**delete_sku**](ProductsApi.md#delete_sku) | **DELETE** /v1/products/{productId}/skus/{skuId} | Delete SKU
[**get_product**](ProductsApi.md#get_product) | **GET** /v1/products/{productId} | Get Product
[**get_sku**](ProductsApi.md#get_sku) | **GET** /v1/skus/{skuId} | Get SKU
[**import_products_using_csv**](ProductsApi.md#import_products_using_csv) | **POST** /v1/products/importCSV | Import Products using CSV
[**import_skus_using_csv**](ProductsApi.md#import_skus_using_csv) | **POST** /v1/skus/importCSV | Import SKUs using CSV
[**list_products**](ProductsApi.md#list_products) | **GET** /v1/products | List Products
[**list_skus_in_product**](ProductsApi.md#list_skus_in_product) | **GET** /v1/products/{productId}/skus | List SKUs in Product
[**update_product**](ProductsApi.md#update_product) | **PUT** /v1/products/{productId} | Update Product
[**update_products_in_bulk**](ProductsApi.md#update_products_in_bulk) | **POST** /v1/products/bulk/async | Update Products in Bulk
[**update_products_metadata_in_bulk**](ProductsApi.md#update_products_metadata_in_bulk) | **POST** /v1/products/metadata/async | Update Products&#39; Metadata in Bulk
[**update_sku**](ProductsApi.md#update_sku) | **PUT** /v1/products/{productId}/skus/{skuId} | Update SKU


# **create_product**
> ProductsCreateResponseBody create_product(products_create_request_body=products_create_request_body)

Create Product

Creates a product object.  📘 Upsert Mode  If you pass an id or a source_id that already exists in the product database, Voucherify will return a related product object with updated fields.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.products_create_request_body import ProductsCreateRequestBody
from voucherify.models.products_create_response_body import ProductsCreateResponseBody
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
    api_instance = voucherify.ProductsApi(api_client)
    products_create_request_body = {"source_id":"first_product","name":"Samsung Phone","price":200000,"attributes":["color","memory","processor"],"metadata":{"test":true,"vendor":"Online Store"},"image_url":"https://www.website.com/image.png"} # ProductsCreateRequestBody | Specify the product parameters. (optional)

    try:
        # Create Product
        api_response = api_instance.create_product(products_create_request_body=products_create_request_body)
        print("The response of ProductsApi->create_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->create_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **products_create_request_body** | [**ProductsCreateRequestBody**](ProductsCreateRequestBody.md)| Specify the product parameters. | [optional] 

### Return type

[**ProductsCreateResponseBody**](ProductsCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a product object if the operation succeeded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sku**
> ProductsSkusCreateResponseBody create_sku(product_id, products_skus_create_request_body=products_skus_create_request_body)

Create SKU

This method adds product variants to a created product.   📘 Upsert Mode  If you pass an id or a source_id that already exists in the sku database, Voucherify will return a related sku object with updated fields.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.products_skus_create_request_body import ProductsSkusCreateRequestBody
from voucherify.models.products_skus_create_response_body import ProductsSkusCreateResponseBody
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
    api_instance = voucherify.ProductsApi(api_client)
    product_id = 'product_id_example' # str | A Voucherify product ID or product source ID.
    products_skus_create_request_body = {"source_id":"first_product_sku_1","sku":"Samsung phone 256GB","price":1300,"currency":"USD","attributes":{"color":"vintage-black","memory":"256","processor":"Intel"},"image_url":"https://www.website.com/image.png","metadata":{"imported":true}} # ProductsSkusCreateRequestBody | Specify the SKU parameters to be created. (optional)

    try:
        # Create SKU
        api_response = api_instance.create_sku(product_id, products_skus_create_request_body=products_skus_create_request_body)
        print("The response of ProductsApi->create_sku:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->create_sku: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| A Voucherify product ID or product source ID. | 
 **products_skus_create_request_body** | [**ProductsSkusCreateRequestBody**](ProductsSkusCreateRequestBody.md)| Specify the SKU parameters to be created. | [optional] 

### Return type

[**ProductsSkusCreateResponseBody**](ProductsSkusCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the created SKU object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_product**
> delete_product(product_id, force=force)

Delete Product

Deletes a product and all related SKUs. This operation cannot be undone.  If the force parameter is set to false or not set at all, the product and all related SKUs will be moved to the bin.

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
    api_instance = voucherify.ProductsApi(api_client)
    product_id = 'product_id_example' # str | A Voucherify product ID or source ID.
    force = True # bool | If this flag is set to true, the product and all related SKUs will be removed permanently. If it is set to false or not set at all, the product and all related SKUs will be moved to the bin. Going forward, the user will be able to create another product with exactly the same source_id. (optional)

    try:
        # Delete Product
        api_instance.delete_product(product_id, force=force)
    except Exception as e:
        print("Exception when calling ProductsApi->delete_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| A Voucherify product ID or source ID. | 
 **force** | **bool**| If this flag is set to true, the product and all related SKUs will be removed permanently. If it is set to false or not set at all, the product and all related SKUs will be moved to the bin. Going forward, the user will be able to create another product with exactly the same source_id. | [optional] 

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

# **delete_sku**
> delete_sku(product_id, sku_id, force=force)

Delete SKU

Deletes a product SKU. This operation cannot be undone.  If the force parameter is set to false or not set at all, the SKU will be moved to the bin.

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
    api_instance = voucherify.ProductsApi(api_client)
    product_id = 'product_id_example' # str | A unique Voucherify product ID or product source ID.
    sku_id = 'sku_id_example' # str | A Voucherify SKU ID or SKU source ID.
    force = True # bool | If this flag is set to true, the SKU will be removed permanently. If it is set to false or not set at all, the SKU will be moved to the bin. Going forward, the user will be able to create another SKU with exactly the same source_id. (optional)

    try:
        # Delete SKU
        api_instance.delete_sku(product_id, sku_id, force=force)
    except Exception as e:
        print("Exception when calling ProductsApi->delete_sku: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| A unique Voucherify product ID or product source ID. | 
 **sku_id** | **str**| A Voucherify SKU ID or SKU source ID. | 
 **force** | **bool**| If this flag is set to true, the SKU will be removed permanently. If it is set to false or not set at all, the SKU will be moved to the bin. Going forward, the user will be able to create another SKU with exactly the same source_id. | [optional] 

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

# **get_product**
> ProductsGetResponseBody get_product(product_id)

Get Product

Retrieve product details.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.products_get_response_body import ProductsGetResponseBody
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
    api_instance = voucherify.ProductsApi(api_client)
    product_id = 'product_id_example' # str | A Voucherify product ID or source ID.

    try:
        # Get Product
        api_response = api_instance.get_product(product_id)
        print("The response of ProductsApi->get_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->get_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| A Voucherify product ID or source ID. | 

### Return type

[**ProductsGetResponseBody**](ProductsGetResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a product object if a valid identifier was provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sku**
> SkusGetResponseBody get_sku(sku_id)

Get SKU

Retrieve details of a SKU.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.skus_get_response_body import SkusGetResponseBody
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
    api_instance = voucherify.ProductsApi(api_client)
    sku_id = 'sku_id_example' # str | A Voucherify SKU identifier or SKU source ID.

    try:
        # Get SKU
        api_response = api_instance.get_sku(sku_id)
        print("The response of ProductsApi->get_sku:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->get_sku: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku_id** | **str**| A Voucherify SKU identifier or SKU source ID. | 

### Return type

[**SkusGetResponseBody**](SkusGetResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns requested SKU object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_products_using_csv**
> ProductsImportCsvCreateResponseBody import_products_using_csv(file=file)

Import Products using CSV

Import products into the repository using a CSV file.   This API request starts a process that affects Voucherify data in bulk.  In case of small jobs (like bulk update) the request is put into a queue and processed once every other bulk request placed in the queue prior to this request is finished. However, when the job takes a longer time (like vouchers generation) then it is processed in small portions in a round-robin fashion. When there is a list of vouchers generation scheduled, then they will all have the IN_PROGRESS status shortly. This way, small jobs added just after scheduling big jobs of the same type will be processed in a short time window.  The result will return the async ID. You can verify the status of your request via this API request.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.products_import_csv_create_response_body import ProductsImportCsvCreateResponseBody
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
    api_instance = voucherify.ProductsApi(api_client)
    file = None # bytearray | File path. (optional)

    try:
        # Import Products using CSV
        api_response = api_instance.import_products_using_csv(file=file)
        print("The response of ProductsApi->import_products_using_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->import_products_using_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**| File path. | [optional] 

### Return type

[**ProductsImportCsvCreateResponseBody**](ProductsImportCsvCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns ID of the scheduled async action. The response informs you that your request has been accepted and products will be added to the repository asynchronously. To check the import status and result, copy the &#x60;async_action_id&#x60; from the response and pass it using the &lt;!-- [Get Async Action](OpenAPI.json/paths/~1async-actions~1{asyncActionId}/get) --&gt;[Get Async Action](ref:get-async-action) endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_skus_using_csv**
> SkusImportCsvCreateResponseBody import_skus_using_csv(file=file)

Import SKUs using CSV

Import SKUs into the repository using a CSV file. The CSV file has to include headers in the first line. All properties which cannot be mapped to standard SKU fields will be added to the metadata object. You can find an example template [here](https://s3.amazonaws.com/helpscout.net/docs/assets/5902f1c12c7d3a057f88a36d/attachments/627b98d08c9b585083488a4c/Import_SKUS_template.csv).  This API request starts a process that affects Voucherify data in bulk.  In case of small jobs (like bulk update) the request is put into a queue and processed once every other bulk request placed in the queue prior to this request is finished. However, when the job takes a longer time (like vouchers generation) then it is processed in small portions in a round-robin fashion. When there is a list of vouchers generation scheduled, then they will all have the IN_PROGRESS status shortly. This way, small jobs added just after scheduling big jobs of the same type will be processed in a short time window.  The result will return the async ID. You can verify the status of your request via this API request.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.skus_import_csv_create_response_body import SkusImportCsvCreateResponseBody
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
    api_instance = voucherify.ProductsApi(api_client)
    file = None # bytearray | File path. (optional)

    try:
        # Import SKUs using CSV
        api_response = api_instance.import_skus_using_csv(file=file)
        print("The response of ProductsApi->import_skus_using_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->import_skus_using_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**| File path. | [optional] 

### Return type

[**SkusImportCsvCreateResponseBody**](SkusImportCsvCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns ID of the scheduled async action. The response informs you that your request has been accepted and SKUs will be added to the repository asynchronously. To check the import status and result, copy the &#x60;async_action_id&#x60; from the response and pass it using the &lt;!-- [Get Async Action](OpenAPI.json/paths/~1async-actions~1{asyncActionId}/get) --&gt;[Get Async Action](ref:get-async-action) endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_products**
> ProductsListResponseBody list_products(limit=limit, page=page, order=order, start_date=start_date, end_date=end_date)

List Products

Retrieve a list of products.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.parameter_order import ParameterOrder
from voucherify.models.products_list_response_body import ProductsListResponseBody
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
    api_instance = voucherify.ProductsApi(api_client)
    limit = 56 # int | Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. (optional)
    page = 56 # int | Which page of results to return. The lowest value is 1. (optional)
    order = voucherify.ParameterOrder() # ParameterOrder | Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp representing the date and time which results must end on. Represented in ISO 8601 format. (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp representing the date and time which results must end on. Represented in ISO 8601 format. (optional)

    try:
        # List Products
        api_response = api_instance.list_products(limit=limit, page=page, order=order, start_date=start_date, end_date=end_date)
        print("The response of ProductsApi->list_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->list_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. | [optional] 
 **page** | **int**| Which page of results to return. The lowest value is 1. | [optional] 
 **order** | [**ParameterOrder**](.md)| Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. | [optional] 
 **start_date** | **datetime**| Timestamp representing the date and time which results must end on. Represented in ISO 8601 format. | [optional] 
 **end_date** | **datetime**| Timestamp representing the date and time which results must end on. Represented in ISO 8601 format. | [optional] 

### Return type

[**ProductsListResponseBody**](ProductsListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a dictionary with product objects. The products are returned sorted by creation date by default, with the most recent products appearing last, unless you specify another sequence using the &#x60;order&#x60; query parameter. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_skus_in_product**
> ProductsSkusListResponseBody list_skus_in_product(product_id, limit=limit, page=page, order=order, start_date=start_date, end_date=end_date)

List SKUs in Product

Retrieve all SKUs for a given product.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.parameter_order import ParameterOrder
from voucherify.models.products_skus_list_response_body import ProductsSkusListResponseBody
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
    api_instance = voucherify.ProductsApi(api_client)
    product_id = 'product_id_example' # str | A Voucherify product ID or product source ID.
    limit = 56 # int | Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. (optional)
    page = 56 # int | Which page of results to return. The lowest value is 1. (optional)
    order = voucherify.ParameterOrder() # ParameterOrder | Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp representing the date and time which results must end on. Represented in ISO 8601 format. (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp representing the date and time which results must end on. Represented in ISO 8601 format. (optional)

    try:
        # List SKUs in Product
        api_response = api_instance.list_skus_in_product(product_id, limit=limit, page=page, order=order, start_date=start_date, end_date=end_date)
        print("The response of ProductsApi->list_skus_in_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->list_skus_in_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| A Voucherify product ID or product source ID. | 
 **limit** | **int**| Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. | [optional] 
 **page** | **int**| Which page of results to return. The lowest value is 1. | [optional] 
 **order** | [**ParameterOrder**](.md)| Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. | [optional] 
 **start_date** | **datetime**| Timestamp representing the date and time which results must end on. Represented in ISO 8601 format. | [optional] 
 **end_date** | **datetime**| Timestamp representing the date and time which results must end on. Represented in ISO 8601 format. | [optional] 

### Return type

[**ProductsSkusListResponseBody**](ProductsSkusListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a dictionary of SKUs. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_product**
> ProductsUpdateResponseBody update_product(product_id, products_update_request_body=products_update_request_body)

Update Product

Updates the specified product by setting the values of the parameters passed in the request body. Any parameters not provided in the payload will be left unchanged.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.products_update_request_body import ProductsUpdateRequestBody
from voucherify.models.products_update_response_body import ProductsUpdateResponseBody
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
    api_instance = voucherify.ProductsApi(api_client)
    product_id = 'product_id_example' # str | A Voucherify product ID or source ID.
    products_update_request_body = {"price":210000} # ProductsUpdateRequestBody | Specify the parameters of the product that are to be updated. (optional)

    try:
        # Update Product
        api_response = api_instance.update_product(product_id, products_update_request_body=products_update_request_body)
        print("The response of ProductsApi->update_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->update_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| A Voucherify product ID or source ID. | 
 **products_update_request_body** | [**ProductsUpdateRequestBody**](ProductsUpdateRequestBody.md)| Specify the parameters of the product that are to be updated. | [optional] 

### Return type

[**ProductsUpdateResponseBody**](ProductsUpdateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns an updated product object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_products_in_bulk**
> ProductsUpdateInBulkResponseBody update_products_in_bulk(products_update_in_bulk_request_body=products_update_in_bulk_request_body)

Update Products in Bulk

Update products in one asynchronous operation. The request can include up to **10 MB** of data. The response returns a unique asynchronous action ID. Use this ID in the query paramater of the GET Async Action endpoint to check, e.g.: - The status of your request (in queue, in progress, done, or failed) - Resources that failed to be updated - The report file with details about the update If a product object is not found, it is **upserted**. This is shown in the report file in the GET Async Action endpoint. The upserted resources have value false in the found column and true in the updated column. This API request starts a process that affects Voucherify data in bulk. In the case of small jobs (like bulk update), the request is put into a queue and processed when every other bulk request placed in the queue prior to this request is finished.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.products_update_in_bulk_request_body import ProductsUpdateInBulkRequestBody
from voucherify.models.products_update_in_bulk_response_body import ProductsUpdateInBulkResponseBody
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
    api_instance = voucherify.ProductsApi(api_client)
    products_update_in_bulk_request_body = [{"source_id":"first_product","name":"Samsung Phone 1","price":220000,"attributes":["color","memory","processor"],"metadata":{"test":true,"vendor":"Online Store - 3"},"image_url":"https://voucherify-uploads.s3.amazonaws.com/org_2qt8DYlM/img_Z2qvs2KFnQyo2Ohz4uhsjGtf.png"},{"source_id":"second_product","name":"Samsung Phone 2","price":230000,"attributes":["color","memory","processor"],"metadata":{"test":true,"vendor":"Online Store - 4"},"image_url":"https://voucherify-uploads.s3.amazonaws.com/org_2qt8DYlM/img_Z2qvs2KFnQyo2Ohz4uhsjGtf.png"}] # List[ProductsUpdateInBulkRequestBody] | List the product fields to be updated in each customer object. (optional)

    try:
        # Update Products in Bulk
        api_response = api_instance.update_products_in_bulk(products_update_in_bulk_request_body=products_update_in_bulk_request_body)
        print("The response of ProductsApi->update_products_in_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->update_products_in_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **products_update_in_bulk_request_body** | [**List[ProductsUpdateInBulkRequestBody]**](ProductsUpdateInBulkRequestBody.md)| List the product fields to be updated in each customer object. | [optional] 

### Return type

[**ProductsUpdateInBulkResponseBody**](ProductsUpdateInBulkResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the ID of the scheduled asynchronous action. The response informs you that the request has been accepted and the resources will be updated in the repository asynchronously. To check the status and result, copy the &#x60;async_action_id&#x60; from the response and use it as a query parameter in the [GET Async Action](ref:get-async-action) endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_products_metadata_in_bulk**
> ProductsMetadataUpdateInBulkResponseBody update_products_metadata_in_bulk(products_metadata_update_in_bulk_request_body=products_metadata_update_in_bulk_request_body)

Update Products' Metadata in Bulk

Updates metadata parameters for a list of products. Every resource in the list will receive the metadata defined in the request. The request can include up to **10 MB** of data. The response returns a unique asynchronous action ID. Use this ID in the query paramater of the GET Async Action endpoint to check, e.g.: - The status of your request (in queue, in progress, done, or failed) - Resources that failed to be updated - The report file with details about the update If a product object is not found, it is **upserted**. This is shown in the report file in the GET Async Action endpoint. The upserted resources have value false in the found column and true in the updated column. This API request starts a process that affects Voucherify data in bulk. In the case of small jobs (like bulk update), the request is put into a queue and processed when every other bulk request placed in the queue prior to this request is finished.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.products_metadata_update_in_bulk_request_body import ProductsMetadataUpdateInBulkRequestBody
from voucherify.models.products_metadata_update_in_bulk_response_body import ProductsMetadataUpdateInBulkResponseBody
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
    api_instance = voucherify.ProductsApi(api_client)
    products_metadata_update_in_bulk_request_body = {"source_ids":["123-567-3433","test_volleyball"],"metadata":{"label":true,"origin":"PL"}} # ProductsMetadataUpdateInBulkRequestBody | List the source_ids of the products you would like to update with the metadata key/value pairs. (optional)

    try:
        # Update Products' Metadata in Bulk
        api_response = api_instance.update_products_metadata_in_bulk(products_metadata_update_in_bulk_request_body=products_metadata_update_in_bulk_request_body)
        print("The response of ProductsApi->update_products_metadata_in_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->update_products_metadata_in_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **products_metadata_update_in_bulk_request_body** | [**ProductsMetadataUpdateInBulkRequestBody**](ProductsMetadataUpdateInBulkRequestBody.md)| List the source_ids of the products you would like to update with the metadata key/value pairs. | [optional] 

### Return type

[**ProductsMetadataUpdateInBulkResponseBody**](ProductsMetadataUpdateInBulkResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the ID of the scheduled asynchronous action. The response informs you that the request has been accepted and the resources will be updated in the repository asynchronously. To check the status and result, copy the &#x60;async_action_id&#x60; from the response and use it as a query parameter in the [GET Async Action](ref:get-async-action) endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sku**
> ProductsSkusUpdateResponseBody update_sku(product_id, sku_id, products_skus_update_request_body=products_skus_update_request_body)

Update SKU

Updates the specified SKU by setting the values of the parameters passed in the request body. Any parameters not provided in the payload will be left unchanged. Fields other than the ones listed in the request body schema wont be modified. Even if provided, they will be silently skipped.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.products_skus_update_request_body import ProductsSkusUpdateRequestBody
from voucherify.models.products_skus_update_response_body import ProductsSkusUpdateResponseBody
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
    api_instance = voucherify.ProductsApi(api_client)
    product_id = 'product_id_example' # str | A unique Voucherify product ID or product source ID.
    sku_id = 'sku_id_example' # str | A Voucherify SKU ID or SKU source ID.
    products_skus_update_request_body = {"price":210000,"currency":"PLN"} # ProductsSkusUpdateRequestBody | Specify the parameters to be updated. (optional)

    try:
        # Update SKU
        api_response = api_instance.update_sku(product_id, sku_id, products_skus_update_request_body=products_skus_update_request_body)
        print("The response of ProductsApi->update_sku:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->update_sku: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| A unique Voucherify product ID or product source ID. | 
 **sku_id** | **str**| A Voucherify SKU ID or SKU source ID. | 
 **products_skus_update_request_body** | [**ProductsSkusUpdateRequestBody**](ProductsSkusUpdateRequestBody.md)| Specify the parameters to be updated. | [optional] 

### Return type

[**ProductsSkusUpdateResponseBody**](ProductsSkusUpdateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the SKU object with the updated parameters. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

