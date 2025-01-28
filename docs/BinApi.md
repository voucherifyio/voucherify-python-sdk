# voucherify.BinApi

All URIs are relative to *https://api.voucherify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_bin_entry**](BinApi.md#delete_bin_entry) | **DELETE** /v1/trash-bin/{binEntryId} | Delete Bin Entry
[**list_bin_entries**](BinApi.md#list_bin_entries) | **GET** /v1/trash-bin | List Bin Entries


# **delete_bin_entry**
> delete_bin_entry(bin_entry_id)

Delete Bin Entry

Deletes permanently a bin entry with a given ID.The following resources can be moved to the bin and permanently deleted: - campaigns - vouchers - products - SKUs To use this endpoint and delete a given resource type, you must have the following permissions: - vouchers.delete to delete a voucher, - campaigns.delete to delete a campaign, - products.delete to delete a product or SKU.

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
    api_instance = voucherify.BinApi(api_client)
    bin_entry_id = 'bin_entry_id_example' # str | Provide the unique identifier of the bin entry.

    try:
        # Delete Bin Entry
        api_instance.delete_bin_entry(bin_entry_id)
    except Exception as e:
        print("Exception when calling BinApi->delete_bin_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bin_entry_id** | **str**| Provide the unique identifier of the bin entry. | 

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

# **list_bin_entries**
> TrashBinListResponseBody list_bin_entries(limit=limit, order=order, starting_after_id=starting_after_id, filters=filters)

List Bin Entries

Retrieves a list of resources moved to the bin. The following resources can be moved to the bin: - campaigns - vouchers - products - SKUs To use this endpoint, you must have the following permissions: - vouchers.read - campaigns.read - products.read

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.parameter_filters_list_bin import ParameterFiltersListBin
from voucherify.models.parameter_order_list_bin import ParameterOrderListBin
from voucherify.models.trash_bin_list_response_body import TrashBinListResponseBody
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
    api_instance = voucherify.BinApi(api_client)
    limit = 56 # int | Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. (optional)
    order = voucherify.ParameterOrderListBin() # ParameterOrderListBin | Orders the bin entries according to the bin entry ID. The dash - preceding a sorting option means sorting in a descending order. (optional)
    starting_after_id = 'starting_after_id_example' # str | A cursor for pagination. It retrieves the results starting after a result with the given ID. (optional)
    filters = voucherify.ParameterFiltersListBin() # ParameterFiltersListBin | Filters for listing bin entries. (optional)

    try:
        # List Bin Entries
        api_response = api_instance.list_bin_entries(limit=limit, order=order, starting_after_id=starting_after_id, filters=filters)
        print("The response of BinApi->list_bin_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinApi->list_bin_entries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. | [optional] 
 **order** | [**ParameterOrderListBin**](.md)| Orders the bin entries according to the bin entry ID. The dash - preceding a sorting option means sorting in a descending order. | [optional] 
 **starting_after_id** | **str**| A cursor for pagination. It retrieves the results starting after a result with the given ID. | [optional] 
 **filters** | [**ParameterFiltersListBin**](.md)| Filters for listing bin entries. | [optional] 

### Return type

[**TrashBinListResponseBody**](TrashBinListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the list of all the bin entries matching the query parameters. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

