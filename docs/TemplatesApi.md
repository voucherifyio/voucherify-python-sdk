# voucherify.TemplatesApi

All URIs are relative to *https://api.voucherify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_tier_from_template**](TemplatesApi.md#add_tier_from_template) | **POST** /v1/templates/campaigns/{campaignTemplateId}/tier-setup | Add Promotion Tier From Template
[**create_campaign_from_template**](TemplatesApi.md#create_campaign_from_template) | **POST** /v1/templates/campaigns/{campaignTemplateId}/campaign-setup | Create Campaign From Template
[**create_campaign_template**](TemplatesApi.md#create_campaign_template) | **POST** /v1/templates/campaigns | Create Campaign Template
[**delete_campaign_template**](TemplatesApi.md#delete_campaign_template) | **DELETE** /v1/templates/campaigns/{campaignTemplateId} | Delete Campaign Template
[**get_campaign_template**](TemplatesApi.md#get_campaign_template) | **GET** /v1/templates/campaigns/{campaignTemplateId} | Get Campaign Template
[**list_campaign_templates**](TemplatesApi.md#list_campaign_templates) | **GET** /v1/templates/campaigns | List Campaign Templates
[**update_campaign_template**](TemplatesApi.md#update_campaign_template) | **PUT** /v1/templates/campaigns/{campaignTemplateId} | Update Campaign Template


# **add_tier_from_template**
> TemplatesCampaignsTierSetupCreateResponseBody add_tier_from_template(campaign_template_id, templates_campaigns_tier_setup_create_request_body=templates_campaigns_tier_setup_create_request_body)

Add Promotion Tier From Template

Creates a promotion tier out of a discount campaign template and adds it to an existing promotion campaign. To add a promotion tier to a campaign, you need to provide the name in the request and the campaign ID. Other fields are optional. If no other fields are sent, the configuration from the template will be used. You can send new values of the fields listed below to replace the settings saved in the template. However, you cannot assign an action or an existing validation rule or create a new one in the request. If the template has a validation rule, a new validation rule is always created for the promotion tier. When the promotion tier has been created, then you can: - Update the validation rule, - Unassign the validation rule, - Assign an existing validation rule.  👍 Promotion Tiers and Campaign Templates You can create a campaign template out of a promotion tier. Promotion tiers are converted to a discount campaign with the DISCOUNT_COUPON type. You can use this template to create: - Discount campaign - Promotion tier  📘 Campaign Templates – Documentation Read the [Campaign Templates documentation](https://support.voucherify.io/article/620-campaign-templates) to learn more about this feature.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.templates_campaigns_tier_setup_create_request_body import TemplatesCampaignsTierSetupCreateRequestBody
from voucherify.models.templates_campaigns_tier_setup_create_response_body import TemplatesCampaignsTierSetupCreateResponseBody
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
    api_instance = voucherify.TemplatesApi(api_client)
    campaign_template_id = 'campaign_template_id_example' # str | Pass the campaign template ID that was assigned by Voucherify.
    templates_campaigns_tier_setup_create_request_body = voucherify.TemplatesCampaignsTierSetupCreateRequestBody() # TemplatesCampaignsTierSetupCreateRequestBody | Only name and campaign_id are required. The rest of the fields will overwrite the template configuration. (optional)

    try:
        # Add Promotion Tier From Template
        api_response = api_instance.add_tier_from_template(campaign_template_id, templates_campaigns_tier_setup_create_request_body=templates_campaigns_tier_setup_create_request_body)
        print("The response of TemplatesApi->add_tier_from_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->add_tier_from_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_template_id** | **str**| Pass the campaign template ID that was assigned by Voucherify. | 
 **templates_campaigns_tier_setup_create_request_body** | [**TemplatesCampaignsTierSetupCreateRequestBody**](TemplatesCampaignsTierSetupCreateRequestBody.md)| Only name and campaign_id are required. The rest of the fields will overwrite the template configuration. | [optional] 

### Return type

[**TemplatesCampaignsTierSetupCreateResponseBody**](TemplatesCampaignsTierSetupCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the details about the added promotion tier and about the resources that have been created out of the template and added to the project. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_campaign_from_template**
> TemplatesCampaignsCampaignSetupCreateResponseBody create_campaign_from_template(campaign_template_id, templates_campaigns_campaign_setup_create_request_body=templates_campaigns_campaign_setup_create_request_body)

Create Campaign From Template

Creates a campaign out of a campaign template. To create a campaign, you need to provide the name in the request, while other fields are optional. If no other fields are sent, the configuration from the template will be used. You can send new values of the fields listed below to replace the settings saved in the template. However, you cannot assign an existing validation rule or create a new one in the request. If the template has a validation rule, a new validation rule is always created for the campaign. When the campaign has been created, then you can: - Update the validation rule, - Unassign the validation rule, - Assign an existing validation rule.  👍 Promotion Tiers and Campaign Templates You can create a campaign template out of a promotion tier. Promotion tiers are converted to a discount campaign with the DISCOUNT_COUPON type. You can use this template to create: - Discount campaign - Promotion tier  📘 Campaign Templates – Documentation Read the [Campaign Templates documentation](https://support.voucherify.io/article/620-campaign-templates) to learn more about this feature.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.templates_campaigns_campaign_setup_create_request_body import TemplatesCampaignsCampaignSetupCreateRequestBody
from voucherify.models.templates_campaigns_campaign_setup_create_response_body import TemplatesCampaignsCampaignSetupCreateResponseBody
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
    api_instance = voucherify.TemplatesApi(api_client)
    campaign_template_id = 'campaign_template_id_example' # str | Pass the campaign template ID that was assigned by Voucherify.
    templates_campaigns_campaign_setup_create_request_body = {"name":"Campaign-out-of-template","description":"Created out of a template","auto_join":true,"join_once":true} # TemplatesCampaignsCampaignSetupCreateRequestBody | Only name is required. The rest of the fields will overwrite the template configuration. (optional)

    try:
        # Create Campaign From Template
        api_response = api_instance.create_campaign_from_template(campaign_template_id, templates_campaigns_campaign_setup_create_request_body=templates_campaigns_campaign_setup_create_request_body)
        print("The response of TemplatesApi->create_campaign_from_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->create_campaign_from_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_template_id** | **str**| Pass the campaign template ID that was assigned by Voucherify. | 
 **templates_campaigns_campaign_setup_create_request_body** | [**TemplatesCampaignsCampaignSetupCreateRequestBody**](TemplatesCampaignsCampaignSetupCreateRequestBody.md)| Only name is required. The rest of the fields will overwrite the template configuration. | [optional] 

### Return type

[**TemplatesCampaignsCampaignSetupCreateResponseBody**](TemplatesCampaignsCampaignSetupCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the details about the created campaign and about the resources that have been created out of the template and added to the project. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_campaign_template**
> TemplatesCampaignsCreateTemplateResponseBody create_campaign_template(templates_campaigns_create_request_body=templates_campaigns_create_request_body)

Create Campaign Template

Creates a template for a discount or gift campaign, or a promotion tier. A template stores campaign configuration **without** the following details: - Campaign name - Category - Code count The following elements are not supported by campaign templates: - Redeeming API keys - Redeeming users - Customer loyalty tier - Static segments  👍 Promotion Tiers and Campaign Templates You can create a campaign template out of a promotion tier. Promotion tiers are converted to a discount campaign with the DISCOUNT_COUPON type. You can use this template to create: - Discount campaign, - Promotion tier.  📘 Campaign Templates – Documentation Read the [Campaign Templates documentation](https://support.voucherify.io/article/620-campaign-templates) to learn more about this feature.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.templates_campaigns_create_request_body import TemplatesCampaignsCreateRequestBody
from voucherify.models.templates_campaigns_create_template_response_body import TemplatesCampaignsCreateTemplateResponseBody
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
    api_instance = voucherify.TemplatesApi(api_client)
    templates_campaigns_create_request_body = voucherify.TemplatesCampaignsCreateRequestBody() # TemplatesCampaignsCreateRequestBody | Provide details for a campaign template (optional)

    try:
        # Create Campaign Template
        api_response = api_instance.create_campaign_template(templates_campaigns_create_request_body=templates_campaigns_create_request_body)
        print("The response of TemplatesApi->create_campaign_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->create_campaign_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **templates_campaigns_create_request_body** | [**TemplatesCampaignsCreateRequestBody**](TemplatesCampaignsCreateRequestBody.md)| Provide details for a campaign template | [optional] 

### Return type

[**TemplatesCampaignsCreateTemplateResponseBody**](TemplatesCampaignsCreateTemplateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the details of a created campaign template. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_campaign_template**
> delete_campaign_template(campaign_template_id)

Delete Campaign Template

Deletes the campaign template permanently.  📘 Campaign Templates – Documentation Read the [Campaign Templates documentation](https://support.voucherify.io/article/620-campaign-templates) to learn more about this feature.

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
    api_instance = voucherify.TemplatesApi(api_client)
    campaign_template_id = 'campaign_template_id_example' # str | Pass the campaign template ID that was assigned by Voucherify.

    try:
        # Delete Campaign Template
        api_instance.delete_campaign_template(campaign_template_id)
    except Exception as e:
        print("Exception when calling TemplatesApi->delete_campaign_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_template_id** | **str**| Pass the campaign template ID that was assigned by Voucherify. | 

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

# **get_campaign_template**
> TemplatesCampaignsGetResponseBody get_campaign_template(campaign_template_id)

Get Campaign Template

Retrieves a campaign template available in the project.  📘 Campaign Templates – Documentation Read the [Campaign Templates documentation](https://support.voucherify.io/article/620-campaign-templates) to learn more about this feature.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.templates_campaigns_get_response_body import TemplatesCampaignsGetResponseBody
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
    api_instance = voucherify.TemplatesApi(api_client)
    campaign_template_id = 'campaign_template_id_example' # str | Pass the campaign template ID that was assigned by Voucherify.

    try:
        # Get Campaign Template
        api_response = api_instance.get_campaign_template(campaign_template_id)
        print("The response of TemplatesApi->get_campaign_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->get_campaign_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_template_id** | **str**| Pass the campaign template ID that was assigned by Voucherify. | 

### Return type

[**TemplatesCampaignsGetResponseBody**](TemplatesCampaignsGetResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the details about a campaign template. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_campaign_templates**
> TemplatesCampaignsListResponseBody list_campaign_templates(limit=limit, starting_after_id=starting_after_id, order=order, include_total=include_total, filters=filters)

List Campaign Templates

Lists all campaign templates available in the project.  📘 Campaign Templates – Documentation Read the [Campaign Templates documentation](https://support.voucherify.io/article/620-campaign-templates) to learn more about this feature.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.parameter_filters_list_templates import ParameterFiltersListTemplates
from voucherify.models.parameter_templates_list import ParameterTemplatesList
from voucherify.models.templates_campaigns_list_response_body import TemplatesCampaignsListResponseBody
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
    api_instance = voucherify.TemplatesApi(api_client)
    limit = 56 # int | Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. (optional)
    starting_after_id = 'starting_after_id_example' # str | A cursor for pagination. It retrieves the campaign templates created after a template with the given ID. (optional)
    order = voucherify.ParameterTemplatesList() # ParameterTemplatesList | Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. (optional)
    include_total = True # bool | If set to true, the response returns the number of all campaign templates, regardless of the applied filters or limits. Set to false by default. (optional)
    filters = voucherify.ParameterFiltersListTemplates() # ParameterFiltersListTemplates | Filters for listing templates. (optional)

    try:
        # List Campaign Templates
        api_response = api_instance.list_campaign_templates(limit=limit, starting_after_id=starting_after_id, order=order, include_total=include_total, filters=filters)
        print("The response of TemplatesApi->list_campaign_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->list_campaign_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. | [optional] 
 **starting_after_id** | **str**| A cursor for pagination. It retrieves the campaign templates created after a template with the given ID. | [optional] 
 **order** | [**ParameterTemplatesList**](.md)| Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. | [optional] 
 **include_total** | **bool**| If set to true, the response returns the number of all campaign templates, regardless of the applied filters or limits. Set to false by default. | [optional] 
 **filters** | [**ParameterFiltersListTemplates**](.md)| Filters for listing templates. | [optional] 

### Return type

[**TemplatesCampaignsListResponseBody**](TemplatesCampaignsListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a dictionary of campaign template objects. The templates are returned by creation date by default. The most recent objects appear last unless specified otherwise with the &#x60;order&#x60; parameter. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_template**
> TemplatesCampaignsUpdateResponseBody update_campaign_template(campaign_template_id, templates_campaigns_update_request_body=templates_campaigns_update_request_body)

Update Campaign Template

Updates the name or description of the campaign template.  📘 Campaign Templates – Documentation Read the [Campaign Templates documentation](https://support.voucherify.io/article/620-campaign-templates) to learn more about this feature.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.templates_campaigns_update_request_body import TemplatesCampaignsUpdateRequestBody
from voucherify.models.templates_campaigns_update_response_body import TemplatesCampaignsUpdateResponseBody
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
    api_instance = voucherify.TemplatesApi(api_client)
    campaign_template_id = 'campaign_template_id_example' # str | Pass the campaign template ID that was assigned by Voucherify.
    templates_campaigns_update_request_body = voucherify.TemplatesCampaignsUpdateRequestBody() # TemplatesCampaignsUpdateRequestBody | Provide the new name or description for the campaign template (optional)

    try:
        # Update Campaign Template
        api_response = api_instance.update_campaign_template(campaign_template_id, templates_campaigns_update_request_body=templates_campaigns_update_request_body)
        print("The response of TemplatesApi->update_campaign_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->update_campaign_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_template_id** | **str**| Pass the campaign template ID that was assigned by Voucherify. | 
 **templates_campaigns_update_request_body** | [**TemplatesCampaignsUpdateRequestBody**](TemplatesCampaignsUpdateRequestBody.md)| Provide the new name or description for the campaign template | [optional] 

### Return type

[**TemplatesCampaignsUpdateResponseBody**](TemplatesCampaignsUpdateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the details of an updated campaign template. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

