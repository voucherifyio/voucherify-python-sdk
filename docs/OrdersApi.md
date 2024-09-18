# voucherify.OrdersApi

All URIs are relative to *https://api.voucherify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_order**](OrdersApi.md#create_order) | **POST** /v1/orders | Create Order
[**create_order_export**](OrdersApi.md#create_order_export) | **POST** /v1/orders/export | Create Orders Export
[**get_order**](OrdersApi.md#get_order) | **GET** /v1/orders/{orderId} | Get Order
[**import_orders**](OrdersApi.md#import_orders) | **POST** /v1/orders/import | Import Orders
[**list_orders**](OrdersApi.md#list_orders) | **GET** /v1/orders | List Orders
[**update_order**](OrdersApi.md#update_order) | **PUT** /v1/orders/{orderId} | Update Order


# **create_order**
> OrdersCreateResponseBody create_order(orders_create_request_body=orders_create_request_body)

Create Order

Creates an order object and triggers an order creation event.  📘 Upsert Mode  If you pass an id or a source_id that already exists in the order database, Voucherify will return a related order object with updated fields.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.orders_create_request_body import OrdersCreateRequestBody
from voucherify.models.orders_create_response_body import OrdersCreateResponseBody
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
    api_instance = voucherify.OrdersApi(api_client)
    orders_create_request_body = {"amount":20000,"customer":{"source_id":"sample_customer"},"status":"PAID","items":[{"quantity":1,"price":20000,"source_id":"sample product1","related_object":"product","product":{"metadata":{"key":"value"}}}]} # OrdersCreateRequestBody | Specify the order parameters. (optional)

    try:
        # Create Order
        api_response = api_instance.create_order(orders_create_request_body=orders_create_request_body)
        print("The response of OrdersApi->create_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->create_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_create_request_body** | [**OrdersCreateRequestBody**](OrdersCreateRequestBody.md)| Specify the order parameters. | [optional] 

### Return type

[**OrdersCreateResponseBody**](OrdersCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns an order object if the operation succeeded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_order_export**
> OrdersExportCreateResponseBody create_order_export(orders_export_create_request_body=orders_export_create_request_body)

Create Orders Export

Creates a downloadable CSV file containing a list of orders. The parameters listed in the payload resembles headers in the CSV file. To include a parameter to the file, add it to the parameters.fields object in the request body. The available filters are all order object attributes. Additionally, any metadata defined in the metadata schema can be exported. Passing an empty JSON will generate a file containing three default fields: id, source_id, and status. The fields array is an array of strings containing the data in the export. These fields define the headers in the CSV file. The array can be a combination of any of the following available fields:    

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.orders_export_create_request_body import OrdersExportCreateRequestBody
from voucherify.models.orders_export_create_response_body import OrdersExportCreateResponseBody
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
    api_instance = voucherify.OrdersApi(api_client)
    orders_export_create_request_body = {"parameters":{"fields":["id","source_id","status","created_at","updated_at","amount","discount_amount","items_discount_amount","total_discount_amount","total_amount","customer_id","referrer_id","metadata.payment_mean"]}} # OrdersExportCreateRequestBody | Specify which order parameters you would like to export. (optional)

    try:
        # Create Orders Export
        api_response = api_instance.create_order_export(orders_export_create_request_body=orders_export_create_request_body)
        print("The response of OrdersApi->create_order_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->create_order_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_export_create_request_body** | [**OrdersExportCreateRequestBody**](OrdersExportCreateRequestBody.md)| Specify which order parameters you would like to export. | [optional] 

### Return type

[**OrdersExportCreateResponseBody**](OrdersExportCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the &#x60;id&#x60; of the export object and &#x60;status&#x60; of the file generation process. The &#x60;id&#x60; is used in the &lt;!-- [Get Export](OpenAPI.json/paths/~1exports~1{exportId}/get) --&gt;[Get Export](ref:get-export) method to generate the url for the downloadable CSV file or in the &lt;!-- [Download Export](OpenAPI.json/paths/~1exports~1{export_Id}/get) --&gt;[Download Export](ref:download-export) method to return the contents of the CSV file. The status indicates whether the file has been scheduled for creation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order**
> OrdersGetResponseBody get_order(order_id)

Get Order

Retrieve an order.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.orders_get_response_body import OrdersGetResponseBody
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
    api_instance = voucherify.OrdersApi(api_client)
    order_id = 'order_id_example' # str | Unique Voucherify order ID or order source ID.

    try:
        # Get Order
        api_response = api_instance.get_order(order_id)
        print("The response of OrdersApi->get_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Unique Voucherify order ID or order source ID. | 

### Return type

[**OrdersGetResponseBody**](OrdersGetResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns an order object if a valid identifier was provided.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_orders**
> OrdersImportCreateResponseBody import_orders(orders_import_create_request_body_item=orders_import_create_request_body_item)

Import Orders

  🚧 Historical orders  This endpoint should only be used to import historical orders into Voucherify. For on-going synchronization, the create order and update order endpoints should be used. This is critical because this endpoint does not store events or launch distributions. # Limitations ## Import volume There can be only a single on-going order import per tenant per project at a given time. The user can schedule more imports but those extra imports will be scheduled to run in sequence one by one.   ## Maximum count of orders in single import There is a 2000 limit but we might decide to change it to a lower / higher value at any given time depending if we find this value is too high or too low with time. # Notifications There are no notifications on the Dashboard because this import is launched via the API. # Triggered actions    If you import orders with customers, then a logic will be scheduled responsible for placing these customers into segments and refreshing the segments summary. Consequently, this update will trigger  - **customers entering into segments**  - **distributions** based on any rules tied to customer entering segment(s) - **earning rules** based on the customer entering segment(s) # What is not triggered 1. No webhooks are triggered during the import of orders - for both orders and upserted products / skus.   2. Distributions based on Order Update, Order Paid, Order Created and Order Cancelled. In other words if you have a distribution based on Order Paid and you import an order with a PAID status, the distribution is not going to be triggered.     3. No events are created during the import of orders - for both orders and upserted products / skus. In other words you wont see any events in the Activity tab in the Dashboard such as Order created or Order paid. If you are additionally upserting products / skus, then you wont see the Product created events listed, etc.    4. Earning rules based on Order Paid wont be triggered. This API request starts a process that affects Voucherify data in bulk.  In case of small jobs (like bulk update) the request is put into a queue and processed once every other bulk request placed in the queue prior to this request is finished. However, when the job takes a longer time (like vouchers generation) then it is processed in small portions in a round-robin fashion. When there is a list of vouchers generation scheduled, then they will all have the IN_PROGRESS status shortly. This way, small jobs added just after scheduling big jobs of the same type will be processed in a short time window.  The result will return the async ID. You can verify the status of your request via this API request.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.orders_import_create_request_body_item import OrdersImportCreateRequestBodyItem
from voucherify.models.orders_import_create_response_body import OrdersImportCreateResponseBody
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
    api_instance = voucherify.OrdersApi(api_client)
    orders_import_create_request_body_item = [{"source_id":"orderImport14","status":"PAID","metadata":{"location_id":["L1","L2"],"payment_mean":["paypal","credit-card"]},"customer":{"source_id":"bob2.smith@email.com","name":"Bob Smith","description":"A nice customer","email":"bob.smith@email.com","phone":"+1 933 222 3333","address":{"city":"New York","country":"United States","line_1":"123 Main St.","line_2":"APT 3 BLG 4","postal_code":"10001","state":"NY"},"metadata":{"lang":"en","test":true},"birthdate":"2022-01-01"},"referrer":{"source_id":"jane.smith@email.com","name":"Jane Smith","description":"A really nice customer","email":"jane.smith@email.com","phone":"+1 933 222 3334","address":{"city":"New York","country":"United States","line_1":"123 Main St.","line_2":"APT 3 BLG 4","postal_code":"10001","state":"NY"},"metadata":{"lang":"en","test":false},"birthday":"2022-03-03"},"items":[{"source_id":"prod_1","related_object":"product","quantity":2,"product":{"name":"Apple iPhone 12","price":70000,"metadata":{"color":["silver"],"vendor":"mall"},"override":true}},{"source_id":"ComicBook_1","related_object":"sku","quantity":1,"product":{"source_id":"Books","name":"Comic Books1","price":1600,"metadata":{"color":["silver"],"vendor":"Bookstore1"},"override":true},"sku":{"sku":"Comics1","source_id":"ComicBook_1","price":1600,"metadata":{"color":["golden"],"vendor":"islands"},"override":true}}]},{"source_id":"orderImport15","status":"PAID","metadata":{"location_id":["L3"],"payment_mean":["wire-transfer"]},"customer":{"source_id":"bob2.smith@email.com"},"referrer":{"source_id":"jane.smith@email.com"},"items":[{"source_id":"ComicBook_1","quantity":4,"related_object":"sku","sku":{"source_id":"ComicBook_1"}},{"source_id":"vase_1","quantity":1,"related_object":"product","product":{"source_id":"vase_1"}}]},{"source_id":"orderImport16","status":"FULFILLED","metadata":{"location_id":["L3"],"payment_mean":["wire-transfer"]},"customer":{"id":"cust_LMY4ZylSdUYB1J4tzqNcl5VV"},"referrer":{"id":"cust_Vzck5i8U3OhcEUFY6MKhN9Rv"},"items":[{"product_id":"prod_0b72b0bd64d198e3ae","quantity":2},{"sku_id":"sku_0b1621b319d248b79f","quantity":2}]},{"source_id":"orderImport17","status":"CANCELED","amount":7000,"metadata":{"location_id":["L3"],"payment_mean":["wire-transfer"]}},{"source_id":"orderImport18","status":"CREATED","metadata":{"location_id":["L3"],"payment_mean":["wire-transfer"]},"items":[{"source_id":"ComicBook_1","amount":900,"related_object":"sku"},{"source_id":"vase_1","amount":2000,"related_object":"product"}]},{"source_id":"orderImport19","status":"CREATED","metadata":{"location_id":["L3"],"payment_mean":["wire-transfer"]},"items":[{"amount":900},{"amount":2000}]},{"source_id":"orderImport20","status":"CREATED","metadata":{"location_id":["L3"],"payment_mean":["wire-transfer"]},"items":[{"price":900,"quantity":2},{"price":2000,"quantity":3}]}] # List[OrdersImportCreateRequestBodyItem] | The request body is sent in the form of an array of order objects. (optional)

    try:
        # Import Orders
        api_response = api_instance.import_orders(orders_import_create_request_body_item=orders_import_create_request_body_item)
        print("The response of OrdersApi->import_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->import_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_import_create_request_body_item** | [**List[OrdersImportCreateRequestBodyItem]**](OrdersImportCreateRequestBodyItem.md)| The request body is sent in the form of an array of order objects. | [optional] 

### Return type

[**OrdersImportCreateResponseBody**](OrdersImportCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the ID of the scheduled asynchronous action, informing you that your request has been accepted and the order(s) will be added to the repository asynchronously. To check the status and result, copy the &#x60;async_action_id&#x60; from the response and pass it using &lt;!-- [Get Async Action](OpenAPI.json/paths/~1async-actions~1{asyncActionId}/get) --&gt;[Get Async Action](ref:get-async-action) endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_orders**
> OrdersListResponseBody list_orders(limit=limit, page=page, order=order)

List Orders

Returns a list of orders. 

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.orders_list_response_body import OrdersListResponseBody
from voucherify.models.parameter_order_list_orders import ParameterOrderListOrders
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
    api_instance = voucherify.OrdersApi(api_client)
    limit = 56 # int | Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. (optional)
    page = 56 # int | Which page of results to return. The lowest value is 1. (optional)
    order = voucherify.ParameterOrderListOrders() # ParameterOrderListOrders | This is a property that controls the sorting direction of the results. Sort the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. (optional)

    try:
        # List Orders
        api_response = api_instance.list_orders(limit=limit, page=page, order=order)
        print("The response of OrdersApi->list_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->list_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. | [optional] 
 **page** | **int**| Which page of results to return. The lowest value is 1. | [optional] 
 **order** | [**ParameterOrderListOrders**](.md)| This is a property that controls the sorting direction of the results. Sort the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. | [optional] 

### Return type

[**OrdersListResponseBody**](OrdersListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a dictionary with order objects. The orders are returned sorted by creation date by default, with the most recent orders appearing last, unless you specify another sequence using the order query parameter. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_order**
> OrdersUpdateResponseBody update_order(order_id, orders_update_request_body=orders_update_request_body)

Update Order

Updates the specified order by setting the values of the parameters passed in the request body. Any parameters not provided will be left unchanged.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.orders_update_request_body import OrdersUpdateRequestBody
from voucherify.models.orders_update_response_body import OrdersUpdateResponseBody
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
    api_instance = voucherify.OrdersApi(api_client)
    order_id = 'order_id_example' # str | Unique Voucherify order ID or order source ID.
    orders_update_request_body = {"status":"CANCELED"} # OrdersUpdateRequestBody | Specify the parameters of the order that are to be updated. (optional)

    try:
        # Update Order
        api_response = api_instance.update_order(order_id, orders_update_request_body=orders_update_request_body)
        print("The response of OrdersApi->update_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->update_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Unique Voucherify order ID or order source ID. | 
 **orders_update_request_body** | [**OrdersUpdateRequestBody**](OrdersUpdateRequestBody.md)| Specify the parameters of the order that are to be updated. | [optional] 

### Return type

[**OrdersUpdateResponseBody**](OrdersUpdateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the order object if the update succeeded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

