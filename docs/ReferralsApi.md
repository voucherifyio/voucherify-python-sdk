# voucherify.ReferralsApi

All URIs are relative to *https://api.voucherify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**referrals_add_holders**](ReferralsApi.md#referrals_add_holders) | **POST** /v1/referrals/members/{memberId}/holders | Add Referral Code Holders
[**referrals_add_holders1**](ReferralsApi.md#referrals_add_holders1) | **POST** /v1/referrals/{campaignId}/members/{memberId}/holders | Add Referral Code Holders
[**referrals_code_holders**](ReferralsApi.md#referrals_code_holders) | **GET** /v1/referrals/{campaignId}/members/{memberId}/holders | List Referral Code Holders
[**referrals_code_holders1**](ReferralsApi.md#referrals_code_holders1) | **GET** /v1/referrals/members/{memberId}/holders | List Referral Code Holders
[**referrals_remove_holder**](ReferralsApi.md#referrals_remove_holder) | **DELETE** /v1/referrals/members/{memberId}/holders/{holderId} | Remove Referral Card Holder
[**referrals_remove_holder1**](ReferralsApi.md#referrals_remove_holder1) | **DELETE** /v1/referrals/{campaignId}/members/{memberId}/holders/{holderId} | Remove Referral Card Holder


# **referrals_add_holders**
> ReferralsMembersHoldersCreateInBulkResponseBody referrals_add_holders(member_id, referrals_members_holders_create_in_bulk_request_body=referrals_members_holders_create_in_bulk_request_body)

Add Referral Code Holders

Adds new holders to a referral code as **referees**. The data sent in the request is upserted into the customer data. If the request returns an error even for one customer, you have to resend the whole request. Customer data is upserted if the data for all customers is correct. To use this endpoint, you must have the following permissions: - Create and modify Customers and Segments (customers.modify) - Publish Voucher (vouchers.publish)  👍 To add a holder as a referer, use the Create Publication endpoint.  📘 Alternative endpoint This endpoint is an alternative to the Add Referral Code Holders endpoint. The URL was re-designed to retrieve the referral member holders without providing the campaignId as a path paremeter.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.referrals_members_holders_create_in_bulk_request_body import ReferralsMembersHoldersCreateInBulkRequestBody
from voucherify.models.referrals_members_holders_create_in_bulk_response_body import ReferralsMembersHoldersCreateInBulkResponseBody
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
    api_instance = voucherify.ReferralsApi(api_client)
    member_id = 'member_id_example' # str | Unique referral code or its identifier.
    referrals_members_holders_create_in_bulk_request_body = {"holders":[{"source_id":"cst-prsn01","name":"Alex Doe","email":"alex-doe@your.domain.com","country":"England"},{"source_id":"cst-prsn02","name":"Alex Joe","email":"alex-joe@your.domain.com","country":"Wales"}],"metadata":{"influencer_code":true}} # ReferralsMembersHoldersCreateInBulkRequestBody | Specify the customer data to be upserted as redeemable holders. (optional)

    try:
        # Add Referral Code Holders
        api_response = api_instance.referrals_add_holders(member_id, referrals_members_holders_create_in_bulk_request_body=referrals_members_holders_create_in_bulk_request_body)
        print("The response of ReferralsApi->referrals_add_holders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferralsApi->referrals_add_holders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**| Unique referral code or its identifier. | 
 **referrals_members_holders_create_in_bulk_request_body** | [**ReferralsMembersHoldersCreateInBulkRequestBody**](ReferralsMembersHoldersCreateInBulkRequestBody.md)| Specify the customer data to be upserted as redeemable holders. | [optional] 

### Return type

[**ReferralsMembersHoldersCreateInBulkResponseBody**](ReferralsMembersHoldersCreateInBulkResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a list of redeemable holder objects. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **referrals_add_holders1**
> ReferralsMembersHoldersCreateInBulkResponseBody referrals_add_holders1(campaign_id, member_id, referrals_members_holders_create_in_bulk_request_body=referrals_members_holders_create_in_bulk_request_body)

Add Referral Code Holders

Adds new holders to a referral code as **referees**. The data sent in the request is upserted into the customer data. If the request returns an error even for one customer, you have to resend the whole request. Customer data is upserted if the data for all customers is correct. To use this endpoint, you must have the following permissions: - Create and modify Customers and Segments (customers.modify) - Publish Voucher (vouchers.publish)  👍 To add a holder as a referer, use the Create Publication endpoint.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.referrals_members_holders_create_in_bulk_request_body import ReferralsMembersHoldersCreateInBulkRequestBody
from voucherify.models.referrals_members_holders_create_in_bulk_response_body import ReferralsMembersHoldersCreateInBulkResponseBody
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
    api_instance = voucherify.ReferralsApi(api_client)
    campaign_id = 'campaign_id_example' # str | Unique identifier of a referral program campaign.
    member_id = 'member_id_example' # str | Unique referral code or its identifier.
    referrals_members_holders_create_in_bulk_request_body = {"holders":[{"source_id":"cst-prsn01","name":"Alex Doe","email":"alex-doe@your.domain.com","country":"England"},{"source_id":"cst-prsn02","name":"Alex Joe","email":"alex-joe@your.domain.com","country":"Wales"}],"metadata":{"influencer_code":true}} # ReferralsMembersHoldersCreateInBulkRequestBody | Specify the customer data to be upserted as redeemable holders. (optional)

    try:
        # Add Referral Code Holders
        api_response = api_instance.referrals_add_holders1(campaign_id, member_id, referrals_members_holders_create_in_bulk_request_body=referrals_members_holders_create_in_bulk_request_body)
        print("The response of ReferralsApi->referrals_add_holders1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferralsApi->referrals_add_holders1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Unique identifier of a referral program campaign. | 
 **member_id** | **str**| Unique referral code or its identifier. | 
 **referrals_members_holders_create_in_bulk_request_body** | [**ReferralsMembersHoldersCreateInBulkRequestBody**](ReferralsMembersHoldersCreateInBulkRequestBody.md)| Specify the customer data to be upserted as redeemable holders. | [optional] 

### Return type

[**ReferralsMembersHoldersCreateInBulkResponseBody**](ReferralsMembersHoldersCreateInBulkResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a list of redeemable holder objects. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **referrals_code_holders**
> ReferralsMembersHoldersListResponseBody referrals_code_holders(campaign_id, member_id, limit=limit, order=order, starting_after_id=starting_after_id, filters=filters)

List Referral Code Holders

Retrieves all the redeemables that have been assigned to the customer. To use this endpoint, you must have the following permissions: - Read Customers (customers.details.read)

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.parameter_filters_list_referrals_redeemable_holders import ParameterFiltersListReferralsRedeemableHolders
from voucherify.models.parameter_order_list_redeemables import ParameterOrderListRedeemables
from voucherify.models.referrals_members_holders_list_response_body import ReferralsMembersHoldersListResponseBody
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
    api_instance = voucherify.ReferralsApi(api_client)
    campaign_id = 'campaign_id_example' # str | Unique identifier of a referral program campaign.
    member_id = 'member_id_example' # str | Unique referral code or its identifier.
    limit = 56 # int | Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. (optional)
    order = voucherify.ParameterOrderListRedeemables() # ParameterOrderListRedeemables | Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. (optional)
    starting_after_id = 'starting_after_id_example' # str | A cursor for pagination. It retrieves the events starting after an event with the given ID. (optional)
    filters = voucherify.ParameterFiltersListReferralsRedeemableHolders() # ParameterFiltersListReferralsRedeemableHolders | Filters for listing customer redeemables. (optional)

    try:
        # List Referral Code Holders
        api_response = api_instance.referrals_code_holders(campaign_id, member_id, limit=limit, order=order, starting_after_id=starting_after_id, filters=filters)
        print("The response of ReferralsApi->referrals_code_holders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferralsApi->referrals_code_holders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Unique identifier of a referral program campaign. | 
 **member_id** | **str**| Unique referral code or its identifier. | 
 **limit** | **int**| Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. | [optional] 
 **order** | [**ParameterOrderListRedeemables**](.md)| Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. | [optional] 
 **starting_after_id** | **str**| A cursor for pagination. It retrieves the events starting after an event with the given ID. | [optional] 
 **filters** | [**ParameterFiltersListReferralsRedeemableHolders**](.md)| Filters for listing customer redeemables. | [optional] 

### Return type

[**ReferralsMembersHoldersListResponseBody**](ReferralsMembersHoldersListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the holders of the redeemable that is assigned to the referral campaign. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **referrals_code_holders1**
> ReferralsMembersHoldersListResponseBody referrals_code_holders1(member_id, limit=limit, order=order, starting_after_id=starting_after_id, filters=filters)

List Referral Code Holders

Retrieves the holders of the referral code from a referral campaign. To use this endpoint, you must have the following permissions: - Read Customers (customers.details.read)  📘 Alternative endpoint This endpoint is an alternative to the List Member Holders endpoint. The URL was re-designed to retrieve the referral member holders without providing the campaignId as a path paremeter.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.parameter_filters_list_referrals_redeemable_holders import ParameterFiltersListReferralsRedeemableHolders
from voucherify.models.parameter_order_list_redeemables import ParameterOrderListRedeemables
from voucherify.models.referrals_members_holders_list_response_body import ReferralsMembersHoldersListResponseBody
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
    api_instance = voucherify.ReferralsApi(api_client)
    member_id = 'member_id_example' # str | Unique referral code or its identifier.
    limit = 56 # int | Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. (optional)
    order = voucherify.ParameterOrderListRedeemables() # ParameterOrderListRedeemables | Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. (optional)
    starting_after_id = 'starting_after_id_example' # str | A cursor for pagination. It retrieves the events starting after an event with the given ID. (optional)
    filters = voucherify.ParameterFiltersListReferralsRedeemableHolders() # ParameterFiltersListReferralsRedeemableHolders | Filters for listing customer redeemables. (optional)

    try:
        # List Referral Code Holders
        api_response = api_instance.referrals_code_holders1(member_id, limit=limit, order=order, starting_after_id=starting_after_id, filters=filters)
        print("The response of ReferralsApi->referrals_code_holders1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferralsApi->referrals_code_holders1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**| Unique referral code or its identifier. | 
 **limit** | **int**| Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. | [optional] 
 **order** | [**ParameterOrderListRedeemables**](.md)| Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. | [optional] 
 **starting_after_id** | **str**| A cursor for pagination. It retrieves the events starting after an event with the given ID. | [optional] 
 **filters** | [**ParameterFiltersListReferralsRedeemableHolders**](.md)| Filters for listing customer redeemables. | [optional] 

### Return type

[**ReferralsMembersHoldersListResponseBody**](ReferralsMembersHoldersListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the holders of the redeemable that is assigned to the referral campaign. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **referrals_remove_holder**
> referrals_remove_holder(member_id, holder_id)

Remove Referral Card Holder

Removes the holder from a referral card. You can remove a referee only. To use this endpoint, you must have the following permissions: - Create and modify Customers and Segments (customers.modify) - Publish Voucher (vouchers.publish)  📘 Alternative endpoint This endpoint is an alternative to the Remove Referral Card Holder endpoint. The URL was re-designed to retrieve the referral member holders without providing the campaignId as a path paremeter.

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
    api_instance = voucherify.ReferralsApi(api_client)
    member_id = 'member_id_example' # str | Unique referral code or its identifier.
    holder_id = 'holder_id_example' # str | Unique identifier of a redeemable holder.

    try:
        # Remove Referral Card Holder
        api_instance.referrals_remove_holder(member_id, holder_id)
    except Exception as e:
        print("Exception when calling ReferralsApi->referrals_remove_holder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**| Unique referral code or its identifier. | 
 **holder_id** | **str**| Unique identifier of a redeemable holder. | 

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
**2XX** | Returns no content if removal is successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **referrals_remove_holder1**
> referrals_remove_holder1(campaign_id, member_id, holder_id)

Remove Referral Card Holder

Removes the holder from a referral card. You can remove a referee only. To use this endpoint, you must have the following permissions: - Create and modify Customers and Segments (customers.modify) - Publish Voucher (vouchers.publish)

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
    api_instance = voucherify.ReferralsApi(api_client)
    campaign_id = 'campaign_id_example' # str | Unique identifier of a referral program campaign.
    member_id = 'member_id_example' # str | Unique referral code or its identifier.
    holder_id = 'holder_id_example' # str | Unique identifier of a redeemable holder.

    try:
        # Remove Referral Card Holder
        api_instance.referrals_remove_holder1(campaign_id, member_id, holder_id)
    except Exception as e:
        print("Exception when calling ReferralsApi->referrals_remove_holder1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Unique identifier of a referral program campaign. | 
 **member_id** | **str**| Unique referral code or its identifier. | 
 **holder_id** | **str**| Unique identifier of a redeemable holder. | 

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
**2XX** | Returns no content if removal is successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

