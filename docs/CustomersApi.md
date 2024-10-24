# voucherify.CustomersApi

All URIs are relative to *https://api.voucherify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_customer**](CustomersApi.md#create_customer) | **POST** /v1/customers | Create Customer
[**customer_permanently_deletion**](CustomersApi.md#customer_permanently_deletion) | **POST** /v1/customers/{customerId}/permanent-deletion | Delete Customer Permanently
[**delete_customer**](CustomersApi.md#delete_customer) | **DELETE** /v1/customers/{customerId} | Delete Customer
[**get_customer**](CustomersApi.md#get_customer) | **GET** /v1/customers/{customerId} | Get Customer
[**import_customers_using_csv**](CustomersApi.md#import_customers_using_csv) | **POST** /v1/customers/importCSV | Import and Update Customers using CSV
[**list_customer_activity**](CustomersApi.md#list_customer_activity) | **GET** /v1/customers/{customerId}/activity | List Customer Activity
[**list_customer_redeemables**](CustomersApi.md#list_customer_redeemables) | **GET** /v1/customers/{customerId}/redeemables | List Customer&#39;s Redeemables
[**list_customer_segments**](CustomersApi.md#list_customer_segments) | **GET** /v1/customers/{customerId}/segments | List Customer&#39;s Segments
[**list_customers**](CustomersApi.md#list_customers) | **GET** /v1/customers | List Customers
[**update_customer**](CustomersApi.md#update_customer) | **PUT** /v1/customers/{customerId} | Update Customer
[**update_customers_in_bulk**](CustomersApi.md#update_customers_in_bulk) | **POST** /v1/customers/bulk/async | Update Customers in Bulk
[**update_customers_metadata_in_bulk**](CustomersApi.md#update_customers_metadata_in_bulk) | **POST** /v1/customers/metadata/async | Update Customers&#39; Metadata in Bulk


# **create_customer**
> CustomersCreateResponseBody create_customer(customers_create_request_body=customers_create_request_body)

Create Customer

Creates a customer object.  📘 Upsert Mode  If you pass an id or a source_id that already exists in the customer database, Voucherify will return a related customer object with updated fields.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.customers_create_request_body import CustomersCreateRequestBody
from voucherify.models.customers_create_response_body import CustomersCreateResponseBody
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
    api_instance = voucherify.CustomersApi(api_client)
    customers_create_request_body = {"source_id":"source_123","name":"Bob Smith","description":"A frequent customer","email":"bob.smith@email.com","phone":"+1 933 222 3333","address":{"city":"New York","country":"United States","line_1":"123 Main St.","line_2":"APT 3 BLG 4","postal_code":"10001","state":"NY"},"metadata":{"lang":"en","test":true},"birthdate":"2022-01-01"} # CustomersCreateRequestBody | Create a customer with specified parameters. (optional)

    try:
        # Create Customer
        api_response = api_instance.create_customer(customers_create_request_body=customers_create_request_body)
        print("The response of CustomersApi->create_customer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->create_customer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customers_create_request_body** | [**CustomersCreateRequestBody**](CustomersCreateRequestBody.md)| Create a customer with specified parameters. | [optional] 

### Return type

[**CustomersCreateResponseBody**](CustomersCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a customer object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_permanently_deletion**
> CustomersPermanentDeletionCreateResponseBody customer_permanently_deletion(customer_id)

Delete Customer Permanently

The organization user can remove consumer data permanently from the Voucherify system by using this API method. It deletes all customer data and connected resources. It makes the customer profile forgotten by Voucherify.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.customers_permanent_deletion_create_response_body import CustomersPermanentDeletionCreateResponseBody
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
    api_instance = voucherify.CustomersApi(api_client)
    customer_id = 'customer_id_example' # str | A Voucherify customers id or source_id.

    try:
        # Delete Customer Permanently
        api_response = api_instance.customer_permanently_deletion(customer_id)
        print("The response of CustomersApi->customer_permanently_deletion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->customer_permanently_deletion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A Voucherify customers id or source_id. | 

### Return type

[**CustomersPermanentDeletionCreateResponseBody**](CustomersPermanentDeletionCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a permanent deletion object and status of the deletion. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_customer**
> delete_customer(customer_id)

Delete Customer

This method deletes a customer.

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
    api_instance = voucherify.CustomersApi(api_client)
    customer_id = 'customer_id_example' # str | A Voucherify customers id or source_id.

    try:
        # Delete Customer
        api_instance.delete_customer(customer_id)
    except Exception as e:
        print("Exception when calling CustomersApi->delete_customer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A Voucherify customers id or source_id. | 

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

# **get_customer**
> CustomersGetResponseBody get_customer(customer_id)

Get Customer

Retrieve customer details.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.customers_get_response_body import CustomersGetResponseBody
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
    api_instance = voucherify.CustomersApi(api_client)
    customer_id = 'customer_id_example' # str | A Voucherify customers id or source_id.

    try:
        # Get Customer
        api_response = api_instance.get_customer(customer_id)
        print("The response of CustomersApi->get_customer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->get_customer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A Voucherify customers id or source_id. | 

### Return type

[**CustomersGetResponseBody**](CustomersGetResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a customer object if a valid identifier was provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_customers_using_csv**
> CustomersImportCsvCreateResponseBody import_customers_using_csv(file=file)

Import and Update Customers using CSV

This API method lets you import or update customer data. To get a proper and valid response, please send a CSV file with data separated by commas.   # Request Example # CSV File Format The CSV file has to include headers in the first line. All properties which cannot be mapped to standard customer fields will be added to the metadata object.  📘 Standard customer fields mapping  **No spaces allowed in field names**    Id, Name, Email, Phone, Birthdate, Source_id, Address_line_1, Address_line_2, Address_Postal_Code, Address_City, Address_State, Address_Country, Description, Metadata_name_1, Metadata_name_2 # Update Customers using CSV If you would like to update customers data, you can do it using the CSV file with new data. However, remember to include a source_id in your CSV file to manage the update successfully. This API request starts a process that affects Voucherify data in bulk.  In case of small jobs (like bulk update) the request is put into a queue and processed once every other bulk request placed in the queue prior to this request is finished. However, when the job takes a longer time (like vouchers generation) then it is processed in small portions in a round-robin fashion. When there is a list of vouchers generation scheduled, then they will all have the IN_PROGRESS status shortly. This way, small jobs added just after scheduling big jobs of the same type will be processed in a short time window.  The result will return the async ID. You can verify the status of your request via this API request.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.customers_import_csv_create_response_body import CustomersImportCsvCreateResponseBody
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
    api_instance = voucherify.CustomersApi(api_client)
    file = None # bytearray | File path. (optional)

    try:
        # Import and Update Customers using CSV
        api_response = api_instance.import_customers_using_csv(file=file)
        print("The response of CustomersApi->import_customers_using_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->import_customers_using_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**| File path. | [optional] 

### Return type

[**CustomersImportCsvCreateResponseBody**](CustomersImportCsvCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns ID of the scheduled async action. The response informs you that your request has been accepted and customers will be added to the repository asynchronously. To check the import status and result, copy the &#x60;async_action_id&#x60; from the response and pass it using the &lt;!-- [Get Async Action](OpenAPI.json/paths/~1async-actions~1{asyncActionId}/get) --&gt;[Get Async Action](ref:get-async-action) endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_customer_activity**
> CustomersActivityListResponseBody list_customer_activity(customer_id, limit=limit, order=order, starting_after_id=starting_after_id, start_date=start_date, end_date=end_date, campaign_id=campaign_id, campaign_type=campaign_type, category=category, type=type)

List Customer Activity

Retrieve customer activities.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.customers_activity_list_response_body import CustomersActivityListResponseBody
from voucherify.models.parameter_activity_category import ParameterActivityCategory
from voucherify.models.parameter_campaign_type import ParameterCampaignType
from voucherify.models.parameter_order_created_at import ParameterOrderCreatedAt
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
    api_instance = voucherify.CustomersApi(api_client)
    customer_id = 'customer_id_example' # str | A Voucherify customers id or source ID of the customer who performed the activities.
    limit = 56 # int | Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. (optional)
    order = voucherify.ParameterOrderCreatedAt() # ParameterOrderCreatedAt | Apply this filter to order the events according the date and time when it was created.  (optional)
    starting_after_id = 'starting_after_id_example' # str | A cursor for pagination. It retrieves the events starting after an event with the given ID. (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp representing the date and time which results must begin on. Represented in ISO 8601 format. (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp representing the date and time which results must end on. Represented in ISO 8601 format. (optional)
    campaign_id = 'campaign_id_example' # str | Requests only events related to specific campaign identified by its ID. (optional)
    campaign_type = voucherify.ParameterCampaignType() # ParameterCampaignType | Filters related customers activity for the selected campaign types. Allowed values:  DISCOUNT_COUPONS, REFERRAL_PROGRAM, GIFT_VOUCHERS, PROMOTION, LOYALTY_PROGRAM. (optional)
    category = voucherify.ParameterActivityCategory() # ParameterActivityCategory | Filters activities for actions or effects. Allowed values:  ACTION, EFFECT. (optional)
    type = 'type_example' # str | Event name of the customer event. (optional)

    try:
        # List Customer Activity
        api_response = api_instance.list_customer_activity(customer_id, limit=limit, order=order, starting_after_id=starting_after_id, start_date=start_date, end_date=end_date, campaign_id=campaign_id, campaign_type=campaign_type, category=category, type=type)
        print("The response of CustomersApi->list_customer_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->list_customer_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A Voucherify customers id or source ID of the customer who performed the activities. | 
 **limit** | **int**| Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. | [optional] 
 **order** | [**ParameterOrderCreatedAt**](.md)| Apply this filter to order the events according the date and time when it was created.  | [optional] 
 **starting_after_id** | **str**| A cursor for pagination. It retrieves the events starting after an event with the given ID. | [optional] 
 **start_date** | **datetime**| Timestamp representing the date and time which results must begin on. Represented in ISO 8601 format. | [optional] 
 **end_date** | **datetime**| Timestamp representing the date and time which results must end on. Represented in ISO 8601 format. | [optional] 
 **campaign_id** | **str**| Requests only events related to specific campaign identified by its ID. | [optional] 
 **campaign_type** | [**ParameterCampaignType**](.md)| Filters related customers activity for the selected campaign types. Allowed values:  DISCOUNT_COUPONS, REFERRAL_PROGRAM, GIFT_VOUCHERS, PROMOTION, LOYALTY_PROGRAM. | [optional] 
 **category** | [**ParameterActivityCategory**](.md)| Filters activities for actions or effects. Allowed values:  ACTION, EFFECT. | [optional] 
 **type** | **str**| Event name of the customer event. | [optional] 

### Return type

[**CustomersActivityListResponseBody**](CustomersActivityListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a dictionary with customer activities. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_customer_redeemables**
> CustomersRedeemablesListResponseBody list_customer_redeemables(customer_id, limit=limit, order=order, starting_after_id=starting_after_id, filters=filters)

List Customer's Redeemables

Retrieves all the redeemables that have been assigned to the customer. To use this endpoint, you must have the following permissions: - Read Customers (customers.details.read)

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.customers_redeemables_list_response_body import CustomersRedeemablesListResponseBody
from voucherify.models.parameter_filters_list_customer_redeemables import ParameterFiltersListCustomerRedeemables
from voucherify.models.parameter_order_list_redeemables import ParameterOrderListRedeemables
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
    api_instance = voucherify.CustomersApi(api_client)
    customer_id = 'customer_id_example' # str | Unique identifier of a customer represented by an internal customer ID or customer source ID.
    limit = 56 # int | Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. (optional)
    order = voucherify.ParameterOrderListRedeemables() # ParameterOrderListRedeemables | Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. (optional)
    starting_after_id = 'starting_after_id_example' # str | A cursor for pagination. It retrieves the events starting after an event with the given ID. (optional)
    filters = voucherify.ParameterFiltersListCustomerRedeemables() # ParameterFiltersListCustomerRedeemables | Filters for listing customer redeemables. (optional)

    try:
        # List Customer's Redeemables
        api_response = api_instance.list_customer_redeemables(customer_id, limit=limit, order=order, starting_after_id=starting_after_id, filters=filters)
        print("The response of CustomersApi->list_customer_redeemables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->list_customer_redeemables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Unique identifier of a customer represented by an internal customer ID or customer source ID. | 
 **limit** | **int**| Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. | [optional] 
 **order** | [**ParameterOrderListRedeemables**](.md)| Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. | [optional] 
 **starting_after_id** | **str**| A cursor for pagination. It retrieves the events starting after an event with the given ID. | [optional] 
 **filters** | [**ParameterFiltersListCustomerRedeemables**](.md)| Filters for listing customer redeemables. | [optional] 

### Return type

[**CustomersRedeemablesListResponseBody**](CustomersRedeemablesListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | The method returns redeemable(s) to which the given customer is assigned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_customer_segments**
> CustomersSegmentsListResponseBody list_customer_segments(customer_id)

List Customer's Segments

Returns the list of segments IDs to which the customer belongs to.   If you pass a customerId which is not stored and recognized by Voucherify as an existing customer in the system, the response will generate a list of segments that the customer would potentialy qualify for if they were to become a customer tracked in the system.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.customers_segments_list_response_body import CustomersSegmentsListResponseBody
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
    api_instance = voucherify.CustomersApi(api_client)
    customer_id = 'customer_id_example' # str | Unique identifier of a customer represented by an internal customer ID or customer source ID.

    try:
        # List Customer's Segments
        api_response = api_instance.list_customer_segments(customer_id)
        print("The response of CustomersApi->list_customer_segments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->list_customer_segments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Unique identifier of a customer represented by an internal customer ID or customer source ID. | 

### Return type

[**CustomersSegmentsListResponseBody**](CustomersSegmentsListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | The method returns segment(s) to which the given customer belongs to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_customers**
> CustomersListResponseBody list_customers(limit=limit, page=page, email=email, city=city, name=name, segment_id=segment_id, created_at_before=created_at_before, created_at_after=created_at_after, updated_at_before=updated_at_before, updated_at_after=updated_at_after, order=order, starting_after=starting_after)

List Customers

Returns a list of customers.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.customers_list_response_body import CustomersListResponseBody
from voucherify.models.parameter_order_list_customers import ParameterOrderListCustomers
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
    api_instance = voucherify.CustomersApi(api_client)
    limit = 56 # int | Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. (optional)
    page = 56 # int | Which page of results to return. The lowest value is 1. (optional)
    email = 'email_example' # str | Limit the customers to the ones that have this specific email address. (optional)
    city = 'city_example' # str | Limit the customers to the ones that are located in the specified city. (optional)
    name = 'name_example' # str | Filter customers by the name property. (optional)
    segment_id = 'segment_id_example' # str | Filter customers by the segment id. (optional)
    created_at_before = '2013-10-20T19:20:30+01:00' # datetime | Filter customers by date customer was created. (optional)
    created_at_after = '2013-10-20T19:20:30+01:00' # datetime | Filter customers by date customer was created. (optional)
    updated_at_before = '2013-10-20T19:20:30+01:00' # datetime | Filter customers by date customer was updated last time. (optional)
    updated_at_after = '2013-10-20T19:20:30+01:00' # datetime | Filter customers by date customer was updated last time. (optional)
    order = voucherify.ParameterOrderListCustomers() # ParameterOrderListCustomers | This is a property that controls the sorting direction of the results. Sort the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. (optional)
    starting_after = '2013-10-20T19:20:30+01:00' # datetime | A cursor for pagination. This is a date-time value that defines your place in the list based on created_at property from the customer object. For instance, if you make a list request and receive 100 objects, ending with an object created at 2020-05-24T13:43:09.024Z, your subsequent call can include starting_after 2020-05-24T13:43:09.024Z in order to fetch the next page of the list.   (optional)

    try:
        # List Customers
        api_response = api_instance.list_customers(limit=limit, page=page, email=email, city=city, name=name, segment_id=segment_id, created_at_before=created_at_before, created_at_after=created_at_after, updated_at_before=updated_at_before, updated_at_after=updated_at_after, order=order, starting_after=starting_after)
        print("The response of CustomersApi->list_customers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->list_customers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. | [optional] 
 **page** | **int**| Which page of results to return. The lowest value is 1. | [optional] 
 **email** | **str**| Limit the customers to the ones that have this specific email address. | [optional] 
 **city** | **str**| Limit the customers to the ones that are located in the specified city. | [optional] 
 **name** | **str**| Filter customers by the name property. | [optional] 
 **segment_id** | **str**| Filter customers by the segment id. | [optional] 
 **created_at_before** | **datetime**| Filter customers by date customer was created. | [optional] 
 **created_at_after** | **datetime**| Filter customers by date customer was created. | [optional] 
 **updated_at_before** | **datetime**| Filter customers by date customer was updated last time. | [optional] 
 **updated_at_after** | **datetime**| Filter customers by date customer was updated last time. | [optional] 
 **order** | [**ParameterOrderListCustomers**](.md)| This is a property that controls the sorting direction of the results. Sort the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. | [optional] 
 **starting_after** | **datetime**| A cursor for pagination. This is a date-time value that defines your place in the list based on created_at property from the customer object. For instance, if you make a list request and receive 100 objects, ending with an object created at 2020-05-24T13:43:09.024Z, your subsequent call can include starting_after 2020-05-24T13:43:09.024Z in order to fetch the next page of the list.   | [optional] 

### Return type

[**CustomersListResponseBody**](CustomersListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a dictionary with customer objects. The customers are returned sorted by creation date, with the most recent customers appearing first. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_customer**
> CustomersUpdateResponseBody update_customer(customer_id, customers_update_request_body=customers_update_request_body)

Update Customer

Updates the specified customer by setting the values of the parameters passed in the request body. Any parameters not provided in the payload will be left unchanged.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.customers_update_request_body import CustomersUpdateRequestBody
from voucherify.models.customers_update_response_body import CustomersUpdateResponseBody
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
    api_instance = voucherify.CustomersApi(api_client)
    customer_id = 'customer_id_example' # str | A Voucherify customers id or source_id.
    customers_update_request_body = {"name":"Alice McDonald","email":"alice.mdconald@email.com","description":"Updating customer data","phone":"+1 (132) 222-2222","address":{"city":"New York","country":"United States","line_1":"123 Main St.","line_2":"APT 3 BLG 4","postal_code":"10001","state":"NY"},"metadata":{"lang":"en","test":true},"birthdate":"2022-01-01","birthday":"2022-01-02"} # CustomersUpdateRequestBody | Specify the parameters to be updated. (optional)

    try:
        # Update Customer
        api_response = api_instance.update_customer(customer_id, customers_update_request_body=customers_update_request_body)
        print("The response of CustomersApi->update_customer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->update_customer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A Voucherify customers id or source_id. | 
 **customers_update_request_body** | [**CustomersUpdateRequestBody**](CustomersUpdateRequestBody.md)| Specify the parameters to be updated. | [optional] 

### Return type

[**CustomersUpdateResponseBody**](CustomersUpdateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a customer object if updates were successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_customers_in_bulk**
> CustomersUpdateInBulkResponseBody update_customers_in_bulk(customers_update_in_bulk_request_body=customers_update_in_bulk_request_body)

Update Customers in Bulk

Updates customers in one asynchronous operation. The request can include up to **10 MB** of data. The response returns a unique asynchronous action ID. Use this ID in the query paramater of the GET Async Action endpoint to check, e.g.: - The status of your request (in queue, in progress, done, or failed) - Resources that failed to be updated - The report file with details about the update If a customer object is not found, it is **upserted**. This is shown in the report file in the **GET** Async Action endpoint. The upserted resources have value false in the found column and true in the updated column. This API request starts a process that affects Voucherify data in bulk. In the case of small jobs (like bulk update), the request is put into a queue and processed when every other bulk request placed in the queue prior to this request is finished.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.customers_update_in_bulk_request_body import CustomersUpdateInBulkRequestBody
from voucherify.models.customers_update_in_bulk_response_body import CustomersUpdateInBulkResponseBody
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
    api_instance = voucherify.CustomersApi(api_client)
    customers_update_in_bulk_request_body = [{"source_id":"John.Smith@email.com","name":"John Smith","email":"john.smith@email.com","description":"Updating customer data","phone":"+1 (132) 222-2222","address":{"city":"New York","country":"United States","line_1":"123 Main St.","line_2":"APT 3 BLG 4","postal_code":"10001","state":"NY"},"metadata":{"lang":"en","test":true},"birthday":"2022-04-04"},{"source_id":"Jane.Smith@email.com","name":"Jane Smith","email":"Jane.Smith@email.com","description":"Updating customer data","phone":"+1 (132) 222-2222","address":{"city":"New York","country":"United States","line_1":"123 Main St.","line_2":"APT 3 BLG 4","postal_code":"10001","state":"NY"},"metadata":{"lang":"en","test":true},"birthday":"2022-03-03"},{"source_id":"Sally.Smith@email.com","name":"Sally Smith","email":"Sally.Smith@email.com","description":"Updating customer data","phone":"+1 (132) 222-2222","address":{"city":"New York","country":"United States","line_1":"123 Main St.","line_2":"APT 3 BLG 4","postal_code":"10001","state":"NY"},"metadata":{"lang":"en","test":true},"birthdate":"2022-02-02"}] # List[CustomersUpdateInBulkRequestBody] | List the customer fields to be updated in each customer object. (optional)

    try:
        # Update Customers in Bulk
        api_response = api_instance.update_customers_in_bulk(customers_update_in_bulk_request_body=customers_update_in_bulk_request_body)
        print("The response of CustomersApi->update_customers_in_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->update_customers_in_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customers_update_in_bulk_request_body** | [**List[CustomersUpdateInBulkRequestBody]**](CustomersUpdateInBulkRequestBody.md)| List the customer fields to be updated in each customer object. | [optional] 

### Return type

[**CustomersUpdateInBulkResponseBody**](CustomersUpdateInBulkResponseBody.md)

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

# **update_customers_metadata_in_bulk**
> CustomersMetadataUpdateInBulkResponseBody update_customers_metadata_in_bulk(customers_metadata_update_in_bulk_request_body=customers_metadata_update_in_bulk_request_body)

Update Customers' Metadata in Bulk

Updates metadata parameters for a list of customers. Every resource in the list will receive the metadata defined in the request. The request can include up to **10 MB** of data. The response returns a unique asynchronous action ID. Use this ID in the query paramater of the GET Async Action endpoint to check, e.g.: - The status of your request (in queue, in progress, done, or failed) - Resources that failed to be updated - The report file with details about the update If a product object is not found, it is **upserted**. This is shown in the report file in the **GET** Async Action endpoint. The upserted resources have value false in the found column and true in the updated column. This API request starts a process that affects Voucherify data in bulk. In the case of small jobs (like bulk update), the request is put into a queue and processed when every other bulk request placed in the queue prior to this request is finished.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.customers_metadata_update_in_bulk_request_body import CustomersMetadataUpdateInBulkRequestBody
from voucherify.models.customers_metadata_update_in_bulk_response_body import CustomersMetadataUpdateInBulkResponseBody
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
    api_instance = voucherify.CustomersApi(api_client)
    customers_metadata_update_in_bulk_request_body = {"source_ids":["source_123","source_456"],"metadata":{"lang":"en","test":false}} # CustomersMetadataUpdateInBulkRequestBody | List the source_ids of the customers you would like to update with the metadata key/value pairs. (optional)

    try:
        # Update Customers' Metadata in Bulk
        api_response = api_instance.update_customers_metadata_in_bulk(customers_metadata_update_in_bulk_request_body=customers_metadata_update_in_bulk_request_body)
        print("The response of CustomersApi->update_customers_metadata_in_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->update_customers_metadata_in_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customers_metadata_update_in_bulk_request_body** | [**CustomersMetadataUpdateInBulkRequestBody**](CustomersMetadataUpdateInBulkRequestBody.md)| List the source_ids of the customers you would like to update with the metadata key/value pairs. | [optional] 

### Return type

[**CustomersMetadataUpdateInBulkResponseBody**](CustomersMetadataUpdateInBulkResponseBody.md)

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

