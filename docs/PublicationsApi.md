# voucherify.PublicationsApi

All URIs are relative to *https://api.voucherify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_publication**](PublicationsApi.md#create_publication) | **POST** /v1/publications | Create Publication
[**create_publication1**](PublicationsApi.md#create_publication1) | **GET** /v1/publications/create | Create Publication
[**list_publications**](PublicationsApi.md#list_publications) | **GET** /v1/publications | List Publications


# **create_publication**
> PublicationsCreateResponseBody create_publication(join_once=join_once, publications_create_request_body=publications_create_request_body)

Create Publication

This method selects vouchers that are suitable for publication, adds a publish entry and returns the publication. A voucher is suitable for publication when its active and hasnt been published yet.    🚧 Clearly define the source of the voucher  You must clearly define which source you want to publish the voucher code from. It can either be a code from a campaign or a specific voucher identified by a code.    🚧 Publish multiple vouchers  In case you want to publish multiple vouchers within a single publication, you need to specify the campaign name and number of vouchers you want to publish.    📘 Auto-update campaign  In case you want to ensure the number of publishable codes increases automatically with the number of customers, you should use an **auto-update** campaign.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.publications_create_request_body import PublicationsCreateRequestBody
from voucherify.models.publications_create_response_body import PublicationsCreateResponseBody
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
    api_instance = voucherify.PublicationsApi(api_client)
    join_once = True # bool | Through this flag, you can control if a particular person gets only one and always the same code even if the app sends multiple publication requests. It means that if you have a referral program, a referrer is assigned only to one code if an integration sends publication requests more than once for the same customer. (optional)
    publications_create_request_body = {"campaign":{"name":"campaign-name"},"customer":{"source_id":"source-id","Name":"Customer Name","email":"customer email"},"voucher":"voucher-code","metadata":{"key":"value"}} # PublicationsCreateRequestBody | Specify the publication parameters. (optional)

    try:
        # Create Publication
        api_response = api_instance.create_publication(join_once=join_once, publications_create_request_body=publications_create_request_body)
        print("The response of PublicationsApi->create_publication:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicationsApi->create_publication: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **join_once** | **bool**| Through this flag, you can control if a particular person gets only one and always the same code even if the app sends multiple publication requests. It means that if you have a referral program, a referrer is assigned only to one code if an integration sends publication requests more than once for the same customer. | [optional] 
 **publications_create_request_body** | [**PublicationsCreateRequestBody**](PublicationsCreateRequestBody.md)| Specify the publication parameters. | [optional] 

### Return type

[**PublicationsCreateResponseBody**](PublicationsCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a publication object if a valid identifier was provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_publication1**
> PublicationsCreateResponseBody create_publication1(customer, join_once=join_once, voucher=voucher, campaign=campaign, source_id=source_id, metadata=metadata)

Create Publication

This method selects vouchers that are suitable for publication, adds a publish entry and returns the publication. A voucher is suitable for publication when its active and hasnt been published yet.  ❗️ Limited access  Access to this endpoint is limited. This endpoint is designed for specific integrations and the API keys need to be configured to access this endpoint. Navigate to the **Dashboard** &rarr; **Project Settings** &rarr; **General** &rarr; **Integration Keys** to set up a pair of API keys and use them to send the request.    🚧 Clearly define the source of the voucher  You must clearly define which source you want to publish the voucher code from. It can either be a code from a campaign or a specific voucher identified by a code.    🚧 Publish multiple vouchers  This endpoint does not support the publishing of multiple vouchers from a single campaign. In case you want to publish multiple vouchers within a single publication, you need to use a dedicated endpoint.    📘 Auto-update campaign  In case you want to ensure the number of publishable codes increases automatically with the number of customers, you should use an **auto-update** campaign.   # Example Request      ❗️ Required    Query param voucher OR campaign MUST be filled out. If you provide both, campaign param will be skipped.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.create_publication_campaign import CreatePublicationCampaign
from voucherify.models.customer import Customer
from voucherify.models.publications_create_response_body import PublicationsCreateResponseBody
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
    api_instance = voucherify.PublicationsApi(api_client)
    customer = voucherify.Customer() # Customer | Contains information about the customer to whom the publication was directed.
    join_once = True # bool | Through this flag, you can control if a particular person gets only one and always the same code even if the app sends multiple publication requests. It means that if you have a referral program, a referrer is assigned only to one code if an integration sends publication requests more than once for the same customer. (optional)
    voucher = 'voucher_example' # str | Code of voucher being published. (optional)
    campaign = voucherify.CreatePublicationCampaign() # CreatePublicationCampaign | Create publication with campaign. (optional)
    source_id = 'source_id_example' # str | The merchants publication ID if it is different from the Voucherify publication ID. Its an optional tracking identifier of a publication. It is really useful in case of an integration between multiple systems. It can be a publication ID from a CRM system, database or 3rd-party service. If source_id is provided only 1 voucher can be published per request. (optional)
    metadata = None # object | The metadata object stores all custom attributes assigned to the publication. A set of key/value pairs that you can attach to a publication object. It can be useful for storing additional information about the publication in a structured format. (optional)

    try:
        # Create Publication
        api_response = api_instance.create_publication1(customer, join_once=join_once, voucher=voucher, campaign=campaign, source_id=source_id, metadata=metadata)
        print("The response of PublicationsApi->create_publication1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicationsApi->create_publication1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer** | [**Customer**](.md)| Contains information about the customer to whom the publication was directed. | 
 **join_once** | **bool**| Through this flag, you can control if a particular person gets only one and always the same code even if the app sends multiple publication requests. It means that if you have a referral program, a referrer is assigned only to one code if an integration sends publication requests more than once for the same customer. | [optional] 
 **voucher** | **str**| Code of voucher being published. | [optional] 
 **campaign** | [**CreatePublicationCampaign**](.md)| Create publication with campaign. | [optional] 
 **source_id** | **str**| The merchants publication ID if it is different from the Voucherify publication ID. Its an optional tracking identifier of a publication. It is really useful in case of an integration between multiple systems. It can be a publication ID from a CRM system, database or 3rd-party service. If source_id is provided only 1 voucher can be published per request. | [optional] 
 **metadata** | [**object**](.md)| The metadata object stores all custom attributes assigned to the publication. A set of key/value pairs that you can attach to a publication object. It can be useful for storing additional information about the publication in a structured format. | [optional] 

### Return type

[**PublicationsCreateResponseBody**](PublicationsCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a publication object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_publications**
> PublicationsListResponseBody list_publications(limit=limit, page=page, order=order, campaign=campaign, customer=customer, voucher=voucher, result=result, voucher_type=voucher_type, is_referral_code=is_referral_code, filters=filters, source_id=source_id)

List Publications

Retrieve a list of publications. To return a **particular** publication, you can use the source_id query parameter and provide the source_id of the publication you are looking for specifically. # Pagination  🚧 Important!  If you want to scroll through a huge set of records, it is recommended to use the Exports API. This API will return an error page_over_limit if you reach a page above 1000. # Filter Query The filters query parameter allows for joining multiple parameters with logical operators. The syntax looks as follows:  ## Operators:  ## Examples  

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.parameter_filters_list_publications import ParameterFiltersListPublications
from voucherify.models.parameter_order_list_publications import ParameterOrderListPublications
from voucherify.models.parameter_result_list_publications import ParameterResultListPublications
from voucherify.models.parameter_voucher_type_list_publications import ParameterVoucherTypeListPublications
from voucherify.models.publications_list_response_body import PublicationsListResponseBody
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
    api_instance = voucherify.PublicationsApi(api_client)
    limit = 56 # int | Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. (optional)
    page = 56 # int | Which page of results to return. The lowest value is 1. (optional)
    order = voucherify.ParameterOrderListPublications() # ParameterOrderListPublications | Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. (optional)
    campaign = 'campaign_example' # str | Filters by a given campaign name. (optional)
    customer = 'customer_example' # str | Filters by a unique customer ID. (optional)
    voucher = 'voucher_example' # str | Filters by a given voucher code. (optional)
    result = voucherify.ParameterResultListPublications() # ParameterResultListPublications | Filters by a publication result. (optional)
    voucher_type = voucherify.ParameterVoucherTypeListPublications() # ParameterVoucherTypeListPublications | Filters by a voucher type. (optional)
    is_referral_code = True # bool | This filter works only for the true option. If set to true, the query returns only publications of codes from referral campaigns.  (optional)
    filters = voucherify.ParameterFiltersListPublications() # ParameterFiltersListPublications | Filter conditions. (optional)
    source_id = 'source_id_example' # str | Using this endpoint with a particular publication source_id, which was sent with the original request to create a publication, returns in the response, exactly the same code published initially because the code was assigned to the given publication. As a result, you can use this endpoint as a reference and return a code that was assigned in a publication by using a particular source_id. (optional)

    try:
        # List Publications
        api_response = api_instance.list_publications(limit=limit, page=page, order=order, campaign=campaign, customer=customer, voucher=voucher, result=result, voucher_type=voucher_type, is_referral_code=is_referral_code, filters=filters, source_id=source_id)
        print("The response of PublicationsApi->list_publications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicationsApi->list_publications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. | [optional] 
 **page** | **int**| Which page of results to return. The lowest value is 1. | [optional] 
 **order** | [**ParameterOrderListPublications**](.md)| Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. | [optional] 
 **campaign** | **str**| Filters by a given campaign name. | [optional] 
 **customer** | **str**| Filters by a unique customer ID. | [optional] 
 **voucher** | **str**| Filters by a given voucher code. | [optional] 
 **result** | [**ParameterResultListPublications**](.md)| Filters by a publication result. | [optional] 
 **voucher_type** | [**ParameterVoucherTypeListPublications**](.md)| Filters by a voucher type. | [optional] 
 **is_referral_code** | **bool**| This filter works only for the true option. If set to true, the query returns only publications of codes from referral campaigns.  | [optional] 
 **filters** | [**ParameterFiltersListPublications**](.md)| Filter conditions. | [optional] 
 **source_id** | **str**| Using this endpoint with a particular publication source_id, which was sent with the original request to create a publication, returns in the response, exactly the same code published initially because the code was assigned to the given publication. As a result, you can use this endpoint as a reference and return a code that was assigned in a publication by using a particular source_id. | [optional] 

### Return type

[**PublicationsListResponseBody**](PublicationsListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a list of publications you&#39;ve previously created with &lt;!-- [create publication](OpenAPI.json/paths/~1publications/post) --&gt;[create publication](ref:create-publication) or implicitly by the distribution manager. The publications are returned in sorted order, with the most recent ones appearing first. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

